
# simple contacts book 

contacts = {}

while True : 
    print('****Welcome to contacts book****')
    print("1. Create contect :")
    print("2. Veiw   contect :")
    print("3. Update contact :")
    print("4. Delete contect :")
    print("5. Search contect :")
    print("6. Count  contect :")
    print("7. Exit :")
    
    
    choice = int(input("Enter your choice = "))
    
    if choice == 1:
        name = input('Enter your name = ')
        if name in contacts: 
            
          print(f'Contact name {name} already exists')
        else :
            age = input ('Enter age = ')
            email = input('Enter email = ')
            mobile = input('Enter mobile = ')
            contacts[name] = {'age': int (age ) , 'email':email , 'mobile':mobile}
            print(f'Contact name {name } has been created succesfully!') 
    elif choice == 2:
        name = input ('Enter contact name to veiw = ')
        if name in contacts : 
            contact = contacts[name]
            print (f'Name :{name}, Age :{age}, Mobile Number:{mobile},Email : {email}') 
        else :
            print("Contact not found ") 
            
    elif choice == 3:
        name = input("Enter name to update contact = ")
        if name in contacts:
         contact = contacts [name ]
         age = input ('Enter age update  = ')
         email = input('Enter email  update = ')
         mobile = input('Enter mobile update =')
         
        else:
            print ('Contact not found ')
            
         
    elif choice == 4 :
        name = input('Enter the name to deleted contact = ')
        if name in contacts:
             del contacts[name]
             print(f'Contact name {name } has been  deleted succesfully')
        else:
            print ('Contact not found ')
            
    elif choice == 5:
       search_name = input("Enter the name to search contact = ")
       found = False 
       for name, contact in contacts .items():
           if search_name.lower() in name.lower():
               print(f'Found- Nmae {name }, Age:{age}, Mbolile Number :{mobile} , Email:{email}')
               found = True
           if not found :
               print('No contact found with that name ')
    elif choice == 6:
        print(f'Total contacts in your book :{len(contacts)}')  
        
    elif choice == 7:
        print('Thanks!')    
        break
    else:
        
        print('Invalid input , please enter input 1 to 7 !')
               
           
           
        
                         
        
        
            


        
        
