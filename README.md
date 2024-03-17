# 第一次寫爬蟲的練習

## Installation
`
pip install -r requirements.txt
`

## Usage

### 1. 引入 Article 類別

在你的程式碼中引入 `src/article.py` 內的 `Article` 類別：

```python
from src.article import Article
```

### 2. 創建 Article 物件

使用 `Article` 類別創建一個文章物件。在建構時，傳入 PTT 文章的網址（不包括 "https://www.ptt.cc" 部分）：

```python
article = Article("/bbs/car/M.1709972123.A.A17.html")
```

### 3. 查看文章資訊

透過`Article`物件可以查看文章資訊，內部包含`Comment`物件的`list`則是文章下方留言

```python
print("URL : " , article.url)        # 文章的 URL (str)
print("Author : " , article.author)  # 文章的作者 (str)
print("Title : " , article.title)    # 文章的標題 (str)
print("Board : " , article.board)    # 文章所屬的看板 (str)
print("Time : " , article.date_time) # 文章發布的日期和時間 (datetime.datetime 物件)
print(article.content)               # 文章的本文 (str)
for comment in article.comment:      # 文章的所有留言 (list[Comment])
    print("--------------------comment-----------------------")
    print(f"tag : {comment.tag}")           # 評論的標籤 (str)
    print(f"author : {comment.author}")     # 評論的作者 (str)
    print(f"content : {comment.content}")   # 評論的內容 (str)
    print(f"ip : {comment.ip}")             # 評論發布時的 IP 地址 (str or None)
    print(f"datetime : {comment.date_time}")# 評論發布的日期和時間 (datetime.datetime 物件)
```

## 注意事項

- 目前此工具僅支援爬取單篇文章，若需要爬取其他類型文章或多篇文章，需進行程式碼調整。
- 在使用時，請小心遵守 PTT 網站的使用條款，以免觸碰到網站的爬蟲規定。