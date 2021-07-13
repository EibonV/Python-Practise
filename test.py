import xlwings as xw
app=xw.App(visible=True,add_book=False)
wb=app.books.open(r'd:\work\test.xlsx')
# wb就是新建的工作簿(workbook)，下面则对wb的sheet1的A1单元格赋值
wb.sheets['sheet1'].range('A1').value='苦短'
wb.save(r'd:\work\test.xlsx')
wb.close()
app.quit()