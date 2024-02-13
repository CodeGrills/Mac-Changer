MAC spoofer By codegrills

TOOL CREATOR - Saurabh Kumar

=========================

MAC Spoofer is an tool that makes the maniputation of MAC
addresses of the network interfaces easier in linux systems.

It's very easy to use.
We only need to have Python installed in our system.

<h1> Installation Video </h1>
<object width="425" height="350">
  <param name="movie" value="https://www.youtube.com/embed/3c49AyDEpO8?si=XQ-jS2Pa0N3zy7Tl" />
  <param name="wmode" value="transparent" />
  <embed src="https://www.youtube.com/embed/3c49AyDEpO8?si=XQ-jS2Pa0N3zy7Tl"
         type="application/x-shockwave-flash"
         wmode="transparent" width="425" height="350" />
</object>
First clone the repository in your system  by typing following command:

git clone https://github.com/CodeGrills/Mac-Changer

To install requirements for using the to use the tool, type this command on the terminal:

pip install -r requirements.txt

To see help section:
python3 mac-spoofer.py -h

Now we have sucessfully installed all requirements to use the tool.
To change you MAC address, simply follow the following syntax:

python3 mac-spoofer.py -i your_interface -m your_new_mac

e.g python3 mac-spoofer.py -i eth0 -m 00:11:22:33:44:55

THATS ALL
THANKS 
BE AWARE BE SAFE !!!
