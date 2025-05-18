const tarjeta = document.getElementById("tarjeta");

const inputNumero = document.getElementById("input-numero");
const inputNombre = document.getElementById("input-nombre");
const inputFecha = document.getElementById("input-fecha");
const inputCCV = document.getElementById("input-ccv");

const numeroTarjeta = document.getElementById("num-tarjeta");
const nombreTarjeta = document.getElementById("nombre-tarjeta");
const fechaTarjeta = document.getElementById("fecha-tarjeta");
const ccvTarjeta = document.getElementById("ccv-tarjeta");

// Formato de número
inputNumero.addEventListener("input", e => {
  let valor = e.target.value.replace(/\D/g, "").slice(0, 16);
  valor = valor.replace(/(.{4})/g, "$1 ").trim();
  numeroTarjeta.textContent = valor.padEnd(19, "#");
  e.target.value = valor;
});

// Nombre
inputNombre.addEventListener("input", e => {
  nombreTarjeta.textContent = e.target.value.toUpperCase() || "NOMBRE DEL TITULAR";
});

// Fecha
inputFecha.addEventListener("input", e => {
  const fecha = e.target.value;
  if (fecha) {
    const [anio, mes] = fecha.split("-");
    fechaTarjeta.textContent = `${mes}/${anio.slice(2)}`;
  } else {
    fechaTarjeta.textContent = "MM/AA";
  }
});

// CCV
inputCCV.addEventListener("focus", () => {
  tarjeta.style.transform = "rotateY(180deg)";
});
inputCCV.addEventListener("blur", () => {
  tarjeta.style.transform = "rotateY(0deg)";
});
inputCCV.addEventListener("input", e => {
  ccvTarjeta.textContent = e.target.value || "###";
});
