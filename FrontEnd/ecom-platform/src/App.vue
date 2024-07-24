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
</script>
<style>

</style>
