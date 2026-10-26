# Formula Fitness: Personal Training landing page (separate version)

Plain HTML, CSS and a little JavaScript. No build step. **Deploy only the `public/` folder.** Preview version: `noindex` is on. Nothing has been published and no DNS was changed.

## Project layout
```
public/                 deployable site: index.html, style.css, script.js, robots.txt, images/, fonts/
source-images/          original coaching photos (masters). NOT deployed
docs/                   the content brief, image handoff notes, image map, baseline README. NOT deployed
tools/build-images.py   rebuilds the web derivatives from the masters (needs Pillow)
screenshots/            desktop, tablet and mobile screenshots from testing. NOT deployed
CHANGELOG.md            what changed, including every non-text change
LAUNCH-CHECKLIST.md     items the business must complete before launch
```
Briefs, masters and image inventories are outside `public/`.

## What this version is
The existing page converted to a one-on-one Personal Training page: copy, navigation labels, image sources, alt text and metadata only. Design, section count and order (9 in v2: hero, program, reviews, first visit, features, trainers, workflow, FAQ, CTA), section IDs, grids, staggered headline, carousels, fonts, colours, spacing and mobile behaviour are as in the baseline. Details are in `CHANGELOG.md`.

Baseline note: the `website/` folder named in the request did not arrive as a folder. I used the corrected page from the previous delivery (same files) as the baseline. The original baseline README is in `docs/BASELINE-README.md`.

## GHL form (unchanged)
- Seven enquiry controls open the same modal: header button, new hero "Book a Consultation" button, hero trainer "+" (aria-label "Book a Consultation with our trainers"), both feature buttons, closing CTA, footer "Book a Consultation". Each is a normal link to the form URL if JavaScript is unavailable.
- Form `https://api.formulafitness.co/widget/form/cCHvBgZHH4fkFVQY6907` (ID unchanged). `https://api.formulafitness.co/js/form_embed.js` is loaded once. No fields, validation, redirect, submission or conversion logic was added or changed.
- The iframe gets its `src` once, on first open; closing the modal only hides it, so typed data is kept. A spinner, a 15-second timeout message with a retry button, and a permanent "Open it in a new tab" link are in the modal. A load event is never reported as proof the form works.
- **Escape inside the form:** the form is cross-origin, so Escape does not close the modal while keyboard focus is inside it. Users can Shift+Tab to the close button. This cannot be fixed from this page.
- A deployment or custom domain alone will not fix a blank form; GHL must also allow the domain to frame the form.

## v2 changes (round 3)
Hero sentence, button and microcopy; single verified testimonial after the training section; first-visit copy and photo; five-question FAQ above the closing CTA; closing CTA photo. Details: `CHANGELOG.md`. `script.js`, the modal markup, the form URL and the embed tag are unchanged.

**Merging into the live site:** this project does not contain the live site's tracking, redirect or UTM handling (only GTM placeholders). Do not replace the live page with `public/index.html`. Apply `v2-changes.patch` (diff against the previous build) to the live files, or send me the live files so I can rebase onto them. Copy the new images in `public/images/` and the appended rules in `style.css`.

## Tracking
`index.html` contains only the two marked GTM placeholders (head and body). **No tracking code or container ID is present, so no analytics or Ads conversion tracking exists in this build.** Paste the real snippets at the marked places.

## Preview locally
```
python3 -m http.server -d public 8000
```
Then open http://localhost:8000 (do not rely on `file://`). The form modal needs internet access.

## Testing record

### Performed (headless Chromium via Playwright, local HTTP server, widths 375, 390, 768, 1024, 1440)
**The real GHL form and `form_embed.js` could not be reached from my workspace (the network blocks that host), so both were replaced by local stand-ins served on the real URLs: a plain page with 8 fields and a do-nothing button, and an empty script. No enquiry was submitted.**

