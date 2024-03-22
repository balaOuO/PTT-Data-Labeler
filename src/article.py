import requests
from bs4 import BeautifulSoup
from config import BASE_URL , HEADER_18
from src.comment import Comment
from datetime import datetime

class Article:

    def __init__(self , article_url : str) -> None:
        self.url : str = BASE_URL + article_url
        self._main_area : BeautifulSoup
        self.content : str
        self.comment : list[Comment] = []
        self.author : str
        self.title : str
        self.board : str
        self.date_time : datetime
        self.Refresh()


    def Refresh(self):
        article_data = requests.get(url=self.url , headers=HEADER_18)
        self._main_area = BeautifulSoup(article_data.text , "html.parser").select_one("div#main-content")
        self._crawlInformation()
        self._crawlContent()
        self._crawlComment()
        self._mergeComment()

    def _crawlInformation(self):
        info = self._main_area.select("span.article-meta-value")

        self.author = info[0].text.split(" ")[0]
        self.board = info[1].text
        self.title = info[2].text
        self.date_time = datetime.strptime(info[3].text , "%c") # Sat Dec 24 20:03:52 2005


    def _crawlContent(self):
        main_area = self._main_area.__copy__()
        for child in main_area.find_all():
            child.decompose()
        self.content = main_area.text

    def _crawlComment(self):
        comment_area = self._main_area.select("div.push")
        self.comment : list[Comment] = []
        for comment in comment_area:
            try:
                tag = comment.select_one("span.push-tag")
                author = comment.select_one("span.push-userid")
                content = comment.select_one("span.push-content")
                ip_datetime = comment.select_one("span.push-ipdatetime")
                self.comment.append(
                    Comment(
                        tag=tag.text,
                        author=author.text,
                        content=content.text,
                        _sourse_year=self.date_time.year,
                        _ip_datetime=ip_datetime.text
                        )
                    )
            except Exception as e:
                print(f"Catch error : {e}")
                print(f"Reason : {comment}")
            
    def _mergeComment(self) -> None:
        i = 0
        while(i < len(self.comment)):
            self._merge(index = i , offset = 1)
            i += 1

    def _merge(self , index : int , offset : int) -> None:
        if (index + offset >= len(self.comment)):
            return
        
        if (offset > 3):
            return
        
        if (self.comment[index].author == self.comment[index + offset].author):
            self._merge(index = index + offset , offset = 1)
            self.comment[index].content += " " + self.comment[index + offset].content
            self.comment.pop(index + offset)
        else:
            self._merge(index = index , offset = offset + 1)

    def ParseDict(self) -> dict:
        return {
            "url" : self.url,
            "content" : self.content,
            "author" : self.author,
            "title" : self.title,
            "board" : self.board,
            "time" : str(self.date_time),
            "comments" : [
                {
                    "tag" : comment.tag,
                    "author" : comment.author,
                    "content" : comment.content,
                    "ip" : comment.ip,
                    "time" : str(comment.date_time)
                } for comment in self.comment
            ]
        }