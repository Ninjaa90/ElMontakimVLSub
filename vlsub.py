import os , sys
os.system('clear')
os.system('pip install --upgrade pip')
os.system('pip install bs4')
os.system('pip install termcolor')
os.system('pip install requests')
os.system('pip install time')
os.system('pip install pyfiglet')
os.system('pip install webbrowser')
os.system('pip install --upgrade setuptools')
os.system('pip install --upgrade distribute')
import requests
import time
import os
import pyfiglet
import webbrowser
os.system('clear')
k =pyfiglet.figlet_format ("El Montakim")
print(k)
time.sleep(1)
print("       " , "="*30)
time.sleep(1)
print("Al salam Alykom ")
time.sleep(1)
print("Bism Allah")
time.sleep(1)
print("\033[;33;mEl Montakim presents :  ")
time.sleep(1)
print("\033[;31;m VLSub script")
time.sleep(1)
print("\033[1m \033[;32;m   join us on telegram")
print(" \033[1m https://t.me/ElMontakim")
time.sleep(2)
webbrowser.open('https://t.me/ElMontakim')
time.sleep(2)
print("Get the password from : ", " https://linkjust.com/AxnaYIP9Z29Qm0iii ")
time.sleep(2)
password=input("Enter The password :: ")
while password != "ElMontakim" :
    print('wrong password')
    password=input("Enter The password :: ")
time.sleep(1)
userid =input('enter your userid :: ')
time.sleep(1)
token = input('enter your token :: ')
time.sleep(1)
headers = {
    'language': 'en',
    'version': '29',
    'session':'b2dd5e8e6bd14712',
    'Content-Length': '148',
    'Host':'vlsub.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'user-agent':'Mozilla/5.0 (Linux; Android 11; SM-A705FN Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.162 Mobile Safari/537.36',
    'package':'com.vlsub',
    'id':'75fdbffe43f16cda',
    'Content-Type':'application/x-www-form-urlencoded',
}

data = {
    'userId': userid,
    'token': token,
    'reward': '1',
    'click':'0'
}
for y in range(1000):
    sec=220
    req=requests.post('https://vlsub.com/reward', headers=headers, data=data).json()
    for k , v in req.items() :
        if k =="coin":
            print("\033[;32;m you got 50 points, points now ==> \033[;37;m",v)
    for x in range(sec,0,-1):
        print("\033[;31;mwait till it is availabe again",f"{x} \r" , end=" ")
        time.sleep(1)
