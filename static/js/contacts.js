document.addEventListener("DOMContentLoaded", function () {
  var successMessage = document.getElementById("success_message");
  if (successMessage) {
    successMessage.style.display = "block"; // Muestra el mensaje de éxito
    setTimeout(function () {
      successMessage.style.display = "none"; // Oculta el mensaje después de 5 segundos
    }, 5000);
  }
});
