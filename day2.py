Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
apple=100
banana=200
pineapple=300
print(apple)
100
print(banana)
200
print(pineapple)
300
print(apple,end=' ')
100 
print(apple,end='*')
100*
print(apple,end='*',banana)
SyntaxError: positional argument follows keyword argument
print(apple,banana,pineapple)
100 200 300
print(apple,end='*',banana,end='-')
SyntaxError: positional argument follows keyword argument
print((apple,end='*'),(banana,end='-'))
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
x,y,z=input("Enter a three value:").split()
Enter a three value:100
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x,y,z=input("Enter a three value:").split()
ValueError: not enough values to unpack (expected 3, got 1)
x,y,z=input("Enter a three value:").split()
Enter a three value:100 200 300
print("Total number of students:")
Total number of students:
print("Total number of students:",x)
Total number of students: 100
print("Number of boys is:",y)
Number of boys is: 200
print("Number of girls are:",z)
Number of girls are: 300
x,y,z=input("Enter a three value:").split('0')
Enter a three value:100 200 300
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    x,y,z=input("Enter a three value:").split('0')
ValueError: too many values to unpack (expected 3)
x,y,z=input("Enter a three value:").split('*')
Enter a three value:100 200 300
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    x,y,z=input("Enter a three value:").split('*')
ValueError: not enough values to unpack (expected 3, got 1)
x,y,z=input("Enter a three value:").split('0')
Enter a three value:1 0 20 3
print("Total number of students:",x)
Total number of students: 1 
print("Number of boys is:",y)
Number of boys is:  2
print("Number of girls are:",z)
Number of girls are:  3
x,y,z=input("Enter a three value:").split('0')
Enter a three value:1102000330003
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    x,y,z=input("Enter a three value:").split('0')
ValueError: too many values to unpack (expected 3)
x,y,z=input("Enter a three value:").split('0')
Enter a three value:1110222203333
print("Total number of students:",x)
Total number of students: 111
print("Number of boys is:",y)
Number of boys is: 2222
print("Number of girls are:",z)
Number of girls are: 3333
x,y,z=input("Enter a three value:").split('*')
Enter a three value:10*80*90
print("Total number of students:",x)
Total number of students: 10
x,y,z=input("Enter a three value:").split('0')
Enter a three value:100
print("Total number of students:",x)
Total number of students: 1
print("Number of boys is:",y)
Number of boys is: 
print("Number of girls are:",z)
Number of girls are: 
x,y,z=input("Enter a three value:").split('00')
Enter a three value:1002003
print("Total number of students:",x)
Total number of students: 1
print("Number of boys is:",y)
Number of boys is: 2
print("Number of girls are:",z)
Number of girls are: 3
email="snehachandrika51@gmail.com"
pswd="12345"
cemail=input("enter the email") #c=clientemail
enter the emailc
cpswd=input("enter the pswd")
enter the pswd123
if(email==cemail and pswd==cpswd):
    print("login successfully")
    else:
        
SyntaxError: invalid syntax
if(email==cemail and pswd==cpswd):
    print("login successfully"):
        
SyntaxError: invalid syntax
if(email==cemail and pswd==cpswd):
    print("login successfully")
else:
    print("login failed")
    cemail=input("enter the email")
    