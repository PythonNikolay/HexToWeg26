# Example:
# Card 0xB438F525 - input without "0x"
# card_uid B438F525 = F5 38B4 (3,2,1 read byte)
# F5 to DEC = 245
# 38B4 to DEC = 14516
# wiegand26 = 245,14516

def uid_to_weg26(card_uid):
	
	uid_to_321 = card_uid[4:6] + card_uid[2:4] + card_uid[0:2]
	hex_to_dec_1 = int(card_uid[4:6], 16) # Hex to dec 1 byte
	hex_to_dec_2_3 = int(card_uid[2:4] + card_uid[0:2], 16) # Hex to dec 2 and 3 byte
	wiegand26 = (str(hex_to_dec_1).rjust(3, str(0)) + "," + str(hex_to_dec_2_3).rjust(5, str(0)))
	
	return print (wiegand26)

print("Enter/Paste your UIDs. Ctrl-D or Ctrl-Z ( windows ) to convert it.")
uids = []
while True:
    try:
        line = input()
    except EOFError:
        break
    uids.append(line)
while("" in uids): 
    uids.remove("") #remove empty elements

print("---Wiegand26---")
for x in uids:
	uid_to_weg26(x)

