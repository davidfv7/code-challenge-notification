/** @type {import('next').NextConfig} */

module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: 'http://api:8000/:path*' // Proxy to Backend
      }
    ]
  }
}
