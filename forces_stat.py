import requests

def forces_stat(usernames):
    users_data = []
    leaderboard = []
#   leaderboard.append("Username       | wpm | acc | secs|")
    leaderboard.append("Username       | rating  | rank    |")
    leaderboard.append("---------------|---------|---------|")  

    for username in usernames:
        rating = 0
        ranking = "None"
        url = f"https://codeforces.com/api/user.info?handles={username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data["status"] == "OK":
                user_info = data["result"][0]
                rating = user_info.get("rating", 0)
                ranking = user_info.get("rank", "None")
            else:
                continue
        else:
            print(f"unable to fetch username: {username}")
            continue
        
        users_data.append((username, rating, ranking))

    # Sort users by typing speed in descending order for ranking
    sorted_users = sorted(users_data, key=lambda x: (x[2]), reverse=True)
    # Add each user's data to the leaderboard
    for rank, user in enumerate(sorted_users, start=1):
        name, rating, ranking = user
        if rating == 0 : rating = "Unrated"
        row = f"{rank:<2} {name[:11]:<11} | {rating:<7} | {ranking:<7} |"
        leaderboard.append(row)

    result = "👨‍💻   🏆   `CODEFORCES LEADERBOARD`   🏆   👩‍💻\n\n"
    result += "```\n" 
    result += "\n".join(leaderboard)
    result += "\n```" 
    result +="\nTo appear on the leaderboard, please `reply to this message with your codeforces username`. Congratulations to everyone who has already submitted their usernames—keep up the great work and keep improving your Coding and Math skills! `Happy Coding!` 👩‍💻👨‍💻\n"
    return result
