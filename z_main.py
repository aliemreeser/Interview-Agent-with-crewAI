from z_crew import InterviewAgent
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings(action='ignore', module='.*paramiko.*')

# Load environment variables
load_dotenv()

# Initialize the interview agent
interview_agent = InterviewAgent()

# Define the history file path
HISTORY_FILE = "history.txt"

def clear_history():
    """Clear the contents of the history file."""
    with open(HISTORY_FILE, "w") as f:
        f.write("")  # Write an empty string to clear the file

def load_file(file_path):
    """Load content from a file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found.")
    with open(file_path, "r") as file:
        return file.read().strip()

def store_in_history(content):
    """Append content to the history file."""
    with open(HISTORY_FILE, "a") as f:
        f.write(content + "\n")

def load_history():
    """Load all content from the history file as a single text with line breaks between lines."""
    if not os.path.exists(HISTORY_FILE):
        return ""  # Return an empty string if history doesn't exist
    with open(HISTORY_FILE, "r") as f:
        return "\n".join(f.readlines())
    
def analyze_cv_and_job():
    """Analyze the CV and job posting, then store the result in history."""
    cv_content = load_file("/Users/alieser/Desktop/Çalışmalar/generion3/CV.txt")
    job_content = load_file("/Users/alieser/Desktop/Çalışmalar/generion3/JOB.txt")
    inputs = {
        "cv_content": cv_content,
        "job_content": job_content
    }
    
    crew = interview_agent.crew()
    crew.tasks = [interview_agent.writer_task()]
    analysis = crew.kickoff(inputs=inputs).tasks_output[0].raw.strip()
    print(f"Analysis: {analysis}")
    store_in_history(f"Analysis:\n{analysis}")

def generate_and_ask_question():
    """Generate a new question based on the history and get the user's answer."""
    history_content = load_history()
    user_response = None
    inputs = {"history_content": history_content, "user_response": user_response}
    
    # Set up the question generation task with the updated history
    crew = interview_agent.crew()
    crew.tasks = [interview_agent.question_generator_task()]
    
    question = crew.kickoff(inputs=inputs).tasks_output[0].raw.strip()
    
    # Save the generated question to history immediately
    store_in_history(f"QUESTION: {question}")
    
    print("\n")
    print("=><" * 25)
    print("\n")
    print(f"Interviewer: {question}")
    print("\n")
    
    # Check if the question includes the ending phrase
    if "Thank you again for your time today." in question:
        return False  # End the interview if the ending phrase is found
    
    # Get the user's answer
    while True:
        user_response = input("Candidate: ").strip()
        if user_response.lower() in ["exit", "quit"]:
            print("Interview Finished. Goodbye!")
            return False
        else:
            # Save the answer to history immediately
            store_in_history(f"ANSWER: {user_response}")
            break

    return True

def run():
    """Main function to run the interview process."""

    print("Clearing history...")
    print("\n")
    clear_history()  # Clear history at the start of each run


    print("Analyzing CV and Job Posting...")
    print("\n")
    analyze_cv_and_job()
    print("\n")
    print("=><"*25)
    print("\n")
    
    print("Starting the interview...")
    while generate_and_ask_question():
        continue

# Start the interview process
if __name__ == "__main__":
    run()