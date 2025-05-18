# API Backend README

## Requisitos previos

* Python 3.10+ instalado.
* `venv` o similar para entornos virtuales.
* `pip` para instalar dependencias.

---

## 1. Clonar el repositorio y preparar el entorno

```bash
# Sitúate en la carpeta raíz de tu proyecto
cd /ruta/a/PracticaVue/backend

# Crear y activar el entorno virtual
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
# venv\Scripts\activate    # Windows (PowerShell)

# Instalar las dependencias
pip install -r requirements.txt
```

---

## 2. Arrancar el servidor Flask + GraphQL

```bash
# Con el entorno virtual activo:
python app.py
```

* El servidor escuchará en `http://0.0.0.0:5001/graphql`.

---

## 3. Probar manualmente en GraphiQL

Abrir el navegador en:

```
http://localhost:5001/graphql
```

### 3.1. Consulta de productos

Pegar en el editor:

```graphql
query {
  allProducts {
    id
    nombre
    precio
    stock
    disponible
  }
}
```

▶️ Cuando se ejecuta y se debería ver el array de productos.

### 3.2. Mutaciones de stock

**Incrementar stock** (id = 1):

```graphql
mutation {
  incrementStock(id: 1) {
    ok
    product { id nombre stock disponible }
  }
}
```

**Disminuir stock** (id = 1):

```graphql
mutation {
  decrementStock(id: 1) {
    ok
    product { id nombre stock disponible }
  }
}
```

---

## 4. Ejecutar pruebas automáticas

El proyecto incluye pruebas unitarias en `test.py`.

```bash
# Con el entorno virtual activo:
python test.py
```

O usando `pytest`:

```bash
pip install pytest
pytest test.py
```

Se vera que cubren:

* Consulta `allProducts` retorna la lista completa.
* `incrementStock` incrementa stock y actualiza `disponible`.
* `decrementStock` disminuye el stock, llega a 0 y no permite valores negativos.

---
