# Program for result processing.
# Rules taken from GOST P 8.736-2011.
import logging

logging.basicConfig(level=logging.WARNING, format=' %(asctime)s - %(levelname)s -  %(message)s')

grabbs_dict = {3: 1.155,
               4: 1.496,
               5: 1.764,
               6: 1.973,
               7: 2.139,
               8: 2.274,
               9: 2.387,
               10: 2.482
               }

t_distibution_dict = {3: (3.182, 5.841),
                      4: (2.776, 3.604),
                      5: (2.571, 4.032),
                      6: (2.447, 3.707),
                      7: (2.365, 2.998),
                      8: (2.306, 3.355),
                      9: (2.262, 3.250),
                      10: (2.228, 3.169)
                      }


# Find blunder and delete from results if exist.
def blunder(results, avrg, deviat, g1_flag, g2_flag):
    grabbs = grabbs_dict[len(results)]
    logging.info(f'g: {grabbs}')
    x_min = min(results)
    x_max = max(results)
    if g1_flag:
        g1 = abs(x_max - avrg) / deviat
        logging.info(f'g1 {g1}')
        if grabbs < g1:
            results.pop(results.index(x_max))
        else:
            g1_flag = False
    if g2_flag:
        g2 = abs(x_min - avrg) / deviat
        logging.info(f'g2 {g2}')
        if grabbs < g2:
            results.pop(results.index(x_min))
        else:
            g2_flag = False
    return g1_flag, g2_flag


# Find arithmetic mean.
def average(results):
    return sum(results) / len(results)


# Find standart deviation.
def deviation(results, avrg):
    return (sum([(x - avrg) ** 2 for x in results]) / (len(results) - 1)) ** (1 / 2)
    pass


# Function for rounding.
def rounding(avrg, conf_limits):
    ten_power = 0
    while conf_limits > 1:
        conf_limits /= 1000
        avrg /= 1000
        ten_power += 3

    # Loop for rounding conf_limits.
    # r - rank to which to round.
    for r, dec in enumerate(str(conf_limits)[2:]):
        if int(dec) >= 3:
            break
        elif dec == '0':
            continue
        else:
            r += 1
            break

    if r == 0:
        conf_limits = f'{conf_limits:.1f}'
        avrg = f'{avrg:.1f}'
    elif r == 1:
        conf_limits = f'{conf_limits:.2f}'
        avrg = f'{avrg:.2f}'
    else:
        conf_limits = f'{conf_limits:.3f}'
        avrg = f'{avrg:.3f}'

    return avrg, conf_limits, ten_power


def main(results, prob):
    g1_flag, g2_flag = True, True
    while True:
        logging.debug(results)
        avrg = average(results)
        deviat = deviation(results, avrg)
        logging.info(deviat)
        g1_flag, g2_flag = blunder(results, avrg, deviat, g1_flag, g2_flag)
        if not g1_flag and not g2_flag:
            break
    avrg_deviat = deviat / len(results) ** (1 / 2)
    conf_limits = t_distibution_dict[len(results)][prob] * avrg_deviat
    logging.warning(avrg)
    logging.warning(conf_limits)
    avrg, conf_limits, ten_power = rounding(avrg, conf_limits)
    print(f'{avrg}+-{conf_limits}(10^{ten_power})')


main([7.47, 7.5, 7.49, 7.58, 7.48], 0)  # 7.50+-0.05(10^0)
main([12.4, 12.6, 13, 12, 12.9, 12.4, 12.7], 0)  # 12.6+-0.3(10^0)
main([1241, 1242, 1254, 1300, 1100, 1200], 0)  # 1.22+-0.07(10^3)
main([0.124, 0.13, 0.129, 0.12, 0.125], 0)  # 0.126+-0.005(10^0)
main([956784, 956122, 956777, 960123, 942123], 0)  # 0.954+-0.008(10^6)
