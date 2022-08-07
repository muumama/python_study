str = 'X-DSPAM-Confidence: 0.8475'

ipos = str.find(':')
print(ipos)
piece = str[ipos+2:]
value = float(piece)
print(value+1)
