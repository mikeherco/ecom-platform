<template>
  <v-app class="main">
    <nav-bar :data="data" />
    <v-main>
      <Maintenance v-if="data.mantenimiento" />
      <router-view v-else />
    </v-main>
    <main-footer />
  </v-app>
</template>

<script lang="ts" setup>
import NavBar from "@/components/NavBar.vue";
import MainFooter from "@/components/MainFooter.vue";
import apiBase from '@/utils/axios';
import { ref } from 'vue';
import Maintenance from "@/pages/Maintenance.vue";

const data = ref([]);

async function getData() {
  try {
    const response = await apiBase.get('/configuracion-sitio/');
    data.value = response.data.length > 0 ? response.data[0] : {};
    console.log(data.value);
  } catch (error) {
    console.error('Error al obtener datos:', error);
  }
}

getData();
</script>
<style>

</style>
