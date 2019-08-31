# metnum-tp1

## Compilar

```
g++ src/tp1.cpp -o bin/tp1
```

## Ejecutar

```
./bin/tp1 [metodo] [in] [out]
```

- `metodo`

| # | Método |
| - | - |
| 0 | CMM |
| 1 | WP |
| 2 | ? |

- `in` path al archivo de entrada
- `out` path al archivo de salida

Ejemplo

```
./bin/tp1 0 input/test-prob-1.in output/out
```

## Scripts

### `run.py`

Compila y corre `test-prob-1` en modo 0

```
python ./scripts/run.py
```

### Cuantitativo

Resultado del analisis cuantitativo con los resultados de la catedra.

```
# desde root
python ./scripts/cuantitativo.py
```

- Resutlado: los resultados formateados para insertar en Latex en `./cuantitativo/resultado_latex.out`.

### Comparacion de puestos

Resultados de la comparacion entre los rankings para un input dado, con formato para latex.

```
# desde root
python ./scripts/comparacion.py INPUT
```

- `INPUT` en el directorio `./input/INPUT.in`
- Resultado: rankings y tabla de comparcion en `./comparacion/INPUT/resultado_latex.out`
