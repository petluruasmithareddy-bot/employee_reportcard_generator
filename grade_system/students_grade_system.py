def calculate_total(marks):
    return sum(marks)


def calculate_avg(marks,no_of_sub):
    return total/no_of_sub

def assign_grade(average):
    if average>=90:
        return("grade A")
    elif average>=80:
        return("grade B")
    elif average>=75:
        return("grade C")
    elif average<= 60:
        return("improvement")
    else:
        return("fail")
marks=[]
n= int(input("enter your no subjects"))

for i in range(n):
    mark=int(input(f"enter marks for subject {i+1}:"))
    marks.append(mark)

total=calculate_total(marks)
average =calculate_avg(total,n)
grade=assign_grade(average)
print("\n Result")

print(f"Total_marks:{total}")
print(f"Average:{average:2f}")
print(f"Grade:{grade}")