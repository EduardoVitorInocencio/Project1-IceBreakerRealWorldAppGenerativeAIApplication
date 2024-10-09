# CORE PACKAGES
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile


# ADDITIONAL PACKAGES
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key = os.getenv('OPENAI_KEY')


if __name__ == '__main__':
    print(os.getenv('OPENAI_KEY'))
    
    summary_template = """
    
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting fact about them
    """
      
    summary_prompt_template = PromptTemplate(input_variables =["information"], template = summary_template)
    
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo',openai_api_key=openai_api_key)
    # llm = ChatOllama(model='mistral')
    
    # Criar a cadeia LLM (PromptTemplate + ChatOpenAI)
    chain = prompt=summary_prompt_template | llm |StrOutputParser()
    
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eduardoinocencio/")
    
    # Executar a cadeia de prompts
    res = chain.invoke(input={"information": linkedin_data})
    
    print(res)