document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("descToggle");
    const wrapper = document.getElementById("descWrapper");
    const controls = document.getElementById("descControls");

    if (!btn || !wrapper || !controls) return;

    let isOpen = false;

    btn.addEventListener("click", () => {
        isOpen = !isOpen;
        wrapper.classList.toggle("open", isOpen);

        if (isOpen) {
            btn.textContent = "Скрыть";
            controls.classList.add("expanded");
        } else {
            btn.textContent = "Развернуть";
            controls.classList.remove("expanded");
        }
    });
});