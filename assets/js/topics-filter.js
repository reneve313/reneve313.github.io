(() => {
  const root = document.querySelector("[data-topics]");
  if (!root) return;
  const entries = [...root.querySelectorAll("[data-topic-entry]")];
  const buttons = [...root.querySelectorAll("[data-filter]")];
  const search = root.querySelector("[data-search]");
  let subject = "all";
  const update = () => {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    entries.forEach((entry) => {
      const visible = (subject === "all" || entry.dataset.subject === subject) && entry.textContent.toLocaleLowerCase().includes(query);
      entry.hidden = !visible;
      if (visible) count += 1;
    });
    root.querySelector("[data-empty]").hidden = count !== 0;
    root.querySelector("[data-result-count]").textContent = `${count}개의 글`;
  };
  buttons.forEach((button) =>
    button.addEventListener("click", () => {
      subject = button.dataset.filter;
      buttons.forEach((item) => {
        const active = item === button;
        item.classList.toggle("is-active", active);
        item.setAttribute("aria-pressed", String(active));
      });
      update();
    })
  );
  search.addEventListener("input", update);
})();
