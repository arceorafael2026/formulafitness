# Formula Fitness: Personal Training, Strength & Longevity design (separate version)

Plain HTML, CSS and a little JavaScript. No build step. **Deploy only the `public/` folder.** Preview version: `noindex` is on. Nothing has been published and no DNS was changed. The current Personal Training project was copied, not modified.

## Latest changes (Tony's feedback, rounds 6-7)
- **Hero:** the supplied AI-generated images are integrated: portrait for phones (under 700 px), landscape for tablets and desktop, as WebP (`hero-ai-portrait-*`, `hero-ai-landscape-*`, built by `tools/build-hero.py`; masters in `source-images/hero-ai/`, not deployed). The dark left of the landscape image carries the existing headline, text and button; both people and the kettlebell stay in frame at every width. The alt text marks the image as illustrative AI-generated; it is separate from the real results and is not presented as a client.
- **Results:** three authentic composites with faces blurred inside the image files in both panels (`client-result-01/02/03.webp`, built by `tools/blur-faces.py`). Selected from the supplied files `22389831-image.png`, `7764d0a5-image.png`, `76d5fb68-image.png`. No names, timelines, numbers or training-format claims; the disclaimer is unchanged. Unblurred originals are not in this project or in `public/` (keep them private). Identity, permission and training format are **unresolved** (see `LAUNCH-CHECKLIST.md`).
- **Team:** Amber and CJ removed (cards and image files); eight coaches remain; carousel unchanged in code.

## Layout
```
public/                 deployable site: index.html, style.css, script.js, robots.txt, images/, fonts/
source-images/          original photo masters (not deployed)
docs/                   earlier briefs and baseline notes (not deployed)
tools/build-images.py   rebuilds the web derivatives from the masters (needs Pillow)
screenshots/            desktop, tablet and mobile screenshots
README.md  CHANGELOG.md  CONTENT-NEEDED.md  COPY-SUGGESTIONS.md  LAUNCH-CHECKLIST.md
```

## What this version is
A new visual design for the Personal Training page, following the supplied concept's hierarchy: dark photographic hero with the text beside the coaching photo and a subtle overlay, bright blue consultation button, compact benefit strip, white sections with light-blue accents, three benefit cards, alternating photo/coaching rows, a three-step consultation section, client proof, FAQ accordion, a closing consultation card and a compact footer. The first design's oversized staggered headline is replaced by a two-line headline (Build Strength. / For Life.). Sora, black, white and Formula blue are kept.

**Round 2 copy (approved by you):** hero headline and sentence, benefits heading and the second row's heading were changed as instructed; all other text is the earlier approved copy, reorganised not rewritten (see `CHANGELOG.md`). `COPY-SUGGESTIONS.md` holds older optional proposals, not applied. The page makes no promise of a longer life, reversed ageing, pain-free living, injury prevention or guaranteed results.

## Photos
Only the supplied real Formula Fitness photos, unretouched, as WebP derivatives (EXIF applied, metadata stripped, no upscaling; masters in `source-images/`). The concept's illustrative photos were not used. Hero: coach guiding a kettlebell squat. Row 1: coach watching a client hold two kettlebells. Row 2: coach guiding a dumbbell hinge. Closing: coach talking with a client over a tablet. No photo is repeated; the machine/dumbbell-curl photo is no longer used (master kept in `source-images/`). All use `object-fit: cover` with crop positions that keep the coach and client in view.

## Form and CTAs (unchanged integration)
- Seven enquiry controls open the same shared modal: header button, hero button, both coaching-row buttons, the closing consultation card button, the mobile sticky button and the footer link. Each is an ordinary link to the form URL if JavaScript is unavailable.
- Form `https://api.formulafitness.co/widget/form/cCHvBgZHH4fkFVQY6907` (ID unchanged), `form_embed.js` loaded once. `script.js` is byte-for-byte the previous version. The concept's simplified form was **not** recreated and no second form or form ID exists; the closing section is a consultation card that opens the existing modal.
- Loading spinner, 15 s timeout with retry, and the permanent "Open it in a new tab" fallback link are unchanged. Escape does not close the modal while focus is inside the cross-origin form (Shift+Tab to the close button).
- **Mobile sticky button:** fixed to the bottom on screens under 700 px, with page padding so it never covers content, and hidden while the modal is open (it uses the `lock` class the existing script already sets on `body`).

