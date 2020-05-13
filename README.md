# sistema\_matricula
POC sistema de matrículas usando Clean Architecture


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
## Service
## Controller

Poderia ser implementado em um próximo passo uma camada de *service*, reponsável por chamar
os *use cases*, diminuindo o acoplamento entre o *controller* e *use cases*.


- pip install -r requirements.txt
- setar PYTHONPATH com o presente diretório.
  set PYTHONPATH=$PYTHONPATH:$(pwd)
