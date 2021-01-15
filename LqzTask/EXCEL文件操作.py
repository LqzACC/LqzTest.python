import openpyxl
wb=openpyxl.load_workbook('C:\\Users\\Lqz\\source\\repos\\PythonApplication1\\PythonApplication1\\ss.xlsx')
sheet=wb.get_sheet_by_name('工作表1')
print(sheet.title)
print(sheet.cell(row=3,column=2).value)
type(wb)