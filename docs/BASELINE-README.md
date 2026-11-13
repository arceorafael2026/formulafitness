# Formula Fitness landing page (rebuilt from the join.formulafitness.co reference)

Plain HTML, CSS and minimal JavaScript. No build step. Publish the `public/` folder.

## Files
- `public/index.html`: all content, GTM slots, the one shared consultation modal
- `public/style.css`: design (colours and font stack are variables at the top)
- `public/script.js`: mobile menu, carousels, consultation modal (no tracking, no form logic)
- `public/fonts/`: self-hosted Sora (variable, latin + latin-ext) and its OFL licence
- `public/robots.txt`: allows crawling so crawlers can read the noindex tag
- `public/images/`: supplied images, `logo.png`, `image-sources.csv`

## Consultation form (existing GHL form)
- Five controls open the SAME modal: header "Book a Consultation", both "Learn More" buttons, the hero trainer/avatar "+" control (aria-label "Join Trainers: book a consultation") and "Book Your Full Consultation". Each has `data-open-form`.
- Without JavaScript (or without `<dialog>` support) each of those is a normal link that opens the form URL in a new tab.
- Form URL used everywhere: `https://api.formulafitness.co/widget/form/cCHvBgZHH4fkFVQY6907`. Form ID unchanged. Nothing recreates fields, validation, submission, redirects or conversion tracking.
- `https://api.formulafitness.co/js/form_embed.js` is loaded once (one `<script async>` at the end of `index.html`).
- If your GHL embed code has extra attributes (`data-form-name`, `data-height`), add them to `<iframe id="inline-cCHvBgZHH4fkFVQY6907">`.

### Blank-form diagnosis (what I could and could not establish)
I could not reach `api.formulafitness.co` from my workspace (HTTP 403 from the sandbox proxy), so **the real GHL form was never loaded and the actual cause of the blank form is not confirmed.** What the code review found:
1. `loading="lazy"` on an iframe inside a closed `<dialog>`: a lazy iframe in a hidden container is deferred until it becomes visible, and browsers differ in when they start it. Removed.
2. Even without `loading="lazy"`, an iframe loaded while its container is `display:none` has zero width, so the GHL form can measure itself wrongly and `form_embed.js` can size it wrongly. The `src` is now set (once) from `data-src` when the modal first opens, so the form loads into a visible, full-width frame.
3. The old CSS gave the iframe `height:100%` inside a flex/overflow container, which is easy to collapse. It now has an explicit height (920px, 1100px on phones) inside one scrolling modal body; `form_embed.js` may override the height inline.
4. Causes I cannot rule out from here: the GHL form/domain settings refusing to be framed on the preview domain (`frame-ancestors`/allowed-domain rules), a form that is unpublished, or `form_embed.js` being blocked. **A deployment or custom domain on its own will not fix a blank form**; if the form is still blank in the modal, open the "Open it in a new tab" link: if that page is also blank, the problem is inside GHL, not this page.

### How loading works now
- First open: iframe `src` is set once, a spinner/"Loading the form..." status shows.
- A load event hides the spinner only. It does not mean the form rendered (a blocked or error page also fires `load`), so the page never says "loaded". A permanent footer link, "Form not showing? Open it in a new tab", is always visible in the modal.
- After 15 s with no load event: a message explains the delay and a "Try loading again" button appears.
- Close/reopen only hides the dialog. The iframe is not reloaded, so entered data is kept.
- To load the form on page load instead, put the `src` straight on the iframe (not recommended; see item 2).

### Keyboard and cross-origin limits
- Native `<dialog>`: Escape closes it, focus is trapped inside, the page behind is inert, focus goes to the close button on open and returns to the button that opened it on close.
- **Escape while keyboard focus is inside the embedded form does not close the modal.** The iframe is cross-origin, so its key events never reach this page (observed in testing with a cross-origin stand-in). Press Shift+Tab to reach the close button, or click it. The page cannot read or react to anything inside the form.
- Because the form is cross-origin, this page cannot detect real form errors, validation state or successful submission, and does not try to.
- Only one scroll area (the modal body) is intended. If GHL does not resize the iframe and a form is taller than 920/1100px, the iframe will scroll internally; raise the heights in `style.css` (`.modal-body iframe`).

## GTM
Marked slots only; nothing is installed. Paste the existing GTM snippets at the two marked places (`<head>` and right after `<body>`). No container ID or other tracking has been invented.

## Privacy policy
No confirmed URL was supplied, so no link was added. A marked comment in the footer CONTACT list shows where to put it.

