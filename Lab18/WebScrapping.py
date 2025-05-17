from urllib.request import urlopen
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt


my_site='https://csumb.edu/admissions-aid/visit-campus/admitted-otter-days/'

site_html=urlopen(my_site)

soup = BeautifulSoup(site_html.read(), 'lxml')

images = soup.find_all('img')

for image in images:
  print(image['src'])
# Task 2 Image URL: https://pxl-csumbedu.terminalfour.net/fit-in/400x235/filters:format(webp)/filters:quality(75)/0x299:7517x4715/prod01/channel_2/media/csumb/phase-2a-site-launch/20241005_open_house_047.jpg

#Task 3
paragraphs = soup.find_all('p')
text = ' '.join(p.get_text() for p in paragraphs)

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

