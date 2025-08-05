FROM node:alpine as build

WORKDIR /app

COPY package.json package.json
RUN npm install

COPY . .
RUN npm run build

FROM nginx:stable-alpine

COPY --from=build /app/dist /usr/share/nginx/html
COPY --from=build /app/nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build /app/ssl_sertificate/certificate.crt /etc/ssl/aksenovegor.crt
COPY --from=build /app/ssl_sertificate/certificate.key /etc/ssl/aksenovegor.key


EXPOSE 5000
CMD [ "nginx", "-g", "daemon off;" ]