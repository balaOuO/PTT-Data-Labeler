import json

from src.article import Article
from src.dict_article import DictArticle

class JsonManager:

    def SaveArticle(article : dict) -> None:
        with open("src/temp_article.json", "w") as temp_article:
            json.dump(article, temp_article)
            temp_article.close()
        
    def LoadArticle() -> Article:
        with open('src/temp_article.json', 'r') as temp_article:
            article_dict = json.load(temp_article)
            temp_article.close()
        return DictArticle(article_dict)
        
    def SaveArticeList(artice_list : dict) -> None:
        with open("src/temp_article_list.json", "w") as temp_article_list:
            json.dump(artice_list, temp_article_list)
            temp_article_list.close()

    def LoadArticleList() -> dict:
        with open('src/temp_article_list.json', 'r') as temp_article_list:
            article_list = json.load(temp_article_list)
            temp_article_list.close()
        return article_list

