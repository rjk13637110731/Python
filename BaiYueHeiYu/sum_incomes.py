import xlrd

book = xlrd.open_workbook('income.xlsx')

sheets = book.sheets()
incomes = 0
toSubstance = 0
for sheet in sheets:
    incomes += sum(sheet.col_values(colx=1,start_rowx=1))
    monthes = sheet.col_values(colx=0)
    for row,month in enumerate(monthes):
        if type(month) is str and month.endswith('*'):
            income = sheet.cell_value(rowx=row, colx=1)
            print(sheet.name,month,income)
            toSubstance += income

    print(sheet.name,incomes,income)

print(f"2016-2018年真实收入为:{incomes - toSubstance}")
