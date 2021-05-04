# Google Map Review

Google Map 餐廳評價爬蟲

## 步驟

- 爬取數家指定餐廳門市的Google map
- 對每筆資料進行內容構面分析，如使用者、發布時間、餐廳位置、評價等等
- 將資料儲存與noSQL資料庫中，如mongodb
- 對每筆資料做基本的情緒分析

## TODO
- [ ] 設計簡易的網站呈現結果(使用flask)
- [ ] 以Docker Compose建置服務

## Usage

### 爬蟲
先將要爬的餐廳存在`query.txt`
```bash
cd src
python scraper.py
```

### 情緒分析
因目前手邊沒有算力，這裡使用[cnsenti中文情緒情感分析庫](https://zhuanlan.zhihu.com/p/117673231)快速完成任務，而此package使用語言為簡體中文，所以會先將繁體中文暫時轉成簡體，但最後分析結果為繁體，此方法為暫時應急用，可以抽換掉。

```bash
cd src
python sentiment.py
```

### Mongodb

啟動mongodb
```bash
sudo brew services start mongodb-community

cd src
python mongodb.py

# sudo brew services stop mongodb-community
```


other commands
```bash
mongo

# check
netstat -an | grep 27017
```



## Reference

[Scraping Google Maps reviews in Python](https://towardsdatascience.com/scraping-google-maps-reviews-in-python-2b153c655fc2)

[Google Maps Scraper](https://github.com/gaspa93/googlemaps-scraper)

[cnsenti中文情緒情感分析庫](https://zhuanlan.zhihu.com/p/117673231)
