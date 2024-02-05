import requests
import json
import os

num = 0
response = requests.get('https://mouban.mythsman.com/guest/user_book?id=231261343&action=collect')  # 替换为你的URL
data = json.loads(response.text)

def remove_spaces_and_newlines(input_string):
    input_string = input_string.replace("-", "/")
    return input_string

def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"图片已保存到 {save_path}")
    else:
        print("下载失败")

for comment in data["result"]["comment"]:
    num += 1
    save_path = f"E:/Users/Pictures/UbisoftConnect/image{num}.jpg"  # 替换为你要保存图片的本地文件夹路径
    download_image(comment["item"]["thumbnail"], save_path)
    