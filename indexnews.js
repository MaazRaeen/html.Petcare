const button = document.getElementById("logins-button");
const menu = document.getElementById("logins-menu");


button.addEventListener("click", function () {
    if (menu.classList.contains("show-menu")) {
        menu.classList.remove("show-menu");
    } else {
        menu.classList.add("show-menu");
    }
});