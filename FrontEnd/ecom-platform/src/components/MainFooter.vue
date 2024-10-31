<template>
  <v-footer
    class="bg-indigo-lighten-1 d-flex flex-column pt-4"
  >
          <div class="d-flex">
        <div class="d-flex flex-row px-2" style="flex: 1 1 50%;">
          <div>
            <p class="text-h6">Redes sociales</p>
            <v-btn
              v-for="icon in icons"
              :key="icon"
              :icon="icon"
              class="mx-4"
              variant="text"
            ></v-btn>
          </div>
        </div>
        <div style="flex: 1 1 50%;">
          Phasellus feugiat arcu sapien, et iaculis ipsum elementum sit amet. Mauris cursus commodo interdum.
        </div>
      </div>

    <v-divider></v-divider>

    <div class="py-3">
      {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
    </div>
  </v-footer>
</template>
<script>
  export default {
    data: () => ({
      icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
    }),
  }
</script>
