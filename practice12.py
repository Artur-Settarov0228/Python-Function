def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height **2)
def bmi_status(bmi: float) -> str:
    if bmi < 25 :
        return "normal"
    else:
        return "overweight"
    
weight = float(input("vaznningizni kiriting :"))
height = float(input("boyignizni kriting :"))

bmi = calculate_bmi(weight, height)

result = bmi_status(bmi)

print(result)