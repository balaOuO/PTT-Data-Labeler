import requests
from bs4 import BeautifulSoup
from config import BASE_URL , HEADER_18

class Artice:

    def __init__(self , artice_url : str) -> None:
        self.main_area = self._get_main_area(url = BASE_URL + artice_url)

    def _get_main_area(self , url) -> BeautifulSoup:
        artice_data = requests.get(url=url , headers=HEADER_18)
        artice_html = BeautifulSoup(artice_data.text , "html.parser")
        return artice_html.select_one("div#main-content")
    
    def GetContent(self) -> str:
        main_area = self.main_area.__copy__()
        for child in main_area.find_all():
            child.decompose()
        return main_area.text
    
    def GetMessages(self) -> list[str]:
        messages_area = self.main_area.select("div.push")
        return [message.text for message in messages_area]