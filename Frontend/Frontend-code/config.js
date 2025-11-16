// Frontend/config.js
// Deployment-time configuration for the frontend.
// Replace the placeholder values during deployment or generate this file dynamically.

window.APP_CONFIG = {
  // Backend API address (ALB DNS or domain). Use https:// if your ALB/CloudFront terminates TLS.
  API_URL: "https://BACKEND_ALB_OR_DOMAIN",

  // S3 upload endpoint if backend exposes a dedicated upload endpoint.
  S3_UPLOAD_URL: "https://BACKEND_ALB_OR_DOMAIN/api/upload",

  // A flag for environment
  ENV: "production"
};
