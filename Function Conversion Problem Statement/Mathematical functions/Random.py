# Using ADF random function 
def random_wrapper(seed = 0):  # Setting the seed as 0 as Data Stage's random function returns value from 0 to pow(2,32)-1. 
    otp = random(seed)  
    return otp
