import bottle
import urllib.request
from bs4 import BeautifulSoup
import json


@bottle.route('/')
def home_page():
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
    return bottle.template(data)


bottle.debug(False)
bottle.run(host='0.0.0.0', port=2020)
