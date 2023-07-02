 import nmap

scanner = nmap.PortScanner()

print("Welcome To Our Nmap Scanner")
print("Version : 1.0")
print("Developed By Cyber_Bytezz")
print("Creativity From Nmap.org")
print("----Nothing Is Secure From Your Click =)----")

print("-------------------------------------------")

ip_addr = input("Please Enter The IP You Want To Scan")

print("The Ip Address Is :",ip_addr)

type(ip_addr)
response = input("""\n 
                Please Enter The Type Of Scan You Want To Perforn
                1.SYN ACK Scan
                2.UDP Scan
                3.Comperehensive Scan
                4.More
                       """)

print("You Have Selected The Option", response)


if response == '1':
    print("Nmap Version",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS')
    print(scanner.scaninfo())
    print("IP Status :",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports :",scanner[ip_addr]['TCP'].key()) #Dictionary [34,54,120]

elif response == '2' :
    print("Nmap Version",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS -A')
    print(scanner.scaninfo())
    print("IP Status :",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports :",scanner[ip_addr]['UDP'].key()) #Dictionary [34,54,120]

elif response == '3' :
    print("Nmap Version",scanner.nmap_version())
    scanner.scan(ip_addr,'1-1024','-v -sS -v -O')
    print(scanner.scaninfo())
    print("IP Status :",scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols)
    print("Open Ports :",scanner[ip_addr]['TCP'].key()) #Dictionary [34,54,120]

elif response == '4' :
    print("We Will Update Soon-----------")
    print("Click: Ctrl+C")



