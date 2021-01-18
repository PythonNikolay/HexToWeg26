# Example:
# card_uid B438F525 = F538B4 (321)
# F5 to DEC = 245
# 38B4 to DEC = 14516
# wiegand = 245,14516
# 4 byte and 7 byte cards

def uid_to_weg26 (card_uid):
    card_uid = card_uid
    uid_to_321 = card_uid[4:6] + card_uid[2:4] + card_uid[0:2]
    hex_to_dec_1 = int(card_uid[4:6], 16) # Hex to dec 1 element
    hex_to_dec_2_3 = int(card_uid[2:4] + card_uid[0:2], 16) # Hex to dec 2 and 3 element
    wiegand26 = (str(hex_to_dec_1).rjust(3, str(0)) + "," + str(hex_to_dec_2_3).rjust(5, str(0)))
    return print(wiegand26)

uid_to_weg26("B438F525")
uid_to_weg26("1D115631000001")