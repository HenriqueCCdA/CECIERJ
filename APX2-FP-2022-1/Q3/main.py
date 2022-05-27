NAME_TEMP_FILE = '.temp'

def eh_primo(numero):

    numero = abs(int(numero))

    if numero == 1 or numero == 0:
        return False

    for i in range(numero-1, 1, -1):
        if numero % i == 0:
            return False

    return True


def imprime_arquivo(nome_arquivo):
    with open(nome_arquivo) as f:

        while True:

            linha = f.readline()

            if not linha:
                break

            print(linha, end='')

def retira_primos(nome_arquivo):

    with open(NAME_TEMP_FILE, 'w') as f_temp:

        with open(nome_arquivo) as f:

            while True:

                linha = f.readline()

                if not linha:
                    break

                numeros = linha.split()

                tem_primo = False
                for n in numeros:
                    if eh_primo(n):
                        tem_primo = True
                        break

                print(' '.join(numeros))

                if not tem_primo:
                    f_temp.write(' '.join(numeros))
                    f_temp.write('\n')


def novo_arquivo(nome_arquivo):
    import os
    # renomenado o arquivo temporario
    os.rename(NAME_TEMP_FILE, nome_arquivo)


def main(nome_arquivo):

    retira_primos(nome_arquivo)

    # Arquivo original
    print()
    print(f'Conteúdo do Arquivo {nome_arquivo}')
    imprime_arquivo(nome_arquivo)

    novo_arquivo(nome_arquivo)

    # Arquivo modificado
    print()
    print(f'Conteúdo do Arquivo {nome_arquivo} apos eventuais remoções.')
    imprime_arquivo(nome_arquivo)

if __name__ == '__main__':
    main('numeros.txt')