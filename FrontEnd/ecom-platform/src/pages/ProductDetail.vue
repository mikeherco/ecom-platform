<script setup lang="ts">
import HeroProduct from "@/components/HeroProduct.vue";

const productos = [
  {
    id: 1,
    nombre: 'Camiseta Azul',
    descripcion: 'Una camiseta azul hecha de algodón 100% con un diseño moderno y cómodo.',
    imagen: 'https://example.com/images/camiseta-azul.jpg',
    precio: 19.99,
    color: 'Azul',
    resumen: 'Camiseta azul de algodón 100%.'
  },
  {
    id: 2,
    nombre: 'Zapatos Deportivos',
    descripcion: 'Zapatos deportivos diseñados para correr, con suela antideslizante y materiales transpirables.',
    imagen: 'https://example.com/images/zapatos-deportivos.jpg',
    precio: 49.99,
    color: 'Negro',
    resumen: 'Zapatos deportivos con suela antideslizante.'
  },
  {
    id: 3,
    nombre: 'Bolso de Mano',
    descripcion: 'Elegante bolso de mano de cuero genuino, perfecto para cualquier ocasión.',
    imagen: 'https://example.com/images/bolso-de-mano.jpg',
    precio: 89.99,
    color: 'Marrón',
    resumen: 'Bolso de mano de cuero genuino.'
  },
  {
    id: 4,
    nombre: 'Reloj de Pulsera',
    descripcion: 'Reloj de pulsera con correa de acero inoxidable y resistencia al agua hasta 50 metros.',
    imagen: 'https://example.com/images/reloj-de-pulsera.jpg',
    precio: 129.99,
    color: 'Plateado',
    resumen: 'Reloj de pulsera resistente al agua.'
  },
  {
    id: 5,
    nombre: 'Gafas de Sol',
    descripcion: 'Gafas de sol polarizadas con protección UV, ideales para días soleados.',
    imagen: 'https://example.com/images/gafas-de-sol.jpg',
    precio: 29.99,
    color: 'Negro',
    resumen: 'Gafas de sol polarizadas con protección UV.'
  }
];
</script>

<template>
<HeroProduct :datos="productos[0]" />
</template>

<style scoped>

</style>
