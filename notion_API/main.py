import requests, json

token = "secret_cALvUPsYarLSYBn4TKTMd7zfodIgHPMl5M8AMscAmjx"

database_id = "8ee490e3938c418e961b1cd5eecc43a8"

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2022-06-28"
}

def read_database(database_id, headers):
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"

    res = requests.request("POST", read_url, headers=headers)
    data = res.json()
    print(res.status_code)

    # json 파일 확인용 저장 코드(실행시 db.json으로 파일 생성)
    # with open("./db.json", "w", encoding="utf8") as f:
    #     json.dump(data, f, indent=2, ensure_ascii=False)

    if res.status_code == 200:
        try:
            for i in data["results"]:
                col1 = i["properties"]["이름"]["title"][0]["text"]["content"]
                col2 = i["properties"]["역할"]["rich_text"][0]["text"]["content"]
                print(f"{col1} 소속: {col2}")

        except:
            print(f"status code가 200이 아닙니다 현재 status code: {res.status_code}")

def create_page():
    pass

def update_page():
    pass


read_database(database_id, headers)
