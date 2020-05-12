class Oferta:
    def __init__(self, oferta_info: dict):
        """
            oferta_info = {
                "disciplina": str,
                "alunos_matriculados": list(int),
                "alunos_pendentes": list(int),
                "max_alunos": int
            }
        """
        self.disciplina = oferta_info.get('disciplina', 'N/A') 
        self.alunos_matriculados = oferta_info.get('alunos_matriculados', 'N/A') 
        self.alunos_pendentes = oferta_info.get('alunos_pendentes', 'N/A') 
        self.max_alunos = oferta_info.get('max_alunos', 'N/A') 