## Tracking
Google Tag Manager container **GTM-K28JZ7N** is installed with Google's standard snippets: the script is the first thing in `<head>` after `<meta charset>`, and the `<noscript>` iframe is the first element after `<body>`. There is exactly one loader. No other tracking code (gtag, Analytics, Ads) is in this project, so nothing else needed preserving here; if the live site has other tracking that is not in these files, keep it when you deploy. **Nothing here tests or proves conversion tracking.** No form submission was made, so GHL delivery, the thank-you redirect, Ads conversion and UTM attribution remain unverified (they were reported working on the previous live version).

## Favicon
Built from the existing logo mark by `tools/build-favicons.py`: white diamond mark on a black tile (only the mark, since the wordmark is unreadable at small sizes). Files in `public/`: `favicon.ico` (16/32/48), `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` (180, opaque), plus `icon-192.png` and `icon-512.png` (not linked; spare). The page links use `?v=20261030`; change that value whenever the icons change. The source logo is only 70x81 px, so the mark was smoothed and re-sharpened; supply a vector logo for an even crisper result.

## Preview locally
`python3 -m http.server -d public 8000`, then http://localhost:8000 (not `file://`). The form modal needs internet access.

## Testing record
Headless Chromium (Playwright), local server, widths 375, 390, 768, 1024 and 1440. **The real GHL form and `form_embed.js` were replaced by stand-ins (the sandbox cannot reach that host). No enquiry was submitted.**

### Performed: 398 automated checks passed (79-80 per width) after round 3
- All seven enquiry controls open the shared modal from the keyboard; Escape closes it and focus returns to the opener; the page URL does not change; the form is requested once; one embed tag, one iframe, one form ID; typed data survives close/reopen; the modal body scrolls to the stand-in form's last field (full-screen at phone widths); fallback link always visible.
- Mobile: sticky button pinned to the bottom, opens the modal, is hidden while it is open and returns after; it does not cover the last footer line at page end; tap targets (buttons, menu, FAQ rows) at least 44 px; mobile menu opens and closes.
- Desktop: navigation visible; all nav anchors resolve.
- Text: headline is two spans on one line each at every width with no clipping; hero sentence, button and microcopy exact; benefit strip, three cards, row headings and checklist titles, three steps, testimonial (exact, mixed-format context, no photo, no placeholder text), five FAQ answers, closing card, address and map link.
- FAQ: Enter opens, Space closes, Tab moves with a visible focus ring. Team carousel: eight coaches (Amber and CJ removed in round 6), exact step count to each end, last card complete.
- Round 3: both coaching sections' bodies and supporting points exact, three steps and the enquiry-not-appointment note exact, five FAQ answers exact (address is a map link), closing body exact, and a scan that no duration, price, response time, free/no-obligation or lifespan/medical claims appear.
- Round 2: new hero headline/sentence, benefits heading and row-2 heading exact; row 1 = kettlebell photo, closing = tablet photo, all photos different; section padding reduced and measured (see CHANGELOG).
- Photos: loaded, `object-fit: cover`, none used twice; crops reviewed by eye in `screenshots/` at all five widths.
- Contrast: all body text at least 4.5:1; large blue headings and the button at least 3:1.
- Scans of the HTML and visible text found none of: free, assessment, injury, guarantee, discount, pain-free, reverse/longer-life wording, "longevity", before-and-after, old address, or earlier-service terms. No horizontal overflow, console errors or failed requests.

### Not tested
- **Real GHL form inspection:** the host is not reachable from my workspace, so required fields (including any date of birth or intake fields) are **unverified**; see `CONTENT-NEEDED.md`.
- **The real GHL form**: rendering, validation, submission, thank-you redirect, Ads conversion, UTM attribution, and whether GHL allows framing on the final domain.
- Safari/iOS, Firefox, real phones (including the on-screen keyboard with the sticky button), screen readers, real touch swiping, performance scoring.
- The loading-timeout behaviour was not re-run (`script.js` is unchanged and it passed earlier).
