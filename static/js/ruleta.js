let tickets = 3;

    function spin() {
        if (tickets > 0) {
            const cells = document.querySelectorAll('.ruleta-cell');
            const options = [
                '25% de descuento', 
                'Game Over', 
                '50% de descuento', 
                'Game Over', 
                'Game Over', 
                '75% de descuento', 
                'Game Over', 
                '100% de descuento'
            ];
            const randomIndex = Math.floor(Math.random() * options.length);
            const result = options[randomIndex];

            let currentIndex = 0;
            const totalCells = cells.length;
            let spins = 0;
            const maxSpins = 24;
            const interval = setInterval(() => {
                cells.forEach(cell => cell.classList.remove('ruleta-highlight'));
                cells[currentIndex].classList.add('ruleta-highlight');
                currentIndex = (currentIndex + 1) % totalCells;
                spins++;
                if (spins > maxSpins && currentIndex === randomIndex) {
                    clearInterval(interval);
                    setTimeout(() => {
                        alert(result === 'Game Over' ? 'Lo siento, no ganaste nada esta vez.' : `¡Felicidades! Ganaste un ${result}.`);
                        tickets--;
                        document.getElementById('ruleta-tickets').textContent = tickets;
                    }, 500);
                }
            }, 100);

        } else {
            alert('No tienes más tickets para jugar.');
        }
    }