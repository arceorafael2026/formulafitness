# Changelog: Semi-Private, Strength & Longevity design

## Version 5: new results from the supplied pool, CTA wording
- **Results replaced** from the eight supplied originals. None of the three is on the Personal Training page. Pool images matching the PT results were excluded by pixel comparison: `76d5fb68` (woman, side view) and `7764d0a5` (dark-haired man, front view). The three now on the page: `ac287212-image.jpg` (man, front view, same wall and pose, clear change) as `client-result-04`; `8d46a509-image.jpg` (woman, front view, same wall) as `client-result-05`; `bfa4772a-image.png` (= `05fbcf7b`, woman, front view, same wall) as `client-result-06`. Faces are blurred in both panels, locally, with bodies, labels and whole comparisons unchanged. Originals stay outside the project. No names, timelines, numbers or format claims; disclaimer kept.
- **Name labels not mapped:** the labels you gave (Chase, Miguel, Yaska, Daniel, Monica, Adriane, Alisha, Daisy) cannot be tied to files with certainty, and are not used anywhere on the page or in file names.
- **CTA wording:** every "Book a Consultation" button (header, hero, results, both coaching sections, closing card, sticky mobile bar, mobile menu, modal heading and iframe title) now reads **Enter Info to Get Prices**. Related sentences now say "We’ll contact you to discuss pricing and your next steps" (hero note, step 01, closing card); the meta description ends "Enter your info to get prices."; the FAQ answer says "Your form sends an enquiry." The GHL form ID, URL, embed, fields, redirects and modal behaviour are unchanged. The text inside the GHL form (its own heading or button) is not editable from this project.
- **Personal Training page:** not changed.

## Version 4: image pack, results blur, coaches (copy, colours, typography, GHL form and tracking unchanged)
- **Hero:** replaced the slam-ball photo with the supplied illustrative AI-generated images (fictional adults): portrait on phones (under 700 px), landscape from 700 px, via `<picture>`, WebP (`semi-hero-landscape-640/960/1280/1672`, `semi-hero-portrait-480/720/960/1024`). Headline, copy, button and layout unchanged: stacked below 1280 px, text on the dark left space from 1280 px (the photo's left edge fades into the black). Alt text says it is illustrative and AI-generated; it is not presented as a client result.
- **Build Strength. Keep Showing Up.:** now uses the supplied AI-enhanced version of the real kettlebell-swing photo (`semi-build-strength-480/720/960/1200.webp`). It is an enhanced derivative, not an untouched original. Inspected against the original: group, exercise, wall branding and the coach's shirt mark are intact.
- **Your Goals. Your Plan. Small-Group Support.:** **kept the existing real knee-raise photo.** The supplied `semi-your-goals-enhanced.png` was held back because inspection found accidental changes versus the original: the left TV screen content was removed, the coach's shirt wordmark is garbled, and several facial expressions differ. It is stored in `docs/held-for-review/` (not deployed) with a comparison image. To use it anyway, swap the image in that section; see `docs/held-for-review/README.txt`.
- **Results:** the previous `client-result-04` used the same person as a Personal Training result and has been replaced. New set, three people who are not on the Personal Training page: `a5732235` (04), `ab737aa5` (05), `e1d09de0` (06). **Faces are now permanently blurred in both panels of all three** (the earlier Semi-Private results were not blurred). Bodies, backgrounds, BEFORE/AFTER labels and the 1080x1080 whole composites are preserved (`object-fit: contain`). No names, timelines, numbers or format claims; disclaimer kept. Unblurred originals were removed from the project and ZIP (`tools/blur-faces.py` regenerates from a private folder).
- **Coaches:** Amber and CJ removed (8 coaches: Tony, Jason, Chris, Christy, Michael, Dwayne, Mikaela, J.P.), including their image files. Carousel script is generic; ends flush on J.P.
- **Removed images:** `semi-group-slam-ball-sq-*`, `semi-group-kettlebell-swing-sq-*`, `trainer-amber`, `trainer-cj`.
- **Unchanged:** GTM-K28JZ7N (single install), favicons, GHL form ID/URL/embed/modal/CTAs, `noindex`, `script.js`.
- **Files changed:** `public/index.html`, `public/style.css` (hero rules appended), new/removed files under `public/images/`, `tools/` (new `blur-faces.py`, `build-hero.py`, `build-coaching.py`), `source-images/`, docs.

## Version 3: GTM and favicon (no design, copy, photo or flow changes)
- **GTM:** the empty placeholder comments were replaced by Google's standard GTM-K28JZ7N script (first in `<head>`, after `<meta charset>`) and the standard `<noscript>` iframe immediately after `<body>`. One loader; no duplicates; no GA4/Ads/gtag tags or conversion actions added; no dataLayer events from buttons or the modal.
- **Favicon:** added `favicon.ico`, `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` (and spare `icon-192.png`, `icon-512.png`), linked with `?v=20261031`. There were no earlier favicon references to remove.
- **Files changed:** `public/index.html`; new `public/favicon.ico`, `public/favicon-16x16.png`, `public/favicon-32x32.png`, `public/apple-touch-icon.png`, `public/icon-192.png`, `public/icon-512.png`; new `tools/build-favicons.py`; docs (`README.md`, `CHANGELOG.md`, `LAUNCH-CHECKLIST.md`, `CONTENT-NEEDED.md`).
- **Not changed:** CSS, `script.js`, photos, results, copy, GHL form/ID/embed/modal, `noindex`, `robots.txt`, the personal-training project.


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
