const path = require('path');

module.exports = {
  entry: './source/index.js',
  performance: {
    hints:false
  },
  output: {
    path: path.resolve(__dirname, 'build'),
    filename: 'index_pack.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: [
          {
            loader: 'babel-loader',
            options: {
              presets: ['react', 'latest'],
              plugins: ['transform-class-properties']
            }
          }
        ],
        exclude: path.resolve(__dirname, 'node_modules')
      }
    ]
  }
};
