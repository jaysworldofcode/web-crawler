from urllib.parse import urlparse

def get_hostname_from_url(url:str):
    parsed_uri = urlparse(url)
    
    return parsed_uri.netloc