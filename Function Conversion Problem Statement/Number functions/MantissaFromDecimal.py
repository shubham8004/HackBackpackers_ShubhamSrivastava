#using ADF toFloat function
def float_wrapper(inp):
    # Assuming the number is a decimal point number , we will first convert it to string and then split by '.'  (decimal) and take the last portion
    inp_string = toString(inp)
    manitssa_part = split(inp_string, '.')[1]
    return manitssa_part
