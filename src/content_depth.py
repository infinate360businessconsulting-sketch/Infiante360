"""Extra depth for thin guides (added 27 Nov 2026). Applied to KB_PAGES at the end of content_kb.py.
Only general, documentation-level statements; no customer results, numbers or product promises.
Each entry: path -> (extra sections, extra faqs). Existing sections are kept; these are appended."""

L = lambda t, h: f'<a href="../{h}">{t}</a>'
IMP = L("AEP implementation guide", "adobe-experience-platform/implementation-guide.html")
XDM = L("XDM schemas", "adobe-experience-platform/xdm-schemas.html")
IDS = L("Identity Service", "adobe-experience-platform/identity-service.html")
ING = L("data ingestion", "adobe-experience-platform/data-ingestion.html")
PRO = L("Real-Time Customer Profile", "adobe-experience-platform/real-time-customer-profile.html")
CAT = L("course catalogue", "academy/catalogue.html")

DEPTH = {
    "guides/ecid-data-element-adobe-tags.html": ([
        ("What ECID is and where it lives", "<p>The Experience Cloud ID (ECID) is the identifier Adobe uses to recognise a browser across visits. With the Web SDK it is held in a first-party cookie set by the Edge Network, and the SDK returns it through the identity command. Because the value is created asynchronously, a data element that reads it too early returns nothing. Treat ECID as a value you wait for, not a value you can assume is present on page load.</p>"),
        ("A safe implementation order", "<ol><li>Confirm the Web SDK extension is configured with the correct datastream and that consent is resolved before identity is requested.</li><li>In a rule that fires after the SDK is ready, run the get-identity action and store the result.</li><li>Expose the stored value through a custom-code data element that returns an empty string when nothing is stored yet.</li><li>Reference the data element only in rules that run after that rule, or trigger them from a custom event fired once the value is stored.</li><li>Test in a staging property with the debugger open before publishing to production.</li></ol>"),
        ("Common mistakes", "<ul><li>Reading the ECID in a page-load rule that runs before the SDK responds.</li><li>Storing the ECID in a place other rules cannot reach, such as a local variable inside one rule.</li><li>Forgetting that a user who has not given consent may have no identity at all, so downstream rules must tolerate an empty value.</li><li>Hard-coding the cookie name, which includes organisation-specific text. Use the SDK command instead of parsing cookies.</li></ul>"),
    ], [("Can I read the ECID cookie directly?", "It is better not to. The cookie name is organisation specific and its format can change. Use the SDK identity command so your implementation keeps working."),
        ("Do I need the ECID if I use a first-party ID?", "A first-party device ID can supply the identifier, but the identity map still needs a valid namespace. Decide this during design and document it.")]),

    "guides/evars-vs-props-adobe-analytics.html": ([
        ("How eVar persistence works", "<p>An eVar keeps its value after the hit that set it. You choose how long it lasts, for example until the end of the visit, a number of days or until a specific event, and how credit is allocated when the value changes, typically to the original value, the most recent value or split across values. This is what lets a campaign code captured on landing be credited with an order placed later in the visit.</p>"),
        ("When a prop is the better tool", "<p>A prop describes a single hit. Use it when you want to see what people viewed next, which needs pathing, or when you want a quick count of a value without conversion attribution. Props can also hold multiple values on a hit when configured as list props. They are not designed for crediting later success events.</p>"),
        ("A decision rule you can reuse", "<ul><li>Will someone ask which value led to revenue or a sign-up? Use an eVar.</li><li>Will someone ask which page or value came before or after? Use a prop.</li><li>Need both? Set both from the same data element so the values match.</li></ul><p>When this data later moves to Customer Journey Analytics, those choices become dimension settings in the data view. See " + L("CJA vs Adobe Analytics", "guides/cja-vs-adobe-analytics.html") + ".</p>"),
    ], [("Why does my eVar show Unspecified?", "Usually the variable was not set on the hit, the expiry ended or a different allocation applied. Check the tag rule that sets it and the variable settings."),
        ("Can one value be both an eVar and a prop?", "Yes. Many teams set both from one data element so they can use pathing and attribution on the same value.")]),

    "guides/backfill-months-aep-cja.html": ([
        ("What backfill does not do", "<p>Backfill never reaches into a warehouse, CRM or analytics tool to fetch history that was never sent to the platform. If you need older data, it must first be loaded through a source connection or batch ingestion, and only then can backfill make it usable in the way described above.</p>"),
        ("Questions to settle before choosing a value", "<ol><li>Which reports or audiences need history, and how far back?</li><li>Does the data already exist in the platform or the source connection?</li><li>What does your licence allow for volume, and who confirms it?</li><li>Is there a quality problem in older data that would be better fixed before it is processed?</li></ol>"),
        ("Plan the change like any other release", "<p>Record the chosen value, the reason and the owner in your delivery backlog. Test with a small window first when possible, then widen it. See the " + IMP + " for where this fits in the delivery sequence.</p>"),
    ], [("Will backfill duplicate data I already have?", "That depends on how the connection and datasets are configured. Confirm behaviour in the product documentation for your connection type and test on a small window."),
        ("Who should approve the backfill value?", "The analytics owner for reporting needs and the platform owner for licence and processing impact.")]),

    "guides/aep-ingestion-methods-batch-streaming.html": ([
        ("Choosing between batch and streaming", "<p>Pick the mode from the use case, not from habit. Streaming suits behaviour that should change an experience quickly, such as a cart event that triggers a message. Batch suits large, periodic loads such as nightly CRM or order files, where freshness within hours is acceptable and volume is high. Streaming data still reaches the data lake after a short delay, so do not assume it is instantly queryable in Query Service.</p>"),
        ("What to decide for each feed", "<ul><li>Target dataset and schema, and whether it is enabled for Profile.</li><li>Primary and secondary identities present in each record.</li><li>Expected volume and frequency, and who is told when a load fails.</li><li>How errors are surfaced, reviewed and replayed.</li></ul>"),
        ("Where to go next", "<p>Read the " + ING + " guide for the pipeline end to end, then " + XDM + " and " + IDS + " so records arrive with the right structure and identities.</p>"),
    ], [("Can one dataset receive both batch and streaming data?", "Yes, a dataset can receive data through more than one route as long as the records match its schema."),
        ("Is streaming always better?", "No. It adds design and monitoring effort. Use it where the business case needs fast reaction; otherwise batch is simpler.")]),

    "guides/adobe-analytics-source-connector-aep.html": ([
        ("Planning the connection", "<p>Before you enable the connector, list the report suites that matter, the business questions each answers and the identity each carries. Sending every suite adds volume and noise. Agree a naming convention for the resulting datasets so people can tell them apart later, and decide whether they should be enabled for Profile or used for Customer Journey Analytics only.</p>"),
        ("Checks after the first load", "<ol><li>Compare event counts for a short window with the same window in Analytics, allowing for processing time.</li><li>Confirm the identity field is populated and uses the expected namespace.</li><li>Spot-check a few mapped eVars and props against the source report suite.</li><li>Review which fields are actually used and remove the rest from future mappings.</li></ol>"),
        ("Related reading", "<p>See " + L("CJA vs Adobe Analytics", "guides/cja-vs-adobe-analytics.html") + " and " + PRO + " for what happens once the events are in.</p>"),
    ], [("Do counts match Adobe Analytics exactly?", "Small differences are normal because of processing and data-handling differences. Define an acceptable variance with stakeholders before sign-off."),
        ("Can I connect more than one report suite?", "Yes. Plan datasets and identities per suite so the combined data stays understandable.")]),

    "guides/hashed-email-identity-aep.html": ([
        ("Normalise, then hash, in one shared place", "<p>Most failures come from small differences before hashing: trailing spaces, upper-case letters or different encodings. Agree one routine, trim, lower-case, then hash with the same algorithm, and publish it as a shared function or pipeline step that every source uses. Do not let each team write its own version.</p>"),
        ("Privacy and governance notes", "<ul><li>Hashing is not the same as anonymising. Treat hashed email as personal data and apply the same consent and retention rules as for the raw value.</li><li>Record which systems create the hash and which only receive it.</li><li>Apply the data usage labels your governance team requires before using the field in audiences or destinations.</li></ul>"),
        ("How to test the match", "<p>Take two test records for the same person in different datasets, ingest both, and confirm they appear on one profile. Then try an email with different capitalisation and confirm the hash still matches. Finish by testing a shared mailbox or test address to see how it affects the graph, since shared values can merge people who should stay separate. See " + IDS + ".</p>"),
    ], [("Is hashed email safe to share with partners?", "That depends on your contracts, consent and the partner's requirements. Check with your privacy team; hashing alone does not make sharing automatically acceptable."),
        ("What if some sources send raw email?", "Convert it to the agreed hash in your pipeline before ingestion so every dataset carries the same type of value.")]),

    "guides/validate-large-batch-ingestion.html": ([
        ("Set the acceptance criteria first", "<p>Agree before the load what counts as success: the maximum difference in record counts, the tolerated share of failed records, and which fields must never be empty. Write them down and have the data owner approve. Without that, validation turns into an argument after the fact.</p>"),
        ("What to record", "<ul><li>Source file names and row counts.</li><li>Batch identifiers and their status in the platform.</li><li>Counts and distinct-key counts from your queries.</li><li>Failed records, the reason and the fix applied.</li><li>Who signed off and when.</li></ul>"),
        ("If the numbers do not match", "<ol><li>Check for partial batches or batches that are still processing.</li><li>Look for duplicate keys across files, not only within one file.</li><li>Check schema validation errors for rejected rows.</li><li>Fix upstream, then reload in a controlled batch rather than patching the dataset by hand.</li></ol><p>More context is in the " + ING + " guide.</p>"),
    ], [("How soon can I validate after a load?", "Wait until the batch shows as successful in monitoring, then run your checks. Queries run on an unfinished batch give misleading counts."),
        ("Should I validate in a sandbox first?", "Yes where possible. A dry run in a non-production sandbox shows mapping and volume problems before they touch production data.")]),

    "guides/profile-merge-policies-unification.html": ([
        ("Choosing a merge policy", "<p>Two common approaches are to give precedence to particular datasets, which suits a trusted CRM that should override web behaviour, or to prefer the most recent timestamp, which suits attributes that change often. Pick the rule that matches how the business thinks about truth for each attribute, and write the reasoning into the design record.</p>"),
        ("Keep the profile clean", "<ul><li>Enable only datasets that serve an audience, journey or analysis need.</li><li>Test identities such as shared emails or placeholder IDs can link unrelated people, so review them before go-live.</li><li>Use a dedicated test sandbox with clearly labelled test profiles.</li><li>Document which merge policy each audience and destination uses.</li></ul>"),
        ("Review regularly", "<p>Revisit the policy when a new source is added or a dataset changes owner. See " + PRO + " and " + IDS + " for the underlying behaviour.</p>"),
    ], [("Does changing the merge policy rewrite stored data?", "No. A merge policy controls how data is combined when profiles are read or used; it does not delete the underlying records."),
        ("How do I find a collapsed profile?", "Look for profiles with an unusually large number of identities, then trace which shared value links them.")]),

    "guides/ajo-campaigns-vs-journeys.html": ([
        ("A quick way to choose", "<ul><li>One message, one audience, one send time: a campaign.</li><li>Several steps that depend on what a person does: a journey.</li><li>A message triggered by a single event with no follow-up: either works; choose the simpler one that your team can maintain.</li></ul>"),
        ("Operational differences to plan for", "<p>Campaigns are easy to schedule and review, so they suit regular broadcasts. Journeys need design time, testing of each branch, entry and exit rules and monitoring, because they run continuously. Before launch, check consent and frequency rules, test with seed profiles and agree who owns changes after go-live.</p>"),
        ("Where this fits", "<p>Read " + L("Adobe Journey Optimizer best practices", "guides/ajo-implementation-best-practices.html") + " for the delivery checklist and " + CAT + " if you want structured practice.</p>"),
    ], [("Can I convert a campaign into a journey later?", "They are separate objects, so you normally rebuild the logic in the new form. Plan for that if the use case may grow."),
        ("Which one is easier to test?", "A campaign has fewer paths, so testing is quicker. Journeys need a test for every branch and wait step.")]),
}
