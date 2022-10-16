import subprocess
import optparse
import pyfiglet

a = pyfiglet.figlet_format("MAC SPOOFER BY CODEGRILLS")
print(a)



def opt_parse():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="The interface which you want to change MAC")
    parser.add_option("-m", "--mac", dest="mac_addr", help="The new MAC address you want to set")
    (options, args) =  parser.parse_args()
    if not options.interface:
       parser.error("Please specify the interface, Check help section")
    elif not options.mac_addr:
       parser.error("Please specify the mac address, Check help section")
    return options





def mac_change(interface,mac_addr):
    print("Changing MAC address for " + interface + " to " + mac_addr)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_addr])
    subprocess.call(["ifconfig", interface, "up"])
    
options = opt_parse()

mac_change(options.interface,options.mac_addr)
