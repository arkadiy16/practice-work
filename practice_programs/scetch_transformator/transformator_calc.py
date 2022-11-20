import openpyxl


def get_data(sheet, row):
    data = list(map(lambda x: float(x.value), list(sheet.rows)[row - 1]))
    #
    return data


def get_accessory_table(sheet):
    accessory = [list(map(lambda x: float(x.value.replace(',', '.')), list(sheet.columns)[column])) for column in
                 range(0, 4)]
    return accessory


def nearest_value(items, value):
    return min(items, key=lambda x: abs(value - abs(x)))


def step_1(u1n, u2n, s, w1, w2):
    u1fn = round(u1n / 3 ** (1 / 2), 2)
    u2fn = round(u2n / 3 ** (1 / 2), 2)
    print(f'ufn: {u1fn}, {u2fn}')
    i1n = round(s * 1000 / (3 ** (1 / 2) * u1n), 2)
    i2n = round(s * 1000 / (3 ** (1 / 2) * u2n), 2)
    print(f'in: {i1n}, {i2n}')
    k = round(w1 / w2)
    print(f'k: {k}')
    return u1fn, u2fn, i1n, i2n, k


def step_2():
    # Scetch.
    pass


def step_3(r_sheet, s, i1n, u1fn, w1, pc, pi, hc, c, d, f, kd, accessory, r=7650):
    # Idling experience.
    li = 2 * c + d
    gc = round(3 * hc * pc * r * 10 ** -6, 2)
    gi = round(2 * li * pi * r * 10 ** -6, 2)
    print('G: ', gc, gi)

    row_t2 = 2
    r_sheet['A1'] = 'n'
    r_sheet['B1'] = 'U1f, V'
    r_sheet['C1'] = 'Px, W'
    r_sheet['D1'] = 'Qx, WAp'
    r_sheet['E1'] = 'I0a, A'
    r_sheet['F1'] = 'I0p, A'
    r_sheet['G1'] = 'I0, A'
    r_sheet['H1'] = 'cosp0'

    for n in (0.5, 0.7, 0.8, 0.9, 1, 1.1):
        tabl_data = step_3_tabl(n, u1fn, i1n, w1, pc, pi, f, kd, accessory, gc, gi, s)
        if n == 1:
            r_sheet['K2'] = tabl_data[0]
            r_sheet['K3'] = tabl_data[-1]
        r_sheet[f'A{row_t2}'] = n
        r_sheet[f'B{row_t2}'] = round(n * u1fn, 2)
        r_sheet[f'C{row_t2}'] = tabl_data[0]
        r_sheet[f'D{row_t2}'] = tabl_data[1]
        r_sheet[f'E{row_t2}'] = tabl_data[2]
        r_sheet[f'F{row_t2}'] = tabl_data[3]
        r_sheet[f'G{row_t2}'] = tabl_data[4]
        r_sheet[f'H{row_t2}'] = tabl_data[5]
        row_t2 += 1


def step_3_tabl(n, u1fn, i1n, w1, pc, pi, f, kd, accessory, gc, gi, s):
    u1fn *= n
    bc = round(u1fn * 10 ** 4 / (4.44 * f * w1 * pc), 3)
    bi = round(u1fn * 10 ** 4 / (4.44 * f * w1 * pi), 3)
    c_ac_ind = accessory[0].index(nearest_value(accessory[0], bc))
    i_ac_ind = accessory[0].index(nearest_value(accessory[0], bi))
    pc_ac = accessory[1][c_ac_ind]
    qc_ac = accessory[2][c_ac_ind]
    qzc_ac = accessory[3][c_ac_ind]
    pi_ac = accessory[1][i_ac_ind]
    qi_ac = accessory[2][i_ac_ind]
    qzi_ac = accessory[3][i_ac_ind]

    px = round(kd * (pc_ac * gc + pi_ac * gi), 2)
    qx = round(qc_ac * gc + qi_ac * gi + qzc_ac * 3 * pc + qzi_ac * 4 * pi, 2)

    i_0a = round(px / (10 * s), 2)
    i_0p = round(qx / (10 * s), 2)
    i_0 = round((i_0a ** 2 + i_0p ** 2) ** (1 / 2), 2)
    i0a = round(i_0a * i1n / 100, 5)
    i0p = round(i_0p * i1n / 100, 5)
    i0 = round(i_0 * i1n / 100, 5)
    cosp0 = round(i0a / i0, 3)
    sinp0 = round(i0p / i0, 3)

    z0 = round(u1fn / i0, 2)
    r0 = round(z0 * cosp0, 2)
    x0 = round((z0 ** 2 - r0 ** 2) ** (1 / 2), 2)
    if n == 1:
        print('B: ', bc, bi)
        print('T3c: ', bc, accessory[0][c_ac_ind], pc_ac, qc_ac, qzc_ac)
        print('T3i: ', bi, accessory[0][i_ac_ind], pi_ac, qi_ac, qzi_ac)
        print(f'i0: {i_0a}, {i_0p}, {i_0}')
        print(f'I0: {i0a}, {i0p}, {i0}')
        print(f'cos: {cosp0}, sin: {sinp0}')
        print(f'z,r,x: {z0}, {r0}, {x0}')

    return px, qx, i0a, i0p, i0, cosp0, i_0


def step_4():
    # Short circuit experience.
    pass


def step_6():
    # KPD.
    pass


def step_7():
    # Knocking current.
    pass


def main():
    # get data from excel sheet.
    wb = openpyxl.load_workbook('data.xlsx')
    sheet = wb['Лист1']
    sheet_a = wb['Лист2']
    accessory = get_accessory_table(sheet_a)
    kd = 1.25
    f = 50
    for row in range(1, 2):
        rb = openpyxl.Workbook()
        r_sheet = rb.active
        data = get_data(sheet, row)
        v, s, u1n, u2n, w1, w2, sp1, sp2, d1, a1, a2, a12, l, d, pc, pi, hc, hi, c, pk, px, uk, i0 = data
        u1fn, u2fn, i1n, i2n, k = step_1(u1n, u2n, s, w1, w2)
        step_3(r_sheet, s, i1n, u1fn, w1, pc, pi, hc, c, d, f, kd, accessory)
        r_sheet['J1'] = 'Контрольные данные'
        r_sheet['J2'] = f'Px = {px}W'
        r_sheet['J3'] = f'i0 = {i0}%'
        r_sheet['K1'] = 'Результаты вычислений'

        rb.save(f'result//var{row}.xlsx')


main()
