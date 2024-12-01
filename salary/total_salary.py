from pathlib import Path

def total_salary(file_path: Path) -> tuple[int, int]:
    """
    Calculate total salary and average salary from a file.

    The file should contain one line per employee, with the salary as the
    second column. The function will return a dictionary with the total
    salary and the average salary.

    If the file does not exist, or if there are no valid lines in the
    file, then the function will return a dictionary with total and
    average salary set to 0.0.

    :param file_path: Path to the file to read.
    :return: A dictionary with total and average salary.
    """
    
    total_salary = 0.0
    employee_count = 0

    try:
        with file_path.open(encoding="utf-8") as file:
            for line in file:
                try:
                    _, salary_str = line.strip().split(",")
                    total_salary += float(salary_str)
                    employee_count += 1
                except ValueError:
                    continue
    except FileNotFoundError:
        return ( 0, 0)

    if employee_count == 0:
        return ( 0, 0)

    average_salary = total_salary / employee_count
    return (int(total_salary), int(average_salary))

file_path = Path("./data/employee_salary.csv")
total, average = total_salary(file_path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")