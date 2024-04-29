import os
import time

def all_list(): #this is the list of all data.
    global places_list
    places_list = ['UTAR','Meadow park','New town night market','Econsave','Tesco','E-hub','KTM station','Kampar Putra Sentral Terminal','Westlake Villas','mmCineplexes']#place
    global coordinate_list
    coordinate_list = [0,5,8,9,15,9.5,13,17,3,11]# x point
    global admin_id_list
    admin_id_list = ['sutian','keanyew','jeremy','junbiao','weiyee'] ## admin id
    global admin_pw_list
    admin_pw_list = ['sutian123','keanyew123','jeremy123','junbiao123','weiyee123']## admin password
    global user_id_list
    user_id_list = ['sutian','keanyew','jeremy','junbiao','weiyee']##user id
    global user_pw_list
    user_pw_list = ['sutian123','keanyew123','jeremy123','junbiao123','weiyee123']##user password
    global distance
    distance = 0 #distance
    global transport_list #####New added
    transport_list = ['Walking','Bicycle','Car','Motocycle','Grab']
    global time_rate
    time_rate = [12,7,3,5,3] #in minute/km

def confirmation():# this function is for confirmation
    os.system('cls')
    confirm = input('\n\n\n\n\t\t\t\t\t----Confirmation----\n\t\t\tAre you sure want proceed this action? (Y/N) = ')
    if confirm == 'Y' or confirm == 'y':#choose yes then add or delete item in list
        os.system('cls')
        loading10 = 'Saving..'
        dot10 = str('.')
        for dots in range(1,5):#decoration purpose
            print('\n\n\n\n\t\t\t\t',loading10)
            time.sleep(0.15)
            os.system('cls')
            loading10 = loading10 + dot10
        print('\n\n\n\n\t\t\t\tSaving complete!') 
        time.sleep(0.5)
        os.system('cls')
        return True
    elif confirm == 'N' or confirm == 'n':#choose no then return back admin_page
        os.system('cls')
        loading11 = 'Returning back to first page..'
        dot11 = str('.')
        for dots in range(1,5):#decoration purpose
            print('\n\n\n\n\t\t\t\t',loading11)
            time.sleep(0.15)
            os.system('cls')
            loading11 = loading11 + dot11
        os.system('cls')
        admin_page()
    else:#if input error then return false
        os.system('cls')
        return False

def adduser(): # this function is adduser
    number111 = 0
    print('\n\t\t\t\t----Adding user page----')
    print('\t\t\t\t-------------------')
    print('\t\t\t\tUsername that exist')
    print('\t\t\t\t-------------------')
    for user in user_id_list:#showing user in list
        print('\t\t\t\t',number111,'.',user)
        number111 = number111 + 1
    print('\n\t\t\t\t!!!Username and password only can be number or abc !!!\n')
    add_user_id = input('\n\t\t\t\tPlease enter a username = ') 
    add_user_pw = input('\n\t\t\t\tPlease enter your password = ')
    if add_user_id.isalnum() == True and add_user_pw.isalnum() == True:#ensure user and password input are number and abc only
        os.system('cls') 
        while confirmation() == False:# if the confirmation input is error then loop back
            print('\n\n\n\n\t\t\tINVALID INPUT')
            time.sleep(0.6)
            os.system('cls')
        user_id_list.append(add_user_id)#if confirmation choose yes then proceed this code
        user_pw_list.append(add_user_pw)#if confirmation choose yes then proceed this code
        admin_page()#after add user in list return back to admin_page
    else:#if not abc or number then return false
        return False

def addtransportation(): #this function is addtransportation
    print('\n\t\t\t\t----Adding transportation page----')
    print('\t\t\t\t--------------------')
    print('\t\t\t\tTransport that exist')
    print('\t\t\t\t--------------------')
    number2 = 0
    for transport in transport_list:#showing transport in list
        print('\t\t\t\t',number2,'.',transport,'(',time_rate[number2],"min/km"')')
        number2 += 1
    print('\n\t\t\t\t!!!Time rate only can be number!!!\n')
    add_transport = input('\n\t\t\t\tEnter a transport that you want to add = ')
    add_rate = input('\n\t\t\t\tEnter time rate(min/km) = ')
    if add_rate.isnumeric() == True and add_transport.isspace() == False and add_transport != '': #ensure transport(abc and number) and timerate(number) input are correct
        os.system('cls')
        while confirmation() == False:# if the confirmation input is error then loop back
            print('\n\n\n\n\t\t\tINVALID INPUT')
            time.sleep(0.6)
            os.system('cls')
        transport_list.append(add_transport)#if confirmation choose yes then proceed this code
        time_rate.append(int(add_rate))#if confirmation choose yes then proceed this code
        admin_page()#after add transport in list return back to admin page
    else:#if input wrongly then return False
        return False

