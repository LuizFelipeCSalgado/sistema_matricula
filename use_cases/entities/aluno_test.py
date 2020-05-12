from aluno import Aluno

def test_deve_ser_possivel_criar_aluno():
    novo_aluno_info = {
        "id": 1,
        "nome": "Fulano",
        "curso": "Engenharia",
        "disciplinas_matriculadas": ["Cálculo", "Circuitos"],
        "disciplinas_requisitadas": ["Eletrônica"]
    }

    novo_aluno = Aluno(novo_aluno_info)
    assert(novo_aluno.id == 1)
    assert(novo_aluno.nome == "Fulano")
    assert(novo_aluno.curso == "Engenharia")
    assert(novo_aluno.disciplinas_matriculadas == ["Cálculo", "Circuitos"])
    assert(novo_aluno.disciplinas_requisitadas == ["Eletrônica"])
    
