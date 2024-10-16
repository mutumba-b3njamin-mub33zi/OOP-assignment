class Vehicle:
    def __init__(self,color) -> None:
        self.color = color
        
    # Creating methods getColor and toString
    def getColor(self):
        return self.color
    
    def toString(self):
        print(f"This vehicle is {self.getColor()}")
    
if __name__ == '__main__':
    
    Vehicle1 = Vehicle("red")
    Vehicle2 = Vehicle("blue")

    print(Vehicle1.getColor())
    print(Vehicle1.toString())