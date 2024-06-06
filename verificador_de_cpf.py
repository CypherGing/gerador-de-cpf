import os
from time import sleep

multiplicador = 1
true_digit1 = 100
true_digit2 = 100
soma1 = 0
soma2 = 0
indesejados = ",-.*&¨%$#@!'"
while True:
    print(" "*30)
    raw_input = input("   Digite seu CPF: ")
    trated_raw_input = raw_input
    for char in indesejados:
        trated_raw_input = trated_raw_input.replace(char, "")

    sus_digit1 = int(trated_raw_input[len(trated_raw_input) - 2])
    sus_digit2 = int(trated_raw_input[len(trated_raw_input) - 1])
    print(sus_digit1)
    print(sus_digit2)
    cpf_9 = trated_raw_input[:9]
    print(raw_input, trated_raw_input, cpf_9)

    reversed_cpf_9 = cpf_9[::-1]
    print(reversed_cpf_9)


    if reversed_cpf_9.isnumeric() == True:
        if len(cpf_9) < 9 or len(cpf_9)> 9:
            print("CPF inválido, tente novamente")
            sleep(2)
            os.system("clear")
        else:
            for n in reversed_cpf_9:
                multiplicador += 1
                print(f"{n} x {multiplicador} = {int(n)*multiplicador}")
                soma1 += int(n)*multiplicador
            print(soma1)
            multiplicador = 1
            if soma1 % 11 < 2:
                true_digit1 = 0
                print(f"Primeiro Dígito: {true_digit1}")
                if sus_digit1 != true_digit1:
                    print("CPF INVÁLIDO")
                    break
            
            elif soma1 % 11 >= 2:
                true_digit1 = 11 - (soma1 % 11)
                print(f"Primeiro Dígito: {true_digit1}")
                if sus_digit1 != true_digit1:
                    print("CPF INVÁLIDO!")
                    break

            reversed_cpf_9 = reversed_cpf_9[::-1]
            reversed_cpf_9 = reversed_cpf_9 + str(true_digit1)
            reversed_cpf_9 = reversed_cpf_9[::-1]
            print(reversed_cpf_9)
            for n in reversed_cpf_9:
                multiplicador += 1
                print(f"{n} x {multiplicador} = {int(n)*multiplicador}")
                soma2 += int(n)*multiplicador
            print(soma2)
            if soma2 % 11 < 2:
                true_digit2 = 0
                print(f"Segundo Dígito: {true_digit2}")
                if sus_digit2 != true_digit2:
                    print("CPF INVÁLIDO")
                    break
            elif soma2 % 11 >= 2:
                true_digit2 = 11 - (soma2 % 11)
                print(f"Segundo Dígito: {true_digit2}")
            
            print("="*30)
            print("CPF PERFEITAMENTE VÁLIDO!")
            print("="*30)
            multiplicador = 1
            true_digit1 = 100
            true_digit2 = 100
            soma1 = 0
            soma2 = 0
    else:
        print("_"*25)
        print("Digite apenas números")
        print("-"*25)
        sleep(2)
        os.system("clear")


