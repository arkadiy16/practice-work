import openpyxl


def get_data(sheet, row):
    data = list(map(lambda x: float(x.value), list(sheet.rows)[row - 1]))
    #
    return data


def get_accessory_table(sheet):
    accessory = [list(map(lambda x: float(x.value.replace(',', '.')), list(sheet.rows)[row])) for row in range(1, 17)]
    return accessory


def nearest_value2(items, value):
    return min(items, key=lambda x: abs(value - abs(x)))


def step_1(u1n, u2n, s, w1, w2):
    u1fn = round(u1n / 3 ** (1 / 2), 2)
    u2fn = round(u2n / 3 ** (1 / 2), 2)
    i1n = round(s * 1000 / (3 ** (1 / 2) * u1n), 2)
    i2n = round(s * 1000 / (3 ** (1 / 2) * u2n), 2)
    k = round(w1 / w2)
    return u1fn, u2fn, i1n, i2n, k


def step_2():
    # Scetch.
    pass


def step_3(u1fn, w1, pc, pi, hc, c, d, f, kd, r=7650):
    bc = round(u1fn * 10 ** 4 / (4.44 * f * w1 * pc), 3)
    bi = round(u1fn * 10 ** 4 / (4.44 * f * w1 * pi), 3)
    gc = round(3 * hc * pc * r)
    li = 2 * c + d
    gi = 2 * li / pi * r

    # Idling experience.
    pass


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
    row = 1
    data = get_data(sheet, row)
    v, s, u1n, u2n, w1, w2, sp1, sp2, d1, a1, a2, a12, l, d, pc, pi, hc, hi, c, pk, px, uk, i0 = data

    u1fn, u2fn, i1n, i2n, k = step_1(u1n, u2n, s, w1, w2)
    print(u1fn, u2fn, i1n, i2n, k)
    accessory = get_accessory_table(sheet_a)
    kd = 1.25


main()
