document.addEventListener('DOMContentLoaded', function () {
    const button = document.querySelector('button');
    const neonText = document.querySelector('.neon-text');

    button.addEventListener('click', function () {
        neonText.style.color = getRandomColor();
    });

    function getRandomColor() {
        const colors = ['#ff00ff', '#7f00ff', '#00ffff', '#ff6600'];
        return colors[Math.floor(Math.random() * colors.length)];
    }
});

