import  os

stat = os.system('service sshd status')
print("service: " + stat)
