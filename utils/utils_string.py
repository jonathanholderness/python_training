def capitalise(str):
    """
    Capitalises the first letter of a string and makes the rest of the letters lowercase.

    """
    if len(str) <=1 :
        return str.upper()
    return str[0].upper() + str[1:].lower()
