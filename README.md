# Formula Fitness: Personal Training, PT Booking version (review build)

Plain HTML, CSS and a little JavaScript. No build step. **Deploy only the `public/` folder.** Preview version: `noindex` is on. Nothing has been published, no DNS was changed, and no booking was submitted.

This is the supplied *PT Booking Preview* applied to the current Personal Training source. The preview's hero slides, photos, copy, mobile header, review links, map and section order are kept. The current project's production GTM, favicons and GHL embed helper were carried over.

## What the page does
- **Hero slideshow** (3 slides, no tab buttons) auto-advances every 5 s with a small Pause/Play control; it swaps headline text and photo together and stays still under reduced motion. Slides 1-2 use the preview's formulafitness.co photos (hotlinked, see Open items); slide 3 uses `images/trainer-tony.webp`.
- **Mobile header (320-393 px):** logo, phone number, **Book now**, Menu all visible (a small `max-width:340px` block trims gaps so nothing overflows at 320 px). Above 540 px the button reads **Book a Consultation Call**.
- **Results, "Real People. Real Results."** sits above the calendar and has **no CTA**. 24 before/after comparisons (`public/images/results/result-01..24.webp`), four visible at a time on desktop (fewer on narrower screens), Previous / Next / Play-Pause, a counter, and five-second autoplay. Autoplay is off when the visitor prefers reduced motion.
- **Booking section** `#book-consultation`: the 15-minute GHL calendar iframe (`https://api.formulafitness.co/widget/bookings/formula-fitness-initial-consultation-15-call`, the URL from the preview, unchanged). Every booking CTA (header, hero, coaching, closing, mobile sticky bar, footer) is an anchor to it and reads **Book a Consultation Call**.
- Ratings links, map iframe, team carousel and footer as in the preview. External links open in a new tab (`target="_blank" rel="noopener"`).
- The old pricing-form modal and form ID are gone from the page. `script.js` still contains the modal code but it is inert (no dialog exists).

## Faces
All 24 comparisons were blurred inside the image files, both panels, with localized elliptical masks (`tools/blur-booking-results.py`; strong two-pass Gaussian blur, feathered edge). Bodies, backgrounds, framing and the BEFORE/AFTER labels are unchanged. Unblurred originals are **not** in this ZIP or `public/`; keep them private. Face boxes were found with OpenCV Haar cascades and checked by eye on contact sheets; a second reviewer should still look at every slide (48 faces plus one bystander).

## Tracking (GTM-K28JZ7N)
Installed once: script first in `<head>` after `<meta charset>`, `<noscript>` iframe first in `<body>`. The preview had GTM disabled; this build restores the production snippets. No other tracking code exists in the project. `form_embed.js` (GHL helper, async) is loaded once before `script.js`.

### GTM click triggers: what needs updating
The previous pricing-form buttons were identified by `data-open-form`, an `href` to `https://api.formulafitness.co/widget/form/cCHvBgZHH4fkFVQY6907`, and the modal `dialog`. **None of those exist now.** Any GTM trigger (or Ads/GA event) that matches on `[data-open-form]`, that form URL, the dialog open, or the old "Enter Info to Get Prices" / "Book a Consultation" text will no longer fire. I cannot see the container, so I could not tell which triggers exist. Check the container for those selectors.

New hooks on the six booking buttons:

| Button | `data-booking-cta` |
|---|---|
| Header | `header` |
| Hero | `hero` |
| Coaching section | `coaching` |
| Closing card | `closing` |
| Mobile sticky bar | `sticky` |
| Footer | `footer` |

Suggested trigger: Click - All Elements / Just Links, condition *Click Element matches CSS selector* `a[data-booking-cta]` (or `a[href="#book-consultation"]`), and use *Click Element* attribute `data-booking-cta` as the label. No dataLayer events were added.

**Booking clicks are not booking events.** These clicks only scroll to the calendar. A successful booking can only be recorded from GHL (confirmation redirect to a thank-you URL, or a postMessage from the calendar widget). Neither is configured or tested here. Keep any Ads "conversion" off the click trigger.

## Layout
```
public/        deployable site: index.html, style.css, script.js, robots.txt, favicons, images/, fonts/
tools/         blur-booking-results.py (results blur), older helper scripts
docs/          earlier briefs and baseline notes (not deployed)
screenshots/   desktop and mobile screenshots of this build (booking-*.png)
README.md  CHANGELOG.md  LAUNCH-CHECKLIST.md
```
`source-images/` holds earlier photo masters (not deployed).

## Preview locally
`python3 -m http.server -d public 8000`, then http://localhost:8000 (not `file://`). The calendar, hero photos 1-2 and the map need internet access.

## Testing record
Headless Chromium (Playwright), local server, widths 320, 360, 375, 390, 393, 768, 1024, 1440. GTM, the GHL calendar and `form_embed.js`, the formulafitness.co hero photos and the map were **replaced by stand-ins** (the sandbox cannot reach those hosts). **No booking was submitted.**

### Performed: 209 automated checks passed
- Header: phone, Book now and Menu visible and not overflowing at 320-393 px; full label above 540 px.
- Menu opens and closes; nav anchors resolve.
- Hero: three slides switch text and image via the buttons.
- Results: heading above the calendar, no CTA inside the results section, 24 cards, four visible on desktop, Previous/Next/Play-Pause behave, counter updates, five-second autoplay advances, autoplay does not run under reduced motion.
- All 24 result images load at 1080x1080; no broken images on the page.
- Booking CTAs: six anchors, all go to `#book-consultation`, correct label per width, landing position is at the section top under the sticky header.
- Calendar iframe element present with the preview URL and expected heights.
- External links carry `target="_blank"` and `rel="noopener"`; GTM id appears once (script + noscript), `form_embed.js` once.
- No horizontal overflow; no console errors from the site's own code.

### Not tested
- **Calendar rendering on the real GHL host**, availability, booking, confirmation, and whether GHL allows framing on the final domain.
- The hotlinked formulafitness.co hero photos and the real map.
- Live GTM load (`gtm.js` 200, once), tags firing, and attribution forwarding by `form_embed.js`.
- Any successful-booking event or Ads conversion.
- Safari/iOS, Firefox, real phones, screen readers.
