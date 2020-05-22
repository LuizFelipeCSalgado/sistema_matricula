#!python

from connection import get_cursor

CREATE_DATABASE_QUERY = """
    CREATE DATABASE sistema_matriculas;
"""

CREATE_TABLES_QUERY = """
    CREATE TABLE sistema_matriculas.alunos (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(30) NOT NULL,
        curso VARCHAR(30) NOT NULL,
        disciplinas_matriculadas VARCHAR(240) NOT NULL,
        disciplinas_requisitadas VARCHAR(240) NOT NULL
    );
    CREATE TABLE sistema_matriculas.ofertas (
            id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        alunos_matriculados VARCHAR(240) NOT NULL,
        alunos_pendentes VARCHAR(240) NOT NULL,
        max_alunos INT(2) NOT NULL
    );
"""

cursor = get_cursor()

cursor.execute(CREATE_DATABASE_QUERY)
cursor.commit()

cursor.execute(CREATE_TABLES_QUERY)
cursor.commit()
