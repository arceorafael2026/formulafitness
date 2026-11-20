# Tracking & GTM setup (GTM-K28JZ7N)

All events go to `dataLayer`; nothing is sent to Google Ads directly, so the approved conversion action can be connected in GTM.

| Event | Fires when | Extra params |
|---|---|---|
| `consultation_cta_click` | any `[data-booking-cta]` clicked | cta_location, cta_text |
| `phone_click` | any `tel:` link clicked | phone_location, phone_number (as displayed), phone_href |
| `booking_started` | first click/tap into the calendar (once per page view) | trigger |
| `booking_completed` | `/booking-confirmed/?booking_ref=<id>` loads after GHL confirmation, once per id | booking_ref |

Every event also carries `page_variant: brand`, utm_source/medium/campaign/term/content and `has_click_id` (gclid/gbraid/wbraid presence; the ids themselves are carried in the calendar iframe URL and outbound links).

## GTM
1. Custom Event triggers for each event name above.
2. GA4 event tags on all four. Mark only `booking_completed` as the key event.
3. Google Ads: attach the **approved** conversion action to the `booking_completed` trigger only. Use `booking_ref` as the transaction ID for dedupe. Do not use `booking_started`, CTA or phone clicks as primary conversions unless that is deliberately approved.
4. Test in GTM Preview with a real booking.

## Configuration
`window.FF_TRACKING_CONFIG` (optional, define before `tracking.js`) overrides event names, `confirmationPath`, `confirmationParam`, `storageKey`, `attrKeys`.

## Duplicate protection
Confirmation page: ignores visits without a valid `booking_ref`; stores counted refs in localStorage; refresh/revisit do nothing. If GHL redirects inside the iframe, the framed page posts the ref to the parent, which counts it once and does not load GTM in the frame.
