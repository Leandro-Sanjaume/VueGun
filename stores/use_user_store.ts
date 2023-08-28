import { User } from 'firebase/auth';
import { defineStore } from 'pinia';

export const use_user_store = defineStore( 'user_store', () => {
    const user = ref<User | null>( null );

    return { user };
} );