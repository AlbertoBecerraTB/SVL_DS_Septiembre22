# Resumen Buenas Prácticas Indexación Pandas

Como hemos visto, `pandas` introduce índices personalizados para facilitarnos el trabajo de acceso y mejorar la legibilidad del código. No obstante, esto también supone un incremento de la complejidad del objeto y, por lo tanto, un mejor control por parte del usuario.

**Índice implícito**: Indexación por defecto que python utiliza para objetos como arrays, listas, strings, etc. Se caracteriza por comenzar por el valor `0` terminar por `n-1` donde `n` es el tamaño del elemento.

**Índice explícito**: Indexación personalizada por un usuario, que ofrece mayor flexibilidad y permite un código más legible. En esta ocasión, no hay restricciones sobre el tipo o el orden de los índices.

Buenas prácticas
----

  * Si los índices explícitos son `int`, usar siempre la indexación implícita con el método `iloc`.
  * Para acceder a las columnas, evitar usar la llamada a través de atributo (sobretodo para asignaciones). Por ejemplo: `data.col1`. Mejor usar la llamada de `[]` o, mejor aún, el `.loc`.
  * Recordar que el `.iloc` es abierto por la derecha (funcionamiento estándar de python) en el caso de slicing. Por ejemplo: `data.iloc[1:3]` devolverá los elementos con índices implícitos 1 y 2.
  * Recordar que el `.loc` es cerrado por la derecha (contrario al funcionamiento estándar de python) en el caso de slicing. Por ejemplo: `data.iloc["label1":"labeln]` devolverá también el valor con índice `"labeln"`.

Otros
---

* Se recomienda hacer copias de los `DataFrames` en el caso de hacer modificaciones de tipo `concat`, reasignación de slices y otros. Similar al caso de los numpy array. De esta manera, sólo alteramos el subelemento y no el original. 