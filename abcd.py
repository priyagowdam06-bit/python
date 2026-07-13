from openpyxl import load_workbook

# Open the Excel workbook
wb = load_workbook("student.xlsx")

# Select the active sheet
sheet = wb.active

print("Workbook opened successfully!")