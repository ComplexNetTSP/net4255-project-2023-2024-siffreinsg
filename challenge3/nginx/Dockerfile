FROM nginx:1.25-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY app.conf /etc/nginx/conf.d/app.conf

EXPOSE 80 443

CMD ["nginx", "-g", "daemon off;"]
