palabraSinVocal = ""

userWord = input("Ingresa una palabra: ")
userWord = userWord.upper()

for letra in userWord:
    if letra in ['A', 'E', 'I', 'O', 'U']:
        continue
    palabraSinVocal += letra

print(palabraSinVocal)
