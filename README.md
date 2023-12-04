# Price Monitor Example App

https://github.com/The-Keeper/nuxt-js-prices-monitor/assets/6674932/f0f2a699-eb2f-45dd-b07d-72481835bb68

# Features

Contains dockerised services:
- PostgreSQL database
- Data fetching service
- Web UI using Nuxt 3

This following stack of technologies used:
- [**Nuxt 3 + Vite + TypeScript template**](https://github.com/LighthouseLab/nuxt3-tailwindcss).
- [**Highcharts**](https://www.highcharts.com/): JavaScript library that lets you create charts and dashboards for various platforms and back-ends.
- **Python Modules**:
  - **psycopg2**: the most popular PostgreSQL database adapter for the Python programming language.
  - **schedule**: Python job scheduling for humans.
  - **requests**: simple, yet elegant, HTTP library.



## Running
To build and run the image:

```sh
docker-compose -f docker-compose.dev.yml up
```
or using a helper script

```sh
sh run.sh
```

## License

[ISC License](LICENSE)
