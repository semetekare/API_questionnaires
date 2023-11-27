FROM nginx:1.24-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY /nginx/proxy_params /etc/nginx
COPY /nginx/nginx.conf /etc/nginx/conf.d
