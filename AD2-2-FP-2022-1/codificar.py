from constantes import BANDEIRA_BYTES, VALOR_BYTES
from exececoes import ExceptionSize


def campo_tamanho_fixo(campo, size):
    campo_bytes = bytes(campo.strip(), 'utf-8')
    tamanho_bytes = len(campo_bytes)

    try:
        campo = campo_bytes + bytes(size - tamanho_bytes)
    except ValueError:
        raise ExceptionSize(f'A string {campo} tem mais que o tamanho máximo de {size} bytes')

    return campo


def codificar(nome_txt='cartao.txt'):

    cartoes = []
    with open(nome_txt) as f:
       cartoes = f.readlines()

    nome_bin = nome_txt.split('.')[0] + '.bin'

    with open(nome_bin, 'wb') as f:
        for c in cartoes:
            bandeira, valor = c.split('#')

            f.write(campo_tamanho_fixo(bandeira, BANDEIRA_BYTES))
            f.write(campo_tamanho_fixo(valor, VALOR_BYTES))


if __name__ == '__main__':
    codificar()
