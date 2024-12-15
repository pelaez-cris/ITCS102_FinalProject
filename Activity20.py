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