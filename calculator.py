import math

def calculator():
    print("\n=== ماشین حساب علمی ===")
    print("1. توان (x^y)")   
    print("2. جذر (√x)")
    print("3. سینوس (sin)")
    print("4. کسینوس (cos)")
    print("5. تانژانت (tan)")
    print("6. لگاریتم (log10)")
    print("7. خروج")

def calculate_power():
    try:
        x = float(input("پایه را وارد کنید: "))
        y = float(input("توان را وارد کنید: "))
        return math.pow(x, y)
    except ValueError:
        return "❌ ورودی نامعتبر!"

def calculate_sqrt():
    try:
        z = float(input("یک عدد وارد کنید: "))
        if z < 0:
            return "❌ جذر عدد منفی تعریف نشده!"
        return math.sqrt(z)
    except ValueError:
        return "❌ ورودی نامعتبر!"

def calculate_sin():
    try:
        degree = float(input("زاویه (درجه) را وارد کنید: "))
        return math.sin(math.radians(degree))
    except ValueError:
        return "❌ ورودی نامعتبر!"

def calculate_cos():
    try:
        degree = float(input("زاویه (درجه) را وارد کنید: "))
        return math.cos(math.radians(degree))
    except ValueError:
        return "❌ ورودی نامعتبر!"

def calculate_tan():
    try:
        degree = float(input("زاویه (درجه) را وارد کنید: "))
        rad = math.radians(degree)
        # بررسی نزدیک بودن به 90, 270, ...
        if math.isclose(math.cos(rad), 0, abs_tol=1e-9):
            return "❌ تانژانت در این زاویه تعریف نشده!"
        return math.tan(rad)
    except ValueError:
        return "❌ ورودی نامعتبر!"

def calculate_log():
    try:
        x = float(input("یک عدد مثبت وارد کنید: "))
        if x <= 0:
            return "❌ لگاریتم فقط برای اعداد مثبت تعریف شده!"
        return math.log10(x)
    except ValueError:
        return "❌ ورودی نامعتبر!"

# main loop
while True:
    calculator()
    choice = input("👉 انتخاب شما: ")

    if choice == "1":
        result = calculate_power()
    elif choice == "2":
        result = calculate_sqrt()
    elif choice == "3":
        result = calculate_sin()
    elif choice == "4":
        result = calculate_cos()
    elif choice == "5":
        result = calculate_tan()
    elif choice == "6":
        result = calculate_log()
    elif choice == "7":
        print("✅ خداحافظ! 🌹")
        break
    else:
        result = "❌ گزینه نامعتبر!"

    # چاپ نتیجه با فرمت مناسب
    if isinstance(result, float):
        print(f"📌 نتیجه: {result:.4f}")
    else:
        print(result)
