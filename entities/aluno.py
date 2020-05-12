class Aluno:
    def __init__(self, aluno_info: dict):
        """
            aluno_info = {
                "id": int,
                "nome": str,
                "curso": str,
                "disciplinas_matriculadas": list(str),
                "disciplinas_requisitadas": list(str)
            }
        """
        self.id = aluno_info.get('id', 'N/A')
        self.nome = aluno_info.get('nome', 'N/A')
        self.curso = aluno_info.get('curso', 'N/A')
        self.disciplinas_matriculadas = aluno_info.get('disciplinas_matriculadas', 'N/A')
        self.disciplinas_requisitadas = aluno_info.get('disciplinas_requisitadas', 'N/A')
