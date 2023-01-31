#!/bin/bash
# Developer: SirCryptic (NullSecurityTeam)
# Info: ThreatHunter Dependency installer (BETA)

red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

clear
banner="\
|---------------------------------| 
|ThreatHunter  | NullSecurityTeam |
|---------------------------------|
"

echo -e "$banner"

# Check if hping3 is installed
if [ $(dpkg-query -W -f='${Status}' hping3 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "${red}[-] Installing hping3...${reset}"
  sudo apt-get install -y hping3
else
  echo "${green}[+] hping3 is already installed!${reset}"
fi

# Check if python3 is installed
if [ $(dpkg-query -W -f='${Status}' python3 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "${red}[-] Installing python3...${reset}"
  sudo apt-get install -y python3
else
  echo "${green}[+] python3 is already installed!${reset}"
fi

# Check if python3-pip is installed
if [ $(dpkg-query -W -f='${Status}' python3-pip 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  echo "${red}[-] Installing python3-pip...${reset}"
  sudo apt-get install -y python3-pip
else
  echo "${green}[+] python3-pip is already installed!${reset}"
fi

# Check if subprocess32 is installed
if [ $(pip3 show subprocess32 | grep -c "Name: subprocess32") -eq 0 ];
then
  echo "${red}[-] Installing subprocess32...${reset}"
  sudo pip3 install subprocess32
else
  echo "${green}[+] subprocess32 is already installed!${reset}"
fi

echo "${green}[+] Installation complete!${reset}"
