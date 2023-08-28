<script setup lang="ts">
import { AuthError, AuthErrorType } from '../models/AuthErrors';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth';
import { use_user_store } from '../stores/use_user_store';

const email_login = ref('');
const password_login = ref('');

const email_register = ref('');
const password_register = ref('');

const user_store = use_user_store();
const logged_in = ref( false );
const error: Ref<AuthError> = ref({ type: AuthErrorType.NoError, msg: '' });

const login_user = async () => {
    if ( email_login.value.trim() == "" || password_login.value.trim() == "" ) {
        error.value = { type: AuthErrorType.IncompleteFields, msg: 'Please complete all fields' };
        return;
    }

    const login_result = await signInWithEmailAndPassword( getAuth(), email_login.value, password_login.value )
    .catch( ( reason: any ) => {
        if ( reason instanceof Error ) {
            error.value = { type: AuthErrorType.FirebaseAuthError, msg: reason.message };
            return;
        }
    } );

    user_store.user = login_result!.user;
    logged_in.value = true;

    clear_inputs();
};

const register_user = async () => {
    if ( email_register.value.trim() == "" || password_register.value.trim() == "" ) {
        error.value = { type: AuthErrorType.IncompleteFields, msg: 'Please complete all fields' };
        return;
    }

    const register_result = await createUserWithEmailAndPassword(getAuth(), email_register.value, password_register.value)
    .catch( ( reason: any ) => {
        if ( reason instanceof Error ) {
            error.value = { type: AuthErrorType.FirebaseAuthError, msg: reason.message };
            return;
        }
    } );

    user_store.user = register_result!.user;
    logged_in.value = true;

    clear_inputs();
};

const logout_user = () => {
    user_store.user = null;
    logged_in.value = false;
};

const clear_inputs = () => {
    email_login.value = '';
    password_login.value = '';

    email_register.value = '';
    password_register.value = '';
};

if ( user_store.user != null ) {
    logged_in.value = true;
}

</script>

<template>
    <div>
        <h1>Datos de Serie Comercial en Millones de Dolares</h1>

        <hr>
    </div>

    <div class="logged-user" v-if="logged_in">
        <span>Currently logged in as {{ user_store.user!.email }}</span>
        <input type="button" value="Logout" @click="logout_user">
    </div>

    <div class="auth-controls">
        <div class="login">
            <form @submit.prevent @submit="login_user">
                <input type="email" placeholder="Email" v-model="email_login">
                <input type="password" placeholder="Password" v-model="password_login">

                <input type="submit" value="Login">
            </form>
        </div>
        <div class="register">
            <form @submit.prevent @submit="register_user">
                <input type="email" placeholder="Email" v-model="email_register">
                <input type="password" placeholder="Password" v-model="password_register">

                <input type="submit" value="Register">
            </form>
        </div>
    </div>
    <div class="error-container" v-if="error.type != AuthErrorType.NoError">
        <b style="color: red">Error: {{ error.msg }}</b>
    </div>

    <ApiData v-if="logged_in" @fetch_error="console.error" />
</template>

<style scoped>
.auth-controls {
    display: grid;
    grid-template-areas: "login register";
}

.error-container {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>
