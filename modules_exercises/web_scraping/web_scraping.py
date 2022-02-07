import re

import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions/tagged/python"
response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

for tag in html.select(".question-summary"):
    question = tag.select_one(".question-hyperlink")
    relative_time = tag.select_one(".relativetime")
    votes = tag.select_one(".vote-count-post")
    views = tag.select_one(".views")
    cleaned_views = re.sub(r"[^0-9]", "", views.text)
    print(question.text)
    print(f"{cleaned_views} viram essa pergunta")
    print(f"Essa pergunta tem {votes.text} votos")
    print(relative_time.text)
