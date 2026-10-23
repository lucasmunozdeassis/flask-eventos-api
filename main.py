from flask import Flask, jsonify, abort, make_response, request, json   
import json
from evento import Evento
from eventoonline import EventoOnline


app = Flask(__name__)

evento = Evento("Python & Flask Masterclass", "Auditório Central - São Paulo", "presencial", 50)
eventodois = Evento("Workshop de Git, GitHub e Boas Práticas", "Laboratório de Informática - Bloco B", "presencial", 30)
evento_online = EventoOnline.criar_evento_online("Arquitetura de Microsserviços com Django e FastAPI")
evento_online_dois = EventoOnline.criar_evento_online("Encontro de Desenvolvedores Backend Júnior")
eventos = [evento, eventodois, evento_online, evento_online_dois]

@app.route("/")
def index():
    index1 = [{
        "status": "online",
        "projeto": "API de Gestão de Eventos",
        "total_eventos": len(eventos),
        "listar_eventos": "/api/eventos",
        "detalhar_evento": "/api/eventos/<id>"
    }]
    return jsonify(index1)

    
@app.errorhandler(404)
def nao_encontrado(erro):
    return make_response(jsonify(erro=str(erro)), 404)

@app.route("/api/eventos")
def listar_eventos():
    eventos_dict = []
    for evento in eventos:
        eventos_dict.append(evento.__dict__)
    return jsonify(eventos_dict)



@app.route("/api/eventos", methods=["POST"])
def criar_evento():
#PARCING
    data = json.loads(request.data)
    nome = data.get("nome")
    local = data.get("local")

#VALIDAÇÃO
    if not nome:
        return abort(jsonify({"error": "'nome' do evento é obrigatório"}), 400)

#CRIANDO EVENTO
    if local:
        evento = Evento(nome=nome, local=local)
    else:
        evento = EventoOnline.criar_evento_online(nome=nome)
    eventos.append(evento)
    return {

"message": "Evento criado com sucesso",
        "id": evento.id,
        "url": f"/api/eventos/{evento.id}/"
    }

def get_evento_or_404(id):
    for evento in eventos:
        if evento.id == id:
            return evento
    abort(404, "o evento não foi encontrado na lista de eventos")


@app.route("/api/eventos/<int:id>/")
def detalhar_evento(id):
    evento = get_evento_or_404(id)
    return jsonify(evento.__dict__)
    
@app.route("/api/eventos/<int:id>/", methods=["DELETE"])
def deletar_evento(id):
    evento = get_evento_or_404(id)
    eventos.remove(evento)
    return jsonify(id=id, message="Evento deletado com sucesso")

@app.route("/api/eventos/<int:id>/", methods=["PUT"])
def atualizar_evento(id):
    data = request.get_json()
    nome = data.get("nome")
    local = data.get("local")

    evento = get_evento_or_404(id)

    if not nome or not local:
        return abort(jsonify({"erro": "Os campos 'nome' e 'local' são obrigatórios"}), 400)

    evento.nome = nome
    evento.local = local

    return jsonify(evento.__dict__)

    

@app.route("/api/eventos/<int:id>/", methods=["PATCH"])
def atualizar_parcial_evento(id):
    data = request.get_json()
    nome = data.get("nome")
    local = data.get("local")

    evento = get_evento_or_404(id)

    if nome:
        evento.nome = nome
    if local:
        evento.local = local

    if not nome and not local:
        return abort(jsonify({"error": "Nenhum dado para atualizar"}), 400)

    return jsonify(evento.__dict__)