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

# Ejecutar los test generales
python -m unittest discover -v -s tests

# Ejecutar todos los test de una clase
python -m unittest tests.test_calculator.CalculatorTests

# Ejecutar un test de una clase
python -m unittest tests.test_calculator.CalculatorTests.test_sum

# Ejecutar los test por suite
PYTHONPATH=. python tests/suites.py
```