def delete_user(): #this function is delete user

    print('\n\t\t\t\t----Deleting user page----')
    print('\t\t\t\t---------------')
    print('\t\t\t\tuser that exist')
    print('\t\t\t\t---------------')
    number3 = 0
    for user in user_id_list:#showing user in list
        print('\t\t\t\t',number3,'.',user)
        number3 = number3 + 1
    print('\n\t\t\t\tPlease enter a number to represent user delete\n\t\t\t\tPlease choose from 0 to',len(user_id_list)-1)
    delete_user = input('\t\t\t\tPlease enter your number = ')
    if delete_user.isdigit() == True:#ensure input only number
        delete_user = int(delete_user)#make input become integer
        if delete_user < len(user_id_list):#if input is smaller or equal than element in the list the proceed
            os.system('cls')
            while confirmation() == False:# if the confirmation input is error then loop back
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
            del user_id_list[delete_user]#if confirmation choose yes then proceed this code
            del user_pw_list[delete_user]#if confirmation choose yes then proceed this code
            admin_page()#after delete than return back to admin_page
        else:#if input is bigger than element in list then return back
            return False
    else:# if input are not number then return False
        return False

def delete_transport():#this func is delete transport

    print('\n\t\t\t\t----Deleting transportation page----')
    print('\t\t\t\t-------------------------')
    print('\t\t\t\tTransportation that exist')
    print('\t\t\t\t-------------------------')
    nomber = 0
    for transport in transport_list:#showing transport in list
        print('\t\t\t\t',nomber,'.',transport,'(',time_rate[nomber],' min/km)')
        nomber = nomber + 1
    print('\t\t\t\tPlease choose a number from 0 to',len(transport_list)-1,'to represent the transport')
    delete_transport1 = input('\t\t\t\tPlease enter your number = ')
    if delete_transport1.isdigit() == True:#ensure input is only number
        delete_transport1 = int(delete_transport1)#change input to integer
        if delete_transport1 < len(transport_list):#if input is smaller or equal than element in list
            os.system('cls')
            while confirmation() == False:#if the confirmation input is error then loop back
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
            del transport_list[delete_transport1]#if confirmation choose yes then proceed this code
            del time_rate[delete_transport1]#if confirmation choose yes then proceed this code
            admin_page()#after delete transport then return backk to admin_page
                    
        else:#if input is larger than element in the list then return false
            return False
    else:#if input is not number then return false
        return False
                    
def deleteplace():#this func is delete place
    no = 0 
    print('\n\t\t\t\t----Deleting place page----')
    print('\t\t\t\t----------------')
    print('\t\t\t\tPlace that exist')
    print('\t\t\t\t----------------')
    for places in places_list:#show place in list
        print('\t\t\t\t',no,'.',places)
        no = no + 1
    print('\t\t\t\tPlease enter a number from 0 to ',len(places_list) - 1,'to represent the place',)
    place_delete = input('\t\t\t\tPlease enter your number = ')
    if place_delete.isnumeric() == True:#to ensure input is only number
        if int(place_delete) < len(places_list):#ensure input is smaller or equal to the elemnt in list
            os.system('cls')
            while confirmation() == False:# if the confirmation input is error then loop back
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
            del places_list[int(place_delete)]#if confirmation choose yes then proceed this code
            del coordinate_list[int(place_delete)]#if confirmation choose yes then proceed this code
            admin_page()#after delete place then return back to admin_page
        else:#if input is larger than element in list then return false
            return False
    else:#if input is not number then return false
        return False

