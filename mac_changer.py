#!/usr/bin/env python

import subprocess # for execute cammands
import optparse #for option in terminal

def get_arguments():
    parser=optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="Interface To change Its MAC Address")
    parser.add_option("-m","--mac",dest="mac_add",help="New MAC Address")
    (option,arguments)= parser.parse_args()
    if not option.interface:
        parser.error("[-] Please Specify The Interface, use --help For More Info..")
    elif not option.mac_add:
        parser.error("[-] Please Specify The MAC Address, use --help For More Info..")
    return option



def change_mac(interface,mac_add):
    print(" [+] Changing MAC Address For " + interface + " to "+ mac_add )
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",mac_add])
    subprocess.call(["ifconfig",interface,"up"])
    subprocess.call(["ifconfig",interface])

     #raw_input("New MAC > ")

#basics
# subprocess.call("ifconfig " + interface + " down ",shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + mac_add ,shell=True)
# subprocess.call("ifconfig " + interface + " up ",shell=True)
# subprocess.call("ifconfig " + interface, shell=True)

# call
option = get_arguments()
change_mac(option.interface,option.mac_add )
