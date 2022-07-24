import requests
from bs4 import BeautifulSoup
import os
from time import time
import string

def scrape_script(movie_title, print_error=False):
    try:
        website_url = requests.get("https://www.imsdb.com/scripts/" + movie_title + ".html").text
        soup = BeautifulSoup(website_url, "html.parser")
        #Ctrl+U 시작~끝 태그 확인
        if soup.pre.find_all("pre"):
            script = ""
            for i in soup.pre.find_all("pre"):
                script += str(i)
                print(script)
        else:
            script = str(soup.pre)
            print(script)
    except Exception as e:
        if print_error:
            print(e)
            print(movie_title + ":is not available")
    else:
        if len(script) < 3000:
            if print_error:
                print(movie_title + ":is not available")
        else:
            if "\n" in script:
                script = script.replace("<pre>", "").replace("<b>", "")
                script = script.replace("</b>", "").replace("<u>", "").replace("</u>", "")
                if "/" in movie_title:
                    pass
                else:
                    with open(os.getcwd() + "/scripts/" + movie_title + "_script.txt", "w", encoding="UTF-8") as s:
                        s.write(script)

movie_title = 'movie_title'
scrape_script(movie_title)
