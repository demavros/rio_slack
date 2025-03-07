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

    monkey_users = {
    # coaches users
        "coaches": 
        {
            "users": 
            [
                'hirwa_arnold',
                "Alice_U",
                "BroJeid",
                "NNORBERT",
                "kagaba",
                "Ishimwefrank",
                "Ink6",
                "afsau",
                "JOVz19",
                "Ndevu",
            ],
            # "channel_id": "C086A1D78G6",
            "channel_id": "C08GB4T7QS2",
        },
    # students users
        "students-2024": 
        {
            "users":
            [
                "HappyDavid",
                "divin_d1"
            ],
            # "channel_id": "C086DQ2S5KP"
            "channel_id": "C08GB4T7QS2"
        }
    }

    return monkey_users, monkey_client, monkey_stat
