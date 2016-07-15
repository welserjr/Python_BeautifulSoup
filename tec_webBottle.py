import bottle
import urllib.request
from bs4 import BeautifulSoup
import json


@bottle.route('/')
def home_page():
    url = urllib.request.urlopen("http://www.tec.com.pe")
    html = BeautifulSoup(url)

    array_img = []
    array_data = []
    for item in html.body.find_all("article", "omc-blog-two omc-half-width-category"):
        div1 = item.find_all("div", "omc-resize-290 omc-blog")
        for i in div1:
            imagen = i.img['src']
            array_img.append(imagen)

        div2 = item.find_all("div", "omc-blog-two-text")
        for i in div2:
            titulo = i.h2.a.string
            link = i.h2.a['href']
            aut = i.p.em.string
            author = aut.replace("by ", "")
            a = {"titulo": titulo, "link": link, "author": author}
            array_data.append(a)

    aux = 0
    for item in array_data:
        item['imagen'] = array_img[aux]
        aux += 1

    data = json.dumps(array_data)
    return bottle.template(data)


bottle.debug(False)
bottle.run(host='0.0.0.0', port=2020)
