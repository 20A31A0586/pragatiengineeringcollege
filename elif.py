email="snehachandrika51@gmail.com"
pswd=12345
otp=2222
cemail=input("enter the email")
cpswd=int(input("enter the pswd"))
cotp=int(input("enter the otp"))
if((email==cemail and pswd==cpswd):
    cotp=int(input("enter the otp:"))
    if(otp==cotp);
    print("your amazon order is placed successfully")
elif(email==cemail and pswd==cpswd and otp!=cotp):
    print("your amazon order is failed and mismatched due to otp")
elif(email==cemail and pswd!=cpswd ):
    print("login failed")
elif(email!=cemail and pswd==cpswd):
    print("your amazon order is failed")
    




