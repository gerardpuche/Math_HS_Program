import random

num1 = random.randint(-20,20)
num2 = random.randint(-20,20)

if num1 == 0:
    num1 = random.randint(-20,20)
    
if num2 == 0:   
    num2 = random.randint(-20,20)
    
if num1 == num2:
    num1 = random.randint(-20,20)
    
indepenedentterm = (num1+num2)*(-1)

multi = num1*num2
    
def pol_mola():
    print(f"x² + {indepenedentterm}x + {multi}= 0")
    
pol_mola()

print(num1)
print(num2)
    
