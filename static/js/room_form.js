document.addEventListener("DOMContentLoaded", function () {
  document.getElementById("next_button").addEventListener("click", function () {
    var checkInValue = document.getElementById("check_in").value;
    var checkOutValue = document.getElementById("check_out").value;

    // Check if both check in and check out are filled
    if (checkInValue && checkOutValue) {
      document.getElementById("additional_fields").style.display = "flex";
      document.getElementById("next_button").style.display = "none"; // Hide the next button
    } else {
      alert("Por favor, complete tanto Check In como Check Out.");
    }
  });
});