def addplace():#this func is addplace
    print('\n\t\t\t\t----Adding place page----')
    print('\t\t\t\t-----------------')
    print('\t\t\t\tPlaces that exist')
    print('\t\t\t\t-----------------')
    no = 0
    for place in places_list:#showing place in list
        print('\t\t\t\t',no,'.',place,'(',coordinate_list[no],')')
        no = no + 1
    print('\n\t\t\t\t!!!Place\'coordianate only can be number!!!\n')
    add_place = input('\n\t\t\t\tEnter a place that you want to add = ')#add place into places_list
    add_place_x = input('\n\t\t\t\tEnter place\'s coordiante = ')#add place coordinate into coordinate_list
    if add_place_x.isnumeric() == True and add_place.isspace() == False and add_place != '' :#to ensure input place name (abc and number) and x-coordinate (number only) is correct
        while confirmation() == False:#if the confirmation input is error then loop back
            os.system('cls')
            print('\n\n\n\n\t\t\tINVALID INPUT')
            time.sleep(0.6)
            os.system('cls')
        places_list.append(add_place)#if confirmation choose yes then proceed this code
        coordinate_list.append(int(add_place_x))#if confirmation choose yes then proceed this code
        admin_page()#after adding to the list then return back to admin_page
    else:#if  wrong  input return False
        return False

def admin_page():#this is admin page
    print('\n\n\t\t\t\t-----------------------')
    print('\t\t\t\tWelcome to admin system')
    print('\t\t\t\t-----------------------')
    print('\n\t\t\t\t1.Add places\n\t\t\t\t2.Add transportation\n\t\t\t\t3.Add user\n\t\t\t\t4.Delete places\n\t\t\t\t5.Delete transportation\n\t\t\t\t6.Delete user\n\t\t\t\t0.Return back to login page')#option
    option3 = input('\n\n\t\t\t\tChoose your option = ') #choose option
    loop = 'false'#loop start
    while loop == 'false':
        if option3 == '1':#option1 for add place
            os.system('cls')#clear page
            loop = 'true'#loop break         
            while addplace() == False:
                os.system('cls')
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')

        elif option3 == '2': #option2 for addtransportation
            loop = 'true'
            os.system('cls')          
            while addtransportation() == False:
                os.system('cls')
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')

        elif option3 == '3':#option 3 for add user
            loop = 'true'#  loop break
            os.system('cls')#clr   
            while adduser() == False:
                os.system('cls')
                print('\n\n\n\n\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')

        elif option3 == '4':#option4 for delete place
            loop = 'true'
            os.system('cls')
            if len(places_list) == 1:
                print('\n\n\n\n\t\t\t\tLeft one place cannot be deleted !')
                time.sleep(1)
                os.system('cls')
                admin_page()
            else:
                while deleteplace() == False:
                    os.system('cls')
                    print('\n\n\n\n\t\t\tINVALID input')
                    time.sleep(0.6)
                    os.system('cls')

        elif option3 == '5':#option 5 for delete transportation!
            loop = 'true'
            os.system('cls')
            if len(transport_list) == 1:
                print('\n\n\n\n\t\t\t\tLeft one transportation cannot be deleted !')
                time.sleep(1)
                os.system('cls')
                admin_page()
            else:
                while delete_transport() == False:
                    os.system('cls')
                    print('\n\n\n\n\t\t\tINVALID input')
                    time.sleep(0.6)
                    os.system('cls')     

        elif option3 == '6': #option 6 for delete user
            loop = 'true'
            os.system('cls')
            if len(user_id_list) == 1:
                print('\n\n\n\n\t\t\t\tLeft one user cannot be deleted !')
                time.sleep(1)
                os.system('cls')
                admin_page()
            else:
                while delete_user() == False:
                    os.system('cls')         
                    print('\n\n\n\n\t\t\t\tInvalid input!')
                    time.sleep(0.6)
                    os.system('cls')

        elif option3 == '0':#option 0 for return to login page
            loop = 'true'
            os.system('cls')
            login()
              
        else:## if enter wrong input then renter
            os.system('cls')
            print('\n\n\t\t\t\t-----------------------')
            print('\t\t\t\tWelcome to admin system')
            print('\t\t\t\t-----------------------')
            print('\n\t\t\t\t1.Add places\n\t\t\t\t2.Add transportation\n\t\t\t\t3.Add user\n\t\t\t\t4.Delete places\n\t\t\t\t5.Delete transportation\n\t\t\t\t6.Delete user\n\t\t\t\t0.Return back to login page')#option
            option3 = input('\n\n\t\t\t\tChoose your option = ') #choose option

