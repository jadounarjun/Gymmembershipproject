class GymManager:
    regimen={}
    customers = dict()
    def __init__(self,s_id,s_name):
        self.s_id=s_id
        self.s_name=s_name

    @classmethod
    def addCustomer(cls, customer):
        GymManager.customers[customer.getPhoneNo()]=customer

ob=GymManager('s_1','John')