/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
document.addEventListener('DOMContentLoaded', function () {
    // Control de switches
    document.getElementById('toggleCategoria').addEventListener('change', function () {
        document.getElementById('categoria').disabled = !this.checked;
    });

    document.getElementById('togglePrecio').addEventListener('change', function () {
        document.getElementById('precioRange').disabled = !this.checked;
    });

    document.getElementById('toggleZona').addEventListener('change', function () {
        document.getElementById('zona').disabled = !this.checked;
    });

    // Control de rango de precio
    const precioRange = document.getElementById('precioRange');
    const precioMinDisplay = document.getElementById('precioMin');
    const precioMaxDisplay = document.getElementById('precioMax');
    const precioMinInput = document.getElementById('precioMinInput');
    const precioMaxInput = document.getElementById('precioMaxInput');

    precioRange.addEventListener('input', function () {
        const minValue = this.min;
        const maxValue = this.value;
        precioMinDisplay.innerText = minValue;
        precioMaxDisplay.innerText = maxValue;
        precioMinInput.value = minValue;
        precioMaxInput.value = maxValue;
    });
});
// Script para manejar el modal de eliminación
const eliminarModal = document.getElementById('eliminarModal');
eliminarModal.addEventListener('show.bs.modal', function (event) {
    const button = event.relatedTarget; // Botón que activó el modal
    const servicioId = button.getAttribute('data-id'); // Extraer el ID del servicio
    const url = button.getAttribute('data-url'); // Extraer la URL para eliminar

    // Actualizar el formulario de eliminación con la URL correcta
    const form = document.getElementById('formEliminar');
    form.action = url;
});