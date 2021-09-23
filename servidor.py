import grpc
from concurrent import futures
import time
import search_pb2_grpc as pb2_grpc
import search_pb2 as pb2
import json

#tambien muere si no existe, creo

class SearchService(pb2_grpc.SearchServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        resultados = []
        largo = len(request.message )
    
        with open('productos.json') as products:
            productos = json.load(products)

        for p in productos["product"]:
            if( p["name"].find(request.message) != -1):
                resultados.append(p)
        search_proto = {'product':resultados} 

        return pb2.SearchResults(**search_proto)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pb2_grpc.add_SearchServicer_to_server(SearchService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
