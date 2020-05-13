import connection

def escrever_objeto_aluno(aluno_raw: dict) -> Aluno:
    return Aluno()

class AlunoDAO:
    def __init__(self):
        self.cursor = connection.get_cursor()

    def get_all(self):
        query = 'SELECT * FROM alunos'
        self.cursor.execute(query)
        query_result = cursor.fetchall()
        import pdb; pdb.set_trace()
        return map(escrever_objeto_aluno, query_result)
