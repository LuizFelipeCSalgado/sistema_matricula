from use_cases import matricula
from infrastructure import daos, connection

def aprovar_matricula(oferta_id: int, aluno_id: int) -> bool:
    conn= connection.get_connection()

    oferta_dao = daos.OfertaDAO(conn)
    aluno_dao = daos.AlunoDAO(conn)

    oferta = oferta_dao.get_oferta(oferta_id)
    aluno = aluno_dao.get_aluno(aluno_id)

    oferta_atualizada, aluno_atualizado = matricula.aprovar_matricula(oferta, aluno)

    oferta.atualizar_oferta(oferta_atualizada)
    aluno.atualizar_aluno(ofeta_atualizado)

    return True

def requerer_matricula(oferta_id: int, aluno_id: int) -> bool:
    conn= connection.get_connection()

    oferta_dao = daos.OfertaDAO(conn)
    aluno_dao = daos.AlunoDAO(conn)

    oferta = oferta_dao.get_oferta(oferta_id)
    aluno = aluno_dao.get_aluno(aluno_id)

    oferta_atualizada, aluno_atualizado = matricula.requerer_matricula(oferta, aluno)

    oferta.atualizar_oferta(oferta_atualizada)
    aluno.atualizar_aluno(ofeta_atualizado)

    return True

def get_situacao_requisicao_matricula(oferta_id: int, aluno_id) -> str:
    conn= connection.get_connection()

    oferta_dao = daos.OfertaDAO(conn)
    aluno_dao = daos.AlunoDAO(conn)

    oferta = oferta_dao.get_oferta(oferta_id)
    aluno = aluno_dao.get_aluno(aluno_id)

    situacao_matricula = matricula.verificar_situacao(oferta, aluno)

    return situacao_matricula
