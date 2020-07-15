"""An example library for converting temperatures."""


def convert_f_to_c(temperature_f):
    """Convert Fahrenheit to Celsius."""
    temperature_c = (temperature_f - 32) * (5/9)
    return temperature_c


def convert_c_to_f(temperature_c):
    """Convert Celsius to Fahrenheit."""
    temperature_f = (temperature_c * 9/5) + 32
    return temperature_f


## CREATE THE ADDITIONAL FUNCTIONS BELOW


# convert_c_to_k
def convert_c_to_k(temperature_c):
    temperature_k = temperature_c + 273.15
    return temperature_k 


# convert_f_to_k
def convert_f_to_k(temperature_f):
    temperature_c = (temperature_f - 32) * 5/9
    temperature_k = temperature_c + 273.15
    return temperature_k

# convert_k_to_c
def convert_k_to_c(temperature_k):
    temperature_c= temperature_k - 273.15
    return temperature_c


# convert_k_to_f
def convert_k_to_f(temperature_k):
    temperature_c = temperature_k - 273.15
    temperature_f = (temperature_c * 9/5) + 32
    return temperature_f


## LEVEL UP

# convert_f_to_all
#def convert_f_to_all(temperature_f):
#    x = temperature_c = (temperature_f - 32) * 5/9
#    y = x + 273.15
#    return (x,y)

def f_to_all(temperature_f):
    x = temperature_c = (temperature_f - 32) * 5/9
    y = x + 273.15
    print("The temperature " + str(temperature_f) + " F is: \n - " + str(x) + " in C \n - " + str(y) + " in k")
    #return (x,y)

# convert_f_to_all returning a DataFrame
def convert_f_to_all_DF(temperature_f): 
    x = temperature_c = (temperature_f - 32) * 5/9
    y = x + 273.15
    df = pd.DataFrame({'Celcius': [x], 'Kelvin': [y]})   
    return df

