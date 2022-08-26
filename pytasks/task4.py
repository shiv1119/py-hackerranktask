"""The provided code stub reads two integers,a  and b, from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  a//b . The second line should contain the result of float division,  a/b .

No rounding or formatting is necessary."""

class Divide():
    def __init__(self,a = int(input("")),b = int(input("")) ):
        self.a = a
        self.b = b
    def div_1(self):
        return self.a // self.b 
    def div_2(self):
        return self.a / self.b
my_division = Divide()
print(my_division.div_1())
print(my_division.div_2())


