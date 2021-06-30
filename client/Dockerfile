FROM node:14.17-alpine as build-vue
WORKDIR /client
# copy dependency info for npm install
RUN npm install -g @vue/cli
COPY ["./package.json", "./package-log.json*", "./"]
RUN npm install
RUN npm install -g get-graphql-schema
COPY . .
RUN sed -i 's/\r//g' ./up.sh  && \  
    chmod +x ./up.sh
ENTRYPOINT sh up.sh