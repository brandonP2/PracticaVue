# Respuestas a las preguntas

1. **Vue no detecta cambios dentro de objetos reactivos de la forma que esperarías. ¿Cómo podrías observar un cambio en una propiedad anidada?**  
   Se puede observar un cambio en una propiedad anidada utilizando la opción `deep: true` en `watch()`. Esto permite detectar cambios en cualquier nivel del objeto reactivo.

2. **watch() permite escuchar cambios en propiedades específicas dentro de reactive(), explica cómo funciona.**  
   La función `watch()` recibe dos parámetros principales:  
   - Un _getter_ (una función) que retorna la propiedad o valor a observar.  
   - Una función _callback_ que se ejecuta cuando ese valor cambia.  
   Esto permite reaccionar a cambios específicos sin utilizar propiedades computadas.

3. **¿Cómo harías que un watch() detecte cambios en stock dentro de un array de productos?**  
   Se puede mapear el array para extraer únicamente la propiedad `stock` de cada producto y observar ese arreglo. Por ejemplo:
   ```js
   watch(
     () => productos.map(p => p.stock),
     (newStocks, oldStocks) => {
       // Lógica para actualizar 'disponible' u otras acciones
     }
   )
