# sistema\_matricula
POC sistema de matrículas usando Clean Architecture

Banco de dados utilizado: MySQL\*
Linguagem: Python - versão 3.6.9
Dependências escritas no requirements.txt (pip install -r requirements.txt)

\* Para desenvovimento foi utilizado Docker. Comando para rodar a imagem está
no repositório


Para o sistema foi projetado que tenha as seguintes camadas e padrões:
- Entity
- Use Cases
- DAO
- Service
- Controller -> API RESTful

## Entity
Contém classes que encapsulam dados que são expostos segundo **as regras
de negócio da empresa**.

## Use Cases
Contém funções (puras) que utilizam as regras de negócio. São responsáveis
por conter as regras de negócio da aplicação.
1) Criar um pedido de matrícula
2) Deferir um pedido de matrícula
3) Verificar se um pedido de matrícula foi aprovado

## DAO
Contém objetos reponsáveis pela comunicação com banco de dados (no caso do projeto
MySQL). Realizam as operações simples de leitura e escrita no BD.

## Service
Contém funcões que chamam a camada responsável por prover os dados lidos de um
banco de dados e os usa nos use cases.

## Controller

Poderia ser implementado em um próximo passo uma camada de *service*, reponsável por chamar
os *use cases*, diminuindo o acoplamento entre o *controller* e *use cases*.


- pip install -r requirements.txt
- setar PYTHONPATH com o presente diretório (para rodar testes unitários)
  set PYTHONPATH=$PYTHONPATH:$(pwd)
- rodar ./run-container (bash) para criar e roda a imagem MySQL
- rodar script create\_table.sql para criar a base de dados e as tabelas\*

\* pode ser feito de várias maneiras. Caso haja alguma dificuldade, utilize o
MySQL workbench [https://www.mysql.com/products/workbench/]
