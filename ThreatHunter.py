import socket
import os
import subprocess
import sys

red = "\033[1;31m"
green = "\033[1;32m"
reset = "\033[0;0m"

def check_firewall(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(green + "Firewall not detected" + reset)
        else:
            print(red + "Firewall detected" + reset)
    except Exception as e:
        print(red + "Error while checking firewall: " + str(e) + reset)

def check_ids(host, port):
    try:
        response = os.system("hping3 " + host + " -p " + str(port) + " -c 1")
        if response == 0:
            print(green + "Intrusion Detection System not detected" + reset)
        else:
            print(red + "Intrusion Detection System detected" + reset)
    except Exception as e:
        print(red + "Error while checking Intrusion Detection System: " + str(e) + reset)

def check_antivirus():
    if sys.platform == "win32":
        try:
            process = subprocess.Popen(['powershell.exe', 'Get-MpComputerStatus'], stdout=subprocess.PIPE)
            stdout = process.communicate()[0]
            if b"Enabled" in stdout:
                print(red + "Antivirus detected" + reset)
            else:
                print(green + "Antivirus not detected" + reset)
        except Exception as e:
            print(red + "Error while checking antivirus: " + str(e) + reset)
    else:
        print("Antivirus check not available on this operating system")

def check_log4js():
    try:
        log4js = subprocess.run(["npm", "list", "--depth=0"], capture_output=True, text=True)
        if "log4js" in log4js.stdout:
            print(red + "log4js detected" + reset)
        else:
            print(green + "log4js not detected" + reset)
    except Exception as e:
        print(red + "Error while checking for log4js: " + str(e) + reset)

def use_nameserver():
    try:
        with open("nameserver.txt", "r") as file:
            nameserver = file.read().strip()
    except FileNotFoundError:
        nameserver = input("Enter nameserver address: ")
        with open("nameserver.txt", "w") as file:
            file.write(nameserver)
    return nameserver

if sys.platform == "win32":
    host = use_nameserver()
else:
    host = input("Enter hostname or IP address: ")

port = int(input("Enter port number: "))

check_firewall(host, port)
check_ids(host, port)
check_antivirus()
check_log4js()
