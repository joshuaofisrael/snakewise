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

Future blog posts: use `_templates/new_post.py` (template `_templates/blog-post.html`, not published by Jekyll) — footer includes Contact us mailto + LLC line.

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

## 2026-10-08 — Daily SEO (10:17 run): ID guide region deep links + FAQ
Data: no Search Console query data yet (domain live since 7 Oct ~20:10). Crawl: all 14 sitemap URLs HTTP 200, www → apex 301, robots allows all incl. Bingbot, GSC verification meta present on home.
Pick: the region ID guide (/venomous-or-not.html) is the site's only unique asset and targets the highest-intent queries ("venomous snakes in the UK", "coral snake vs milk snake", "is this snake venomous"). Before today the six region tables could not be linked or cited individually.
Changes:
- Each region section now has a stable id (#north-america, #uk-europe, #australia, #south-asia, #africa, #latin-america) plus a crawlable "Jump to" link row; the region selector reads and writes the URL hash. Without JS all regions remain visible.
- New "Snake identification FAQ" (6 Qs: UK venomous snakes, coral vs milk snake, triangular heads/slit pupils myth, tail-shaking non-rattlesnakes, cobra/krait lookalikes in South Asia, what to do if unsure), answered only from facts already in the tables/safety page; matching FAQPage JSON-LD (parses OK). Links to safety.html.
- llms.txt: region anchor links listed under the ID guide.
- Verified live; Bingbot UA 200; IndexNow ping for venomous-or-not.html + llms.txt → HTTP 200. LLC footer intact.
Why: passage/section-level ranking and AI citations for region-specific ID questions; direct answers for long-tail "is X venomous" queries.
Watch: once GSC data arrives, check which region queries show impressions; split a region into its own page only if it earns impressions.

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-08 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 14 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |
| | 28d | | | | | | | | | |
| | 90d | | | | | | | | | |
