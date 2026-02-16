
class StringHandler:
    def getString(self):
        self.s = input() 
    def printString(self):
        print(self.s.upper()) 


s = StringHandler()
s.getString() 
s.printString() 