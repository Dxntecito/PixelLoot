// const slider = document.querySelector('.slider');
// const slides = slider.querySelectorAll('.slide');
// const prevButton = slider.querySelector('.prev');
// const nextButton = slider.querySelector('.next');
// const dotsContainer = slider.querySelector('.dots');

// let currentSlide = 0;

// // Agrega los puntos de navegación
// for (let i = 0; i < slides.length; i++) {
//   const dot = document.createElement('div');
//   dot.className = 'dot';
//   dotsContainer.appendChild(dot);
// }

// // Establece el slide actual
// slides[currentSlide].classList.add('active');

// // Agrega eventos a los botones de navegación
// prevButton.addEventListener('click', () => {
//   currentSlide--;
//   if (currentSlide < 0) {
//     currentSlide = slides.length - 1;
//   }
//   updateSlider();
// });

// nextButton.addEventListener('click', () => {
//   currentSlide++;
//   if (currentSlide >= slides.length) {
//     currentSlide = 0;
//   }
//   updateSlider();
// });

// // Actualiza el slider según la navegación
// function updateSlider() {
//   slides.forEach((slide) => {
//     slide.classList.remove('active');
//   });
//   slides[currentSlide].classList.add('active');
//   const dots = dotsContainer.querySelectorAll('.dot');
//   dots.forEach((dot, index) => {
//     dot.classList.remove('active');
//     if (index === currentSlide) {
//       dot.classList.add('active');
//     }
//   });
// }


//             const rueda = document.querySelector('.rueda');
//             const boton = document.querySelector('.boton');
//             let estaGirando = false;

//             boton.addEventListener('click', () => {
//                 if (!estaGirando) {
//                     estaGirando = true;
//                     let anguloAleatorio = Math.floor(Math.random() * 360) + 1440; // 4 vueltas completas + ángulo aleatorio
//                     rueda.style.transform = `rotate(${anguloAleatorio}deg)`;
//                     setTimeout(() => {
//                         estaGirando = false;
//                     }, 5000); // Ajusta la duración del giro según sea necesario
//                 }
//             })

document.addEventListener("DOMContentLoaded", function() {
  const carruseles = document.querySelectorAll(".prd-carrusel");

  carruseles.forEach(carrusel => {
      const slides = carrusel.querySelectorAll(".slide");
      const prev = carrusel.querySelector(".prev");
      const next = carrusel.querySelector(".next");
      const dotsContainer = carrusel.querySelector(".dots");
      const dots = [];
      let currentSlide = 0;

      // Create dots
      slides.forEach((slide, index) => {
          const dot = document.createElement("div");
          dot.classList.add("dot");
          if (index === 0) dot.classList.add("active");
          dot.addEventListener("click", () => {
              goToSlide(index);
          });
          dotsContainer.appendChild(dot);
          dots.push(dot);
      });
      

      function showSlide(index) {
          slides.forEach((slide, i) => {
              slide.classList.toggle("active", i === index);
          });
          dots.forEach((dot, i) => {
              dot.classList.toggle("active", i === index);
          });
      }

      function goToSlide(index) {
          currentSlide = index;
          showSlide(currentSlide);
      }

      function prevSlide() {
          currentSlide = (currentSlide === 0) ? slides.length - 1 : currentSlide - 1;
          showSlide(currentSlide);
      }

      function nextSlide() {
          currentSlide = (currentSlide === slides.length - 1) ? 0 : currentSlide + 1;
          showSlide(currentSlide);
      }
      

      prev.addEventListener("click", prevSlide);
      next.addEventListener("click", nextSlide);


      // Miniatures click event
      const miniatures = carrusel.querySelectorAll(".miniatura img");
      miniatures.forEach((miniature, index) => {
          miniature.addEventListener("click", () => {
              goToSlide(index);
          });
      });
      showSlide(0);
  });
});
