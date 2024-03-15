from src.ptt_article_spyder import Artice

def main():
    artice = Artice("/bbs/sex/M.1710469992.A.FE8.html")
    print(artice.GetContent())
    for msg in artice.GetMessages():
        print(msg)

if __name__ == "__main__":
    main()