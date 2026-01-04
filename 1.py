import subprocess
def attacks():
    print("1: TCP Syn Attack -sS")
    print("2: TCP Connect Scan -sT")
    print("3: Full Scan -sF")
    print("4: Null Scan -sN")
    print("5: XMAS Scan -sX")

def syn(ip_a, b):
    if b == "y" or "Y":
        subprocess.run(["nmap", ip_a, "-sS", "-p-", "-O", "-v"])
    elif b == "n" or "N":
        subprocess.run(["nmap", ip_a, "-sS", "-p-"])
    else:
        print("Enter correct option")

def con(ip_a, b):
    if b == "y" or "Y":
        subprocess.run(["nmap", ip_a, "-sT", "-p-", "-O", "-v"])
    elif b == "n" or "N":
        subprocess.run(["nmap", ip_a, "-sT", "-p-"])
    else:
        print("Enter correct option")

def full(ip_a, b):
    if b == "y" or "Y":
        subprocess.run(["nmap", ip_a, "-sF", "-p-", "-O", "-v"])
    elif b == "n" or "N":
        subprocess.run(["nmap", ip_a, "-sF", "-p-"])
    else:
        print("Enter correct option")

def null(ip_a, b):
    if b == "y" or "Y":
        subprocess.run(["nmap", ip_a, "-sN", "-p-", "-O", "-v"])
    elif b == "n" or "N":
        subprocess.run(["nmap", ip_a, "-sN", "-p-"])
    else:
        print("Enter correct option")

def xmas(ip_a, b):
    if b == "y" or "Y":
        subprocess.run(["nmap", ip_a, "-sX", "-p-", "-O", "-v"])
    elif b == "n" or "N":
        subprocess.run(["nmap", ip_a, "-sX"])
    else:
        print("Enter correct option")


print("A small networking tool created by ZAIN")
ip = input("Enter IP Address of the victim: ")
attacks()
print("Enter you attack choice: ")
choice = int(input())

if choice == 1:
    b = input("Do you want to also add -O and -v for more information (Y/N): ")
    syn(ip, b)
elif choice == 2:
    b = input("Do you want to also add -O and -v for more information (Y/N): ")
    con(ip, b)
elif choice == 3:
    b = input("Do you want to also add -O and -v for more information (Y/N): ")
    full(ip, b)
elif choice == 4:
    b = input("Do you want to also add -O and -v for more information (Y/N): ")
    null(ip, b)
elif choice == 5:
    b = input("Do you want to also add -O and -v for more information (Y/N): ")
    xmas(ip, b)
else:
    print("Enter Correct Option")