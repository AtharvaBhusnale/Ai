from datetime import datetime

def getHour():
    cTime = datetime.now().hour
    return cTime

def greet():
    if (getHour()>4 and getHour()<12):
        print("Good Morning!")
    elif(getHour()<16):
        print("Good Afternoon!")
    else:
        print("Good Evening!")

greet()

keys=["department","faculty","Enter query manuaaly"]
dict={'department':["Computer","IT","AIDS","Mechanical"],'faculty':["Atharva","Prasad","Sanket","Piyush"]}

for i in range(len(keys)):
    print(i+1,":",keys[i])

choice=int(input("How may I help you? : "))

if (choice==1):
    key=keys[0]
    print(dict[key])
elif (choice==2):
    key=keys[1]
    print(dict[key])
elif (choice ==3):
    query=input("Enter your query : ")
    flag=0
    for i in keys:
        if i in query:
            # index=query.index()
            flag=1
            print(dict[i])
        # else:
        #     print("Sorry! I don't understand your query")
    if flag==0:
        print("Sorry! I don't understand your query")