def login():# this is login page
    print('\t\t\t\t---------------------------')
    print('\t\t\t\t   Welcome to the system')
    print('''\t\t\t\t---------------------------\n\t\t\t\t 1) Login as a user       \n\t\t\t\t 2) Login  as an admin    \n\t\t\t\t 3) Exit program          \n\t\t\t\t---------------------------''')##option
    login_option = input('\n\t\t\t\tPlease choose a number =  ')#choose option
    loop = 'false'#start a loop
    while loop == 'false':
        if login_option == '1':#option 1 for user
            os.system("cls")
            print('\n\n\n\t\t\t\t----------------------------------')
            print('\t\t\t\tPlease enter your ID and password')
            print('\t\t\t\t----------------------------------')
            user_id = input('\n\t\t\t\tID:')##enter id
            user_pw = input('\n\t\t\t\tPASSWORD:')##enter password
            while loop == 'false':
                if user_id in user_id_list and user_pw == user_pw_list[user_id_list.index(user_id)]:##if user id and passwword are same then proceed ,list is to make sure user id and password are same  
                    os.system("cls")
                    loading1 = 'Login..'
                    dot1 = str('.')
                    for dots in range (1,5):##loading dot can increase
                        print('\n\n\n\n\n\n\n\t\t\t\t\t',loading1)
                        time.sleep(0.15)
                        os.system("cls")
                        loading1 = loading1 + dot1
                    os.system("cls")
                    print('\n\n\n\n\t\t\t\tLOGIN SUCESSFULLY !')
                    time.sleep(1)
                    os.system("cls")
                    print('\n\n\n\n\t\t\t\t\tWELCOME! ',user_id.capitalize())#welcome user
                    time.sleep(1.0)
                    os.system('cls')
                    loop = 'true'#loop break
                    while destination() == False:#call destination func if input error then run again
                        os.system('cls')
                        print('\n\n\n\t\t\t\tINVALID INPUT')
                        time.sleep(0.6)
                        os.system('cls')
                else:##if wrong password or id
                    os.system("cls")
                    loading2 = 'Login..'
                    dot2 = str('.')
                    for dots in range(1,5):##loading dot can increase
                        print('\n\n\n\n\n\n\n\t\t\t\t\t',loading2)
                        time.sleep(0.15)
                        os.system("cls")
                        loading2 = loading2 + dot2
                    os.system("cls")
                    print('\n\n\n\n\n\n\n\t\t\t\t\tINVALID LOGIN\n')
                    print('\t\t\t\t\tPLEASE TRY AGAIN')
                    time.sleep(0.6)
                    os.system("cls")
                    print('\n\n\n\t\t\t\t----------------------------------')
                    print('\t\t\t\tPlease enter your ID and password')
                    print('\t\t\t\t----------------------------------')##return back the login page
                    user_id = input('\n\t\t\t\tID:')
                    user_pw = input('\n\t\t\t\tPASSWORD:')
            loop = 'true'#stop the loop
            
        elif login_option == '2':## option 2 for admin
            os.system("cls")
            print('\n\n\n\t\t\t\t----------------------------------')
            print('\t\t\t\tPlease enter your ID and password')
            print('\t\t\t\t----------------------------------')
            admin_id = input('\n\t\t\t\tID:')
            admin_pw = input('\n\t\t\t\tPASSWORD:')
            while loop == 'false':
                if admin_id in admin_id_list and admin_pw == admin_pw_list[admin_id_list.index(admin_id)]:##if admin id and passwword are same then proceed,list is to make sure user id and password are same  
                    os.system("cls")
                    loading3 = 'Login..'
                    dot3 = str('.')
                    for dots in range (1,5):## loading dot can increase
                        print('\n\n\n\n\t\t\t\t',loading3)
                        time.sleep(0.15)
                        os.system("cls")
                        loading3 = loading3 + dot3
                    os.system("cls")
                    print('\n\n\n\n\t\t\t\tLOGIN SUCESSFULLY')
                    time.sleep(1)
                    os.system("cls")
                    print('\n\n\n\n\t\t\t\tWELCOME !!\n\t\t\t\t', admin_id.capitalize())
                    time.sleep(0.6)
                    os.system('cls')
                    loop = 'true'#stop the loop
                    admin_page()
                else:##if wrong password or id
                    os.system("cls")
                    loading4 = 'Login..'
                    dot4 = str('.')
                    for dots in range (1,5):#loading dot can increase
                        print('\n\n\n\n\t\t\t\t',loading4)
                        time.sleep(0.15)
                        os.system("cls")
                        loading4 = loading4 + dot4
                    os.system("cls")
                    print('\n\n\n\n\t\t\t\tINVALID LOGIN\n')
                    print('\t\t\t\tPLEASE TRY AGAIN')
                    time.sleep(0.6)
                    os.system("cls")
                    print('\n\n\n\t\t\t\t----------------------------------')
                    print('\t\t\t\tPlease enter your ID and password')
                    print('\t\t\t\t----------------------------------')#return back to login
                    admin_id = input('\n\t\t\t\tID:')#renter user name
                    admin_pw = input('\n\t\t\t\tPASSWORD:')#renter password
            loop = 'true'# stop the loop
        elif login_option == '3':##exit program
            os.system("cls")
            print('\n\n\n\n\t\t\t\tGoodbye in 3')
            time.sleep(0.5)
            os.system("cls")
            print('\n\n\n\n\t\t\t\tGoodbye in 2')
            time.sleep(0.5)
            os.system("cls")
            print('\n\n\n\n\t\t\t\tGoodbye in 1')
            time.sleep(0.5)
            os.system("cls")
            print('\n\n\n\n\t\t\t\tGoodbye~~~~~~')
            loop = 'true'
            exit()
            
        else:
            os.system("cls")##if enter except 1,2,3 then return back the login page
            loading5 = 'Please enter a number (1/2/3) to proceed.'
            dot5 = str('.')
            for dots in range(1,5):
                print('\n\n\n\n\n\n\n\t\t\t\t',loading5)
                time.sleep(0.15)
                os.system("cls")
                loading5 = loading5 + dot5
            os.system("cls")
            print('\t\t\t\t---------------------------')
            print('\t\t\t\t   Welcome to the system')
            print('''\t\t\t\t---------------------------\n\t\t\t\t 1) Login as a user       \n\t\t\t\t 2) Login  as an admin    \n\t\t\t\t 3) Exit program          \n\t\t\t\t---------------------------''')##option
            login_option = input('\n\t\t\t\tPlease choose a number =  ')

