import re

def _decimal_to_binary(decimal_num:int)->list:
    result = []
    if decimal_num == 0:
        return [0]
    while decimal_num != 0:
        result.append(decimal_num%2)
        decimal_num = decimal_num//2
    return result

def _parse_cidr(cidr_str:str)->list:
    result = []
    if re.fullmatch('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\/[0-9]{1,2}',cidr_str):
        for s in re.split('[\.\/]',cidr_str):
            k = int(s)
            if k > 255:
                raise ValueError('Over 255')
            result.append(k)
    else:
        raise ValueError('Pattern wrong')
    if result[4] > 32:
        raise ValueError('MASK over then 32')
    return result

def check_cidr(cidr_str:str)-> tuple:
    parsed_cidr = _parse_cidr(cidr_str)
    binary_cidr = []
    r = parsed_cidr[4]//8
    k = parsed_cidr[4]%8
    # check mask 0 or 8 or 16 or 24 or 32
    if k != 0:
        # dicimal ip to binary
        for i in range(4):
            binary_cidr.append(_decimal_to_binary(parsed_cidr[i]))
        # check ip range
        for i in range(8-k):
            if len(binary_cidr[r]) > i:
                if binary_cidr[r][i] != 0:
                    return (False,'Input value range is wrong')
                    # raise ValueError('Input value range is wrong')
    else:
        for i in range(4-r):
            if parsed_cidr[3-i] != 0:
                return (False,'Input value range is wrong')
                # raise ValueError('Input value range is wrong')
    # return (True,parsed_cidr)
    return (True,'OK')