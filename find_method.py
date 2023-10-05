Digits='X-DSPAM-Confidence: 0.8475 '
#In order to find the position in which the number starst
num1 = Digits.find('0')

piece = Digits[num1:]
numero = float(piece)
print(numero + 23)

file = open('xyz.txt', 'r')
d = file.read()
print(d)