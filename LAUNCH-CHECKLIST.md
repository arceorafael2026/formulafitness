# Launch checklist: Personal Training page

Nothing here has been published. DNS and hosting were not touched.

## Must be done by the business before launch
- [ ] **Privacy policy URL.** None was supplied, so no link is on the page. Add `<li><a href="CONFIRMED-URL">Privacy Policy</a></li>` in the footer CONTACT list (marked comment in `index.html`).
- [ ] **GTM snippets.** The page only has the two marked placeholders. Paste the real head and body snippets. No container ID was invented, and no tracking is active in this build.
- [ ] **Trainer roles.** Names, portraits and titles are carried over unchanged. Confirm which people deliver one-on-one personal training and that each title is current. Titles to look at in particular: CJ "Director of Client Acquisitions" (a sales-type title on a trainer carousel), Chris "Lead Nutritionist and Performance Specialist" (nutrition wording on a page that no longer offers a meal-plan promise), Jason "...Recovery Specialist". Do not relabel everyone as a trainer without confirming.
- [ ] **GHL live submission and redirect.** Make one test enquiry (with permission) and confirm: the form renders in the modal on the live domain, required fields and validation work, the submission reaches GHL, and the redirect or thank-you behaviour is correct. Also confirm GHL allows the live domain to frame the form.
- [ ] **Google Ads conversion QA.** After GTM is installed: confirm the conversion tag fires once on a real submission (thank-you page or event), not on modal open, and that it is not double counted.
- [ ] **Claims check.** "Private Studio" and "One-on-One Coaching" are shown next to photos where other clients and coaches are visible in the background. Confirm both statements are accurate for the service being advertised.
- [ ] **Signage.** The word "RECOVERY LAB" is partly visible on the wall in the overhead-press photo (first-visit card and closing CTA) and in the guided-movement photo (small, cropped in the circle). It is the studio's own sign, but confirm you are happy with it on a page that excludes recovery services.
- [ ] **Real-device check** on an iPhone (Safari) and an Android phone with the live form.

## Added in v2
- [ ] **Merge into the live page** with `v2-changes.patch` (this build has no live tracking, redirect or UTM code). After merging, re-test: one Ads conversion per real submission, none on failed submit, direct thank-you visit or refresh; UTM captured.
- [ ] **Testimonial:** confirm Christopher C.'s review and attribution may be used, and that mentioning small-group training on a one-on-one page is acceptable.
- [ ] **Photos:** the kettlebell photo is used twice (features row 2 and closing CTA); swap one if you prefer.
- [ ] **Consultation wording:** confirm what a consultation includes and whether it is free before adding any such claim.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`.
- [ ] Add `<link rel="canonical" href="https://FINAL-ADDRESS/">` and, if wanted, a `Sitemap:` line in `robots.txt`.
- [ ] Re-run the checks in README.md on the live URL.

## Optional later
- [ ] Client results (see README, "Suggested optional result placements"): only after identity, permission and one-on-one attribution are confirmed.
- [ ] Official social-brand icons if guidelines require them (the Yelp mark is a simple stand-in).
