document.addEventListener("DOMContentLoaded", function () {
  // Obtén todos los elementos de la sección__rooms
  const rooms = document.querySelectorAll(".section__rooms_element");
  const elementsPerPage = 3;
  const totalPages = Math.ceil(rooms.length / elementsPerPage);
  const currentPage = 1;

  function showPage(page) {
    rooms.forEach(function (room) {
      room.style.display = "none  !important";
    });

    let startIndex = (page - 1) * elementsPerPage;
    let endIndex = startIndex + elementsPerPage;

    for (var i = startIndex; i < endIndex && i < rooms.length; i++) {
      rooms[i].style.display = "block";
    }
  }

  showPage(currentPage);

  document
    .querySelector(".section__pages button:last-child")
    .addEventListener("click", function () {
      if (currentPage < totalPages) {
        currentPage++;
        showPage(currentPage);
      }
    });

  document
    .querySelector(".section__pages button:first-child")
    .addEventListener("click", function () {
      if (currentPage > 1) {
        currentPage--;
        showPage(currentPage);
      }
    });
});
