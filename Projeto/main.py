def sum_numbers(text: str) -> int:
    palavras = text.split(' ')
    soma = 0
    numeros = []
    for palavra in palavras:
        try:
            numeros.append(int(palavra))
        except:
            pass
    if numeros:
        for numero in numeros:
            soma += numero
    else:
        soma = 0
    return soma


print(sum_numbers(input()))
