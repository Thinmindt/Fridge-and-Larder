FROM node:14.17-alpine as build-vue
WORKDIR /app
# copy dependency info for npm install
RUN npm install -g @vue/cli
COPY ["./package.json", "./package-log.json*", "./"]
RUN npm install
COPY . .
CMD [ "vue", "ui", "--headless", "--port", "8000", "--host", "0.0.0.0" ]