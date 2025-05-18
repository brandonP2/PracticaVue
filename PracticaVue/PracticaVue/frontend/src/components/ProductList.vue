<template>
  <main class="flex-1 p-4">
    <div v-if="loading">Cargando productos...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>

    <template v-else>
      <div class="mb-4">
        <h1 class="text-2xl font-bold mb-1">PLATOS PREPARADOS DE NUESTRA COCINA</h1>
        <p class="text-gray-600 mb-3">Descubre cómo está preparado para que esté en su punto</p>
        <div class="flex justify-between items-center">
          <span>{{ productos.length }} products</span>
          <select class="border rounded px-2 py-1">
            <option>Default sort</option>
            <option>Price (low to high)</option>
            <option>Price (high to low)</option>
          </select>
        </div>
      </div>

      <div class="grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <div
          v-for="producto in productos"
          :key="producto.id"
          class="border rounded p-3 shadow hover:shadow-md transition"
        >
          
          <img :src="imagesMap[producto.id]" alt="Imagen" class="w-full mb-3"/>
          <h3 class="font-semibold mb-1">{{ producto.nombre }}</h3>
          <p class="text-gray-700 mb-1">{{ producto.precio }} €/kg</p>
          <p class="text-sm text-gray-500 mb-3">Descripción rápida</p>

          <div class="flex items-center justify-between mb-3">
            <span>Stock: {{ producto.stock }}</span>
          </div>

          <div v-if="producto.disponible" class="bg-green-100 text-green-800 px-2 py-1 rounded text-center">Disponible</div>
          <div v-else class="bg-red-100 text-red-800 px-2 py-1 rounded text-center">No disponible</div>
        </div>
      </div>
    </template>
  </main>
</template>

<script setup>
import { useProducts } from '@/composables/useProducts'
import ensaladaChina from '@/assets/img/ensalada_china-1.jpg'
import filetePescado from '@/assets/img/filetedepescado.jpg'
import carneVacuno from '@/assets/img/platos-digestivos-con-carne-de-vacuno-interior-noticia.jpg'
import Pasta from '@/assets/img/istockphoto-1144823591-612x612.jpg'

const { productos, loading, error, incrementarStock, disminuirStock } = useProducts()

const imagesMap = {
  1: ensaladaChina,
  2: filetePescado,
  3: carneVacuno,
  4: Pasta
}
</script>

