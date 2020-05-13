from entities.aluno import Aluno
from entities.oferta import Oferta

class MatriculaException(Exception):
    pass

def aprovar_matricula(oferta: Oferta, aluno: Aluno) -> (Oferta, Aluno):
    if len(oferta.alunos_matriculados) >= oferta.max_alunos:
        raise MatriculaException("A oferta não tem mais vagas disponíveis")

    if aluno.esta_matriculado_na_disciplina(oferta.disciplina):
        raise MatriculaException("Aluno já está matriculado na disciplina")

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
    return Oferta(oferta_com_aluno_matriculado_info), Aluno(aluno_matriculado)

def requerer_matricula(oferta: Oferta, aluno: Aluno) -> (Oferta, Aluno):
    if len(oferta.alunos_matriculados) >= oferta.max_alunos:
        raise MatriculaException("A oferta não tem mais vagas disponíveis")

    if aluno.esta_aguardando_aprovacao_na_disciplina(oferta.disciplina):
        raise MatriculaException("Aluno já requeriu matrícula na disciplina")

    oferta_com_aluno_requerente_info = {
        "disciplina": oferta.disciplina,
        "alunos_matriculados": oferta.alunos_matriculados,
        "alunos_pendentes": [*oferta.alunos_pendentes, aluno.id],
        "max_alunos": oferta.max_alunos
    }
    aluno_requerente = {
        "id": aluno.id,
        "nome": aluno.nome,
        "disciplinas_matriculadas": aluno.disciplinas_matriculadas,
        "disciplinas_requisitadas": [*aluno.disciplinas_requisitadas, oferta.disciplina]
    }

    return Oferta(oferta_com_aluno_requerente_info), Aluno(aluno_requerente)

def verificar_situacao(oferta: Oferta, aluno: Aluno) -> str:
    if aluno.esta_matriculado_na_disciplina(oferta.disciplina):
        return "matriculado"
    if aluno.esta_aguardando_aprovacao_na_disciplina(oferta.disciplina):
        return "aguardando-aprovacao"
    return "nao-encontrado"
