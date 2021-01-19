from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# on crée l'application
app = Flask(__name__)

# activation des CORS sur l'app
CORS(app)


# on déclare la structure de donnée (liste) qui gère les todo
todolist = []


############# ON DEFINIT LES "ROUTES" DE L'API ###############

# POST /todo : Crée un nouveau todo 
@app.route('/todo', methods=['POST'])
def creer():
    # 1 - on recupère les données du body
    todo = request.get_json()
    # 2 - on ajoute le todo à la liste
    todolist.append(todo)
    # 3 - on retourne le todo au format json
    return jsonify(todo)
    
    
# GET /todo : Liste les todos 
@app.route('/todo', methods=['GET'])
def lister():
    # 1 - on retourne la liste des todo au format json
    return jsonify(todolist)


# DELETE /todo/id : Supprime le todo situé à l'index id 
@app.route('/todo/<int:id>', methods=['DELETE'])
def supprimer(id):
     # 1 - on supprime le todo situé à l'index id
     del todolist[id] # syntaxe équivalente : todolist.pop(id)
     
     # 2 - on retourne la liste entière des todo au format json
     return jsonify(todolist)