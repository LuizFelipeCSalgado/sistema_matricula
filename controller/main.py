from flask import Flask, request, Response
import json

from services import matricula

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/alunos/<string>/matriculas/pendentes/<int:id>', methods=['PUT'])
def aprovar_matricula():
    try:
        aluno_id = request.args.get('aluno_id')
        oferta_id = request.args.get('oferta_id')

        requisicao_feita = matricula.aprovar_matricula(oferta_id, aluno_id)
        if requisicao_feita:
            return Response(status=202)
        return Response(status=500)
    except Exception as e:
        print(e)
        return Response(status=500)
