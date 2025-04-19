# 永續智慧創新黑客松爬蟲工具 (Sustainability Hackathon Scraper)

## 中文說明

這個專案包含一組 Python 爬蟲工具，用於從永續智慧創新黑客松競賽網站爬取企業命題資訊。專案分為兩個主要步驟：

1. **步驟一 (step1_scrape_links.py)**：從主頁面爬取所有命題連結、標題和企業名稱。
2. **步驟二 (step2_scrape_details.py)**：訪問每個命題的詳細頁面，提取更多信息（如企業介紹、命題說明等）。

目標網站：[永續智慧創新黑客松](https://sustainabilityhackathon-tw.org) - 這是一個促進永續發展創新解決方案的黑客松競賽平台，匯集了多家企業提出的實際挑戰和命題。

### 不同年度資料的爬取方法

若要爬取不同年度的黑客松資料，請按照以下步驟：

1. 修改 `step1_scrape_links.py` 中的目標網頁 URL，找到當年度的命題方式頁面
2. 執行 `step1_scrape_links.py` 獲取當年度的 challenges 列表
3. 將輸出的 challenges 列表複製並貼上到 `step2_scrape_details.py` 中的 challenges 變數
4. 執行 `step2_scrape_details.py` 爬取詳細資訊並存為 CSV

### 動機

開發這個爬蟲的目的是希望從企業角度了解他們的需求與挑戰，這可能與我們日常思考問題的角度不同。這也是一個練習爬蟲技術的好機會，特別是使用 BeautifulSoup 和 Pandas 等工具進行數據抓取與處理。

我最初嘗試用單一文件實現所有功能，希望寫出優雅且精巧的代碼，但發現這種做法可能過度工程化，導致難以解決錯誤。因此，我採用分步驟的方法，計劃在未來可能優化為單一腳本版本。

### 未來展望

作為這個專案的開發者，以下是我對未來可能的改進方向：

1. **代碼整合與模塊化**
   - 將兩個腳本整合為一個完整的工具，同時保持模塊化結構
   - 建立配置文件系統，允許用戶自定義爬蟲行為而不需修改代碼

2. **穩健性增強**
   - 添加更完善的錯誤處理和重試機制
   - 增加網站結構變化的自適應能力，減少維護成本

3. **功能擴展**
   - 添加數據分析功能，自動生成命題趨勢分析報告
   - 實現歷史數據比較，追踪跨年度的主題變化
   - 添加自動化定時爬取功能，無需人工干預

4. **技術提升**
   - 學習使用異步爬蟲提高效率
   - 探索 Selenium 等工具處理動態加載內容
   - 考慮使用 scrapy 框架重構，提高可維護性

### 學習心得

Vibe Coding (感覺編程) 是一種強調直覺和創造力的編程方式。在本項目中，我體驗到：

1. **分步設計的價值** - 通過將複雜任務分解為簡單步驟，可以更容易理解問題和調試錯誤
2. **逆向工程的學習模式** - 先實現基本功能，然後通過分析和改進代碼來學習更優雅的實現方式
3. **正確使用第三方庫** - BeautifulSoup 提供了強大的 HTML 解析能力，Pandas 則簡化了數據處理

即使是看似簡單的爬蟲項目，也能提供豐富的學習機會，從 HTTP 請求、HTML 解析、數據處理到文件操作，涵蓋了多個實用技能點。

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

### 爬取不同年度黑客松資料的流程

1. 修改 `step1_scrape_links.py` 中的 URL 變數：
   ```python
   url = "https://當年度黑客松網站/命題方式頁面/"
   ```

2. 執行 `step1_scrape_links.py` 獲取命題列表輸出

3. 複製輸出的 challenges 列表，並替換 `step2_scrape_details.py` 中的 challenges 變數

4. 執行 `step2_scrape_details.py` 完成詳細資訊爬取

## English Description

This project contains a set of Python web scrapers designed to extract challenge information from the Sustainability Hackathon competition website. The project is divided into two main steps:

1. **Step 1 (step1_scrape_links.py)**: Scrapes all challenge links, titles, and company names from the main page.
2. **Step 2 (step2_scrape_details.py)**: Visits each challenge detail page to extract more information (such as company introduction, challenge description, etc.).

Target Website: [Sustainability Hackathon Taiwan](https://sustainabilityhackathon-tw.org) - This is a hackathon competition platform promoting innovative solutions for sustainable development, gathering actual challenges and topics proposed by various companies.

### Scraping Data from Different Years

To scrape hackathon data from different years, follow these steps:

1. Modify the target URL in `step1_scrape_links.py` to point to that year's challenge page
2. Run `step1_scrape_links.py` to get the challenges list for that year
3. Copy the output challenges list and paste it into the challenges variable in `step2_scrape_details.py`
4. Run `step2_scrape_details.py` to scrape detailed information and save as CSV

### Motivation

The purpose of developing this scraper is to understand the needs and challenges from a business perspective, which may differ from how we think about problems in our daily lives. This is also a good opportunity to practice web scraping techniques, especially using tools like BeautifulSoup and Pandas for data extraction and processing.

I initially tried to implement all functionality in a single file, hoping to write elegant and fancy code, but found this approach might be over-engineered, making it difficult to resolve errors. Therefore, I adopted a step-by-step approach, with plans to possibly optimize it into a single script version in the future.

### Future Prospects

As a developer of this project, here are some potential improvements for the future:

1. **Code Integration and Modularization**
   - Integrate the two scripts into a complete tool while maintaining a modular structure
   - Build a configuration file system to allow users to customize scraper behavior without modifying code

2. **Enhanced Robustness**
   - Add more comprehensive error handling and retry mechanisms
   - Increase adaptability to website structure changes, reducing maintenance costs

3. **Feature Extensions**
   - Add data analysis features to automatically generate trend reports on challenges
   - Implement historical data comparison to track theme changes across years
   - Add automated scheduled scraping functionality, requiring no manual intervention

4. **Technical Improvements**
   - Learn to use asynchronous scraping to improve efficiency
   - Explore tools like Selenium to handle dynamically loaded content
   - Consider refactoring with the Scrapy framework to improve maintainability

### Learning Reflections

Vibe Coding (intuitive programming) is a programming approach that emphasizes intuition and creativity. In this project, I experienced:

1. **The value of step-by-step design** - By breaking complex tasks into simple steps, it becomes easier to understand problems and debug errors
2. **Reverse engineering learning model** - Implementing basic functionality first, then learning more elegant implementation methods through analysis and code improvement
3. **Proper use of third-party libraries** - BeautifulSoup provides powerful HTML parsing capabilities, while Pandas simplifies data processing

Even seemingly simple scraping projects can provide rich learning opportunities, covering multiple practical skills from HTTP requests, HTML parsing, and data processing to file operations.

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

### Process for Scraping Different Year's Hackathon Data

1. Modify the URL variable in `step1_scrape_links.py`:
   ```python
   url = "https://that-year-hackathon-website/challenges-page/"
   ```

2. Run `step1_scrape_links.py` to get the challenges list output

3. Copy the output challenges list and replace the challenges variable in `step2_scrape_details.py`

4. Run `step2_scrape_details.py` to complete the detailed information scraping