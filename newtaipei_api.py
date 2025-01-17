import requests
import json
from datetime import datetime
import os
import csv
import io


def convert_date_format(date_str: str) -> str:
    """將日期字串轉換為 MySQL 可接受的格式 (YYYY-MM-DD HH:MM:SS)"""
    if not date_str:
        return None

    # 定義可能的日期格式
    date_formats = [
        '%Y/%m/%d %H:%M:%S',  # YYYY/MM/DD HH:MM:SS
        '%Y-%m-%d %H:%M:%S',  # YYYY-MM-DD HH:MM:SS
        '%d/%m/%Y %H:%M:%S',  # DD/MM/YYYY HH:MM:SS
        '%m/%d/%Y %H:%M:%S',  # MM/DD/YYYY HH:MM:SS
        '%b %d, %Y %I:%M:%S %p',  # Jan 18, 2025 12:00:00 AM
        '%Y/%m/%d',           # YYYY/MM/DD
        '%Y-%m-%d',           # YYYY-MM-DD
        '%d/%m/%Y',           # DD/MM/YYYY
        '%m/%d/%Y',           # MM/DD/YYYY
        '%b %d, %Y',          # Jan 18, 2025
    ]

    # 預處理日期字串
    date_str = date_str.strip()

    for date_format in date_formats:
        try:
            date_obj = datetime.strptime(date_str, date_format)
            # 如果原始格式沒有時間部分，加上 00:00:00
            if len(date_format) <= 10:  # 只有日期部分
                return date_obj.strftime('%Y-%m-%d 00:00:00')
            return date_obj.strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            continue

    print(f"無法解析日期格式: {date_str}")
    return None


def fetch_newtaipei_events():
    """
    從台北市政府開放資料平台獲取活動資訊
    """
    url = "https://data.ntpc.gov.tw/api/datasets/029e3fc2-1927-4534-8702-da7323be969b/csv/file"

    try:
        response = requests.get(url)
        response.raise_for_status()

        # 使用 StringIO 來處理 CSV 內容
        csv_content = io.StringIO(response.text)
        csv_reader = csv.DictReader(csv_content)

        # 將 CSV 轉換為列表並重新映射欄位
        events = []
        for row in csv_reader:
            event = {
                "id": row.get("﻿\"id\"", "").strip('"'),  # 移除多餘的引號
                "活動名稱": row.get("title", ""),
                "活動起始日期": row.get("activeDate", ""),
                "活動結束日期": row.get("activeEndDate", ""),
                "簡介說明": row.get("description", ""),
                "活動類別": row.get("className", ""),
                "主辦單位": row.get("author", ""),
                "活動場地": row.get("place", ""),
                "場地電話": row.get("placeTel", ""),
                "地址": row.get("address", ""),
                "交通說明": row.get("traffic", ""),
                "相關連結": row.get("aboutUrl", ""),
                "圖片連結": row.get("picUrl", "")
            }
            events.append(event)

        # 建立固定名稱的輸出目錄
        output_dir = "newtaipei_api"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 儲存完整資料（檔名包含時間戳記）
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_file = os.path.join(
            output_dir, f"新北市政府近期活動_{timestamp}.json")
        with open(output_file, "w", encoding="utf-8-sig") as f:
            json.dump(events, f, ensure_ascii=False, indent=2)

        print(f"成功獲取 {len(events)} 筆活動資料")
        print(f"資料已儲存至: {output_file}")

        # 將資料轉換為標準格式
        formatted_data = {
            "result": [],
            "queryTime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total": len(events),
            "limit": len(events),
            "offset": 0
        }

        for event in events:
            formatted_event = {
                "uid": event["id"],
                "title": event["活動名稱"],
                "description": event["簡介說明"],
                "organizer": event["主辦單位"],
                "address": event["地址"],
                "startDate": convert_date_format(event["活動起始日期"]),
                "endDate": convert_date_format(event["活動結束日期"]),
                "location": event["活動場地"],
                "latitude": None,  # 新北市的資料沒有經緯度資訊
                "longitude": None,
                "price": "",  # 新北市的資料沒有價格資訊
                "url": event["相關連結"],
                "imageUrl": event["圖片連結"]
            }
            formatted_data["result"].append(formatted_event)

        return formatted_data

    except requests.exceptions.RequestException as e:
        print(f"獲取資料時發生錯誤: {e}")
        return {"result": []}
    except csv.Error as e:
        print(f"處理 CSV 資料時發生錯誤: {e}")
        return {"result": []}
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")
        return {"result": []}


if __name__ == "__main__":
    fetch_newtaipei_events()
