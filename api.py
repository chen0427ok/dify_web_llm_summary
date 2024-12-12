import requests

# API 相關資訊
url = "https://api.dify.ai/v1/workflows/run"
api_key = "app-HO3yyLOcKiOKfUWD1iLUsWCq"  # 你的 API Key

# 設定 headers，包括 Authorization
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 要摘要的網址
url_to_summarize = "https://edition.cnn.com/2024/11/04/business/americans-homebuying-richer/index.html"  

# 設定 payload，根據 API 文件
payload = {
    "inputs": {
        "url": url_to_summarize
    },
    "response_mode": "blocking",  # 或 "streaming"，根據需要選擇
    "user": "unique_user_id"  # 用戶的唯一識別符，可自定義
}

# 進行 API 請求 (POST 請求)
response = requests.post(url, headers=headers, json=payload)

# 檢查回應結果
if response.status_code == 200:
    result = response.json()
    if 'data' in result and 'outputs' in result['data']:
        summary = result['data']['outputs']
        print("成功取得摘要:")
        print(summary)
    else:
        print("回應中沒有找到摘要資料:", result)
else:
    print(f"請求失敗，狀態碼: {response.status_code}，訊息: {response.text}")
