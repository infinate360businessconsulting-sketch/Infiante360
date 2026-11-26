"""Practice hub: one page that links the hands-on resources that already exist (simulators, quiz, handout, labs and workbooks in guides, test series on the LMS).
Original text. Claims only what is already published elsewhere on the site; no sandboxes, badges or graded-mission claims."""
PRACTICE_PAGE = dict(
    path="academy/practice.html", nav="Practice hub",
    title="Hands-On Practice Hub: Simulators, Labs and Quizzes",
    desc="Practise Adobe MarTech skills with Infiante360 simulators, lab guides, a banking quiz, a journey handout and a test series. Pick the exercise that fits you.",
    h1="Hands-on practice hub", kicker="Practice",
    keywords=["adobe martech practice", "aep hands-on labs", "aep practice exercises", "martech simulators", "adobe test series"],
    schema="WebPage", category="Academy",
    answer="Practice is how Adobe MarTech skills stick. This hub collects what Infiante360 Tech Academy offers today: simulators for enterprise scenarios, lab and workbook guides, a banking quiz, a journey best-practice handout, interview questions and a test series on the learning platform. Pick the exercise that matches your level. No placement, credential or exam result is promised.",
    sections=[
        ("Simulators", '<p>Work through enterprise scenarios in banking, airline, hospitality, insurance and telecom, from schema design to journeys. <a href="simulators.html">Open the simulators page</a>.</p>'),
        ("Lab and workbook guides", '<ul class="checklist"><li><a href="../guides/identity-graph-collapse-test-lab.html">Identity graph collapse test lab</a></li><li><a href="../guides/snowflake-incremental-load-lab.html">Snowflake incremental load lab</a></li><li><a href="../guides/cja-backfill-reconciliation-workbook.html">CJA backfill reconciliation workbook</a></li><li><a href="../guides/aep-batch-ingestion-failure-diagnostic.html">Batch ingestion failure diagnostic</a></li><li><a href="../guides/web-sdk-troubleshooting.html">Web SDK troubleshooting</a></li></ul>'),
        ("Quiz, handout and interview questions", '<ul class="checklist"><li><a href="aep-bfsi-quiz.html">AEP banking quiz</a></li><li><a href="ajo-best-practices-handout.html">Journey Optimizer best-practices handout</a></li><li><a href="../adobe-experience-platform/interview-questions.html">AEP interview questions</a></li></ul>'),
        ("Test series and learning platform", '<p>Our learning platform hosts the test series and course materials: <a href="https://techacademy.infinate360.in/" rel="noopener" target="_blank">techacademy.infinate360.in</a>.</p>'),
        ("What this hub does not promise", '<p>These are learning exercises. They do not come with a vendor licence, a credential, a job or an exam pass, and Infiante360 is independent of Adobe.</p>'),
        ("Next step", '<p>Want guided practice with a trainer? See the <a href="../lp/batches.html">live batches</a>, the <a href="catalogue.html">course catalogue</a> or <a href="../contact-us.html">contact us</a> (WhatsApp or call +91 82968 93895). Free demos are on the <a href="https://www.youtube.com/@Infiante360TechAcademy" rel="noopener" target="_blank">YouTube channel</a>.</p>'),
    ],
    faqs=[("Do I need an Adobe licence to practise?", "Not for the quiz, handout and guides. Simulator access is described on the simulators page."),
          ("Does practice lead to a credential?", "No credential is issued from this hub. It is for learning only.")],
    related=["academy/simulators.html", "academy/catalogue.html", "lp/batches.html"],
)
PRACTICE_ALL = [PRACTICE_PAGE]
