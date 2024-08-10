document.addEventListener("DOMContentLoaded", function() {
  // Obtener todos los checkboxes de las películas
  const movieCheckboxes = document.querySelectorAll('.movie-checkbox');

  // Añadir evento de cambio a cada checkbox
  movieCheckboxes.forEach(checkbox => {
    checkbox.addEventListener('change', function() {
      // El elemento a resaltar es el siguiente hermano del checkbox (el div .movie-data)
      const movieDataDiv = this.nextElementSibling.querySelector('.movie-data');

      // Si el checkbox está seleccionado, añadir la clase de resaltado
      if (this.checked) {
        movieDataDiv.classList.remove('bg-red-500'); // Remueve el resaltado si se deselecciona
        movieDataDiv.classList.add('bg-blue-500'); // Resalta en amarillo
      } else {
        movieDataDiv.classList.remove('bg-blue-500'); // Remueve el resaltado si se deselecciona
        movieDataDiv.classList.add('bg-red-500'); // Resalta en amarillo
      }
    });
  });
});
