class Numero:
    def __init__(self, num, lin, col):
        self.num = num
        self.lin = lin
        self.col = col
        self.bloco = self.findbloco()
        if num == 0:
            self.protecao = False
            self.lpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.cpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.bpos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            self.protecao = True

    def findbloco(self):
        sublinha = int( str(self.lin) + str(self.col) )
        subcoluna = int( str(self.col) + str(self.lin) )
        if sublinha < 29:
            if subcoluna < 29:
                return 1
            if (subcoluna > 29) and (subcoluna < 59):
                return 2
            if subcoluna > 59:
                return 3
        if (sublinha > 29) and (sublinha < 59):
            if subcoluna < 29:
                return 4
            if (subcoluna > 29) and (subcoluna < 59):
                return 5
            if subcoluna > 59:
                return 6
        if sublinha > 59:
            if subcoluna < 29:
                return 7
            if (subcoluna > 29) and (subcoluna < 59):
                return 8
            if subcoluna > 59:
                return 9

    def possibilidade(self, lin, col, blo):
        for n in lin:
            if n != 0:
                try:
                    self.lpos.remove(n)
                except:
                    pass
        for n in col:
            if n != 0:
                try:
                    self.cpos.remove(n)
                except:
                    pass
        for n in blo:
            if n != 0:
                try:
                    self.bpos.remove(n)
                except:
                    pass
        lin = self.lpos.copy()
        col = self.cpos.copy()
        blo = self.bpos.copy()
        soma = self.lpos + self.cpos + self.bpos
        v = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.val = []

        for n in v:
            if soma.count(n) == 3:
                self.val.append(n)
        if len(self.val) == 1:
            global fim
            fim = 1
            self.num = self.val[0]
            self.protecao == True

    def ver(self):
        print(self.lpos)
        print(self.cpos)
        print(self.bpos)

    def Board(self, casa):
        x = 0
        y = 0
        i = 0
        while x < 9:
            y = 0
            while y < 9:
                print(casa[i].num, end='')
                i += 1
                y += 1
            print("\n")
            x += 1


grid = [
    [7, 1, 0, 4, 0, 6, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 8, 0],
    [0, 0, 9, 1, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 0, 0, 3, 0, 9],
    [0, 0, 0, 8, 1, 0, 0, 5, 0],
    [0, 0, 0, 9, 3, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 8, 0, 2],
    [0, 7, 1, 0, 0, 4, 6, 0, 5],
    [0, 0, 4, 5, 6, 3, 0, 0, 7]
]
x = 0
i = 0
casa = []
c = []
k = 0
q1 = []
q2 = []
q3 = []
q4 = []
q5 = []
q6 = []
q7 = []
q8 = []
q9 = []
fim = 1
leitura = 1
while fim:
    x = 0
    i = 0
    k = 0
    fim = 0
    q1.clear()
    q2.clear()
    q3.clear()
    q4.clear()
    q5.clear()
    q6.clear()
    q7.clear()
    q8.clear()
    q9.clear()
    while x < 9:
        y = 0
        while y < 9:  # transformando 9x9 em 1x81, carregando os blocos com os valores iniciais
            if leitura == 1:
                casa.append(Numero(grid[x][y], x, y))
            if leitura == 0:
                grid[x][y] = casa[k].num
            if casa[k].bloco == 1 and casa[k].num != 0:
                q1.append(casa[k].num)
            elif casa[k].bloco == 2 and casa[k].num != 0:
                q2.append(casa[k].num)
            elif casa[k].bloco == 3 and casa[k].num != 0:
                q3.append(casa[k].num)
            elif casa[k].bloco == 4 and casa[k].num != 0:
                q4.append(casa[k].num)
            elif casa[k].bloco == 5 and casa[k].num != 0:
                q5.append(casa[k].num)
            elif casa[k].bloco == 6 and casa[k].num != 0:
                q6.append(casa[k].num)
            elif casa[k].bloco == 7 and casa[k].num != 0:
                q7.append(casa[k].num)
            elif casa[k].bloco == 8 and casa[k].num != 0:
                q8.append(casa[k].num)
            elif casa[k].bloco == 9 and casa[k].num != 0:
                q9.append(casa[k].num)

            k += 1
            y += 1
            i += 1
        x += 1
    leitura = 0
    n = 0

    while n < len(casa):
        if not casa[n].protecao:
            l = grid[casa[n].lin][:]
            x = 0

            while x < 9:
                c.append(grid[x][casa[n].col])
                x += 1

            if casa[n].bloco == 1:
                casa[n].possibilidade(l, c, q1)
            elif casa[n].bloco == 2:
                casa[n].possibilidade(l, c, q2)
            elif casa[n].bloco == 3:
                casa[n].possibilidade(l, c, q3)
            elif casa[n].bloco == 4:
                casa[n].possibilidade(l, c, q4)
            elif casa[n].bloco == 5:
                casa[n].possibilidade(l, c, q5)
            elif casa[n].bloco == 6:
                casa[n].possibilidade(l, c, q6)
            elif casa[n].bloco == 7:
                casa[n].possibilidade(l, c, q7)
            elif casa[n].bloco == 8:
                casa[n].possibilidade(l, c, q8)
            elif casa[n].bloco == 9:
                casa[n].possibilidade(l, c, q9)
            c.clear()
        n += 1
casa[7].Board(casa)
