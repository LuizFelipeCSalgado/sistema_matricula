from use_cases import matricula
from infrastructure import daos, connection

def aprovar_matricula(oferta_id: int, aluno_id: int) -> bool:
    connection = connection.get_connection()

    oferta_dao = daos.OfertaDAO(connection)
    aluno_dao = daos.AlunoDAO(connection)

    oferta = oferta_dao.get_oferta(oferta_id)
    aluno = aluno_dao.get_aluno(aluno_id)

    oferta_atualizado, aluno_atualizado = matricula.aprovar_matricula(oferta, aluno)

    oferta.atualizar_oferta(oferta_atualizado)
    aluno.atualizar_aluno(ofeta_atualizado)

    return True
