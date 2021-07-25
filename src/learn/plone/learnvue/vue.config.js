const path = require("path");

const DIST_DIR = path.resolve(__dirname, "app");
const SRC_DIR = path.resolve(__dirname, "src");
const STATIC_DIR = path.resolve(__dirname, "../browser/static/");

module.exports = {
  // 部署應用時的基本路徑 URL，baseUrl從 Vue CLI 3.3 起，已棄用，使用publicPath來替代
  publicPath: "/++plone++learn.plone/",

  // build時構建檔案的目錄，構建時傳入 --no-clean 可關閉該行為
  outputDir: STATIC_DIR, // 當執行 vue-cli-service build 時生成的生產環境構建檔案的目錄

  // build時放置生成的靜態資源 (js、css、img、fonts) 的 (相對於 outputDir 的) 目錄
  assetsDir: "assets",

  // 指定生成的 index.html 的輸出路徑 (相對於 outputDir)。也可以是一個絕對路徑。
  //  indexPath: 'index.pt',

  // 預設在生成的靜態資原始檔名中包含hash以控制快取
  filenameHashing: true,

  // 構建多頁面應用，頁面的設定
  pages: {
    index: {
      // page 的入口
      entry: "src/main.ts",
      // 模板來源
      template: "public/index.html",
      // 在 dist/index.html 的輸出
      // filename: "views/templates/index_test.pt",
      filename: "../../views/templates/index_test.pt",
      // 當使用 title 選項時，
      // template 中的 title 標籤需要是
      // <title><%= htmlWebpackPlugin.options.title %></title>
      title: "Index Page",
      // 在這個頁面中包含的塊，預設情況下會包含
      // 提取出來的通用 chunk 和 vendor chunk。
      chunks: ["chunk-vendors", "chunk-common", "index"],
    },
    subpage: {
      // page 的入口
      entry: "src/login/index.ts",
      // 模板來源
      template: "public/subpage.html",
      // 在 dist/index.html 的輸出
      filename: "../../views/templates/subpage.pt",
      // 當使用 title 選項時，
      // template 中的 title 標籤需要是
      // <title><%= htmlWebpackPlugin.options.title %></title>
      title: "Sub Page",
      // 在這個頁面中包含的塊，預設情況下會包含
      // 提取出來的通用 chunk 和 vendor chunk。
      chunks: ["chunk-vendors", "chunk-common", "index"],
    },
    // 當使用只有入口的字串格式時，
    // 模板會被推導為 `public/subpage.html`
    // 並且如果找不到的話，就回退到 `public/index.html`。
    // 輸出檔名會被推導為 `subpage.html`。
    //  subpage: 'src/subpage/main.ts'
  },

  // 是否在開發環境下通過 eslint-loader 在每次儲存時 lint 程式碼 (在生產構建時禁用 eslint-loader)
  lintOnSave: process.env.NODE_ENV !== "production",

  // 是否使用包含執行時編譯器的 Vue 構建版本
  runtimeCompiler: false,

  // Babel 顯式轉譯列表
  transpileDependencies: [],

  // 如果你不需要生產環境的 source map，可以將其設定為 false 以加速生產環境構建
  productionSourceMap: true,

  // 設定生成的 HTML 中 <link rel="stylesheet"> 和 <script> 標籤的 crossorigin 屬性
  // （注：僅影響構建時注入的標籤）
  crossorigin: "",

  // 在生成的 HTML 中的<link rel="stylesheet">和<script>標籤上啟用 Subresource Integrity (SRI)
  integrity: false,

  // 如果這個值是一個物件，則會通過 webpack-merge 合併到最終的設定中
  // 如果你需要基於環境有條件地設定行為，或者想要直接修改設定，那就換成一個函數 (該函數會在環境變數被設定之後懶執行)。該方法的第一個引數會收到已經解析好的設定。在函數內，你可以直接修改設定，或者返回一個將會被合併的物件
  configureWebpack: {
    output: {
      filename: "js/login/[name].[hash].js",
      chunkFilename: "js/chunk/[name].[chunkhash].js",
    },
  },
  // 對內部的 webpack 設定（比如修改、增加Loader選項）(鏈式操作)
  chainWebpack: () => {},

  // css的處理
  // css: {
  //   // 當為true時，css檔名可省略 module 預設為 false
  //   modules: true,
  //   // 是否將元件中的 CSS 提取至一個獨立的 CSS 檔案中,當作為一個庫構建時，你也可以將其設定為 false 免得使用者自己匯入 CSS
  //   // 預設生產環境下是 true，開發環境下是 false
  //   extract: false,
  //   // 是否為 CSS 開啟 source map。設定為 true 之後可能會影響構建的效能
  //   sourceMap: true,
  //   //向 CSS 相關的 loader 傳遞選項(支援 css-loader postcss-loader sass-loader less-loader stylus-loader)
  //   loaderOptions: {
  //     sass: {
  //       prependData: `
  //          @import "@/assets/scss/main.scss";
  //       `,
  //     },
  //   },
  // },

  // 所有 webpack-dev-server 的選項都支援
  devServer: {
    open: true, // 設定瀏覽器自動開啟專案
    port: 8888, // 設定埠
    proxy: {
      // 設定代理
      "/api": {
        target: "localhost",
        changeOrigin: true, // 開啟跨域
        // secure: true,   // 如果是https介面，需要設定這個引數
      },
    },
  },

  // 是否為 Babel 或 TypeScript 使用 thread-loader
  parallel: require("os").cpus().length > 1,

  // 向 PWA 外掛傳遞選項
  pwa: {},

  // 可以用來傳遞任何第三方外掛選項
  pluginOptions: {},
};
