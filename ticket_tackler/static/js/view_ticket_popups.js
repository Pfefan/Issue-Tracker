function toggleEdit() {
    var display = document.getElementById("ticket-display");
    var form = document.getElementById("ticket-edit-form");
    if (display.style.display === "block") {
        display.style.display = "none";
        form.style.display = "block";
    } else {
        display.style.display = "block";
        form.style.display = "none";
    }
}
