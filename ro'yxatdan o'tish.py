# -*- coding: utf-8 -*-


Emails=["olim","sardor","abror"]
parols=["0","1","2"]

a=input("do you want to log in  register\n>>>").lower()
if a=="log in":
        emailcheck=input("enter your login\n>>>")
        i=0
        lenemail=len(Emails)
        for i in range(lenemail):
            if emailcheck==Emails[i]:
                parolchek=input("Enter your parol\n>>>")
                if parolchek==parols[i]:
                   print( "you  entered successfully")
                   break
                else :
                    print("you entered wrongly")
            else:
                if i==lenemail-1:
                   print ("you didn't log in")
if a=="register":
        newlogin=input("write your login\n>>>")
        j=0
        lenemail=len(Emails)
        for j in range(lenemail):
            if newlogin == Emails[j]:
               print("this login using")
               break
            else: 
               if j==lenemail-1:
                     Emails.append(newlogin)
                     newparol=input("create new parol\n>>>")
                     renewparol=input("enter your parol again\n>>>")
                     if newparol==renewparol:
                        parols.append(newparol)
                        print("you registered successfully ")
                        print("your login-",Emails[-1],"\nYour parol-",parols[-1])
                     else :
                        print("Repaet the parol correctly\n>>>")
                
               else:
                   continue

