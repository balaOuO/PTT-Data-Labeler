from src.article import Article

from supabase import create_client, Client
import os
from dotenv import load_dotenv
load_dotenv()

class DatabaseManeger:

    def __init__(self) -> None:
        url : str = os.getenv("SUPABASE_URL")
        key : str = os.getenv("SUPABASE_KEY")
        self.db: Client = create_client(url, key)

    def PageFinished(self , board : str , index : int) -> None:
        self.db.table("TagState").update({
            "is_finished" : True
        }).eq("board" , board).eq("index" , index).execute()

    def NewPage(self , board : str) -> int | None:
        return self.db.rpc("newpage" , params={"board_name" : board}).execute().data
    
    def StartNewBoard(self , board : str , index : int) -> None:
        self.db.table("Board").upsert({
            "name" : board
        }).execute()
        self.db.table("TagState").insert({
            "board" : board,
            "index" : index,
            "is_finished" : False
        }).execute()

    def UploadNewArticle(self, article : Article, index : int):
        self.db.table('Article').insert({
            'url': article.url ,
            "author" : article.author ,
            "title" : article.title ,
            "time" : str(article.date_time) ,
            "content" : article.content ,
            "board" : article.board ,
            "page_index" : index
        }).execute()