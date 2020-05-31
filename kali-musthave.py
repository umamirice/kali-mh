#!/usr/bin/python3
##important! this shit is outdated cause it's just copy of my old script (it can work, but Im not sure if it will)
import os
print('Well run this as root or you\'ll have much errors')
os.system("echo 'deb http://http.kali.org/kali kali-rolling main non-free contrib\ndeb-src http://http.kali.org/kali kali-rolling main non-free contrib' > /etc/apt/sources.list") #that will remove your actual sources.list
os.system('''dpkg --add-architecture i386
apt update
apt upgrade -y
apt full-upgrade -y
apt dist-upgrade -y
apt autoremove
apt autoclean
apt clean
''') #added 32 bit support and update system
print('ok')
print('now some tools') #and other stuff which will be useful
os.system('apt install -y git python3 python3-pip build-essential')
print('done')
print('some bugs kali have now will be fixed...')
os.system('''echo "
[main]
plugins=ifupdown,keyfile

[ifupdown]
managed=true
" > /etc/NetworkManager/NetworkManager.conf''')
print("done\nscript will add dark theme to prefered in gtk") #your eyes should say "thank u"
os.system("echo '[Settings]' > /root/.config/gtk-*/settings.ini\necho 'gtk-application-prefer-dark-theme=1' >> /root/.config/gtk-3.0/settings.ini")
print('some good pip stuff')
os.system('pip install --upgrade pip\npip install whatportis\npip install pinggraph')
print('last thing script will do is adding syntax to vim') #if u know how to exit vim lol
os.system('echo "syntax on" >> /root/.vimrc')
print('now have fun')
print('if you don\'t like your graphical environment then check environment.txt')