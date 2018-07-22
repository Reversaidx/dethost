import subprocess,multiprocessing
host="kurwasdasdasdasdasd.pw"
ip=subprocess.check_output("dig +short %s" %(host),shell=True)
ips=ip.split('\n')
#print(ips)

def genhostlist(base):
    hostlist=[]
    for i in range(1,15):
        host=base+'%0*d' %(3,i)
        hostlist.append(host)
    return hostlist


def ava_check(hostlist):
    for ip in hostlist:
     avaible=subprocess.check_output("ping -c 1 %s>/dev/null && echo True" %(ip),shell=True)
     if not 'True' in avaible:
        avaible='False'

print( genhostlist("us0101bls"))