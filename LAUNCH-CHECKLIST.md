# Launch checklist: Strength & Longevity design

Nothing has been published. DNS, GitHub and Google Ads were not touched.

## Confirm before launch
- [ ] **AI hero image (integrated, needs your sign-off):** the supplied AI images are on the page. Review both crops (portrait on phones, landscape elsewhere) on real devices. It is labelled as illustrative in the alt text and must not be presented as a real client or result; decide whether to add a visible AI disclosure. Check you are happy that the people shown are fictional.
- [ ] **Face-blurred results:** check each blurred composite once more in the browser (six faces: before and after for three people). Keep the unblurred originals out of GitHub and `public/`.
- [ ] **Inspect the real GHL form** (required fields, consent wording, mobile usability, thank-you redirect). It could not be inspected from my workspace, so this is **unverified**. See CONTENT-NEEDED.md.
- [ ] **Answers still missing** for the consultation journey and proof (duration, price, format, response time, extra testimonials): see CONTENT-NEEDED.md.
- [ ] **Merge into the live site** so the live GTM, thank-you redirect, Ads conversion and UTM/lead-source handling carry over. GTM-K28JZ7N is now installed here (standard snippets), but if the live site carries any other tracking it must be preserved when merging.
- [ ] **Tracking QA on the live site** (test enquiry only with permission): enquiry reaches GHL, redirect works, the Ads conversion fires once per real submission and not on failed submits, direct thank-you visits or refreshes, and UTM is captured.
- [ ] **Sticky mobile button** on real iPhone (Safari) and Android, including the on-screen keyboard and the full-screen modal.
- [ ] **Copy suggestions** (COPY-SUGGESTIONS.md): approve, edit or reject; none are applied.
- [ ] **Results images (draft on the page; selection approved, details UNRESOLVED):** `client-result-01.webp` = supplied `22389831-image.png`, `client-result-02.webp` = `7764d0a5-image.png`, `client-result-03.webp` = `76d5fb68-image.png`. Faces are blurred in both panels inside the files. Approving the draft selection does **not** confirm any of the following, which remain open for each image: (a) **client identity** (names on the supplied source page conflict for files 15-23: 15 Rachel/CJ, 16 Chase/Renata, 17 Anna/Thomas, 18 Erik/Michael, 19 Marissa/Daisy, 20 Miguel/Ruby, 21 Dharshun/Angela, 22 Yaska/Levik, 23 Heather/Lizzi; I could not tie these hash-named files to numbers); (b) **written permission** to publish each person's photos, including in blurred form; (c) **training format** (one-on-one, semi-private or other; the page claims none); (d) that the images are current and accurate and that the progress shown is not affected by lighting, posture, clothing or camera angle. Remove any that fail. Keep the unblurred originals out of GitHub and `public/`.
- [ ] **Old testimonial removed:** the Christopher C. panel no longer appears on the page, so its permission check is no longer needed for this page. No review replaces it.
- [ ] **Trainer roles and titles** (unchanged; Amber and CJ removed): Chris "Lead Nutritionist...", Jason "...Recovery Specialist". Confirm who delivers one-on-one personal training.
- [ ] **Signage:** the "RECOVERY LAB" sign is visible at the top of the second coaching-row photo; confirm you are happy with it on this page.
- [ ] **Photo resolution:** the closing (tablet) and row-1 (kettlebell) photos are 1200 px wide masters and the closing photo is shown about 900 px wide on large screens. Supply larger masters if desired.
- [ ] **Privacy policy URL:** none supplied, so no link was added (marked comment in the footer). This is a launch requirement.
- [ ] **GTM on the live page:** after deploying, confirm in the browser (Network tab or Tag Assistant) that `gtm.js?id=GTM-K28JZ7N` loads with status 200 exactly once and that the container publishes your intended tags. **Not verified from my workspace** (googletagmanager.com and the live site are blocked there; tested only with a stand-in). Confirm GHL allows the live domain to frame the form.
- [ ] **Favicon on the live page:** hard-refresh and check the tab, `/favicon.ico` and `/apple-touch-icon.png?v=20261030`. If the host (GHL, Netlify, etc.) injects its own default favicon, remove that in the host settings; the page declares its own icons.
- [ ] **Conversion tracking:** untested until a real form submission is made and the GTM/Ads/GHL events are observed.

## At go-live
- [ ] Remove `<meta name="robots" content="noindex, nofollow">`; add a canonical URL; re-run the checks on the live URL.
