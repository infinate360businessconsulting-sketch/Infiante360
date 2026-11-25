# White-label platform footer: link corrections (set these in the platform admin)

The footer on the white-label learning platform currently points Contact Us and Blog to the homepage, and Sitemap to the platform's own file. Set these instead (platform admin; the static site cannot change them):

| Footer item | Current | Set to |
|---|---|---|
| Contact Us | https://infiante360techacademy.com/ | https://infiante360techacademy.com/contact-us.html |
| Blog | https://infiante360techacademy.com/ | https://infiante360techacademy.com/insights/ |
| Sitemap | platform-hosted sitemap.xml | https://infiante360techacademy.com/sitemap.xml |
| About Us | https://infiante360techacademy.com/about-us.html | no change |

Also add (if the platform allows): RSS feed https://infiante360techacademy.com/rss.xml.

Status: not applied. Verify each target returns HTTP 200 on the live site before saving.
