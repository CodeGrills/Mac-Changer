MAC spoofer By codegrills
=========================

MAC Spoofer is an tool that makes the maniputation of MAC
addresses of the network interfaces easier in linux systems.

It's very easy to use.
We only need to have Python installed in our system.

First clone the repository in your system  by typing following command:

git clone htt.............

To install requirements for using the to use the tool, type this command on the terminal:

pip install -r requirements.txt

To see help section:
python3 mac-spoofer.py -h

Now we have sucessfully installed all requirements to use the tool.
To change you MAC address, simply follow the following syntax:

python3 mac-spoofer.py -i your_interface -m your_new_mac

e.g python3 mac-spoofer.py -i eth0 -m 00:11:22:33:44:55


