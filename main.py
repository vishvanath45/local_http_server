#!/usr/bin/env python 

import os
import commands
import webbrowser
import thread

def begin(start):
	x = os.system("python -m SimpleHTTPServer >/dev/null 2>&1")

# def browser_open(final_add):
# 	y = os.system('python -m webbrowser -t "final_add" >/dev/null 2>&1')

thread.start_new_thread( begin ,( 1, ) )
ip_addr = commands.getoutput("hostname -I")
ip_addr = ip_addr.strip()
final_add = 'http://'+ip_addr+':8000'
print "share this address with people in your local network to share files "
print final_add
final_comm = 'python -m webbrowser -t '+final_add+' >/dev/null 2>&1'
y = os.system(final_comm)


# problems i faced and solutions 

# the os.system call was giving output on terminal at the same time 
# webbrowser call was also running in same terminal, so clash was inevitable
# so i made a thread and started system call for server in that and other process
# in parent.


#  some other things i tried while implementing this 
# y = os.system('python -m webbrowser -t "https://google.com" >/dev/null 2>&1')
# thread.start_new_thread(browser_open ,(final_add, ))
# Regex call for finding ip address
#a  = os.system('ip add show | grep -oE "([0-9]{1,3}\.){3}[0-9]{1,3}"')

