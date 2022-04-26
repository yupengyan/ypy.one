#D ockerfile构建Nginx镜像

##
参考：https://www.cnblogs.com/rongfengliang/p/13451631.html
```text
FROM alpine:3.8
ENV TENGINE_VERSION 2.3.2
# nginx: https://git.io/vSIyj
RUN rm -rf /var/cache/apk/* && \
    rm -rf /tmp/*
ENV CONFIG "\
        --prefix=/etc/nginx \
        --sbin-path=/usr/sbin/nginx \
        --modules-path=/usr/lib/nginx/modules \
        --conf-path=/etc/nginx/nginx.conf \
        --error-log-path=/var/log/nginx/error.log \
        --http-log-path=/var/log/nginx/access.log \
        --pid-path=/var/run/nginx.pid \
        --lock-path=/var/run/nginx.lock \
        --http-client-body-temp-path=/var/cache/nginx/client_temp \
        --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
        --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
        --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
        --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
        --user=nginx \
        --group=nginx \
        --with-http_ssl_module \
        --with-http_realip_module \
        --with-http_addition_module \
        --with-http_sub_module \
        --with-http_dav_module \
        --with-http_flv_module \
        --with-http_mp4_module \
        --with-http_gunzip_module \
        --with-http_gzip_static_module \
        --with-http_random_index_module \
        --with-http_secure_link_module \
        --with-http_stub_status_module \
        --with-http_auth_request_module \
        --with-http_xslt_module=dynamic \
        --with-http_image_filter_module=dynamic \
        --with-http_geoip_module=dynamic \
        --with-threads \
        --with-stream \
        --with-stream_ssl_module \
        --with-stream_ssl_preread_module \
        --with-stream_realip_module \
        --with-stream_geoip_module=dynamic \
        --with-http_slice_module \
        --with-mail \
        --with-mail_ssl_module \
        --with-compat \
        --with-file-aio \
        --with-http_v2_module \
        --add-module=modules/ngx_http_lua_module \
        --add-module=modules/ngx_http_upstream_check_module \
        --add-module=modules/headers-more-nginx-module-0.33 \
        --add-module=modules/ngx_http_proxy_connect_module \
        --add-module=modules/ngx_http_user_agent_module \
        --add-module=modules/ngx_multi_upstream_module \
        --add-module=modules/ngx_http_upstream_session_sticky_module \
        --add-module=modules/ngx_http_upstream_vnswrr_module \
        --add-module=modules/ngx_http_slice_module \
        --add-module=modules/ngx_http_reqstat_module \
        --add-module=modules/ngx_http_footer_filter_module \
        --add-module=modules/ngx_http_trim_filter_module \
        --add-module=modules/mod_config \
        --add-module=modules/mod_dubbo \
        "
RUN     addgroup -S nginx \
        && adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \
        && addgroup -g 82 -S www-data && adduser -u 82 -D -S -G www-data www-data \
        && apk update && apk add --no-cache --virtual .build-deps \
                gcc \
                g++ \
                libc-dev \
                make \
                openssl-dev \
                pcre-dev \
                zlib-dev \
                linux-headers \
                curl \
                libxslt-dev \
                gd-dev \
                geoip-dev \
        && curl -L "https://github.com/alibaba/tengine/archive/$TENGINE_VERSION.tar.gz" -o tengine.tar.gz \
        && mkdir -p /usr/src \
        && tar -zxC /usr/src -f tengine.tar.gz \
        && rm tengine.tar.gz \
        && cd /usr/src/tengine-$TENGINE_VERSION \
        && curl -L "https://github.com/openresty/headers-more-nginx-module/archive/v0.33.tar.gz" -o more.tar.gz \
        && curl -L "https://github.com/openresty/luajit2/archive/v2.1-20200102.tar.gz" -o v2.1-20200102.tar.gz \
        && tar -zxC /usr/src/tengine-$TENGINE_VERSION/modules -f more.tar.gz \
        && tar -zxC /usr/src/tengine-$TENGINE_VERSION -f v2.1-20200102.tar.gz \
    && rm  more.tar.gz v2.1-20200102.tar.gz\
    && ls -l /usr/src/tengine-$TENGINE_VERSION/modules \
        && cd luajit2-2.1-20200102 && make && make install \
        && export LUAJIT_LIB=/usr/local/lib  export LUAJIT_INC=/usr/local/include/luajit-2.1 \
    && cd .. && ./configure $CONFIG --with-debug \
        && make -j$(getconf _NPROCESSORS_ONLN) \
        && mv objs/nginx objs/nginx-debug \
        && mv objs/ngx_http_xslt_filter_module.so objs/ngx_http_xslt_filter_module-debug.so \
        && mv objs/ngx_http_image_filter_module.so objs/ngx_http_image_filter_module-debug.so \
        && mv objs/ngx_http_geoip_module.so objs/ngx_http_geoip_module-debug.so \
        && mv objs/ngx_stream_geoip_module.so objs/ngx_stream_geoip_module-debug.so \
        && ./configure $CONFIG \
        && make -j$(getconf _NPROCESSORS_ONLN) \
        && make install \
        && rm -rf /etc/nginx/html/ \
        && mkdir /etc/nginx/conf.d/ \
        && mkdir -p /usr/share/nginx/html/ \
        && install -m644 html/index.html /usr/share/nginx/html/ \
        && install -m644 html/50x.html /usr/share/nginx/html/ \
        && install -m755 objs/nginx-debug /usr/sbin/nginx-debug \
        && install -m755 objs/ngx_http_xslt_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_xslt_filter_module-debug.so \
        && install -m755 objs/ngx_http_image_filter_module-debug.so /usr/lib/nginx/modules/ngx_http_image_filter_module-debug.so \
        && install -m755 objs/ngx_http_geoip_module-debug.so /usr/lib/nginx/modules/ngx_http_geoip_module-debug.so \
        && install -m755 objs/ngx_stream_geoip_module-debug.so /usr/lib/nginx/modules/ngx_stream_geoip_module-debug.so \
        && ln -s ../../usr/lib/nginx/modules /etc/nginx/modules \
        && strip /usr/sbin/nginx* \
        && strip /usr/lib/nginx/modules/*.so \
        && rm -rf /usr/src/tengine-$NGINX_VERSION \
        \
        # Bring in gettext so we can get `envsubst`, then throw
        # the rest away. To do this, we need to install `gettext`
        # then move `envsubst` out of the way so `gettext` can
        # be deleted completely, then move `envsubst` back.
        && apk add --no-cache --virtual .gettext gettext \
        && mv /usr/bin/envsubst /tmp/ \
        \
        && runDeps="$( \
                scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx /usr/lib/nginx/modules/*.so /tmp/envsubst \
                        | tr ',' '\n' \
                        | sort -u \
                        | awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1 }' \
        )" \
        && apk add --no-cache --virtual .nginx-rundeps $runDeps \
        && apk del .build-deps \
        && apk del .gettext \
        && mv /tmp/envsubst /usr/local/bin/ \
        \
        # Bring in tzdata so users could set the timezones through the environment
        # variables
        && apk add --no-cache tzdata \
        \
        # forward request and error logs to docker log collector
        && ln -sf /dev/stdout /var/log/nginx/access.log \
        && ln -sf /dev/stderr /var/log/nginx/error.log
EXPOSE 80 443
STOPSIGNAL SIGTERM
CMD ["nginx", "-g", "daemon off;"]
```

