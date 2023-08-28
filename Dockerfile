FROM node:18

RUN mkdir -p /usr/src/nuxt-app
WORKDIR /usr/src/nuxt-app

COPY . /usr/src/nuxt-app/
RUN npm ci
RUN npm run build

EXPOSE 80

ENV PORT 80


CMD [ "npm", "start" ]