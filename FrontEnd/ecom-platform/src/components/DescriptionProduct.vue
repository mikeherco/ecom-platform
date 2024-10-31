<script setup lang="ts">
const props = defineProps({
  datos: {}
})

</script>
<template>
  <v-container fluid class="my-4 contenedor">
    <div class="justify-center align-center d-flex" v-for="item in props.datos" v-bind:key="item.id">
      <div v-if="item.type === 'imagen'">
        {{item.descripcion}}
        <v-img
        :aspect-ratio="1"
        class="bg-white"
        :src="item.descripcion"
        />
      </div>
      <div v-else-if="item.type === 'texto'">
        {{item.descripcion}}
      </div>
    </div>
  </v-container>
</template>

<style scoped>

</style>
