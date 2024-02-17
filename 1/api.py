import requests

# 替换为你的API密钥和终结点
api_key = "your_api_key"
endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/search"

# 设置请求参数
params = {
    "q": "Microsoft",
    "count": 5,
    "offset": 0,
    "mkt": "en-US",
    "safesearch": "Moderate",
}

# 添加API密钥到请求头
headers = {
    "Ocp-Apim-Subscription-Key": api_key,
}

# 发送请求并获取响应
response = requests.get(endpoint, headers=headers, params=params)
response.raise_for_status()
search_results = response.json()

# 输出搜索结果
for result in search_results["webPages"]["value"]:
    print(result["name"])
