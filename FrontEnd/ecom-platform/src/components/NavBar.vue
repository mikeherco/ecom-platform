<template>
    <v-toolbar class="pa-1 bg-indigo-lighten-1" density="compact">
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
      <v-btn icon>
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </v-toolbar>
</template>
<script setup lang="ts">
</script>
