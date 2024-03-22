from src.comment import Comment
from datetime import datetime

class DictComment(Comment):
    def __init__(self , comment_dict : dict):
        self.tag = comment_dict["tag"]
        self.author = comment_dict["author"]
        self.content = comment_dict["content"]
        self.ip = comment_dict["ip"]
        self.date_time = datetime.strptime(comment_dict["time"], "%Y-%m-%d %H:%M:%S")
