import sys


PONTO = '.'
DOIS_PONTOS = ':'
VIRGULA = ','


def retira_caracteres_indesejados(palavras):
    for i in range(len(palavras)):
        p = palavras[i]

        if PONTO in p:
            p = p.replace(PONTO,'')
        elif DOIS_PONTOS  in p:
            p = p.replace(DOIS_PONTOS ,'')
        elif VIRGULA in p:
            p = p.replace(VIRGULA ,'')

        palavras[i] = p

    return palavras


def busca_palavra(palavra_buscada, palavras):
    for i, p in enumerate(palavras):
        if p == palavra_buscada:
            return i + 1
    return 0


def main(nome_arquivo, palavra_buscada):

    with open(nome_arquivo) as f:

        numero_da_linha = 1
        while True:

            linha = f.readline()

            if not linha:
                break

            palavras = retira_caracteres_indesejados(linha.split())

            pos = busca_palavra(palavra_buscada, palavras)

            if pos:
                print(f'Linha {numero_da_linha}, Palavra {pos} nesta linha!')

            numero_da_linha+=1


if __name__ == '__main__':
    main(*sys.argv[1:])

'''
Exemplo de uso:

python main.py sambaDeUmaNotaSo.txt nota
'''