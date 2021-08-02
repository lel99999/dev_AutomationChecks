import os

def check_ping(hostname):
#   _hostname = "www.google.com"
    response = os.system("ping -c 1 " + hostname)
    # and then check the response...
    if response == 0:
        pingstatus = "Network Active"
    else:
        pingstatus = "Network Error"

    return pingstatus

def checkhosts(hostfile):
    goodhosts = []
    badhosts = []
    i=1
    try:
#       f = open("hostlist.txt","r")
        f = open(hostfile,"r")
        lines = f.readlines()
        for line in lines:
            print(str(i) + ": " + line + "\n")
            i+=1
            print("Network Status: " + check_ping(line))
            if check_ping(line) == "Network Active":
                goodhosts.append(line)
            else:
                badhosts.appen(line)
    except Exception as ex:
        print(ex)
    print("goodhosts:")
    print(*goodhosts)
#   print(*goodhosts,sep="\n")
    print("\n")
    print("badhosts:")
#   print(*badhosts,sep="\n")
    print(*badhosts)


def main():
#   print("Network Status: " + check_ping("www.apple.com"))
    checkhosts("hostlist.txt")

if __name__ == "__main__":
    main()
