import axios from "axios";

const api = axios.create({
  baseURL: "https://projectpulse-ai-h2l6.onrender.com",
});

export default api;