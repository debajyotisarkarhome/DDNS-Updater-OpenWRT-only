#!/usr/bin/python3
import paramiko as pm
import json
import requests
fil=open("creds.json","r")
cred_dat=json.load(fil)
client = pm.SSHClient()
client.load_system_host_keys()
client.connect('192.168.1.1',username=cred_dat["user"],password=cred_dat["passwd"])
stdin, stdout, stderr = client.exec_command('ubus call network.interface.wan status')
stdin.close()
out=str(stdout.read().decode())
out1=json.loads(out)
out2=out1['ipv4-address']
out3=out2[0]
ipaddr=out3['address']
fil1=open("creds_ddns.json","r")
ddns_cred_data=json.load(fil1)
res=requests.get("http://"+ddns_cred_data['user']+":"+ddns_cred_data['passwd']+"@dynupdate.no-ip.com/nic/update?hostname="+ddns_cred_data["user"]+".ddns.net&myip="+ipaddr)

