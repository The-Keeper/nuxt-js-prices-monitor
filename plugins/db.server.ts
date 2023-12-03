import { Client } from 'pg';

export default defineNuxtPlugin(() => {
    const client = new Client({
        user: 'admin',
        host: 'postgres',
        database: 'price',
        password: 'admin',
        port: 5432, // Default PostgreSQL port
      })
    
//    client.connect()
    

    return {
      provide: {
      }
    }
  })
  