"""Adobe Experience Platform (AEP) pillar + cluster pages.

Keyword source: seo-keyword-sitemap-50000.csv (all rows are cluster "AEP").
Each keyword = "adobe experience platform" + subtopic + modifier + "for" + audience + location.
Subtopics map 1:1 to the cluster pages below; modifiers map to sections inside them
(guide / step by step / best practices / examples / use cases / checklist / template ...),
career-type modifiers (career path, skills, salary, jobs, roles) map to career-path.html,
interview questions -> interview-questions.html, course/training/certification -> training/,
services/consultant/specialist -> services/aep-consulting.html.
"""

EL = "https://experienceleague.adobe.com/en/docs/experience-platform"

AUDIENCE_NOTE = (
    "<p>This guide is written for beginners, students and career switchers who want a clear "
    "mental model, and for developers, data engineers, implementation specialists, consultants, "
    "architects, marketers, agencies and enterprise teams who need practical, step-by-step "
    "detail they can apply on real projects.</p>"
)

AEP_PAGES = [
    # ------------------------------------------------------------------ PILLAR
    dict(
        path="adobe-experience-platform/index.html",
        nav="AEP Guides",
        title="AEP Guide: Adobe Experience Platform Architecture & Training",
        desc="Practical Adobe Experience Platform (AEP) guide: XDM schemas, datasets, ingestion, identity, profiles, segments and activation, with steps and training paths.",
        h1="Adobe Experience Platform (AEP): the complete practical guide",
        kicker="AEP knowledge hub",
        keywords=["adobe experience platform", "adobe experience platform guide", "adobe experience platform tutorial",
                  "adobe experience platform implementation", "adobe experience platform architecture",
                  "adobe experience platform training", "aep for beginners"],
        answer="Adobe Experience Platform (AEP) is Adobe's real-time customer data foundation. It standardises data with Experience Data Model (XDM) schemas, ingests batch and streaming data into datasets, stitches identities into Real-Time Customer Profiles, evaluates audiences, and activates them to destinations and Adobe applications such as Real-Time CDP, Journey Optimizer and Customer Journey Analytics.",
        schema="Article",
        sections=[
            ("How AEP fits together", """
<p>Most AEP implementations follow the same end-to-end flow. Understanding the order matters more than memorising every screen:</p>
<ol class="steps">
<li><strong>Model</strong> &mdash; design <a href="xdm-schemas.html">XDM schemas</a> for profiles and experience events.</li>
<li><strong>Store</strong> &mdash; create <a href="datasets.html">datasets</a> based on those schemas.</li>
<li><strong>Ingest</strong> &mdash; load data through <a href="data-ingestion.html">batch, streaming and source connectors</a>.</li>
<li><strong>Resolve</strong> &mdash; link identifiers with <a href="identity-service.html">Identity Service</a>.</li>
<li><strong>Unify</strong> &mdash; build <a href="real-time-customer-profile.html">Real-Time Customer Profiles</a> with merge policies.</li>
<li><strong>Segment</strong> &mdash; define <a href="segmentation-audiences.html">audiences</a> with batch, streaming or edge evaluation.</li>
<li><strong>Activate</strong> &mdash; send audiences to <a href="activation-destinations.html">destinations</a> and Adobe apps.</li>
</ol>
<p>Wrapping all of this is the platform <a href="architecture.html">architecture</a>: sandboxes, data governance, consent, APIs, Query Service and monitoring. The <a href="implementation-guide.html">implementation guide</a> turns these pieces into a delivery plan.</p>"""),
            ("Choose your learning path", """
<div class="grid-3">
<a class="card link-card" href="xdm-schemas.html"><h3>Beginner</h3><p>Start with schemas, datasets and ingestion to understand how data enters AEP.</p></a>
<a class="card link-card" href="implementation-guide.html"><h3>Implementation specialist</h3><p>Follow the step-by-step implementation checklist from use case to go-live.</p></a>
<a class="card link-card" href="architecture.html"><h3>Architect</h3><p>Design sandboxes, identity strategy, governance and integration patterns.</p></a>
<a class="card link-card" href="career-path.html"><h3>Career switcher</h3><p>See AEP roles, skills, certification options and a realistic roadmap.</p></a>
<a class="card link-card" href="interview-questions.html"><h3>Interview preparation</h3><p>Practise scenario-based AEP interview questions with model answers.</p></a>
<a class="card link-card" href="../services/aep-consulting.html"><h3>Enterprise team</h3><p>Get AEP consulting, architecture review and implementation support.</p></a>
</div>"""),
            ("AEP, Real-Time CDP, AJO and CJA: how they relate", """
<p>AEP is the shared data foundation. Applications are licensed on top of it:</p>
<ul>
<li><a href="../services/real-time-cdp.html">Real-Time CDP</a> uses AEP profiles and audiences for activation to marketing and advertising destinations.</li>
<li><a href="../services/adobe-journey-optimizer.html">Adobe Journey Optimizer (AJO)</a> uses profiles and events to orchestrate journeys and messages.</li>
<li><a href="../services/customer-journey-analytics.html">Customer Journey Analytics (CJA)</a> reports on AEP datasets across channels.</li>
</ul>
<p>Read the full comparison in <a href="../guides/aep-vs-real-time-cdp.html">AEP vs Real-Time CDP</a>.</p>"""),
            ("Who this hub is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("Is Adobe Experience Platform a CDP?", "AEP is the underlying data platform. The customer data platform capability is Real-Time CDP, an application built on AEP that adds audience activation to destinations."),
            ("How long does it take to learn AEP?", "With hands-on practice, most professionals can understand the core flow (schemas, datasets, ingestion, identity, profile, segments, activation) in a few weeks. Production-level architecture skills come from working through real use cases and troubleshooting."),
            ("Do I need coding skills for AEP?", "Not for the basics, which are UI-driven. Developers and data engineers benefit from JSON, REST APIs, SQL (for Query Service) and JavaScript (for Web SDK)."),
        ],
        sources=[("Adobe Experience Platform documentation", EL)],
        related=["services/aep-consulting.html", "training/index.html", "adobe-experience-platform/career-path.html"],
    ),
    # ------------------------------------------------------------------ SCHEMAS
    dict(
        path="adobe-experience-platform/xdm-schemas.html",
        title="AEP Schemas (XDM): Design Guide, Examples & Best Practices",
        desc="How to design Adobe Experience Platform XDM schemas: classes, field groups, identity fields, Profile enablement, examples and a design checklist.",
        h1="AEP schemas: designing XDM schemas step by step",
        kicker="AEP schemas",
        keywords=["adobe experience platform schemas", "aep xdm schema", "xdm schema design", "aep schemas best practices", "aep schemas examples", "aep schemas tutorial"],
        answer="An AEP schema is an Experience Data Model (XDM) definition of how data is structured. Each schema is built from a class (usually XDM Individual Profile for attributes or XDM ExperienceEvent for time-stamped events) plus field groups. Mark identity fields, choose a primary identity, and enable the schema for Profile only when the data should feed Real-Time Customer Profile.",
        schema="Article",
        sections=[
            ("Key concepts", """
<dl class="defs">
<dt>Class</dt><dd>Defines the behaviour of the data: record (profile attributes) or time-series (events).</dd>
<dt>Field group</dt><dd>A reusable set of fields added to a schema, either Adobe-provided or custom.</dd>
<dt>Data type</dt><dd>A reusable object structure (for example an address) used inside field groups.</dd>
<dt>Identity field</dt><dd>A field tagged with an identity namespace so Identity Service can link records.</dd>
<dt>Union schema</dt><dd>The combined view of all Profile-enabled schemas of the same class.</dd>
</dl>"""),
            ("Step-by-step: design a schema", """
<ol class="steps">
<li>Start from the business use case and list the attributes and events it needs.</li>
<li>Pick the class: XDM Individual Profile for CRM-style attributes, XDM ExperienceEvent for web, app, transaction and interaction events.</li>
<li>Reuse standard field groups first; create custom field groups under your tenant namespace only for what is missing.</li>
<li>Identify identity fields (email, CRM ID, ECID, phone) and set one primary identity per schema where required.</li>
<li>Review naming, types and required fields with data owners before creating datasets.</li>
<li>Enable for Profile only when you are sure &mdash; Profile-enabled schemas can only have additive changes afterwards.</li>
</ol>"""),
            ("Example: retail purchase event", """
<p>A purchase event schema typically uses the XDM ExperienceEvent class with the Commerce Details field group, an Environment Details field group for web context, and identity fields for ECID and a hashed customer ID. Order totals, product SKUs and quantities sit in standard commerce fields so that Customer Journey Analytics and Journey Optimizer can use them without custom mapping.</p>"""),
            ("Best practices checklist", """
<ul class="checklist">
<li>Design for use cases, not for every column in the source system.</li>
<li>Keep custom fields under one tenant object with consistent naming.</li>
<li>Avoid storing personal data you do not need; apply data usage labels.</li>
<li>Separate profile attributes from events &mdash; never put frequently changing events into profile records.</li>
<li>Version and document schemas; treat breaking changes as a new schema.</li>
<li>Validate sample payloads against the schema before production ingestion.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("Can I change a schema after enabling it for Profile?", "Only additive (non-breaking) changes are allowed once a schema is enabled for Profile and used. Removing or renaming fields requires a new schema."),
            ("What is the difference between a schema and a dataset?", "The schema defines structure; a dataset is the storage container that holds data conforming to one schema."),
        ],
        sources=[("XDM system overview", f"{EL}/xdm/home")],
        related=["adobe-experience-platform/datasets.html", "adobe-experience-platform/identity-service.html", "adobe-experience-platform/data-ingestion.html"],
    ),
    # ------------------------------------------------------------------ DATASETS
    dict(
        path="adobe-experience-platform/datasets.html",
        title="AEP Datasets: Setup, Profile Enablement & Best Practices",
        desc="Adobe Experience Platform datasets explained: schemas, enabling for Profile and Identity, monitoring ingestion and a troubleshooting checklist.",
        h1="AEP datasets: setup, enablement and troubleshooting",
        kicker="AEP datasets",
        keywords=["adobe experience platform datasets", "aep dataset", "aep datasets tutorial", "aep datasets best practices", "aep dataset profile enabled"],
        answer="An AEP dataset is a storage and management container for data that conforms to one XDM schema. Data lands in the data lake first; if the dataset is enabled for Profile and Identity, records also feed Real-Time Customer Profile and the identity graph. Datasets show batch status, errors and ingested record counts for monitoring.",
        schema="Article",
        sections=[
            ("Step by step: create and enable a dataset", """
<ol class="steps">
<li>Create the dataset from an existing <a href="xdm-schemas.html">schema</a>.</li>
<li>Decide whether it should feed Profile. Enable the schema first, then the dataset.</li>
<li>Ingest a small test batch or stream and check batch status and failed records.</li>
<li>Confirm profiles and identities appear as expected before loading full history.</li>
<li>Apply data usage labels for governance and set retention where available.</li>
</ol>"""),
            ("Common use cases", """
<ul>
<li>CRM profile attributes (Profile-enabled record dataset).</li>
<li>Web and app events collected with <a href="../services/web-sdk-adobe-tags.html">Web SDK</a> (Profile-enabled event dataset).</li>
<li>Historical or analytical data used only in Query Service or CJA (not Profile-enabled).</li>
</ul>"""),
            ("Troubleshooting checklist", """
<ul class="checklist">
<li>Batch failed: check the error preview for type mismatches and missing required fields.</li>
<li>Data in the dataset but not in profiles: confirm both schema and dataset are enabled for Profile and that records carry a valid primary identity.</li>
<li>Dataset missing in CJA: confirm it is added to a CJA connection with the correct person ID.</li>
<li>Unexpected volumes: review duplicate ingestion from multiple sources.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("Should every dataset be enabled for Profile?", "No. Enable only data that is needed for real-time profiles, segmentation or personalisation. Analytical or archival data can stay in the data lake."),
        ],
        sources=[("Datasets overview", f"{EL}/catalog/datasets/overview")],
        related=["adobe-experience-platform/xdm-schemas.html", "adobe-experience-platform/data-ingestion.html", "services/customer-journey-analytics.html"],
    ),
    # ------------------------------------------------------------------ INGESTION
    dict(
        path="adobe-experience-platform/data-ingestion.html",
        title="AEP Data Ingestion: Batch, Streaming & Source Connectors",
        desc="AEP data ingestion explained: batch vs streaming, source connectors, Data Prep mapping, Web SDK collection, validation and best practices.",
        h1="AEP data ingestion: batch, streaming and sources",
        kicker="AEP data ingestion",
        keywords=["adobe experience platform data ingestion", "aep data ingestion", "aep streaming ingestion", "aep batch ingestion", "aep source connectors", "aep data ingestion framework"],
        answer="AEP ingests data in two modes. Batch ingestion loads files or scheduled extracts through source connectors or the Batch Ingestion API. Streaming ingestion sends records in near real time through the HTTP API or the Edge Network via Web SDK and Mobile SDK. Data Prep maps and transforms incoming fields into the target XDM schema.",
        schema="Article",
        sections=[
            ("Batch vs streaming at a glance", """
<div class="table-wrap"><table>
<thead><tr><th>Aspect</th><th>Batch</th><th>Streaming</th></tr></thead>
<tbody>
<tr><td>Typical sources</td><td>Cloud storage, databases, CRM extracts</td><td>Web, mobile, server events, HTTP API</td></tr>
<tr><td>Latency</td><td>Scheduled</td><td>Near real time</td></tr>
<tr><td>Best for</td><td>History, profile attributes, large volumes</td><td>Behavioural events, triggers for journeys</td></tr>
</tbody></table></div>"""),
            ("Step-by-step ingestion framework", """
<ol class="steps">
<li>Confirm the target <a href="xdm-schemas.html">schema</a> and <a href="datasets.html">dataset</a>.</li>
<li>Choose the source connector or API and configure authentication securely.</li>
<li>Map source fields to XDM with Data Prep; add calculated fields where needed.</li>
<li>Run a sample load and review errors and partial-ingestion thresholds.</li>
<li>Schedule the dataflow and set up monitoring and alerts.</li>
<li>Reconcile record counts with the source system before go-live.</li>
</ol>"""),
            ("Best practices", """
<ul class="checklist">
<li>Send only the fields your use cases need.</li>
<li>Keep identity values clean and consistently formatted (for example lowercase, trimmed, hashed where required).</li>
<li>Use streaming only for data that needs real-time action.</li>
<li>Document every dataflow owner, schedule and dependency.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("What is Data Prep in AEP?", "Data Prep maps, transforms and validates source fields into XDM fields during ingestion, using mapping rules and calculated fields."),
            ("Is Web SDK a form of streaming ingestion?", "Yes. Web SDK sends events to the Adobe Edge Network, which forwards them through a datastream into AEP datasets in near real time."),
        ],
        sources=[("Data ingestion overview", f"{EL}/ingestion/home")],
        related=["adobe-experience-platform/datasets.html", "services/web-sdk-adobe-tags.html", "services/data-engineering.html"],
    ),
    # ------------------------------------------------------------------ IDENTITY
    dict(
        path="adobe-experience-platform/identity-service.html",
        title="AEP Identity Resolution: Namespaces, Graphs & Best Practices",
        desc="How identity resolution works in Adobe Experience Platform: namespaces, primary identity, identity graphs, graph collapse and a strategy checklist.",
        h1="AEP identity: how identity resolution works",
        kicker="AEP identity",
        keywords=["adobe experience platform identity", "aep identity service", "aep identity resolution", "aep identity namespaces", "aep identity graph", "identity resolution best practices"],
        answer="AEP Identity Service links identifiers that belong to the same person into an identity graph. Each identifier is tagged with a namespace such as ECID, Email, Phone or a custom CRM ID. When records sharing an identifier are ingested into Profile-enabled datasets, their identities are linked, allowing Real-Time Customer Profile to merge fragments into one view.",
        schema="Article",
        sections=[
            ("Core concepts", """
<dl class="defs">
<dt>Identity namespace</dt><dd>The context of an identifier, for example Email or CRM ID. Custom namespaces can be created.</dd>
<dt>Primary identity</dt><dd>The identifier used to store a record's profile fragment.</dd>
<dt>Identity graph</dt><dd>The set of linked identities for one person.</dd>
</dl>"""),
            ("Designing an identity strategy step by step", """
<ol class="steps">
<li>Inventory every identifier in each source and how reliably it identifies a person.</li>
<li>Rank identifiers by uniqueness (for example CRM ID above email above device IDs).</li>
<li>Decide which identifiers should link profiles and which should not.</li>
<li>Exclude shared or low-quality values (shared devices, placeholder emails, test data).</li>
<li>Test graphs with real sample data in a development sandbox before production.</li>
</ol>"""),
            ("Common identity problems", """
<ul class="checklist">
<li><strong>Graph collapse:</strong> a shared identifier (such as a call-centre phone number) links many people into one graph.</li>
<li><strong>Missing links:</strong> authenticated events do not carry the CRM ID, so known and anonymous activity never join.</li>
<li><strong>Format mismatch:</strong> the same email arrives in different cases or hashing formats.</li>
</ul>
<p>Review the current Adobe documentation for identity graph linking rules and limits before you design production graphs, as these capabilities evolve.</p>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("What is ECID?", "The Experience Cloud ID is Adobe's device/browser identifier set by Web SDK and Mobile SDK. It is usually linked to known identifiers after login."),
            ("Can identity graphs merge the wrong people?", "Yes, if shared or low-quality identifiers are allowed to link profiles. A deliberate identity strategy and testing prevent this."),
        ],
        sources=[("Identity Service overview", f"{EL}/identity/home")],
        related=["adobe-experience-platform/real-time-customer-profile.html", "adobe-experience-platform/xdm-schemas.html", "services/real-time-cdp.html"],
    ),
    # ------------------------------------------------------------------ PROFILES
    dict(
        path="adobe-experience-platform/real-time-customer-profile.html",
        title="AEP Real-Time Customer Profile & Merge Policies Explained",
        desc="AEP profiles explained: Real-Time Customer Profile, profile fragments, merge policies, Customer 360 use cases and best practices.",
        h1="AEP profiles: Real-Time Customer Profile explained",
        kicker="AEP profiles",
        keywords=["adobe experience platform profiles", "aep real-time customer profile", "aep merge policies", "customer 360 aep", "aep profiles best practices"],
        answer="Real-Time Customer Profile merges profile fragments from Profile-enabled datasets into one view per person, using the identity graph to decide which fragments belong together and a merge policy to decide which values win. Profiles combine attributes and behavioural events and are used for segmentation, personalisation and activation.",
        schema="Article",
        sections=[
            ("How a profile is built", """
<ol class="steps">
<li>Records arrive in Profile-enabled <a href="datasets.html">datasets</a> as fragments keyed by their primary identity.</li>
<li><a href="identity-service.html">Identity Service</a> links the identities across fragments.</li>
<li>A merge policy combines the fragments at read time into a single profile.</li>
</ol>"""),
            ("Merge policies", """
<p>Merge policies define how conflicting attribute values are resolved, for example by timestamp (most recent value wins) or by dataset precedence (a trusted source such as CRM wins). Each audience and destination uses a merge policy, so choose and document a default policy deliberately.</p>"""),
            ("Customer 360 use cases", """
<ul>
<li>Unified view for service agents and personalisation.</li>
<li>Real-time audiences for <a href="../services/adobe-journey-optimizer.html">Journey Optimizer</a> triggers.</li>
<li>Suppression of recent purchasers from paid media through <a href="activation-destinations.html">destinations</a>.</li>
</ul>"""),
            ("Best practices", """
<ul class="checklist">
<li>Profile-enable only data needed for real-time use cases.</li>
<li>Monitor profile counts and fragment distribution for unexpected growth.</li>
<li>Apply experience event expiration where appropriate to control volume.</li>
<li>Validate sample profiles end to end before launching audiences.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("What is a profile fragment?", "A fragment is the portion of a person's data stored under one primary identity in one dataset. The profile is the merged view of all linked fragments."),
        ],
        sources=[("Real-Time Customer Profile overview", f"{EL}/profile/home")],
        related=["adobe-experience-platform/identity-service.html", "adobe-experience-platform/segmentation-audiences.html", "services/real-time-cdp.html"],
    ),
    # ------------------------------------------------------------------ SEGMENTS
    dict(
        path="adobe-experience-platform/segmentation-audiences.html",
        title="AEP Segments & Audiences: Batch, Streaming & Edge Guide",
        desc="Adobe Experience Platform segmentation: audiences, batch vs streaming vs edge evaluation, examples, validation steps and best practices.",
        h1="AEP segments and audiences: a practical guide",
        kicker="AEP segments",
        keywords=["adobe experience platform segments", "aep segmentation", "aep audiences", "aep streaming segmentation", "aep edge segmentation", "aep segment examples"],
        answer="AEP segmentation evaluates Real-Time Customer Profiles against rules to build audiences. Batch evaluation runs on a schedule for complex rules; streaming evaluation updates qualification as events arrive; edge evaluation qualifies profiles instantly on the Edge Network for same-page personalisation. Audiences can also be imported or created from other sources.",
        schema="Article",
        sections=[
            ("Choosing an evaluation method", """
<div class="table-wrap"><table>
<thead><tr><th>Method</th><th>Speed</th><th>Typical use</th></tr></thead>
<tbody>
<tr><td>Batch</td><td>Scheduled</td><td>Complex rules, large lookbacks, daily campaigns</td></tr>
<tr><td>Streaming</td><td>Near real time</td><td>Event-triggered journeys and fast suppression</td></tr>
<tr><td>Edge</td><td>Instant</td><td>Same-page or next-page personalisation</td></tr>
</tbody></table></div>
<p>Each method supports different rule types; check the current Adobe eligibility rules before relying on streaming or edge evaluation.</p>"""),
            ("Examples", """
<ul>
<li>High-value customers: lifetime spend above a threshold and purchase in the last 90 days.</li>
<li>Cart abandoners: added to cart, no purchase within 1 hour (streaming).</li>
<li>Loyalty members browsing a category this session (edge).</li>
</ul>"""),
            ("Step-by-step validation", """
<ol class="steps">
<li>Write the business definition in plain language first.</li>
<li>Build the rule and check the estimated audience size.</li>
<li>Inspect sample qualified profiles to confirm the logic.</li>
<li>Check the merge policy and identity behaviour behind the audience.</li>
<li>Monitor qualification counts after activation.</li>
</ol>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("Why is my audience size different from what I expected?", "Common causes are the merge policy, identity linking, event lookback windows, and whether the rule is evaluated in batch or streaming."),
        ],
        sources=[("Segmentation Service overview", f"{EL}/segmentation/home")],
        related=["adobe-experience-platform/real-time-customer-profile.html", "adobe-experience-platform/activation-destinations.html", "services/adobe-journey-optimizer.html"],
    ),
    # ------------------------------------------------------------------ ACTIVATION
    dict(
        path="adobe-experience-platform/activation-destinations.html",
        title="AEP Activation & Destinations: Send Audiences to Channels",
        desc="How AEP activation works: streaming and batch destinations, mapping, governance and consent checks, and an activation QA checklist.",
        h1="AEP activation: sending audiences to destinations",
        kicker="AEP activation",
        keywords=["adobe experience platform activation", "aep destinations", "aep activation tutorial", "rtcdp activation", "aep activation best practices"],
        answer="Activation sends AEP audiences and selected profile attributes to destinations such as advertising platforms, email and CRM systems, cloud storage and Adobe applications. Streaming destinations update as profiles qualify; batch (file-based) destinations export on a schedule. Data governance policies and consent are enforced before export.",
        schema="Article",
        sections=[
            ("Step-by-step activation", """
<ol class="steps">
<li>Connect the destination with the right account and permissions.</li>
<li>Select audiences and choose the identity and attributes to send.</li>
<li>Review data usage labels and marketing actions to avoid policy violations.</li>
<li>Schedule exports (batch) or confirm streaming behaviour.</li>
<li>Validate match rates and counts in the receiving platform.</li>
</ol>"""),
            ("Activation QA checklist", """
<ul class="checklist">
<li>Only consented profiles are exported.</li>
<li>Hashed identifiers use the format the destination expects.</li>
<li>Audience counts reconcile between AEP and the destination.</li>
<li>Owners are defined for each destination dataflow.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("Is activation part of AEP or Real-Time CDP?", "Destination activation is a Real-Time CDP capability built on AEP. Availability depends on your Adobe licensing."),
        ],
        sources=[("Destinations overview", f"{EL}/destinations/home")],
        related=["adobe-experience-platform/segmentation-audiences.html", "services/real-time-cdp.html", "guides/aep-vs-real-time-cdp.html"],
    ),
    # ------------------------------------------------------------------ ARCHITECTURE
    dict(
        path="adobe-experience-platform/architecture.html",
        title="AEP Architecture Best Practices: Sandboxes & Governance",
        desc="Adobe Experience Platform architecture for architects: reference model, sandboxes, governance, consent, APIs and enterprise integration patterns.",
        h1="AEP architecture: an enterprise reference model",
        kicker="AEP architecture",
        keywords=["adobe experience platform architecture", "aep architecture best practices", "aep reference architecture", "aep enterprise architecture", "aep architect"],
        answer="A sound AEP architecture separates environments with sandboxes, defines a single identity strategy, models data in XDM around use cases, enforces governance with data usage labels and consent, and integrates sources and destinations through monitored dataflows and APIs. It is documented so that every dataset, audience and destination has an owner.",
        schema="Article",
        sections=[
            ("Reference architecture layers", """
<ol class="steps">
<li><strong>Collection</strong> &mdash; Web SDK, Mobile SDK, server APIs and source connectors.</li>
<li><strong>Foundation</strong> &mdash; XDM schemas, datasets, Identity Service, Real-Time Customer Profile.</li>
<li><strong>Intelligence</strong> &mdash; segmentation, Query Service and analytics in CJA.</li>
<li><strong>Activation</strong> &mdash; Real-Time CDP destinations, Journey Optimizer, Target and partner tools.</li>
<li><strong>Governance</strong> &mdash; sandboxes, roles, labels, policies, consent and monitoring.</li>
</ol>"""),
            ("Architecture best practices", """
<ul class="checklist">
<li>Use development and production sandboxes with a promotion process.</li>
<li>Agree the identity strategy before building schemas.</li>
<li>Apply least-privilege access and audit changes.</li>
<li>Design for consent from the start rather than retrofitting it.</li>
<li>Plan capacity: profile counts, event volumes and audience limits.</li>
<li>Keep secrets for APIs in a secure vault; never in code or tag managers.</li>
</ul>"""),
            ("Enterprise integration patterns", """
<p>Common patterns include CRM-to-AEP batch syncs, event streaming from Kafka or cloud pub/sub into the streaming API, warehouse integration with Snowflake, BigQuery or Databricks, and server-to-server event forwarding. See <a href="../services/data-engineering.html">data engineering</a> for pipeline design.</p>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("How many sandboxes should we use?", "At minimum one production and one development sandbox. Larger programmes add sandboxes for testing, regions or business units, depending on licensing."),
        ],
        sources=[("Sandboxes overview", f"{EL}/sandbox/home"), ("Data Governance overview", f"{EL}/data-governance/home")],
        related=["adobe-experience-platform/implementation-guide.html", "services/aep-consulting.html", "services/martech-strategy-advisory.html"],
    ),
    # ------------------------------------------------------------------ IMPLEMENTATION
    dict(
        path="adobe-experience-platform/implementation-guide.html",
        title="AEP Implementation Guide: End-to-End Steps & Checklist",
        desc="End-to-end Adobe Experience Platform implementation guide: phases, step-by-step checklist, project roles, timeline factors and common risks.",
        h1="AEP implementation: an end-to-end guide",
        kicker="AEP implementation",
        keywords=["adobe experience platform implementation", "aep implementation guide", "aep implementation checklist", "aep implementation step by step", "aep implementation project", "aep end to end implementation"],
        answer="An Adobe Experience Platform implementation moves from prioritised use cases to data model, identity strategy, ingestion, profile and audiences, activation, and finally QA and go-live. Successful projects deliver one end-to-end use case first, prove data quality, then scale to more sources and channels.",
        schema="HowTo",
        steps=[
            ("Prioritise use cases", "Agree 2–3 measurable use cases with business owners and define success metrics."),
            ("Design data and identity", "Create the XDM model and identity strategy needed for those use cases only."),
            ("Set up ingestion", "Configure sources, Data Prep mappings and Web SDK collection in a development sandbox."),
            ("Build profiles and audiences", "Enable datasets for Profile, choose merge policies and build validated audiences."),
            ("Activate", "Connect destinations or Journey Optimizer and validate counts and consent."),
            ("Test and go live", "Run end-to-end QA, promote to production, and set up monitoring and ownership."),
        ],
        sections=[
            ("Implementation checklist", """
<ul class="checklist">
<li>Use cases, KPIs and owners documented.</li>
<li>Source inventory with data quality assessment.</li>
<li>Schemas reviewed; identity namespaces created.</li>
<li>Consent and governance labels applied.</li>
<li>Sample data validated in profiles before full loads.</li>
<li>Audience definitions signed off by marketing.</li>
<li>Monitoring, alerting and runbooks in place.</li>
</ul>"""),
            ("Project roles", """
<p>Typical roles are a solution architect, data engineer, implementation specialist (Web SDK and Tags), marketing technologist for audiences and journeys, and a business owner. Smaller teams combine roles; enterprise teams add data governance and QA leads.</p>"""),
            ("Common risks", """
<ul>
<li>Starting with every data source instead of one use case.</li>
<li>Identity decisions made late, causing rework.</li>
<li>No owner for data quality after go-live.</li>
</ul>"""),
            ("Who this guide is for", AUDIENCE_NOTE),
        ],
        faqs=[
            ("How long does an AEP implementation take?", "It depends on scope, data readiness and licensing. A focused first use case is usually planned in weeks to a few months; enterprise roll-outs continue in phases."),
        ],
        sources=[("Adobe Experience Platform documentation", EL)],
        related=["adobe-experience-platform/architecture.html", "services/aep-consulting.html", "training/index.html"],
    ),
    # ------------------------------------------------------------------ INTERVIEW
    dict(
        path="adobe-experience-platform/interview-questions.html",
        title="AEP Interview Questions & Answers for Developers & Architects",
        desc="Adobe Experience Platform interview questions with model answers for developers, consultants, implementation specialists and architects.",
        h1="AEP interview questions and answers",
        kicker="AEP interview preparation",
        keywords=["adobe experience platform interview questions", "aep interview questions", "aep architect interview questions", "aep developer interview questions", "rtcdp interview questions"],
        answer="Strong AEP interview answers explain the end-to-end data flow, justify design decisions and show how you would troubleshoot. Expect questions on XDM schemas, datasets, ingestion, identity, profiles and merge policies, segmentation methods, activation, governance and how AEP connects to Real-Time CDP, AJO and CJA.",
        schema="Article",
        sections=[
            ("Foundation questions", """
<details class="qa"><summary>What is the difference between the XDM Individual Profile and XDM ExperienceEvent classes?</summary><p>Individual Profile is a record class for attributes that describe a person; ExperienceEvent is a time-series class for time-stamped interactions. Choosing correctly affects storage, segmentation and analytics.</p></details>
<details class="qa"><summary>Why would data be in a dataset but not in the profile?</summary><p>The schema or dataset may not be enabled for Profile, the record may lack a valid primary identity, or ingestion may have partially failed.</p></details>
<details class="qa"><summary>What does a merge policy do?</summary><p>It decides how fragments are combined and which value wins when attributes conflict, using timestamp order or dataset precedence.</p></details>"""),
            ("Scenario questions for architects and consultants", """
<details class="qa"><summary>Profiles are merging different customers together. How do you investigate?</summary><p>Inspect the identity graph for shared identifiers (shared phone numbers, placeholder emails, shared devices), review which namespaces are allowed to link, clean source data and adjust the identity strategy, then validate in a development sandbox.</p></details>
<details class="qa"><summary>A streaming audience is not triggering a journey. Where do you look?</summary><p>Trace the path: event schema and datastream, dataset ingestion, profile update, streaming eligibility of the rule, the journey's audience or event configuration, and consent.</p></details>
<details class="qa"><summary>How would you design an AEP implementation for a bank?</summary><p>Start from prioritised use cases, define a strict identity strategy around the customer ID, apply governance labels to sensitive attributes, separate sandboxes, and phase sources and channels.</p></details>"""),
            ("Developer questions", """
<details class="qa"><summary>How does Web SDK send data to AEP?</summary><p>Web SDK sends events to the Edge Network; a datastream routes them to AEP datasets and other Adobe services.</p></details>
<details class="qa"><summary>How would you validate an ingestion pipeline?</summary><p>Validate sample payloads against the schema, check batch errors, reconcile counts with the source and inspect resulting profiles.</p></details>"""),
            ("How to prepare", """<p>Practise explaining one end-to-end project out loud, from use case to activation. Our <a href="../training/index.html">career accelerator</a> includes mock architecture scenarios, and the <a href="career-path.html">AEP career path</a> explains which roles ask which questions.</p>"""),
        ],
        faqs=[
            ("Which AEP topics come up most in interviews?", "Identity resolution, profile and merge policies, segmentation methods, ingestion troubleshooting and how AEP supports RTCDP, AJO and CJA."),
        ],
        sources=[("Adobe Experience Platform documentation", EL)],
        related=["adobe-experience-platform/career-path.html", "training/index.html", "adobe-experience-platform/identity-service.html"],
    ),
    # ------------------------------------------------------------------ CAREER
    dict(
        path="adobe-experience-platform/career-path.html",
        title="AEP Career Path: Roles, Skills, Jobs, Certification & Salary",
        desc="Adobe Experience Platform career path: developer, engineer, consultant and architect roles, key skills, certification and what drives salary.",
        h1="AEP career path: roles, skills and roadmap",
        kicker="AEP careers",
        keywords=["adobe experience platform career path", "aep jobs", "aep skills", "aep salary", "aep developer", "aep architect", "aep consultant", "aep certification", "aep roadmap"],
        answer="Common Adobe Experience Platform career paths are implementation specialist, AEP developer or data engineer, AEP consultant, and AEP solution architect. Each builds on the same core skills: XDM data modelling, ingestion, identity, profiles, segmentation, activation and governance, plus adjacent skills such as SQL, APIs, Web SDK, AJO and CJA.",
        schema="Article",
        sections=[
            ("AEP roles compared", """
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>Focus</th><th>Key skills</th></tr></thead>
<tbody>
<tr><td>Implementation specialist</td><td>Configuring AEP and data collection</td><td>Schemas, datasets, Web SDK, Tags, QA</td></tr>
<tr><td>AEP developer / data engineer</td><td>Pipelines and integrations</td><td>APIs, SQL, Python, ETL, streaming</td></tr>
<tr><td>AEP consultant</td><td>Use cases and delivery</td><td>Business analysis, audiences, AJO, CJA</td></tr>
<tr><td>Solution architect</td><td>End-to-end design and governance</td><td>Identity strategy, architecture, security</td></tr>
</tbody></table></div>"""),
            ("A realistic learning roadmap", """
<ol class="steps">
<li>Learn the AEP data flow and XDM modelling.</li>
<li>Build a hands-on project: ingest sample data, build profiles and an audience.</li>
<li>Add Web SDK collection and a CJA report or AJO journey.</li>
<li>Study governance, consent and identity edge cases.</li>
<li>Prepare a portfolio story and practise <a href="interview-questions.html">interview questions</a>.</li>
<li>Consider Adobe certification relevant to your target role.</li>
</ol>"""),
            ("What affects AEP salaries and job demand", """
<p>Salaries for AEP roles vary widely by country and city, years of experience, depth of hands-on implementation work, adjacent skills (AJO, CJA, data engineering) and whether the role is consulting, client-side or contract. We do not publish salary figures; check current listings on job boards and salary surveys for your market.</p>"""),
            ("Who this guide is for", "<p>Students, beginners, career switchers and working professionals &mdash; marketers, developers, data engineers and consultants &mdash; planning a move into Adobe Experience Platform roles, whether in India or internationally.</p>"),
        ],
        faqs=[
            ("Is AEP a good career choice?", "AEP skills are specialised and used by enterprises running Adobe Experience Cloud. Demand varies by market, so research current job listings in your region."),
            ("Do I need certification to get an AEP job?", "Certification can help show baseline knowledge, but employers usually value hands-on project experience and the ability to explain design decisions."),
        ],
        sources=[("Adobe Experience League", "https://experienceleague.adobe.com/")],
        related=["training/index.html", "adobe-experience-platform/interview-questions.html", "adobe-experience-platform/index.html"],
    ),
]
