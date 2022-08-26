from math_finc import jc, year2month


class Poupanca:

    def __init__(self, capital_inicial, selic_anual):
        self.capital_inicial = capital_inicial
        self.taxa_rendimento_anual = self._taxa_rendimento_anual(selic_anual)


    def _taxa_rendimento_anual(self, selic_anual):
        if selic_anual < 8.5:
            return 0.7 * selic_anual
        return 6.17

    @property
    def taxa_rendimento_mensal(self):
        return year2month(self.taxa_rendimento_anual/100)


    def montante(self, meses):

        juros = jc(self.taxa_rendimento_mensal/100, meses)

        return self.capital_inicial * (juros + 1), juros * 100


class CDI:

    def __init__(self, capital_inicial, cdi_anual, rentabilidade_cdi):
        self.capital_inicial = capital_inicial
        self.cdi_anual = cdi_anual
        self.rentabilididade_cdi = 0.01 * rentabilidade_cdi * cdi_anual


    @staticmethod
    def ir(meses):
        if meses <= 6:
            return 22.5
        elif 6 < meses <= 12:
            return 20.0
        elif 12 < meses <= 24:
            return 17.5
        elif meses > 24:
            return 15.0

    @property
    def taxa_redimento_anual(self):
        return self.rentabilididade_cdi

    @property
    def taxa_rendimento_mensal(self):
        return year2month(self.rentabilididade_cdi/100)


    def rendimento_liquido(self, meses):

        juros = jc(self.taxa_rendimento_mensal/100, meses)

        ir = self.ir(meses) / 100

        rendimento = juros * self.capital_inicial
        imposto = rendimento * ir

        return self.capital_inicial + rendimento - imposto, imposto