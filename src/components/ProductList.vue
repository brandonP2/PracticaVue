<template>
    <main class="flex-1 p-4">
      <!-- Encabezado -->
      <div class="mb-4">
        <h1 class="text-2xl font-bold mb-1">PLATOS PREPARADOS DE NUESTRA COCINA</h1>
        <p class="text-gray-600 mb-3">
          Descubre cómo es preparado para que esté en su punto
        </p>
        <div class="flex justify-between items-center">
          <span>{{ productos.length }} products</span>
          <select class="border rounded px-2 py-1">
            <option>Default sort</option>
            <option>Price (low to high)</option>
            <option>Price (high to low)</option>
          </select>
        </div>
      </div>
  
      <!-- Grid de productos -->
      <div class="grid gap-4 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4">
        <div
          v-for="(producto, index) in productos"
          :key="index"
          class="border rounded p-3 shadow hover:shadow-md transition"
        >
          <!-- Imagen -->
          <img
            :src="producto.image"
            alt="Imagen del producto"
            class="w-full h-auto mb-3"
          />
  
          <!-- Información -->
          <h3 class="font-semibold mb-1">{{ producto.nombre }}</h3>
          <p class="text-gray-700 mb-1">{{ producto.precio }} €/kg</p>
          <p class="text-sm text-gray-500 mb-3">Descripción rápida del producto</p>
  
          <!-- Stock y acciones -->
          <div class="flex items-center justify-between mb-3">
            <span>Stock: {{ producto.stock }}</span>
            <div>
              <button
                class="bg-blue-500 text-white px-2 py-1 rounded mr-1"
                @click="incrementarStock(index)"
              >
                +
              </button>
              <button
                class="bg-red-500 text-white px-2 py-1 rounded"
                @click="disminuirStock(index)"
              >
                -
              </button>
            </div>
          </div>
  
          <!-- Disponibilidad -->
          <div v-if="producto.disponible" class="bg-green-100 text-green-800 px-2 py-1 rounded text-center">
            Disponible
          </div>
          <div v-else class="bg-red-100 text-red-800 px-2 py-1 rounded text-center">
            No disponible
          </div>
        </div>
      </div>
    </main>
  </template>
  
  <script setup>
  import { useProducts } from '@/composables/useProducts.js'
  
  const { productos, incrementarStock, disminuirStock } = useProducts()
  </script>
  
  <style scoped>
  </style>
  