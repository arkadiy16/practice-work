import openpyxl
import math


def step_2(c_sheet, row, p, f, kci, cos, kcoi, pud):
    pp = kci * p
    tg = math.tan(math.acos(cos))
    qp = pp * tg
    pno = f * pud / 10e2
    ppo = kcoi * pno
    ppsum = pp + ppo
    qpsum = qp
    spsum = math.sqrt(ppsum ** 2 + qpsum ** 2)

    c_sheet[f'B{row}'] = round(pp, 2)
    c_sheet[f'c{row}'] = round(qp, 2)
    c_sheet[f'd{row}'] = round(pno, 2)
    c_sheet[f'e{row}'] = round(ppo, 2)
    c_sheet[f'f{row}'] = round(ppsum, 2)
    c_sheet[f'g{row}'] = round(qpsum, 2)
    c_sheet[f'h{row}'] = round(spsum, 2)
    c_sheet[f'i{row}'] = round(tg, 2)



def main():
    # get data from excel sheet.
    wb = openpyxl.load_workbook('data.xlsx')
    sheet = wb['Лист1']


    c_sheet = wb['Лист2']

    c_sheet['B1'] = 'Pp'
    c_sheet['C1'] = 'Qp'
    c_sheet['D1'] = 'Pno'
    c_sheet['E1'] = 'Ppo'
    c_sheet['F1'] = 'Ppsum'
    c_sheet['G1'] = 'Qpsum'
    c_sheet['H1'] = 'Spsum'
    c_sheet['i1'] = 'tg'

    for row in range(2, 16):
        c_sheet[f'A{row}'] = f'{row - 1}'

        data = list(map(lambda x: float(x.value), list(sheet.rows)[row - 1]))
        p, f, kci, cos, kcoi, pud = data[1:]

        step_2(c_sheet, row, p, f, kci, cos, kcoi, pud)

    pud = 2
    kco = 1
    wb.save('result.xlsx')
main()
