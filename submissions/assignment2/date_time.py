from datetime import datetime, date, time

import pytz

today = date.today()
t = today.strftime("%d-%m-%Y")
now = datetime.now(pytz.timezone('Asia/Kolkata'))
current_time = now.strftime("%I:%M %p")
print(f"current date: {t}\ncurrent time: {current_time}")