## Fonts
Sora (SIL Open Font License, `fonts/OFL-Sora.txt`), self-hosted, with `Avenir Next`, `Segoe UI`, system fonts as fallbacks. Sora's top weight is 800 (the old 850/900 values map to 800).

## Preview locally
`python3 -m http.server -d public 8000` then open http://localhost:8000. Do not rely on `file://`. The form modal needs internet access.

## Publish on Cloudflare Pages
1. Push this folder to GitHub/GitLab.
2. Cloudflare dashboard > Workers & Pages > Create > Pages > Connect to Git.
3. Framework preset: None. Build command: empty. Build output directory: `public`.

## Going live
The page ships with `<meta name="robots" content="noindex, nofollow">` (kept on). At launch: delete it, add `<link rel="canonical" href="https://FINAL-ADDRESS/">`, optionally add a `Sitemap:` line to `robots.txt`, and attach the domain.

## Testing record
Method: headless Chromium (Playwright) against a local HTTP server, widths 375, 390, 768, 1024 and 1440, with the real supplied images.
**The GHL form and `form_embed.js` were replaced by local stand-ins** (a plain HTML page with 8 fields and a do-nothing button, and an empty script) served on the real URLs, because the real host was unreachable. No enquiry was submitted.

Passed at all five widths (200 checks, plus one timeout run):
- All five enquiry controls open the shared modal by keyboard (Enter), page URL/hash unchanged; Escape (focus outside the iframe) closes it; focus returns to the opener; close button closes it.
- Form URL requested once across repeated opens and reopens; one `form_embed.js` tag; iframe `src` exact; text typed into the stand-in form survived close/reopen.
- Modal body scrolls so the stand-in's last field and button are reachable (including on a 375px full-screen modal); fallback link always visible.
- Loading timeout: with a form request that never answers, the status message and "Try loading again" button appeared at 15 s and retry re-requested the form.
- Mobile menu opens and closes (375/390/768); desktop nav visible at 1024/1440.
- Both carousels: first cards are Personal Training / Semi Private Training / Recovery Service and Tony / Amber / Jason; 3 complete cards at 1024 and 1440, 2 at 768, 1 (with the next card peeking) at 375/390; Previous is disabled at the start, Next is disabled at the end with the last card complete; arrow keys move the track. All six services and ten coaches remain.
- No horizontal overflow; hero headline is four lines with no clipping or overlap; Sora loaded; no broken images; no console or page errors; no failed requests (other than the stubbed hosts); tel/mailto/social links present; social icons are SVG with the original aria-labels; copyright is centred.

Not tested / not verified:
- **The real GHL form**: whether it renders, its fields, validation, submission and conversion firing, and its real height.
- Escape-inside-iframe was observed with a cross-origin stand-in only.
- Real phones and Safari/iOS/Firefox (only Chromium was run); screen readers; touch swiping was not driven by real touch gestures.
- Pixel comparison with the reference: the reference site was not reachable from my workspace, so hero crop, badge sizes/rotation, CTA proportions and first-visit panels are my best match from the previous version and your description, not measured against the live reference. Please compare at your target viewport sizes.
- Yelp and the other social icons are simple self-drawn marks (the Yelp mark in particular is a stylised approximation); replace with official brand artwork if required.
- No Lighthouse/performance or `file://` run.

## Flagged for review (reference wording kept as-is; not verified)
Claims copied from the reference that need business confirmation before launch:
1. "20+ Years of Experience" (hero) and "Certified coaches with 20+ years of combined experience" (benefit 5): two different statements.
2. "10 SPECIALIZED TRAINERS": the team carousel lists 10 people; confirm the count and the word "specialized".
3. "LIVE PAIN FREE" and "reduce pain" (Recovery Service): outcome/health claims.
4. "This is included with your training, not an extra fee" (nutrition): included-service claim.
5. "We are now accepting a limited number of new clients": scarcity claim.
6. "No pressure, no sales pitch", "never plateau", "real time" tracking: promises.
7. "Under 60 seconds" and "15+ data points/metrics" (InBody scan).
8. "at a lower price point" (Semi Private), "Active Aging ... adults 55+", "Youth Training".
9. "Full Consultation" label: confirm the consultation is not described as free anywhere (the page does not say free).
10. Job titles for all 10 coaches are copied from the reference.
11. **Studio address** "10831 Los Alamitos Blvd, Los Alamitos CA 90720" (footer text and map link): earlier Formula Fitness materials show a different address. Confirm before launch.
12. Image-to-name mapping of the ten coach photos was inferred from the supplied file order; confirm each photo matches its name and title.
No new offers, results, testimonials or guarantees were added.
Not reproduced exactly: the reference's alt text (written to describe the photos), icon artwork, animations.
