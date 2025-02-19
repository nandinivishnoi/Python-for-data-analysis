class student:
    college_name="ABSR College"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    def welcome(self):
        print("welcomes you")
    
    def get_name(self):
        return self.name
    
    def get_marks(self):
        return self.marks
        
s1=student("Nandini",98)
print(student.college_name)
print(s1.welcome())
print(s1.get_name())
print(s1.get_marks())