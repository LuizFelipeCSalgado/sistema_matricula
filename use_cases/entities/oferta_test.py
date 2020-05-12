from oferta import Oferta

def test_deve_ser_possivel_criar_oferta():
    nova_oferta_info = {
        "disciplina": "Cálculo",
        "alunos_matriculados": [2, 3],
        "alunos_pendentes": [1],
        "max_alunos": 20
    }

    nova_oferta = Oferta(nova_oferta_info)

    assert(nova_oferta.disciplina == "Cálculo")
    assert(nova_oferta.alunos_matriculados == [2, 3])
    assert(nova_oferta.alunos_pendentes == [1])
    assert(nova_oferta.max_alunos == 20)

