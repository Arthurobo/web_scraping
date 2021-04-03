from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.google.com/').text

code = BeautifulSoup(source, 'lxml')

# print(code.prettify())

# Prettify to help format the html code
formatted_code = code.prettify()

# Writes scraped website to an existing file
f = open("existing.html", "w", encoding="utf-8")
f.write(formatted_code)
f.close()


# Creates a file and writes scraped website to file
_f = open("created.html","w+", encoding="utf-8")
_f = open("created.html", "w", encoding="utf-8")
_f.write(formatted_code)
_f.close()