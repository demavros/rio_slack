import requests

def monkey_stat(usernames):
    users_data = []
    leaderboard = []
    leaderboard.append("Username        | wpm | acc | secs|")
    leaderboard.append("----------------|-----|-----|-----|")  
    for username in usernames:
        response = requests.api.get(f"https://api.monkeytype.com/users/{username}/profile")
        if response.status_code == 200:
            data = response.json()
        else:
            print(f"unable to fetch username: {username}")
            continue
        
        name = data['data']['name']
        bests = data['data']['personalBests']['time']

        max_s = 0
        acc = 0
        tm = 0

        for t, values in bests.items():
            if int(t) < 30: continue
            for val in values:
                speed = val['wpm']
                if speed > max_s:
                    max_s = speed
                    acc = val['acc']
                    tm = t
        users_data.append((name, round(max_s), round(acc), tm))

    # Sort users by typing speed in descending order for ranking
    sorted_users = sorted(users_data, key=lambda x: (x[1], x[2]), reverse=True)
    # Add each user's data to the leaderboard
    for rank, user in enumerate(sorted_users, start=1):
        username, speed, accuracy, time_taken = user
        row = f"{rank:<2} {username:<12} | {speed:<3} | {accuracy:<3} | {time_taken:<4}|"
        leaderboard.append(row)

    result = "🏆      `TYPING SPEED LEADERBOARD`      🏆\n\n"
    result += "```\n" 
    result += "\n".join(leaderboard)
    result += "\n```" 
    result += "\nTo appear on the leaderboard, please `reply to this message with your Monkeytype username`. Congratulations to everyone who has already submitted their usernames—keep up the great work and keep improving your typing speed! `Happy Typing!` ⌨️ \n"
    return result
