<script setup lang="ts">
import {ref} from "vue";

const props = defineProps({
  datos: {}
})

const rating = ref(0)
const color = ref("")
</script>

<template>
  <v-container fluid class="my-4 contenedor">
    <v-row no-gutters class="flex justify-center align-center">
      <v-col>
        <v-img
        :aspect-ratio="1"
        class="bg-white"
        :src="props.datos?.imagen"
        cover
        />
      </v-col>
      <v-col class="ml-6">
        <div class="text-h4 mb-2">
          {{props.datos?.nombre}}
        </div>
        <div>
          <v-rating
            v-model="rating"
            class="mb-2"
            density="compact"
          ></v-rating>
        </div>
        <div class="text-md-h6">
          $ {{props.datos?.precio}}
        </div>
        <div>
          {{props.datos?.descripcion}}
        </div>
        <v-col
        cols="12"
        style="padding-left: 0!important;"
        >
          <v-btn-toggle
            v-model="color"
            color="indigo-lighten-1"
            group
          >
            <v-btn v-for="item in props.datos?.color"
            :key="item" class="text-none" :value="item">
              {{item}}
            </v-btn>
          </v-btn-toggle>
        </v-col>
        <v-col style="height: 20%"></v-col>
        <v-col style="width: 100%">
          <div style="justify-content: end; display: flex;">
            <v-btn class="text-none" color="indigo-darken-2">
              Comprar ahora
            </v-btn>
            <v-btn class="ml-2" icon="mdi-cart-plus" color="indigo-darken-2" size="small"></v-btn>
          </div>
        </v-col>
      </v-col>
    </v-row>
  </v-container>

</template>

<style scoped>
</style>
