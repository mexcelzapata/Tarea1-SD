import flask
import grpc
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import redis
import json
from google.protobuf.json_format import MessageToJson
from flask import request, jsonify

#pasos:
    #1-recivir la palabra por el cliente                                             ----------------------    #listo!
    #2-pasarla por el cache                                                          ----------------------    #listo!
        #--(si lo encuentra:)                                                        ----------------------    #listo!
            #enviarlo                                                                ----------------------    #listo!
        #--(si no lo encuentra:)                                                     ----------------------    #listo!
            #pasarlo al servidor donde debe buscar en la base de datos (archivo)     ----------------------    #listo!
                #si lo encuentra enviarlo al cliente                                 ----------------------    #listo!
                    #guardarlo en el cache                                           ----------------------    #listo!
                #si no, enviar un codigo de error o algo!                         

app = flask.Flask(__name__)
app.config["DEBUG"] = True

class SearchClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port)) 
        self.stub = pb2_grpc.SearchStub(self.channel)

    def get_results(self, message):
        message = pb2.Message(message=message)
        print(f'{message}')
        return self.stub.GetServerResponse(message)

@app.route('/')
def index():
    return "Ruta de prueba"

@app.route('/inventory/search', methods = ['GET'])
def buscador():
    if 'q' in request.args:
        buscador= request.args['q']
        r= redis.Redis(host='localhost', port=6379, db=0)
        resultado = r.get(buscador)

        if(resultado==None):
            client = SearchClient()
            result = client.get_results(buscador)
            serialized = MessageToJson(result)
            r.set(buscador, serialized)
            return serialized
        else:
            products= json.loads(resultado)
            return jsonify(products)
    else:
        return "Error de URL"

app.run(host='127.0.0.1', port=3000) #localhost:3000