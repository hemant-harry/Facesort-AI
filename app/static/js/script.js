window.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const loading = document.getElementById("loading");
    const results = document.getElementById("results");

    form.addEventListener("submit", async (e) => {

        e.preventDefault();

        loading.style.display = "block";
        results.innerHTML = "";

        const formData = new FormData(form);

        const response = await fetch("/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loading.style.display = "none";

        if (!data.success) {

            results.innerHTML = `
                <h2>${data.message}</h2>
            `;

            return;
        }

        let html = `
            <h2>✅ ${data.matched_images} Matching Photos Found</h2>

            <div class="gallery">
        `;

        data.files.forEach(file => {

            html += `
                <div class="photo-card">

                    <img src="/output/${file.file}" alt="${file.file}">

                    <h3>${file.file}</h3>

                    <p>Similarity : ${(file.score * 100).toFixed(1)}%</p>

                </div>
            `;

        });

        html += `</div>`;

        if (data.matched_images > 0) {

            html += `
                <a href="/download">
                    <button type="button" class="download-btn">
                        📦 Download All Matched Images
                    </button>
                </a>
            `;
        }

        results.innerHTML = html;

    });

});