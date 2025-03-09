import slack
import os
from pathlib import Path
from dotenv import load_dotenv
from forces_stat import forces_stat

def get_forces():
    # codeforces bot
    load_dotenv()
    force_token=os.environ['CODEFORCES']
    force_client = slack.WebClient(token=force_token)
    COACHES_ID = os.environ['COACHES_ID']
    STUDENTS_ID = os.environ['STUDENTS_ID']

    coaches = []
    with open("./usernames/codeforces/coaches.txt", "r") as f:
        coaches = [c.strip() for c in f]
    
    students_2024 = []
    with open("./usernames/codeforces/students-2024.txt", "r") as f:
        students_2024 = [s.strip() for s in f]

    force_users = {
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

    return force_users, force_client, forces_stat
