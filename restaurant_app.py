# /*
#  * Copyright (C) 2020  Abdullah Azzam Olcay
#  * Gebze Technical University
#  * Lınkedin: https://tr.linkedin.com/in/abdullah-azzam-olcay-613453183
#  *
#  *
#  * Restaurant bill app:
#  *
#  *
#  * Please do not remove this header.
#  * */
import time
import os

clients = dict()

n = int(input("Enter the number of clients:\n"))

for i in range(n):
    k = i
    clients[k] = 0

def add_to_bill():
    clients_no = int(input("Enter the client number:\n"))
    clients_bill = clients[clients_no]
    add_bill = float(input("Enter the added bill:\n"))
    sum = clients_bill + add_bill
    clients[clients_no] = sum
    print("Please wait, the program calculate the bill")
    time.sleep(1)
    print("The new price {} for clients {}".format(clients[clients_no],clients_no))
def remove_bill():
    clients_no = int(input("Enter the client number:\n"))
    clients_bill = clients[clients_no]
    rem_bill = float(input("Enter the removed bill:\n"))
    sum = clients_bill - rem_bill
    if sum < 0:
        sum = 0
        print("Please wait, the program calculate the bill...\n")
        time.sleep(1)
        clients[clients_no] = sum
        print("Please wait, the program calculate the bill")
        time.sleep(1)
        print("The new price {} for clients {}".format(clients[clients_no], clients_no))
    else:
        print("Please wait, the program calculate the bill...\n")
        time.sleep(1)
        clients[clients_no] = sum
        print("Please wait, the program calculate the bill")
        time.sleep(1)
        print("The new price {} for clients {}".format(clients[clients_no], clients_no))

def document_control(document_name):
    try:
        document = open(document_name,"r")
        data = document.read()
        data = data.split("\n")
        data.pop()
        document.close()
        flag = True
    except:
        document = open(document_name,"w")
        document.close()
        print("This document's first working\n")
        flag = False
    if flag:
        for i in enumerate(data):
            clients[i[0]] = float(i[1])
    else:
        pass

def document_update():
    document = open("restaurant_bill.txt","w+")
    for i in range(n):
        string = "Client's number is {} and the bill is {}".format(i, clients[i])+"\n"
        document.write(string)
    document.close()

def menu():
    document_control("restaurant_bill.txt")
    while True:
        os.system("clear")
        print("""
        MENU
        [1] Checking Bills 
        [2] Addition to Bill
        [3] Remove the bill
        [Q] Quit
        """)
        y = input("Enter the number you want on menu:\n")
        if y == "1":
            for i in range(n):
                k = i
                print("Client's number is {} and the bill is {}".format(k,clients[k]))
        elif y == "2":
            add_to_bill()
        elif y=="3":
            remove_bill()
        elif y == "q" or y=="Q":
            print("Please wait to quit in the system...")
            time.sleep(2)
            quit()
        document_update()
menu()