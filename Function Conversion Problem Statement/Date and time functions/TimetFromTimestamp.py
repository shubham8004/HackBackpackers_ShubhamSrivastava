#using ADF's minus function or using '-' operator. They both are valid ADF objects
def unixt_wrapper(inp):
    # First convert given input date to timestamp
    input_dts= toTimestamp(inp)
    # First convert given input date to timestamp
    current_ts = currentTimestamp()
    # Find the difference using '-' operator
    difference_in_ms_using_minus_operater = toTimestamp(current_ts, 'yyyy-MM-dd HH:mm:ss.SSS') - toTimestamp(input_dts, 'yyyy-MM-dd HH:mm:ss.SSS')
    # Alternative using ADF's minus function
    difference_in_ms_using_minus_fn = minus(current_ts, input_dts)
    difference_in_seconds = difference_in_ms_using_minus_operater * 0.001
    difference_in_seconds_from_minus_function = difference_in_ms_using_minus_fn * 0.001
    return difference_in_seconds   # OR return difference_in_seconds_from_minus_function
