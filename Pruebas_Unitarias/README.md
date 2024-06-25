# DOCUMENTACION SOBRE COBERTURA DE PRUEBAS UNITARIAS

Este repositorio, recopila las pruebas unitarias realizadas para las cuatro operaciones aritméticas básicas.
Se realizó las pruebas usando los archivos en python y empleando la herramienta de pytest.

## Operaciones o Funciones del archivo

- `sumar(x, y)`
- `restar(x, y)`
- `multiplicar(x, y)`
- `dividir(x, y)`

## Pruebas Unitarias

Se encuentran en el archivo `test_main.py`. Cada operación tiene dos pruebas unitarias que incluyen valores positivos y negativos, además de una prueba para manejar el caso de la división por cero.

## Informe de Cobertura y html

Para ello se emplea `coverage.py`. Estos fueron los pasos realizados para la generación del informe de cobertura:

1. Instalar las dos herramientas mencionadas:

    ```bash
    pip install pytest coverage
    ```

2. Realizar las pruebas:

    ```bash
    coverage run -m pytest
    ```

3. Generar el reporte de cobertura por terminal:

    ```bash
    coverage report
    ```

4. En adición, generar un reporte de cobertura en formato HTML:

    ```bash
    coverage html
    ```

5. Abrir el archivo `index.html` dentro de la carpeta `htmlcov` en un navegador para ver el informe detallado de cobertura.

## RESULTADOS DE COBERTURA

El informe de cobertura muestra que todas las funciones han sido cubiertas al 100% por las pruebas unitarias. 
Cada línea de código de las funciones de las operaciones aritméticas ha sido ejecutada durante las pruebas.

Las muestras del codigo de cobertura y el resumen del informe de cobertura pueden visualizarse en las imagenes:
-`Imagen de pruebas por terminal.PNG`
-`Imagen de informe de pruebas.PNG`
