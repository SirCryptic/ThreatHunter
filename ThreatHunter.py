import socket
import os
import subprocess
import sys
import platform
import paramiko

red = "\033[1;31m"
green = "\033[1;32m"
reset = "\033[0;0m"
# Developer: SirCryptic (NullSecurityTeam)
# Info: ThreatHunter 1.0
os.system('cls' if os.name == 'nt' else 'clear')
banner = '''
_____________                    ___________  __             _____             
___  __/__  /___________________ __  /___  / / /___  __________  /_____________
__  /  __  __ \_  ___/  _ \  __ `/  __/_  /_/ /_  / / /_  __ \  __/  _ \_  ___/
_  /   _  / / /  /   /  __/ /_/ // /_ _  __  / / /_/ /_  / / / /_ /  __/  /    
/_/    /_/ /_//_/    \___/\__,_/ \__/ /_/ /_/  \__,_/ /_/ /_/\__/ \___//_/     
                                                                               
'''

print(banner)

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

def check_nsg(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(green + "Network Security Group not detected" + reset)
        else:
            print(red + "Network Security Group detected" + reset)
    except Exception as e:
        print(red + "Error while checking Network Security Group: " + str(e) + reset)

def check_ips(host, port):
    try:
        response = os.system("hping3 " + host + " -p " + str(port) + " -c 5")
        if response == 0:
            print(green + "Intrusion Prevention System not detected" + reset)
        else:
            print(red + "Intrusion Prevention System detected" + reset)
    except Exception as e:
        print(red + "Error while checking Intrusion Prevention System: " + str(e) + reset)

def check_os():
    os_name = platform.system()
    os_version = platform.release()
    os_architecture = platform.machine()
    print("Operating System:", os_name + " " + os_version + " " + os_architecture)

def check_service(service_name):
    try:
        service_status = subprocess.run(["systemctl", "is-active", service_name], capture_output=True, text=True)
        if "active" in service_status.stdout:
            print(service_name, "service is running")
        else:
            print(service_name, "service is not running")
    except Exception as e:
        print("Error while checking service:", str(e))

def check_log4js_remote(host, port=22):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, timeout=20)

        stdin, stdout, stderr = ssh.exec_command("npm list --depth=0")
        log4js = stdout.read().decode("utf-8")

        if "log4js" in log4js:
            print(red + "log4js detected" + reset)
        else:
            print(green + "log4js not detected" + reset)

        ssh.close()
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

check_os()
check_service("ssh")
check_service("httpd")
check_firewall(host, port)
check_ids(host, port)
check_antivirus()
check_log4js_remote(host, port=22)
check_nsg(host, port)
check_ips(host, port)
