<template>
  <div>
    <v-list class="flex-row d-flex" :style="'background-color:'+ color +';'+'max-height: 3rem; padding: 0 !important;'">
      <v-list-item
        v-for="(item, index) in categorias"
        :key="index"
        class="mx-2"
      >
        <v-menu
          v-if="item.hijos"
        >
          <template v-slot:activator="{ props }">
            <v-list-item-title
              v-bind="props"
            >
              {{ item.nombre }}
            </v-list-item-title>
          </template>
          <v-list style="margin-top: 0.8rem">
            <v-list-item
              v-for="(subItem, subIndex) in item.categorias"
              :value="subIndex"
              :key="subIndex"
              style="padding-top: 0 !important; padding-bottom: 0 !important;"
            >
              <v-list-item-title>{{ subItem.nombre }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
        <v-list-item-title v-else-if="item.mostrar">{{ item.nombre }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </div>
</template>
<script setup lang="ts">
import {Categoria} from "@/types/NavBarInterfaces";

const props = defineProps<{
  color: string;
  categorias: Categoria[];
}>();

console.log(props.categorias, 'categorias from menu secundario');

</script>
<style scoped>

</style>
