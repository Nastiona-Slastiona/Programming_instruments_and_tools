FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/default.conf

# USER root

RUN mkdir -p /memlife/web/media
RUN mkdir -p /memlife/web/static
RUN chmod 755 /memlife/web/static
RUN chmod 755 /memlife/web/media

# USER nginx