```text
docker build -t nginx .

docker run  \
--restart always \
-p 6080:80 \
-p 6443:443 \
--name nginx \
-d nginx
```

## 
https://github.com/racx/cas-auth-lua-nginx/blob/master/Dockerfile
```text
docker build -t nginx-cas .

```
racx/dev

## 方案
https://github.com/openresty/openresty
https://github.com/EsupPortail/nginx-auth-cas-lua

https://blog.csdn.net/qq_42236935/article/details/106905970

docker run --name openresty -p 80:80 -p 443:443 -di  openresty/openresty
docker exec -it openresty /bin/bash

apt-get update
apt-get -y install vim

https://www.jianshu.com/p/b3b0bf529a0b

$ docker run --rm \
    -p 20000:80 \
    -v 配置文件所在路径:/etc/nginx/conf.d/ \
    -v /tmp/webroot/shared1/:/tmp/webroot/shared1/ \
    -v /tmp/webroot/myshare/:/tmp/webroot/myshare/ \
    openresty/openresty:centos

# 指定提供服务的端口
OPENRESTY_PORT=9992
# 配置反向代理的 Location
OPENRESTY_LOCATION=/baidu/
# 反向代理到的目标
OPENRESTY_PROXY_PASS=http://www.baidu.com/

# 创建用于保存配置的目录
OPENRESTY_CONFIG=/tmp/openresty
mkdir -p "${OPENRESTY_CONFIG}"

# 生成配置文件
cat << EOT > "${OPENRESTY_CONFIG}"/nginx.conf
server {
    listen 80;
    location "${OPENRESTY_LOCATION}" {
        proxy_pass "${OPENRESTY_PROXY_PASS}";
    }
}
EOT

# 启动服务
docker run -d --rm \
    -p ${OPENRESTY_PORT}:80 \
    -v "${OPENRESTY_CONFIG}":/etc/nginx/conf.d/ \
    openresty/openresty:centos


https://registry.hub.docker.com/r/bitnami/openresty


参考：https://github.com/openresty/lua-nginx-module