from math import sqrt


class Ponto:
    def __init__(self, line):
        self.x, self.y = map(float, line.split())

    def distancia(self, p):
        return sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

    def __str__(self):
        return f'{self.x} {self.y}'


def main():

    filename = input('Entre com o nome do arquivo: \n')

    print()
    with open(filename) as f:
        line = f.readline()

        print(f'Conteúdo do Arquivo {filename}:')

        if not line:
            print('Conteudo do arquivo vazio!!!')
            return

        p_novo = p_anterior = p_0 = Ponto(line)
        perimetro = 0.0
        while True:
            print(p_anterior)
            line = f.readline()
            if not line:
                break
            p_novo = Ponto(line)
            perimetro += p_novo.distancia(p_anterior)
            p_anterior = p_novo

        perimetro += p_novo.distancia(p_0)

        print()
        print(f'Perímetro do polígono de pontos contidos no arquivo: {perimetro:.2f}')

if __name__ == '__main__':
    main()