"""Pages built from the Infiante360 company brochure (28 Nov 2026): capabilities, delivery approach, AEP training.
Brochure themes only (pillars, Discover/Design/Build/Optimize, AEP topics). No client names, results, partner status or learner counts."""
from content_academy import course_page

CAP = dict(
    path="capabilities.html", nav="Capabilities", bands=True,
    title="Infiante360 Capabilities: MarTech Consulting and Academy",
    desc="Enterprise MarTech consulting, a hands-on Tech Academy, corporate enablement and research from Infiante360. See what we do and how to start.",
    h1="Infiante360 capabilities: consulting, learning and enablement",
    kicker="Business Consulting & Tech Academy",
    keywords=["enterprise martech consulting", "martech capability building", "adobe experience cloud consulting", "corporate martech training", "agentic ai consulting"],
    answer="Infiante360 Business Consulting & Tech Academy combines enterprise MarTech consulting with hands-on learning. We work on architecture, implementation strategy and optimisation for Adobe Experience Cloud, customer data and Agentic AI, and we build team capability through role-based training, mentoring and practice labs. Start with the challenge you want to solve.",
    schema="WebPage", hero_cta=("Book a discovery call", "https://infiante360techacademy.com/lp/enterprise-martech-demo.html"),
    sections=[
        ("Four ways we help", '<div class="grid-2">'
         '<div class="card"><h3>Business consulting</h3><p>Architecture review, implementation strategy, use-case design, capability building and optimisation for enterprise MarTech, customer 360, data engineering and digital transformation. See <a href="services/">our services</a>.</p></div>'
         '<div class="card"><h3>Tech Academy</h3><p>Hands-on learning, mentoring and career readiness for professionals moving into Adobe MarTech and Agentic AI. See the <a href="academy/catalogue.html">course catalogue</a> and <a href="academy/pricing.html">fees</a>.</p></div>'
         '<div class="card"><h3>Corporate enablement</h3><p>Role-based learning aligned to your organisation: tailored curriculum, hands-on labs, real use cases and assessments. See <a href="training/corporate-training.html">corporate training</a>.</p></div>'
         '<div class="card"><h3>Research and intelligence</h3><p>Technical insights and architecture-led exploration, such as <a href="research/index.html">our research articles</a>.</p></div></div>', "plain", "Overview"),
        ("Topics we work on", '<ul class="checklist cols-2"><li>Adobe Experience Platform and Real-Time CDP</li><li>Adobe Journey Optimizer</li><li>Customer Journey Analytics and Adobe Analytics</li><li>Web SDK and Adobe Tags</li><li>Customer 360 and identity resolution</li><li>Data engineering for customer data</li><li>Agentic AI and MCP for MarTech</li><li>Digital transformation roadmaps</li></ul>', "alt", "Scope"),
        ("How an engagement starts", '<ol><li>Tell us the business challenge, not the product you think you need.</li><li>We hold a discovery conversation to understand goals, current capability and constraints.</li><li>We propose an engagement, such as an architecture review, a delivery plan or a tailored training programme.</li><li>We agree scope, owners and success measures in writing before work begins.</li></ol><p>Read the <a href="services/delivery-approach.html">delivery approach</a> for the four phases.</p>', "plain", "Start"),
        ("Choose your path", '<div class="grid-3"><a class="card link-card" href="lp/aep-architecture-review.html"><h3>Enterprise teams</h3><p>Request an AEP architecture review.</p></a><a class="card link-card" href="lp/corporate-adobe-training.html"><h3>Training leads</h3><p>Request a corporate training proposal.</p></a><a class="card link-card" href="lp/batches.html"><h3>Individuals</h3><p>Register for a live batch.</p></a></div>', "alt", "Next step"),
    ],
    faqs=[("Is Infiante360 an Adobe partner?", "We do not claim any Adobe partner status. Adobe product names are trademarks of Adobe, and Infiante360 is independent."),
          ("Do you work with individuals and companies?", "Yes. Professionals join the Tech Academy, and organisations can ask for consulting or corporate enablement.")],
    related=["services/", "academy/index.html", "training/corporate-training.html"],
)

