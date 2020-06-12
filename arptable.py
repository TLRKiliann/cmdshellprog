#!/usr/bin/python3
# -*-coding:utf-8-*-


import time
from subprocess import call


# Launch this prog in root mode!
print("\n#################################################################################\n")

print("\nLancement de la cmd ifconfig :\n")
call(["ifconfig"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("\nLancement de la cmd arp -anv :\n")
call(["arp", "-an"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("\nLancement de la cmd netstat -antp :\n")
call(["netstat", "-antp"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("\nLancement de la cmd netstat -pute :\n")
call(["netstat", "-pute"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("\nLancement de la cmd netstat -r :\n")
call(["netstat", "-r"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("\nLancement de la cmd nmap -sV [ip]:\n")
call(["nmap", "-sV", "192.168.0.13", "-vv"])
print("\nLa cmd s'est déroulée correctement...\n")
time.sleep(2)
print("\n#################################################################################\n")

print("Fin du programme!\n")
