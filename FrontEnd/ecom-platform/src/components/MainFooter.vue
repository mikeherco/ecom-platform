<template>
  <v-footer
    v-if="data && data.paleta_color && data.paleta_color.length > 0"
    class="d-flex flex-column pt-4"
    :color="data.paleta_color[0].primario"
  >
    <div class="d-flex" v-if="data && data.footer && data.footer.columna && data.footer.columna.length > 0">
      <div class="d-flex flex-row px-2" style="flex: 1 1 50%;">
        <div>
          <p class="text-h6">Redes sociales</p>
          <v-btn
            v-for="(social, index) in filteredRedesSociales"
            :key="index"
            :icon="social.icono.icono"
            variant="text"
            :href="social.enlace.url || null"
          >
          </v-btn>
        </div>
      </div>
      <div v-if="data && data.footer" style="flex: 1 1 50%;">
        <p class="w-100 text-h6" v-if="data.footer.columna[0].titulo">{{data.footer.columna[0].titulo}}</p>
        <p v-html="data.footer.columna[0].texto"></p>
      </div>
    </div>
    <div class="d-flex" v-else>
      <div class="d-flex flex-row px-2" style="flex: 1 1 50%;">
        <div>
          <p class="text-h6">Redes sociales</p>
          <v-btn
            v-for="(social, index) in filteredRedesSociales"
            :key="index"
            :icon="social.icono.icono"
            variant="text"
            :href="social.enlace.url || null"
          >
          </v-btn>
        </div>
      </div>
    </div>

    <v-divider></v-divider>

    <div class="py-3">
      {{ new Date().getFullYear() }} — <strong>{{data.footer.licencia}}</strong>
    </div>
  </v-footer>
</template>
<script setup lang="ts">
import { defineProps, computed } from 'vue';
import { RedSocial } from '@/types/FooterInterfaces';

const props = defineProps({
  data: Object,
});

const filteredRedesSociales = computed(() => {
  return props.data?.footer?.redes_sociales?.filter((social: RedSocial) => social.icono.mostrar) || [];
});
</script>
