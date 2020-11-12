#!/usr/bin/env python3s

import time
import datetime
from plyer import notification

first_Time = True

if __name__ == '__main__':
    while(True):
        if first_Time:
            print('\007')
            notification.notify(
                title = 'Hello Dear, have a nice day!',
                message = 'Break at ' + (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                #displaying time
                timeout = 2
            )
            first_Time = False
        else:
            print('\007')
            notification.notify(
                title = 'GET BACK TO WORK',
                message = 'Next break at ' + (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
                #displaying time
                timeout = 2
            )
        # sleep for 30 minutes
        time.sleep(60 * 30)

        # \007 -> beep sound
        print('\007')
        notification.notify(
            title = 'TAKE A BREAK',
            message = 'Be back at ' + (datetime.datetime.now() + datetime.timedelta(minutes=5)).strftime('%H:%M:%S'),
            #displaying time
            timeout = 2
        )
        # sleep for 5 minutes
        time.sleep(60 * 5)       

