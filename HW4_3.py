import csv

dept_stats = {}

def fill_dept_stats(file_name):
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 0:
                continue
            employee = str(row[0])
            department = str(row[1]) 
            salary = float(row[2])
            if department not in dept_stats:
                dept_stats[department] = {
                    'num_employees': 0,
                    'total_salary': 0.0,
                    'avg_salary': 0.0
                }
            dept_stats[department]['num_employees'] += 1
            dept_stats[department]['total_salary'] += salary
    
    for department in dept_stats:
        num_employees = dept_stats[department]['num_employees']
        total_salary = dept_stats[department]['total_salary']
        if num_employees > 0:
            dept_stats[department]['avg_salary'] = round(total_salary / num_employees, 2)

def get_dept_stats(dept_name):
    if dept_name in dept_stats:
        stats = dept_stats[dept_name]
        return stats['num_employees'], stats['total_salary'], stats['avg_salary']
    else:
        return 0, 0.0, 0.0

fill_dept_stats("Emp_salary.csv")
dept = "R&D"
emp_no, total_sal, avg_sal = get_dept_stats(dept)
print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))
dept = "Accounting"
emp_no, total_sal, avg_sal = get_dept_stats(dept)
print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))

dept = "Not exists"
emp_no, total_sal, avg_sal = get_dept_stats(dept)
print("Department: %s, Employees No.: %d, Total Salary: %.2f, Average Salary: %.2f" %(dept, emp_no, total_sal, avg_sal))
