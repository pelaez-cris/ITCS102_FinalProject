import os
def act_1():
    print("\nThis is my activity 1\n")
    print("Hello World")

def act_2():
    print("\nThis is my activity 2\n")
    name = input( "Please enter a name -----> " )
    print ( "Hi!" + name )

def act_3():
    print("\nThis is my activity \n")
    name = input("Please input your name here ---> ")
    fname = input("Please input your fname here ---> ")
    mname = input("Please input your mname here ---> ")
    birthdate = input("Please input your birth date here ---> ")
    birthmonth = input("Please input your birthmonth here ---> ")
    birthyear = input("Please input your birthyear here ---> ")
    maritalstatus = input("Please input your maritalstatus here ---> ")
    religion = input("Please input your religion here ---> ")
    ethnicity = input("Please input your ethnicity here ---> ")
    mobile = input("Please input your mobile here ---> ")
    email = input("Please input your email here ---> ")
    gender = input("Please input your gender here ---> ")
    address = input("Please input your address here ---> ")
    age = input(" Please input your age here ---> ")
    print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def act_4():
    print("\nThis is my activity 4\n")
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)
    print("The sum of", number1 ,"and",number2,"is",answer)

def act_5():
    print("\nThis is my activity 5\n")
    print("\nFARENHEIT TO CELCIUS CONVERTER")
    temp = eval(input("\nEnter a temperature in Farenheit ---> "))
    celcius = (temp -32) * 5 / 9
    print("\nThe conversion of ", temp , " degrees Farenheit is ", celcius , " degrees Celcius.")
    print(f"\nThe conversion of {temp} degrees Farenheit is {celcius} degrees Celcius")
    (round(celcius, 2))
    print(f"\nThe convertion of {temp} degrees Farenheit is {round(celcius,2)} degrees Celcius.")

def act_6():
    print("\nThis is my activity 6\n")
    x = 5
    print(x)
    x = x + 10
    print(x)
    x = x +15
    print(x)
    x += 10 
    print(x)
    x+=20
    print(x)

def act_7():
    print("\nThis is my activity 7\n")
    gold = 0
    name=input('Hi, enter your name:  ')
    hasMine=input('Did you mine gold today?  ')
    if hasMine.lower() == "yes":
        gold +=1
        print(f'Hi! {name}, Today you have a total of {gold} gold')
    else:
        print(f'Hi! {name}, Today you have a total of {gold} gold')

def act_8():
    print("\nThis is my activity 8\n")
    password = input('Enter your password---> ')
    if password.lower() == "password" :
        print('Access Granted!!!!')
        print('Enjoy using the system')
    elif password.lower() =='secret':
        print('Access Granted!!!!')
        print('Enjoy using the system')
    else:
        print('Access Denied!!!!!')
    print('Thank you for using the system')

def act_9():
    print("\nThis is my activity 9\n")
    age = eval(input("Enter your age --->  "))
    if age >=1 and age <=7:
        print("\nYour age is categorized as Toddler")
    elif age >=8 and age <=13:
        print("\nYour age is categorized as Pre-teen")
    elif age >=14 and age <=18:
        print("\nYour age is categorized as Teenager ")
    elif age >=19 and age <=31:
        print("\nYour age is categorized as Early Adulthood ")
    elif age >=32 and age <=45:
        print("\nYour age is categorized as Mid Adulthood ")
    elif age >=46 and age <=59:
        print("\nYour age is categorized as Post Adulthood ")
    elif age >=60 and age <=90:
        print("\nYour age is categorized as Senior ")
    elif age >=91 and age <=100:
        print("\nPwede ka na mamatay boss, libre na kita kabaong ")
    else:
        print("\nAba naman!! May anting ka ba boss?")

def act_10():
    print("\nThis is my activity 10\n")
    name = input("Enter your name: ")
    isStudent = input("are your current student of DLL? (yes or No) -->")
    if isStudent.lower() == "yes":
        yearlevel = input("\n f - Freshman \n s - sophomore \n j - Junior \n r - Senior \n what is your current level right now in DLL? ")
        if yearlevel.lower() == "f":
            print(f"Hi {name} you are Freshman")
        elif yearlevel.lower() == "s":
            print(f"Hi {name} you are Sophomore ")
        elif yearlevel.lower() == "j":
            print(f"Hi {name} you are Junior")
        elif yearlevel.lower() == "r":
            print(f"Hi {name} you are Senior")
        else:
            print("Invalid choice")

def act_11():
    print("\nThis is my activity 11\n")
    for me in range (1 , 101):
        print(me, 'GOODBYE WORLD')

def act_12():
    print("\nThis is my activity 12\n")
    for cycle in range (10,0,-1):
        (cycle)

def act_13():
    print("\nThis is my activity 13\n")
    sum = 1
    num=int(input('Enter a number: '))
    for x in range (num,0,-1):
        sum *= x
    print(f"The factorial of {num} is {sum}")

def act_14():
    print("\nThis is my activity 14\n")
    for x in range ( 0, 11,):
        print(x,end =" ")
        for y in range (0, 11):
            print("*",end = " ")
        print("")

