# Changelog: Strength & Longevity design

## Round 4: client results added early, old testimonial removed
- **New section `#results`** between the three benefit cards (`#program`) and "Your Goals. Your Plan. Your Coach." (`#features`): heading "Real People. Real Results.", the supplied supporting sentence, three before-and-after composites, the line "Individual results vary. Training history, consistency and other factors influence outcomes.", and a "Book a Consultation" button that opens the existing shared GHL modal (`data-open-form`).
- **Images:** `client-result-01/02/03.webp` (1080x1080, from supplied files `05fbcf7b-image.png`, `22389831-image.png`, `76d5fb68-image.png`). Whole composite kept, with both panels and BEFORE/AFTER labels; `object-fit: contain`; no crop, stretch, reorder or retouching. Masters are in `source-images/results-masters/` (outside `public/`).
- **No names, timeframes, numbers or training-format claims** are shown. Alt text is neutral.
- **Layout:** three columns from 900 px; stacked cards below that (max 30rem wide on tablet). White cards on the existing light-blue tint, 20px radius, Sora.
- **Removed:** the entire Christopher C. panel (quote, name, one-on-one/small-group note), its HTML comment, the `#reviews` section and the unused `.review-card` CSS. Normal section spacing closes the gap. Nothing replaces it.
- **Not changed:** hero, copy, other images, nav anchors (all still resolve), coach carousel, FAQ, address, GHL form/ID/embed/modal/fallback, CTA wiring, sticky mobile button, `script.js`, GTM placeholders, `noindex`. Semi-Private and Personal Training projects untouched.

## Round 3: clarity, credibility and enquiry journey (approved copy)
- **Hero:** already matched the brief (headline, "One-on-One Coaching · Los Alamitos, CA" label, sentence, button); no change.
- **Two coaching sections now distinct:** "Your Goals. Your Plan. Your Coach." explains personalization (new body; points Your Goals, Your Starting Point, Your Coach's Guidance). "Build Strength. Keep Moving Forward." explains progression and consistency (new body; points Technique Feedback, Progress Reviews, Appropriate Adjustments, Consistent Support). No benefit is repeated between them. The three benefit cards above are unchanged.
- **Client proof:** unchanged (single Christopher C. review with its mixed-format context). No additional verified testimonial was in the attachments, so no proof panel was added; missing inputs are in `CONTENT-NEEDED.md`.
- **Enquiry journey:** heading is now "YOUR NEXT STEP STARTS HERE" (same layout, id `#first-visit`, nav label "Your First Visit" unchanged); steps Send Your Enquiry, Talk Through Your Goals, Explore Your Training Options; added the line "Submitting the form is an enquiry, not a confirmed appointment." No duration, price, format, response time or free offer is stated.
- **FAQ:** five questions and answers replaced as supplied (same styling). The address answer is a link to the confirmed Google Maps location.
- **Closing section:** body now says "one-on-one coaching" instead of "one-on-one personal training"; heading, card, button and microcopy unchanged.
- **Not changed:** design, images, section order, GHL modal, form URL and ID, embed tag, CTA wiring, sticky mobile button, `script.js`, GTM placeholders, `noindex`.
- New file `CONTENT-NEEDED.md`.

---

## Round 2: focused refinements (approved copy)
- Hero headline "Build Strength. / For Life."; supporting sentence "One-on-one personal training in Los Alamitos to help you build strength, move with confidence and stay capable in everyday life." Eyebrow label and Book a Consultation button unchanged.
- Benefits heading "Strength for Today. A Plan for the Long Term." The three cards (everyday strength, technique guidance, consistency) are unchanged.
- Second coaching row heading "Build Strength. / Keep Moving Forward." on two lines; its paragraph, checklist and button unchanged.
- Photos: "Your Goals. Your Plan. Your Coach." now uses the supervised kettlebell photo (3:2, replaces the machine/dumbbell-curl photo). The closing section now uses the coach-and-client tablet photo (was the kettlebell photo) so nothing repeats.
- Spacing: section padding reduced (desktop 192px to 128px top+bottom, phone 112px to 80px, row sections 176px to 112px desktop and 96px to 64px phone; fluid in between). Hierarchy unchanged. Full-page height at 1440 px: 6,121 px to 5,515 px (about 10% shorter).
- Not changed: testimonial and context, coach details, FAQ, address, GHL modal, all CTA wiring, `script.js`, GTM placeholders.

---

Baseline: the current Personal Training project (v2.1). New visual design; approved copy unchanged.

## Design
- Dark photographic hero with a gradient overlay behind the text, coaching photo beside it (stacked with an intentional crop on phones). Two-line headline replaces the staggered one.
- Compact benefit strip, white sections, light-blue accents, three benefit cards, alternating photo/checklist rows, three-step consultation section, testimonial card, team carousel, FAQ accordion, closing consultation card, compact footer.
- Mobile layout built separately: stacked content, stacked cards, sticky bottom "Book a Consultation" button with page padding, hidden while the modal is open.
- New `i-check` icon symbol. `style.css` rewritten; the modal, carousel, team and FAQ rules are carried over unchanged.

## Where the existing copy went (nothing rewritten)
- Hero: headline, sentence, button, microcopy as before. Eyebrow = the old badges "One-on-One Coaching" and "Los Alamitos, CA". Strip = old stats ("1:1 Personal Attention", "Your Goals / Your Training Plan") plus "Los Alamitos, CA".
- Three cards (heading "Personal Training That Fits You"): Strength for Everyday Life, Guidance on Every Rep, Support to Stay Consistent (strength, movement guidance, consistency).
- Row 1 "Your Goals. Your Plan. Your Coach." + paragraph; checklist = the other three carousel cards (One-on-One Attention, A Plan for Your Goals, Progress You Can Follow).
- Row 2 "Build Confidence With Every Session" + paragraph; checklist = diagram items Exercise Guidance, Progress Reviews, Ongoing Adjustments, Consistent Support.
- Steps ("What Your First Visit Looks Like"): Your Consultation and Your Starting Point (old first-visit cards), Your Training Plan (old diagram item 2).
- Testimonial, FAQ, closing heading/body, footer, address and links: unchanged text.
- Closing card: heading "Book a Consultation" and the existing sentences "We'll contact you to arrange your consultation." and "Submitting the form does not confirm an appointment."
- **Not carried over (layout reasons):** the six-benefit diagram's item 1 text ("Begin with a conversation about your experience, goals and current training needs.", covered by the Starting Point step), the hero "Private Studio" chip, the first-visit location chips and the hero avatar "+" control. Nav labels are unchanged but re-ordered to follow the page (Training, Coaching, Progress, First Visit, Trainers); "Your Progress" now links to the second coaching row (`#progress`).

## Images
Hero deadlift/kettlebell coaching photo; row 1 dumbbell-curl photo (4:5); row 2 guided-hinge photo; closing kettlebell photo. Removed from `public/` because unused: floor-movement, tablet, first-visit and avatar derivatives (masters kept).

## Preserved
Shared modal, form URL and ID, one embed tag, GTM placeholders, `script.js`, footer address, map link, phone, email, social links, `noindex`, `robots.txt`, Sora.
