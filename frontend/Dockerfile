FROM node:16-alpine

WORKDIR /frontend

COPY package*.json ./
COPY next.config.js ./

RUN npm install

COPY src/ .

EXPOSE 3333

CMD npm run dev