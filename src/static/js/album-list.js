document.addEventListener("DOMContentLoaded", () => {
    let dragSrcEl = null;

    document.querySelectorAll(".album-card").forEach((card) => {
        card.setAttribute("draggable", "true");

        card.addEventListener("dragstart", (e) => {
            dragSrcEl = card;
            card.classList.add("dragging");
            e.dataTransfer.effectAllowed = "move";
            e.dataTransfer.setData("text/plain", card.dataset.albumId);
        });

        card.addEventListener("dragend", () => {
            card.classList.remove("dragging");
            document.querySelectorAll(".album-card").forEach((c) => {
                c.classList.remove("drag-over");
            });
        });

        card.addEventListener("dragover", (e) => {
            e.preventDefault();
            e.dataTransfer.dropEffect = "move";
            card.classList.add("drag-over");
        });

        card.addEventListener("dragleave", () => {
            card.classList.remove("drag-over");
        });

        card.addEventListener("drop", async (e) => {
            e.preventDefault();
            card.classList.remove("drag-over");
            if (dragSrcEl === card) return;

            const parent = card.parentNode;
            const cards = [...parent.querySelectorAll(".album-card")];
            const fromIdx = cards.indexOf(dragSrcEl);
            const toIdx = cards.indexOf(card);

            if (fromIdx < toIdx) {
                parent.insertBefore(dragSrcEl, card.nextSibling);
            } else {
                parent.insertBefore(dragSrcEl, card);
            }

            // Update display order
            const updatedCards = parent.querySelectorAll(".album-card");
            updatedCards.forEach((c, idx) => {
                const albumId = c.dataset.albumId;
                App.api.post("/api/albums/reorder", {
                    album_id: albumId,
                    new_order: idx,
                }).catch(() => {});
            });
        });
    });
});
