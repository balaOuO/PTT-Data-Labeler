import json

from src.article import Article

class JsonManager:

    def ArticeToDict(self , article : Article) -> dict:
        article_dict = {
            "url" : article.url,
            "content" : article.content,
            "author" : article.author,
            "title" : article.title,
            "board" : article.board,
            "time" : str(article.date_time),
            "comments" : [
                {
                    "tag" : comment.tag,
                    "author" : comment.author,
                    "content" : comment.content,
                    "ip" : comment.ip,
                    "time" : str(comment.date_time)
                } for comment in article.comment
            ]
        }
        return article_dict

    def SaveArticle(self , article : dict) -> None:
        with open("src/temp_article.json", "w") as temp_article:
            json.dump(article, temp_article)
            temp_article.close()
        
    def LoadArticle(self) -> dict:
        with open('src/temp_article.json', 'r') as temp_article:
            article_dict = json.load(temp_article)
            temp_article.close()
        return article_dict
        
    def SaveArticeList(self, artice_list : dict) -> None:
        with open("src/temp_article_list.json", "w") as temp_article_list:
            json.dump(artice_list, temp_article_list)
            temp_article_list.close()

    def LoadArticleList(self) -> dict:
        with open('src/temp_article_list.json', 'r') as temp_article_list:
            article_list = json.load(temp_article_list)
            temp_article_list.close()
        return article_list

