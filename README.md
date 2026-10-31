# Formula Fitness: Semi-Private Personal Training, Strength & Longevity design (separate version)

**Latest (image pack, Round 18):** new AI hero (portrait/landscape), AI-enhanced Build Strength photo, three new blurred results (different people from the Personal Training page), Amber and CJ removed. The enhanced knee-raise photo is held back (accidental changes found). See CHANGELOG.md, LAUNCH-CHECKLIST.md and docs/IMAGE-SOURCE-MAP.md. The hero and photo list below predates this round where it mentions the slam-ball hero.

Plain HTML, CSS and a little JavaScript. No build step. **Deploy only the `public/` folder** (when approved). Preview version: `noindex` is on. Nothing has been published, no DNS, GitHub or Google Ads change was made.

This is a **new, separate project** made from the latest Personal Training strength-and-longevity page. The Personal Training project (`formula-fitness-personal-training-strength-longevity`) and the earlier Semi-Private project (`formula-fitness-semi-private`) were not modified.

## What changed (copy and images only)
Design, section order, colors, Sora font, spacing, responsive behavior, results-section styling, coach carousel, FAQ accordion, modal and `script.js` are identical to the Personal Training version. Changed: the supplied Semi-Private copy (hero, benefit strip, three cards, both coaching sections, three steps, team heading, five FAQs, closing, footer, title and description), alt text, and the four photos. See `CHANGELOG.md`.

## Photos
Four of the supplied genuine small-group coaching photos (1200 px square masters in `source-images/semi-masters/`, not deployed): slam-ball squat (hero), standing knee raise (first coaching section), kettlebell swing (second section), coach with two clients at a barbell (closing). WebP derivatives come from `tools/build-images.py` (no cropping, retouching or upscaling). Because the masters are square, each placement is framed by viewport in `style.css` ("Photo framing"):
- **Hero:** under 1280 px the photo sits below the text as a rounded card (4:3 on phones, 16:10 on tablets); from 1280 px it sits beside the text with the text kept clear of the photo edge and a short fade, so the coach on the left and the client on the right are both visible.
- **Kettlebell section:** 4:3 frame, top-aligned, so the foreground client's head, arms and kettlebell stay in frame at every width. Knee-raise section: 4:3, positioned to keep heads and feet in.
- **Closing:** fills the right-hand area on desktop; above the text on mobile and tablet, positioned so heads are not cut.
Alt texts describe only what is visible; no group size or "every rep" claim.

## Results section
Three different individual BEFORE/AFTER composites from the supplied pack (`client-result-04/05/06.webp`, 1080x1080, shown whole with `object-fit: contain`; masters in `private folder (not in this project)`). They are **not** the three on the Personal Training page. They are presented as Formula Fitness community results: no names, timeframes, numbers or service attribution. Identity, permission and training-format checks are in `LAUNCH-CHECKLIST.md`. The Christopher C. testimonial is not restored.

## Form and CTAs (unchanged)
Eight enquiry controls (header, hero, results, both coaching rows, closing card, mobile sticky button, footer link) open the same shared modal for GHL form `cCHvBgZHH4fkFVQY6907`; `form_embed.js` is loaded once; fallback link, loading state and timeout unchanged. Google Tag Manager container **GTM-K28JZ7N** is installed with Google's standard snippets: script first in `<head>` after `<meta charset>`, `<noscript>` iframe first element after `<body>`, one loader, no placeholders. No other tracking, consent or attribution code exists in this project (nothing to preserve or duplicate), and no GA4/Ads tag or conversion was added. The consultation buttons and modal push nothing to the dataLayer, so button clicks and modal opens are not counted as leads. **Nothing here tests conversion tracking:** no form was submitted, so GHL delivery, the thank-you redirect, Ads conversion and UTM attribution are unverified.

## Favicon
Built from the existing logo mark by `tools/build-favicons.py` (white mark on a black tile; the wordmark is omitted as unreadable at small sizes): `favicon.ico` (16/32/48), `favicon-16x16.png`, `favicon-32x32.png`, `apple-touch-icon.png` (180, opaque), plus unlinked `icon-192.png`, `icon-512.png`. Linked with `?v=20261031`; change it whenever the icons change. The source logo is 70x81 px, so the mark was smoothed and re-sharpened; a vector logo would be crisper. No default platform favicon is referenced.

## Preview locally
`python3 -m http.server -d public 8000`, then http://localhost:8000 (not `file://`).

## Testing record
Headless Chromium (Playwright), local server, widths 375, 390, 768, 1024, 1440. The real GHL form was replaced by a stand-in (the host is not reachable from my workspace). **No enquiry was submitted.**

### Performed: 478 automated checks passed (about 96 per width)
- All eight enquiry controls open the shared modal from the keyboard; Escape closes it; the form is requested once; one embed tag, one iframe, one form ID.
- Exact text for hero, strip, benefit cards, both coaching sections, steps, team heading, five FAQs, closing, footer, title and description.
- Photos: four distinct, loaded, `object-fit: cover`, alt text everywhere; hero stacked below 1280 px and clear of the text at 1280+; kettlebell and knee-raise frames 4:3 with explicit positions; closing photo loads eagerly, fills the right-hand area on desktop and sits above the text on mobile/tablet. Every crop was also reviewed by eye at 375, 390, 768, 1024 and 1440 px.
- Results: exact heading, introduction, disclaimer and button; three different composites (none from the Personal Training page), loaded at 1080x1080, `object-fit: contain`, rendered square (no stretch or crop); no names, numbers, timeframes or service attribution in text or alt text; three columns from 900 px, stacked below; section height bounded.
- Mobile sticky button, tap targets, nav/footer anchors, FAQ keyboard use, ten-coach carousel, contrast (body text 4.5:1, large text 3:1), no horizontal overflow, no console errors.
- Scans found no one-on-one wording, free/discount/guarantee/pain-free/scarcity, price, duration, group-size, lifespan or old-address terms. `script.js` is byte-identical to the Personal Training version; `noindex` present; no canonical tag.

### Not tested / unverified
- The real GHL form (fields, validation, submission, redirect, Ads conversion, UTM, framing on the final domain).
- Safari/iOS, Firefox, real phones and on-screen keyboard, screen readers, real touch swiping, performance scoring.
- Whether current coaches deliver semi-private sessions (titles are carried over unchanged).
- Identity, permission and training format of the three people in the results composites (not verifiable from the files).
