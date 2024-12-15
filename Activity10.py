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