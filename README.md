# sistema_matricula
POC sistema de matrículas usando Clean Architecture


Para o sistema foi projetado que tenha as seguintes camadas e padrões:
- Entity
- Use Cases
- DAO
- Controller -> API RESTful

Poderia ser implementado em um próximo passo uma camada de *service*, reponsável por chamar
os *use cases*, diminuindo o acoplamento entre o *controller* e *use cases*.
