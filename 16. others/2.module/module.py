class Module:

    def __init__(self, a,b):

        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a  * self.b
    
    def div(self):
        return self.a / self.b
    

    
def greeting(name):
    return f"hello {name}"



person = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}