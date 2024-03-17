# 第一次寫爬蟲的練習

## Installation
`
pip install -r requirements.txt
`

## Usage
目前只有爬ptt單篇文章的功能(且遇到18+看板會報錯)
可直接修改main.py並執行 (其餘沒提到的檔案請小心使用，造成任何問題後果自負) 

1. 引入 src/artice.py 內的 Artice
    ```py
    from src.artice import Artice
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