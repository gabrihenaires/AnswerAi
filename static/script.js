document.addEventListener("DOMContentLoaded", function() {
    // Esconde o formulário quando há perguntas
    if (document.querySelector("pre")) {
        document.getElementById("qa-form").style.display = "none";
    }

    // Mostrar o ícone de carregamento ao enviar o formulário e esconder o botão
    const form = document.getElementById("qa-form");
    if (form) {
        form.addEventListener("submit", function() {
            document.getElementById("generate-btn").style.display = "none"; 
            document.getElementById("loading1").style.display = "block"; // Alterar para o ID único
        });
    }

    // Para o segundo formulário
    const form2 = document.getElementById("qa-form2");
    if (form2) {
        form2.addEventListener("submit", function() {
            document.getElementById("gerar-btn").style.display = "none"; 
            document.getElementById("loading2").style.display = "block"; // Alterar para o ID único
        });
    }
});