245 automated checks passed (49 per width), plus a separate timeout test. They covered:
- All six enquiry controls open the shared modal from the keyboard (Enter); the page URL does not change; Escape (focus outside the iframe) closes it; focus returns to the control that opened it; the close button works.
- The form URL is requested once across all opens; one `form_embed.js` tag; iframe `src` exact; text typed into the stand-in survived close and reopen; the modal body scrolls to the stand-in's last field and button, including full-screen at 375 px.
- Loading timeout: with a form request that never answers, the status message and "Try loading again" button appeared at 15 s, and retry re-requested the form.
- Mobile menu (375/390/768) opens and closes; desktop navigation visible at 1024/1440; new nav labels present.
- Both carousels: initial cards are One-on-One Attention / A Plan for Your Goals / Strength for Everyday Life and Tony / Amber / Jason; complete cards shown: 3 at 1024 and 1440, 2 at 768, 1 at 375/390; Previous disabled at the start; Next disabled at the end with the last card complete; arrow keys scroll. Six cards and ten coaches remain.
- No horizontal overflow; the four-line headline has no clipping or vertical overlap; hero badges and stats do not overlap each other or leave the viewport (measured).
- Every referenced local file exists; nothing in `public/` is unreferenced; no console or page errors; no failed requests; every image has alt text and loaded.
- Page text and HTML scanned for the previous services and claims (InBody, semi-private, recovery service, active aging, youth, 20+, "SPECIALIZED", limited-number wording, guarantee, discount, pain-free, meal plan, "Under 60 seconds", the old address): none found. The only "Nutritionist" is Chris's carried-over job title (flagged in the checklist).
- New address text and map link, page title, `noindex`, section IDs and count, and GTM placeholders (no IDs) verified.
- Image crops reviewed by eye in screenshots: hero and first-visit card at all five widths, circle and closing CTA at 1440 and 390 (`screenshots/`). Coach and client stay in view in each. In the hero at 375/390 the coach's hair/back of head is slightly cropped so the client's head can stay in frame.

### v2 re-test (performed): 350 automated checks passed (70 per width, same five widths), stand-in form as before
Hero text, button and microcopy exact; button inside the viewport and at least 56 px tall; testimonial text, attribution and context label exact, no image; section order; FAQ text exact, Enter opens, Space closes, Tab moves with a visible focus ring, targets at least 44 px; new first-visit and CTA photos in place; all seven controls open the shared modal; form requested once; contrast at least 4.5:1 for new text (hero button uses the 3:1 large-text rule); banned-term scan extended with "free", "assess", "injur"; no overflow, console errors or failed requests. Crops reviewed by eye in `screenshots/`. The timeout test was not re-run (`script.js` unchanged).
Observation: at 1440x900 the hero button's bottom edge is near the fold; on 375/390 phones it is inside the first screen.

### Not tested
- The real form, thank-you redirect, Ads conversion and UTM handling were not touched and not tested (they are not in this project).

- **The real GHL form**: rendering, fields, validation, submission, redirect, whether GHL allows framing on the final domain. Escape-inside-iframe was observed only with a cross-origin stand-in.
- Tracking and Ads conversions (not installed).
- Safari/iOS, Firefox and real phones (Chromium only); screen readers; real touch-swipe gestures; performance scoring.
- Pixel comparison with any reference site.

## Suggested optional result placements (NOT implemented)
Result images were not added. If identity, permission and one-on-one attribution are confirmed later, two existing image areas could take them (keep each BEFORE/AFTER composite whole):
1. **First feature row image** (`#features`, first `.fimg`, currently the tablet discussion photo, badge "Personalized Coaching").
2. **Second feature row image** (second `.fimg`, currently the kettlebell photo, badge "Guidance & Progress").

Practical notes for whoever does it:
- The composites are square (1080 x 1080) and the frames are 3:2. Use `object-fit: contain` (never `cover`), accepting side bars, or swap to a square frame; do not crop a panel.
- Candidates that are complete, clearly studio-backed and high-resolution: `client-result-16`, `client-result-17`, `client-result-18`, `client-result-27`, `client-result-29`. Less suitable: 19 (non-studio swimwear selfie), 28 (non-studio "before"), 25 (visible medical brace and mask, health-related), 24 (heart-rate gear, no clear one-on-one link). The three 416 x 300 files are too small for these frames.
- The badge text ("Personalized Coaching", "Guidance & Progress") would need approved wording; do not add names, weights, timeframes or quotes. Source names for files 15-23 conflict (see `docs/IMAGE-HANDOFF-READ-ME-FIRST.txt`), and the "Chase" timeline is unverified.
- Alt text should only say what is visible, for example "Before and after comparison photos of a Formula Fitness client".
- The result images were not copied into this ZIP; use your originals.

## Image notes
- Derivatives are in `public/images/` as `pt-coach-*-640/960/1280/1600/1920.webp` (long edge capped at 1920, none upscaled, orientation honoured, metadata stripped). The supplied coaching files were already about 2576 px on the long edge. Masters: `source-images/coaching-masters/`.
- To change a crop, edit the `object-position` rules at the end of `style.css`.

## Publish on Cloudflare Pages (when ready)
Build command: none. Build output directory: `public`. Complete `LAUNCH-CHECKLIST.md` first.
