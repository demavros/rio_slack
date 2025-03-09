from monkey_stat import monkey_stat
from datetime import datetime
from monkeys import get_monkeys
from forces import get_forces

current_day = datetime.now().strftime("%A")

monkeys_days = "Tuesday, Thursday, Sunday"
if current_day in monkeys_days:
    users, client, stat =  get_monkeys()
else:
    users, client, stat = get_forces() 

for user, value in users.items():
    result_string = stat(usernames=value['users'])
    print(result_string)
    client.chat_postMessage(channel=value['channel_id'], text=result_string)
