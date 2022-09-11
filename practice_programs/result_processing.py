# Program for result processing.
# Rules taken from GOST P 8.736-2011.

# Find blunder in measurment results if exist.
def blunder():
    pass


# Find arithmetic mean.
def average(results):
    return sum(results) / len(results)


# Find standart deviation.
def deviation(results, avrg):
    return (sum([(x - avrg) ** 2 for x in results]) / (len(results) - 1))
    pass


def main(resultes, alpha):
    while True:
        avrg = average(results)
        deviat = deviation(results, avrg)

    pass
