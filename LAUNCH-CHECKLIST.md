# Launch checklist: PT Booking version

Nothing has been published. DNS, GitHub and Google Ads were not touched. No booking was submitted.

## Confirm before launch
- [ ] **Hero slide 1 and 2 framing with the real photos:** both are hotlinked from formulafitness.co, which my workspace cannot reach, so they were tested with stand-in images of the same shape (3:2). Slide 2 uses `contain` so it cannot crop; check both on a phone and tell me if the subject sits low or off-centre.
- [ ] **GTM triggers:** open container GTM-K28JZ7N and check for triggers using `[data-open-form]`, the old GHL form URL (`widget/form/cCHvBgZHH4fkFVQY6907`), dialog open, or the old button text. They no longer match. Point click triggers at `a[data-booking-cta]` (values: header, hero, coaching, closing, sticky, footer). Keep these clicks separate from successful-booking conversions.
- [ ] **Successful-booking event:** decide how a booking is recorded (GHL confirmation redirect to a thank-you URL, or postMessage). Not configured or tested here. Make one real test booking only with your permission, then confirm the event fires once, not on clicks.
- [ ] **Calendar on the live page:** confirm the GHL calendar renders at the final domain (framing allowed, height 860 px / 960 px at 640 px and below is enough, no inner scrollbar, times shown correctly). Not verified from my workspace.
- [ ] **Attribution:** confirm UTM / lead source reaches GHL through `form_embed.js` and the calendar. Untested.
- [ ] **Live GTM:** after deploy, confirm `gtm.js?id=GTM-K28JZ7N` loads once with status 200 and the intended tags publish. Untested here (host blocked).
- [ ] **Results images, identity and permission UNRESOLVED:** 24 comparisons, faces blurred in both panels inside the files (48 faces plus one bystander). Check each slide visually. Confirm written permission to publish each person's photos (including blurred), current accuracy, and training format. Comparison 03 has body-fat % labels baked into the image. Keep unblurred originals out of GitHub and `public/`.
- [ ] **Hero photos 1-2 are hotlinked** from formulafitness.co (as in the preview). If that site changes, they break. Consider hosting them in `public/images/`.
- [ ] **Copy to confirm:** "free 15-minute call" wording, review counts and the review note came from the preview and could not be verified against live ratings.
- [ ] **Review links** open the intended Google/Yelp/etc. profiles.
- [ ] **Real devices:** iPhone Safari and Android, header at 320-393 px, mobile menu, sticky Book button over the calendar, results swipe/controls; also Firefox.
- [ ] **Trainer roles and titles:** confirm who delivers one-on-one personal training.
- [ ] **Privacy policy URL:** none supplied, so no link was added. Launch requirement.
- [ ] **Favicon on the live page:** hard-refresh and check `/favicon.ico` and `/apple-touch-icon.png?v=20261030`.
- [ ] **Consent banner / settings:** none exists in these files; confirm production consent handling lives in GTM and works with this page.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`; add a canonical URL; re-run the checks on the live URL.
