
#Name    :- Mokate Om Ranjeet
#program :-   Paswword Genrator
#Date    :-  4 August 2022(THU)





import random
    
alpha_list =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]  #list create karun ghetlay
digit_list =['0','1','2','3','4','5','6','7','8','9']
symbol_list=['!','@','#','$','%','^','&','*']

password = []               #Empty password list create 
passwrd = ''                # empty str ghetli
alpha_count = int(input("Enter how many aplhabates you want in your password =  "))    # user la count vicharla
digit_count  = int(input("Enter how many digit you want in your password =  "))
symbol_count = int(input("Enter how many symbol you want in your password =  "))

for i in range(alpha_count):                # for loop lavla tayla count patvla mhnje tevdhay vela to firen 
    value = random.choice(alpha_list)       #list madhun random choice kela ani value madhe store kela 
    password.append(value)                  #value madhe store kele la password ya list madhe add kela "append" chay help ne 

for i in range(digit_count):
    value = random.choice(digit_list)
    password.append(value)

for i in range(symbol_count):
    value = random.choice(symbol_list)
    password.append(value)


random.shuffle(password)                    #shuffle chy help ne generate zhalela password mix karto (ex --> ['e','#','4','4','e','r','#','$','d'])

for i in password:                      #generate zhalela pass ha list for madhe hota mhnun all elemtnt vist karun tayla str madhe convert kela ani passrd ya madhe srore kela 
    passwrd = passwrd+str(i)

    
print(f"your password is = {passwrd}") # genrated passsword print kela 
