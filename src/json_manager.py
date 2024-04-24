import json
import os

from src.article import Article
from src.dict_article import DictArticle

class JsonManager:

    DEFAULT_ARTICLE = {
        "url": "default",
        "content": "default",
        "author": "default",
        "title": "default",
        "board": "HatePolitics",
        "time": "2999-01-01 00:00:00",
        "comments": [
        ]
    }

    DEFAULT_ARTICLE_LIST = {
        "board": "HatePolitics",
        "index": 1701,
        "article_url_list": [
        ]
    }

    TMP_ARTICLE_PATH = "src/temp_article.json"
    TMP_ARTICLE_LIST_PATH = "src/temp_article_list.json"

    def SaveArticle(article : dict) -> None:
        with open(JsonManager.TMP_ARTICLE_PATH, "w") as temp_article:
            json.dump(article, temp_article)
            temp_article.close()
        
    def LoadArticle() -> Article:
        if (os.path.exists(JsonManager.TMP_ARTICLE_PATH)):
            with open(JsonManager.TMP_ARTICLE_PATH, 'r') as temp_article:
                article_dict = json.load(temp_article)
                temp_article.close()
        else:
            article_dict = JsonManager.DEFAULT_ARTICLE
        return DictArticle(article_dict)
        
    def SaveArticeList(artice_list : dict) -> None:
        with open(JsonManager.TMP_ARTICLE_LIST_PATH, "w") as temp_article_list:
            json.dump(artice_list, temp_article_list)
            temp_article_list.close()

    def LoadArticleList() -> dict:
        if (os.path.exists(JsonManager.TMP_ARTICLE_LIST_PATH)):
            with open(JsonManager.TMP_ARTICLE_LIST_PATH, 'r') as temp_article_list:
                article_list = json.load(temp_article_list)
                temp_article_list.close()
        else:
            article_list = JsonManager.DEFAULT_ARTICLE_LIST
        return article_list
    
    def SaveResult(result : list[dict] , path : str = "result" , file_name : str = "result.json") -> None:
        if not os.path.exists(path):
            os.mkdir(path=path)

        if (os.path.exists(f"{path}/{file_name}")):
            with open(f"{path}/{file_name}", 'r') as tag_file:
                data = json.load(tag_file)
                tag_file.close()
        else : 
            data = []

        data += result
        with open(f"{path}/{file_name}" , 'w') as tag_file:
            json.dump(data, tag_file)
            tag_file.close()
        

    def LoadLabels() -> list[dict]:
        labels_dict : dict = {}
        with open("labels.json", 'r' , encoding="UTF-8") as labels_file:
            labels_dict = json.load(labels_file)
            labels_file.close()
        return labels_dict["categories"]


