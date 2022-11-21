import openpyxl
import math


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
            r_sheet['K1'] = 'Результаты вычислений'
            r_sheet['K2'] = f'{tabl_data[0]} W'
            r_sheet['K3'] = f'{tabl_data[-2]} %'
            bc = tabl_data[-4]
            px = tabl_data[0]
            r0 = tabl_data[-2]
            x0 = tabl_data[-1]
        r_sheet[f'A{row_t2}'] = n
        r_sheet[f'B{row_t2}'] = round(n * u1fn, 2)
        r_sheet[f'C{row_t2}'] = tabl_data[0]
        r_sheet[f'D{row_t2}'] = tabl_data[1]
        r_sheet[f'E{row_t2}'] = tabl_data[2]
        r_sheet[f'F{row_t2}'] = tabl_data[3]
        r_sheet[f'G{row_t2}'] = tabl_data[4]
        r_sheet[f'H{row_t2}'] = tabl_data[5]
        row_t2 += 1
    bc40 = round(u1fn * 10 ** 4 / (4.44 * 40 * w1 * pc), 3)
    bc60 = round(u1fn * 10 ** 4 / (4.44 * 60 * w1 * pc), 3)
    px40 = round(px * (bc40 / bc) ** 2 * (40 / 50) ** 1.5, 2)
    px60 = round(px * (bc60 / bc) ** 2 * (60 / 50) ** 1.5, 2)
    print(f'px40/60: {px40}, {px60}')
    return r0, x0


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

    return px, qx, i0a, i0p, i0, cosp0, i_0, bc, z0, r0, x0


def step_4(u1fn, i1n, i2n, sp1, sp2, d1, a1, a12, a2, l, w1, w2, s, al, f, r_sheet):
    # Short circuit experience.
    c = 3
    if s <= 100:
        kdob = 1.03
    elif 160 <= s <= 630:
        kdob = 1.06
    else:
        kdob = 1.12
    d_avg1 = round(d1 + 2 * a1, 2)
    d_avg2 = round(d_avg1 + 2 * a12 + a2 / 2, 2)
    j1 = i1n / sp1
    j2 = i2n / sp2
    if al:
        g01 = 8.47 * c * d_avg1 * w1 * sp1 * 10 ** (-5)
        posn1 = 12.75 * g01 * j1 ** 2

        g02 = 8.47 * c * d_avg2 * w2 * sp2 * 10 ** (-5)
        posn2 = 12.75 * g02 * j2 ** 2
    else:
        g01 = 28 * c * d_avg1 * w1 * sp1 * 10 ** (-5)
        posn1 = 2.4 * g01 * j1 ** 2

        g02 = 28 * c * d_avg2 * w2 * sp2 * 10 ** (-5)
        posn2 = 2.4 * g02 * j2 ** 2

    posn = posn1 + posn2
    pk = posn * kdob
    print(f'd_avg: {d_avg1}, {d_avg2}')
    print(f'J: {round(j1, 2)}, {round(j2, 2)}')
    print(f'G0: {round(g01, 2)}, {round(g02, 2)}')
    print(f'Posni: {round(posn1, 2)}, {round(posn2, 2)}')
    print(f'Posn: {round(posn, 2)}')
    print(f'Kdob: {kdob}')
    print(f'Pk: {round(pk, 2)}')

    usv = u1fn / w1
    ss = s / c
    d12 = d1 + 2 * a1 + a12
    b = 3.1415 * d12 / l
    ap = a12 + (a1 + a2) / 3
    kp = 0.95

    uap = pk / (10 * s)
    upp = 7.92 * f * ss * b * ap * kp / (usv ** 2 * 10 ** 3)
    ukp = (uap ** 2 + upp ** 2) ** (1 / 2)

    print(f'up: {round(uap, 2)}, {round(upp, 2)}, {round(ukp, 2)}')
    print(f'S\': {round(ss, 2)}')
    print(f'b: {round(b, 2)}')
    print(f'd12: {d12}')
    print(f'ap: {round(ap, 2)}')
    print(f'kp: {kp}')

    uk = u1fn * ukp / 100
    uka = u1fn * uap / 100
    ukp = u1fn * upp / 100
    print(f'Uk: {round(uk, 2)}, {round(uka, 2)}, {round(ukp, 2)}')

    zk = uk / i1n
    rk = uka / i1n
    xk = ukp / i1n
    cospk = uka / ukp
    print(f'zk, rk, xk: {round(zk, 2)}, {round(rk, 2)}, {round(xk)}')
    print(f'cospk: {round(cospk, 2)}')

    r_sheet['K5'] = 'Результаты вычислений'
    r_sheet['K6'] = f'{round(pk, 2)} W'
    r_sheet['K7'] = f'{round(upp, 2)} %'

    p2_max, delt_u_max = step_4_tabl1(uka, ukp, r_sheet)
    step_4_tabl2(i2n, u1fn, r_sheet, uka, ukp)

    return p2_max, delt_u_max, zk, rk, xk


