
def linear_search(employees, column, value):
    comparisons = 0

    for employee in employees:
        comparisons += 1

        if employee[column] == value:
            return employee, comparisons
          # Assuming we want to stop after finding the first match

    return None, comparisons


def range_search(employees, column, start, end):
    results = []
    comparisons = 0

    for employee in employees:
        comparisons += 1

        if start <= employee[column] <= end:
            results.append(employee)

    return results, comparisons



def multi_condition_search(employees, conditions, operator="AND"):
    results = []
    comparisons = 0

    for employee in employees:
        comparisons += 1

        checks = [
            employee[column] == value
            for column, value in conditions.items()
        ]

        if operator == "AND" and all(checks):
            results.append(employee)

        elif operator == "OR" and any(checks):
            results.append(employee)

    return results, comparisons
