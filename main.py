def celcius_to_fahrenheit(celcius:float) -> float:
    '''
    this function converts a temperature in degrees celcius to degrees fahrenheit
    :param celcius:
    :return:
    '''
    if type(celcius) not in [int, float]:
        raise TypeError("Temperature must be given as a float")
    celcius = float(celcius)
    if celcius < -273.15:
        raise ValueError("temperature must be above absolute zero")
    return (celcius * (9.0/5.0)) + 32

    try:
        print(celcius_to_fahrenheit(20))
    except TypeError as e:
        print("an error occurred", e.args)
    except ValueError as e:
        print("an error occurred", e.args)