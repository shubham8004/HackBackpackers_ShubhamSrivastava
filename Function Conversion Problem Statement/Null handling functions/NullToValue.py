#using ADF iifNull function
def notnullvalue_wrapper(inp , def_inp = 10):
    otp = iifNull(inp, def_imp)   
    return otp
