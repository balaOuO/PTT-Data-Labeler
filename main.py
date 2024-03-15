from src.ptt_article_spyder import Artice
from src.comment import Comment

def main():
    artice = Artice("/bbs/Gossiping/M.1710507493.A.309.html")
    print(artice.GetContent())
    for comment in artice.GetComment():
        print("--------------------comment-----------------------")
        print(f"tag : {comment.tag}")
        print(f"author : {comment.author}")
        print(f"content  {comment.content}")
        print(f"ip : {comment.ip}")
        print(f"datetime : {comment.date_time}")

if __name__ == "__main__":
    main()