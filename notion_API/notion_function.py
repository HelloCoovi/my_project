import requests, json
import numpy as np
import pandas as pd


def read_database(database_id, token):
    """
    데이터베이스id의 정보를 받고 리턴해주는 함수,
    아래 with open 코드의 주석을 해제하면 받아온 정보를 json으로 저장해서 확인할수 있다.
    (디버깅 or 새로운 코드 적용시 사용)
    """
    headers = {
        "Authorization": "Bearer " + token,
        "Notion-Version": "2022-06-28"
    }
    read_url = f"https://api.notion.com/v1/databases/{database_id}/query"

    res = requests.request("POST", read_url, headers=headers)
    data = res.json()
    print(res.status_code)

    # json 파일 확인용 저장 코드(실행시 db.json으로 파일 생성)
    # with open("./db.json", "w", encoding="utf8") as f:
    #     json.dump(data, f, indent=2, ensure_ascii=False)

    if res.status_code == 200:
        # try:
        col_value = list(data["results"][0]["properties"].keys())
        print("데이터 조회에 성공했습니다.")

        for i in col_value:
            if "title" in data["results"][0]["properties"][i]:
                title = i

        print(f"총 열 갯수는 {len(col_value)}개 이며 각 항목의 이름은")
        print(f"{', '.join(col_value)} 입니다.")
        print(f"이 중 제목 유형은 '{title}' 입니다.")

        col_value.remove(title)
        col_value.insert(0, title)

        # pd.DataFrame(np.arange(1, 26).reshape(5, 5),
        #              columns=col_value)

        # np.append(배열, 값(배열), axis)

        row = []

        for i in data["results"]:
            for j in col_value:
                row_data = i["properties"][j]
                if row_data["type"] == "title":
                    row.append(row_data["title"][0]["text"]["content"])
                elif row_data["type"] == "email":
                    row.append(row_data["email"])
                elif row_data["type"] == "date":
                    row.append(row_data["date"]["start"])
                # elif row_data["type"] == "status":
                #     print(row_data["status"]["name"])
                #     print(type(row_data["status"]["name"]))
                #     row.append(row_data["status"]["name"])
                elif row_data["type"] == "select":
                    row.append(row_data["select"]["name"])
                elif row_data["type"] == "multi_select":
                    row.append(row_data["multi_select"][0]["name"])
                elif row_data["type"] == "files":
                    try:
                        row.append(row_data["files"][0]["name"])
                        # row.append(row_data["files"][0]["name"],
                        #            row_data["files"][0]["file"]["url"])
                    except:
                        row.append(None)
                elif row_data["type"] == "number":
                    row.append(row_data["number"])
                elif row_data["type"] == "rich_text":
                    row.append(row_data["rich_text"][0]["text"]["content"])
                elif row_data["type"] == "people":
                    row.append(row_data["people"][0]["name"])
                elif row_data["type"] == "phone_number":
                    row.append(row_data["phone_number"])
                elif row_data["type"] == "checkbox":
                    if row_data["checkbox"] == True:
                        row.append("✓")
                    elif row_data["checkbox"] == False:
                        row.append("")
                elif row_data["type"] == "url":
                    row.append(row_data["url"])

        print(row)
        # 배열로 변환
        # arr = np.arange(row)
        # shape 출력
        # print(arr.shape)
        # shape 변환
        #   ㅓ

        # for i in key_data:
        #     col1 = i["properties"]["이름"]["title"][0]["text"]["content"]
        #     col2 = i["properties"]["역할"]["rich_text"][0]["text"]["content"]
        #     print(f"{col1} 소속: {col2}")

        # except:
        #     print(f"status code가 200이 아닙니다 현재 status code: {res.status_code}")
