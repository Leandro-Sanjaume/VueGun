<script lang="ts" setup>
import { use_user_store } from '../stores/use_user_store';

const user_store = use_user_store();
const logged_in = ref( false );

if ( user_store.user != null ) {
    logged_in.value = true;
}

const logout_user = () => {
    user_store.user = null;
    logged_in.value = false;
    navigateTo({ path: '/login' })
};

const checked = ref( false );
const dire = ref( '' );
const tipo = ref( 'En que tipo de arma estas interesado?' );

function sumbitGun(){
  if(tipo.value == 'En que tipo de arma estas interesado?'){
    alert("Por favor seleccione un tipo de arma");
    return;
  }else if(dire.value == ''){
    alert("Por favor ingrese una direccion");
    return;
  }
  let aux = ''
  let aux2 = 'usuario no registrado'
  if(checked.value == true){
    aux = "cargada";}
    else{
      aux = "descargada";
    }
  if(logged_in.value == true){
    aux2 = user_store.user!.email!;
  }
  alert("El " + tipo.value + " fue enviado a " + dire.value + " "+ aux + ". Gracias por su compra " + aux2);
}

</script>

<template>
  <header>
    <div class="navbar bg-yellow-400">
  <div class="navbar-start">
    <div class="dropdown">
      <label tabindex="0" class="btn btn-ghost btn-circle">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" /></svg>
      </label>
      <ul tabindex="0" class="menu menu-sm dropdown-content mt-3 z-[1] p-2 shadow rounded-box w-52 bg-yellow-400">
        <li> <input class="drop" type="button" value="Logout" @click="logout_user"></li>
        <li><a class="drop" href="/login">Login</a></li>
        <li><a class="drop" href="https://www.stemplayer.com/stemprojector">About</a></li>
      </ul>
    </div>
  </div>
  <div class="navbar-center">
    <a class="btn btn-ghost normal-case text-xl" href="https://www.youtube.com/watch?v=3gWA6DRcih0" target="_blank">Leto's Gun Shop</a>
  </div>
  <div class="navbar-end">
    <button class="btn btn-ghost btn-circle">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
    </button>
    <button class="btn btn-ghost btn-circle">
      <div class="indicator">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" /></svg>
        <span class="badge badge-xs badge-primary indicator-item"></span>
      </div>
    </button>
  </div>
</div>
</header>
<body>
  <div>
    <div class="logged-user" v-if="logged_in">
        <span>Currently logged in as {{ user_store.user!.email }}</span>       
    </div>
    <form @submit.prevent @submit="sumbitGun()">
    <div class="join grid mt-8 mx-auto max-w-sm h-52 place-items-center bg-yellow-400">
      <select id="selector_arma" v-model="tipo" class="select select-bordered select-accent w-full max-w-xs">
        <option disabled selected>En que tipo de arma estas interesado?</option>
        <option id="rifle">Rifle de asalto</option>
        <option id="subfusil">Subfusil</option>
        <option id="explosivo">Explosivos (Hasta 10 MegaTones)</option>
      </select>
      <input id="direccion" v-model="dire" type="text" placeholder="Escribe la dirección de envío" class="input input-bordered input-accent w-full max-w-xs" />
      <div class="form-control">
    <label class="cursor-pointer label">
    <span class="label-text" style="color: black;">Lista para usar?</span>
    <input id="box" type="checkbox" v-model="checked" class="checkbox checkbox-secondary ml-2" />
    <input id="submit" class="btn btn-error ml-6" type="submit">
  </label>
</div>
    </div>
  </form>
  </div>
</body>
</template>



  
<style>
.navbar{
  color: black;
}
.drop:hover{
  color: white;
  background-color: black;
}
</style>
