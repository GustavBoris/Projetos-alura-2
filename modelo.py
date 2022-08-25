class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0  # assim define que todos filmes começarão com 0 likes

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def imprime(self):
        print(f' {self._nome} - {self.ano} - {self._likes} Likes')

class Filme(Programa): #dentro do parentes é a classe mae
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #a  função super chama qualquer metodo da classe mae, chama o inicializador da classe mae
        self.duracao = duracao

    def __str__(self): # str é uma orientação textual para o elemento
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(Programa): #dentro do parentes é a classe mae
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano) #a função super chama qualquer metodo da classe mae, chama o inicializador da classe mae
        self.temporadas = temporadas

    def imprime(self):
        return f' {self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'

class Playlist(list): #esta herdando de list
        def __init__(self, nome, programas):
            self.nome = nome
            super().__init__(programas) #definindo a lista de programas no inicializador na playlist




# Nome do filme e serie
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
supernatural = Serie('supernatural', 2007, 25)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016,2)


# Quantidade de likes em cada um
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
demolidor.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.dar_like()
supernatural.dar_like()


filmes_e_series = [vingadores, supernatural, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    print(programa)

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')