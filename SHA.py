import hashlib

msg=input("Enter a Message :")
mi=hashlib.sha1(msg.encode())
u=mi.hexdigest()
print(f"Hexadecimal hash value is :{u}")


