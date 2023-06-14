import prettytable as pt

#显示坐席
def show_ticket(row_num):
    tb=pt.PrettyTable()      #最大的疑惑点 大写的PrettyTable可以 小写的就错了
    tb.field_names=['行号','座位1','座位2','座位3','座位4','座位5']
    for i in range(row_num):
        lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
        tb.add_row(lst)
    print(tb)
#订票   重新把售出的那一行给创建了
def order_ticket(row_num,row,column):
    tb=pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row)==i+1:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)]='已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num=13
    show_ticket(row_num)
    choose_num=input('请输入座位号，如13排座位5写为13,5')
    try:
        row,column=choose_num.split(',')
    except:
        print('注意输入内容，13排4号座写为13,4')
    order_ticket(row_num,row,column)
