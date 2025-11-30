function pingServer() {
fetch("/")
    .then(r => r.text())
    .then(() => document.getElementById("result").innerHTML = "Serveur OK ✔")
    .catch(() => document.getElementById("result").innerHTML = "Erreur ❌");
}
