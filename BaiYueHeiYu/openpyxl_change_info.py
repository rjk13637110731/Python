import openpyxl

wb = openpyxl.load_workbook('income.xlsx')

sheet = wb['2017']

sheet['A1'] = '修改一下'

wb.save('income-1.xlsx')
