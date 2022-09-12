# Program for result processing.
# Rules taken from GOST P 8.736-2011.
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')

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
    logging.warning(f'g: {grabbs}')
    x_min = min(results)
    x_max = max(results)
    if g1_flag:
        g1 = abs(x_max - avrg) / deviat
        logging.warning(f'g1 {g1}')
        if grabbs < g1:
            results.pop(results.index(x_max))
        else:
            g1_flag = False
    if g2_flag:
        g2 = abs(x_min - avrg) / deviat
        logging.warning(f'g2 {g2}')
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
    if conf_limits < 1:
        rank = 1
        for r, dec in enumerate(str(conf_limits)[2:]):
            if int(dec) >= 3:
                r += 1
                conf_limits = f'{conf_limits:.rf}'
                break
            elif dec == '0':
                continue
            else:
                r += 2
                conf_limits = f'{conf_limits:.rf}'
                break

    pass

def main(results, prob):
    g1_flag, g2_flag = True, True
    while True:
        logging.debug(results)
        avrg = average(results)
        deviat = deviation(results, avrg)
        logging.warning(deviat)
        g1_flag, g2_flag = blunder(results, avrg, deviat, g1_flag, g2_flag)
        if not g1_flag and not g2_flag:
            break
    avrg_deviat = deviat / len(results) ** (1 / 2)
    conf_limits = t_distibution_dict[len(results)][prob] * avrg_deviat

    print(f'{avrg}+-{conf_limits}')

main([7.47, 7.5, 7.49, 7.58, 7.48], 0)
