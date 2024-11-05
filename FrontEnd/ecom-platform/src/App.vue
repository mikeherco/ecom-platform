<template>
  <v-app class="main">
    <nav-bar :data="data" />
    <v-main>
      <Maintenance v-if="data.mantenimiento" />
      <router-view v-else />
    </v-main>
    <main-footer :data="data" />
  </v-app>
</template>

<script lang="ts" setup>
import NavBar from "@/components/NavBar.vue";
import MainFooter from "@/components/MainFooter.vue";
import apiBase from '@/utils/axios';
import {onBeforeMount, onMounted, ref} from 'vue';
import Maintenance from "@/pages/Maintenance.vue";

const data = ref([]);

const getData= async () => {
  try {
    const response = await apiBase.get('/configuracion-sitio/');
    data.value = response.data.length > 0 ? response.data[0] : {};
    console.log(data.value);
  } catch (error) {
    console.error('Error al obtener datos:', error);
  }
}

onBeforeMount(() => {
  getData();
});
</script>
<style>

</style>
