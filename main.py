print("🌟Contact Card🌟")
print()
name = input("input your name:").capitalize()
birthD = input("input your date of birth: ")
number = input("input your telephone number:")
email = input("input your email: ")
address = input("input your address: ").capitalize()
print()
print("===========================================")
print()
print("Here is your contact card")
print()
contactcard = {"name": name, "birth": birthD, "number": number, "email":email, "address":address}
print(f"""Name: {contactcard["name"]}
DOB: {contactcard["birth"]}
Tel: {contactcard["number"]}
Tel: {contactcard["number"]}
e-mail: {contactcard["email"]}
address: {contactcard["address"]}""")