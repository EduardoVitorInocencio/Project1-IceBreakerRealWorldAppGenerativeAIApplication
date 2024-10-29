import os
import requests

from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn profiles,
    Mannualy scrape the information from LinkedIn profile.
    
    """
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/EduardoVitorInocencio/7d64f82b4a5b48c1040fe65ac2b420b2/raw/79ef40c72b2a50828971ef0d05ce95e035484ed8/eduardo-inocencio.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=30,
        )
        
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers_dic = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=headers_dic,
            timeout=30,
        )
    
    data = response.json()
    
    # REMOVER OS CONTEÚDOS/TOKENS QUE NÃO AGREGAM VALOR AO CONJUNTO DE DADOS
    # AQUI REMOVEMOS TODAS AS COLEÇÕES VAZIAS E OS TÓPICOS ["people_also_viewed","certifications"]
    # ONDE: K CORRESPONDE À CHAVE E V CORRESPONDE AO VALOR
    data = {
        k:v
        for k, v in data.items()
        if v not in ([],"","",None)
        and k not in ["people_also_viewed","certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
    
    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url='https://www.linkedin.com/in/eduardoinocencio/'
        )
    )
