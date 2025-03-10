import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from monkey_stat import monkey_stat

def get_monkeys():
    # monkeytype bot
    load_dotenv()
    monkey_token=os.environ['MONKEYS']
    monkey_client = slack.WebClient(token=monkey_token)

    COACHES_ID = os.environ['COACHES_ID']
    STUDENTS_ID = os.environ['STUDENTS_ID']
    BASE_PATH = os.environ['BASE_PATH']

    coaches = []
    with open(f"{BASE_PATH}/usernames/monkeytype/coaches.txt", "r") as f:
        coaches = [c.strip() for c in f]
    
    students_2024 = []
    with open(f"{BASE_PATH}/usernames/monkeytype/students-2024.txt", "r") as f:
        students_2024 = [s.strip() for s in f]

    monkey_users = {
    # coaches users
        "coaches": 
        {
            "users": coaches,
            "channel_id": COACHES_ID,
        },
    # students users
        "students-2024": 
        {
            "users": students_2024,
            "channel_id": STUDENTS_ID
        }
    }

    return monkey_users, monkey_client, monkey_stat
