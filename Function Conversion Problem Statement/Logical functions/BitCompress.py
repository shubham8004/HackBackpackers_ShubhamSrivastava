#Using ADF toBinary & toInteger functions
def bitAnd_wrapper(binary_string):
  binary_num = toBinary(binary_string)
  int_num = toInteger(binary_num)
  return int_num
