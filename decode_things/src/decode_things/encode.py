def str_hex(string):
    if isinstance(string, str):
        return string.encode().hex()
    else:
        raise TypeError("encode>1\nMore at: https://github.com/justwaitfor-me/decode_things/")
    
def int_hex(integer):
    if isinstance(integer, int):
        return hex(integer)
    else:
        raise TypeError("encode>1\nMore at: https://github.com/justwaitfor-me/decode_things/")
    