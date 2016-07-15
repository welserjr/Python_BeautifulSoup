import urllib.request
import json
from bs4 import BeautifulSoup

url = urllib.request.urlopen("http://elcomercio.pe/movil")
html = BeautifulSoup(url)

posts = []
for a in html.body.find_all("article", "nota"):
    figure = a.figure
    titulo = figure.figcaption.h3.a.string
    link = figure.figcaption.h3.a['href']
    hora = figure.figcaption.span.string
    imagen = figure.a.img['data-src']

    aux = {"titulo": titulo, "link": link, "hora": hora, "imagen": imagen}
    posts.append(aux)
data = json.dumps(posts)
print(data)
