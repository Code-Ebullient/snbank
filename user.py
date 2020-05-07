#Importing the modules that will be used within the program
from random import randint
import os
import random
class Staff:
    accNumber: ''

    #The first loop on program run
    def mainloop(self):
        print(' 1) STAFF LOGIN')
        print(' 2) CLOSE APP')
        choice = input(">>>")
        if choice == '1':
            self.loginDetails()
        elif choice == '2':
            print('Thanks for checking out our banking system')
            exit()
        else:
            print('Error try again later')

    # read file and append it to an array
    def readFile(self, filename):
        file = open(filename, 'r')
        lines = file.readlines()
        details = []
        for i in range(len(lines)):
            details.append(lines[i].rstrip('\n').split(";"))
        return details

    # checking if a user exit in the staff.txt file. If yes, then log the staff in
    def loginDetails(self):
        self.user = input('Enter your username: ')
        self.password = input('Your password please: ')
        staffDetails = self.readFile('staff.txt')
        loginCreds = False
        for i in range(len(staffDetails)):
            if self.user and self.password in staffDetails[i]:
                loginCreds = True
        if loginCreds:
            self.loggingStaff()
        else:
            print("Sorry you entered an incorrect login credentials")
    def loggingStaff(self):
        print('\t SELECT FROM THESE OPTIONS')
        print('\t1. Create New Bank Account')
        print('\t2. Check Account Details')
        print('\t3. Logout')
        choice = input(">>>")
        if choice == '1':
            self.createAccount()
        elif choice == '2':
            Staff.accNumber = input('Your account number please: ')
            self.checkAccount(Staff.accNumber)
        elif choice == '3':
            self.mainloop()
        else:
            print('Error!! try again')

    #generate a random 10 digit number
    def generateAccNumber(self):
        stringLength = 10
        return ''.join(["{}".format(randint(0, 9)) for num in range(0, stringLength)])

    #Creating a new bank details
    def createAccount(self):
        self.accName = input('Enter your name: ')
        self.accType = input('Enter the type of account, [current/saving]: ')
        self.email = input('Your email, please: ')
        self.balance = input('Your opening balance is what? ')
        Staff.accNumber = self.generateAccNumber()
        customerFile = open("customer.txt", "a")
        lines = [
            self.accName + ';',
            self.accType + ';',
            self.email + ';',
            self.balance + ';',
            Staff.accNumber + '\n'
        ]
        for line in lines:
            customerFile.writelines(line)
        customerFile.close()
        print("\n Acount Created successfully.")
        print("\n This is your account number: %s" % Staff.accNumber)

    #Displays the account info if staff what's to check
    def checkAccount(self, accNumber):
        customerDetails = self.readFile('customer.txt')
        customerDetail = ''
        for i in range(len(customerDetails)):
            if accNumber in customerDetails[i]:
                customerDetail = customerDetails[i]
        if customerDetail != '':
            print('Account name: ', customerDetail[0])
            print('Account Type: ', customerDetail[1])
            print('Acount Email: ', customerDetail[2])
            print('Account balance is: ', customerDetail[3])
        else:
            print("sorry you entered an incorrect account number")
emp = Staff()
emp.mainloop()
