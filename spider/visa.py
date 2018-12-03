import requests
import time
import traceback
from say import notice_me
from say import tips


url = "https://www.vfsvisaservice.com/DIAC-China-Appointment_new_test/AppScheduling/AppWelcome.aspx?p=Gta39GFZnstZVCxNVy83zTlkvzrXE95fkjmft28XjNg="
#url = "https://www.baidu.com"

success_counter = 0

for i in range(10000):
    try:
        r = requests.get(url)
    except:
        print(traceback.format_exc())
    else:

        if r.status_code == 200:
            success_counter = success_counter + 1
            for i in range(success_counter):
                notice_me()
                    

    print("Try again .....{} times || success time {}".format(i, success_counter))
    time.sleep(1)
    #tips()
