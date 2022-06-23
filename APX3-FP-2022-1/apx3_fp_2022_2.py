def eh_par(c):
    if c == 0:
        return False
    return c % 2 == 0

def main():

    entrada = input('Entre com o nome do arquivo: \n')

    contador_valor_posicao_iguais = 0
    elementos_pares = []
    c_anterior = entrada[0]
    ordernado = True
    for i, c in enumerate(entrada, start=1):

        if not c.isdigit():
            print(f'A entrada {entrada} não está no formato solicitado')
            return

        if i == int(c):
            contador_valor_posicao_iguais += 1

        if eh_par(int(c)):
            elementos_pares.append(c)

        if int(c) < int(c_anterior):
            ordernado = False

        c_anterior = c

    if not contador_valor_posicao_iguais:
        print(f'Na entrada {entrada} não há elementos com valores iguais as suas posições')
    else:
        print(f'Na entrada {entrada} há {contador_valor_posicao_iguais} elemento com valor igual as suas posição')

    if ordernado:
        print(f'A entrada {entrada} está ordena')
        print(f'A lista dos elementos pares de {entrada} em ordem de aparição é {elementos_pares}')
    else:
        print(f'A entrada {entrada} não está ordena')


if __name__ == '__main__':
    main()