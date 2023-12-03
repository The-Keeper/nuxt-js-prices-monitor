import { Client } from 'pg'
const client = new Client({
    user: 'postgres',
    host: 'localhost',
    database: 'price',
    password: 'postgres',
    port: 5432, // Default PostgreSQL port
  })

client.connect()
export default client