DELIVERY = dict(
    path="services/delivery-approach.html", nav="Delivery approach", bands=True,
    title="Enterprise MarTech Delivery Approach: Discover to Optimize",
    desc="Our four-phase approach to enterprise MarTech work: discover goals, design the architecture, build the plan and capability, then optimise continuously.",
    h1="Enterprise MarTech delivery approach: discover, design, build, optimize",
    kicker="Services · How we work",
    keywords=["martech delivery approach", "enterprise martech implementation approach", "adobe experience platform implementation phases", "martech architecture roadmap", "digital transformation consulting approach"],
    answer="Our enterprise MarTech approach has four phases. Discover goals, current capability and constraints. Design the target architecture, use cases and governance. Build the implementation plan, integrations and team capability. Optimize by reviewing outcomes, finding gaps and improving continuously. Each phase has named outputs and owners so progress can be reviewed.",
    schema="Service", hero_cta=("Request an architecture review", "https://infiante360techacademy.com/lp/aep-architecture-review.html"),
    sections=[
        ("Phase 1: Discover", '<p>Understand business goals, the current stack, data sources, team skills and constraints such as consent, security and budget.</p><ul><li>Stakeholder interviews and goal definition.</li><li>Inventory of systems, data and identifiers.</li><li>Gap list and early risks.</li></ul>', "plain", "Discover"),
        ("Phase 2: Design", '<p>Define the target architecture, the use cases it must support and the governance around it.</p><ul><li>Reference architecture and integration patterns.</li><li>Data model and identity design (see <a href="../adobe-experience-platform/xdm-schemas.html">XDM schemas</a> and <a href="../adobe-experience-platform/identity-service.html">Identity Service</a>).</li><li>Prioritised use cases and a dependency backlog.</li></ul>', "alt", "Design"),
        ("Phase 3: Build", '<p>Plan implementation, integrations and capability development so the team can run what is built.</p><ul><li>Implementation plan and sequencing, as in the <a href="../adobe-experience-platform/implementation-guide.html">AEP implementation guide</a>.</li><li>Integration and data-ingestion design.</li><li>Role-based training and hands-on labs for the delivery team.</li></ul>', "plain", "Build"),
        ("Phase 4: Optimize", '<p>Review outcomes against the measures agreed at the start, identify gaps and improve continuously.</p><ul><li>Measurement review and data-quality checks.</li><li>Backlog refresh and governance review.</li><li>Capability assessment and next-phase planning.</li></ul>', "alt", "Optimize"),
        ("What you receive", '<ul class="checklist"><li>Written findings and a prioritised recommendation set.</li><li>Architecture and data-model documents your team can reuse.</li><li>A dependency-based backlog.</li><li>Named owners and review points.</li></ul><p>Outcomes depend on your data, team and decisions. We do not promise results in advance.</p>', "plain", "Outputs"),
        ("Where to go next", '<p>See <a href="../capabilities.html">all capabilities</a>, <a href="martech-strategy-advisory.html">MarTech strategy advisory</a> or <a href="engagement-model.html">engagement models</a>.</p>', "alt", "Next step"),
    ],
    faqs=[("How long does each phase take?", "It depends on scope and team availability. We agree timings per engagement after discovery."),
          ("Can we start at the Design or Build phase?", "Yes, if discovery work already exists. We review it first so the design rests on accurate facts.")],
    related=["services/engagement-model.html", "services/martech-strategy-advisory.html", "capabilities.html"],
)

AEP_COURSE = course_page(
    "academy/courses/aep-training.html", "Adobe Experience Platform", "AEP",
    "AEP Training: Adobe Experience Platform Course | Infiante360",
    "Adobe Experience Platform training: XDM schemas, ingestion, identity, Real-Time Customer Profile, segmentation, activation and governance, with projects.",
    ["aep training", "adobe experience platform course", "aep course online", "xdm schema training", "real-time customer profile course"],
    "Adobe Experience Platform training teaches how raw data becomes intelligent experiences. You learn XDM schema design, ingestion, identity and the identity graph, Real-Time Customer Profile, segmentation, activation and governance, and practise each step in hands-on projects built around realistic enterprise scenarios.",
    [("Data model and ingestion", ["XDM schemas, classes and field groups", "Datasets and how they link to schemas", "Batch, streaming and source connections"]),
     ("Identity and profile", ["Identity namespaces and the identity graph", "Primary and secondary identities", "Real-Time Customer Profile and merge policies"]),
     ("Audiences and activation", ["Segmentation and audience design", "Destinations and activation", "Using the APIs for common tasks"]),
     ("Governance and delivery", ["Data usage labels, consent and access control", "Validation and troubleshooting", "Planning an implementation backlog"])],
    [("Schema and dataset build", "Design an XDM schema, create datasets and ingest sample data."),
     ("Identity and profile exercise", "Configure identities and check how profiles stitch across datasets.")],
    ["Basic data concepts such as tables, JSON and identifiers", "A laptop and a stable internet connection", "No prior Adobe experience required for the foundations path"],
    [("adobe-experience-platform/", "AEP guides"), ("adobe-experience-platform/xdm-schemas.html", "XDM schemas"), ("adobe-experience-platform/identity-service.html", "Identity Service"), ("adobe-experience-platform/architecture.html", "AEP architecture")],
    [("Is this course the same as the Career Accelerator?", "No. This is a focused single-tool path. The Career Accelerator covers more tools and includes a larger project."),
     ("Do you provide a certification?", "We do not promise certification outcomes. The course supports your own exam preparation.")],
)

BROCHURE_ALL = [CAP, DELIVERY, AEP_COURSE]
