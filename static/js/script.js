const nav_links = document.getElementsByClassName("nav-link");

for (let i = 0; i < nav_links.length; i++) {
    nav_links[i].addEventListener("click", activate);
}

function activate() {
    this.classList.add("active")
}