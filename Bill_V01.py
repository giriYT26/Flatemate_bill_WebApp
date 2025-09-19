class Bill:
    def __init__(self,amount,period):
        self.amount = amount
        self.period = period

class Flatemate:
    def __init__(self,name,day_in_house):
        self.name = name
        self.day_in_house = day_in_house
    def pay(self,bill,flatemate2):
        weight = self.days_in_house / (self.days_in_house + flatemate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay