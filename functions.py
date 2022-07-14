import time
import requests
import numpy as np
import pandas as pd
from random import choice



#randomize the useragent credentials
def get_headers():
   ua = ["Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36",
       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
   ]
   headers = {
       "User-Agent": choice(ua),
       "Accept": "*/*",
       "Accept-Encoding": "gzip, deflate",
       "Accept-Language": "en-en,en;q=0.8,en-US;q=0.6,en;q=0.4,uk;q=0.2",
       "Connection": "keep-alive",
   }


#connection check - returns the website's response if the connection is up
def get_connection(url):
    retry = 3
    while retry:
        try:
            r = requests.get(url, headers=get_headers())

        except Exception as e:
            retry -=1
            if retry:
                time.sleep(0.5)
                continue
            else: 
                print(f"Bad connection : {e}")
                pass
        # connection ok
        else: 
            if r.ok:
                return r
                break
            else:   
                print(r.status_code)
