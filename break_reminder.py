#!/usr/bin/env python3s

import time
import datetime
from plyer import notification


if __name__ == '__main__':
    while(True):

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
        print('\007')
        notification.notify(
            title = 'GET BACK TO WORK',
            message = str(datetime.datetime.now()) + (datetime.datetime.now() + datetime.timedelta(minutes=30)).strftime('%H:%M:%S'),
            #displaying time
            timeout = 2
        )

        # sleep for 30 minutes
        time.sleep(60 * 30)
