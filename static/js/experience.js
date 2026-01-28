(function () {
  const root = document.querySelector("[data-accordion]");
  if (!root) return;

  const items = Array.from(root.querySelectorAll(".exp-item"));

  function closeItem(item) {
    const btn = item.querySelector(".exp-trigger");
    const panel = item.querySelector(".exp-panel");
    if (!btn || !panel) return;

    btn.setAttribute("aria-expanded", "false");
    panel.hidden = true;
  }

  function openItem(item) {
    const btn = item.querySelector(".exp-trigger");
    const panel = item.querySelector(".exp-panel");
    if (!btn || !panel) return;

    btn.setAttribute("aria-expanded", "true");
    panel.hidden = false;
  }

  items.forEach((item) => {
    const btn = item.querySelector(".exp-trigger");
    const panel = item.querySelector(".exp-panel");
    if (!btn || !panel) return;

    btn.addEventListener("click", () => {
      const isOpen = btn.getAttribute("aria-expanded") === "true";

      // close all others
      items.forEach(closeItem);

      // toggle this one
      if (!isOpen) openItem(item);
    });
  });
})();
