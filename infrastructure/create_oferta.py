#!python

from entities.oferta import Oferta
from daos import OfertaDAO
from connection import get_connection

nova_oferta = Oferta({
    'disciplina': 'calculo-numerico',
    'alunos_matriculados': ['ricky', 'morty'],
    'alunos_pendentes': ['jef'],
    'max_alunos': 25
})

conn = get_connection()
oferta_dao = OfertaDAO(conn)

todas_ofertas = oferta_dao.get_all()
print('todas as ofertas na tabela')
print(list(oferta.disciplina for oferta in todas_ofertas))

print(f'criando oferta {nova_oferta.disciplina}')
oferta_dao.create(nova_oferta)

print('oferta criada calculo-numerico')
oferta_criada = oferta_dao.get_oferta(2)
print(f'oferta {oferta_criada.disciplina} - {oferta_criada.alunos_matriculados}')

todas_ofertas = oferta_dao.get_all()
print('todas as ofertas na tabela')
print(list(oferta.disciplina for oferta in todas_ofertas))

