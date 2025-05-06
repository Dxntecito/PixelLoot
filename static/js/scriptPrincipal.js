document.addEventListener('DOMContentLoaded', function() {
    function initFirstSlider() {
        const slider = document.querySelector('.p-oferta-wrapper');
        const prevButton = document.querySelector('.p-oferta-prev');
        const nextButton = document.querySelector('.p-oferta-next');
        let currentIndex = 0;
        const slides = document.querySelectorAll('.p-oferta-slide');

        function updateSliderPosition() {
            const slideWidth = slides[0].clientWidth;
            slider.style.transform = `translateX(-${slideWidth * currentIndex}px)`;
        }

        nextButton.addEventListener('click', function() {
            if (currentIndex < slides.length - 1) {
                currentIndex++;
            } else {
                currentIndex = 0; // Vuelve al inicio si llega al final
            }
            updateSliderPosition();
        });

        prevButton.addEventListener('click', function() {
            if (currentIndex > 0) {
                currentIndex--;
            } else {
                currentIndex = slides.length - 1; // Va al final si está en el inicio
            }
            updateSliderPosition();
        });

        // Avanza automáticamente cada 5 segundos
        setInterval(function() {
            if (currentIndex < slides.length - 1) {
                currentIndex++;
            } else {
                currentIndex = 0;
            }
            updateSliderPosition();
        }, 5000); // Cambia a cada 5 segundos

        // Asegurar que el slider se ajuste al cambiar el tamaño de la ventana
        window.addEventListener('resize', updateSliderPosition);

        updateSliderPosition(); // Ajuste inicial
    }

    function initOfertaSlider() {
        const ofertasWrapper = document.querySelector('.p-oferta-wrapper2');
        const ofertas = document.querySelectorAll('.p-oferta-slide2');
        const prevBtn = document.querySelector('.p-oferta-prev2');
        const nextBtn = document.querySelector('.p-oferta-next2');

        let currentIndex = 0;

        function updateOfertaPosition() {
            const containerWidth = ofertasWrapper.clientWidth;
            const itemsToShow = window.innerWidth < 768 ? 1 : 3; // Cambiar la cantidad de elementos a mostrar según el ancho de la ventana
            const itemWidth = containerWidth / itemsToShow;
            const offset = itemWidth * currentIndex;
            ofertasWrapper.style.transform = `translateX(-${offset}px)`;
        }

        function showOferta(index) {
            const itemsToShow = window.innerWidth < 768 ? 1 : 3;
            const maxIndex = ofertas.length - itemsToShow;
            if (index > maxIndex) {
                currentIndex = 0; // Volver al principio si llega al final
            } else if (index < 0) {
                currentIndex = maxIndex; // Ir al final si está en el principio
            } else {
                currentIndex = index;
            }
            updateOfertaPosition();
        }

        prevBtn.addEventListener('click', () => {
            showOferta(currentIndex - 1); // Avanza de uno en uno hacia atrás
        });

        nextBtn.addEventListener('click', () => {
            showOferta(currentIndex + 1); // Avanza de uno en uno hacia adelante
        });

        // Ajuste inicial
        showOferta(currentIndex);

        // Ajustar al cambiar el tamaño de la ventana
        window.addEventListener('resize', updateOfertaPosition);
    }

    // Inicializar ambos sliders
    initFirstSlider();
    initOfertaSlider();
});
