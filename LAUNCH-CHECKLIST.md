# Launch checklist: Semi-Private version

Nothing has been published. DNS, GitHub and Google Ads were not touched.

## Confirm before launch
- [ ] **Results images (on the page now):** `client-result-04.webp`, `client-result-05.webp`, `client-result-06.webp` (masters in `source-images/results-masters/`, from the supplied `7764d0a5-image.png`, `ab737aa5-image.png`, `e1d09de0-image.png`). These are **not** the three used on the Personal Training page. For each, confirm: (a) **client identity**, because names on the supplied source page conflict (15 Rachel/CJ, 16 Chase/Renata, 17 Anna/Thomas, 18 Erik/Michael, 19 Marissa/Daisy, 20 Miguel/Ruby, 21 Dharshun/Angela, 22 Yaska/Levik, 23 Heather/Lizzi) and these files cannot be tied to a name with certainty; (b) **written permission** to publish each person's photos; (c) **training format**: the page does not say these clients used semi-private training, so keep it that way unless confirmed; (d) the images are current and accurate. Remove any that fail.
- [ ] **Coach roles and titles** (unchanged): confirm who delivers semi-private coaching and that each title is current. CJ "Director of Client Acquisitions", Chris "Lead Nutritionist...", Jason "...Recovery Specialist".
- [ ] **Format wording:** confirm "semi-private", "small group" and "individual programming" describe how sessions really run; the page states no group size, price, timetable or duration.
- [ ] **Photos:** confirm the four group photos (hero slam-ball squat, knee raise, kettlebell swing, closing barbell) may be used and that people shown are fine with publication. Check for visible signage you do not want.
- [ ] **Inspect the real GHL form** (required fields, consent wording, mobile usability, thank-you redirect): **unverified**.
- [ ] **Merge into the live site** so the live GTM, thank-you redirect, Ads conversion and UTM handling carry over. Only GTM placeholders exist here.
- [ ] **Tracking QA on the live site** (test enquiry only with permission).
- [ ] **Sticky mobile button** on a real iPhone (Safari) and Android, with the on-screen keyboard and full-screen modal.
- [ ] **Privacy policy URL** and **GTM snippets:** none supplied; add at the marked places. Confirm GHL allows the live domain to frame the form.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`; add a canonical URL; re-run checks on the live URL.
- [ ] Confirm the old address (10831 Los Alamitos Blvd) appears nowhere. Correct: 3971 Ball Rd, Los Alamitos, CA 90720.
