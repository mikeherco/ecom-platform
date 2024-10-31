<template>
  <v-container fluid class="my-4">
    <div class="title text-h4">Productos destacados</div>
    <div class="cards-wrapper" v-if="$vuetify.display.mdAndUp">
      <div class="cards-container">
        <v-card
          class="card-item my-4"
          max-width="344"
          link
          v-for="item in productos" :key="item.id"
          :href="item.link"
        >
          <v-img
            height="200px"
            :src="item.imagen"
            cover
          ></v-img>

          <v-card-title>
            {{ item.nombre }}
          </v-card-title>

          <v-card-subtitle class="mb-8">
            {{ item.descripcion }}
          </v-card-subtitle>
        </v-card>
      </div>
    </div>
    <div v-else>
<!--
      TODO: Mobile version
-->
      mobile
    </div>
  </v-container>
</template>
<script setup lang="ts">
const productos = [
  {
    id: 1,
    nombre: 'Producto A',
    descripcion: 'Descripción breve del Producto A. Ideal para múltiples usos.',
    imagen: 'https://via.placeholder.com/150?text=Producto+A',
    link: 'https://example.com/producto-a'
  },
  {
    id: 2,
    nombre: 'Producto B',
    descripcion: 'Descripción breve del Producto B. Excelente calidad y durabilidad.',
    imagen: 'https://via.placeholder.com/150?text=Producto+B',
    link: 'https://example.com/producto-b'
  },
  {
    id: 3,
    nombre: 'Producto C',
    descripcion: 'Descripción breve del Producto C. Perfecto para tus necesidades.',
    imagen: 'https://via.placeholder.com/150?text=Producto+C',
    link: 'https://example.com/producto-c'
  },
  {
    id: 4,
    nombre: 'Producto D',
    descripcion: 'Descripción breve del Producto D. Innovador y eficiente.',
    imagen: 'https://via.placeholder.com/150?text=Producto+D',
    link: 'https://example.com/producto-d'
  },
  {
    id: 5,
    nombre: 'Producto E',
    descripcion: 'Descripción breve del Producto E. Con características únicas.',
    imagen: 'https://via.placeholder.com/150?text=Producto+E',
    link: 'https://example.com/producto-e'
  }
];
</script>
<style scoped>
.title {
  margin-bottom: 20px;
}

.cards-wrapper {
  display: flex;
  justify-content: center;
}

.cards-container {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
  gap: 20px;
  max-width: 75%;
}

.card-item {
  flex: 0 0 auto;
}
</style>
