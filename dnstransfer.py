# https://www.dnspython.org/
# https://www.tutorialspoint.com/python_network_programming/python_dns_look_up.htm
#
import dns.resolver
import dns.zone
import dns.query
import socket 
 
def get_ips(domain): 
    try: 
        hname = domain
        hip = socket.gethostbyname(hname) 
        print(hname, hip)
        ips.append(hip)
    except: 
        print("Unable to get domain name and ip") 



domainname=input('Domain name:')
ns=[]
ips=[]
result = dns.resolver.resolve(domainname, 'NS')
for ipval in result:
    ns.append(ipval.to_text())

for ip in ns:
    get_ips(ip)


for ip in ips:
    try:
     z = dns.zone.from_xfr(dns.query.xfr(ip, domainname))
     names = z.nodes.keys()

     for n in names:
       print(z[n].to_text(n))
    except:
        print('\nUnable to transfer from', ip,'\n')
