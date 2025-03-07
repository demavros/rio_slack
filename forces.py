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

    force_users = {
    # coaches users
        "coaches": 
        {
            "users": 
            [
                "Hirwa",
                "koseko",
            ],
            "channel_id": "C08GB4T7QS2",
        },
    # students users
        "students-2024": 
        {
            "users":
            [
                "HappyDavid",
                "Eze_chiel",
                "koseko",
                "mugishabarnabee",
                "Hirwa"
            ],
            "channel_id": "C08GB4T7QS2"
        }
    }

    return force_users, force_client, forces_stat
