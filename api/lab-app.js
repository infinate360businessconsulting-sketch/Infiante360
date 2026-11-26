// GET /lab: serves the lab only with a valid session cookie; otherwise sends the visitor to the sign-in page.
const fs = require("fs"), path = require("path");
const { checkSession, cookieOf } = require("./_labauth");
module.exports = (req, res) => {
  const email = checkSession(process.env.LAB_SECRET, cookieOf(req, "lab_session"));
  if (!email) { res.statusCode = 302; res.setHeader("Location", "/lab/login"); res.end(); return; }
  const html = fs.readFileSync(path.join(process.cwd(), "labs-private", "identity-xdm", "index.html"), "utf8").replace("{{EMAIL}}", email.replace(/[<>&"]/g, ""));
  res.setHeader("Content-Type", "text/html; charset=utf-8");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Robots-Tag", "noindex");
  res.status(200).send(html);
};
