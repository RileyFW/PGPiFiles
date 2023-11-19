#!/bin/bash
echo "checking for updates..."
sudo apt update -y
echo "done!\n"

echo "installing firefox"
sudo apt install firefox-esr -y
echo "done with firefox!"

echo "installing python3"
sudo apt install python3 -y 
echo "done!"

echo "install unclutter"
sudo apt install unclutter -y
echo "@unclutter -idle 0" | sudo tee -a /etc/xdg/lxsession/LXDE-pi/autostart
echo "done!"

echo "disabling sleep settings..."
xset s noblank
xset -dpms
xset -s off
echo "done!"

echo "run pip installs..."
pip install selenium
pip install pause
echo "done!"

echo "get files from github..."
mkdir /home/admin/view
wget -O /home/admin/view/view.sh https://raw.githubusercontent.com/RileyFW/PGPiFiles/master/view.sh
wget -O /home/admin/view/view.py https://raw.githubusercontent.com/RileyFW/PGPiFiles/master/pgpi2/view.py
dos2unix /home/admin/view/view.sh
sudo chmod 777 /home/admin/view/view.sh
sudo chmod 777 /home/admin/view/view.py
echo "done!"

curl https://sh.rustup.rs -sSf | sh
source "$HOME/.cargo/env"

echo "installing cargo and building geckodriver..."
echo "this could take a while..."

cargo install geckodriver
echo "done!"

echo "adding to autostart..."
mkdir /home/admin/.config/lxsession
mkdir /home/admin/.config/lxsession/LXDE-pi
cp /etc/xdg/lxsession/LXDE-pi/autostart /home/admin/.config/lxsession/LXDE-pi/
echo '@bash /home/admin/view/view.sh' >> /home/admin/.config/lxsession/LXDE-pi/autostart

echo "rebooting in 5 seconds..."
sleep 5
sudo reboot now
