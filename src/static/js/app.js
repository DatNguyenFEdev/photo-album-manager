// Application utilities
const App = {
    api: {
        async post(url, data) {
            const body = new FormData();
            for (const [key, value] of Object.entries(data)) {
                body.append(key, value);
            }
            const res = await fetch(url, { method: "POST", body });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return res.json();
        },

        async delete(url) {
            const res = await fetch(url, { method: "DELETE" });
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return res.json();
        },
    },

    keyboard: {
        init() {
            document.addEventListener("keydown", (e) => {
                if (e.key === "Escape") {
                    const modal = document.getElementById("create-album-modal");
                    if (modal && modal.style.display !== "none") {
                        closeCreateAlbum();
                    }
                }
                if (e.key === "Enter") {
                    const btn = document.querySelector(".btn-primary:focus, .album-card:focus");
                    if (btn) btn.click();
                }
            });

            document.querySelectorAll(".album-card-link").forEach((link) => {
                link.addEventListener("keydown", (e) => {
                    if (e.key === "Enter" || e.key === " ") {
                        e.preventDefault();
                        window.location.href = link.href;
                    }
                });
            });
        },
    },
};

document.addEventListener("DOMContentLoaded", () => {
    App.keyboard.init();
});
