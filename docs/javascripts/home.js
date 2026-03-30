(() => {
  const root = document.documentElement;

  const updateHomeScroll = () => {
    if (!root.classList.contains("codex-homepage")) return;

    const hero = document.querySelector("[data-codex-home-hero]");
    if (!hero) return;

    const viewport = Math.max(window.innerHeight, 1);
    const distance = Math.max(hero.offsetHeight - viewport * 0.2, 1);
    const progress = Math.min(1, Math.max(0, window.scrollY / distance));

    root.style.setProperty("--codex-hero-progress", progress.toFixed(3));
    root.classList.toggle("codex-homepage-scrolled", progress > 0.72);
  };

  window.addEventListener("scroll", updateHomeScroll, { passive: true });
  window.addEventListener("resize", updateHomeScroll);
  window.addEventListener("load", updateHomeScroll);
})();
