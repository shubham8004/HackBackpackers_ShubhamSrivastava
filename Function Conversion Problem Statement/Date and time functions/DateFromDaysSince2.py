#Using ADF addDays function
def DateFromDaysSince(input_date_as_string, num_to_be_added):
    return addDays(toDate(input_date_as_string), num_to_be_added)
