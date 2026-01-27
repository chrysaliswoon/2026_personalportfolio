(() => {
  const rail = document.querySelector("[data-tech-rail]");
  const left = document.querySelector("[data-tech-left]");
  const right = document.querySelector("[data-tech-right]");
  if (!rail) return;

  const step = () => Math.max(260, Math.floor(rail.clientWidth * 0.6));

  left?.addEventListener("click", () => {
    rail.scrollBy({ left: -step(), behavior: "smooth" });
  });

  right?.addEventListener("click", () => {
    rail.scrollBy({ left: step(), behavior: "smooth" });
  });

  // Optional: mouse wheel scroll horizontally
  rail.addEventListener("wheel", (e) => {
    // only if user is scrolling normally
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      rail.scrollBy({ left: e.deltaY, behavior: "auto" });
      e.preventDefault();
    }
  }, { passive: false });
})();
