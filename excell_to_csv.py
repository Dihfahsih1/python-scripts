import xlrd
import csv
import pandas as pd

sheet = xlrd.open_workbook('list_of_emails.xls').sheet_by_index(0)

col = csv.writer(open('emails.csv','w', newline=""))

for row in range(sheet.nrows):
    col.writerow(sheet.row_values(row))
    
df = pd.DataFrame(pd.read_csv("emails.csv"))

df