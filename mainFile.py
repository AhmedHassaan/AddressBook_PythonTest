import fileinput


class ahmed():
    def __init__(self,firstName=None,lastName=None,address=None,number=None):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.number = number


def add():
    ahmedd = ahmed()
    ahmedd.firstName = str(input("Enter the First name"))
    ahmedd.lastName = str(input("Enter the Last name"))
    ahmedd.number = str(input("Enter the number"))
    ahmedd.address = str(input("Enter the address"))
    file = open("testFile.txt",'a')
    file.write(ahmedd.firstName + "$")
    file.write(ahmedd.lastName + "$")
    file.write(ahmedd.address + "$")
    file.write(ahmedd.number + "\n")
    file.close()

def display():
    with open("testFile.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    for i in range(0,len(content)):
        temp = content[i].split('$')
        aa = ahmed(temp[0],temp[1],temp[3],temp[2])
        print(i+1)
        print(" Name: " + aa.firstName + " " + aa.lastName + "\n")
        print("number: " + aa.number + "\n")
        print("addrress: " + aa.address + "\n")

def edit():
    with open("testFile.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    allContactData = []
    for i in range(0,len(content)):
        temp = content[i].split('$')
        aa = ahmed(temp[0],temp[1],temp[3],temp[2])
        allContactData.append(aa)
        print(i+1)
        print(" Name: " + aa.firstName + " " + aa.lastName + "\n")
        print("number: " + aa.number + "\n")
        print("Address: " + aa.address + "\n")
    indexToUpdate = int(input("Enter the number of contact that you want to update"))
    print("1- first name \n 2-first name \n 3- number \n 4-address")
    attToUpdate = int(input("enter the number you want to update: "))
    s = ""
    aaaaa = str(input("Enter the new value: "))
    if attToUpdate==1:
        s= aaaaa + "$" + allContactData[indexToUpdate-1].lastName + "$"+ allContactData[indexToUpdate-1].number + "$"+ allContactData[indexToUpdate-1].address
    if attToUpdate==2:
        s= allContactData[indexToUpdate-1].firstName + "$" + aaaaa + "$"+ allContactData[indexToUpdate-1].number + "$"+ allContactData[indexToUpdate-1].address
    if attToUpdate==3:
        s= allContactData[indexToUpdate-1].firstName + "$" + allContactData[indexToUpdate-1].lastName + "$"+ aaaaa + "$"+ allContactData[indexToUpdate-1].address
    if attToUpdate==4:
        s= allContactData[indexToUpdate-1].firstName + "$" + allContactData[indexToUpdate-1].lastName + "$"+ allContactData[indexToUpdate-1].number + "$"+ aaaaa
    print(s + "\n")
    print(content[indexToUpdate-1] + "\n")
    for line in fileinput.input('testFile.txt', inplace=True):
        print(line.rstrip().replace(content[indexToUpdate-1], s))


def main():
    while(True):
        choice = int(input("Enter 1 to enter a new contact \n 2 to display all contact \n 3 to edit a contact"))
        print(choice)
        if choice == 1:
            add()
        elif choice == 2:
            display()
        elif choice == 3:
            edit()
        a = str(input("Enter y to continue"))
        if a != 'y':
            break


if __name__ == '__main__':
    main()