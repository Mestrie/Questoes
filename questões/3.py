def inverter_string(string):
    inverted_string = ""
    for i in range(len(string) - 1, -1, -1):
        inverted_string += string[i]
    return inverted_string

entrada = input("Digite uma string para inverter: ")

print("String invertida:", inverter_string(entrada))
