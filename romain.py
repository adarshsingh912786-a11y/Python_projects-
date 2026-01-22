Roman_map = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

value = [(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]

def roman_to_dec(roman):

    roman = roman.upper()
    total = 0

    for i in range(len(roman)):
        if roman[i] not in Roman_map:
            return None
        
        value = Roman_map[roman[i]]

        if i+1 < len(roman) and value < Roman_map.get(roman[i+1]):
            total -= value
        else:
            total += value
    
    return total

def main():
    print("-------Roman Converter-----")
    user = input("Enter the roman number: ")
    answer = roman_to_dec(user)
    print(answer)

main()

