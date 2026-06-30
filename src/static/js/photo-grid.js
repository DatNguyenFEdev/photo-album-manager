document.addEventListener("DOMContentLoaded", () => {
    const uploadInput = document.getElementById("photo-upload-input");
    if (uploadInput) {
        uploadInput.addEventListener("change", async (e) => {
            const files = e.target.files;
            if (!files.length) return;
            const form = document.getElementById("upload-form");
            for (const file of files) {
                const fd = new FormData();
                fd.append("file", file);
                try {
                    const res = await fetch(form.action, { method: "POST", body: fd });
                    if (!res.ok) throw new Error("Upload failed");
                    location.reload();
                } catch (err) {
                    alert("Failed to upload: " + file.name);
                }
            }
        });
    }

    document.querySelectorAll(".delete-btn").forEach((btn) => {
        btn.addEventListener("click", async (e) => {
            e.stopPropagation();
            const photoId = btn.dataset.photoId;
            const albumId = window.location.pathname.split("/").pop();
            if (!confirm("Delete this photo?")) return;
            try {
                await App.api.delete(`/api/albums/${albumId}/photos/${photoId}`);
                btn.closest(".photo-tile").remove();
            } catch (err) {
                alert("Failed to delete photo");
            }
        });
    });
});
