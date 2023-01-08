

# Tablas in memory con los usuarios logados. Simulamos un DB
# Otras dos tablas extra para facilitar el acceso a los datos de cada usuario
# Esto se hace para no iterar
users = [
    {
        'id': 1,
        'username': 'bob',
        'password': 'asdf'
    }
]

username_mapping = {'bob': {
    'id': 1,
    'username': 'bob',
    'password': 'asdf'
}}

userid_napping = {1: {
   'id': 1,
   'username': 'bob',
   'password': 'asdf'
}}

def authenticate(username, password):
    user = username_mapping.get(username, None)