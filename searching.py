import requests

class Searching:
    """docstring for searching"""
    def __init__(self):
        self.api_end_point = 'https://www.wikidata.org/w/api.php'
    
    """função para retornar dados acerca de uma entidade automaticamente"""
    """entrada: uma string"""
    """saida: um dicionario (formato json)"""
    
    def getEntitie(self, query):
        consultas = self.pagesEntitie(query)
        # primeiro resultado
        id = consultas[0]['id']
        site = consultas[0]['concepturi']
        return self.wbGetEntitie(id, site)
    
    """função para retornar paginas de entidades correspondentes a pesquisa, funcao wbseachentities"""
    """entrada: uma string"""
    """saida: uma lista de dicionarios (formato json)"""
    def pagesEntitie(self, query):
        parameters = {
            'action' : 'wbsearchentities',
            'format' : 'json',
            'language' : 'pt-br',
            'search' : query}
        return self.request(parameters).json()['search']

    
    """funcao para retornar dados acerca de uma entidade, funcao wbgetentities"""
    """entrada: id, site"""
    def wbGetEntitie(self, id, site):
        parameters = {
            'action': 'wbgetentities',
            'format': 'json',
            'language': 'pt-br',
            'sites': site,
            'titles': id,
            'ids': id}
        return self.request(parameters).json()['entities']
      
    """funcao para realizar a requisicao na api"""
    """entrada: lista de parametros"""
    """saida: uma lista de dicionario com as informacoes da entidade (formato json)"""
    def request(self, parameters):
        try:
            return requests.get(self.api_end_point, params = parameters)
            pass
        except Exception as e:
            return []