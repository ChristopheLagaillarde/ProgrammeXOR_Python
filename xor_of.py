# Program : xor_of
# Description : give the xor of 2 boolean value
# Date : 24/05/22
# Author : Christophe Lagaillarde
# Version :1.0

def xor_of(bool_value1, bool_value2):
    if not isinstance(bool_value1, bool) or not isinstance(bool_value2, bool):
        raise TypeError
    elif bool_value1 is True or bool_value2 is True:
        if bool_value1 == bool_value2:
            return False
        else:
            return True
    else:
        return False


