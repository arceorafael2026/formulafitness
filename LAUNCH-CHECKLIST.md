# Launch checklist: Strength & Longevity design

Nothing has been published. DNS, GitHub and Google Ads were not touched.

## Confirm before launch
- [ ] **Inspect the real GHL form** (required fields, consent wording, mobile usability, thank-you redirect). It could not be inspected from my workspace, so this is **unverified**. See CONTENT-NEEDED.md.
- [ ] **Answers still missing** for the consultation journey and proof (duration, price, format, response time, extra testimonials): see CONTENT-NEEDED.md.
- [ ] **Merge into the live site** so the live GTM, thank-you redirect, Ads conversion and UTM/lead-source handling carry over. This project has only GTM placeholders (no IDs).
- [ ] **Tracking QA on the live site** (test enquiry only with permission): enquiry reaches GHL, redirect works, the Ads conversion fires once per real submission and not on failed submits, direct thank-you visits or refreshes, and UTM is captured.
- [ ] **Sticky mobile button** on real iPhone (Safari) and Android, including the on-screen keyboard and the full-screen modal.
- [ ] **Copy suggestions** (COPY-SUGGESTIONS.md): approve, edit or reject; none are applied.
- [ ] **Results images (draft, on the page now):** `client-result-01.webp`, `client-result-02.webp`, `client-result-03.webp` (masters: `source-images/results-masters/`, from `05fbcf7b-image.png`, `22389831-image.png`, `76d5fb68-image.png`). Before launch confirm for each: (a) **client identity**, since names on the supplied source page conflict (15 Rachel/CJ, 16 Chase/Renata, 17 Anna/Thomas, 18 Erik/Michael, 19 Marissa/Daisy, 20 Miguel/Ruby, 21 Dharshun/Angela, 22 Yaska/Levik, 23 Heather/Lizzi) and the supplied files cannot be tied to a name with certainty; (b) **training format**: confirm these clients trained one-on-one, since the page makes no such claim; (c) **written permission** to publish each person's photos; (d) that the images are current and accurate. Remove any that fail.
- [ ] **Old testimonial removed:** the Christopher C. panel no longer appears on the page, so its permission check is no longer needed for this page. No review replaces it.
- [ ] **Trainer roles and titles** (unchanged): CJ "Director of Client Acquisitions", Chris "Lead Nutritionist...", Jason "...Recovery Specialist". Confirm who delivers one-on-one personal training.
- [ ] **Signage:** the "RECOVERY LAB" sign is visible at the top of the second coaching-row photo; confirm you are happy with it on this page.
- [ ] **Photo resolution:** the closing (tablet) and row-1 (kettlebell) photos are 1200 px wide masters and the closing photo is shown about 900 px wide on large screens. Supply larger masters if desired.
- [ ] **Privacy policy URL:** none supplied, so no link was added (marked comment in the footer). This is a launch requirement.
- [ ] **GTM snippets:** paste the real head and body snippets at the marked places. Confirm GHL allows the live domain to frame the form.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`; add a canonical URL; re-run the checks on the live URL.
