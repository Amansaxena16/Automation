import xlsxwriter
from GeminiAPI import input_list
from GeminiAPI import output_list

row1 = 2
row2 = 2

    
workbook = xlsxwriter.Workbook('Bhagavad Gita.xlsx')
worksheet = workbook.add_worksheet('Chapter 1')

worksheet.write(0,0,'Questions')
worksheet.write(0,1,'Answers')

def insertIntoExcel(input,output):

    global row1, row2
    worksheet.write(row1, 0,input)
    row1 = row1 + 1
    
    worksheet.write(row2, 1,output)
    row2 = row2 + 1

    print('Done')


for i in range(len(input_list)):
    insertIntoExcel(input_list[i], output_list[i])
    
workbook.close()
print('Done')