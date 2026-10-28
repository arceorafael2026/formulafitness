# Formula Fitness: Personal Training, Strength & Longevity design (separate version)

Plain HTML, CSS and a little JavaScript. No build step. **Deploy only the `public/` folder.** Preview version: `noindex` is on. Nothing has been published and no DNS was changed. The current Personal Training project was copied, not modified.

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
Only the two marked GTM placeholders exist. **No tracking, redirect or UTM code is in this project and no Google Ads conversion is installed or verified.** Merge this design into your live files (or send them to me) so the live tracking, redirect and attribution carry over; do not replace the live page with this one blindly.

## Preview locally
`python3 -m http.server -d public 8000`, then http://localhost:8000 (not `file://`). The form modal needs internet access.

## Testing record
Headless Chromium (Playwright), local server, widths 375, 390, 768, 1024 and 1440. **The real GHL form and `form_embed.js` were replaced by stand-ins (the sandbox cannot reach that host). No enquiry was submitted.**

### Performed: 398 automated checks passed (79-80 per width) after round 3
- All seven enquiry controls open the shared modal from the keyboard; Escape closes it and focus returns to the opener; the page URL does not change; the form is requested once; one embed tag, one iframe, one form ID; typed data survives close/reopen; the modal body scrolls to the stand-in form's last field (full-screen at phone widths); fallback link always visible.
- Mobile: sticky button pinned to the bottom, opens the modal, is hidden while it is open and returns after; it does not cover the last footer line at page end; tap targets (buttons, menu, FAQ rows) at least 44 px; mobile menu opens and closes.
- Desktop: navigation visible; all nav anchors resolve.
- Text: headline is two spans on one line each at every width with no clipping; hero sentence, button and microcopy exact; benefit strip, three cards, row headings and checklist titles, three steps, testimonial (exact, mixed-format context, no photo, no placeholder text), five FAQ answers, closing card, address and map link.
- FAQ: Enter opens, Space closes, Tab moves with a visible focus ring. Team carousel: ten coaches, boundaries and last card complete.
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
