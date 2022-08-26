import math


def jc(r:float,t:int ,n:int=1) -> float :
    '''
    ## Juros compostos .
    #
    #  É a adição de juros ao capital principal de um empréstimo ou depósito, ou em outras palavras,
    #  juros sobre juros.
    #
    #  É o resultado do reinvestimento dos juros, ao invés de pagá-lo, de tal forma que a taxa no
    #  próximo período é calculada sobre o principal, mais os juros recebidos previamente.
    #
    #  A função de acumulação mostra como uma unidade monetária cresce após o período de tempo.
    #
    #  @param r taxa de juros nominal.
    #  @param t período de tempo total no qual os juros são aplicados (expressa nas mesmas
    #         unidades de tempo de r, usualmente anos).
    #  @param n frequência de composição(pagamento dos juros), por exemplo, mensal, trimestral
    #         ou anual.
    #  @return juros obtidos no período : (1 + r/n)^nt − 1
    #
    '''
    return (1 + r / float(n))**(n*t) - 1


def day2year(d:float, wd:int=252) -> float :
    '''
    ## Converte uma taxa diária para uma taxa anual .
    #  Em matemática financeira, consideramos 252 dias por ano .
    #
    #  @param d taxa de juros diária.
    #  @param wd número de dias úteis por ano .
    #  @return taxa de juros anual dada a taxa diária, na forma de um percentual.
    #
    '''
    return 100 * jc(d, wd)

def year2month(a:float) -> float :
    '''
    # Converte uma taxa de juros anual para uma taxa mensal.
    #
    #   @param a taxa de juros anual .
    #   @return taxa de juros mensal dada a taxa anual,na forma de um percentual.
    #
    '''
    return 100 * jc(a, 1/12.0)


def doublePrincipal(r:float) -> float:
    '''
    ## Calcula o logaritmo de 2 na base 1 + r.
    #   Pode ser aproximado por 72/(100 ∗ r).
    #
    #   É usada para calcular o tempo necessário
    #   para dobrar o principal quando sujeito uma taxa de juros dada.
    #
    #   @param r taxa de juros nominal.
    #   @return tempo para dobrar o principal.
    #
    '''
    return math.log(2, 1 + r)
