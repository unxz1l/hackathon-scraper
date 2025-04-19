# 永續智慧創新黑客松爬蟲工具 (Sustainability Hackathon Scraper)

## 中文說明

這個專案包含一組 Python 爬蟲工具，用於從永續智慧創新黑客松競賽網站爬取企業命題資訊。專案分為兩個主要步驟：

1. **步驟一 (step1_scrape_links.py)**：從主頁面爬取所有命題連結、標題和企業名稱。
2. **步驟二 (step2_scrape_details.py)**：訪問每個命題的詳細頁面，提取更多信息（如企業介紹、命題說明等）。

### 動機

開發這個爬蟲的目的是希望從企業角度了解他們的需求與挑戰，這可能與我們日常思考問題的角度不同。這也是一個練習爬蟲技術的好機會，特別是使用 BeautifulSoup 和 Pandas 等工具進行數據抓取與處理。

我最初嘗試用單一文件實現所有功能，希望寫出優雅且精巧的代碼，但發現這種做法可能過度工程化，導致難以解決錯誤。因此，我採用分步驟的方法，計劃在未來可能優化為單一腳本版本。

### 功能特點

- 自動生成時間戳記錄結果
- 將結果保存為 CSV 格式
- 提取包括企業官網、社群網址、企業介紹和命題說明在內的信息
- 穩健的錯誤處理機制

### 使用方法

1. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

2. 執行爬蟲：
   ```bash
   python step1_scrape_links.py  # 爬取命題連結
   python step2_scrape_details.py  # 爬取詳細資訊
   ```

3. 結果將保存在 `results` 資料夾中，文件名格式為 `hackathon_YYYYMMDD_HHMMSS.csv`

## English Description

This project contains a set of Python web scrapers designed to extract challenge information from the Sustainability Hackathon competition website. The project is divided into two main steps:

1. **Step 1 (step1_scrape_links.py)**: Scrapes all challenge links, titles, and company names from the main page.
2. **Step 2 (step2_scrape_details.py)**: Visits each challenge detail page to extract more information (such as company introduction, challenge description, etc.).

### Motivation

The purpose of developing this scraper is to understand the needs and challenges from a business perspective, which may differ from how we think about problems in our daily lives. This is also a good opportunity to practice web scraping techniques, especially using tools like BeautifulSoup and Pandas for data extraction and processing.

I initially tried to implement all functionality in a single file, hoping to write elegant and fancy code, but found this approach might be over-engineered, making it difficult to resolve errors. Therefore, I adopted a step-by-step approach, with plans to possibly optimize it into a single script version in the future.

### Features

- Automatic timestamp generation for results
- Saving results in CSV format
- Extraction of information including company website, social media links, company introduction, and challenge description
- Robust error handling mechanisms

### Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the scrapers:
   ```bash
   python step1_scrape_links.py  # Scrape challenge links
   python step2_scrape_details.py  # Scrape detailed information
   ```

3. Results will be saved in the `results` folder, with filenames in the format `hackathon_YYYYMMDD_HHMMSS.csv`