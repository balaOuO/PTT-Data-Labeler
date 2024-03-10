from src.ptt_article_spyder import Artice

def main():
    artice = Artice("/bbs/BabyMother/M.1709873056.A.AB3.html")
    print(artice.GetContent())
    for msg in artice.GetMessages():
        print(msg)

if __name__ == "__main__":
    main()