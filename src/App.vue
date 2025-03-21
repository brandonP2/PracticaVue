<template>
    <div class="container">
      <!-- Barra lateral de categorías -->
      <aside class="sidebar">
        <h2>SUPERMARKET</h2>
        <ul>
          <li>General food</li>
          <li>Charity collaboration</li>
          <li>Eggs</li>
          <li>Flours and prepared dishes</li>
          <li>International food</li>
          <li>Oils</li>
          <li>Poultry</li>
          <li>Meats</li>
          <li>Fish</li>
          <li>Pizzas</li>
          <li>Bakery</li>
          <li>Frozen food</li>
          <!-- ... más categorías -->
        </ul>
      </aside>
  
      <!-- Contenido principal -->
      <main class="content">
        <div class="header">
          <h1>PLATOS PREPARADOS DE NUESTRA COCINA</h1>
          <p>Descubre cómo preparado para que esté en su punto</p>
          <div class="product-toolbar">
            <span>{{ productos.length }} products</span>
            <select>
              <option>Default sort</option>
              <option>Price (low to high)</option>
              <option>Price (high to low)</option>
            </select>
          </div>
        </div>
  
        <!-- Grid de productos -->
        <div class="product-grid">
          <div
            v-for="(producto, index) in productos"
            :key="index"
            class="product-card"
          >
            <!-- Imagen del producto -->
            <img
              :src="producto.image"
              alt="Imagen del producto"
              class="product-image"
            />
  
            <!-- Información del producto -->
            <h3>{{ producto.nombre }}</h3>
            <p class="product-price">{{ producto.precio }} €/kg</p>
            <p class="product-description">
              Descripción rápida del producto (opcional).
            </p>
  
            <!-- Control de stock -->
            <div class="product-actions">
              <p>Stock: {{ producto.stock }}</p>
              <button @click="incrementarStock(index)">+</button>
              <button @click="disminuirStock(index)">-</button>
            </div>
  
            <!-- Disponibilidad -->
            <div class="product-availability" v-if="producto.disponible">
              <span class="available">Disponible</span>
            </div>
            <div class="product-availability" v-else>
              <span class="unavailable">No disponible</span>
            </div>
          </div>
        </div>
      </main>
    </div>
  </template>
  
  <script setup>
  import { reactive, watch } from 'vue'
  
  // Importa las imágenes locales
  import ensaladaChina from '@/assets/IMG/ensalada_china-1.jpg'
  import filetePescado from '@/assets/IMG/filetedepesacado.jpg'
  import stockPhoto from '@/assets/IMG/istockphoto-1144823591-612x612.jpg'
  import carneVacuno from '@/assets/IMG/platos-digestivos-con-carne-de-vacuno-interior-noticia.jpg'
  
  // Array reactivo de productos
  const productos = reactive([
    {
      nombre: 'Ensalada China',
      precio: 11.0,
      stock: 5,
      disponible: true,
      image: ensaladaChina
    },
    {
      nombre: 'Filete de Pescado',
      precio: 36.0,
      stock: 2,
      disponible: true,
      image: filetePescado
    },
    {
      nombre: 'Carne de Vacuno',
      precio: 43.95,
      stock: 0,
      disponible: false,
      image: carneVacuno
    },
    {
      nombre: 'Foto de Stock (ejemplo)',
      precio: 14.95,
      stock: 10,
      disponible: true,
      image: stockPhoto
    }
  ])
  
  // Watch para detectar cambios en el stock y actualizar "disponible"
  watch(
    () => productos.map(p => p.stock),
    () => {
      productos.forEach(producto => {
        producto.disponible = producto.stock > 0
      })
    }
  )
  
  // Funciones para modificar el stock
  function incrementarStock(index) {
    productos[index].stock++
  }
  
  function disminuirStock(index) {
    if (productos[index].stock > 0) {
      productos[index].stock--
    }
  }
  </script>
  
  <style scoped>
  /* Reset básico */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: Arial, sans-serif;
  }
  
  /* Contenedor principal */
  .container {
    display: flex;
    min-height: 100vh;
  }
  
  /* Barra lateral */
  .sidebar {
    width: 250px;
    background-color: #f5f5f5;
    padding: 20px;
  }
  
  .sidebar h2 {
    font-size: 18px;
    margin-bottom: 10px;
    color: #333;
  }
  
  .sidebar ul {
    list-style: none;
  }
  
  .sidebar li {
    margin-bottom: 8px;
    color: #666;
    cursor: pointer;
    transition: color 0.2s ease-in-out;
  }
  
  .sidebar li:hover {
    color: #333;
  }
  
  /* Contenido principal */
  .content {
    flex: 1;
    padding: 20px;
  }
  
  /* Encabezado y toolbar */
  .header {
    margin-bottom: 20px;
  }
  
  .header h1 {
    font-size: 24px;
    margin-bottom: 5px;
    color: #333;
  }
  
  .header p {
    color: #666;
    margin-bottom: 10px;
  }
  
  .product-toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .product-toolbar select {
    padding: 5px;
    font-size: 14px;
  }
  
  /* Grid de productos */
  .product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 20px;
  }
  
  .product-card {
    background-color: #fff;
    border: 1px solid #eee;
    border-radius: 6px;
    padding: 15px;
    text-align: center;
    transition: box-shadow 0.2s ease-in-out;
  }
  
  .product-card:hover {
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  }
  
  .product-image {
    width: 100%;
    height: auto;
    margin-bottom: 10px;
  }
  
  /* Información del producto */
  .product-price {
    font-size: 16px;
    color: #333;
    margin: 5px 0;
  }
  
  .product-description {
    color: #666;
    font-size: 14px;
    margin-bottom: 10px;
  }
  
  /* Controles de stock */
  .product-actions {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
  }
  
  .product-actions p {
    margin-bottom: 5px;
  }
  
  .product-actions button {
    width: 30px;
    height: 30px;
    border: none;
    background-color: #ddd;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
    margin: 2px;
  }
  
  .product-actions button:hover {
    background-color: #ccc;
  }
  
  /* Disponibilidad */
  .product-availability {
    font-size: 14px;
  }
  
  .available {
    color: #fff;
    background-color: #007b00;
    padding: 5px 10px;
    border-radius: 4px;
  }
  
  .unavailable {
    color: #fff;
    background-color: #c00;
    padding: 5px 10px;
    border-radius: 4px;
  }
  </style>
  