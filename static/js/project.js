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
    img.src = "/static/" + project.modal_image;
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

    // project snapshots
    const shotsWrap = document.getElementById("pmodalShotsWrap");
    const shotsEl = document.getElementById("pmodalShots");

    shotsEl.innerHTML = "";

    if (project.shots && project.shots.length) {
      shotsWrap.style.display = "block";

      project.shots.forEach((src) => {
        const img = document.createElement("img");
        img.src = "/static/" + src;
        img.alt = project.title + " snapshot";
        img.className = "pmodal-shot";

        img.addEventListener("click", () => openShotbox(img.src));

        shotsEl.appendChild(img);
      });

    } else {
      shotsWrap.style.display = "none";
    }


    // footer link buttons
    const linksEl = document.getElementById("pmodalLinks");
    linksEl.innerHTML = "";

    const links = project.links || {};
    const linkOrder = [
      ["github", "GitHub Repository"],
      ["demo", "Live Demo"],
      ["docs", "Documentation"],
      ["slides", "Presentation"]
    ];

    linkOrder.forEach(([key, label]) => {
      const url = links[key];
      if (!url) return;

      const a = document.createElement("a");
      a.className = "pmodal-linkbtn";
      a.href = url;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = label;
      linksEl.appendChild(a);
    });


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

  const shotbox = document.getElementById("shotbox");
  const shotboxImg = document.getElementById("shotboxImage");

  function openShotbox(src) {
    shotboxImg.src = src;
    shotbox.classList.add("is-open");
    shotbox.setAttribute("aria-hidden", "false");
  }

  function closeShotbox() {
    shotbox.classList.remove("is-open");
    shotbox.setAttribute("aria-hidden", "true");
    shotboxImg.src = "";
  }

  // close handlers
  shotbox.querySelectorAll("[data-shot-close]").forEach(el => {
    el.addEventListener("click", closeShotbox);
  });

  // ESC support
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && shotbox.classList.contains("is-open")) {
      closeShotbox();
    }
  });


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
