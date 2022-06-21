const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,

  publicPath: '/static/src/vue/dist/', // Should be STATIC_URL + path/to/build
  outputDir:  '../static/src/vue/dist/', // Output to a directory in STATICFILES_DIRS

  devServer: {
 //   static: {
  //    directory: path.join(__dirname, 'public'),
 //   },
    compress: true,
    port: 3000,
  /*  proxy: {
      '^/api': {
        target: 'http://localhost:3000',
        changeOrigin: true,
        secure:false,
        pathRewrite: {'^/api': '/api'},
        logLevel: 'debug' 
                },
    }*/
    devMiddleware: {
      // see https://github.com/webpack/webpack-dev-server/issues/2958
      writeToDisk: true, 
    }
  },


})

