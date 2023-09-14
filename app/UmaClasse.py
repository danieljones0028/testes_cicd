"""MIMIMIMI"""

import urllib3


class PerguntaLa():
    
    def __init__(self) -> None:
        pass
    
    def nosite(self, fqdn, on_ssl=None):
        
        # Aquela jumbada basica rsrsrsrs
        if on_ssl == None:
            method = 'https'
        else:
            method = 'http'
            
        
        try:
            http = urllib3.PoolManager()
            
            resp = http.request("GET", f"{method}://{fqdn}")
            
            if resp.status == 200:
                print('Deu bom')
        except Exception as erro_nosite:
            print(f'Deu ruim no site: {fqdn}')
            print(resp.status)
