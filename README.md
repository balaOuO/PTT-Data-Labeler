# 第一次寫爬蟲的練習

## 環境建置
`
pip install -r requirements.txt
`

## 如何使用
目前只有爬ptt單篇文章的功能(且遇到18+看板會報錯)

1. 引入 src/ptt_article_spyder.py 內的 Artice
    ```py
    from src.ptt_article_spyder import Artice
    ```

1. 創建 Artice 物件，建構時傳入ptt文章網址(不含"https://www.ptt.cc" 的部分)
    ```py
    artice = Artice("/bbs/car/M.1709972123.A.A17.html")
    ```

1. 呼叫GetContent()回傳本文，GetMessages()回傳所有留言
    ```py
    artice.GetContent() # return type : str
    artice.GetMessages() # return type : list[str]
    ```