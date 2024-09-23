import axios from 'axios';

const BaseURL = 'http://localhost:8000/rest/'; // Reemplaza con tu URL base

const axiosInstance = axios.create({
  baseURL: BaseURL,
});

export default axiosInstance;
