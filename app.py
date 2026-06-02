from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Una pequeña sorpresa</title>

<style>
body{
    margin:0;
    font-family:Arial, sans-serif;
    background:linear-gradient(135deg,#ff9a9e,#fad0c4);
    display:flex;
    justify-content:center;
    align-items:center;
    min-height:100vh;
    overflow:auto;
}

.carta{
    background:white;
    width:700px;
    max-width:90%;
    padding:40px;
    border-radius:25px;
    text-align:center;
    box-shadow:0 0 25px rgba(0,0,0,0.2);
    margin:30px;
}

h1{ color:#ff4f81; }

p{
    font-size:20px;
    line-height:1.5;
}

button{
    border:none;
    padding:12px 25px;
    border-radius:12px;
    cursor:pointer;
    font-size:18px;
    margin-top:20px;
}

.abrir{ background:#ff4f81; color:white; }

.si{ background:#4CAF50; color:white; }

.no{
    background:#f44336;
    color:white;
    position:absolute;
}

.final{ animation:aparecer 1.5s ease; }

.galeria{
    display:flex;
    flex-wrap:wrap;
    justify-content:center;
    gap:15px;
    margin-top:25px;
}

.galeria img{
    width:180px;
    height:180px;
    object-fit:cover;
    border-radius:15px;
    box-shadow:0 0 10px rgba(0,0,0,0.25);
    transition:0.3s;
}

.galeria img:hover{ transform:scale(1.08); }

@keyframes aparecer{
    from{ opacity:0; transform:scale(0.5); }
    to{ opacity:1; transform:scale(1); }
}

.corazon{
    position:fixed;
    font-size:25px;
    animation:flotar 6s linear infinite;
    pointer-events:none;
}

@keyframes flotar{
    from{ transform:translateY(100vh); opacity:1; }
    to{ transform:translateY(-120vh); opacity:0; }
}
</style>
</head>

<body>

<div class="carta">

    <h1>✉️ Carta Digital ✉️</h1>

    <p id="texto">Tengo una pequeña sorpresa para ti...</p>

    <button class="abrir" onclick="iniciar()">Abrir carta</button>

    <div id="botones"></div>

</div>

<script>
function iniciar(){
    let mensajes = [
        "Hola Johan 😊",
        "Tengo algo que quiero mostrarte...",
        "No es exactamente un secreto 🤔",
        "Porque en realidad ya lo sabes...",
        "Pero quería demostrártelo de una manera diferente ❤️",
        "¿Quieres verlo?"
    ];

    let indice = 0;
    document.querySelector(".abrir").style.display = "none";

    let intervalo = setInterval(() => {
        document.getElementById("texto").innerHTML = mensajes[indice];
        indice++;

        if(indice >= mensajes.length){
            clearInterval(intervalo);

            document.getElementById("botones").innerHTML = `
                <button class="si" onclick="mostrarFinal()">Sí</button>
                <button class="no" id="no">No</button>
            `;

            activarBotonNo();
        }
    }, 1800);
}

function activarBotonNo(){
    let boton = document.getElementById("no");

    boton.addEventListener("mouseover", () => {
        let x = Math.random() * (window.innerWidth - 120);
        let y = Math.random() * (window.innerHeight - 80);

        boton.style.left = x + "px";
        boton.style.top = y + "px";
    });
}

function mostrarFinal(){
    document.body.innerHTML = `
    <div class="carta final">

        <h1 style="font-size:55px;">
            ❤️ ME GUSTAS, JOHAN ❤️
        </h1>

        <p>Ya sé que esto no es algo nuevo para ti.</p>
        <p>Pero llevo un tiempo pensando en cómo demostrártelo.</p>
        <p>Decidí crear esta página para recordártelo.</p>
        <p>Porque algunas personas merecen algo más que un simple "me gustas". ❤️</p>

        <h2>📸 Algunos recuerdos 📸</h2>

        <div class="galeria">

            <img src="/static/foto1.jpeg">
            <img src="/static/foto2.jpeg">
            <img src="/static/foto3.jpeg">
            <img src="/static/foto4.jpeg">
            <img src="/static/foto5.jpeg">
            <img src="/static/foto6.jpeg">
            <img src="/static/foto7.jpeg">
            <img src="/static/foto8.jpeg">

        </div>

    </div>
    `;

    crearCorazones();
}

function crearCorazones(){
    setInterval(() => {
        let corazon = document.createElement("div");
        corazon.classList.add("corazon");
        corazon.innerHTML = "❤️";

        corazon.style.left = Math.random() * window.innerWidth + "px";

        document.body.appendChild(corazon);

        setTimeout(() => corazon.remove(), 6000);
    }, 250);
}
</script>

</body>
</html>
"""

@app.route("/")
def inicio():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)