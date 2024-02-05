import requests
import json

response = requests.get('https://mouban.mythsman.com/guest/user_book?id=231261343&action=collect')  # 替换为你的URL
data = json.loads(response.text)

def remove_spaces_and_newlines(input_string):
    input_string = input_string.replace("-", "/")
    return input_string

num = 0

for comment in data["result"]["comment"]:
    douban_id = comment["item"]["douban_id"]
    title = comment["item"]["title"]
    author = comment["item"]["author"]
    mark_date = remove_spaces_and_newlines(comment["mark_date"])
    rate = comment["rate"]
    thumbnail = comment["item"]["thumbnail"]
    if num == 0:
        print(f"- class_name: 📖 书籍清单\n  class_desc: 静下来慢慢感受着，流淌的故事。\n  link_list: \n    - name: {title}\n      score: {rate}\n      premiere: {author}\n      time: {mark_date}\n      img: {thumbnail}\n      link: https://book.douban.com/subject/{douban_id}/\n")
    # if num == 3:
    #     break
    if num != 0:
        print(f"    - name: {title}\n      score: {rate}\n      premiere: {author}\n      icon: fa-solid fa-book-bookmark\n      time: {mark_date}\n      img: {thumbnail}\n      link: https://book.douban.com/subject/{douban_id}/\n")
    num += 1
