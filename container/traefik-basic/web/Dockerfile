FROM nginx:alpine

WORKDIR /usr/share/nginx/html

COPY content/index.html ./index.html
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 8080
