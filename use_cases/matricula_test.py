import matricula
from entities.aluno import Aluno
from entities.oferta import Oferta

def test_eh_possivel_matricular_se_houver_vagas():
    aluno_requerente = Aluno({
        "id": 1,
        "nome": "Fulano",
        "curso": "Engenharia",
        "disciplinas_matriculadas": ["Cálculo", "Circuitos"],
        "disciplinas_requisitadas": ["Eletrônica"]
    })
    oferta = Oferta({
        "disciplina": "Eletrônica",
        "alunos_matriculados": [2, 3],
        "alunos_pendentes": [1],
        "max_alunos": 20
    })

    oferta_alterada, aluno_matriculado, = matricula.aprovar_matricula(oferta, aluno_requerente)
    assert(aluno_matriculado.disciplinas_matriculadas == ["Cálculo", "Circuitos", "Eletrônica"])
    assert(aluno_matriculado.disciplinas_requisitadas == [])

    assert(oferta_alterada.alunos_matriculados == [2, 3, 1])

# TODO
# def test_nao_eh_possivel_matricular_se_nao_houver_vagas():
