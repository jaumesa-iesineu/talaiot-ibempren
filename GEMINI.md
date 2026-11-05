[text](GEMINI.md) [text](CLAUDE.md)# Directrius per a Agents d'IA (Gemini) - Talaiot IBEmpren

Aquest document estableix les directrius, l'arquitectura i les bones pràctiques per a qualsevol agent d'IA que col·labori en el repositori `talaiot-ibempren`.

---

## 1. Context i Visió del Projecte

- **Projecte:** Talaiot (marca: **Tal<span style="color: #a855f7; font-weight: 800;">AI</span>ot**)
- **Àmbit:** Projecte Intermodular del Cicle Formatiu de Grau Superior DAM (Desenvolupament d'Aplicacions Multiplataforma), vinculat al programa **IBEmpren** a l'IES Sineu.
- **Objectiu:** Desenvolupar un sistema basat en visió per computador i intel·ligència artificial per a la detecció de conductes irregulars o trampes en exàmens presencials mitjançant càmeres zenitals (instal·lades al sostre de l'aula).
- **Publicació del lloc web:** Cada `push` a la branca `main` es publica automàticament a [https://talaiot.eu/ibempren/](https://talaiot.eu/ibempren/) (subdomini: `ibempren.talaiot.eu`).

### Pilars Tècnics del Sistema
1. **Model Directe vs. Arquitectura Modular:**
   - El prototip inicial d'IA directa des de keypoints 2D va obtenir només un ~50% d'encert pel soroll de l'entorn i la manca de context temporal i espacial.
   - La nova arquitectura adopta un disseny per capes desacoblades:
     - **Capa 0 (Control d'aula):** Detecció i filtratge de transeünts (professors, alumnes en trànsit) i mapeig/segmentació de pupitres (distingint alumne actiu examinant-se vs. pupitre buit o inactiu).
     - **Capa 1 (Vectors de moviment):** Extracció de punts clau 2D (cap, coll, espatlles, mans) i conversió a vectors diferencials normalitzats (trajectòries, velocitats, acceleracions, girs) independents de la posició zenital de la càmera.
     - **Capes superiors:** Classificadors de patrons de comportament i models de detecció d'anomalies.
2. **Ètica i Seguretat de Dades:**
   - Totes les gravacions d'exàmens s'emmagatzemen xifrades/encriptades.
   - Talaiot no reporta les trampes detectades per sancionar els alumnes al seu centre.
   - Programa de recompenses (a partir de 100 €) per a estudiants que trobin buits o conductes no detectades i col·laborin amb dades per al calibratge del model.

---

## 2. Estructura del Repositori

```text
talaiot-ibempren/
├── .github/
│   └── workflows/
│       └── blog.yml           # GitHub Actions: regenera index.html a cada push
├── blog/
│   ├── style.css              # Estils globals del blog i dels articles
│   ├── AAAA-MM-DD-titol-post/ # Carpeta de cada entrada del blog
│   │   ├── titol.txt          # Títol del post (text pla, 1 línia)
│   │   ├── data.txt           # Data en format DD/MM/AAAA
│   │   ├── index.html         # Contingut HTML del post
│   │   └── *.svg / *.png      # Gràfics o esquemes associats
│   └── ...
├── tools/
│   └── build_blog.py          # Script Python que genera index.html a l'arrel
├── .gitignore
├── index.html                 # Índex autogenerat (llista cronològica inversa)
├── README.md                  # Informació bàsica del repositori
├── GEMINI.md                  # Aquestes directrius
└── CLAUDE.md                  # Directrius mirrors per a Claude
```

---

## 3. Normes i Estructura de les Entrades del Blog

Quan es creï o s'editi una entrada del blog, s'ha de respectar estrictament aquesta convenció:

### 3.1 Nomenclatura de la carpeta
- Format: `blog/AAAA-MM-DD-slug-descriptiu/`
- Exemple: `blog/2026-11-05-definicio-capes/`
- La data en el nom de la carpeta determina l'ordre cronològic invers en què `build_blog.py` llista els posts.

### 3.2 Fitxers requerits dins la carpeta
1. `titol.txt`:
   - Concepte breu i descriptiu en text pla UTF-8 (sense etiquetes HTML).
   - Exemple: `Definició de capes`
2. `data.txt`:
   - Data de publicació en format `DD/MM/AAAA`.
   - Exemple: `05/11/2026`
3. `index.html`:
   - Document HTML5 semàntic seguint l'estructura canònica:

```html
<!DOCTYPE html>
<html lang="ca">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>[Títol del post] - Blog TalAIot IBEmpren</title>
  <link rel="stylesheet" href="../style.css">
</head>

<body>
  <main class="post">
    <p class="tornar"><a href="../../index.html">&larr; Blog</a></p>
    <h1>[Títol del post]</h1>
    <p class="data">[DD/MM/AAAA]</p>

    <!-- Paràgraf introductori -->
    <p>...</p>

    <!-- Seccions de contingut -->
    <h2>[Títol de secció]</h2>
    <p>...</p>

    <!-- Exemple d'avís destacat -->
    <div class="avis">
      <strong>Nota:</strong> Informació rellevant, consell o reflexió destacada.
    </div>

    <!-- Exemple de llista numerada de passos -->
    <ol class="passos">
      <li><strong>Pas 1:</strong> Descripció.</li>
      <li><strong>Pas 2:</strong> Descripció.</li>
    </ol>

    <!-- Exemple d'esquema o imatge -->
    <figure>
      <img src="esquema.svg" alt="Descripció accessible de la imatge">
      <figcaption>Peu d'imatge descriptiu.</figcaption>
    </figure>
  </main>
</body>

</html>
```

### 3.3 Elements d'estil i CSS (`blog/style.css`)
- **Branding:** Utilitzar `Tal<span style="color: #a855f7; font-weight: 800;">AI</span>ot` quan es presenti el nom corporatiu o s'emfatitzi el caràcter d'IA.
- **Caixes d'avís:** Utilitzar la classe `.avis` per a apunts, advertències o claus d'aprenentatge.
- **Passos i llistes estilitzades:** Utilitzar la classe `.passos` en elements `<ol>` o `<ul>` per a passos numerats visuals amb cercle d'accent.
- **Imatges i diagrames:** Embolicar en etiquetes `<figure>` amb `<figcaption>` per a peus d'imatge nets.
- **Codi i termes tècnics:** Utilitzar `<code>` per a comandes, fitxers, paràmetres o coordenades (ex: `(x, y)`).
- **Tema:** El CSS suporta natiu `light` i `dark` mode (`prefers-color-scheme`). No incrustar estils inline innecessaris que trenquin el mode fosc.

---

## 4. Llengua, To i Estil Editorial

- **Llengua:** Català normatiu i natural (`lang="ca"`).
- **To:** Professional, acadèmic-emprenedor, transparent i rigorós.
- **Enfocament:** Diari d'enginyeria i d'emprenedoria. S'expliquen tant els èxits com els fracassos o canvis d'estratègia tècnica (ex: passar del model 2D directe a capes modulars).
- **Consistència temporal:** Assegurar que la data de la carpeta, la data a `data.txt` i la data a `<p class="data">` coincideixin.

---

## 5. Flux de Treball i Comandes

### 5.1 Comprovació i generació local de l'índex
L'arxiu `index.html` de l'arrel és generat pel script Python:

```bash
# Execució del generador d'índex
python tools/build_blog.py
```

*Nota:* No modifiqueu mai a mà la llista `<ul>` d'`index.html` directament; s'ha d'executar sempre el script per mantenir la coherència.

### 5.2 Flux de Git
1. Fer sempre `git pull` abans d'iniciar nous canvis.
2. Crear o modificar els arxius corresponents.
3. Executar `python tools/build_blog.py` per verificar que la llista es regenera sense errors.
4. Fer commit amb un missatge clar en català o anglès senzill.
5. Fer `git push` a `main`. GitHub Actions executarà el workflow `.github/workflows/blog.yml` per validar i actualitzar el repositori remot.

---

## 6. Directrius Específiques per a l'Agent d'IA

Quan se't demani crear una nova entrada o modificar codi:
1. **Comprova les dates:** Usa la data real indicada per l'usuari o la data del dia en format `AAAA-MM-DD` per a la carpeta i `DD/MM/AAAA` per a `data.txt` i `index.html`.
2. **Genera els 3 fitxers indispensables:** Crea sempre `titol.txt`, `data.txt` i `index.html` a `blog/AAAA-MM-DD-nom/`.
3. **Diagrames i gràfics:** Si el post requereix il·lustracions o diagrames d'arquitectura, utilitza preferentment gràfics vectorials SVG integrats a la mateixa carpeta del post, amb tipografies de sistema i colors que s'adaptin bé a fons clar/fosc.
4. **Executa el script generador:** Executa `python tools/build_blog.py` després de crear o eliminar qualsevol post per mantenir l'arrel actualitzada.
5. **No afegeixis dependències externes pesades:** Mantingues la web lleugera, estàtica, ràpida i accessible.

