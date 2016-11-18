import csv
csvFile = open("C:/Users/hi/desktop/test1.csv",'w+')
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times 2'))
    # 写入一行用writerow
    for i in range(10):
        writer.writerow((i,i+2,i*2))
finally:
    csvFile.close()



csvFile = open("C:/Users/hi/desktop/test2.csv",'w+')
writer = csv.writer(csvFile)
writer.writerow(['姓名', '年龄', '电话'])

data = [
    ('小河', '25', '1234567'),
    ('小芳', '18', '789456')
]
writer.writerows(data)
#多行用writerows
csvFile.close()

