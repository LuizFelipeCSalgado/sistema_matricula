#!python

from entities.aluno import Aluno
from daos import AlunoDAO
from connection import get_connection

novo_aluno = Aluno({
    "nome": "beltrano",
    "curso": "psicologia",
    "disciplinas_matriculadas": ["calculo", "circuitos"],
    "disciplinas_requisitadas": ["eletronica"]
})

conn = get_connection()
aluno_dao = AlunoDAO(conn)

todos_alunos = aluno_dao.get_all()
print('todos os alunos na tabela')
print(list(aluno.nome for aluno in todos_alunos))

print(f'criando aluno {novo_aluno.nome} - {novo_aluno.curso}')
aluno_dao.create(novo_aluno)

print('aluno criado beltrano')
aluno_criado = aluno_dao.get_aluno(1)
print(f'aluno {aluno_criado.nome} - {aluno_criado.curso}')

todos_alunos = aluno_dao.get_all()
print('todos os alunos na tabela')
print(list(aluno.nome for aluno in todos_alunos))
