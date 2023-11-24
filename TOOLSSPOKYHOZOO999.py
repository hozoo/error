import sys

try:

    print('')
except SyntaxError as e:
    if e == True:
        print("Hey Idiot, Use python3.")   
import time
print("Please Wait.. The Tools Is Loading Assets..")
time.sleep(1)
try:
    print("Checking For Module..")
except ModuleNotFoundError as e:
    if e == True:
        print('Module Not Found: ', (e))
        
import time
import os
from os.path import exists
import googlesearch #googlesearch-python
import wget #wget
import urllib.request #urllib
import colorama
from threading import Thread, Lock #threading2
from subprocess import Popen, PIPE
from signal import SIGINT, signal
import scapy #scapy
from colorama import Fore, Style, init
import random
import socket
import requests
import sys
from googlesearch import search
from subprocess import getoutput
from urllib.parse import urlparse
import argparse
import ipaddress
import faker
from faker import Faker
from bs4 import BeautifulSoup
import re
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
from pythonping import ping
import exiftool
import importlib
red = '\033[1;91m'

white = '\033[37m'

green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
red_t = '\033[0;31;40m'
gray = '\033[1;37;40m'

package_name = "adafruit"

try:
    pass
except ImportError or ModuleNotFoundError:
    importlib.import_module(package_name)
    print(info + f"[ + ] Downloading adafruits ! [ + ]")
    os.system('pip3 install adafruit-io')
    os.system('pip install adafruit-circuitpython-adafruitio')
    os.system('pip install adafruit-circuitpython-motor')
    os.system('pip install adafruit-circuitpython-circuitplayground')

print(f"""
{red}          
                                                       ⣀⣠⣤⡶⠶                ⠲⠶⣤⣤⣄⣀       
                                                ⢀⣠⣶⣿⣿⠟⠉                     ⠙⠻⡿⣿⣦⣄    
                                               ⣰⣿⣿⢏⡔⠁                         ⠘⢎⠻⣿⣷⡄  
                                              ⣰⣿⣻⠃⡞                            ⠈⡇⢹⣿⣿⡄ 
                                            ⢰⣿⣟⡗ ⡇                             ⣿⠐⣛⣿⣿ 
                                           ⢸⣿⣿⡓ ⢳⡀        ⣀⣀     ⠠⢄⣀⡀        ⣰⠇⠐⣻⣿⣿⡆
                                         ⢸⣿⣿⡷⠖⠋⠻⣄  ⣀⣤⠶⠚⠉⠁         ⠈⠙⠲⢦⣄⡀ ⢀⣴⠏⠈⠲⢿⣿⣿⠇
                                           ⠸⣿⣿⣿⣧⠞⠁⠈⠻⢾⣏                  ⠈⣻⡷⠋⡁⠈⢦⣾⣿⣿⣿ 
                                            ⠹⣿⣿⣷⣷⡴⠃  ⡿                   ⣧  ⠱⣴⣷⣯⣿⡿⠃ 
                                            ⠙⢿⣿⣯⣾⣿⢗⣼⠃                   ⠹⣦⢾⣿⣮⣿⣿⠟⠁  
                                             ⣽⣿⣿⡿⠟⠁                     ⠘⠳⣽⣿⣿⡍    
                                            ⢀⣿ ⣀                          ⢀⡠⢸⣇    
                                           ⢸⡇ ⠘⣄                         ⡜  ⣿    
                                          ⠘⣇ ⢄⣿⡰⡄                     ⡴⢸⣇ ⢀⡟    
                                             ⣿ ⣾⣿⠇⠹⣶⣤⣀⣀ ⠙⢶⣤⡀   ⣠⣴⠖⠉⢀⣀⣠⣴⡾⠁⢿⣿⡆⢸⡇    
                                            ⢸⡀⣿⠏⢠⣾⣿⣿⣿⣿⣿⣦⡀⠹⡿  ⠸⡿⠁⣤⣾⣿⣿⣿⣿⣷⣦ ⢿⡇⡸     
                                            ⢧⢿⡀⢸⣿⣿⣿⣿⣿⣿⣿⡟⠆     ⠞⣿⣿⣿⣿⣿⣿⣿⣿ ⣸⢧⠇     
                                            ⠈⢈⡷⠈⢿⣿⣿⣿⣿⣿⣿⡇  ⣠⣤⡀  ⣿⣿⣿⣿⣿⣿⣿⠃ ⣏⠈      
                                            ⢀⡆   ⠙⠻⠿⠿⠿⠟⠁ ⢠⣿⣿⣧  ⠙⠿⠿⠿⠿⠛⠁   ⣆      
                                             ⢸⡄          ⢀⣾⣿⢻⣿⣆           ⣸      
                                            ⠘⢷⣄⡀        ⢾⣿⡿⢸⣿⣿⠆        ⣀⣴⡟      
                                            ⠈⠙⠛⢛⣿⣿⣿⡖⠦⡀  ⠉⠁ ⠉⠁  ⢠⠖⣾⣿⣿⣿⠛⠛⠉       
                                              ⠘⡇⣿⢻⣿⣴⣠⢀ ⡄ ⡀⢀⡄⢀⣀⣼⣼⣿⠹⡇⡟          
                                              ⡀⠧⡇⢸⣿⣿⡇⢹⠒⡟⠙⡟⠉⡗⢹⠁⣿⣿⣿ ⡧⠇⡀         
                                             ⢱  ⠘⢿⣹⠛⠼⣦⣿⣄⣧⣀⣷⣾⠴⢻⣸⠟  ⢠⡇         
                                              ⠘⢧⡀  ⠊⠳⠧⣼⣠⣤⣧⣱⣸⡦⠷⠚⠃  ⣠⠟          
                                               ⠈⠲⣤⡀   ⠈  ⠈    ⣠⡴⠋⠁           
                                                 ⠙⢿⣦        ⢀⣾⡟⠁             
                                                ⠈⠻⢷⣄⣠⣴⣶⣤⣄⣰⠿⠋               
                                                     ⠈⠉⠉⠉
                                   ██╗░░██╗░█████╗░███████╗░█████╗░░█████╗░
                                  ██║░░██║██╔══██╗╚════██║██╔══██╗██╔══██╗
                                 ███████║██║░░██║░░███╔═╝██║░░██║██║░░██║
                                ██╔══██║██║░░██║██╔══╝░░██║░░██║██║░░██║
                               ██║░░██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝
                               ╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░

""")


