print(" *** Wind classification ***")
windspeed = float(input("Enter wind speed (km/h) : "))
def windclassification(windspeed):
    if windspeed > 0 and windspeed <= 51.99:
        return "Breeze"
    elif windspeed >= 52.00 and windspeed <= 55.99:
        return "Depression"
    elif windspeed >= 56.00 and windspeed <= 101.99:
        return "Tropical Storm"
    elif windspeed >= 102.00 and windspeed <= 208.99:
        return "Typhoon"
    else:
        return "Super Typhoon"


print("Wind classification is "+windclassification(windspeed)+".")
