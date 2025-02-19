class student:
    def __init__(self,fullname,marks):
        self.name=fullname
        self.marks=marks
        print("Adding new student to database")

s1=student("Nandini",96)
print(s1.name,s1.marks)
s2=student("Manish",97)
print(s2.name,s2.marks)
s3=student("Vishank",87)
print(s3.name,s3.marks)
s4=student("Khushbu",85)
print(s4.name,s4.marks)
s5=student("Lovely",79)
print(s5.name,s5.marks)