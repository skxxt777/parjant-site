# parjant-site — Parjant & Kiet UGC portfolio

Static site, no build step: `index.html` + `images/`. Hosted on **Cloudflare Pages**, connected to this GitHub repo.
- Push to `master` = goes live (Cloudflare auto-deploys).
- Push any other branch = Cloudflare preview deployment (safe place to review changes).

## Media
- Images/logos: `images/` and `images/logos/` in this repo.
- Videos: Cloudflare R2 public bucket `https://pub-b69d4bdaeeb5433680b91e5cbe472e83.r2.dev/<name>.mp4`
  (brands-1..4, lifestyle-1..4, product-1..4, food-1..4, events-1..4, service-1..4). Not stored in git (`videos/` is ignored).
- New videos are uploaded by the owner in the Cloudflare dashboard (R2 → bucket → Upload); then reference the URL in the HTML.

## Working from a Claude session
- Claude's workspace cannot reach *.r2.dev or Cloudflare APIs (network allowlist) — no wrangler deploys, no R2 uploads from the shell. Deploy is via git push only.
- Preview locally: `python3 scripts/preview.py` (desktop + mobile screenshots, JS error + overflow check).
- Work on a branch, push it, let the owner review the Cloudflare preview, then merge to `master`.
