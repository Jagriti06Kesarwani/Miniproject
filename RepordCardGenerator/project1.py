def gd(avg):
        if(avg>=80):
             return "A"
        elif(avg>=70):
            return "B"
        elif(avg>=50):
            return "C"
        else:
             return "D"

students = {}

n = int(input("How many students? "))        
o=int(input("enter no. of subjects: "))        
for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    m=[]
    for j in range(o):
        while True:
            try:
                 marks=int(input(f"enter marks{j+1} : "))
                 if 0<=marks<=100:
                     m.append(marks)
                     break
                 else:
                     print("Marks must be between 0 and 100.")
            except ValueError :
                print("Please enter a valid integer.")        
    total=sum(m)
    avg=total/o
    grade=gd(avg) 

    students[roll] = {"name": name, "marks": m,"total": total, "average": avg, "grade": grade}
print("\n ----STUDENTS REPORT CARD---- ") 
for roll, info in students.items():
    print(f"\nRoll No: {roll}")
    print(f"Name: {info['name']}")
    print(f"Marks: {info['marks']}")
    print(f"Total: {info['total']}")
    print(f"Average: {info['average']:.2f}")
    print(f"Grade: {info['grade']}")
     
