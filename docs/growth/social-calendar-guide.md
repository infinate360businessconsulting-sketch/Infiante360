# 100-post social calendar: how it works

File: `data/social/calendar-100.csv` (upload-post bulk template: text, media_url, date, networks, title, profile, media_type). Built by `scripts/build_social_calendar.py`. Nothing has been uploaded or posted.

Schedule: 27 Nov 2026 to 24 Jan 2027, weekdays 09:30 and 18:30, weekends 11:00. Times are the owner's local time (IST); confirm the tool's timezone setting before upload.

## Mix (100 posts)
| Type | Count | Goes to |
|---|---|---|
| Guide posts, each with its own real guide page and og image | 36 | LinkedIn, Facebook, Instagram, X |
| Programs and batches | 10 | mostly all four |
| Course spotlights with banner images | 10 | all four |
| YouTube references | 8 | LinkedIn, Facebook, X |
| Services | 10 | all four or text networks |
| Tips and education | 12 | LinkedIn, Facebook, X |
| Polls and questions | 6 | LinkedIn, Facebook, X |
| Brand and community | 8 | mixed |
62 rows have an image (Instagram needs one, so only those rows include it). Images are the guide `og.png` files and the 20 banners in `assets/social/` (PNG, 1200x675).

## How each post stays unique
1. Different topic: no two posts share a page except the batches, catalogue and channel, which use different angles.
2. Different hook: six rotating hook patterns for guides (rule, question, checklist, save-this, quick read); other types differ by format (poll, tip, spotlight, proof-of-process).
3. Different link: every URL carries its own `utm_campaign=cal100-NNN`, so results show which post worked.
4. Different image: a guide image or banner is not reused until the whole set has run.
5. Different tags: two or three tags per post, chosen by topic.
6. Spacing: guide posts are interleaved with other types; never two of one type in a row.
7. Rewrite per network if you reuse a post: LinkedIn longer and reflective, X shorter, Facebook friendlier. Do not paste the same text everywhere in the same hour.
8. Refresh after 90 days: new angle on the same guide, never a repeat.

## Rules the calendar follows
- No learner counts, ratings, job, salary or certification promises, and no Adobe endorsement.
- No batch dates or fees (none confirmed). Posts say "next dates on enquiry".
- Instagram does not make links clickable. Set the profile link to https://infiante360techacademy.com/lp/batches.html and treat the link in the caption as a reference.
- YouTube posts link to the channel and demo pages; add specific video URLs when you choose them.
- Review each week's rows before upload; edit freely.

## Measuring
Open Analytics, filter `utm_campaign` starting with `cal100-`, compare by post type, and repeat the best-performing types.

## YouTube descriptions
`data/social/youtube-descriptions-100.csv`: a title (under 100 characters), description, tags and source page for each of the 100 posts, in the same order and date as the calendar. Built by `scripts/build_youtube_descriptions.py`. Each description opens with the post's own text, then the page link, the links block, a disclaimer (independent of Adobe, no guarantees) and hashtags. Chapters are left to add after recording; no video contents are invented. Upload a description only with a video that covers that topic.
