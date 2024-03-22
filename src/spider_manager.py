from src.json_manager import JsonManager
from src.article import Article
from src.database_manager import DatabaseManeger
from config import BASE_URL , HEADER_18

import requests
from bs4 import BeautifulSoup


class SpiderManager:
    def __init__(self) -> None:
        self.board : str
        self.new_board : str
        self.index : int
        self.article_url_list : list = []
        self.database_manager : DatabaseManeger = DatabaseManeger()
        self._loadArticleList()

    def __del__(self) -> None:
        self._saveArticleList()

    def _saveArticleList(self) -> None:
        article_list_dict = {
            "board" : self.board,
            "index" : self.index,
            "article_url_list" : self.article_url_list
        }
        JsonManager.SaveArticeList(article_list_dict)

    def _loadArticleList(self) -> None:
        article_list_dict : dict = JsonManager.LoadArticleList()
        self.article_url_list = article_list_dict["article_url_list"]
        self.index = article_list_dict["index"]
        self.board = article_list_dict["board"]
        self.new_board = self.board

    def GetNextArticle(self) -> Article:
        if (len(self.article_url_list) <= 0):
            self._finishPage()
            self._crawlPage()
        return Article(article_url=self.article_url_list.pop())

    def _finishPage(self):
        self.database_manager.PageFinished(board=self.board , index=self.index)
        self.board = self.new_board
        self.index = self.database_manager.NewPage(board=self.board)
        if (self.index is None):
            self._startNewBoard()

    def _crawlPage(self):
        data = requests.get(BASE_URL + f"/bbs/{self.board}/index{self.index}.html" , headers=HEADER_18)
        soup = BeautifulSoup(data.text , "html.parser")
        headers = soup.select("div.r-ent div.title a")
        urls = []
        for header in headers:
            urls.append(header["href"])
        self.article_url_list = urls

    def _startNewBoard(self):
        raise Exception("You Can't Switch New Board.")
