import pg from 'pg';
const Client = pg.Client

const client = new Client({
  user: 'admin',
  host: 'postgres',
  database: 'price',
  password: 'admin',
  port: 5432, // Default PostgreSQL port
});

client.connect();

async function fetchData(){
  const result = await client.query('SELECT * FROM price_data;');
  // transform to format
    const data = result.rows.map( r => {
        return  [new Date(r.time).getTime(), r.price]
    })
  return data;

}


export default defineEventHandler(async (event) => {

  const data = await fetchData();

  return data;
  })
