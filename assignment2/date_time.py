from datetime import datetime

import pytz

today = datetime.today()
# print(today)
t = today.strftime("%d-%m-%Y and %I:%M:%p")
print(t)

# now = datetime.now(pytz.timezone('Asia/Kolkata'))
# current_time = now.strftime("%I:%M %p")
# print(f"current date: {t}\ncurrent time: {current_time}")
