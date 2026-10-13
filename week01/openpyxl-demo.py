import openpyxl

new_wb = openpyxl.Workbook()
new_wb.save('new_workbook.xlsx')
new_wb.create_sheet('Data')
new_wb['Data']['A1'].value = 2
print(new_wb['Data']['A1'].value)
new_wb.save('new_workbook.xlsx')
