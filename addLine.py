# 给测试集添加标签
import csv
#我看不懂，但我大受震撼
with open(r'..\test\sentiment-analysis\test.csv') as csvfile:
    rows = csv.reader(csvfile)
    with open(r'..\test\sentiment-analysis\test1.csv', 'a+', newline='') as f:
        writer = csv.writer(f)
        for index,row in enumerate(rows):
            if index<1000:
               row.append("-1")
               writer.writerow(row)

