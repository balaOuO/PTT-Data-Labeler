import requests
from bs4 import BeautifulSoup
from config import BASE_URL , HEADER_18
from src.comment import Comment

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
    
    def GetComment(self) -> list[Comment]:
        comment_area = self.main_area.select("div.push")
        comment_list : list[Comment] = []
        for comment in comment_area:
            tag = comment.select_one("span.push-tag")
            author = comment.select_one("span.push-userid")
            content = comment.select_one("span.push-content")
            ip_datetime = comment.select_one("span.push-ipdatetime")
            comment_list.append(Comment(tag=tag.text , author=author.text , content=content.text , ip_datetime=ip_datetime.text))
        return comment_list