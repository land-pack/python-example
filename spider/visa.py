import requests
import time
import traceback
from say import notice_me
from say import tips


url = "https://www.vfsvisaservice.com/DIAC-China-Appointment_new_test/AppScheduling/AppWelcome.aspx?p=Gta39GFZnstZVCxNVy83zTlkvzrXE95fkjmft28XjNg="

for i in range(10000):
    try:
        r = requests.get(url)
    except:
        print(traceback.format_exc())
    else:
        notice_me()
        print(r.status_code)
    print("Try again .....{} times".format(i))
    time.sleep(1)
    tips()