import re

file = open("ressources/day_one_input.txt", "r")
print('Day one')

numberPairs = []

for line in file.readlines():
    digits = re.findall(r'\d', line)

    if digits:
        first_num = digits[0]
        last_num = digits[-1]
        numberPairs.append([first_num, last_num])
        print(f"Ligne traitée: {line.strip()}, Chiffres extraits: {digits}, Paire: {first_num}, {last_num}")

file.close()

result = 0
for pair in numberPairs:
    number = int(''.join(pair))
    print(f"Nombre formé à partir de la paire {pair}: {number}")
    result += number

print("Résultat total:", result)
