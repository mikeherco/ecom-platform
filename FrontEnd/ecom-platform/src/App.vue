<template>
  <v-app class="main">
    <nav-bar/>
    <v-main>
      <router-view />
    </v-main>
    <main-footer />
  </v-app>
</template>

<script lang="ts" setup>
  //
import NavBar from "@/components/NavBar.vue";
import MainFooter from "@/components/MainFooter.vue";
import { ref, onMounted } from 'vue';
import axiosInstance from '@/plugins/axios';

const data = ref([]);

//Añadir get de la configuracion de sitio y las categorias
onMounted(async () => {
  try {
    const response = await axiosInstance.get('/endpoint');
    data.value = response.data;
  } catch (error) {
    console.error(error);
  }
});

</script>
<style>

</style>
