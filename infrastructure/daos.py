from entities.aluno import Aluno

def escrever_objeto_aluno(aluno_raw: dict) -> Aluno:
    return Aluno()

class AlunoDAO:
    def __init__(self, cursor):
        self.cursor = cursor

    def get_all(self):
        query = 'SELECT * FROM alunos'
        self.cursor.execute(query)
        query_result = cursor.fetchall()
        import pdb; pdb.set_trace()
        return map(escrever_objeto_aluno, query_result)

    def create(self, aluno: Aluno) -> bool:
        query = f"""
            INSERT INTO sistema_matriculas.alunos (
                nome,
                curso,
                disciplinas_matriculadas,
                disciplinas_requisitadas
            ) VALUES (
                '{aluno.nome}',
                '{aluno.curso}',
                '{aluno.disciplinas_matriculadas}',
                '{aluno.disciplinas_requisitadas}'
            );
        """
        self.cursor.execute(query)
        return True

    def get_aluno(id: int) -> Aluno:
        pass
