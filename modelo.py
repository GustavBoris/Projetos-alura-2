class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0  # assim define que todos filmes começarão com 0 likes

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'


class Filme(Programa):  # dentro do parentes é a classe mae
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,
                         ano)  # a  função super chama qualquer metodo da classe mae, chama o inicializador da classe mae
        self.duracao = duracao

    def __str__(self):  # str é uma orientação textual para o elemento
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'


class Serie(Programa):  # dentro do parentes é a classe mae
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,
                         ano)  # a função super chama qualquer metodo da classe mae, chama o inicializador da classe mae
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):  # ter as vantagens de iterável de um list, sem precisar fazer herança
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


# Nome do filme e serie
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

# Quantidade de likes em cada um
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')

