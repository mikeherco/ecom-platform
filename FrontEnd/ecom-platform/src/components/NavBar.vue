<template>
    <v-toolbar
      v-if="data && data.paleta_color && data.paleta_color.length > 0"
      class="pa-1"
      :color="data.paleta_color[0].primario.formato === 'name' ? data.paleta_color[0].primario.valor : null"
      :style="data.paleta_color[0].primario.formato === 'hex' ? {background: data.paleta_color[0].primario.valor} : null"
      density="compact">
<!--
      <v-toolbar-title>Title</v-toolbar-title>
-->
      <router-link to="/">
        <v-img src="https://e7.pngegg.com/pngimages/900/287/png-clipart-logo-icon-design-graphics-illustration-company-text.png" width="110px"/>
      </router-link>
      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-cart</v-icon>
      </v-btn>
      <v-btn v-if="data.invitado_login" icon>
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-toolbar>
    <MenuSecundario v-if="data && data.paleta_color && data.paleta_color.length > 0" :color="data.paleta_color[0].primario" :categorias="categorias"/>
</template>
<script setup lang="ts">
import MenuSecundario from "@/components/MenuSecundario.vue";
import {defineProps, watchEffect, ref} from 'vue';

const props = defineProps(
  {
    data: [Object],
    dataNavbarSecundario: [Object],
  }
);

let categorias = ref([]);

watchEffect(() => {
  if (props.dataNavbarSecundario) {
    categorias.value = props.dataNavbarSecundario.navbar_categorias;
  }
});
</script>
