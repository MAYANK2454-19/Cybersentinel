document.addEventListener("DOMContentLoaded", () => {

    const body = document.body;
    const button = document.getElementById("theme-toggle");

    if (!button) return;

    // Load saved theme
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "light") {
        body.classList.add("light-theme");
        button.innerHTML = "🌙";
    } else {
        button.innerHTML = "☀";
    }

    // Toggle theme
    button.addEventListener("click", () => {

        body.classList.toggle("light-theme");

        if (body.classList.contains("light-theme")) {

            localStorage.setItem("theme", "light");
            button.innerHTML = "🌙";

        } else {

            localStorage.setItem("theme", "dark");
            button.innerHTML = "☀";

        }

    });

});