# CORE PACKAGES
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as likedin_lookup_agent
from output_parsers import summary_parser, Summary

# ADDITIONAL PACKAGES
import os
from dotenv import load_dotenv
from typing import Tuple

load_dotenv()
openai_api_key = os.getenv('OPENAI_KEY')

def ice_breaker_with(name:str) -> Tuple[Summary,str]:
    linkedin_username = likedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username,mock=True)
    
    summary_template = """
    
        given the LinkedIn information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting fact about them
        
        Use both information from LinkedIn
        \n{format_instructions}
    """
      
    summary_prompt_template = PromptTemplate(
        input_variables =["information"], template = summary_template,
        partial_variables = {"format_instructions":summary_parser.get_format_instructions()}
    )
    
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo',openai_api_key=openai_api_key)
    
    # Criar a cadeia LLM (PromptTemplate + ChatOpenAI)
    chain = summary_prompt_template | llm | summary_parser
    
    # linkedin_data = scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/eduardoinocencio/")
    
    # Executar a cadeia de prompts
    res:Summary = chain.invoke(input={"information": linkedin_data})
    
    return res, linkedin_data.get("profile_pic_url")



if __name__ == '__main__':
    
    ice_breaker_with(name='Harrison Chase')
          