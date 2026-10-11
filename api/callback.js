// GitHub OAuth callback for Decap CMS: exchanges the code for a token and hands it to the CMS window.
module.exports = async (req, res) => {
  const { code, state } = req.query || {};
  const cookie = (req.headers.cookie || "").split(";").map((c) => c.trim()).find((c) => c.startsWith("i360_oauth_state="));
  const expected = cookie ? cookie.split("=")[1] : "";
  const send = (status, content) => {
    const msg = JSON.stringify(`authorization:github:${status}:${JSON.stringify(content)}`);
    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.setHeader("Set-Cookie", "i360_oauth_state=; Path=/api; HttpOnly; Secure; SameSite=Lax; Max-Age=0");
    res.end(`<!doctype html><meta charset="utf-8"><body><script>
(function () {
  function receive(e) {
    if (e.origin !== window.location.origin) return;
    window.opener.postMessage(${msg}, e.origin);
    window.removeEventListener("message", receive, false);
  }
  window.addEventListener("message", receive, false);
  window.opener.postMessage("authorizing:github", window.location.origin);
})();
</script></body>`);
  };
  if (!code || !state || state !== expected) return send("error", { message: "Invalid sign-in state. Please try again." });
  try {
    const r = await fetch("https://github.com/login/oauth/access_token", {
      method: "POST",
      headers: { Accept: "application/json", "Content-Type": "application/json" },
      body: JSON.stringify({
        client_id: process.env.OAUTH_GITHUB_CLIENT_ID,
        client_secret: process.env.OAUTH_GITHUB_CLIENT_SECRET,
        code,
      }),
    });
    const data = await r.json();
    if (!data.access_token) return send("error", { message: "GitHub did not return a token." });
    return send("success", { token: data.access_token, provider: "github" });
  } catch (err) {
    return send("error", { message: "Sign-in failed." });
  }
};
