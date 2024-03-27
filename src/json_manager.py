import json
import os

from src.article import Article
from src.dict_article import DictArticle

class JsonManager:

    DEFAULT_ARTICLE = {
        "url": "https://www.ptt.cc/bbs/Gossiping/M.1704036476.A.97F.html",
        "content": "\n\n\n\n\n\n\n\n\n\u525b\u525b\u770b\u6c11\u8996\n\n\u59d0\u59d0\u525b\u525b\u597d\u50cf\u628a\u63db\u8863\u670d\u7684\u906e\u853d\u7269\u62ff\u5230\u53f0\u4e0a\n\n\u7136\u5f8c\u76f4\u63a5\u628a\u8863\u670d\u812b\u4e0b\u653e\u5728\u67b6\u5b50\u4e0a\n\n\n\u96d6\u7136\u6f38\u6f38\u5df2\u7d93\u770b\u4e0d\u51fa\u4f86\u9019\u59d0\u59d0\u5230\u5e95\u662f\u8ab0\n\n\u53ef\u80fd\u8981\u770b\u5b57\u5e55\u624d\u77e5\u9053\u662f\u8ab0\n\n\u4e0d\u77e5\u9109\u6c11\u600e\u770b \u8de8\u5e74\u7684\u59d0\u59d0??\n\n\u5230\u73fe\u5728\u90fd\u5e7e\u5e74\u4e86 \u59d0\u59d0\u600e\u9ebc\u6c92\u6709\u8b8a\u8001\u7684\u8da8\u5411??\n\n\u96e3\u9053\u4e03\u9f8d\u73e0\u7684\u9577\u751f\u4e0d\u8001\u8a31\u9858\u6210\u529f\u4e86??\n\n\u5f8c\u9762\u821e\u8005\u600e\u7a7f\u7684\u8ddf\u4f5b\u5229\u624e\u4e00\u6a23??\n\n\n\n\n--\n\u6296\u97f3\u4e00\u97ff \u7236\u6bcd\u767d\u990a\n\u9f13\u8072\u82e5\u97ff \u6c5f\u8559\u5feb\u6d3b\n\u5587\u53ed\u4e00\u97ff \u5c71\u7f8a\u63a7\u5834\n\u5783\u573e\u82e5\u97ff \u5954\u8dd1\u8ffd\u5834\n\n--\n",
        "author": "sasolala",
        "title": "[\u554f\u5366] \u59d0\u59d0\u525b\u525b\u5728\u53f0\u4e0a\u63db\u8863\u670d\u55ce??",
        "board": "Gossiping",
        "time": "2023-12-31 23:27:52",
        "comments": [
        ]
    }

    DEFAULT_ARTICLE_LIST = {
        "board": "Gossiping",
        "index": 33410,
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
        


