import xlsxwriter
import xlrd

# excel = xlsxwriter.Workbook('new.xlsx')
# book = excel.add_worksheet('one')
#
# title = ['名称', '销量', '库存', '价格']
#
# for i, v in enumerate(title):
#     book.write(0, i, v)
#
# excel.close()


# 读取一个xls文件
excel = xlrd.open_workbook('test.xls')
book = excel.sheet_by_name('one')

# 将这个xls第一个工作本的全部内容写入到新的xlsx文件中
# 1、读取
rows = []
for index, row in enumerate(book.get_rows()):
    rows.append([])
    for item in row:
        rows[index].append(item.value)

# 2、写入
new_excel = xlsxwriter.Workbook('new_test.xlsx')
new_book = new_excel.add_worksheet('one')
for r_index, row in enumerate(rows):
    for c_index, cell in enumerate(row):
        new_book.write(r_index, c_index, cell)

# 创建图表
book_chart = new_excel.add_worksheet('学生等级')

data = [
    ['优秀', '良好', '中', '差'],
    [1100, 2000, 1000, 900]
]

# 纵向填充数据
book_chart.write_column('A1', data[0])
book_chart.write_column('B1', data[1])

# 创建图表对象
chart = new_excel.add_chart({'type': 'column'})
chart.add_series({
    'categories': '=学生等级!$A1:$A4',
    'values': '=学生等级!$B1:$B4',
    'name': '成绩占比'
})
book_chart.insert_chart('A10', chart)

new_excel.close()

