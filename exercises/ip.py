#!/usr/bin/env python

ip = raw_input("Enter an IP address: ")

ip_list = ip.split('.')

print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))

ip_list[3] = '0'

bin_list = []

for num in ip_list:
    bin_list.append(bin(int(num)))

print("{:<12}{:<12}{:<12}{:<12}".format(*ip_list))
print("{:<12}{:<12}{:<12}{:<12}".format(*bin_list))


