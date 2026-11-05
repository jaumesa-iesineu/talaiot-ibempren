#!/usr/bin/env python3
"""Genera blog/index.html a partir de les carpetes de blog/.

Cada post és una carpeta amb el nom de la data (AAAA-MM-DD-nom) i conté:
  titol.txt  -> el títol del post
  data.txt   -> la data que es mostra (p. ex. 29/10/2026)
  index.html -> el contingut del post

La pàgina d'inici del projecte (index.html de l'arrel) és aquesta llista.

Ús: python3 tools/build_blog.py
"""

import html
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
BLOG = ARREL / "blog"
SORTIDA = ARREL / "index.html"


def llegir(carpeta, fitxer):
    return (carpeta / fitxer).read_text(encoding="utf-8").strip()


def posts():
    carpetes = [
        c for c in BLOG.iterdir()
        if c.is_dir() and not c.name.startswith((".", "_"))
    ]
    # Els noms comencen per la data, així que ordenar-los alfabèticament
    # deixa els posts més nous primer.
    return sorted(carpetes, key=lambda c: c.name, reverse=True)


def generar():
    items = []
    for carpeta in posts():
        titol = html.escape(llegir(carpeta, "titol.txt"))
        data = html.escape(llegir(carpeta, "data.txt"))
        items.append(
            f'  <li><a href="blog/{carpeta.name}/index.html">{titol}</a> '
            f"<small>{data}</small></li>"
        )

    llista = "\n".join(items) if items else "  <li>Encara no hi ha posts.</li>"

    pagina = f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TalAIot - IBEmpren</title>
<link rel="stylesheet" href="blog/style.css">
<script>
  (function () {{
    const t = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.setAttribute('data-theme', t);
  }})();
</script>
<script src="blog/theme.js" defer></script>
</head>
<body>
<main class="blog">
<div class="nav-top">
<h1>Tal<span style="color: #a855f7; font-weight: 800;">AI</span>ot</h1>
<button id="theme-toggle" class="theme-toggle" aria-label="Canvia el tema" title="Canvia el tema (clar/fosc)">
  <svg class="icon-dark" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
  </svg>
  <svg class="icon-light" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <circle cx="12" cy="12" r="5"></circle>
    <line x1="12" y1="1" x2="12" y2="3"></line>
    <line x1="12" y1="21" x2="12" y2="23"></line>
    <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
    <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
    <line x1="1" y1="12" x2="3" y2="12"></line>
    <line x1="21" y1="12" x2="23" y2="12"></line>
    <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
    <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
  </svg>
</button>
</div>
<ul class="llista-posts">
{llista}
</ul>
</main>
</body>
</html>
"""
    SORTIDA.write_text(pagina, encoding="utf-8")
    print(f"index.html generat amb {len(items)} post(s).")


if __name__ == "__main__":
    generar()
