from entities.aluno import Aluno
from entities.oferta import Oferta

class MatriculaException(Exception):
    pass

def aprovar_matricula(oferta: Oferta, aluno: Aluno):
    if len(oferta.alunos_matriculados) >= oferta.max_alunos:
        raise MatriculaException("A oferta não tem mais vagas disponíveis")

    oferta_com_aluno_matriculado_info = {
        "disciplina": oferta.disciplina,
        "alunos_matriculados": [*oferta.alunos_matriculados, aluno.id],
        "alunos_pendentes": oferta.alunos_pendentes,
        "max_alunos": oferta.max_alunos
    }

    remover_disciplina = lambda disciplina: disciplina != oferta.disciplina
    aluno_matriculado = {
        "id": aluno.id,
        "nome": aluno.nome,
        "disciplinas_matriculadas": [*aluno.disciplinas_matriculadas, oferta.disciplina],
        "disciplinas_requisitadas": list(filter(remover_disciplina, aluno.disciplinas_requisitadas))
    }
    return Aluno(aluno_matriculado), Oferta(oferta_com_aluno_matriculado_info)
