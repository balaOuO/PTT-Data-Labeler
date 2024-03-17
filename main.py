from src.article import Article
from src.comment import Comment

def main():
    article = Article("/bbs/C_Chat/M.1710679059.A.331.html")
    print("URL : " , article.url)
    print("Author : " , article.author)
    print("Title : " , article.title)
    print("Board : " , article.board)
    print("Time : " , article.date_time)
    print(article.content)
    for comment in article.comment:
        print("--------------------comment-----------------------")
        print(f"tag : {comment.tag}")
        print(f"author : {comment.author}")
        print(f"content : {comment.content}")
        print(f"ip : {comment.ip}")
        print(f"datetime : {comment.date_time}")

if __name__ == "__main__":
    main()