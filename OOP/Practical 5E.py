#5.E Hybrid inheritance
import datetime
class Vehicle:
    def register(self):
        self._regno=str(input("enter registration no:"))
        self._regdate=datetime.datetime.now()
        print(self._regdate)
class HMV(Vehicle):
    def detail_1(self):
        self.register()
        self._cname=str(input("Enter company name:"))
        self._type=str(input("type of vehicles:"))
        self._price=int(input("Enter price:"))
class LMV(Vehicle):
    def detail_2(self):
        self.register()
        self._cname=str(input("Enter company name:"))
        self._type=str(input("type of vehicles:"))
        self._price=int(input("Enter price:"))
class RTO(HMV,LMV):
    def rule(self):
        print("\nRegistration is valid for 15 years for all vehicles")
r=RTO()
print("LMV details")
r.detail_2()
print("HMV details")
r.detail_1()
r.rule()