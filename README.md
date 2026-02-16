╔════════════════════════════════════════════════════════════════╗
║                       Search · Dorks · AI                      ║
╚════════════════════════════════════════════════════════════════╝

**Descripción**
────────────────
Proyecto en Python para **búsqueda automatizada usando dorks** y apoyo con agentes de IA.
Genera consultas (dorks), ejecuta búsquedas, descarga resultados y parsea páginas
para extraer información relevante. Diseñado como prototipo para automatizar
recolección y análisis de hallazgos en motores de búsqueda.

**Estado:** Prototype / Proof of Concept  
**Lenguajes:** Python  
**Branch principal:** `ninja_dorks`

────────────────────────────────────────────────────────────────
◆ Estructura relevante (ejemplos de archivos)
────────────────────────────────────────────────────────────────
- `ninja_dorks.py`         → Script orquestador principal
- `ai_agent.py`            → Lógica del agente IA
- `googlesearch.py`        → Funciones para búsquedas (dorks)
- `results_parser.py`      → Parsers para resultados
- `file_downloader.py`     → Descarga y almacenamiento
- `html_template.html`     → Plantilla para reportes HTML
- `requirements.txt`       → Dependencias (pip)
- `test.py`                → Scripts de prueba rápidos
- `.gitignore`             → Ignorados (revisar que incluya `.env`)
- `bfg.jar`                → Herramienta de limpieza de historial (si aplica)

────────────────────────────────────────────────────────────────
◆ Requisitos mínimos
────────────────────────────────────────────────────────────────
- Python 3.10+  
- pip  
- Entorno virtual recomendado:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```
Instala dependencias:
```bash
pip install -r requirements.txt
```

────────────────────────────────────────────────────────────────
◆ Uso rápido (ejemplo)
────────────────────────────────────────────────────────────────
1. Configura variables de entorno (NO subir a GitHub):
```bash
# crea un .env con tus claves; NUNCA subirlo al repo
OPENAI_API_KEY=sk-...
OTHER_SECRET=...
```

2. Ejecutar (ejemplo básico):
```bash
python ninja_dorks.py
```
Revisa los comentarios en cada script para parámetros y flags.

────────────────────────────────────────────────────────────────
◆ Seguridad / Buenas prácticas
────────────────────────────────────────────────────────────────
- **NUNCA** subas `.env` ni claves API.  
- Si una clave fue expuesta, **revócala** inmediatamente.  
- Para eliminar secretos del historial usa BFG o `git filter-repo` (haciendo backup antes).  
- Asegura `.gitignore` con al menos:
```
.env
.venv/
__pycache__/
*.pyc
```

────────────────────────────────────────────────────────────────
◆ Cómo añadir este README desde tu local (VS Code) y subir a GitHub
────────────────────────────────────────────────────────────────
1. Guardar este archivo como `README.md` en la raíz del repositorio local.
2. Abrir VS Code en la carpeta del proyecto.
3. En la terminal integrada:
```bash
# Asegura .env no se suba
grep -qxF ".env" .gitignore || echo ".env" >> .gitignore
git rm --cached .env || true

# Agrega README y .gitignore
git add README.md .gitignore
git commit -m "Add README and update .gitignore"
# Empuja la rama actual (ej. ninja_dorks) al remoto
git push -u origin ninja_dorks
```
Si tu rama local no existe o quieres renombrarla a `main`:
```bash
git branch -M main
git push -u origin main
```

Si GitHub bloquea el push por detección de secretos, asegúrate de haber **revocado** las claves comprometidas y limpia la historia antes de empujar.

────────────────────────────────────────────────────────────────
◆ Contribuir
────────────────────────────────────────────────────────────────
1. Haz fork del repo.  
2. Crea una rama: `git checkout -b feature/mi-cambio`.  
3. Haz commits claros y pequeños.  
4. Envía PR describiendo cambios y riesgos.

────────────────────────────────────────────────────────────────
╔════════════════════════════════════════════════════════════════╗
║   Nota: confirma que `.env` esté en .gitignore ANTES del push  ║
╚════════════════════════════════════════════════════════════════╝
