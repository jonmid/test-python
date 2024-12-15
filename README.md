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

# Ejecutar un test utilizando "DocTest"
python -m doctest src/calculator.py
```

## Test Name Syntax

Para escribir los nombres de los test se puede seguir la siguiente sintaxis:

- Se debe empezar por: <code>test\_</code>
- Nombre del método que se va probar: <code>\_deposit\_</code>
- El escenario que se va probar: <code>\_positive_amount\_</code>
- Resultado esperado: <code>\_increment_balance</code>

**SINTAXIS**: <code>test_method_scenario_result</code><br/>
**Resultado Sintaxis**: <code>test_deposit_positive_amount_increment_balance</code>
