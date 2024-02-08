function openNavbar() {
  var navbar = document.getElementById("navbar");
  navbar.style.display =
    navbar.style.display === "none" || navbar.style.display === ""
      ? "flex"
      : "none";
}
