<script lang="ts" setup>
import { AuthError, AuthErrorType } from '../models/AuthErrors';
import { getAuth, signInWithEmailAndPassword, createUserWithEmailAndPassword } from 'firebase/auth';
import { use_user_store } from '../stores/use_user_store';

const email_register = ref('');
const password_register = ref('');

const user_store = use_user_store();
const logged_in = ref( false );
const error: Ref<AuthError> = ref({ type: AuthErrorType.NoError, msg: '' });

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
    await navigateTo({ path: '/home' })

    clear_inputs();
};

const clear_inputs = () => {
    email_register.value = '';
    password_register.value = '';
};



</script>

<template>
 <div class="flex flex-row">
    <div class="w-1/3 flex items-center justify-center pl-24 pr-12 py-24">
      <NuxtLink
        to="/login" id="switch_button"
        class="px-4 py-2 font-medium text-4xl text-white capitalize transition-colors duration-200 transform bg-primary rounded-md focus:outline-none focus:ring focus:ring-opacity-80"
      >Register Page</NuxtLink>
    </div>
   
    <div class="w-1/3 px-12 py-12 my-24 mx-24">
      <form @submit.prevent @submit="register_user" class="space-y-3">
        <div>
          <h1 class="font-bold text-lg md:text-xl xl:text-2xl tracking-tight">Register</h1>
        </div>
        <div class="space-y-2">
          <label for="email" class="block font-medium tracking-tight">Email</label>
          <input type="email" placeholder="Email" id="email_input" v-model="email_register"
            class="w-full border border-gray-400 text-gray-800 placeholder-gray-400 rounded focus:border-transparent focus:outline-none focus:shadow-outline px-3 py-2"
          />
        </div>
        <div class="space-y-2">
          <label for="password" class="block font-medium tracking-tight">Password</label>
          <input
          type="password" placeholder="Password" id="password_input" v-model="password_register"
          class="w-full border border-gray-400 text-gray-800 placeholder-gray-400 rounded focus:border-transparent focus:outline-none focus:shadow-outline px-3 py-2"
          />
        </div>
        <div class="flex justify-end">
          <input type="submit" class="btn btn-accent" id="sumbit_button" value="Register">
        </div>
      </form>
    </div>
  </div>

  <div class="error-container" v-if="error.type != AuthErrorType.NoError">
     <b id="error-message" style="color: red">Error: {{ error.msg }}</b>
    </div>

</template>

<style>
.error-container {
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>