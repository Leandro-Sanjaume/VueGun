<script lang="ts" setup>
import { AuthError, AuthErrorType } from '../models/AuthErrors';
import { getAuth, signInWithEmailAndPassword } from 'firebase/auth';
import { use_user_store } from '../stores/use_user_store';

const email_login = ref('');
const password_login = ref('');

const user_store = use_user_store();
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
  await navigateTo('/home')
};

if ( user_store.user != null ) {
  await navigateTo({ path: '/home' })
}

</script>

<template>
 <div class="flex flex-row">
    <div class="w-1/3 flex items-center justify-center px-24 py-24">
      <NuxtLink
        to="/register" id="switch_button"
        class="px-4 py-2 font-medium text-4xl text-white capitalize transition-colors duration-200 transform bg-primary rounded-md focus:outline-none focus:ring focus:ring-opacity-80"
      >Login Page</NuxtLink>
    </div>
   
    <div class="w-1/3 px-12 py-12 my-24 mx-24">
      <form  @submit.prevent @submit="login_user" class="space-y-3">
        <div>
          <h1 class="font-bold text-lg md:text-xl xl:text-2xl tracking-tight">Login</h1>
        </div>
        <div class="space-y-2">
          <label for="email" class="block font-medium tracking-tight">Email</label>
          <input type="email" placeholder="Email" id="email_input" v-model="email_login"
class="w-full border border-gray-400 text-gray-800 placeholder-gray-400 rounded focus:border-transparent focus:outline-none focus:shadow-outline px-3 py-2"
          />
        </div>
        <div class="space-y-2">
          <label for="password" class="block font-medium tracking-tight">Password</label>
          <input type="password" placeholder="Password" id="password_input" v-model="password_login"
          class="w-full border border-gray-400 text-gray-800 placeholder-gray-400 rounded focus:border-transparent focus:outline-none focus:shadow-outline px-3 py-2"
          />
        </div>
        <div class="flex justify-end">
          <input class="btn btn-accent" type="submit" id="sumbit_button" value="Login">
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