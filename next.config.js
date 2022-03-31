/** @type {import('next').NextConfig} */

const debug = process.env.NODE_ENV !== "production";
module.exports = {
  exportPathMap: function () {
    return {
      "/": { page: "/" },
    }
  },
  assetPrefix: !debug ? 'http://sohil876.github.io/TestWorld/' : '',
  //nextConfig
  reactStrictMode: true,
  images: {
    loader: "custom",
  },
}

