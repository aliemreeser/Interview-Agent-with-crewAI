from crewai import Agent, Crew, Process, Task
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from crewai.project import CrewBase, agent, crew, task




# Çevresel değişkenleri yükle
load_dotenv()
# Groq API anahtarını al
api_key = os.getenv('GROQ_API_KEY')
# ChatGroq LLM oluşturma
llm = ChatGroq(
    api_key=api_key,  # Çevresel değişkenden gelen API anahtarı
    model="groq/llama-3.1-70b-versatile"
)


@CrewBase
class InterviewAgent:
    """InterviewAgent crew"""

    agents_config = "/Users/alieser/Desktop/Çalışmalar/generion3/z_config/z_agent.yaml"
    tasks_config = "/Users/alieser/Desktop/Çalışmalar/generion3/z_config/z_task.yaml"


    @agent
    def reader(self) -> Agent:
        return Agent(
            config=self.agents_config["reader"],
            llm=llm,
            verbose=False,
        )
    @agent
    def question_generator(self) ->Agent:
        return Agent(
            config=self.agents_config['question_generator'],
            llm=llm,
            verbose=False
        )
    
    @task
    def writer_task(self) -> Task:
        return Task(config=self.tasks_config["writer_task"],
                    agent=self.reader())
    @task
    def question_generator_task(self) ->Task:
        return Task(config=self.tasks_config['question_generator_task'],
                    agent=self.question_generator())
  
    @crew
    def crew(self) -> Crew:
        """creates the crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )