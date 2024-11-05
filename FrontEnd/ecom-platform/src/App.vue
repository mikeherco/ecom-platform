<template>
  <v-app class="main">
    <nav-bar/>
    <v-main>
      <router-view />
    </v-main>
    <main-footer />
  </v-app>
</template>

<script lang="js" setup>
import NavBar from "@/components/NavBar.vue";
import MainFooter from "@/components/MainFooter.vue";
import apiBase from '@/utils/axios'; // Asegúrate de usar la ruta correcta

async function getData() {
  try {
    const response = await apiBase.get('/configuracion-sitio/');
    console.log(response.data);
  } catch (error) {
    console.error('Error al obtener datos:', error);
  }
}

getData();
</script>
<style>

</style>
