import wexpect


##for i in range(18):
##    if i == 0:
##        exec(open("Networking 3.py").read())
##        "http://py4e-data.dr-chuck.net/known_by_Georgi.html"
##        
##    else:
##        exec(open("Networking 3.py").read())
##        link

        


for i in range(18):
    if i==0:
        child = wexpect.spawn("Networking 3.py")
        child.expect("Enter - ")
        child.sendline('http://py4e-data.dr-chuck.net/known_by_Georgi.html')

    else:
        child = wexpect.spawn("Networking 3.py")
        child.expect("Enter - ")
        child.sendline(link)
