import requests

def execute():
    print('コマンドが実行されました')
    responese = requests.get('https://www.google.com/')
    print(responese.status_code)