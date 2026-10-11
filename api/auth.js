// GitHub OAuth start for Decap CMS. Requires Vercel env vars:
// OAUTH_GITHUB_CLIENT_ID and OAUTH_GITHUB_CLIENT_SECRET (never commit them).
const crypto = require("crypto");

module.exports = (req, res) => {
  const clientId = process.env.OAUTH_GITHUB_CLIENT_ID;
  if (!clientId) {
    res.status(500).send("Admin sign-in is not configured: set OAUTH_GITHUB_CLIENT_ID and OAUTH_GITHUB_CLIENT_SECRET in Vercel.");
    return;
  }
  const state = crypto.randomBytes(16).toString("hex");
  const host = req.headers["x-forwarded-host"] || req.headers.host;
  const redirect = `https://${host}/api/callback`;
  res.setHeader("Set-Cookie", `i360_oauth_state=${state}; Path=/api; HttpOnly; Secure; SameSite=Lax; Max-Age=600`);
  const url = new URL("https://github.com/login/oauth/authorize");
  url.searchParams.set("client_id", clientId);
  url.searchParams.set("redirect_uri", redirect);
  url.searchParams.set("scope", "repo");
  url.searchParams.set("state", state);
  res.writeHead(302, { Location: url.toString() });
  res.end();
};
