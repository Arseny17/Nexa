document.addEventListener("DOMContentLoaded", () => {
    const mainImage = document.getElementById("productMainImage");
    const thumbnails = document.querySelectorAll(".thumbnail");

    if (!mainImage || !thumbnails.length) return;

    thumbnails.forEach((thumbnail) => {
        thumbnail.addEventListener("click", () => {
            const nextSrc = thumbnail.dataset.fullSrc;
            const nextAlt = thumbnail.dataset.fullAlt || mainImage.alt;

            if (!nextSrc) return;

            mainImage.src = nextSrc;
            mainImage.alt = nextAlt;

            thumbnails.forEach((item) => item.classList.remove("active"));
            thumbnail.classList.add("active");
        });
    });
});