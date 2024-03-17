import xlrd

excel = xlrd.open_workbook('test.xls')

book = excel.sheet_by_name('one')
# book = excel.sheet_by_index(0)
print(book)


rows = []
for index, row in enumerate(book.get_rows()):
    print(index)
    rows.append([])
    for item in row:
        rows[index].append(item.value)

print(rows)