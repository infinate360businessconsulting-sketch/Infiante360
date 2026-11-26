"""Practice Labs: waitlist landing page. The paid labs product is not built yet, so the page takes interest only (no price, no checkout, no feature claims).
Scope and phases: docs/labs/LABS_PRODUCT_SCOPE.md."""
from content_growth import landing

LABS_PAGE = landing(
    "labs", "Practice Labs for Adobe MarTech: Join the Waitlist",
    "Paid hands-on practice labs for Adobe MarTech are being planned at Infiante360 Tech Academy. Join the waitlist and tell us which lab you want first.",
    "Practice Labs waitlist",
    ["adobe martech practice labs", "aep hands-on lab", "martech simulator lab", "adobe practice environment", "buy aep labs"],
    "Infiante360 is planning paid practice labs for Adobe MarTech, built on the simulator scenarios we already teach with. They are not on sale yet. Join the waitlist, tell us which lab you want first, and we will write to you when the first one opens, with scope and price. No credential, job or exam result is promised.",
    "Practice Labs waitlist",
    ["Tell us which lab you want first: AEP, Real-Time CDP, AJO, CJA or Web SDK", "You are told the scope and price before anything is sold", "Early joiners hear first when the first lab opens", "No payment is taken on this form"],
    "Learners who want hands-on practice beyond courses: developers, analysts, architects and career switchers.", "Practice labs waitlist",
)
LABS_PAGE["sections"].insert(0, ("What is planned", '<p>Scenario-based labs in the style of our <a href="../academy/simulators.html">simulators</a>, sold separately from courses. Nothing is on sale yet, and the exact features, price and refund terms will be published before the first lab opens. Until then, try the free <a href="../academy/practice.html">practice hub</a>.</p>'))
LABS_PAGE["related"] = ["academy/practice.html", "academy/simulators.html", "lp/batches.html"]
LABS_ALL = [LABS_PAGE]
