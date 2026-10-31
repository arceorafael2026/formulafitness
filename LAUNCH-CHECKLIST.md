# Launch checklist: Semi-Private version

Nothing has been published. DNS, GitHub and Google Ads were not touched.

## Confirm before launch
- [ ] **Results images (UNRESOLVED: identity, permission, training format):** `client-result-04.webp` (supplied `ac287212-image.jpg`), `client-result-05.webp` (`8d46a509-image.jpg`), `client-result-06.webp` (`bfa4772a-image.png`, also named `05fbcf7b`). Different people from the three on the Personal Training page (`22389831`, `7764d0a5`, `76d5fb68`). Faces are blurred in the files. Choosing an image is **not** confirmation of any of these facts. For each confirm: (a) **identity**, because the website labels you gave (Chase, Miguel, Yaska, Daniel, Monica, Adriane, Alisha, Daisy) and the older source-page names (15 Rachel/CJ, 16 Chase/Renata, 17 Anna/Thomas, 18 Erik/Michael, 19 Marissa/Daisy, 20 Miguel/Ruby, 21 Dharshun/Angela, 22 Yaska/Levik, 23 Heather/Lizzi) conflict and cannot be tied to these files; (b) **written permission** to publish each person's photos (blurring does not replace permission; tattoos remain identifying); (c) **training format**: the page does not say these clients trained semi-private; (d) the images are current. Caveats: 06 has different clothing and gloves between panels; 05 has different leggings and a different expression. Alternates: `32d9a63f` (beach before photo, not comparable), `23b94e08` (wedding before photo, not comparable), `452a044b` (home before photo, different lighting). Remove any that fail.
- [ ] **"Enter Info to Get Prices" wording:** confirm what actually happens after the form is submitted. The page says the team will contact the person to discuss pricing and next steps; if prices are shown or sent automatically, or the wording should differ, update the button and the three supporting sentences. Also check the heading and button text **inside the GHL form** and the thank-you page, which this project cannot change, so they do not still say "consultation".
- [ ] **Hero is AI-generated:** decide whether to add a visible "illustrative image" note. It shows fictional people, not clients or the real gym.
- [ ] **Held knee-raise enhancement:** `docs/held-for-review/` holds the supplied `semi-your-goals-enhanced.png` with the accidental changes found. Approve use, or supply a corrected version.
- [ ] **Coach roles and titles** (unchanged): confirm who delivers semi-private coaching and that each title is current. Chris "Lead Nutritionist...", Jason "...Recovery Specialist".
- [ ] **Format wording:** confirm "semi-private", "small group" and "individual programming" describe how sessions really run; the page states no group size, price, timetable or duration.
- [ ] **Photos:** confirm the four group photos (knee raise (original), AI-enhanced kettlebell swing, closing barbell; hero is AI-generated) may be used and that people shown are fine with publication. Check for visible signage you do not want.
- [ ] **Inspect the real GHL form** (required fields, consent wording, mobile usability, thank-you redirect): **unverified**.
- [ ] **Merge check:** this project contains GTM-K28JZ7N only. If the live site has other tracking, consent settings, redirects or attribution handling that are not in these files, keep them when uploading.
- [ ] **Tracking QA on the live site** (test enquiry only with permission).
- [ ] **Sticky mobile button** on a real iPhone (Safari) and Android, with the on-screen keyboard and full-screen modal.
- [ ] **GTM on the live page:** after publishing, confirm `gtm.js?id=GTM-K28JZ7N` loads with status 200 exactly once (Network tab or Tag Assistant) and that the container publishes the intended tags. **Not verified here** (googletagmanager.com and the live site are unreachable from my workspace; tested only with a stand-in).
- [ ] **Favicon on the live page:** hard-refresh; check the tab, `/favicon.ico` and `/apple-touch-icon.png?v=20261031`. If the host injects a default favicon, remove it there.
- [ ] **Conversion tracking:** untested until a real form submission is made and the GHL, thank-you and Ads events are observed. Button clicks and modal opens are not lead events.
- [ ] **Privacy policy URL:** none supplied. Confirm GHL allows the live domain to frame the form.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`; add a canonical URL; re-run checks on the live URL.
- [ ] Confirm the old address (10831 Los Alamitos Blvd) appears nowhere. Correct: 3971 Ball Rd, Los Alamitos, CA 90720.
