import random

current_password = '1234'
tried_password_list = []


def generate_otp(length=4):
    otp = ""
    for i in range(length):
        otp += str(random.randint(0, 9))
    return otp

start = True

count = 0
while start:
    tried_password = generate_otp(4)
    if tried_password in tried_password_list:
        tried_password = generate_otp()
    elif tried_password != current_password:
        tried_password = generate_otp()
        tried_password_list.append(tried_password)
        count += 1
    else:
        print(f"Password Cracked! at {count}th count")
        start = False
        print("Password :", tried_password)
