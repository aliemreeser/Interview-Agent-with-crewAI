from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from z_crew import InterviewAgent
import os

app = Flask(__name__)

# Configure file upload
UPLOAD_FOLDER = "data"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = {"txt"}

# Initialize the InterviewAgent
interview_agent = InterviewAgent()

# Define file paths
CV_FILE = os.path.join(UPLOAD_FOLDER, "CV.txt")
JOB_FILE = os.path.join(UPLOAD_FOLDER, "JOB.txt")
HISTORY_FILE = os.path.join(UPLOAD_FOLDER, "history.txt")

# Utility Functions
def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]

def clear_history():
    """Clear the contents of the history file."""
    with open(HISTORY_FILE, "w") as f:
        f.write("")  # Write an empty string to clear the file

def load_file(file_path):
    """Load content from a file."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r") as file:
        return file.read().strip()

def store_in_history(content):
    """Append content to the history file."""
    with open(HISTORY_FILE, "a") as f:
        f.write(content + "\n")

def load_history():
    """Load all content from the history file as a structured list of Q&A."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        lines = f.readlines()

    history = []
    current_entry = None
    for line in lines:
        if line.startswith("QUESTION:"):
            if current_entry:  # Save the previous entry
                history.append(current_entry)
            current_entry = {"question": line[len("QUESTION: "):].strip(), "answer": None}
        elif line.startswith("ANSWER:"):
            if current_entry:
                current_entry["answer"] = line[len("ANSWER: "):].strip()
    if current_entry:  # Save the last entry
        history.append(current_entry)
    return history

def analyze_cv_and_job():
    """Analyze the CV and job posting, then store the result in history."""
    cv_content = load_file(CV_FILE)
    job_content = load_file(JOB_FILE)
    inputs = {
        "cv_content": cv_content,
        "job_content": job_content
    }
    crew = interview_agent.crew()
    crew.tasks = [interview_agent.writer_task()]
    analysis = crew.kickoff(inputs=inputs).tasks_output[0].raw.strip()
    store_in_history(f"Analysis:\n{analysis}")
    return analysis

def generate_and_ask_question():
    """Generate a question based on the history and get the user's response."""
    history_content = load_history()
    inputs = {"history_content": history_content}
    
    # Set up the question generation task
    crew = interview_agent.crew()
    crew.tasks = [interview_agent.question_generator_task()]
    
    question = crew.kickoff(inputs=inputs).tasks_output[0].raw.strip()
    store_in_history(f"QUESTION: {question}")
    return question

# Flask Routes
@app.route("/", methods=["GET", "POST"])
def index():
    """Landing page with file upload."""
    if request.method == "POST":
        # Handle CV upload
        cv_file = request.files.get("cv_file")
        job_file = request.files.get("job_file")
        if cv_file and allowed_file(cv_file.filename):
            cv_file.save(os.path.join(app.config["UPLOAD_FOLDER"], "CV.txt"))
        else:
            return "Invalid CV file. Please upload a .txt file."

        if job_file and allowed_file(job_file.filename):
            job_file.save(os.path.join(app.config["UPLOAD_FOLDER"], "JOB.txt"))
        else:
            return "Invalid Job file. Please upload a .txt file."

        # Redirect to the interview page
        return redirect(url_for("interview"))
    return render_template("index.html")

@app.route('/interview', methods=['GET', 'POST'])
def interview():
    """Interview page."""
    if request.method == 'POST':
        user_response = request.form['user_response'].strip()
        if user_response.lower() in ["exit", "quit"]:
            clear_history()  # History temizleniyor
            return redirect(url_for('index'))  # Ana sayfaya yönlendiriliyor
        else:
            # Kullanıcı cevabı kaydediliyor
            store_in_history(f"ANSWER: {user_response}")

            # Sonraki soru üretiliyor
            question = generate_and_ask_question()
            
            # Bitiş koşulu kontrol ediliyor
            if "Thank you again for your time today." in question:
                clear_history()  # History temizleniyor
                return redirect(url_for('index'))  # Ana sayfaya yönlendiriliyor
            
            return render_template("interview.html", question=question, history=load_history())
    
    # İlk ayarlar: history temizleniyor, analiz yapılıyor ve ilk soru oluşturuluyor
    clear_history()
    analyze_cv_and_job()
    question = generate_and_ask_question()
    return render_template("interview.html", question=question, history=load_history())
    
    # Initial setup: clear history, analyze, and generate the first question
    clear_history()
    analysis = analyze_cv_and_job()
    question = generate_and_ask_question()
    return render_template("interview.html", question=question, history=load_history())

if __name__ == "__main__":
    app.run(debug=True)