# Changelog

## v2.1: "Build Confidence With Every Session" repair
- **Cause:** the testimonial card from v2 used the class `.rev`, and the second feature row already used `.rev` as its layout class (`<div class="feat rev">`). The card rules (border, background, padding and the large quotation mark via `::before`) therefore also applied to that row. Fix: the testimonial now uses its own class `.review-card` (HTML and CSS); the feature row is back to `<div class="feat">`. No unclosed wrappers were found.
- **Image:** the row now uses the supplied dumbbell-curl photo (`pt-coach-dumbbell-curl-*.webp`, 4:5, shown whole, unretouched; the extra people are mirror reflections). Alt text as specified. The kettlebell photo is now used only in the closing CTA.
- Duplicate-photo check: no photo is used twice on the page.
- Master renamed `pt-strength-machine-support.jpg` -> `pt-coach-dumbbell-curl.jpg` (source-images only).

## v2 (round 3): focused improvements
- **Hero:** kept the headline; added the supporting sentence, a large "Book a Consultation" button (same `data-open-form` modal action) and the microcopy "We'll contact you to arrange your consultation." Hero avatar label is now "Book a Consultation with our trainers".
- **Testimonial:** new `#reviews` section after the training section and before the first visit. Only the supplied Christopher C. excerpt and the context label. No photo, rating or other claims.
- **First visit:** copy now says: send an enquiry, the team contacts you to arrange a consultation, you discuss goals and suitable training options; submitting does not confirm an appointment. No free, assessment or duration wording.
- **Images:** first-visit "Your Starting Point" now uses the floor-movement coaching photo (crop `100% 50%` keeps the badge off the coach); closing CTA uses the kettlebell coach/client photo. The kettlebell photo is also in features row 2.
- **FAQ:** new `#faq` (native details/summary, keyboard operable) above the closing CTA with the five supplied Q&As.
- **Code:** `style.css` rules appended (hero, review, FAQ, two crops). `script.js`, modal, form URL, embed tag, GTM placeholders, footer and team unchanged.
- Unused image derivatives removed; `tools/build-images.py` updated.

---

# Changelog: Personal Training version

Baseline: the corrected Formula Fitness landing page from the previous round (shared GHL modal, Sora, carousel fixes). Section count (7), section order, section IDs, grids, carousels, fonts, colours, spacing and mobile rules are unchanged.

## Content (per PERSONAL-TRAINING-CONTENT.md)
- Title and meta description replaced. `noindex, nofollow` kept. No canonical added.
- Navigation: Services -> Your Training, What We Offer -> Your Coaching, Our Team -> Your Trainers, Your Results -> Your Progress. "Your First Visit" unchanged. Anchors (`#program`, `#features`, `#trainers`, `#workflow`) kept.
- Hero: four staggered lines PERSONAL / TRAINING. / BUILT AROUND / YOU.; badges One-on-One Coaching, Los Alamitos, CA, Private Studio; stats "1:1 / Personal Attention" and "YOUR GOALS / YOUR TRAINING PLAN".
- Carousel 1: heading "Personal Training That Fits You", six new cards, decorative background word "Training". All six cards and controls kept.
- First visit: both cards rewritten ("Your Consultation", "Your Starting Point"); badges "Your Goals" and "Your Starting Point"; location/private-studio chips kept.
- Feature rows rewritten ("Your Goals. Your Plan. Your Coach." / "Build Confidence With Every Session"); badges "Personalized Coaching" and "Guidance & Progress"; both buttons now read "Book a Consultation" (still open the shared modal).
- Team: heading "MEET YOUR PERSONAL TRAINING TEAM". Portraits, names and titles unchanged (see LAUNCH-CHECKLIST.md).
- Six-benefit diagram: six new items; hidden heading "Your Progress".
- Closing CTA: "READY TO TRAIN WITH A PLAN?", new body, button "Book a Consultation"; scarcity wording removed.
- Footer: new description, column "PERSONAL TRAINING" with the six specified links (last one opens the shared modal), address 3971 Ball Rd, Los Alamitos, CA 90720 and the specified Google Maps link. Phone, email and social links unchanged. The previous street address is removed everywhere, including the map URL.
- Accessible labels updated: section label "Your coaching", carousel labels, button labels. All image alt text rewritten to describe what is visible.

## Images
- New: three coaching photos from the supplied pack, as WebP derivatives (640/960/1280/1600/1920 px wide, no upscaling, EXIF orientation applied, metadata stripped, no cropping or retouching of the files). Used with `srcset`/`sizes`.
  - Hero: `pt-coach-guided-deadlift-*`
  - First-visit right card and closing CTA: `pt-coach-overhead-press-*` (CTA uses a different crop; it is not next to the first-visit card)
  - Six-benefit circle: `pt-coach-guided-movement-*`
- Kept: `first-visit-consultation.webp`, `hero-trainer-stat-avatar.webp`, `logo.png`, all ten trainer portraits.
- Renamed (removes nutrition/tracking wording from the URL): `features-nutrition-meal-plans.webp` -> `coach-client-tablet-discussion.webp`; `features-strength-intensity-tracking.webp` -> `coach-supervised-kettlebell-hold.webp`.
- Removed from `public/` (no longer used): `hero-man`, `first-visit-assessment`, `workflow-coach`, `cta-athletes`. The baseline image inventory moved out of `public/` to `docs/`.
- Not used: `pt-assisted-floor-movement` (reads as recovery), `pt-strength-machine-support` (several people, weaker one-on-one signal). Masters kept in `source-images/`.
- No client before/after image is on the page.

## Minimal non-text changes (documented, strictly for fit or accuracy)
1. Crop only: `object-position` rules at the end of `style.css` (hero, first-visit card, circle, CTA), plus a mobile-only hero value so the client's head stays in view. No frame size changed.
2. `text-wrap: balance` on `.feat h2` and `.cta-copy h2`. The new headlines are longer; without it the last line is a single word ("PLAN?", "Coach.").
3. Icons: hero badge icon changed from the chart icon to the person icon; carousel card 2 icon changed from the two-people icon to the star icon, so no group icon appears on a one-on-one page. Other icons kept.
4. Natural wrapping (no CSS change): at 375/390 px the two hero stats wrap ("Personal / Attention"; "YOUR GOALS / YOUR TRAINING / PLAN") and the carousel headings wrap to two or three lines. No overlap or overflow was measured.

## Preserved (verified in tests)
- Shared GHL modal, form `cCHvBgZHH4fkFVQY6907`, single `form_embed.js` tag, loading indicator, timeout message, fallback link, focus return. `script.js` unchanged.
- GTM placeholders (head and body) unchanged. They are placeholders only: no container ID, so no tracking exists in this build.
- `robots.txt` and the preview `noindex` unchanged.
