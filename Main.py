from os import name
from GymManager import GymManager
from Customer import Customer

print("Gym Manager Portal")
print("Hello, Please Select a choice from the menu")

def menu():
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Memeber")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("0. Exit")
    print("\nEnter Your Choise: ")

menu()

while(True):
    option = int(input())
    if option == 1:
        name = str(input("Enter Member Name - "))
        age = str(input("Enter Member Age - "))
        gender = str(input("Enter Member Gender - "))
        phoneNo = str(input("Enter Member Phone No. - "))
        email = str(input("Enter Member Emaid Address - "))
        bmi = str(input("Enter Member BMI - "))
        if bmi<'18.5':
            r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Rest','Sun': 'Rest'}
        elif bmi<'25':
             r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio/Abs','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Rest'}
        elif bmi<'30':
             r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Rest','Thu': 'Back','Fri': 'Triceps','Sat': 'Legs','Sun': 'Cardio'}
        elif bmi>='30':
             r={'Mon': 'Chest','Tue': 'Biceps','Wed': 'Cardio','Thu': 'Back','Fri': 'Triceps','Sat': 'Cardio','Sun': 'Cardio'}
        duration = str(input("enter Duration (In Months) - "))
        customer = Customer(name,age,gender,phoneNo,email,bmi,duration)
        GymManager.regimen[phoneNo]=r
        GymManager.addCustomer(customer)

    elif option ==2:
        check_phn=input('Enter phone no. of member - ')
        print("Name\tAge\tGender\tPhone\tEmail\tBMI\tDuration")
        for cusId in GymManager.customers.keys():
            if cusId==check_phn:
                customer=GymManager.customers[cusId]
                name = customer.getName()
                age = customer.getAge()
                gender = customer.getGender()
                phoneNo = customer.getPhoneNo()
                email = customer.getEmail()
                bmi = customer.getBmi()
                duration = customer.getDuration()
                print(name + "\t" +age+ "\t" +gender+ "\t" +phoneNo+ "\t" +email+ "\t" +bmi+ "\t" +duration)
        print("\n")

    elif option == 3:
        check_phn=input('Enter phone number of member you want to delete:')
        try:
            for curId in GymManager.customers.keys():
                if cusId==check_phn:
                    print("Member Deleted")
            GymManager.customers.pop(check_phn)
        except:

            print("Number doesn't exist\n")

    elif option == 4:
        check=input("Enter phone no. - ")
        exr=input("Enter if you want to extend or revoke")
        if exr == 'extend':
            for cusID in GymManager.customers.keys():
                customer = GymManager.customers[cusId]
                if cusId== check:
                    dur=customer.getDuration()
                    s=int(dur)+int(input("Enter how many months you want it to be extended for - "))
                    res=str(s)
                    customer.setDuration(res)
        elif exr=='revoke':
            for cusId in GymManager.customers.keys():
                customer = GymManager.customers[cusId]
                if cusId==check:
                    customer.setDuration('0')
                    print("Membership revoked")

    elif option == 5:
        phn=input("Enter the phone number of member you want to create regimen of - ")
        for i in GymManager.regimen:
            if i==phn:
                for j in GymManager.regimen[i]:
                    GymManager.regimen[i][j]=input(j+":")

    elif option == 6:
        check_phn=input('Enter phone number of member - ')
        for i in GymManager.regimen:
            if i==check_phn:
                for key,val in GymManager.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 7:
        check_phn=input('Enter phone number of member - ')
        for i in GymManager.regimen:
            if i== check_phn:
                print("Workout regimen is deleted")
        GymManager.regimen.pop(check_phn)
        print("\n")

    elif option == 8:
        check_phn=input("Enter phone no. of member who regimen you want to update - ")
        for i in GymManager.regimen:
            if i == check_phn:
                d=input("Enter the day which you want to update - ")
                for j in GymManager.regimen[i]:
                    if j== d:
                        GymManager.regimen[i][j]=input("Enter the workout - ")
                        print("updation successfull")
        print("\n")

    elif option==0:
        break

    else:
        print("Please enter valid number -")
    menu()

def memenu():
    print("\n__Member Portal__\n")
    print("1. My Regimen")
    print("2. My Profile")
    print("3. Exit")
    print("\nEnter your choice - ")

memenu()
while(True):
    option=int(input())
    if option==1:
        p=input("Enter your phone no. - ")
        print("__Your Regimen Based on your BMI__")
        for i in GymManager.regimen:
            if i==p:
                for key,val in GymManager.regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 2:
        p=input("Enter your phone number - ")
        try:
            for cusId in GymManager.customers.keys():
                if cusId == p:
                    customer = GymManager.customers[cusId]
                    name = customer.getName()
                    age = customer.getAge()
                    gender = customer.getGender()
                    phoneNo = customer.getPhoneNo()
                    email = customer.getEmail()
                    bmi = customer.getBmi()
                    duration = customer.getDuration()
                    print("--Your Profile--")
                    print("Name:",name,"\nAge:",age,"\nGender:",gender,"\nPhone:",phoneNo,"\nEmail:",email,"\nBmi:",bmi,"\nDuration:",duration)
        except:
            print("No user with this phone no. exist")

    elif option == 3:
        break
    else:
        print("Please enter a Valid no.")
    memenu()   
            



