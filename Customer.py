class Customer:
    def __init__(self,name='',age='',gender='',phoneNo='',email='',bmi='',duration=''):
        self.__name = name
        self.__phoneNo = phoneNo
        self.__age = age
        self.__gender = gender
        self.__email = email
        self.__bmi = bmi
        self.__duration = duration

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setPhoneNo(self, phoneNo):
        self.__phoneno = phoneNo

    def getPhoneNo(self):
        return self.__phoneNo

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setBmi(self, bmi):
        self.__bmi = bmi

    def getBmi(self):
        return self.__bmi

    def setDuration(self, duration):
        self.__duration = duration

    def getDuration(self):
        return self.__duration

    def __str__(self):
        return self.getName()+" "+self.getPhoneNo()+" "+self.getDuration()+" "+self.getAge()+" "+self.getGender()+" "+self.getBmi()+" "+self.getEmail()