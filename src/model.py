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
        self.label_list : list[str] = JsonManager.LoadLabels()
        self.LoadTmpArticle()
        self.NextComment()

    def __del__(self) -> None:
        if (max(tag for tag in self.comment_tag["tag"]) == 0):
            self._article.comment.append(self.tmp_comment)
        self.Save()

    def LoadTmpArticle(self) -> None:
        self._article = JsonManager.LoadArticle()

    def NextComment(self) -> None:
        if (self.comment_tag is not None):
            self.comment_tag_list.append(self.comment_tag)
        self._checkArticle()
        self.tmp_comment = self._article.comment.pop()
        self.comment_tag = {
            "url" : self._article.url,
            "text" : self.tmp_comment.content,
            "tag" : [0 for _ in range(len(self.label_list))]
        }

    def ClearTag(self) -> None:
        if (self.comment_tag is not None):
            self.comment_tag = {
                "url" : self._article.url,
                "text" : self.tmp_comment.content,
                "tag" : [0 for _ in range(len(self.label_list))]
            }
        else:
            raise Exception("There is no comment now.")

    def _checkArticle(self):
        if (len(self._article.comment) <= 0):
            self._article = self.spider_manager.GetNextArticle()
            self.Save()

    def Save(self):
        JsonManager.SaveResult(self.comment_tag_list)
        JsonManager.SaveArticle(self._article.ParseDict())
        self.comment_tag_list = []

    def GetNowArticle(self) -> Article:
        return self._article

    def GetNowComment(self) -> dict:
        return self.comment_tag
    
    def AddCommentTag(self, label_index : int) -> None:
        if (label_index < len(self.label_list)):
            self.comment_tag["tag"][label_index] = 1
        else:
            raise Exception(f"Index \"{label_index}\" is out of labels list range.")

    def DeleteNowComment(self) -> None:
        self.comment_tag = None

    def GetLabels(self) -> list[str]:
        return self.label_list