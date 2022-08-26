import unittest

from aplicacoes import CDI, Poupanca
from math_finc import jc


class TestPoupanca(unittest.TestCase):

    def test_taxa_juros_selic_menor_que_85(self):

        apli = Poupanca(capital_inicial=None, selic_anual=13.25)

        self.assertAlmostEqual(apli.taxa_rendimento_anual, 6.17, delta=1e-2)
        self.assertAlmostEqual(apli.taxa_rendimento_mensal, 0.5, delta=1e-2)



    def test_taxa_juros_selic_maior_que_85(self):

        apli = Poupanca(capital_inicial=None, selic_anual=8.0)

        self.assertAlmostEqual(apli.taxa_rendimento_anual, 5.6, delta=1e-2)
        self.assertAlmostEqual(apli.taxa_rendimento_mensal, 0.46, delta=1e-2)


    def test_montante(self):

        apli = Poupanca(capital_inicial=1000.0, selic_anual=13.25)

        acumulado, juros = apli.montante(meses=1)

        self.assertAlmostEqual(acumulado, 1005.00, delta=1e-2)
        self.assertAlmostEqual(juros, 0.5, delta=1e-2)


class TestCDI(unittest.TestCase):


    def test_redimento_liquido(self):
        apli = CDI(capital_inicial=1000.0, cdi_anual=13.15, rentabilidade_cdi=93)

        rendimento, imposto = apli.rendimento_liquido(meses=1)

        self.assertAlmostEqual(rendimento, 1007.49, delta=1e-2)
        self.assertAlmostEqual(imposto, 2.1737, delta=1e-4)


    def test_rentabilidade(self):
        apli = CDI(capital_inicial=None, cdi_anual=13.15, rentabilidade_cdi=93)

        r = apli.taxa_redimento_anual

        self.assertAlmostEqual(r, 12.23, delta=1e-2)


    def test_ir(self):

        tabela_ir = [
            (1, 22.5),
            (6, 22.5),
            (7, 20.0),
            (12, 20.0),
            (13, 17.5),
            (24, 17.5),
            (25, 15.0),
        ]

        for m, ir in tabela_ir:
            with self.subTest(meses=m, IR=ir):
                IR = CDI.ir(meses=m)
                self.assertAlmostEqual(IR, ir, delta=1e-2)
