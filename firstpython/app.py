"""def studentGrade (score):
    result = "";
    if score >= 80 and score <= 100:
        result = 'A';
    elif score >= 70 and score <=79:
        result = "B";    
    elif score >= 60 and score <=69:
        result = "C";
    elif score >= 50 and score <=59:
        result = "D";
    elif score >= 40 and score <=49:
        result = "E";
    elif score >= 0 and score <=39:
        result = "F";
    else : 
        result ="";
    
    return result

print("Please enter student name");
name = input();

print("Please enter student age");
while True:
    age = input()
    try:
        age = int(age)
        break  # Exit the loop if the input is a valid integer
    except ValueError:
        print("Invalid input. Please enter a valid integer for your age.")    
        continue


while True:
    score = input("Please enter student score");
    try:
        score = int(score)
        if score >100 or score < 0:
            continue
        break
    except error:
        print("Please enter a number!");
        continue;

result = studentGrade(score)
print(f"Hello {name}, your grade is {studentGrade(score)}")

"""

a = "b";
print(type(a))



x = 0;
while (x<5):
    print(x)
    x+=1;

day = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(day[0])
print(len(day) - 1)
for x in day:
    print(x)


import random

random_number = random.randrange(2,3)
print(random_number)