/**
 * Este script é carregado em todas as páginas do seu site MkDocs.
 * Ele é responsável por inicializar os efeitos visuais dinâmicos.
 */

// Executa o script apenas quando o conteúdo da página estiver totalmente carregado.
document.addEventListener('DOMContentLoaded', () => {

    /**
     * Função para criar e animar as partículas de fundo.
     * Ela adiciona dinamicamente elementos 'div' a um container
     * e os anima usando CSS.
     */
    function createParticles() {
        // O container precisa existir no seu HTML. Verifique as instruções abaixo.
        const particlesContainer = document.getElementById('particles-container');
        if (!particlesContainer) {
            // Se o container não for encontrado, a função não faz nada.
            // Isso evita erros em páginas que talvez não tenham o efeito.
            return;
        }

        const particleCount = 25; // Número de partículas na tela

        for (let i = 0; i < particleCount; i++) {
            const particle = document.createElement('div');
            particle.classList.add('particle');

            // Posições, tamanhos e tempos de animação aleatórios para um efeito orgânico
            const posX = Math.random() * 100;
            const posY = Math.random() * 100;
            const size = Math.random() * 3 + 1; // Tamanho entre 1px e 4px
            const delay = Math.random() * 10;   // Atraso de até 10s
            const duration = Math.random() * 10 + 15; // Duração entre 15s e 25s

            particle.style.left = `${posX}%`;
            particle.style.top = `${posY}%`;
            particle.style.width = `${size}px`;
            particle.style.height = `${size}px`;
            particle.style.animationDelay = `${delay}s`;
            particle.style.animationDuration = `${duration}s`;

            particlesContainer.appendChild(particle);
        }
    }

    /**
     * Função para revelar elementos gradualmente conforme o usuário rola a página.
     * Utiliza a API IntersectionObserver para performance e eficiência.
     */
    function setupRevealAnimations() {
        const revealElements = document.querySelectorAll('.reveal');
        if (revealElements.length === 0) return;

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                // Quando o elemento está visível na tela
                if (entry.isIntersecting) {
                    // Adiciona a classe 'visible' para ativar a animação CSS
                    entry.target.classList.add('visible');
                    // Opcional: Para de observar o elemento para não animar novamente
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1 // A animação começa quando 10% do elemento está visível
        });

        revealElements.forEach(element => {
            observer.observe(element);
        });
    }

    // --- INICIALIZAÇÃO DAS FUNÇÕES ---
    createParticles();
    setupRevealAnimations();

});