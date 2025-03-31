Email = "Revolver0x90@RedTeam.com"
domain = Email.split("@")[1]
print(domain)
domain2 = Email.split("@")[0]
print(domain2)

usarname = Email[:Email.index("@")]
domainName= Email[Email.index("@") +1:]
print("User Name : ", usarname)
print("Domain Name : ", domainName)