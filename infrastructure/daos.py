from entities.aluno import Aluno
from entities.oferta import Oferta

def escrever_objeto_aluno(aluno_raw: tuple) -> Aluno:
    return Aluno({
        'id': aluno_raw[0],
        'nome': aluno_raw[1],
        'curso': aluno_raw[2],
        'disciplinas_matriculadas': aluno_raw[3].split(','),
        'disciplinas_requisitadas': aluno_raw[4].split(',')
    })

def escrever_objeto_oferta(oferta_raw: tuple) -> Oferta:
    return Oferta({
        'id': oferta_raw[0],
        'disciplina': oferta_raw[1],
        'alunos_matriculados': oferta_raw[2],
        'alunos_pendentes': oferta_raw[3],
        'max_alunos': oferta_raw[4],
    })

class AlunoDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_cursor(self):
        return self.connection.cursor()

    def get_all(self):
        query = 'SELECT * FROM sistema_matriculas.alunos'
        cursor = self.get_cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        return map(escrever_objeto_aluno, query_result)

    def get_aluno(self, id_aluno: int) -> Aluno:
        query = f'''
            SELECT * FROM sistema_matriculas.alunos
            WHERE id = {id_aluno}
        '''
        cursor = self.get_cursor()
        cursor.execute(query)
        query_result = cursor.fetchone()
        print(query_result)
        return escrever_objeto_aluno(query_result)

    def atualizar_aluno(self, aluno: Aluno) -> bool:
        query = f'''
            UPDATE sistema_matriculas.alunos
            SET 
                id = {aluno.id},
                nome = '{aluno.nome}',
                curso = '{aluno.curso}',
                disciplinas_matriculadas = '{",".join(aluno.disciplinas_matriculadas)}',
                disciplinas_requisitadas = '{",".join(aluno.disciplinas_requisitadas)}'
            WHERE
                id = {aluno.id}
        '''
        cursor = self.get_cursor()
        cursor.execute(query)
        cursor.commit()
        return True

    def create(self, aluno: Aluno) -> bool:
        query = f'''
            INSERT INTO sistema_matriculas.alunos (
                nome,
                curso,
                disciplinas_matriculadas,
                disciplinas_requisitadas
            ) VALUES (
                '{aluno.nome}',
                '{aluno.curso}',
                '{",".join(aluno.disciplinas_matriculadas)}',
                '{",".join(aluno.disciplinas_requisitadas)}'
            );
        '''
        self.get_cursor().execute(query)
        self.connection.commit()
        return True

class OfertaDAO:
    def __init__(self, connection):
        self.connection = connection

    def get_cursor(self):
        return self.connection.cursor()

    def get_all(self):
        query = 'SELECT * FROM sistema_matriculas.ofertas'
        cursor = self.get_cursor()
        cursor.execute(query)
        query_result = cursor.fetchall()
        return map(escrever_objeto_oferta, query_result)

    def get_oferta(self, id_oferta: int) -> Oferta:
        query = f'''
            SELECT * FROM sistema_matriculas.ofertas
            WHERE id = {id_oferta}
        '''
        cursor = self.get_cursor()
        cursor.execute(query)
        query_result = cursor.fetchone()
        return escrever_objeto_oferta(query_result)

    def atualizar_oferta(self, oferta: Oferta) -> bool:
        query = f'''
            UPDATE sistema_matriculas.ofertas
            SET 
                disciplina = '{oferta.disciplina}',
                alunos_matriculados = '{",".join(oferta.alunos_matriculados)}',
                alunos_pendentes = '{",".join(oferta.alunos_pendentes)}',
                max_alunos = {oferta.max_alunos}
            WHERE
                id = {oferta.id}
        '''
        cursor = self.get_cursor()
        cursor.execute(query)
        cursor.commit()
        return True

    def create(self, oferta: Oferta) -> bool:
        query = f'''
            INSERT INTO sistema_matriculas.ofertas (
                disciplina,
                alunos_matriculados,
                alunos_pendentes,
                max_alunos
            ) VALUES (
                '{oferta.disciplina}',
                '{",".join(oferta.alunos_matriculados)}',
                '{",".join(oferta.alunos_pendentes)}',
                '{oferta.max_alunos}'
            );
        '''
        self.get_cursor().execute(query)
        self.connection.commit()
        return True
