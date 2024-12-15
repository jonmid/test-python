## Getting Started

```bash
# Crear entorno virtual del proyecto
python -m venv venv

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Generar archivo de "requirements.txt"
pip freeze >  requirements.txt

# Ejecutar los test
python -m unittest discover -v -s tests

# Ejecutar los test por suite
PYTHONPATH=. python tests/suites.py
```
