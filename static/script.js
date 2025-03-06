document.addEventListener("DOMContentLoaded", function() {
    // Esconde o formulário quando há perguntas
    if (document.querySelector("pre")) {
        document.getElementById("qa-form").style.display = "none";
    }

    // Mostrar o ícone de carregamento ao enviar o formulário e esconder o botão
    const form = document.getElementById("qa-form");
    if (form) {
        form.addEventListener("submit", function(event) {
            // Exibe o ícone de carregamento e esconde o botão
            document.getElementById("generate-btn").style.display = "none"; 
            document.getElementById("loading1").style.display = "block"; // Alterar para o ID único

            // Agora evita o envio imediato para garantir que a animação de carregamento seja exibida
            event.preventDefault();
            
            // Submete o formulário após um pequeno delay para garantir que o ícone de carregamento tenha tempo de aparecer
            setTimeout(() => {
                form.submit();
            }, 300); // Ajuste o delay conforme necessário
        });
    }

    // Para o segundo formulário
    const form2 = document.getElementById("qa-form2");
    if (form2) {
        form2.addEventListener("submit", function(event) {
            // Exibe o ícone de carregamento e esconde o botão
            document.getElementById("gerar-btn").style.display = "none"; 
            document.getElementById("loading2").style.display = "block"; // Alterar para o ID único

            // Agora evita o envio imediato para garantir que a animação de carregamento seja exibida
            event.preventDefault();
            
            // Submete o formulário após um pequeno delay para garantir que o ícone de carregamento tenha tempo de aparecer
            setTimeout(() => {
                form2.submit();
            }, 300); // Ajuste o delay conforme necessário
        });
    }
});

function autoResize(textarea) {
    // Reseta a altura para auto, para que ela seja ajustada dinamicamente
    textarea.style.height = 'auto';
    
    // Ajusta a altura para a altura do conteúdo
    textarea.style.height = (textarea.scrollHeight) + 'px';
}

// Seleciona todos os textareas com a classe .topic
document.querySelectorAll('.topic').forEach(textarea => {
    textarea.addEventListener('keydown', function(event) {
        const form = this.closest('form'); // Encontra o formulário correto para cada textarea

        // Se o usuário pressionar Enter (sem Shift ou Ctrl), envia o formulário
        if (event.key === 'Enter' && !event.ctrlKey && !event.shiftKey) {
            event.preventDefault(); // Impede o comportamento padrão de enviar com Enter

            // Verifica qual formulário está sendo submetido e exibe o ícone correto
            if (form.id === "qa-form") {
                document.getElementById("generate-btn").style.display = "none"; 
                document.getElementById("loading1").style.display = "block"; 
            } else if (form.id === "qa-form2") {
                document.getElementById("gerar-btn").style.display = "none"; 
                document.getElementById("loading2").style.display = "block";
            }

            // Submete o formulário após um pequeno delay para garantir que o ícone de carregamento tenha tempo de aparecer
            setTimeout(() => {
                form.submit();
            }, 300); // Ajuste o delay conforme necessário
        }

        // Se o usuário pressionar Ctrl + Enter ou Shift + Enter, adiciona uma quebra de linha
        if ((event.key === 'Enter' && event.ctrlKey) || (event.key === 'Enter' && event.shiftKey)) {
            event.preventDefault(); // Impede o envio
            this.value += '\n'; // Adiciona uma quebra de linha
        }
    });
});
