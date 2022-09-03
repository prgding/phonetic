import get_phonetic
from openpyxl import load_workbook

if __name__ == '__main__':
    wb = load_workbook(filename='/Users/dingshuai/Dev/Code/Python/phonetic/words.xlsx')
    sheet1 = wb['Sheet1']

    for i in range(2,sheet1.max_row+1):
        words_line = sheet1.cell(row=i, column=1).value
        phonetic_line = sheet1.cell(row=i, column=6).value
        if words_line is not None and phonetic_line is None:
            print(sheet1.cell(row=i, column=1).value)
            sheet1.cell(row=i, column=6).value = get_phonetic.get_ph(sheet1.cell(row=i, column=1).value)

    wb.save('/Users/dingshuai/Dev/Code/Python/phonetic/words.xlsx')