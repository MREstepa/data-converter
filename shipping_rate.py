
def get_shipping_rate(location, weight:float):
    "Returns shipping_rate (int) depending on location and weight"

    mindanao = {
        "0-0.5": 85,
        "0.5-1": 155,
        "1-3": 180,
        "3-4": 270,
        "4-5": 360,
        "5-6": 455,
        "6-7": 565,
        "7-8": 605,
        "8-9": 703,
        "9-10": 801,
        "10-11": 899,
        "11-12": 997,
        "12-13": 1095,
    }
    manila = {
        "0-0.5":105,
        "0.5-1":195,
        "1-3":215,
        "3-4":325,
        "4-5":435,
        "5-6":545,
        "6-7":640,
        "7-8":680,
        "8-9":796,
        "9-10":912,
        "10-11":1028,
        "11-12":1144,
        "12-13":1260
    }

    if location == "Mindanao": shipping_rates = mindanao
    elif location == "Manila": shipping_rates = manila

    for rec in shipping_rates:
        rate = rec.split('-')
        lower_bound = float(rate[0])
        upper_bound = float(rate[1])

        if ((lower_bound < weight) and (weight <= upper_bound)):
            return shipping_rates[rec]
