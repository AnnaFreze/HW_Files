from HR_people import people
from Accounting_salary import salary
import datetime


if __name__ == '__main__':
    print(people.get_employees(people.candidates))
    print(salary.calculate_salary(salary.salary_rates))
    print(datetime.date.today())




