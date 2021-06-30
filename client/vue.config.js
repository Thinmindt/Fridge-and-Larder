module.exports = {
  pluginOptions: {
    apollo: {
      // Enable ESLint for `.gql` files
      lintGQL: true,
    },
    devServer: {
      'port': 5000,
      'host': '0.0.0.0',
    }
  }
}