#!/usr/bin/env python

import subprocess # for execute cammands
import optparse #for option in terminal

parser=optparse.OptionParser()
parser.add_option("-i","--interface",dest="interface",help="Interface To change Its MAC Address")
parser.add_option("-m","--mac",dest="mac_add",help="New MAC Address")
(option,arguments)=parser.parse_args()
interface= option.interface     #raw_input("Interface > ")
mac_add= option.mac_add       #raw_input("New MAC > ")
print(" [+] Changing MAC Address For " + interface + " to "+ mac_add )
#basics
# subprocess.call("ifconfig " + interface + " down ",shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + mac_add ,shell=True)
# subprocess.call("ifconfig " + interface + " up ",shell=True)
# subprocess.call("ifconfig " + interface, shell=True)

# security
subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",mac_add])
subprocess.call(["ifconfig",interface,"up"])
