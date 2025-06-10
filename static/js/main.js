document.getElementById('submitBtn').addEventListener('click', function() {
    const repoName = {{ repo_name|tojson }};
    const issueUrl = {{ issue_url|tojson }};

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            repo_name: repoName,
            issue_url: issueUrl
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        document.getElementById('output').textContent = JSON.stringify(data, null, 2);
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('output').textContent = 'Error al enviar datos al backend.';
    });
});
