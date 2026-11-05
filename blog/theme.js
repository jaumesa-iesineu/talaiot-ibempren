(function () {
  function getPreferredTheme() {
    var saved = localStorage.getItem("theme");
    if (saved) {
      return saved;
    }
    return window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }

  function setTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme);
    localStorage.setItem("theme", theme);
  }

  if (!document.documentElement.hasAttribute("data-theme")) {
    setTheme(getPreferredTheme());
  }

  function initToggle() {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var current = document.documentElement.getAttribute("data-theme") || getPreferredTheme();
      var next = current === "dark" ? "light" : "dark";
      setTheme(next);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initToggle);
  } else {
    initToggle();
  }
})();
