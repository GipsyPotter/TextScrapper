import requests
from bs4 import BeautifulSoup

import reportlab.rl_config

reportlab.rl_config.warnOnMissingFontGlyphs = 0

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))
my_canvas = canvas.Canvas("test.pdf", pagesize=A4)
my_canvas.setFont('Vera', 15)

URL = "https://docln.net/truyen/11898-daininki-idol-na-classmate-ni-natsukareta-isshou-hatarakitakunai-ore-isshou-hataraki-taku-nai-ore-ga-classmate-no-dainiki-idol-ni-natsukaretara/c105799-chuong-60-quyen-ra-lenh-6"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="chapter-content")
#print(results.prettify())
txt_elements = results.find_all("p")
all_txt = [txt.get_text() for txt in txt_elements]
for txt_element in txt_elements:
    print(txt_element.text)
# y = 750
# for txt in all_txt:
#     my_canvas.drawString(10, y, txt)
#     y -= 15
#     if y < 50:
#         my_canvas.showPage()
#         y = 750
# my_canvas.save()
