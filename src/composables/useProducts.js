import { reactive, watch } from 'vue'

export function useProducts() {
  // 1. Array reactivo
  const productos = reactive([
    {
      nombre: 'Ensalada China',
      precio: 11.0,
      stock: 5,
      disponible: true,
      image: require('@/assets/img/ensalada_china-1.jpg')
    },
    {
      nombre: 'Filete de Pescado',
      precio: 36.0,
      stock: 2,
      disponible: true,
      image: require('@/assets/img/filetedepesacado.jpg')
    
    },
    {
      nombre: 'Carne de Vacuno',
      precio: 43.95,
      stock: 0,
      disponible: false,
      image: require('@/assets/img/platos-digestivos-con-carne-de-vacuno-interior-noticia.jpg')
    },
    {
      nombre: 'Foto de Stock (ejemplo)',
      precio: 14.95,
      stock: 10,
      disponible: true,
      image: require('@/assets/img/istockphoto-1144823591-612x612.jpg')
    }
  ])

  // 2. Watch para actualizar la disponibilidad
  watch(
    () => productos.map(p => p.stock),
    () => {
      productos.forEach(producto => {
        producto.disponible = producto.stock > 0
      })
    }
  )

  // 3. Funciones para modificar el stock
  function incrementarStock(index) {
    productos[index].stock++
  }

  function disminuirStock(index) {
    if (productos[index].stock > 0) {
      productos[index].stock--
    }
  }

  return {
    productos,
    incrementarStock,
    disminuirStock
  }
}
