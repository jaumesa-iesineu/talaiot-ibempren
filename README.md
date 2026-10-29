# talaiot-ibempren

Web del projecte Talaiot per a IBEmpren (Projecte Intermodular, DAM).

Cada push a `main` es publica a https://talaiot.eu/ibempren/

## Blog

Per afegir un post, crea una carpeta `blog/AAAA-MM-DD-nom/` amb:

- `titol.txt`: el títol del post.
- `data.txt`: la data que es mostra (p. ex. `29/10/2026`).
- `index.html`: el contingut del post (enllaços relatius, com a la resta).

Fes commit i push a `main`. Una GitHub Action regenera `index.html` sola i el publica amb la llista de posts.
