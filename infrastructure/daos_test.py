from entities.aluno import Aluno
from daos import AlunoDAO
from connection import get_cursor

cursor = get_cursor()

def test_eh_possivel_adicionar_aluno():
    aluno_dao = AlunoDAO(cursor)
    novo_aluno = Aluno({
        "nome": "fulano",
        "curso": "engenharia",
        "disciplinas_matriculadas": ["calculo", "circuitos"],
        "disciplinas_requisitadas": ["eletronica"]
    })

    success = aluno_dao.create(novo_aluno)
    assert(success is True)
