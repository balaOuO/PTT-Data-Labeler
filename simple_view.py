from src.database_manager import DatabaseManeger
from src.article import Article
from src.json_manager import JsonManager
from src.model import Model

model = Model()
input_text = ""

while(True):
    print("---------------------------------------------------------------")
    print(f"Article : {model.GetNowArticle().content}")
    print(f"text : {model.GetNowComment()["text"]}")
    print("Input \"del\" to delete this comment.")
    print("Input \"q\" or \"Q\" to exit.")
    print("Input \"save\" to save.")
    input_text = input("Input tag : ")
    if (input_text == "q" or input_text == "Q"):
        break
    elif (input_text == "" or input_text == " "):
        continue
    elif (input_text == "del"):
        model.DeleteNowComment()
    elif (input_text == "save"):
        model.Save()
        continue
    else:
        for tag in input_text.split():
            model.AddCommentTag(tag)
    model.NextComment()