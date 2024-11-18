# **Dynamic Interview Process Management System**

This project provides a **dynamic interview process** that generates interview questions based on the **analysis of a candidate's CV and the job posting**. It collects responses, detects off-topic answers, and dynamically adjusts the interview flow. All responses are stored, and the history is used to create new questions.

---

## **Table of Contents**

1. [Installation](#installation)  
2. [File Structure](#file-structure)  
3. [Usage](#usage)  
4. [Functions and Tasks](#functions-and-tasks)  
5. [Agent and Task Descriptions](#agent-and-task-descriptions)  
6. [Workflow](#workflow)  
 

---

## **Installation**

1. **Install the required libraries**:
   ```bash
   pip install crewai langchain_groq python-dotenv

2. **Set environment variables**:
   Add the following line to your **.env** file:
`GROQ_API_KEY=your_api_key_here`

- **Install Dependencies**: Run `pip install -r requirements.txt`
    

---


## **Usage**
1. **Run the application**: Run `python z_main.py` to start the application.
2. **Commands**:
- End the interview: `exit` or `quit`
- If the answer is off-topic: A **warning** is displayed, and the user is asked to try again.


---


## **Functions and Tasks**
1. **`analyze_cv_and_job()`**
Analyzes the candidate’s CV and the job posting, and saves the results to **history.txt**.
**Task Used**: `writer_task()` 
2. **`generate_and_ask_question()`**
* Generates dynamic questions based on past responses and collects answers from the user.
* If "Thank you again for your time today." is in the created question, then terminate the program.
**Task Used**: `question_generator_task()`


---

## Agent and Task Descriptions
### Agents
1. **Reader Agent**:
- Role: Analyzes the CV and job posting.
- Associated Task: writer_task
2. **Question Generator Agent**:
- Role: Generates relevant questions based on previous responses.
- Associated Task: question_generator_task


### Tasks
1. **Writer Task**:
- Description: Analyzes the candidate’s CV and job posting to evaluate compatibility.
2. **Question Generator Task**:
- Description: This task is designed to manage and guide the interview process, simulating an interviewer’s role in a professional job interview. The question_generator_task uses conversation history and recent candidate responses to naturally progress the interview and assess four specific skills:
   * **Professional Competence**
    **Analytical Skills**
    **Problem-solving Skills**
    **Communication Skills**
- The Interview Process follows these steps:
  - **Identify Missing Skills:** Review the candidate’s answers in the "Conversation History" to determine which skills have not yet been assessed, ensuring comprehensive coverage.
  - **Question Progression:** The task generates questions based on the most recent response, guiding the conversation smoothly and prioritizing skills that haven’t been evaluated. If the candidate’s response is off-topic, a polite reminder is issued to refocus the conversation.
  - **Concluding the Interview:** Once all skills are assessed, the interview concludes with a professional closing message, ensuring a structured and respectful ending. The other condition is to terminate the program if candidate requests and approves it.


---

## Workflow
1. **Clear The Memory**
2. **CV and Job Posting Analysis**:
Loads and analyzes the candidate’s CV and job posting. Logs the result in history.txt.
3. **Dynamic Question Generation**:
Generates new questions based on the candidate’s history and previous answers.
4. **Interview Termination**:
Check the termination conditions and terminate the program id there is any.

