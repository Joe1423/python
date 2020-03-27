#modified so the test will fail

# def get_formatted_name (first, middle, last):
#     """Returns a neatly formatted name."""
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()

#This version will pass the test

def get_formatted_name(first, last, middle=''):
    """Returns a neatly formatted name."""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    
    return full_name.title()