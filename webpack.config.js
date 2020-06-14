const webpack = require('webpack');
const resolve = require('path').resolve;

const config = {
    entry: __dirname + '/js/index.jsx',
    devtool: 'eval-source-map',
    output:{
        path: resolve('dist'),
        filename: 'bundle.js',
        publicPath: resolve('dist')
    },
    resolve: {
        extensions: ['.js','.jsx','.css']
    },
    module: {
        rules: [{
            test: /\.jsx?/,
            loader: 'babel-loader',
            exclude: /node_modules/
        }]
    }
};

module.exports = config;