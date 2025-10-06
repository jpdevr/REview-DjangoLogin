document.addEventListener("DOMContentLoaded", () => {
    const body = document.body;
    body.classList.add("fade");
    setTimeout(() => body.classList.add("show"), 50);
});

document.querySelectorAll("a").forEach(link => {
    link.addEventListener("click", e => {
        if (link.target === "_blank" || link.href.startsWith("#")) return;
        e.preventDefault();
        document.body.classList.remove("show");
        setTimeout(() => {
            window.location.href = link.href;
        }, 300);
    });
});
