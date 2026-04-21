FROM node:16
LABEL TITLE This is for node application
MAINTAINER Author Subhu
EXPOSE 80
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node","index.js"]
