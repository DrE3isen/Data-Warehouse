
import pandas as pd
import time

from linear_scan import (
    linear_search,
    range_search,
    multi_condition_search
)


# Excel file settings
FILE_NAME = "assets/BTree_Indexing_Employee_Dataset-v2 (1).xlsx"
SHEET_NAME = "Employee_Dataset"


# Read Excel file without assuming header location
data = pd.read_excel(FILE_NAME, sheet_name=SHEET_NAME, header=None)

# Find the header row
header_index: int | None = None

for i in range(len(data.index)):
    row = data.iloc[i]
    if "Employee_ID" in row.values:
        header_index = i
        break

if header_index is None:
    raise ValueError("Header row not found!")

# Set column names
data.columns = data.iloc[header_index]
data = data.iloc[header_index + 1:]

# Keep the required columns
columns = [
    "Record_Ptr",
    "Employee_ID",
    "Full_Name",
    "Department",
    "Nationality",
    "Gender",
    "Hire_Date",
    "Salary_JOD",
    "Performance_Score"
]

data = data[columns].copy()

# Remove invalid and empty Employee IDs
data["Employee_ID"] = pd.to_numeric(
    data["Employee_ID"], errors="coerce"
)

data = data.dropna(subset=["Employee_ID"])

# Convert Employee_ID to integer
data["Employee_ID"] = data["Employee_ID"].astype(int)

# Replace empty cells
data = data.fillna("")

# Convert Excel data to a list
employees = data.to_dict("records")

print("Total Employees:", len(employees))


# ---------------------------------
# Query 1: Exact Key Lookup
# ---------------------------------
employee_id = int(input("Enter Employee ID: "))
start = time.perf_counter()
result, comparisons = linear_search(employees, "Employee_ID", employee_id)

end = time.perf_counter()

print("\nQuery 1: Employee ID = ", employee_id)

if result is None:
    print("No employee found.")
else:
    print(result)

print("Comparisons:", comparisons)
print("Execution Time:", end - start, "seconds")


# ---------------------------------
# Query 2: Range Search
# ---------------------------------
start_id = int(input("Enter starting Employee ID: "))
end_id = int(input("Enter ending Employee ID: "))
# start = time.perf_counter()

# results, comparisons = range_search(employees, "Employee_ID", start_id, end_id)

# end = time.perf_counter()

# print("\nQuery 2: Employee IDs between ", start_id, " and ", end_id)

# for employee in results:
#     print(employee)

# if not results:
#     print("No employees found.")

# print("Comparisons:", comparisons)
# print("Execution Time:", end - start, "seconds")


# ---------------------------------
# Query 3: Multi-Condition Search
# ---------------------------------

# start = time.perf_counter()

# results, comparisons = multi_condition_search(
#     employees,
#     {
#         "Nationality": "Jordanian",
#         "Gender": "M",
#         "Department": "HR"
#     }
# )

# end = time.perf_counter()

# print("\nQuery 3: Jordanian Male Employees in HR")

# for employee in results:
#     print(employee)

# if not results:
#     print("No employees found.")

# print("Comparisons:", comparisons)
# print("Execution Time:", end - start, "seconds")
