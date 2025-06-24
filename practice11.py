def calculate_tax(salary: float) -> float:
    if salary < 5000000:
        foiz = salary * 0.2
        return foiz
    else:
        foiz = salary * 0,13
        return foiz
    
def calculate_net_salary(salary: float) -> float:
    sof_oylik = salary - calculate_tax(salary)
    return sof_oylik
salary = float(input("oylikingizni kiriting :"))

result = f"oylikingiz {salary} saloq = {calculate_tax(salary)} sof oylikingiz {calculate_net_salary(salary)}"

print(result)