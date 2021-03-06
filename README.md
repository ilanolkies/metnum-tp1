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
| 2 | AHP |
| 3 | ODI |
| 4 | CMM c/Cholesky |
| 5 | CMM c/Cholesky ralo | 

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

### Distancias

Resultados de la comparación entre rankings normalizado, para evaluar la distancia entre los puestos.

```
# desde root
python ./scripts/distancias.py INPUT
```

- `INPUT` en el directorio `./input/INPUT.in`
- Resultado: rankings en `./comparacion/INPUT/resultado_latex.out` y gráfico de barras en `./comparacion/INPUT/img/metodo-X.out`

### Performance

Tiempo de ejecución del ranking CMM con Eliminación Gaussiana y con Factorización de Cholesky

```
# desde root
python ./scripts/performance.py INPUT
```

- `INPUT` en el directorio `./input/INPUT.in`
- Resultado: rankings en `./output/INPUT.out` y table en `./performance/INPUT/valores.out`

### ATP Datasets

Para convertir el dataset de ATP a un input de `tp1.cpp` se debe

1. Copiar los archivos `atp_matches_2015.csv` y `atp_players.csv` a la carpeta `./dataset`
2. Correr `python ./scripts/convert_atp_dataset.py`

El resultado es un archivo `./input/atp_matches_2015.in` que representa los enfrentamientos del dataset.

> Los archivos estan ignorados debido a su peso

### `2e_random`

Dados `ejecuciones` y `enfrentamientos` (linea 36) ejecuta los 3 algoritmos (no ODI) `ejecuciones` veces para el rango de `enfrentamientos` y guarda los plots en `2e_random`.

### Equipos ordenados con ranking

Resultados de la comparacion entre los rankings para un input dado, con formato para latex.

```
# desde root
python ./scripts/equiposordenados_nada_ranking.py INPUT
```

- `INPUT` en el directorio `./input/INPUT.in`
- Resultado: rankings y tabla de comparcion en `./comparacion/INPUT/resultado_latex.out`

> A diferencia de `comparacion`, esta devuelve los puntos en el ranking en la misma tabla.

### Justo
Porcentaje en el que cambio el puntaje del equipo 1 si se juegan multiplos de n partidos extra en los que no juega el equipo 1.

```
# desde root
python ./scripts/justo.py INPUT
```

-`INPUT` en el directorio `./input/INPUT.in`
-`METODO` numero de metodo 
-`N` cantidad de partidos a jugar extra
-Resultado en /Justo/INPUT-METODO.out