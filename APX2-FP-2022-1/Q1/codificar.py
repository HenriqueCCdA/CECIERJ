import struct
from constantes import MOEDA_BYTES
from exececoes import ExceptionSize


def campo_tamanho_fixo(campo, size):
    campo_bytes = bytes(campo.strip(), 'utf-8')
    tamanho_bytes = len(campo_bytes)

    try:
        campo = campo_bytes + bytes(size - tamanho_bytes)
    except ValueError:
        raise ExceptionSize(f'A string {campo} tem mais que o tamanho máximo de {size} bytes')

    return campo


def codificar(nome_txt='conversoes.txt'):

    conversoes = []
    with open(nome_txt) as f:
       conversoes = f.readlines()

    nome_bin = nome_txt.split('.')[0] + '.bin'

    with open(nome_bin, 'wb') as f:
        for c in conversoes:
            moeda1, moeda2, valor = c.split('#')

            f.write(campo_tamanho_fixo(moeda1, MOEDA_BYTES))
            f.write(campo_tamanho_fixo(moeda2, MOEDA_BYTES))
            f.write(struct.pack('d', float(valor)))



if __name__ == '__main__':
    codificar()
