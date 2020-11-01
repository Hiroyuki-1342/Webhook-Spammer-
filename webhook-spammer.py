from dhooks import Webhook
from pynput.keyboard import Listener
import time
import os
from colorama import Fore, Back, Style
from colorama import init as cinit
import platform
os.system('cls')
os.system('title Webhook-Spammer by Hiroyuki#2173')

print(Fore.RED + """

 █     █░ ▓█████ ▄▄▄▄     ██░ ██  ▒█████   ▒█████   ██ ▄█▀      ██████  ██▓███   ▄▄▄      ███▄ ▄███▓ ███▄ ▄███▓ ▓█████ ██▀███  
▓█░ █ ░█░ ▓█   ▀▓█████▄ ▒▓██░ ██ ▒██▒  ██▒▒██▒  ██▒ ██▄█▒     ▒██    ▒ ▓██░  ██ ▒████▄   ▓██▒▀█▀ ██▒▓██▒▀█▀ ██▒ ▓█   ▀▓██ ▒ ██▒
▒█░ █ ░█  ▒███  ▒██▒ ▄██░▒██▀▀██ ▒██░  ██▒▒██░  ██▒▓███▄░     ░ ▓██▄   ▓██░ ██▓▒▒██  ▀█▄ ▓██    ▓██░▓██    ▓██░ ▒███  ▓██ ░▄█ ▒
░█░ █ ░█  ▒▓█  ▄▒██░█▀   ░▓█ ░██ ▒██   ██░▒██   ██░▓██ █▄       ▒   ██▒▒██▄█▓▒ ▒░██▄▄▄▄██▒██    ▒██ ▒██    ▒██  ▒▓█  ▄▒██▀▀█▄  
░░██▒██▓ ▒░▒████░▓█  ▀█▓ ░▓█▒░██▓░ ████▓▒░░ ████▓▒░▒██▒ █▄    ▒██████▒▒▒██▒ ░  ░▒▓█   ▓██▒██▒   ░██▒▒██▒   ░██▒▒░▒████░██▓ ▒██▒
░ ▓░▒ ▒  ░░░ ▒░ ░▒▓███▀▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒    ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░▒▒   ▓▒█░ ▒░   ░  ░░ ▒░   ░  ░░░░ ▒░ ░ ▒▓ ░▒▓░
  ▒ ░ ░  ░ ░ ░  ▒░▒   ░   ▒ ░▒░ ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░    ░ ░▒  ░  ░▒ ░     ░ ░   ▒▒ ░  ░      ░░  ░      ░░ ░ ░    ░▒ ░ ▒ 
  ░   ░      ░   ░    ░   ░  ░░ ░░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░     ░  ░  ░  ░░         ░   ▒  ░      ░   ░      ░       ░    ░░   ░ 
    ░    ░   ░   ░        ░  ░  ░    ░ ░      ░ ░  ░  ░             ░                 ░         ░          ░   ░   ░     ░     

 
     """ + Fore.RED)

print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Welcome To The"+Fore.LIGHTGREEN_EX+" Webhook-Spammer ")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Version: "+Fore.LIGHTGREEN_EX+"1.0")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                                         Developer: "+Fore.LIGHTGREEN_EX+"Hiroyuki#2173")
print(Style.BRIGHT + Fore.WHITE + Back.BLACK +"                         ["+Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+Style.BRIGHT + Fore.WHITE + Back.BLACK +"]"+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"-------------------------------------------------------"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"["+ Style.BRIGHT + Fore.LIGHTGREEN_EX + Back.BLACK +"+"+ Style.BRIGHT + Fore.WHITE + Back.BLACK +"]")

webhook = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " Your webhook: " + Fore.RED)
user = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " What is your webhook name: " + Fore.RED)
avatar=input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX +" Avatar: "+ Fore.RED)
say = input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " Say:" + Fore.RED)
delay = float(input(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + " Delay:" + Fore.RED))

print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Spamming...")
time.sleep(1)

if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

os.system(clearcmd)

hook = Webhook(webhook)

msg = 0
while True:
  for i in range(0,30):
    hook.send(say, username=user, avatar_url=avatar)
    time.sleep(delay)
    msg = msg + 1
    print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Message sent:"+ Fore.RED, say)
    print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Message delay:"+ Fore.RED,(delay))
    print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "+" + Fore.WHITE + "]" + Fore.LIGHTGREEN_EX + "Sending message:"+ Fore.RED, msg)

  print(Fore.WHITE + "[" + Fore.LIGHTGREEN_EX + "-" + Fore.WHITE + "]" + Fore.RED + "Please Waiting...")