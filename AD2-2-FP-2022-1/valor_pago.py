from pathlib import Path
import sys

from constantes import BANDEIRA_BYTES, VALOR_BYTES
from exececoes import ValidacaoError, BandeiraError


class Cartoes:

    def __init__(self, arquivo_bin):
        self.arquivo_bin = arquivo_bin
        self.cartoes = {}

    def checa_cartao(self, bandeira):
        try:
            self.cartoes[bandeira]
        except KeyError:
            raise BandeiraError(f'Cartão não consta: {bandeira}')

    def get_cartao(self, bandeira):
        self.checa_cartao(bandeira)
        return self.cartoes[bandeira]

    def lendo_arquivo(self):

        with open(self.arquivo_bin, 'rb') as f:
            while True:

                bandeira = f.read(BANDEIRA_BYTES)
                valor = f.read(VALOR_BYTES)

                if not bandeira and not valor:
                    break

                bandeira = bandeira.decode('utf-8').rstrip('\x00')
                valor = float(valor.decode('utf-8').rstrip('\x00'))

                self.cartoes[bandeira] = Cartao(bandeira, valor)


class Cartao:
    def __init__(self, bandeira, adicional):
        self.bandeira = bandeira
        self.adicional = adicional

    def valor_final(self, taxa_conv, valor):
        return valor * taxa_conv + self.adicional


def valida_entrada(arquivo_bin, bandeira, taxa_conv, valor):

    if not Path(arquivo_bin).is_file():
        raise ValidacaoError('Um dos arquivos não foi encontrado ou digitou errado')

    try:
        taxa_conv = float(taxa_conv)
    except ValueError:
        raise ValidacaoError(f'você colocou um taxa não correspondente: {taxa_conv}')

    try:
        valor = float(valor)
    except ValueError:
        raise ValidacaoError(f'você colocou um valor não correspondente: {valor}')

    return arquivo_bin, bandeira, taxa_conv, valor


def main(argv):

    try:
        arquivo_bin, bandeira, taxa_conv, valor = valida_entrada(*argv[1:])

        cartoes = Cartoes(arquivo_bin)

        cartoes.lendo_arquivo()

        cartao = cartoes.get_cartao(bandeira)

        valor_total = cartao.valor_final(taxa_conv, valor)

        print(f'Como o seu cartão é da bandeira {bandeira}, então você parará {valor_total:.2f}')

    except (ValidacaoError, BandeiraError) as e:
        print(e)


if __name__ == '__main__':
    main(sys.argv)