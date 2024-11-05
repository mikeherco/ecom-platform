import axios from 'axios';

const apiBase = axios.create({
  baseURL: import.meta.env.VITE_APP_BACKEND_URL, // Usa tu variable de entorno aquí
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiBase;
