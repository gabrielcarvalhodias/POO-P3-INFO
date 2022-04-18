class Alunos:
    def __init__(self, nomeal, matricula, nota):
        self.nomeal = nomeal
        self.matricula = matricula
        self.nota = nota

class Disciplinas(Alunos):
    def __init__(self):
        self.nome = []
        if self.nomeal in self.nome:
            print('você está na turma!')
        else:
            self.nome = [self.nomeal]

gab = Alunos('gab', '990', 8)
Disciplinas()