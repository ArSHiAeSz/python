import math 

def calculator():
    print("1. توان")   
    print("2. جذر")
    print("3. sin")
    print("4. exit")

def calculate_power():
    x = float(input("پایه را وارد کنید: "))
    y = float(input("توان را وارد کنید: "))
    return math.pow(x, y)

def calculate_sin():
    degree = float(input("زاویه (درجه) را وارد کنید: "))
    q = math.radians(degree)
    return math.sin(q)

def calculate_sqrt():
    z = float(input("یک عدد وارد کنید: "))
    return math.sqrt(z)

# main
while True:
    calculator()
    choice = input("انتخاب شما: ")
    
    if choice == "1":        
        print(calculate_power())
    elif choice == "2":
        print(calculate_sqrt())
    elif choice == "3":
        print(calculate_sin())
    elif choice == "4":
        break
    else:
        print("گزینه نامعتبر!")
