email=input("Enter your Email:").strip()
l=email.partition('@')
userName=l[0]
domain=l[-1]
print("Your username is ",userName)
print("Your domain is ",domain)
