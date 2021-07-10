class jioCaller():
    def call(self):
        print("calling")

class trueCaller():
    def call(self):
        print("calling")
        print("caller details")


class PhoneCall:
    def call_function(self,phoneApp):
        phoneApp.call()
j=jioCaller()
t=trueCaller()
p1 = PhoneCall()
p1.call_function(j)
print("----------------------------")
p1.call_function(t)
