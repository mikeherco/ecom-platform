<template>
  <v-carousel
      height="600"
      show-arrows="hover"
      cycle
      hide-delimiter-background
    >
    <v-carousel-item
      v-for="(slide, i) in productos"
      :key="i"
    >
      <v-sheet
        :color="colors[i]"
        height="100%"
      >
      <div class="d-flex fill-height pl-16 justify-start align-center">
        <div class="flex-column d-flex">
          <div class="text-h2">
            {{ slide }}
          </div>
          <div>
            Información secundaria de {{ slide }}
          </div>
        </div>
      </div>
      </v-sheet>
    </v-carousel-item>
  </v-carousel>
</template>
<script setup lang="ts">
import { ref } from 'vue'

const colors = ref([
  'indigo',
  'warning',
  'pink darken-2',
  'red lighten-1',
  'deep-purple accent-4',
])

const productos = ref([
  'Producto 1',
  'Producto 2',
  'Producto 3',
  'Producto 4',
  'Producto 5',
])
</script>
<style scoped>

</style>
