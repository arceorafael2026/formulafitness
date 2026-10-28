# Changelog: Semi-Private, Strength & Longevity design

## Version 2: crop, results and closing fixes
- **Hero crop:** the coach (left) and client (right) were hidden by the overlay and cut by the frame. Below 1280 px the hero photo now sits below the text as a rounded card (4:3 phones, 16:10 tablets); from 1280 px it is narrower (55%), the text is clear of the photo edge and the fade is short. Photo not zoomed, stretched or flipped.
- **Kettlebell section:** 4:3 frame, top-aligned (`crop-b`), so the foreground client's head, arms and kettlebell are visible at every width. The knee-raise photo also moved to 4:3 with its own position so heads and feet stay in frame.
- **Results:** the three placeholders were replaced by three different individual BEFORE/AFTER composites (`client-result-04/05/06.webp`; none of the three used on the Personal Training page). Whole composites, `object-fit: contain`, neutral alt text, no names, timeframes, numbers or service attribution. Introduction, disclaimer and consultation button unchanged.
- **Closing section:** the right-hand area now shows a bright, clear photo (coach with two clients at a barbell) instead of the dark pull-up photo (removed from the project), with a lighter overlay so the photo shows while the text and button stay readable; positioned separately for mobile and tablet so heads are not cut. The closing photo now loads immediately rather than lazily.
- **Not changed:** all copy, design, GHL URL/ID/embed/modal, CTA wiring, `script.js`, `noindex`, other projects.


## Version 1 (from the latest Personal Training strength-and-longevity page)
Copy and images only. Design, section order, ids, nav anchors, results-section styling, carousel, FAQ design, modal, `script.js`, GHL form and CTA wiring are unchanged.

- **Metadata:** title "Semi-Private Personal Training in Los Alamitos | Formula Fitness"; supplied description. `noindex` kept; no canonical added.
- **Hero:** label "SEMI-PRIVATE COACHING • LOS ALAMITOS, CA"; headline "Your Plan. / Stronger Together."; supplied body; button and microcopy unchanged. Strip: Individual Training Plans, Small-Group Coaching, Los Alamitos, CA. New hero photo: genuine small-group slam-ball squat.
- **Benefit cards:** "Strength for Today. Support for the Long Term."; Your Own Program, Coaching That Guides You, Shared Motivation.
- **Results (`#results`):** heading, supporting text, disclaimer and consultation button kept. The three Personal Training client composites were **removed** (not confirmed for this service). They are replaced by three labelled "Asset placeholder" cards in the same grid. Replace each with a confirmed composite (`object-fit: contain`) when approved. The Christopher C. testimonial is not restored.
- **First coaching section:** "Your Goals. Your Plan. Small-Group Support."; new body and points; badge YOUR OWN PROGRAM; knee-raise group photo.
- **Second coaching section:** "Build Strength. Keep Showing Up."; new body and four points (Shared Accountability replaces Consistent Support); badge COACHING & SUPPORT; kettlebell-swing group photo.
- **Three steps:** Send Your Enquiry, Explore the Format, Discuss Training Options; note unchanged.
- **Team:** heading "MEET YOUR SEMI-PRIVATE COACHING TEAM". Names, portraits and titles unchanged. Header nav label "Your Trainers" became "Your Coaches" to match the footer link.
- **FAQ:** five questions and answers as supplied (address answer keeps the map link).
- **Closing:** "YOUR GOALS. SHARED MOTIVATION."; new body; consultation card unchanged; pull-up/kettlebell group photo.
- **Footer:** new description; column "SEMI-PRIVATE TRAINING"; links Your Training, Your Individual Program, Your First Visit, Your Coaches, Your Progress, Book a Consultation (same targets). Phone, email, social links and address unchanged.
- **Removed from this project:** Personal Training photos and result images, `COPY-SUGGESTIONS.md`, the Personal Training content brief.
- **Not changed:** `script.js`, GTM placeholders, robots.txt, fonts, other projects.
