# 보일러플레이트를 이용하여 URL을 입력받아 온라인 상태인지 아닌지 체크하는 프로그램
import os
import requests

while True:
    os.system('cls')
    print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")

    url_input = input()
    url_list = url_input.split(',')

    for url in url_list:
        url = url.strip()
        if not"." in url:
            print(f"{url} is not a valid URL.")
        else:
            if not("http://" in url or "https://" in url):
                url = f"http://{url}"
            try:
                r = requests.get(url)
                if r.status_code < 300:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url} is down!")

    while True:
        restart = input("Do you want to start over? y/n ")
        if restart is "n":
            print("k. bye!")
            quit()
        elif restart is "y":
            break
        else:
            print("That's not a valid answer.")