def choose_transport():#this is choose transport page
    global result
    global hours
    global minutes
    print('\n\n\t\t\t\t-------------------------')
    print("\t\t\t\tPlease choose a transport")
    print('\t\t\t\t-------------------------\n')
    print("\t\t\t\tTypes of transport")
    number1 = 0
    result = ''
    rate = 0 #min/km
    for transport in transport_list:
        print("\t\t\t\t",number1,".",transport)
        number1 += 1
    choice_transport = input("\n\t\t\t\tPlease enter your choice of tranportation in number: ")
    if choice_transport.isdigit() == True:#ensure input is all number
        choice_transport = int(choice_transport)
        if choice_transport >= 0 and choice_transport <= len(transport_list)-1:
            result = transport_list[choice_transport]
            rate = time_rate[choice_transport]
            time1 = distance * rate
            hours = time1 // 60
            minutes = time1 % 60
            os.system('cls')## clear page
            loading14 = 'Calculating..' 
            dot14 =str( '.')
            for dots in range (1,5): 
                print('\n\n\n\n\t\t\t\t',loading14)
                time.sleep(0.15)
                os.system('cls')
                loading14 = loading14 + dot14
            os.system('cls')#clear page        
            caltime()   
        else:
            return False
    else:
        return False

def caldistance():#this is page show distance
    os.system('cls')
    print('\n\n\t\t\t\t----------------------------------------------------------------------')
    print('\t\t\t\tThe distance between',place1,'and',place2,'is',distance,'KM') ##distance result
    print('\t\t\t\t----------------------------------------------------------------------')
    print('\n\t\t\t\tEnter 1 to continue calculate the distance') #option1
    print('\t\t\t\tEnter 2 to estimate the time travel') #option2
    print('\t\t\t\tEnter 3 to return back login page') #option3
    print('\t\t\t\tEnter 0 to exit the program\n') #option0
    option4 = input('\t\t\t\tChoose a number (1/2/3/0) to represent your choice: ')
    while True:
        if option4 == '1':#choose back to destination
            os.system('cls')
            while destination() == False:
                os.system('cls')
                print('\n\n\n\t\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
        elif option4 == '2':#go to choose transport
            os.system('cls')
            while choose_transport() == False:
                os.system('cls')
                print('\n\n\n\t\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
        elif option4 == '3':#choose back to login page
            os.system('cls')
            login()
        elif option4 == '0':# exit program
            os.system('cls')
            print('\n\n\n\t\t\t\tGOODBYE~')
            time.sleep(0.5)
            exit()
        else:
            os.system('cls')
            print('\n\n\n\t\t\t\tINVALID INPUT')
            time.sleep(0.4)
            os.system('cls')
            print('\n\n\t\t\t\t----------------------------------------------------------------------')
            print('\t\t\t\tThe distance between',place1,'and',place2,'is',distance,'KM') ##distance result
            print('\t\t\t\t----------------------------------------------------------------------')
            print('\n\t\t\t\tEnter 1 to continue calculate the distance') #option1
            print('\t\t\t\tEnter 2 to estimate the time travel') #option2
            print('\t\t\t\tEnter 3 to return back login page') #option3
            print('\t\t\t\tEnter 0 to exit the program\n') #option0
            option4 = input('\t\t\t\tChoose a number (1/2/3/0) to represent your choice: ')
        
def destination():#this is page choose place
    print('\n\t\t\t\t-----Welcome to Kampar-----\n')
    number = 0 
    for place in places_list: # show place in list
        print('\t\t\t\t',number,'.',place)
        number = number + 1   
    print('\n\t\t\t\tChoose a number(0-',len(places_list)-1,')to represent the place.')
    starting = input('\n\t\t\t\tPlease enter your starting point:')
    ending = input('\t\t\t\tPlease enter your ending point:')
    if starting.isdigit() == True and ending.isdigit() == True:#ensure input is correct
        starting = int(starting)
        ending = int(ending)
        if starting < len(places_list) and ending <len(places_list) and starting != ending:
            os.system('cls')
            distance1 = coordinate_list[starting]
            distance2 = coordinate_list[ending]
            global distance
            global place1
            global place2
            distance = abs(distance2 - distance1)
            place1 = places_list[starting]
            place2 = places_list[ending]
            loading6 = 'Calculating..' 
            dot6 =str( '.')
            for dots in range (1,5): ## let the calculating dot can increase, prevent user thought system hang(decoration)
                print('\n\n\n\n\t\t\t\t',loading6)
                time.sleep(0.15)
                os.system('cls')
                loading6 = loading6 + dot6
            os.system('cls')#clear page
            caldistance()
        else:
            return False
    else:
        return False

def caltime():#this is place show time travel
    print('\n\n\t\t\t\t-------------------------------------------------------------------')
    print("\t\t\t\tYour chosen transport is " , result,'from',place1, 'to' ,place2)
    print("\t\t\t\tTime needed to reach the destination is %d hours and %02d minutes" %(hours, minutes))
    print('\t\t\t\t-------------------------------------------------------------------')
    print('\n\t\t\t\t1.Return back to choose destination\n\t\t\t\t2.Return back to choose another transportation\n\t\t\t\t3.Return back to login page\n\t\t\t\t0.Exit the program')
    option11 = input('\n\t\t\t\tChoose a number(1/2/3/0) to represent your choice :')
    while True:
        if option11 == '1':
            os.system('cls')
            while destination() == False:
                os.system('cls')
                print('\n\n\n\t\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
                
        elif option11 == '2':
            os.system('cls')
            while choose_transport() == False:
                os.system('cls')
                print('\n\n\n\t\t\t\tINVALID INPUT')
                time.sleep(0.6)
                os.system('cls')
                
        elif option11 == '3':
            os.system('cls')
            login()

        elif option11 == '0':
            os.system('cls')
            print('\n\n\n\n\t\t\tGOODBYE~')
            time.sleep(0.5)
            exit()
        else:
            os.system('cls')
            print('\n\n\n\t\t\t\tINVALID INPUT')
            time.sleep(0.4)
            os.system('cls')#input wrong go back
            print('\n\n\t\t\t\t-------------------------------------------------------------------')
            print("\t\t\t\tYour chosen transport is " , result,'from',place1, 'to' ,place2)
            print("\t\t\t\tTime needed to reach the destination is %d hours and %02d minutes" %(hours, minutes))
            print('\t\t\t\t-------------------------------------------------------------------')
            print('\n\t\t\t\t1.Return back to choose destination\n\t\t\t\t2.Return back to choose another transportation\n\t\t\t\t3.Return back to login page\n\t\t\t\t0.Exit the program')
            option11 = input('\n\t\t\t\tChoose a number(1/2/3/0) to represent your choice :')

all_list()         
os.system('cls')  #clear all thing in page           
login() # run program
