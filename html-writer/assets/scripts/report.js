(function () {
  function slugify(text, index) {
    return (text || "section")
      .trim()
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, "-")
      .replace(/^-+|-+$/g, "") || "section-" + index;
  }

  function buildToc() {
    const toc = document.getElementById("toc");
    if (!toc) return [];
    const headings = Array.from(document.querySelectorAll(".content h2, .content h3"));
    const used = new Set();
    headings.forEach((heading, index) => {
      if (!heading.id) {
        let id = slugify(heading.textContent, index + 1);
        const base = id;
        let suffix = 2;
        while (used.has(id)) {
          id = base + "-" + suffix;
          suffix += 1;
        }
        heading.id = id;
      }
      used.add(heading.id);
      const link = document.createElement("a");
      link.href = "#" + heading.id;
      link.textContent = heading.textContent;
      link.dataset.depth = heading.tagName === "H3" ? "3" : "2";
      toc.appendChild(link);
    });
    return headings;
  }

  function bindProgress() {
    const bar = document.querySelector("[data-reading-progress]");
    if (!bar) return;
    const update = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      const pct = max > 0 ? (window.scrollY / max) * 100 : 0;
      bar.style.width = pct + "%";
    };
    update();
    window.addEventListener("scroll", update, { passive: true });
  }

  function bindActiveHeading(headings) {
    const links = Array.from(document.querySelectorAll("#toc a"));
    if (!headings.length || !links.length) return;
    const map = new Map(links.map((link) => [link.getAttribute("href").slice(1), link]));
    const observer = new IntersectionObserver((entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      links.forEach((link) => link.classList.remove("active"));
      const link = map.get(visible.target.id);
      if (link) link.classList.add("active");
    }, { rootMargin: "-18% 0px -70% 0px" });
    headings.forEach((heading) => observer.observe(heading));
  }

  function bindDetailsControls() {
    const expand = document.querySelector("[data-expand-all]");
    const collapse = document.querySelector("[data-collapse-all]");
    const allDetails = () => Array.from(document.querySelectorAll("details"));
    if (expand) {
      expand.addEventListener("click", () => allDetails().forEach((node) => { node.open = true; }));
    }
    if (collapse) {
      collapse.addEventListener("click", () => allDetails().forEach((node) => { node.open = false; }));
    }
  }

  function bindCopyButtons() {
    document.querySelectorAll("pre").forEach((pre) => {
      const code = pre.querySelector("code");
      if (!code || pre.querySelector(".copy-code")) return;
      const button = document.createElement("button");
      button.className = "copy-code";
      button.type = "button";
      button.textContent = "Copy";
      button.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(code.innerText);
          button.textContent = "Copied";
          setTimeout(() => { button.textContent = "Copy"; }, 1200);
        } catch (_) {
          button.textContent = "Failed";
          setTimeout(() => { button.textContent = "Copy"; }, 1200);
        }
      });
      pre.appendChild(button);
    });
  }

  function initLibraries() {
    if (window.mermaid) {
      window.mermaid.initialize({ startOnLoad: true, securityLevel: "loose" });
    }
    if (window.Prism) {
      window.Prism.highlightAll();
    }
    if (window.renderMathInElement) {
      window.renderMathInElement(document.body, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false }
        ],
        throwOnError: false
      });
    }
  }

  document.addEventListener("DOMContentLoaded", () => {
    const headings = buildToc();
    bindProgress();
    bindActiveHeading(headings);
    bindDetailsControls();
    bindCopyButtons();
    initLibraries();
  });
})();
