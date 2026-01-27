(function () {
  const modal = document.getElementById("projectModal");
  if (!modal) return;

  const shell = document.querySelector(".projects-shell");
  const closeEls = modal.querySelectorAll("[data-close]");

  function openModal(project) {
    document.getElementById("pmodalTitle").textContent = project.title || "";
    document.getElementById("pmodalSubtitle").textContent = project.subtitle || "";
    document.getElementById("pmodalDesc").textContent = project.description || "";

    // image
    const img = document.getElementById("pmodalImage");
    img.src = "/static/" + project.image;
    img.alt = project.title ? `${project.title} preview` : "Project preview";

    // stack pills
    const stackEl = document.getElementById("pmodalStack");
    stackEl.innerHTML = "";
    (project.stack || []).forEach((s) => {
      const pill = document.createElement("div");
      pill.className = "pmodal-pill";
      pill.textContent = s;
      stackEl.appendChild(pill);
    });

    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.body.style.overflow = "hidden";
    if (shell) shell.classList.add("modal-open");

    // focus close button for accessibility
    const closeBtn = modal.querySelector(".pmodal-close");
    closeBtn?.focus();
  }

  function closeModal() {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.body.style.overflow = "";
    if (shell) shell.classList.remove("modal-open");
  }

  // Open on card click
  document.querySelectorAll(".project-card").forEach((card) => {
    card.addEventListener("click", () => {
      const raw = card.getAttribute("data-project");
      if (!raw) return;
      openModal(JSON.parse(raw));
    });
  });

  // Close on X or backdrop
  closeEls.forEach((el) => el.addEventListener("click", closeModal));

  // Close on ESC
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && modal.classList.contains("is-open")) {
      closeModal();
    }
  });
})();
