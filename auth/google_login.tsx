import { createClient } from '@supabase/supabase-js';
import { useState } from 'react';
import dotenv from 'dotenv';

dotenv.config();

const supabaseUrl = process.env.SUPABASE_PROJECTURL || '';
const supabaseAnonKey = process.env.SUPABASE_APIKEY || '';

const supabase = createClient(
    supabaseUrl,
    supabaseAnonKey
)

export default function Login() {
  const signInWithGoogle = async () => {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: 'google',
    })
    if (error) console.error(error)
  }

  return (
    <button 
      onClick={signInWithGoogle} 
      className="bg-red-500 text-white px-4 py-2 rounded-lg"
    >
      Sign in with Google
    </button>
  )
}
