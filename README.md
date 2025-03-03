# Web Article Summarization using Dify API

## Overview
This project implements a web article summarization tool using the Dify API. Given a URL, the script fetches the content and summarizes it automatically. The API request is made using Python's `requests` library.

## Features
- Sends a URL to the Dify API for summarization.
- Retrieves and displays the summarized content.
- Uses API authentication via an API key.
- Supports `blocking` and `streaming` response modes.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `requests` library

### Install Dependencies
```bash
pip install requests
```

## Usage

### 1. Set Up API Key and Endpoint
Modify the script with your Dify API key and the URL you want to summarize:

```python
url = "https://api.dify.ai/v1/workflows/run"
api_key = "your_api_key"  # Replace with your API Key
```

### 2. Run the Script
Execute the script to send a request and receive a summary:

```bash
python summarize.py
```

### 3. Expected Output
Upon successful execution, the script will return the summarized content:

```bash
成功取得摘要:
<summary_text>
```

If the request fails, the script will output the error message and HTTP status code.

## Code Explanation
### API Request Configuration
The script sets up an HTTP `POST` request to the Dify API with authentication headers:
```python
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
```

### Sending the Request
The script sends the URL to the API for processing:
```python
payload = {
    "inputs": {"url": url_to_summarize},
    "response_mode": "blocking",
    "user": "unique_user_id"
}
response = requests.post(url, headers=headers, json=payload)
```

### Handling the Response
If successful, the summarized text is extracted and printed:
```python
if response.status_code == 200:
    result = response.json()
    summary = result['data']['outputs']
    print("成功取得摘要:", summary)
else:
    print(f"請求失敗，狀態碼: {response.status_code}，訊息: {response.text}")
```

## Notes
- Ensure you replace `your_api_key` with a valid Dify API key.
- The API supports different response modes (`blocking` or `streaming`). Adjust `response_mode` as needed.
- If summarization fails, verify that the provided URL is accessible and contains valid content.

## License
This project is licensed under the MIT License.

