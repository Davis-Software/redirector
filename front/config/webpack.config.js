const path = require("path");
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

const devMode = process.env.NODE_ENV !== "production";
const mode = devMode ? "development" : "production";
console.info(`Building in ${mode} mode.`);

module.exports = {
    mode,
    watch: devMode,

    entry: "./src/index.tsx",

    output: {
        path: __dirname + "/../../static/bundle",
        filename: devMode ? "[name].bundle.js" : "[contenthash].b.js",
        chunkFilename: devMode ? "[name].chunk.js" : "[contenthash].c.js",
        clean: true
    },

    module: {
        rules: [
            {
                test: /\.(ts|tsx)$/,
                loader: "babel-loader",
                include: [
                    path.resolve(__dirname, "../src"),
                    path.resolve(__dirname, "../node_modules/swc_ui/src")
                ]
            },
            {
                test: /\.(sa|sc|c)ss$/i,
                use: [
                    devMode ? "style-loader" : MiniCssExtractPlugin.loader,
                    {loader: "css-loader", options: {url: false}},
                    "postcss-loader",
                    "sass-loader",
                ]
            }
        ]
    },

    plugins: [
        new HtmlWebpackPlugin({
            publicPath: "/static/bundle",
            scriptLoading: "blocking",
            template: __dirname + "/../../templates/pages/index.template.html",
            filename: __dirname + "/../../templates/pages/index.html",
            inject: false,
            minify: !devMode
        }),
        new BundleAnalyzerPlugin({
            analyzerMode: devMode ? "server" : "static",
            openAnalyzer: !devMode
        }),
        new MiniCssExtractPlugin({
            filename: devMode ? "[name].bundle.css" : "[contenthash].b.css",
            chunkFilename: devMode ? "[name].chunk.css" : "[contenthash].c.css",
        })
    ],

    resolve: {
        extensions: [".js", ".ts", ".tsx", ".css", "..."]
    },

    devtool: "source-map"
}