def step_4_tabl1(uka, ukp, r_sheet):
    r_sheet['A9'] = 'φ_2'
    r_sheet['B9'] = 'ΔU, V'
    delt_u_max = 0
    p2_max = 0
    for ind, p2 in enumerate([-90, -60, -45, -30, 0, 30, 45, 60, 90]):
        r_sheet[f'A{ind + 10}'] = p2
        p2 = math.radians(p2)
        delt_u = uka * math.cos(p2) + ukp * math.sin(p2)
        if delt_u_max < delt_u:
            delt_u_max = delt_u
            p2_max = math.degrees(p2)

        r_sheet[f'B{ind + 10}'] = round(delt_u, 2)
    for p2 in range(round(p2_max) - 10, round(p2_max) + 10):
        p2 = math.radians(p2)
        delt_u = uka * math.cos(p2) + ukp * math.sin(p2)
        if delt_u_max < delt_u:
            delt_u_max = delt_u
            p2_max = math.degrees(p2)
    print(f'phik: {round(p2_max)}\ndeltUmax: {round(delt_u_max, 2)}')
    return p2_max, delt_u_max


def step_4_tabl2(i2n, u1fn, r_sheet, uka, ukp):
    r_sheet['D9'] = 'К_нг'
    r_sheet['E9'] = 'I2, A'
    r_sheet['F9'] = 'ΔU,V\ncosφ_2=1'
    r_sheet['G9'] = 'U2fn,V\ncosφ_2=1'
    r_sheet['H9'] = 'ΔU,V\ncosφ_2=0.7'
    r_sheet['I9'] = 'U2fn,V\ncosφ_2=0.7'
    for ind, kng in enumerate([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2]):
        r_sheet[f'D{ind + 10}'] = kng
        r_sheet[f'E{ind + 10}'] = round(i2n * kng, 2)
        for cos_val in (1, 0.7):
            delt_u = kng * (uka * cos_val + ukp * math.sin(math.acos(cos_val)))
            u2f = (u1fn - delt_u) / 25
            if cos_val == 1:
                letter = ('F', 'G')
            else:
                letter = ('H', 'I')
            r_sheet[f'{letter[0]}{ind + 10}'] = round(delt_u, 2)
            r_sheet[f'{letter[1]}{ind + 10}'] = round(u2f, 2)


def step_5(u1fn, i1n, i2n, p2_max, delt_u_max, rk, xk, r0, x0):
    p2_max = math.radians(p2_max)
    r1 = rk / 2
    x1 = xk / 2
    rm = r0
    xm = x0
    i0 = 0
    print(f'r12, x12: {round(r1, 2)}, {round(x1, 2)}')
    print(f'rm, xm: {round(rm, 2)}, {round(xm, 2)}')

    u2fs = u1fn - delt_u_max
    i2s = i1n
    u2s = u2fs * complex(math.cos(p2_max), math.sin(p2_max))
    print(f'u2f\': {round(u2fs, 2)}')
    print(f'u2\': {round(u2s.real, 2)} + j{round(u2s.imag, 2)}')

    e2s = u2s + i2s * complex(r1, x1)
    i1 = - i2s
    u1 = -e2s + i1 * complex(r1, x1)
    print(f'E2\': {round(e2s.real, 2)} + j{round(e2s.imag, 2)}')
    print(f'u1: {round(u1.real, 2)} + j{round(u1.imag, 2)}')


def step_6(s, px, pk, r_sheet):
    # KPD.
    px *= 1e-3
    pk *= 1e-3
    r_sheet['K9'] = 'Snom,kW'
    r_sheet['L9'] = 'η\ncosφ_2=1'
    r_sheet['M9'] = 'η\ncosφ_2=0.7'
    for ind, kng in enumerate([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2]):
        r_sheet[f'K{ind + 10}'] = s * kng
        for cos_val in (1, 0.7):
            if cos_val == 1:
                letter = ('L')
            else:
                letter = ('M')
            r_sheet[f'{letter}{ind + 10}'] = round(1 - (px + kng ** 2 * pk) / (kng * s * cos_val + px + kng * pk), 3)

    kng_max = (px / pk) ** (1 / 2)
    kpd_max = 1 - (px + kng_max ** 2 * pk) / (kng_max * s + px + kng_max * pk)
    print(f'kng_max: {round(kng_max, 3)}')
    print(f'kpd_max: {round(kpd_max, 3)}')


def step_7(i1n, uk, rk, xk):
    # Knocking current.
    ikust = i1n * 100 / uk
    kud = 1 + math.exp(-(math.pi * rk / xk))
    ikm = kud * ikust * 2 ** (1 / 2)
    print(f'ikust: {round(ikust, 2)}')
    print(f'kud: {round(kud, 3)}')
    print(f'ikm: {round(ikm, 2)}')

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
        r0, x0 = step_3(r_sheet, s, i1n, u1fn, w1, pc, pi, hc, c, d, f, kd, accessory)
        r_sheet['J1'] = 'Контрольные данные'
        r_sheet['J2'] = f'Px = {px}W'
        r_sheet['J3'] = f'i0 = {i0}%'
        if 21 < v <= 31:
            al = False
        else:
            al = True
        r_sheet['J5'] = 'Контрольные данные'
        r_sheet['J6'] = f'Pk = {pk}W'
        r_sheet['J7'] = f'uk% = {uk}%'
        p2_max, delt_u_max, zk, rk, xk = step_4(u1fn, i1n, i2n, sp1, sp2, d1, a1, a12, a2, l, w1, w2, s, al, f, r_sheet)

        step_5(u1fn, i1n, i2n, p2_max, delt_u_max, rk, xk, r0, x0)

        step_6(s, px, pk, r_sheet)

        step_7(i1n, uk, rk, xk)

        rb.save(f'result//var{row}.xlsx')


main()
