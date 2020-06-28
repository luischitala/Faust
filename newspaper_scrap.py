import requests
import bs4

url = "https://www.semana.com/"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.text, 'html.parser')
news = soup.select('.article-h')

for item in news:
    print(f"Noticia:{item.text} | Link: {url}{'href'}")



#Aquí ya tengo una lista con todas las URL de los artículos de la web

