#!/bin/bash

# Install dependencies
echo "Installing dependencies..."
sudo apt-get install -y hping3
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo pip3 install subprocess32

echo "Installation complete!"
