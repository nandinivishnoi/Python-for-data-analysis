class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hello!!",self.name,"Your average score is",(sum/3))    
        
s1=student("Nandini",[89,97,85])
s1.get_avg()
