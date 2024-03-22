from src.json_manager import JsonManager
from src.article import Article
from src.spider_manager import SpiderManager
from src.comment import Comment

class Model:
    def __init__(self) -> None:
        self._article : Article
        self.comment_tag : dict = None
        self.spider_manager = SpiderManager()
        self.comment_tag_list : list[dict] = []
        self.tmp_comment : Comment
        self.LoadTmpArticle()
        self.NextComment()

    def __del__(self) -> None:
        if (len(self.comment_tag["tag"]) == 0):
            self._article.comment.append(self.tmp_comment)
        JsonManager.SaveResult(self.comment_tag_list)
        JsonManager.SaveArticle(self._article.ParseDict())

    def LoadTmpArticle(self) -> None:
        self._article = JsonManager.LoadArticle()

    def NextComment(self) -> None:
        if (self.comment_tag is not None):
            self.comment_tag_list.append(self.comment_tag)
        if (len(self._article.comment) <= 0):
            self._article = self.spider_manager.GetNextArticle()
        self.tmp_comment = self._article.comment.pop()
        self.comment_tag = {
            "text" : self.tmp_comment.content,
            "tag" : []
        }

    def GetNowArticle(self) -> Article:
        return self._article

    def GetNowComment(self) -> dict:
        return self.comment_tag
    
    def AddCommentTag(self, tag : str) -> None:
        self.comment_tag["tag"].append(tag)

    def DeleteNowComment(self) -> None:
        self.comment_tag = None