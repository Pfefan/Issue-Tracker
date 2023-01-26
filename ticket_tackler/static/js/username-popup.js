window.onload = function() {
    document.getElementById("username-container").addEventListener("click", function() {
        let popup = document.getElementById("user-popup");
        if (popup.style.display === "none") {
            popup.style.display = "block";
        } else {
            popup.style.display = "none";
        }
    });
}
