from src.article import Article
from src.dict_comment import DictComment
from datetime import datetime

class DictArticle(Article):

    def __init__(self, article_dict: dict) -> None:
        self.url = article_dict["url"]
        self.content = article_dict["content"]
        self.author = article_dict["author"]
        self.title = article_dict["title"]
        self.board = article_dict["board"]
        self.date_time = datetime.strptime(article_dict["time"], "%Y-%m-%d %H:%M:%S")
        self.comment = [DictComment(comment_dict) for comment_dict in article_dict["comments"]]