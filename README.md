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

---
## Web Outputs
1. **Main Page**
![Main Page](https://github.com/aliemreeser/Interview-Agent-with-crewAI/blob/main/Screenshot%202024-11-20%20at%2018.45.16.png)
2. **Questions&Answers**
   ![Q&A](https://github.com/aliemreeser/Interview-Agent-with-crewAI/blob/main/Screenshot%202024-11-20%20at%2018.35.45.png)

# Interview Process Analysis and Sample Conversations

## Analysis
The CV appears to demonstrate significant relevance to the job posting for a Data Scientist at InnovateTech Solutions. The candidate's educational background in Mathematics Engineering, with a focus on data science, machine learning, and AI, aligns with the job's requirements for a degree in a related field. The candidate's proficiency in programming languages such as Python and Java, as well as their experience with machine learning algorithms and data analysis, also match the job's requirements.

Furthermore, the candidate's projects showcase their skills in data science and machine learning, including image processing, classification problems, and predictive modeling. The candidate's experience with Convolutional Autoencoders, TensorFlow, and data visualization tools also aligns with the job's requirements for experience with machine learning algorithms and data visualization. Additionally, the candidate's experience with database management and programming languages such as Java, Python, and C++ demonstrate their technical skills.

The candidate's communication skills, as demonstrated through their ability to write a clear and concise CV, also suggest that they possess the excellent communication skills required for the job. Moreover, the candidate's eagerness to contribute to a dynamic team and add value to the company, as stated in their CV, aligns with the job's requirements for a team-oriented mindset.

However, the candidate's CV does not explicitly mention experience with big data technologies such as Hadoop or Spark, which is a requirement for the job. Additionally, the candidate's experience with A/B testing and experimental design, as well as their experience with cloud platforms such as AWS or Azure, is not mentioned in their CV, which are preferred qualifications for the job.

Overall, the candidate's CV demonstrates a strong foundation in data science and machine learning, and their skills and experience align with many of the job's requirements. However, the candidate may need to provide additional information or examples to demonstrate their experience with big data technologies, A/B testing, and cloud platforms.

---

## Sample Interview Conversations

### Analytical Skills
**Question:** Welcome to the interview for the Data Scientist position at InnovateTech Solutions. I must say that your CV is quite impressive, and I'm excited to learn more about your skills and experience. Before we begin, I'd like to briefly review your background to ensure that we cover all the necessary topics during our conversation.

As I reviewed your CV, I noticed that you have a strong foundation in data science and machine learning, but I'd like to dive deeper into some of the skills that are required for this position. Specifically, I'd like to start by assessing your Analytical Skills. Can you walk me through your process when approaching a complex data analysis problem, and how you ensure that you're asking the right questions to drive meaningful insights?

**Answer:** When I start a complex data analysis, I first define the goal—what we need to learn or solve. I then explore the data through patterns, outliers, and relationships, making sure it aligns with the goal. I ask questions like, “What key factors influence the outcome?” and “How can we use these findings?” Finally, I validate insights by cross-checking results with metrics or business objectives, ensuring they are accurate and actionable.

---

### Problem-Solving Skills
**Question:** That's a great approach to tackling complex data analysis problems. I appreciate how you emphasized the importance of aligning the analysis with the goal and ensuring that the findings are accurate and actionable. Now, I'd like to move on to assessing your Problem-Solving Skills. You mentioned that you validate insights by cross-checking results with metrics or business objectives. Can you walk me through a specific instance where you had to troubleshoot an issue with a machine learning model that wasn't producing the expected results, and how you went about resolving it?

**Answer:** In a project predicting loan defaults, the model's accuracy was low, and it seemed some features were causing issues. I used the VIF (Variance Inflation Factor) score to check for multicollinearity and found that some features were too closely related, confusing the model. I removed the features with high VIF scores, keeping only the most important ones. After this, I re-trained the model and saw a clear improvement in accuracy. This made the predictions more reliable, helping us identify high-risk cases better.

---

### Professional Competence
**Question:** I'd like to delve deeper into your experience with big data technologies, as it wasn't explicitly mentioned in your CV, but is a requirement for this position. You've demonstrated strong analytical and problem-solving skills, and I'm curious to know how you would handle working with large datasets. Can you walk me through your experience with data management and how you've handled situations where you've had to process and analyze large amounts of data?

**Answer:** I have no experience with big data technologies but plan to start learning them as soon as possible.

---

### Communication Skills
**Question:** To present complex results to non-technical stakeholders, how would you approach creating a presentation? Specifically, can you describe how you would structure your presentation, what visual aids you would use, and how you would ensure that your message is clear and concise?

**Answer:** To present complex results to non-technical stakeholders, I’d start with a simple overview of the project and its goals. Then, I’d use visual aids like charts and graphs to explain the main findings. For example, a line chart to show progress over time or a bar chart to compare results. I’d avoid technical terms and focus on what the results mean for the business. At the end, I’d highlight key takeaways and offer clear recommendations. This way, the presentation stays clear, focused, and easy to understand.

---

### Closing
**Question:** I think we've covered all the necessary topics in this interview. I'd like to thank you for your time today and for sharing your experiences with me. It was a pleasure speaking with you, and I appreciate your honesty and willingness to learn. Although we didn't have a chance to discuss some topics in more depth, I believe this conversation has provided a good overview of your skills and qualifications for the Data Scientist position at InnovateTech Solutions. Once again, thank you for your time today.

---

This document provides a summary of the interview process and highlights key interactions during the conversation. The detailed examples demonstrate how various skills are assessed during the interview.
