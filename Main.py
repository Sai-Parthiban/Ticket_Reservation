#Importing the Table Files
from Agent import AGENT
from Bus import BUS
from Tickets import TICKETS
while(1):
    print("\t ___________________________\n\t|           menu            |\n\t|---------------------------|\n\t| Enter 1  -->  Admin Login |\n\t| Enter 2  -->  Agent Login |\n\t| Enter 3  -->  Exit        |\n\t|---------------------------|\n")
    case=int(input("Enter the Case : "))
    if(case==1):
        #Validating the Admin Login and Password from the default single Admin
        if(input("Enter Admin Name : ")=="ADMIN" and input("Enter password : ")=="admin@123"):
            while(1):
                print("\t ___________________________\n\t|           menu-1          |\n\t|---------------------------|\n\t| Enter 1 -->  Add Bus      |\n\t| Enter 2 -->  Add Agent    |\n\t| Enter 3 -->  Logout       |\n\t|---------------------------|\n")
                menu=int(input("\nEnter Menu : "))
                #To Insert the Bus Values 
                if(menu==1):
                    BUS.insert()
                #To Insert the Agent Values
                elif(menu==2):
                    AGENT.insert()
                elif(menu==3):
                    print("\n________________Admin Logged Out_________________\n")
                    break
    elif(case==2):
        agent_name=input("Enter Agent id : ")
        password=input("Enter Agent password : ")
        agent_data=AGENT(Agent_Name=agent_name,Password=password).login()
        agent_id=False
        #Checking whether the given Agent Name and Password exists 
        if(agent_data[0]==agent_name and agent_data[2]==password):
            agent_id=agent_data[3]
        
        if(agent_id!=False):
            while(1):
                print("\t ___________________________\n\t|           menu-2          |\n\t|---------------------------|\n\t| Enter 1  -->  list Bus    |\n\t| Enter 2  -->  Book Ticket |\n\t| Enter 3  -->  Show Book   |\n\t| Enter 4  -->  Logout      |\n\t|---------------------------|\n")
                menu=int(input("\nEnter Menu : "))
                #To display the Bus details
                if (menu == 1):
                    print("list")
                    obj1 = BUS()
                    obj1.display()
                    del obj1
                #To book the tickets 
                elif (menu == 2):
                    obj1 = BUS()
                    Bus_id = input("Enter Bus ID : ")
                    price = obj1.wherebusid(Bus_id)
                    nt = int(input('Enter the no of tickets : '))
                    obj1.booking(nt, Bus_id, agent_id)
                    del obj1
                #To display the Latest Booked Tickets First
                elif (menu == 3):
                    print("Show")
                    obj1 = TICKETS()
                    obj1.reversedisplay()
                    del obj1
                elif(menu==4):
                    print("\n________________Agent Logged Out_________________\n")
                    break
        else:
            print("Invalid User")
    elif case==3:
        print(" !!! Thank You !!!")
        break
