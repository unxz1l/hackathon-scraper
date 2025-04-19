import requests
from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning
import warnings

# 忽略URL警告
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def scrape_hackathon_challenges(url):
    """
    從永續智慧創新黑客松競賽網頁抓取企業命題資訊
    
    Args:
        url: 網頁URL
    
    Returns:
        包含命題資訊的列表
    """
    try:
        # 發送HTTP請求獲取網頁內容
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 如果請求出錯，拋出異常
        
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 嘗試定位到表格 - 找到包含"命題目標"和"命題企業"的表格
        target_table = None
        for table in soup.find_all('table'):
            if table.find(text=lambda t: "命題目標" in t if t else False) and table.find(text=lambda t: "命題企業" in t if t else False):
                target_table = table
                break
        
        challenges = []
        
        if target_table:
            # 遍歷表格行，跳過表頭
            for row in target_table.find_all('tr')[1:]:  # 跳過表頭行
                cells = row.find_all('td')
                if len(cells) >= 4:  # 確保有足夠的單元格 (場次、命題目標、命題企業、負責單位)
                    # 找到第二個單元格中的<a>標籤 (命題目標單元格)
                    link = cells[1].find('a')
                    if link:
                        challenge = {
                            "url": link.get('href', ''),  # 獲取連結URL
                            "title": link.get_text(strip=True),  # 獲取命題標題
                            "company": cells[2].get_text(strip=True)  # 獲取企業名稱
                        }
                        challenges.append(challenge)
        
        return challenges
    
    except Exception as e:
        print(f"爬取過程中發生錯誤: {e}")
        return []

if __name__ == "__main__":
    # 目標網頁URL
    url = "https://sustainabilityhackathon-tw.org/%e5%91%bd%e9%a1%8c%e6%96%b9%e5%bc%8f/"
    
    # 抓取資料
    challenges = scrape_hackathon_challenges(url)
    
    # 輸出結果 (Python格式)
    print("challenges = [")
    for i, challenge in enumerate(challenges):
        comma = "," if i < len(challenges) - 1 else ""
        print(f"    {challenge}{comma}")
    print("]")