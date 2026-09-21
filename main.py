import re
import random
import statistics

from bs4 import BeautifulSoup

HTML_FILE = "python_class_question.html"

def extract_colours_from_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, "html.parser")
    colours = []
    for row in soup.find_all("tr")[1:]:
        cells = row.find_all("td")
        if len(cells) >= 2:
            text = cells[1].get_text(" ", strip=True)
            for colour in re.split(r",\s*", text):
                colour = colour.strip().upper()
                if colour == "BLEW":
                    colour = "BLUE"
                if colour:
                    colours.append(colour)
    return colours