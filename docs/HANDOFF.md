# Active Aging landing page – handoff (outstanding items)

The public page contains no TODO text. Everything unfinished is listed here. Launch gate: `python3 -I tools/check-placeholders.py` (only the noindex/canonical items should remain).

## Awaiting Tony's confirmation (page uses general wording)
| Item | Current page wording |
|---|---|
| SilverSneakers participation | Not mentioned. |
| Training formats | "Your coach will explain the formats available…"; FAQ names the existing one-on-one and semi-private formats generally. |
| Assessments / inclusions | Only "your coach assesses what will suit you". |
| Consultation calendar + appointment routing | **Reused from the Brand page** as instructed: `https://api.formulafitness.co/widget/bookings/formula-fitness-initial-consultation-15-call` + `form_embed.js`. It is the generic 15-minute consultation calendar: confirm it is the approved Active Aging calendar and how bookings are routed. Set its GHL redirect to `/booking-confirmed/?booking_ref=<appointment id merge field>` (merge field unverified) or no completed booking is counted. |
| Free 15-minute call | Not stated on the page (the calendar name says 15 minutes); confirm it applies to Active Aging before adding the duration/offer. |
| Pricing / scheduling | No prices; FAQ says they are discussed when you call. |
| Public phone number | (714) 380-2562 with GHL Number Pool scripts. Google Maps listing shows +1 562-669-4030 – confirm. |

## Reviews and testimonials
- Added: Google 4.9 (38 reviews) and Yelp 5.0 (63 reviews) in the hero and a "What Members Say" section, each linking to the live review pages. **These are the historical figures from the reference screenshots – re-check before launch.**
- **Real-person testimonial quotes are NOT on the page.** No exact, verified quote text or permission exists in the project (the other pages only link to Google/Yelp), and quotes were not invented. To add them, send the exact wording, the name/initials to show, and written permission; they go inside the What Members Say section.

## Photos (v7)
- **Hero** is now a real coaching photo (Tony with an older client, supplied by client) instead of the AI image. The AI image was removed from the project.
- **Before/after (result-11, face blurred)** now sits inside What Members Say. The separate Real People. Real Results. section and the second coaching photo were removed.
- Confirm written permission for the hero photo and the before/after, and that the before/after suits Active Aging (shows a knee brace and body; the caption makes no claims). Still no testimonial text.

## Hidden until content exists
- **Member Experiences photo section** – saved in `docs/HIDDEN-member-experiences-section.html`. Needs real approved older-adult photos (written permission) and verified testimonials. The AI hero image must not be used there.
- **Coach profiles beyond names/roles** – no unconfirmed profile content is shown. The Meet the Coaches section shows only the approved portraits, names and roles used on the other pages. Still to confirm: which coaches work with Active Aging, and any verified relevant experience.

## Other
1. Final URL (canonical, og:url/og:image; remove noindex). 2. Privacy Policy: footer link removed (Terms and Refund links remain). 3. Opening hours came from the Google listing – confirm. 4. Hero is a real photo (see Photos). 5. Claims review: the existing formulafitness.co/active-aging page could not be read here – review any accuracy, supplement, injury-prevention or health claims before reusing text. This draft makes none. 6. YouTube video (3ktIZoJ0X20): content, embed permission and **captions not verified** (the player requests captions by default; confirm they exist). Nothing loads from YouTube until Play. 7. Google Ads conversion: not connected (TRACKING.md).

## Checks
Done (local, third parties stubbed): 320/393/768/1024/1440px – no horizontal scroll, no JS errors/404s, text ≥16px (except eyebrow labels and the copyright line), tap targets ≥40px, hero stacked below copy under 900px and uncropped, no repeated images, all images load, FAQ opens by keyboard, tracking events (below).
**Could not complete:** the REAL GHL calendar loading (the build environment cannot reach api.formulafitness.co, so screenshots show a stand-in page inside the iframe; the iframe size, position, URL and parameters are real); real GHL calendar/redirect/booking (none supplied); GTM/Ads firing; number-pool swap and call routing, including whether the pool also swaps the tel link on button CTAs (tested only that the number is read from the link); real devices; video playback/captions; screen-reader pass.

## Hero video (v9) - needs review
- The video is an **InBody 580 scan explainer**, not Active Aging-specific. Whether the scan is part of Active Aging is unconfirmed (pending Tony), so the page does not mention InBody in its own copy and has no InBody section.
- The video makes health claims (visceral fat linked to diabetes, stroke and heart disease; scan can show inflammation/fluid imbalance; comparison with DEXA). Have Tony confirm these are acceptable for a Google Ads page, or re-cut.
- Captions/transcript are machine-generated; proofread before launch.
- File is 540p ~8 MB for page speed; swap in a higher-quality encode if preferred. Decide whether to keep the YouTube video in Benefits as well.
- Not verified: actual video playback (sandbox browser has no H.264 decoder; file is standard H.264/AAC), real calendar, GTM/Ads, number pool, real devices.

- (v10) Results slider now uses the 24 shared community comparisons; permission and fit for Active Aging still to confirm.
