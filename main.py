from src.artice import Artice
from src.comment import Comment

def main():
    artice = Artice("/bbs/C_Chat/M.1710679059.A.331.html")
    print("URL : " , artice.url)
    print("Author : " , artice.author)
    print("Title : " , artice.title)
    print("Board : " , artice.board)
    print("Time : " , artice.date_time)
    print(artice.content)
    for comment in artice.comment:
        print("--------------------comment-----------------------")
        print(f"tag : {comment.tag}")
        print(f"author : {comment.author}")
        print(f"content : {comment.content}")
        print(f"ip : {comment.ip}")
        print(f"datetime : {comment.date_time}")

if __name__ == "__main__":
    main()