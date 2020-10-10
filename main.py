import random
import requests
import string
letters=string.ascii_letters
print("how many thread?")
z=int(input(">"))
print("lenght of password and username?")
d=int(input(">"))
print("\nwhat's register url?")
a=str(input(">"))
print("what's login url?")
b=str(input(">"))
print("what's index url?")
c=str(input(">"))
def rnd():
    randome="".join(random.choice(letters) for i in range(d))
    return randome
url=a
url2=b
url3=c
for i in range(z):
    name=rnd()
    passwd=rnd()
    session=requests.session()
    login_data={"name":name,"password":passwd,"register":""}
    x = session.post(url,data=login_data)
    y = session.post(url2,data=login_data)
    v = session.get(url3)
if v.status_code ==200:
    print("a number of "+str(z)+" account were created on "+url)
