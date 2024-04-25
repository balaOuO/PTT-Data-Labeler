from src.database_manager import DatabaseManeger
from src.article import Article
from src.json_manager import JsonManager
from src.model import Model
from rich.console import Console
from rich.table import Table

console = Console()

def SetInputInfo(label_list : list[str]) -> str:
    table = Table()
    table.add_column("Key", justify="left", style="cyan", no_wrap=True)
    table.add_column("Name", justify="left" , style="magenta", no_wrap=True)
    for label in label_list:
        table.add_row(label["key"], label["name"])

    return table

def main():
    model = Model()
    input_text = ""
    input_info = SetInputInfo(model.GetLabels())
    while(True):
        console.print(input_info)
        console.print("[yellow bold]---------------------------------------------------------------")
        console.print(f"[yellow bold]Article : [black]{model.GetNowArticle().content}")
        console.print(f"[yellow bold]text : [black]{model.GetNowComment()["text"]}")
        console.print("Input \"del\" to delete this comment.")
        console.print("Input \"q\" or \"Q\" to exit.")
        console.print("Input \"save\" to save.")
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
            is_error : bool = False
            for tag in input_text.split():
                result = model.AddCommentTag(tag)
                if (result == False):
                    console.input(f"[red bold]tag [cyan]{tag} [red bold]is not in labels.json.")
                    is_error = True

            if is_error:
                model.ClearTag()
                continue

            now_comment_tag_state = model.GetNowComment()["tag"]
            labels = model.GetLabels()
            console.print("[yellow bold]This comment's tag :")

            for i in range(len(now_comment_tag_state)):
                if (now_comment_tag_state[i] == 1):
                    console.print(labels[i]["name"], style="green bold", end="  ")
            print("")

            if (console.input("[yellow bold]Continue? ([green bold]y[yellow bold]/[red]n[yellow bold]) : ") in ('y', 'Y')):
                pass
            else:
                model.ClearTag()
                continue
            
        model.NextComment()


if __name__ == "__main__":
    main()