from src.database_manager import DatabaseManeger
from src.article import Article
from src.json_manager import JsonManager
from src.model import Model

def SetInputInfo(label_list : list[str]) -> str:
    text = f"Tags : \n"
    index_length = len(str(len(label_list) - 1))
    max_length = max(len(label) for label in label_list)
    for i in range(len(label_list)):
        text += f"{f"({i})":<{index_length + 2}} {label_list[i]:{chr(12288)}<{max_length + 2}} "
        if ((i + 1) % 5 == 0):
            text += '\n'
    return text

def main():
    model = Model()
    input_text = ""
    input_info = SetInputInfo(model.GetLabels())
    while(True):
        print("---------------------------------------------------------------")
        print(f"Article : {model.GetNowArticle().content}")
        print(f"text : {model.GetNowComment()["text"]}")
        print(input_info)
        print("Input \"del\" to delete this comment.")
        print("Input \"q\" or \"Q\" to exit.")
        print("Input \"save\" to save.")
        input_text = input("Input : ")
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
            try:
                tag_list = list(map(int, input_text.split()))
            except:
                input("Please input number.\nPress \"enter\" to continue.")
                continue
            try:
                for tag in input_text.split():
                    model.AddCommentTag(int(tag))
            except Exception as e:
                print(e)
                input("Press \"enter\" to continue.")
                model.ClearTag()
                continue
        model.NextComment()


if __name__ == "__main__":
    main()