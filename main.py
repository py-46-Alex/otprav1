from application.salary import calculate_salary
from application.db.people import get_employees
import datetime


if __name__ == '__main__':
    calculate_salary()
    get_employees()

    what_time = datetime.datetime.today()

    print('__________________________________________')
    print(f'Hello world! today is  \n{what_time}')
