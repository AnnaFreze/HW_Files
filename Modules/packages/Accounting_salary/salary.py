from HR_people import people

salary_rates = {"junior": 100, "middle": 200, "senior": 300, "lead":400}

def calculate_salary(rates):
    salaries = {}
    for employee in people.get_employees(people.candidates):
        if employee["position"] == "lead":
            salaries[employee["name"]] = salary_rates["lead"]
    salary_amount = sum(salaries.values())
    return salary_amount
