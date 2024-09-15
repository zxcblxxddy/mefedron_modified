import requests
from bs4 import BeautifulSoup

def crawl(url):
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        headers = []
        for header_tag in ['h1', 'h2', 'h3']:
            for header in soup.find_all(header_tag):
                headers.append((header_tag, header.text.strip()))
        
        return headers
    else:
        print(f"Не удалось получить доступ к {url}")
        return None

if __name__ == "__main__":
    url = input("Введите URL для краулинга: ")
    headers = crawl(url)
    
    if headers:
        print("Найденные заголовки:")
        for tag, text in headers:
            print(f"{tag.upper()}: {text}")