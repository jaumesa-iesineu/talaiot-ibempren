# talaiot-ibempren

Web del projecte Talaiot per a IBEmpren (Projecte Intermodular, DAM).

Cada push a `main` es publica a https://talaiot.eu/ibempren/

## Blog

Per afegir un post, crea una carpeta `blog/AAAA-MM-DD-nom/` amb:

- `titol.txt`: el títol del post.
- `data.txt`: la data que es mostra (p. ex. `29/10/2026`).
- `index.html`: el contingut del post (enllaços relatius, com a la resta).

Després executa `python3 tools/build_blog.py` per regenerar `index.html` i fes el commit de tot.