time.sleep(0.2)

 #Whoever Recode This Project, You Are Fuck Ass Kid

time.sleep(0.2)
print(info + f'            [ ]Remember !, If The Tools Had A Error, Please Waiting For The Update.[ ]')
print(f"""{red}┌─────────────────────────────────────────────────────────────────────────────────────────────────┐{blue}
{red}│{red} [01] SPAM WHATS APP SMS 
{red}│{red} [02]
{red}│{red} [03]
{red}│{red} [04]
{red}│{red} [05]
{red}│{red} [06]
{red}│{red} [07]
{red}│{red} [08]
{red}│{red} [09]
{red}│{red} [10]
{red}│{red} [11]
{red}│{red} [11]
{red}└─────────────────────────────────────────────────────────────────────────────────────────────────┘{red}
""")    
print('')

print(f'\033[37m')

print(f"╭─[{yellow} SPOKYHOZOO@localhost {white} ~/home")
answer = input("╰─$ ")
print('\033[1;32m\n')
if answer == ("1"):
mport sys          # Untuk fungsi pada terminal, seperti autoketik() dan exit()
import subprocess   # Installing python module within code / script (Tanpa requirements.txt)

try: # Import Module
    import requests # Post, Get, & Put URL API
    import time     # Untuk informasi waktu
    import random   # Untuk random user
    import os       # Untuk "clear" terminal
    import urllib3  # HTTP client untuk Python
    import json     # Agar body requests dapat dilihat dengan cara di print
    import bs4      # Untuk variasi output
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'urllib3'])
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'bs4'])
finally:
    import requests # Post, Get, & Put URL API
    import urllib3  # HTTP client untuk Python
    from bs4 import BeautifulSoup as bs
    
from urllib3.exceptions import *
from bs4 import BeautifulSoup as bs
from pip._vendor.requests import post,get # Bisa langsung "from requests import post,get"

