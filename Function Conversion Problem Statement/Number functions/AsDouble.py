#using ADF toDouble function
def double_wrapper(inp):
    updated_inp = inp / 4.32  # Seeing the Data Stage function example I am dividng the number by 4.32
    otp = toDouble(updated_inp) 
    return otp
