# Primer ejercicio

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



## Segundo Ejercicio

### 1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

- **Fetch preciso de datos**  
  Permite que la solicitud sea exactamente los campos que se necesita (`id`, `nombre`, `stock`), reduciendo el _overfetching_ y _underfetching_ que es muy común de REST.  
- **Un único endpoint**  
  En lugar de múltiples rutas REST (`/products`, `/products/:id`, `/products/:id/stock`…), todo se consulta contra `/graphql`, simplificando la configuración de red.  
- **Esquema auto-documentado**  
  Gracias al esquema tipado (SDL), herramientas como GraphiQL o Apollo Studio muestran automáticamente los tipos, queries y mutaciones disponibles.  
- **Agilidad en evolución**  
  Al añadir nuevos campos al tipo `Product`, el front puede empezar a solicitarlos sin que el backend añada nuevas rutas.

---

## 2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

En una API GraphQL, los tipos y los resolvers se definen de la siguiente manera así:


```python
# Definición para un tipo de objeto
class Product(graphene.ObjectType):
    id = graphene.ID(required=True)
    nombre = graphene.String(required=True)
    precio = graphene.Float(required=True)
    stock = graphene.Int(required=True)
    disponible = graphene.Boolean(required=True)

# Definición de la Query
class Query(graphene.ObjectType):
    all_products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.ID(required=True))

# Definición de Mutacion
class IncrementStock(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    ok = graphene.Boolean()
    product = graphene.Field(lambda: Product)

class Mutation(graphene.ObjectType):
    increment_stock = IncrementStock.Field()
    decrement_stock = DecrementStock.Field()

# Creación para el esquema
schema = graphene.Schema(query=Query, mutation=Mutation)
```

Para los resolvers son funciones que ayudan a determinar cómo se obtienen los datos para cada campo solictado:

```python
class Query(graphene.ObjectType):
    all_products = graphene.List(Product)
    product = graphene.Field(Product, id=graphene.ID(required=True))

    # Resolver para la función all_products
    def resolve_all_products(self, info):
        return ProductModel.get_all()
    
    # Resolver para función deproduct
    def resolve_product(self, info, id):
        return ProductModel.get_by_id(id)

class IncrementStock(graphene.Mutation):
    # Resolver para la mutación
    def mutate(self, info, id):
        product = ProductModel.get_by_id(id)
        product.stock += 1
        product.disponible = product.stock > 0
        product.save()
        return IncrementStock(ok=True, product=product)
```

Los resolvers se podría que son el puente entre el esquema GraphQL y la lógica o la capa de acceso a los datos.

## 3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

* **Integridad de datos:** El backend es la única fuente confiable de verdad. Si confiamos en que el frontend calcule la disponibilidad, podríamos tener inconsistencias cuando múltiples clientes interactúan con la API ya que todo se mantiene en el frontend.

* **Seguridad:** Nunca se debe confiar en la validación del cliente. Un hacker podría manipular las peticiones para intentar comprar productos no disponibles si la lógica solo está en el frontend.

* **Operaciones masivas:** El backend puede actualizar la disponibilidad durante operaciones masivas como importaciones de inventario, que para ser una tienda en línea se debe tener muy en cuenta.

## 4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

* **Encapsulación de la lógica:** Implementé la lógica de actualización en un solo lugar (un servicio o modelo) que se reutiliza en todos los resolvers de mutación, así pudiendo evitar duplicidad y posibles discrepancias.

* **Reglas de negocio explícitas:** Definí claramente que significa "disponible" (por ejemplo, stock > 0) y aseguro que esta regla se aplica consistentemente en cada operación.

* **Validaciones:** Implementé validaciones tanto a nivel de aplicación como de base de datos (por ejemplo, stock >= 0) para evitar que algún estado sea inválido.

* **Tests:** Desarrollé pruebas automatizadas que verifican que la lógica de negocio se comporte como se espera en diversos escenarios.
