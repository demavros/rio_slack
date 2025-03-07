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
                # 'hirwa_arnold',
                "Alice_U",
                "BroJeid",
                "NNORBERT",
                "kagaba",
                "Ishimwefrank",
                "Ink6",
                "Hakim",
                "afsau",
                "ucynthia",
                "JOVz19",
                "JdFils",
                "Ndevu",
                "koseko",
                "aruns1",
                "hirwarnold",
            ],
            "channel_id": "C08GB4T7QS2",
        },
    # students users
        "students-2024": 
        {
            "users":
            [
                "HappyDavid",
                "divin_d1",
                "GanzaMike",
                "hirwarnold",
                "BrianMuhizi",
                "eiran",
                "shamimelissa",
                "DariusNiyonkuru",
                "Bernise_n4",
                # "aruns1",
                "TDPrince",
                "mugisha_pacific",
                "elhumura",
                "Isaac_Precieux",
                "Reyne",
                "koseko",
                "Joyau",
                "MUGEMA",
                "byiringiro_aloys",
                "lucky_king",
                "ishimweirene",
                "Nelson",
                "MwizerwaNelson",
                "bertin_muhirwa",
                "ngabofreddy233",
            ],
            "channel_id": "C08GB4T7QS2"
        }
    }


    return monkey_users, monkey_client, monkey_stat
