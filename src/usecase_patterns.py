P=[]
def blk(cat, rows):
    for r in rows: P.append((cat,)+r)
blk("Acquisition",[
("Welcome journey for a new {customer}","first {event_b}","RTCDP, AJO","Email","First-activation rate vs holdout"),
("Lookalike seed audience of high-value {customer}s","repeat {product} activity after {event_b}","RTCDP, ad destination","Paid media","Cost per qualified lead"),
("Suppress existing {customer}s from acquisition ads","existing {product} holder flag","RTCDP suppression audience","Paid media","Wasted-spend reduction"),
("Anonymous-to-known stitching after sign-in","login after {event_a}","Identity graph, Web SDK","Web","Known-profile rate"),
("Retarget {event_a} visitors with a relevant {product} message","{event_a} without conversion","Edge audience, destinations","Display","Return-visit rate"),
("Follow-up after {event_b} form submission","{event_b} form submit","AEP source, AJO","Email, SMS","Contact-to-qualified rate"),
("Referral invitation for satisfied {customer}s","positive service event","RTCDP, AJO","Email, in-app","Referral conversion"),
("Registration reminder sequence for {product} events","registration without attendance","AJO","Email, WhatsApp","Attendance rate"),
("Channel preference capture at first {event_a}","first {event_a}","Consent and preference datasets","Web","Opt-in rate"),
("Next-best-offer for a first-time {customer}","first {event_b}","Decisioning, AJO","Web, email","Offer acceptance rate")])
blk("Onboarding",[
("Day-0 to day-30 {product} onboarding series","{product} created","AJO","Email, push","30-day activation"),
("Milestone nudge when {event_a} has not happened in 7 days","no {event_a} for 7 days","AJO, profile attributes","Email, in-app","Milestone completion"),
("Preference centre invitation after first {event_b}","first {event_b}","Consent datasets, AJO","Email","Preference completion"),
("Detail completion reminder for an unfinished {product} setup","incomplete {product} setup","AJO, Web SDK","Email, SMS","Completion rate"),
("Educational tip series matched to {product} usage","{event_a} frequency band","RTCDP, AJO","In-app","Feature adoption"),
("Welcome-back journey for a {customer} returning after setup","return after 14 days","AJO","Push","Return engagement"),
("Account-linking prompt for a {customer} using two channels","two identities seen","Identity graph","In-app","Linked-profile rate"),
("First-value celebration message","first success event","AJO","Push, email","Retention at 60 days"),
("Support-light onboarding for a self-serve {customer}","self-serve path","RTCDP, AJO","Email","Support-contact reduction"),
("Onboarding survey and routing","survey response","AEP source, AJO","Email","Survey response rate")])
blk("Engagement",[
("Personalised homepage hero for returning {customer}s","returning visit","Edge profile, personalisation","Web","Click-through rate"),
("Content recommendation after {event_a}","{event_a}","Decisioning","Web, email","Content engagement"),
("Frequency-capped weekly digest for {customer}s","weekly schedule","AJO, profile","Email","Digest engagement"),
("Re-engage {customer}s inactive for 30 days","30 days without {event_a}","RTCDP audience, AJO","Email, push","Reactivation rate"),
("Send-time and channel selection by past response","scheduled send","Profile attributes, AJO","Email, SMS","Open and click rate"),
("Dynamic banner for a {product} interest segment","{event_a} interest score","Edge segmentation","Web","Conversion rate"),
("In-app message for a feature a {customer} has not used","feature gap","AJO in-app","In-app","Feature adoption"),
("Seasonal campaign for a high-propensity audience","seasonal window","RTCDP, AJO","Email","Revenue per send vs holdout"),
("Quiet-hours and fatigue protection across channels","any journey send","Journey rules","All","Complaint and unsubscribe rate"),
("Interest-based newsletter variants","content-view history","AJO content variants","Email","Click-through rate")])
blk("Cross-sell and upsell",[
("Complementary {product} offer after {event_b}","{event_b}","Decisioning, AJO","Email, web","Attach rate"),
("Upgrade prompt for heavy {product} users","usage threshold","RTCDP, AJO","In-app","Upgrade rate"),
("Bundle suggestion for a {customer} with two items","two {product} holdings","Profile, decisioning","Web","Bundle conversion"),
("Renewal-time upsell review","renewal window","AJO","Email, advisor task","Renewal value"),
("Accessory or add-on prompt","post-purchase day 3","AJO","Email","Add-on rate"),
("Family or household plan invitation","household identity cluster","Identity graph","Email","Plan conversion"),
("Premium trial for engaged free {customer}s","engagement score threshold","RTCDP, AJO","Email, in-app","Trial-to-paid rate"),
("Cross-brand introduction for shared {customer}s","shared identity","Identity graph, destinations","Email","Cross-brand conversion"),
("Educational content before an upsell","upsell eligibility","AJO","Email","Content-assisted conversion"),
("Advisor callback offer for a high-value {customer}","high-value segment and {event_b}","AJO, task creation","Phone, email","Meetings booked")])
blk("Retention",[
("Churn-risk intervention for {customer}s","churn score above threshold","Profile scores, RTCDP","Email, phone","Churn reduction vs holdout"),
("Proactive notice on {event_b}","{event_b}","AJO, streaming events","SMS, push","Contact-centre call reduction"),
("Plan-fit review before renewal","renewal in 30 days","RTCDP, AJO","Email","Retention rate"),
("Low-usage education for a {product}","usage drop","AJO","In-app, email","Usage recovery"),
("Service-recovery message after a poor experience","negative service event","AJO, AEP source","Email, phone","Repeat-complaint rate"),
("Payment-failure recovery sequence","payment failure","AJO","Email, SMS","Recovery rate"),
("Loyalty milestone recognition","tenure milestone","AJO","Email, in-app","Engagement after milestone"),
("Pause or downgrade option instead of cancel","cancel intent","AJO, web","Web, email","Saves vs cancellations"),
("Check-in for a newly high-value {customer}","value tier change","RTCDP","Email, advisor task","Satisfaction measure"),
("Anniversary and renewal reminder","anniversary date","AJO","Email","Renewal on time")])
blk("Win-back",[
("Win-back offer for lapsed {customer}s","90 days without {event_b}","RTCDP, AJO","Email","Win-back rate"),
("What-has-changed message for a returning {customer}","return after long gap","AJO","Email, web","Re-engagement"),
("Survey-first win-back","lapse signal","AJO, survey source","Email","Survey response, return rate"),
("Suppress win-back for open service issues","open service case","Journey rules","All","Complaint avoidance"),
("Reactivation via a preferred channel","channel history","Profile attributes","SMS, push","Reactivation per channel"),
("Quote or cart revival with context","abandoned {event_b}","AJO","Email, SMS","Revival rate"),
("Seasonal return prompt","same-season history","RTCDP","Email","Seasonal return"),
("Last-chance reminder before account expiry","expiry in 14 days","AJO","Email, SMS","Retained accounts"),
("Referred-friend return incentive","referral link click","AJO","Email","Referral-linked return"),
("Re-permission request for faded consent","consent expiring","Consent datasets, AJO","Email","Re-opt-in rate")])
blk("Loyalty and advocacy",[
("Tier-upgrade progress message","points near threshold","AJO, loyalty source","Email, app","Tier upgrades"),
("Birthday or anniversary recognition","date attribute","AJO","Email","Redemption rate"),
("Early access for top-tier {customer}s","tier attribute","RTCDP","Email","Early-access uptake"),
("Points-expiry reminder","points expiring","AJO","Email, push","Redemptions before expiry"),
("Review request after a good {event_b}","positive outcome","AJO","Email","Review submission rate with consent"),
("Community invitation for engaged {customer}s","engagement score","RTCDP","Email","Community joins"),
("Reward choice by preference","preference attributes","Decisioning","App","Reward satisfaction"),
("Advocate referral reward","referral completion","AJO","Email","Referrals per advocate"),
("Personalised thank-you after repeat {event_b}","repeat {event_b}","AJO","Email, card","Repeat rate"),
("Exclusive content for loyal {customer}s","tenure and engagement","Personalisation","Web","Content engagement")])
blk("Service and support",[
("Deflect a support contact with proactive help","{event_a} error pattern","AEP events, AJO","In-app, email","Contacts avoided"),
("Case-status updates without a call","case opened","AJO, case source","SMS, email","Status-call reduction"),
("Priority routing for high-value {customer}s","tier and open case","Profile to routing system","Phone","Handle-time and satisfaction"),
("Post-resolution survey","case closed","AJO","Email","Survey response"),
("Known-issue notice to affected {customer}s","affected audience","RTCDP","Email, banner","Complaint reduction"),
("Self-service article suggestion after {event_a}","{event_a} confusion signal","Decisioning","Web","Self-service success"),
("Appointment or callback scheduling prompt","complex request","AJO","SMS, email","Callbacks booked"),
("Warranty or entitlement reminder","entitlement date","AJO","Email","Claims or renewals"),
("Disruption communication with options","{event_b} disruption","Streaming events, AJO","SMS, push","Rebooking or contact reduction"),
("Escalation alert for a repeat complaint","repeat complaint","AEP, task creation","Internal alert","Escalation resolution time")])
blk("Personalisation and decisioning",[
("Real-time offer ranking at {event_a}","{event_a}","Decisioning","Web, app","Offer conversion vs holdout"),
("Location-aware content","consented location","Edge profile","App","Store or branch visits"),
("Language and region adaptation","locale attribute","Profile","Web, email","Engagement by locale"),
("Device-aware experience","device attribute","Edge","Web, app","Mobile conversion"),
("Next-best-action for advisors","customer context","Profile to CRM","Advisor tool","Advisor action adoption"),
("Dynamic pricing message within policy","approved price rule","Decisioning","Web","Conversion within guardrails"),
("Personalised search ranking signals","search history","Edge","Web","Search success"),
("Content eligibility by consent and age rules","consent and age attributes","Profile, governance","All","Zero policy breaches"),
("A/B and holdout framework for personalisation","experiment","Target or AJO experimentation","Web, email","Valid uplift readout"),
("Real-time inventory-aware offers","stock event","Streaming events","Web, email","Offers shown for available items")])
blk("Measurement and governance",[
("Journey performance dashboard in Customer Journey Analytics","journey events","CJA","Dashboard","Funnel and drop-off visibility"),
("Cross-channel attribution view","touchpoint events","CJA, data views","Dashboard","Contribution by channel"),
("Audience overlap and size monitoring","audience refresh","RTCDP, reporting","Dashboard","Audience health"),
("Data quality alerts on ingestion","ingestion run","Monitoring, AEP APIs","Alert","Time to detect a failure"),
("Consent audit report","consent change","Consent datasets","Report","Consent coverage"),
("Identity match-rate tracking","identity events","Identity graph reporting","Dashboard","Match and duplicate rate"),
("Schema change impact review","schema change","XDM governance","Review","Breaking changes caught"),
("Holdout-based incrementality report","campaign end","CJA or warehouse","Report","Measured incremental lift"),
("Data-label and policy enforcement check","activation request","Governance policies","Check","Blocked non-compliant activations"),
("Deletion and access request workflow","privacy request","Privacy Service","Workflow","Requests completed on time")])
assert len(P)==100,len(P)
