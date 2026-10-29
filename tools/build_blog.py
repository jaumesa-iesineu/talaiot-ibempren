#!/usr/bin/env python3
"""Genera blog/index.html a partir de les carpetes de blog/.

Cada post és una carpeta amb el nom de la data (AAAA-MM-DD-nom) i conté:
  titol.txt  -> el títol del post
  data.txt   -> la data que es mostra (p. ex. 29/10/2026)
  index.html -> el contingut del post

Ús: python3 tools/build_blog.py
"""

import html
from pathlib import Path

ARREL = Path(__file__).resolve().parent.parent
BLOG = ARREL / "blog"


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
            f'  <li><a href="{carpeta.name}/index.html">{titol}</a> '
            f"<small>{data}</small></li>"
        )

    llista = "\n".join(items) if items else "  <li>Encara no hi ha posts.</li>"

    pagina = f"""<!DOCTYPE html>
<html lang="ca">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Blog - Talaiot IBEmpren</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<main class="blog">
<p class="tornar"><a href="../index.html">&larr; Inici</a></p>
<h1>Blog</h1>
<ul class="llista-posts">
{llista}
</ul>
</main>
</body>
</html>
"""
    (BLOG / "index.html").write_text(pagina, encoding="utf-8")
    print(f"blog/index.html generat amb {len(items)} post(s).")


if __name__ == "__main__":
    generar()
