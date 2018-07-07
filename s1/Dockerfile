FROM busybox

LABEL maintainer="https://github.com/suryaval"

RUN apt update -y && apt install nginx -y

RUN apt install nodejs nodejs-npm

COPY . /src

WORKDIR /src

RUN npm install

RUN service nginx start

EXPOSE 80

ENTRYPOINT ["node","./app.js"]