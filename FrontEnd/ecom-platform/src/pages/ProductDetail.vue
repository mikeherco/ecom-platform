<script setup lang="ts">
import HeroProduct from "@/components/HeroProduct.vue";
import DescriptionProduct from "@/components/DescriptionProduct.vue";

const productos = [
  {
    id: 1,
    nombre: 'Camiseta',
    descripcion: 'Una camiseta azul hecha de algodón 100% con un diseño moderno y cómodo.',
    imagen: 'https://contents.mediadecathlon.com/p2571341/k$abada217bebeb85a5602b984f6ed6363/camiseta-de-futbol-manga-corta-essentiel-azul.jpg?format=auto&quality=40&f=452x452',
    precio: 19.99,
    color: ['Azul', 'Negro'],
    resumen: 'Camiseta azul de algodón 100%.',
    especificaciones: [
    {
      type: 'texto',
      descripcion: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac elementum mauris. Aliquam et mattis tortor. Integer quam massa, luctus eget massa a, pulvinar dignissim velit. Vivamus semper dolor risus, sed volutpat metus lacinia nec. Aenean ac orci dui. Nunc pulvinar cursus eros. Donec ultricies at enim a accumsan. Donec euismod iaculis suscipit. Aliquam elementum lacinia fermentum. .'
    },
    {
      type: 'imagen',
      descripcion: 'https://i.pinimg.com/236x/d6/97/65/d697651877c46eef7c64f01ae5542ad5.jpg'
    },
    {
      type: 'texto',
      descripcion: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac elementum mauris. Aliquam et mattis tortor. Integer quam massa, luctus eget massa a, pulvinar dignissim velit. Vivamus semper dolor risus, sed volutpat metus lacinia nec. Aenean ac orci dui. Nunc pulvinar cursus eros. Donec ultricies at enim a accumsan. Donec euismod iaculis suscipit. Aliquam elementum lacinia fermentum. '
    },
    ]
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
  <DescriptionProduct :datos="productos[0].especificaciones"/>
</template>

<style scoped>

</style>
