# Editorial standards for research

1. **One distinct question per page.** Check `data/research/topic_registry.json` and the route snapshot first. Update an existing page rather than writing a near-duplicate.
2. **Primary sources only** for technical claims: vendor documentation, standards bodies, official project sites.
3. **No invented proof.** No made-up statistics, client names, testimonials, rankings, learner counts or partner status. Numbers come from a cited source or are labelled as illustrative.
4. **Label hypotheticals.** Every example that is not a real, permitted engagement carries the note "Illustrative example for teaching" (the `ILL` snippet).
5. **Separate fact, interpretation and recommendation.** Use headings so the reader can tell which is which.
6. **State limits.** Include a limitations section: version dependence, vendor differences, what was not tested.
7. **Vendor neutrality.** Do not claim a product feature unless the documentation says so. When unsure, tell the reader to verify.
8. **Plain style.** Short paragraphs, defined acronyms, no engagement bait, no filler.
9. **Metadata.** Title up to 65 characters, description 70 to 160, unique H1, answer paragraph of 25 to 90 words, at least two FAQs, sources list.
10. **Dates.** Show "last updated" only from the build date. Do not state a review that did not happen.
11. **Disclosure.** Keep the site's AI-assisted-content disclosure accurate. Say "reviewed" only when a person reviewed.
12. **Revisions.** Do not silently change findings. Record the change in the commit message.

Mechanical checks for items 3, 4 and 9 run in `scripts/validate_research.py` and the tests.