# Inisialisasi Variasi Warna Output Terminal.
hijau   =   "\033[1;92m"
putih   =   "\033[1;97m"
abu     =   "\033[1;90m"
kuning  =   "\033[1;93m"
ungu    =   "\033[1;95m"
merah   =   "\033[1;91m"
biru    =   "\033[1;96m"

# Function ini berfungsi sebagai pengganti print(), agar lebih menarik saat terlihat di terminal.
def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.050)

# Function ini berfungsi sebagai informasi waktu saat pengiriman spam berlangsung.
def countdown(time_sec):
        mins, secs = divmod(time_sec,60)
        timeformat = '\033[1;97m[\033[1;93m•\033[1;97m] Silakan Menunggu Dalam Waktu \033[1;92m{:02d}:{:02d}'.format(mins,secs)
        waktu = time.localtime()
        keterangan_jam = time.strftime("%H:%M:%S", waktu)
        keterangan_tanggal = time.strftime("%d",waktu)
        keterangan_bulan = time.strftime("%B",waktu)

        bulan_bulan = {

        "January"    : 'Januari',
        "February"   : "Februari",
        "March"      : "Maret",
        "April"      : "April",
        "May"        : "Mei",
        "June"       : "Juni",
        "July"       : "Juli",
        "August"     : "Agustus",
        "September"  : "September",
        "October"    : "Oktober",
        "November"   : "November",
        "December"   : "Desember"
        } # Mengubah keterangan bulan menjadi bahasa Indonesia.
        bulan = bulan_bulan.get(keterangan_bulan)
        
        keterangan_tahun = time.strftime("%Y",waktu)

        keterangan_hari = time.strftime("%A",waktu)
        hari_hari = {
        "Sunday"    : 'Minggu',
        "Monday"    : "Senin",
        "Tuesday"   : "Selasa",
        "Wednesday" : "Rabu",
        "Thursday"  : "Kamis",
        "Friday"    : "Jum'at",
        "Saturday"  : "Sabtu"
        } # Mengubah keterangan hari menjadi bahasa Indonesia.
        hari = hari_hari.get(keterangan_hari)
        print(f"{timeformat} | {biru}{hari}, {keterangan_tanggal} {bulan} {keterangan_tahun} | {kuning}Waktu {keterangan_jam}",end='\r')

        time.sleep(1)

        time_sec -= 1

def tanya(nomor):
    check_input = 0
    while check_input == 0:            
        a = input(f"""{merah}Apakah Anda ingin mengulangi Spam Tools? y/t 
{putih}Input Anda: {hijau}""")
        if a == "y" or a == "Y":
            check_input = 1
            start(nomor,1)
            break
        elif a == "t" or a == "T":
            check_input = 1
            autoketik(f"{hijau}Berhasil Keluar Dari Tools")
            sys.exit()
            break
        else:
            print ("Masukkan Pilihan Dengan Benar")
            sys.exit

def jam(nomor): # Don't Remove Code !!!!
        autoketik("Program Berjalan!")
        b       =   nomor[1:12] # Contoh: nomor = 89508226367
        c       =   "62" + b    # Contoh: nomor = 6289508226367
        rto     =   0           # Flag ketika memasuki RTO maka akan program akan otomatis menunda proses selama 80 detik
        RTO_flag = 0
        for _ in range(10): # Looping
            try: # requests yang dikomen dapat dibuka komennya sesuai dengan kondisi error (Baca README.md)
                # Tokopedia                             =  requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'User-Agent' : "Mozilla/5.0 (Linux; Android 5.1.1; SM-G600S Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",'Accept-Encoding' : 'gzip, deflate','Connection' : 'keep-alive','Origin' : 'https://accounts.tokopedia.com','Accept' : 'application/json, text/javascript, */*; q=0.01','X-Requested-With' : 'XMLHttpRequest','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8'}, data = {"otp_type" : "116","msisdn" : nomor,"tk" : re.search(r'\<input\ id=\"Token\"\ value=\"(.*?)\"\ type\=\"hidden\"\>', requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn='+nomor+'&ld=https%
        
        
  