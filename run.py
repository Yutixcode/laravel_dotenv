import sys
import requests as req
req.urllib3.disable_warnings()
from colorama import Fore,Style
from multiprocessing import Pool
from multiprocessing.dummy import Pool as DeadPool

red    = Fore.RED
yellow = Fore.YELLOW
blue   = Fore.BLUE
reset  = Style.RESET_ALL
bold   = Style.BRIGHT
green  = Fore.GREEN
white  = Fore.WHITE
dim    = Style.DIM
purple = Fore.MAGENTA
cyan   = Fore.CYAN

class Gaskeun:
	def __init__(self,situs):
		self.url = situs if "://" in situs else "http://" + situs
		self.dei = 0
		self.x()
	
	def x(self):
		for path in [".env","api/.env","laravel/.env"]:
			target = self.url if self.url.endswith("/") else self.url + "/"
			self.scan(target+path)
	
	def scan(self,site):
		try:
			raw = req.get(site,headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'},timeout=3,verify=False).text
			if "DB_PASSWORD" in raw:
				print(f" {reset}{green}[ FOUND ] {reset}{white}{site}")
				open("founds.txt","a").write(f"{site}\n")
			else:
				print(f" {reset}{red}NOT FOUND {reset}{reset}{dim}{site}")
				
		except req.exceptions.Timeout:
			if self.dei == 5:
				print(f" {reset}{red}-TIMEOUT- {reset}{dim}{site}")
			else:
				print(f" {reset}{yellow}[ RETRY ] {reset}{dim}{site}")
				self.dei += 1
				self.scan(site)
			
		except Exception as er:
			print(f" {reset}{red}NOT FOUND {reset}{dim}{white}{site}")
				
		except KeyboardInterrupt:
			exit()
	
print(f"""{reset}
 .'.         .'.
 |  \       /  |
 '.  \  |  /  .'
   '. \\\\|// .' 
     '-- --'   {cyan}Laravel dotenv Scanner{reset}
 v1  .'/|\\'.   Created by YutixCode
    '..'|'..'  bug report: {white}t.me/yutixverse
""")

def main():
	try:
		file = open(input(f"{reset}{white}   > File: {cyan}")).read().splitlines()
		pool = int(input(f"{reset}{white}   > Thread: {cyan}"))
		
		print()
		
		DeadPool = Pool(pool)
		DeadPool.map(Gaskeun, file)
		DeadPool.close()
		DeadPool.join()
		
		print(f"{reset}{white}Help me to buy a pc: {cyan}https://saweria.co/lordyutix")
		
	except FileNotFoundError:
		print(f"\n {red}ERROR {reset}File not found")
	except ValueError:
		print(f"\n {red}ERROR {reset}Thread must be a number")
	except KeyboardInterrupt:
		exit()

if __name__ == "__main__":
    main()