import os
from datetime import datetime
import requests, json, csv
from bs4 import BeautifulSoup
import pandas as pd
import urllib3
urllib3.disable_warnings()

# === 1) 在程式開頭就產生時間戳，所有檔案共用 ===
STAMP = datetime.now().strftime("%Y%m%d_%H%M%S")

# === 2) 加一個專門存放結果的子資料夾（可選）===
OUT_DIR = "results"
os.makedirs(OUT_DIR, exist_ok=True)  # 如果不存在就自動建立

def get_page_content(url):
    """
    獲取頁面內容
    
    Args:
        url: 目標網頁URL
    
    Returns:
        網頁文本內容，若請求失敗則返回None
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        print(f"正在請求: {url}")
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            return response.text
        else:
            print(f"請求失敗: {response.status_code}")
            return None
    except Exception as e:
        print(f"請求異常: {e}")
        return None

def extract_challenge_info(url, title, company):
    """
    從挑戰頁面提取資訊
    
    Args:
        url: 挑戰頁面URL
        title: 挑戰標題
        company: 命題企業名稱
    
    Returns:
        包含挑戰詳情的字典，若提取失敗則返回None
    """
    content = get_page_content(url)
    if not content:
        return None
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # === 3) 提取網站資訊 ===
    company_website = ""
    website_tag = soup.find(string=lambda text: text and "企業官網" in text)
    if website_tag and website_tag.find_next('a'):
        company_website = website_tag.find_next('a')['href']
    
    # === 4) 提取社群網址 ===
    social_url = ""
    social_tag = soup.find(string=lambda text: text and "社群網址" in text)
    if social_tag and social_tag.find_next('a'):
        social_url = social_tag.find_next('a')['href']
    
    # === 5) 提取企業介紹 ===
    company_intro = ""
    intro_tag = soup.find(string=lambda text: text and "企業介紹" in text)
    if intro_tag and intro_tag.find_next('p'):
        company_intro = intro_tag.find_next('p').text.strip()
    
    # === 6) 提取命題說明 ===
    challenge_description = ""
    desc_tag = soup.find(string=lambda text: text and "命題說明" in text)
    if desc_tag:
        current = desc_tag.find_parent('p')
        if current:
            desc_texts = []
            desc_texts.append(current.text.strip())
            
            next_elem = current.find_next_sibling()
            while next_elem and next_elem.name in ['p', 'ol', 'ul']:
                if next_elem.name == 'p':
                    desc_texts.append(next_elem.text.strip())
                elif next_elem.name in ['ol', 'ul']:
                    for li in next_elem.find_all('li'):
                        desc_texts.append(f"- {li.text.strip()}")
                next_elem = next_elem.find_next_sibling()
            
            challenge_description = "\n\n".join(desc_texts)
    
    return {
        "挑戰標題": title,
        "企業名稱": company,
        "企業官網": company_website,
        "社群網址": social_url,
        "企業介紹": company_intro,
        "命題說明": challenge_description,
        "挑戰連結": url
    }

def main():
    # === 7) 從step1程式的輸出複製來的挑戰資訊列表 ===
    # 切換年度時，請執行step1_scrape_links.py並複製輸出結果到這裡
    challenges = [
    {'url': 'https://sustainabilityhackathon.fcu.edu.tw/%e9%8a%80%e9%ab%ae%e6%99%ba%e6%85%a7%e7%85%a7%e8%ad%b7/', 'title': '銀髮智慧照護', 'company': '點我看影片'},
    {'url': 'https://sustainabilityhackathon.fcu.edu.tw/%e9%8a%80%e9%ab%ae%e7%ac%ac%e4%b8%89%e4%ba%ba%e7%94%9f/', 'title': '銀髮第三人生', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%f0%9f%8f%a5%e6%9c%aa%e4%be%86%e9%86%ab%e9%99%a2/', 'title': '未來醫院', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e5%81%8f%e9%84%89%e6%95%99%e8%82%b2%e5%89%b5%e6%96%b0/', 'title': '偏鄉教育創新', 'company': '點我看影片'},
    {'url': 'https://sustainabilityhackathon.fcu.edu.tw/%f0%9f%8e%92-%e5%81%8f%e9%84%89%e6%95%99%e8%82%b2%e7%94%9f%e6%85%8b%e5%9c%88/', 'title': '偏鄉教育生態圈', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%a6%82%e5%bf%b5%e5%ba%97%e5%89%b5%e6%84%8f%e8%a1%8c%e9%8a%b7/', 'title': '概念店創意行銷', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%f0%9f%96%a5-%e6%95%b8%e4%bd%8d%e8%a1%8c%e9%8a%b7%e8%88%87%e7%a4%be%e6%9c%83%e8%b2%ac%e4%bb%bb/', 'title': '生活圈創新互動模式', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%a8%82%e9%bd%a1%e5%ae%9c%e5%b1%85%e7%94%9f%e6%85%8b%e7%b3%bb/', 'title': '樂齡宜居生態系', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%f0%9f%91%a9%e2%80%8d%f0%9f%8f%ab%e6%99%ba%e6%85%a7%e8%a1%8c%e9%8a%b7/', 'title': '智慧行銷', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%99%ba%e6%85%a7%e5%b1%85%e5%ae%b6%e7%85%a7%e8%ad%b7/', 'title': '智慧居家照護', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%99%ba%e6%85%a7%e9%86%ab%e7%99%82%e8%88%87%e7%ae%a1%e7%90%86/', 'title': '智慧醫療與管理', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%99%ba%e6%85%a7%e4%ba%a4%e9%80%9a%e8%88%87%e7%ae%a1%e7%90%86/', 'title': '智慧交通與管理', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%99%ba%e6%85%a7%e6%b0%b4%e8%b3%87%e6%ba%90%e7%ae%a1%e7%90%86/', 'title': '智慧水資源管理', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e5%89%b5%e6%96%b0%e5%93%81%e7%89%8c%e8%a1%8c%e9%8a%b7/', 'title': '創新品牌行銷', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e6%b0%b8%e7%ba%8c%e8%a1%8c%e9%8a%b7/', 'title': '永續行銷', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%f0%9f%8f%a4-%e5%89%b5%e6%96%b0%e8%a1%8c%e9%8a%b7/', 'title': '創新行銷', 'company': '點我看影片'},
    {'url': 'https://sustainabilityhackathon.fcu.edu.tw/%e6%a8%82%e9%bd%a1%e6%b0%b8%e7%ba%8c%e5%95%86%e6%a5%ad/', 'title': '樂齡永續商業', 'company': '點我看影片'},
    {'url': 'https://sustainabilityhackathon.fcu.edu.tw/%e6%b0%b8%e7%ba%8c%e6%99%ba%e6%85%a7%e5%95%86%e6%a5%ad/', 'title': '永續智慧商業', 'company': '點我看影片'},
    {'url': 'http://sustainabilityhackathon.fcu.edu.tw/%e9%98%b2%e7%96%ab%e6%84%9f%e8%ac%9d%e5%be%ae%e9%9b%bb%e5%bd%b1/', 'title': '防疫感謝微電影特別場', 'company': '點我看影片'}
    ]
    
    # === 8) 爬取每個挑戰的詳細資訊 ===
    results = []
    for i, ch in enumerate(challenges, start=1):
        print(f"\n處理 ({i}/{len(challenges)}): {ch['title']}")
        info = extract_challenge_info(ch['url'], ch['title'], ch['company'])
        if info:
            results.append(info)
            print("✔ 完成")
        else:
            print("✖ 失敗")

    # === 9) 用 pandas 直接存成 CSV ===
    if results:                       # 確保有資料才寫檔
        df = pd.DataFrame(results)

        csv_path = os.path.join(OUT_DIR, f"hackathon_{STAMP}.csv")

        df.to_csv(csv_path, index=False, encoding="utf-8-sig")

        print(f"\n✅ 已寫入：{csv_path}")
        print(f"共 {len(results)} 筆挑戰資訊")
    else:
        print("⚠ 沒有任何資料可寫入")

if __name__ == "__main__":
    main()