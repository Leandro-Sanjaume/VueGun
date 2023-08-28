import { initializeApp } from 'firebase/app';
import { getAuth } from 'firebase/auth';

export default defineNuxtPlugin( ( nuxt_app ) => {
    // To use environment variables use useRuntimeConfig() and define runtimeConfig in nuxt.config.ts
    const firebase_config = {
        apiKey: "AIzaSyACfiVIGUtYZ-VFyRByZbsVB8BEqvQ4aZ4",
        authDomain: "datos-series-pruscino-pt.firebaseapp.com",
        projectId: "datos-series-pruscino-pt",
        storageBucket: "datos-series-pruscino-pt.appspot.com",
        messagingSenderId: "837621605947",
        appId: "1:837621605947:web:fa7a654374e673dd439e1e",
        measurementId: "G-TJ5SWEYHZJ"
    };

    const app   = initializeApp( firebase_config );
    const auth  = getAuth( app );

    nuxt_app.vueApp.provide( 'auth', auth );
    nuxt_app.provide( 'auth', auth );

    nuxt_app.vueApp.provide( 'app', app );
    nuxt_app.provide( 'app', app );
} );
