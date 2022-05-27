from pathlib import Path
import struct
import sys


from constantes import MOEDA_BYTES
from exececoes import ValidacaoError


NOMES_MOEDAS = dict(euro='EUR',real='BRL', dolar='USD')


class Conversoes:

    moedas = set()
    conversoes = {}

    def __init__(self, arquivo_bin):
        self.arquivo_bin = arquivo_bin
        self._lendo_arquivo()

    def valor_final(self, moeda1, moeda2, valor):

        key1 = f'{moeda1}-{moeda2}'
        key2 = f'{moeda2}-{moeda1}'

        if (cotacao:=self.conversoes.get(key1, None)) is not None:
            return valor * cotacao

        if (cotacao:=self.conversoes.get(key2, None)) is not None:
            return valor / cotacao

        return None

    def _lendo_arquivo(self):

        with open(self.arquivo_bin, 'rb') as f:
            while True:

                moeda1 = f.read(MOEDA_BYTES)
                moeda2 = f.read(MOEDA_BYTES)

                if not moeda1 and not moeda2:
                    break

                valor  = struct.unpack('d', f.read(8))[0]

                moeda1 = moeda1.decode('utf-8').rstrip('\x00')
                moeda2 = moeda2.decode('utf-8').rstrip('\x00')

                self.moedas.add(moeda1)
                self.moedas.add(moeda2)

                self.conversoes[f'{moeda1}-{moeda2}'] = valor

    @property
    def moedas_cadastradas(self):
        return self.moedas

    def __str__(self):

        line1 = f'conversoes: {self.conversoes}\n'
        line2 = f'moedas cadastras: {self.moedas}'

        return line1 + line2

    @classmethod
    def esta_cadastra(cls, moeda):
        return moeda in cls.moedas


def valida_entrada(arquivo_bin, moeda1, moeda2, valor):

    if not Path(arquivo_bin).is_file():
        raise ValidacaoError('Um dos arquivos não foi encontrado ou digitou errado')

    if Conversoes.esta_cadastra(moeda1):
        raise ValidacaoError(f'"Alguma moeda não consta: {moeda1}')

    if Conversoes.esta_cadastra(moeda2):
        raise ValidacaoError(f'"Alguma moeda não consta: {moeda1}')

    try:
        valor = float(valor)
    except ValueError:
        raise ValidacaoError(f'você colocou um valor não correspondente: {valor}')

    return arquivo_bin, moeda1, moeda2, valor


def main(argv):

    try:
        arquivo_bin, moeda1, moeda2, valor = valida_entrada(*argv[1:])
        cotacoes = Conversoes(arquivo_bin)

        valor_total = cotacoes.valor_final(moeda1, moeda2, valor)

        print(f'Você pagará {valor_total:.2f} {NOMES_MOEDAS[moeda2]} por {valor:.2f} {NOMES_MOEDAS[moeda1]}')

    except ValidacaoError as e:
        print(e)


if __name__ == '__main__':
    main(sys.argv)


'''
Exemplo

python main.py conversoes.bin euro real 1000
Você pagará 5170.00 EUR por 1000.00 BRL

python main.py conversoes.bin real euro 1000
Você pagará 193.42 EUR por 1000.00 BRL
'''