from config import ERROR_NUMB_LEN, ERROR_NUMB_PREFIX_PO


def checkpo(poid: str = None):
    valid = False
    err_msg = None
    if len(poid) != 10:
        err_msg = ERROR_NUMB_LEN
    elif poid[0:2] != '40':
        err_msg = ERROR_NUMB_PREFIX_PO
    else:
        valid = True
        err_msg = None
        # print("find PO Status")
    return valid, err_msg
