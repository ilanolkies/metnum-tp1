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

- `run.py` compila y corre `test-prob-1` en modo 0
  ```
  python ./scripts/run.py
  ```

- `cuantitativo.py` compila y corre el test de error absoluto. Imprime los resultados formateados para insertar en Latex.
