
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return "<h1>APP automática Flask</h1><p>Sin configuración manual del environment.</p>"

if __name__ == '__main__':
	app.run()

