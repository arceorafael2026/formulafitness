# Formula Fitness – Brand landing page (NPA | Search | Brand)

Status: **layout, copy and tracking built; NOT ready to publish** until the items below are confirmed.
Run `python3 -I tools/check-placeholders.py` – it lists every unresolved placeholder (yellow "TODO" highlights on the page). It must report 0 before launch.

## 1. Must confirm before launch
| # | Item | Where | Notes |
|---|------|-------|-------|
| 1 | Final landing-page URL | `index.html` canonical / og:url / og:image; remove `noindex` | Domain undecided. Update the ad final URL afterwards. |
| 2 | GHL calendar embed + routing | `#bookingCalendar` `data-src` | Currently the 15-min consultation calendar URL used on the reference pages. Confirm it is the right calendar and who receives bookings. |
| 3 | GHL post-booking redirect | GHL calendar settings | Set to `https://<final-domain>/booking-confirmed/?booking_ref=<appointment id merge field>`. The merge field name is **unverified** – confirm in GHL. Without it no completed booking is counted (by design). |
| 4 | Public phone number | header / location / footer | Page uses (714) 380-2562 – **note the Google Maps listing shows +1 562-669-4030** + GHL Number Pool scripts (same as reference pages; the two screenshots showed different numbers). Confirm which number is public and that the pool swap + call routing work with a real call. |
| 5 | Opening hours | location section + FAQ | Filled from the Google Maps listing screenshot (Mon–Fri 5 AM–10 PM, Sat–Sun 6 AM–6 PM, seen 2026-11-20). Confirm they are still current. |
| 6 | Review figures | hero badges + results | 4.9 Google/38, 5.0 Yelp/63 are historical screenshot figures. Re-check, or remove. |
| 7 | Coach roster | Meet the Coaches | Uses current team photos/names from the PT/Semi pages. Confirm roster and roles. |
| 8 | Other services | Explore Other Services | Active Aging and InBody Scan cards now have descriptions, links (formulafitness.co/active-aging/ and /inbody/) and images; please confirm wording. |
| 9 | Privacy URL | footer | Still a placeholder. Terms (formulafitness.co/terms-of-service/) and Refund Policy (formulafitness.co/refund-policy/) are linked. |
| 10 | Client photos, testimonials, permissions | Results | 24 result photos reused from the Semi-Private page – confirm permission for this use. **No testimonials were supplied, so none are shown** (none invented). Add exact verified text when supplied. |
| 11 | Google Ads conversion action | GTM | See TRACKING.md. Bidding goal is still under review; do not attach to the campaign until approved. |

## 2. What was tested (local, stubbed third parties)
- Layout 320 / 375 / 393 / 768 / 1440: no horizontal overflow, header fits, hero photo above sticky CTA on phones.
- Section order, links (open new tab, carry UTM/gclid), no lazy-loaded images, no JS errors, GTM installed once.
- Tracking (Playwright): CTA click → only `consultation_cta_click`; phone click → `phone_click` with displayed number; first calendar interaction → one `booking_started` per page view; direct visit to `/booking-confirmed/` or malformed ref → nothing; valid ref → one `booking_completed`; refresh / revisit same ref → not repeated; new ref → counted; GHL redirecting inside the iframe → parent records once; repeat and reload → no duplicate; GTM not loaded inside the iframe.

## 3. Not tested (needs the live setup)
- The real GHL calendar, its redirect and merge field.
- GTM tags/triggers and Google Ads conversion firing (Tag Assistant / Preview).
- Number-pool swap, call routing and GHL attribution with a real call.
- Real phones / browsers. Attribution (UTM/gclid) arriving inside GHL contacts.
- `booking_started` is an approximation: the calendar is cross-origin, so it fires on first click/tap into it, not on a specific step.
- localStorage de-duplication is per browser; a different browser/device re-opening the same confirmation link would count again (clear the redirect after use or use GA/Ads transaction-id dedupe – see TRACKING.md).

## 4. Content decisions
- No ad statistics are shown. Page copy follows the brief (H1, hero copy, CTA text, two training cards, FAQ list).
- All six phrase-match keywords retained – no page change needed; page covers pricing, hours, location, training options up front.

## 5. Video
A click-to-play YouTube video (3ktIZoJ0X20, via youtube-nocookie) sits under Why Train at Formula Fitness. Nothing from YouTube loads until it is played. Not verified: the video content/permissions, and that embedding is allowed for it (check in a live browser).
