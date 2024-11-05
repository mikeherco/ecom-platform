<template>
  <div class="maintenance-page">
    <div class="gear">
      ⚙️
    </div>
    <h1>Mantenimiento</h1>
    <p>Estamos trabajando para mejorar tu experiencia. Vuelve pronto.</p>
  </div>
</template>

<script setup>
</script>

<style scoped>
.maintenance-page {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  text-align: center;
  background-color: #f5f5f5;
  color: #333;
  font-family: Arial, sans-serif;
}

.gear {
  font-size: 80px;
  animation: spin 2s linear infinite;
  margin-bottom: 20px;
}

h1 {
  font-size: 2em;
  margin: 0;
}

p {
  font-size: 1.2em;
  color: #666;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
