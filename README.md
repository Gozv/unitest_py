# Proyecto de Pruebas Unitarias

Un proyecto de ejemplo para demostrar pruebas unitarias en Python usando pytest.

1. **Estructura profesional**: Separación clara entre código fuente y pruebas
2. **Parametrización de pruebas**: Uso de `@pytest.mark.parametrize` para múltiples casos
3. **Manejo de excepciones**: Pruebas que verifican errores esperados
4. **Fixtures**: Uso de fixtures de pytest para reutilización de código
5. **Reportes de cobertura**: Integración con pytest-cov
6. **Tipado estático**: Uso de type hints en el código
7. **Pruebas negativas**: Casos de prueba para entradas inválidas
8. **Documentación clara**: Docstrings en las pruebas y README completo

## Cómo ejecutar:
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar todas las pruebas con reporte de cobertura
pytest

# Ver reporte de cobertura
open htmlcov/index.html
