# Перевести все буквы в заглавные

input = input()

output = ''

offset = ord('A') - ord('a')

for c in input:
    o = ord(c)
    if ord('a') <= o <= ord('z'):
        output += chr(o + offset)
    else:
        output += c

print(output)

