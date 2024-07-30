<script setup lang="ts">
let menu = [
  { nombre: 'Cat1', id: 1 },
  { nombre: 'Cat2', id: 2 },
  { nombre: 'Cat3', categorias: [{ nombre: 'categoria1' }, { nombre: 'categoria2' }], id: 3 }
];

</script>

<template>
  <div>
    <v-list class="flex-row d-flex bg-indigo-lighten-1" style="max-height: 3rem; padding: 0 !important;">
      <v-list-item
        v-for="(item, index) in menu"
        :key="index"
        class="mx-2"
      >
        <v-menu
          v-if="item.categorias"
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
        <v-list-item-title v-else>{{ item.nombre }}</v-list-item-title>
      </v-list-item>
    </v-list>
  </div>
</template>



<style scoped>

</style>
