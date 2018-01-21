import fileinput


#Gathered from here
#https://www.pythoncentral.io/how-to-check-if-a-string-is-a-number-in-python-including-unicode/
def is_number(s):
    foundDecimal = False
    for c in s:
        if(c == '.'):
            if(foundDecimal == False):
                foundDecimal = True
            else:
                return False
    if(foundDecimal == False):
        return False

    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False


f = open('receipt.txt', 'r')
itemsName = []
itemsPrice = []
subtotal = 0
tax = 0

# Scan the file
for line in f:
    # Clean up the numbers
    line = line.replace('$', '')
    if('subtotal' in line.lower() or 'sub-total' in line.lower() or 'sub total' in line.lower()):
        break
    if(is_number(line)):
        print(line)
        itemsPrice.append(float(line))

# After reaching subtotal, scan in the subtotal and tax
while True:
    # Clean up the numbers
    line = line.replace('$', '')
#    print("THIS IS LINE: " + line)
    if(is_number(line)):
        break
    print(line)
    line = next(f)
subtotal = float(line)
tax = float(next(f).replace('$', ''))

# Printlines for testing
print(itemsName)
print(itemsPrice)
print(subtotal)
print(tax)

f.close()


#END