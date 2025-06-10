import requests
from flask import Flask, request, jsonify, render_template

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
    repo_name = "TestRepo"  # Nombre del repositorio
    issue_url = issue_data['html_url']  # URL del issue

    # Pasar esos datos al template
    return render_template('index.html', repo_name=repo_name, issue_url=issue_url)

# Ruta para manejar el envío al backend
@app.route('/submit', methods=['POST'])
def submit():
    # Get JSON data sent by client to /submit
    data = request.get_json()

    # URL of the local service running on port 5000
    local_service_url = "http://localhost:5000/run"

    try:
        # Forward the JSON data to the local service /run endpoint
        response = requests.post(local_service_url, json=data)
        response.raise_for_status()  # check for errors
    except requests.exceptions.RequestException as e:
        return jsonify({'status': 'error', 'message': f"Error calling local service: {str(e)}"}), 500

    # Optionally, you can return the local service response content back to the client
    return jsonify({
        'status': 'success',
        'message': 'Data sent to local service',
        'local_service_response': response.json()  # assuming it returns JSON
    })

if __name__ == '__main__':
    app.run(debug=True, port=3000)
