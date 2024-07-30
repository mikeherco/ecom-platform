<script setup lang="ts">
const props = defineProps({
  datos: []
})
</script>

<template>
  <v-container fluid class="my-4 contenedor">
    <div class="text-h4 mb-4">
    {{props.datos?.nombre}}
  </div>
    <v-row>
      <v-col>
        <v-img
        :aspect-ratio="1"
        class="bg-white"
        src="https://cdn.vuetifyjs.com/images/parallax/material.jpg"
        cover
        />
      </v-col>
      <v-col>
        Texto
      </v-col>
    </v-row>
  </v-container>

</template>

<style scoped>

</style>
