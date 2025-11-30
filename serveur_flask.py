# serveur_flask.py
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>Mini Serveur Flask</title>
<style>
body { font-family: Arial; background: #f0f0f0; padding: 20px; }
h1 { color: #2c66d6; }
</style>
</head>
<body>
<h1>Mini Serveur Flask Fonctionne 🚀</h1>
<p>Bienvenue Yanis ! Ton serveur tourne parfaitement.</p>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
