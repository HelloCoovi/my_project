import requests, json
from notion_function import read_database

token = "secret_cALvUPsYarLSYBn4TKTMd7zfodIgHPMl5M8AMscAmjx"
database_id = "8ee490e3938c418e961b1cd5eecc43a8"

# choice_func = input("어떤 작업을 하시겠습니까?\n 데이터를 읽으려면 'r'\n 새로운 데이터를 추가하려면 'n'\n  -> ")

# if choice_func == 'r':
#     read_database(database_id, token)

read_database(database_id, token)






def create_page(database_id, token, page_values):
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }

    created_url = "https://api.notion.com/v1/pages"

    new_page_data = {
        "parent": {"database_id": database_id},
        "properties": {
            "이름": {
                "title": [
                    {
                        "text": {
                            "content": page_values['이름']
                        }
                    }
                ]
            },
            "역할": {
                "rich_text": [
                    {
                        "text": {
                            "content": page_values['역할']
                        }
                    }
                ]
            }
        }
    }

    data = json.dumps(new_page_data)

    res = requests.post(created_url, headers=headers, data=data)

    print(res.status_code)


page_values = {
    '이름': '도지',
    '역할': '기간제 강사'
}


def update_page():
    pass

# read_database(database_id, headers)




# create_page(database_id, page_values)
