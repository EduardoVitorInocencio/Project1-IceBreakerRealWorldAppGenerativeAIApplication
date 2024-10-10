import os
import sys

# Adiciona o diretório principal ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Especificar o caminho completo para o arquivo .env
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))


from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool # Permite os agentes a conectar com elementos do mundo exterior
from langchain.agents import (create_react_agent, AgentExecutor)
from langchain import hub

from tools.tools import get_profile_url_tavily

load_dotenv(dotenv_path='..env')
OPENAI_API_KEY = os.getenv("OPENAI_KEY")

print(OPENAI_API_KEY)
# FUNCTIONS

def lookup(name:str) -> str:
    llm = ChatOpenAI(
        temperature=0, 
        model="gpt-4o-mini",
        openai_api_key = OPENAI_API_KEY
    )
    
    template ="""given the full name {name_of_person} I want you to get it me a link to their LinkedIn profile page.
    Your Answer should contain only URL"""
    
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="useful for when you need the LinkeDin Page URL",
        )
    ]
    
    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agent, verbose=True)
    
    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )
    
    
    linkedin_profile_url = result["output"]
    return linkedin_profile_url
    
if __name__=='__main__':
    linkedin_url = lookup(name='Eduardo Inocencio')