# SnakeWise SEO log

## 2026-10-07 — Day 1 (no Search Console data yet)
Audit: 12 static pages, mobile-friendly, fast (no images/frameworks, one small CSS file). Gaps: no structured data, thin OG, no 404, generic titles, no "unique" asset vs. results dominated by Wikipedia/National Geographic/zoo/wildlife sites. Main queries ("venomous snakes", "is this snake venomous", "snake species", "snake bite first aid") reward practical, region-specific answers and comparison tables.

Changes (highest EV first):
1. **New tool: /venomous-or-not.html** — region selector (N. America, UK/Europe, Australia, South Asia, Africa, Latin America) comparing venomous species with harmless lookalikes, plus safety caveat. Why: high-intent, underserved by generic lists; linked from nav, safety, habitats, species, home; added to sitemap.
2. **Species page**: added a comparison table (length, prey capture, range) and keyword-rich H1. Why: table/snippet eligibility for "biggest/longest snakes" type queries.
3. **Structured data**: WebSite + Organization (home), Article (content pages), FAQPage (myths). All truthful.
4. **Open Graph/Twitter**: og:type, og:site_name, twitter:card on all pages.
5. **Titles**: rewrote home, anatomy, movement, safety titles for query match/CTR.
6. **Custom 404.html** (noindex, absolute links).
7. Accessible SVG logo title. LLC footer retained on all pages.

Next ideas: verify Search Console once DNS live and submit sitemap; add original SVG diagrams (anatomy, movement); per-region ID pages only if impressions justify; add og:image.

## 2026-10-08 — IndexNow
- Key file: https://snakewise.org/a822d72a62a4cf99a3f79086eeace725.txt (key a822d72a62a4cf99a3f79086eeace725). robots.txt allows all bots (incl. Bingbot) and lists the sitemap.
- **Rule: every future publish/update must be pinged** with `./indexnow.sh <url> [url...]` (no args = submit all sitemap URLs). Add new pages to sitemap.xml first.

## 2026-10-08 — AI-search readiness
- robots.txt: kept `User-agent: * / Allow: /`; added explicit Allow groups for OAI-SearchBot, ChatGPT-User, GPTBot, PerplexityBot, Perplexity-User, ClaudeBot, Claude-SearchBot, Claude-User, Google-Extended, Applebot, Applebot-Extended, Bingbot, DuckAssistBot, Amazonbot; Sitemap line kept.
- New https://snakewise.org/llms.txt (llmstxt.org format, key pages + one-line descriptions, LLC line); added to sitemap.xml.
- Answer-first lead paragraphs added to home and all topic pages (anatomy, movement, venom-constriction, species, habitats, myths, safety, pets, glossary), summarising facts already on each page; no new claims.
- Titles: species → "Notable Snake Species: Facts & Comparison Table"; venom-constriction → "Venom vs Constriction: How Snakes Subdue Prey".
- JSON-LD checked and parses OK: WebSite+Organization (home), Article (topic pages + ID guide), FAQPage (myths).
- Verified: 28/28 HTTP 200 for home + venomous-or-not.html across all 14 crawler UAs. IndexNow ping for 13 changed URLs → HTTP 200; indexnow.sh now exits 0.
- Why: AI search/answer engines favour crawlable pages with a concise direct answer at the top and a machine-readable site map.

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| | 7d | | | | | | | | | |
| | 28d | | | | | | | | | |
| | 90d | | | | | | | | | |
