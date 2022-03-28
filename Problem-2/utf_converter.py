def utf_converter(utf8_string):
    result = []
    cur_codepoint = 0
    for byte in utf8_string:
        if byte < 128:
            if cur_codepoint != 0:
                result.append(cur_codepoint)
                cur_codepoint = 0
            result.append(bytearray(byte))
        elif byte < 192:
            cur_codepoint = cur_codepoint << 6
            cur_codepoint += byte & 63
        else:
            if cur_codepoint != 0:
                result.append(cur_codepoint)
                cur_codepoint = 0
            if byte < 224:
                cur_codepoint += byte & 31
            elif byte < 240:
                cur_codepoint += byte & 15           
            elif byte < 248:
                cur_codepoint += byte & 7
    if cur_codepoint != 0:
        result.append(cur_codepoint)
    
    return result

# def utf8_print_bin(str):
#     encoding = str.encode('utf-8')
#     for byte in encoding:
#         print(format(byte, '#010b'))
#     return

# def utf32_print_bin(str):
#     encoding = str.encode('utf-32-be')
#     for byte in encoding:
#         print(format(byte, '#010b'))
#     return

# def print_bytes(bytes):
#     for byte in bytes:
#         print(byte)
#     return