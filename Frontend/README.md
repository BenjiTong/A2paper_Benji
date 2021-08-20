# a2-project

> frontend part of a2 project

## Set environment

1. Node 16.7.0
2. Vue 2.X

```
Windows 下的 VM 官方网址： https: //github.com coreybutler nvm-windows  
nvm根目录下settings.txt添加（从国内镜像安装）  
node_mirror: http://npm.taobao.org/mirrors/node/  
npm_mirror: https://npm.taobao.org/mirrors/npm/
```

```bash
# install node
ηvm install 16.7.0

# use node
nvm use 16.7.0

# install cpn to replace npm
npm install - g cnpm --registry=https//registry.npm.taobao.com

# install vue cli
cnpm install vue-cli -g
```

## Run Frontend

```bash
# install modules
cd Frontend  
cnpm nstall

# serve with hot reload at localhost:8080
npm run dev
```

## Build Setup

``` bash
# install dependencies
npm install

# serve with hot reload at localhost:8080
npm run dev

# build for production with minification
npm run build

# build for production and view the bundle analyzer report
npm run build --report

# run unit tests
npm run unit

# run e2e tests
npm run e2e

# run all tests
npm test
```

For a detailed explanation on how things work, check out the [guide](http://vuejs-templates.github.io/webpack/) and [docs for vue-loader](http://vuejs.github.io/vue-loader).
