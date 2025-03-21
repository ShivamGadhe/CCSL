import hashlib

msg=input("Enter a Message :")
mi=hashlib.md5(msg.encode())
u=mi.hexdigest()
print(f"Hexadecimal hash value is :{u}")
