# syntax = docker/dockerfile:1

ARG NODE_VERSION=18.14.2

FROM node:${NODE_VERSION}-slim as base

ENV NODE_ENV=development

WORKDIR /src

# Build
FROM base as build

COPY package*.json ./
RUN npm install

# Run

FROM build as development
COPY --from=build /src/node_modules /src/node_modules

CMD [ "npm", "run", "dev" ]