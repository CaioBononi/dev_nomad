import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const firebaseConfig = {
  apiKey: "AIzaSyCVUzsQok4wV9z8cpg8u21eUlxRXTI6Has",
  authDomain: "dev-nomad-bononi.firebaseapp.com",
  projectId: "dev-nomad-bononi",
  storageBucket: "dev-nomad-bononi.firebasestorage.app",
  messagingSenderId: "633149362318",
  appId: "1:633149362318:web:1a1c1db9807c77cbd339df",
  measurementId: "G-EPKFMVMEK3"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);