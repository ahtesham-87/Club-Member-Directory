members = []

def add_member():
    name=input("Enter Name: ")
    domain=input("Enter Domain: ")
    members.append([name,domain])
    print("Member",len(members),"- Name:",name,"Domain:",domain,"added successfully")

def remove_member():
    name=input("Enter Name: ")
    domain=input("Enter Domain: ")
    if [name,domain] in members:
        members.remove([name,domain])
        print("Member removed successfully")
    else:
        print("No such member exists")

def list_members():
    if len(members)>0:
        print("List of all the members:")
        for a in range(len(members)):
            name, domain=members[a]
            print(a+1, name, domain)
        print("--- End of the list ---")
    else:
        print("There are no members to list")

def search_domain():
    domain,c=input("Enter the Domain: "),0
    for a in range(len(members)):
        if members[a][1]==domain:
            print(members[a][0])
            c+=1
    if c==0:
        print("No member of such domain exists")

functions=[add_member, remove_member, list_members, search_domain]

while True:
    print("Menu\n1: Add Member\n2: Remove Member\n3: List all Members\n4: Search by Domain\n5: Exit\nEnter your choice:")
    choice=input()
    if choice in ("1","2","3","4"):
        functions[int(choice)-1]()
    elif choice=="5":
        print("Thankyou for using this program")
        break
    else:
        print("Invalid Choice")
