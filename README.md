# RIO Slack Leaderboards

## 📌 Overview
This repository contains the logic for managing **Rwanda Informatics Olympiad (RIO) leaderboards** on Slack. It provides a way to track and display rankings, making it easier for participants and organizers to monitor progress and promote friendly competitions.

## 🚀 Features
- 🏆 **Dynamic Leaderboards**: Fetch and update rankings in real time.
- 🔄 **Slack Integration**: Automatically send leaderboard updates to Slack channels.
- ⚙️ **Customizable**: Easily extend to add new leaderboards or modify ranking criteria.
- 🔍 **Open Source**: Contributions are welcome!

## 📂 Project Structure
```
📦 rio_slack
 ┣ 📂 usernames                 # Folder which holds usernames' files
    ┣ 📂 codeforces             # Folder which holds codeforces usernames' files   
        ┣ 📜 coaches.txt        # Document which includes coaches' usernames
        ┣ 📜 students-2024.txt  # Document which includes students-2024' usernames
    ┣ 📂 monkeytype             # Folder which holds monkeytype usernames' files   
        ┣ 📜 coaches.txt        # Document which includes coaches' usernames
        ┣ 📜 students-2024.txt  # Document which includes students-2024' usernames
 ┗ 📜 bot.py                    # Entry point
 ┗ ⚙  data.conf                 # For showing sample formats of jsons provided by API's
 ┗ 📜 forces_stat.py            # Ranking function of codeforces users
 ┗ 📜 forces.py                 # For getting usernames, slack bot, and ranking function of codeforces users
 ┗ 📜 monkey_stat.py            # Ranking function of monkeytype users
 ┗ 📜 monkeys.py                # For getting usernames, slack bot, and ranking function of monkeytype users
 ┗ 📜 requirements.txt          # File that includes required libraries
 ┣ 📜 README.md                 # This document
```

## 🛠 Installation
### Prerequisites
- Python 3.x
- A Slack App with necessary permissions

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/demavros/rio_slack.git
   cd rio_slack
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Configure environment variables:
   - Copy the example file and update it with your credentials:
     ```sh
     cp .env.example .env
     ```
   - Open `.env` and set your values:
     ```ini
     MONKEYS_TOKEN=monkeytype-bot-token
     CODEFORCES_TOKEN=codeforces-bot-token
     COEACHES_ID=coaches channel ID
     STUDENTS_2024_ID=students-2024 channel ID
     BASE_PATH=full path to rio_slack folder
     ```
4. You need to create and populate the usernames' folder. For privacy reasons, this folder is hidden within the repository.

## 🚀 Usage
Run the leaderboard update script:
```sh
python3 bot.py
```

## 🤝 Contributing
We welcome contributions! If you want to add new leaderboards or improve existing ones:
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to your branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License
This project is licensed under the MIT License.

## 📞 Contact
For questions or suggestions, feel free to open an issue or reach out on RIO Slack!
