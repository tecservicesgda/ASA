import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Ruta para la página principal
@app.route('/')
def home():
    # URL de la API de GitHub para obtener información del repositorio
    repo_url = "https://api.github.com/repos/SWE-agent/test-repo"
    issue_url = "https://api.github.com/repos/SWE-agent/test-repo/issues/1"

    # Obtener información del repositorio
    repo_response = requests.get(repo_url)
    repo_data = repo_response.json()

    # Obtener información del issue
    issue_response = requests.get(issue_url)
    issue_data = issue_response.json()

    # Extraer los datos necesarios
    repo_name = repo_data['name']  # Nombre del repositorio
    issue_url = issue_data['html_url']  # URL del issue

    # Pasar esos datos al template
    return render_template('index.html', repo_name=repo_name, issue_url=issue_url)

# Ruta para manejar el envío al backend
@app.route('/submit', methods=['POST'])
def submit():

    return jsonify({'status': 'success', 'message': 'Data received'})

if __name__ == '__main__':
    app.run(debug=True)
