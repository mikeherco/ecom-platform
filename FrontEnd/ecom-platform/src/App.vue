<template>
  <v-app class="main">
    <nav-bar :data="data" :dataNavbarSecundario="dataNavBar" />
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
import {onBeforeMount, ref} from 'vue';
import Maintenance from "@/pages/Maintenance.vue";
import {NavBarDetail, NavBarItem} from "@/types/NavBarInterfaces";

const data = ref([]);
const itemsNavbar = ref<NavBarItem[]>([]);
const dataNavBar = ref<NavBarDetail | undefined>(undefined);

const getData= async () => {
  try {
    const response = await apiBase.get('/configuracion-sitio/');
    data.value = response.data.length > 0 ? response.data[0] : {};
    console.log(data.value);
  } catch (error) {
    console.error('Error al obtener datos:', error);
  }
}

const getNavBar = async (): Promise<void> => {
  try {
    const response = await apiBase.get<{ items: NavBarItem[] }>('/paginas/?type=paginas.NavBar');
    itemsNavbar.value = response.data.items;
    const [firstNavBar] = itemsNavbar.value;

    if (firstNavBar) {
      const detailResponse = await apiBase.get<NavBarDetail>(firstNavBar.meta.detail_url);
      dataNavBar.value = detailResponse.data;
    }
    console.log(dataNavBar.value, 'Navbar details');
  } catch (error) {
    console.error('Error al obtener los datos:', error);
  }
};

onBeforeMount(() => {
  getData();
  getNavBar();
});
</script>
<style>

</style>
