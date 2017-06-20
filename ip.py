#!/usr/bin/env python

ip = raw_input("Enter an IP address: ")

ip_list = ip.split('.')

print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))
