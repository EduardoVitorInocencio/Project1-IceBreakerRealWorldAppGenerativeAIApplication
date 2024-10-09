import os
import requests

from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = True):
    """
    Scrape information from LinkedIn profiles,
    Mannualy scrape the information from LinkedIn profile.
    
    """
    
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/EduardoVitorInocencio/7d64f82b4a5b48c1040fe65ac2b420b2/raw/22a6184f266f5ddbcef78992bb9fa41d9422301b/eduardo-inocencio.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=20,
        )
        
    else:
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        headers_dic = {'Authorization': f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=headers_dic,
            timeout=20,
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
    
    return data


if __name__ == '__main__':
    print(
        scrape_linkedin_profile(
            linkedin_profile_url='https://www.linkedin.com/in/eduardoinocencio/'
        )
    )
