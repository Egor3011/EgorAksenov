FROM node:alpine as build

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build

FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

COPY /certs/aksenovegor.crt /etc/nginx/certs/aksenovegor.crt
COPY /certs/aksenovegor.key /etc/nginx/certs/aksenovegor.key


EXPOSE 5000
CMD [ "nginx", "-g", "daemon off;" ]