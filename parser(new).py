from bs4 import BeautifulSoup
import requests, fake_useragent
from time import sleep
line = "---------------------------------------------------------------"
ua = fake_useragent.UserAgent() 
user = ua.random
header = {'User-Agent':str(user)}
ipSite='http://icanhazip.com'
adress = requests.get(ipSite, headers = header)
print(line + "\n[*] IP your network:\n"+adress.text + line)
print("[!] Connecting to the Tor network /", end = "")
for i in range(5): 
	sleep(0.2)
	print('.', end = '', flush = True)
proxie = {
	'http': 'socks5h://127.0.0.1:9050', 
	'https': 'socks5h://127.0.0.1:9050'
}
try:
	adress = requests.get(ipSite, proxies = proxie, headers = header)
except:
	connection = False
	print("/\n[x] Stopping connect to the Tor network\n" + line)
else:
	connection = True
	print("/\n[+] Connected to the Tor network\n" + line)
	print("[*] IP Tor network:\n" + adress.text + line)
finally:
	url = input("[!] Uniform Resource Locator:\nhttp://")

	if connection == True:
		page = requests.get("http://"+str(url.split()[0]), proxies = proxie, headers = header)
	else:
		page = requests.get("http://"+str(url.split()[0]), headers = header)

	soup = BeautifulSoup(page.text, "html.parser")
	if url.split()[0] == url.split()[-1]:
		code = ""
		for tag in soup.findAll('html'):
			code += str(tag)
		with open("index.html","w") as html:
			html.write(code)
	else:
		if url.split()[1] == url.split()[-1]:
			for tag in soup.findAll(url.split()[1]):
				print(tag)
		else:
			for tag in soup.findAll(url.split()[1]):
				print(tag[url.split()[2]])
	print(line)