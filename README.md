# Predictora de riesgo cardíaco

Aplicación en Streamlit que pide la edad y el colesterol y muestra si una persona podría sufrir problemas del corazón.

## Requisitos

- Python 3.10+
- Streamlit

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Subir a GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <URL_DEL_REPOSITORIO>
git push -u origin main
```

## Desplegar en Streamlit Cloud

1. Ve a https://streamlit.io/cloud
2. Inicia sesión con GitHub
3. Haz clic en "New app"
4. Selecciona el repositorio
5. Elige la rama `main`
6. En "Main file path" escribe `app.py`
7. Haz clic en "Deploy"

La app quedará disponible en tu navegador con la URL pública que te proporcione Streamlit.