def act_15():
    print("\nThis is my activity 15\n")
    for x in range ( 0, 11,):
        print(x,end =" ")
        for y in range (0, x):
            print("*",end = " ")
        print("")

def act_16():
    print("\nThis is my activity 16\n")
    for x in range (1,11,):
        for y in range (1, x + 1):
            print(" ",end=" ")
        for z in range(11, x, -1):
            print(" * ",end=" ")
        print()

def act_17():
    print("\nThis is my activity 17\n")
    col = eval(input("Enter number of columns---> "))
    for x in range (1, 11):
        for y in range (1, col + 1):
            print(f"{x} x {y} = {x*y}" ,end="\t")
        print()

def act_18():
    print("\nThis is my activity 18\n")
    tri = eval(input("Enter a number of triangle---> "))
    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()

def act_19():
    print("\nThis is my activity 19\n")
    tri = eval(input("Enter a number of triangle---> "))
    for x in range (1, 6):
        for r in range (1 , tri + 1):
            for y in range (1 , x + 1):
                print("*", end=" ")
            for z in range (6, x, -1):
                print(" ",end=" ")
        print()

def act_20():
    print("\nThis is my activity 20\n")
    import os
isContinue =True
brrt = 0
while isContinue == True:
    ngi=input("Would you like to add another triangle (yes/no)? ")
    if ngi.lower() == "no":
        print("PROGRAM TERMINATED")
        break
    else:
        os.system('cls')
        brrt += 1
        for x in range(1,6):
            for y in range(brrt+1):
                for z in range(1,x+1):
                    print("*", end= " ")
                for a in range(5,x,-1):
                    print(" ", end= " ")
                print( end= " ")
            print()
        continue    

def act_21():
    print("\nThis is my activity 21\n")
    def pang_hi():
        print("HI IT1C")
        def pang_hi_v2(name):
            print(f"Hello {name}")
        def termi():
            print("PROGRAM TERMINATED")
        def activity_2():
            number1 = eval (input("enter a number--->" ))
            number2 = eval (input("enter another number--->" ))
            answer = (number1 + number2)
            print(f"The sum of {number1} and {number2} is {answer}")
        tuloy =  True
        while tuloy == True:
            ask = input("Enter a name---> ")
            if ask.lower() != "stop":
                pang_hi_v2(ask)
                if ask == "2":
                    activity_2()
                    continue
            else:
                termi()
                break
def act_22():
    print("\nThis is my activity 22\n")
    def activity22():
        def activity1():
            print("Hello World")
        activity1()
    activity22()

def act_23():
    print("\nThis is my activity 23\n")
    def factorial(number):
        """ This function's purpose is to compute/calculate the factorial of any number given """
        fact = 1
        for x in range(number, 0, -1):
            fact *= x
        return fact
    print(f"the factorial of 13 is {factorial(13)}")

def act_24():
    print("\nThis is my activity 24\n")
    from Activity23 import factorial
    print(f"the factorial of 7 is {factorial(7)} ")

def act_25():
    print("\nThis is my activity 25\n")
    courses = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]
    courses.remove("Delete w/o index")
    courses.pop()
    courses.append("DHRS")
    courses.insert(0, "ABELS")
    print(courses)

def cc_1():
    print("\nThis is my Code Challenge 1\n")

def cc_2():
    print("\nThis is my Code Challenge 2\n")

def cc_3():
    print("\nThis is my Code Challenge 2\n")

def cc_4():
    print("\nThis is my Code Challenge 4\n")

def cc_5():
    print("\nThis is my Code Challenge 5\n")

def cc_6():
    print("\nThis is my Code Challenge 6\n")

def cc_7():
    print("\nThis is my Code Challenge 7\n")

def cc_8():
    print("\nThis is my Code Challenge 8\n")

def cc_9():
    print("\nThis is my Code Challenge 9\n")

def cc_10():
    print("\nThis is my Code Challenge 10\n")

def cc_11():
    print("\nThis is my Code Challenge 11\n")

def cc_12():
    print("\nThis is my Code Challenge 12\n")

def cc_13():
    print("\nThis is my Code Challenge 13\n")

def cc_14():
    print("\nThis is my Code Challenge 14\n")

def cc_15():
    print("\nThis is my Code Challenge 15\n")

def cc_16():
    print("\nThis is my Code Challenge 16\n")
    

# def body():
#         print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
#         print(f"Bachelor Of Science In Infomation Technology - 1C")
#         print(f"\nPlease Select an Option:   ")
#         print(f"\n1. Open Activity Folder")  
#         print(f"2. Open Code Challenge Folder")
#         print(f"3. Exit Program")
#         menu = input(f"\nChoose what action you want to do:  ")
#         while body:
#             if menu == "1":
#                 os.system("cls")
#                 act_folder()
#             elif menu == "2":
#                 cc_folder()
#                 os.system("cls")
#             elif menu == "3":
#                 os.system("cls")
#                 print(f"\nProgram terminated, Thank you for checking my Program.\n")
#                 break
#             else:
#                 print("Invalid Choice, Please try again.")         
# body()

# def act_folder():
#     print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
#     print(f"Bachelor Of Science In Infomation Technology - 1C")

# def cc_folder():
#     print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
#     print(f"Bachelor Of Science In Infomation Technology - 1C")

