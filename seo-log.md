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

## 2026-10-08 — Daily fact article #1 (11:43 routine): paradise flying snake
- New blog section: https://snakewise.org/blog/ (Blog JSON-LD), "Blog" added to the nav on every page and the post template, Blog tile on home.
- New post: https://snakewise.org/blog/paradise-flying-snake.html (answer-first lead, BlogPosting JSON-LD with about=Taxon and 5 citation entries, og:type article). Internal links to species, habitats, movement, ID guide, safety, shop; species.html paradise tree snake profile links to it.
- Sources opened and checked against each claim: Socha, O'Dempsey & LaBarbera 2005 JEB (doi:10.1242/jeb.01579); Socha 2006 JEB (doi:10.1242/jeb.02381); Yeaton, Ross, Baumgardner & Socha 2020 Nature Physics (doi:10.1038/s41567-020-0935-4); Socha 2002 Nature (doi:10.1038/418603a); Reptile Database species account. Conservation status skipped (IUCN listing could not be fetched to confirm).
- sitemap.xml (+2 URLs with lastmod), llms.txt Blog section, topic log in fact-reports.md.
- Verified live: post, /blog/, species, sitemap, llms.txt all HTTP 200 (Bingbot UA); LLC footer present. IndexNow ping of all 16 sitemap URLs (nav changed sitewide) sent.

## 2026-10-08 — Redesign, legal pages, games, teachers hub
- Design: the pastel restyle (aadb939) was replaced by a bright neon look (43a6cbe): lime/cyan/magenta glow on a light #fbfff2 base, dark neon footer, Fredoka headings, original SVG doodles. Body text 18.19:1 contrast and all text pairs WCAG AA; prefers-reduced-motion respected. style.css 2,590 -> 13,731 bytes.
- Legal: footer on every page now reads "© 2026 Joshua Israel Ventures LLC. All rights reserved. SnakeWise is owned and operated by Joshua Israel Ventures LLC." with Terms, Privacy, Disclaimer, About and Contact (mailto). New pages: /terms.html, /privacy.html, /disclaimer.html, /about.html (aadb939). Florida LLC, Florida governing law and venue (eba4fc4). JSON-LD publisher = Joshua Israel Ventures LLC (brand SnakeWise).
- Games (908583b): /games/ hub plus Lookalike Lab, Scale Snap and Shed Shuffle (original code and art, VideoGame JSON-LD, LLC publisher; credits at /games/CREDITS.md). game.html unchanged.
- Teachers (68d5dbc): /teachers/ hub, fact sheet, adaptations worksheet, answer keys, vocabulary, NGSS lesson ideas (PE codes checked on nextgenscience.org); /research/ with DOIs checked via Crossref and doi.org; cite boxes and last-reviewed dates; Teachers in nav and home tile.
- sitemap.xml now 31 URLs; llms.txt has About & legal, Games and For teachers sections.
- IndexNow HTTP 200 for legal pages, the Florida fix, games set, and the teachers/research set (11 URLs, 8 Oct). All new URLs verified 200 live with the LLC footer.
- Pending: photos and a /credits/ page (after 19:45, under the heavy-build lock); screenshots after 19:45.

## 2026-10-08 (late, ~23:20 BST) — Photos + /credits/ (commit 68ff5e9)
- 8 freely licensed Wikimedia Commons snake photos added as WebP (all <=800px wide, all <80 KB): rough green snake (home hero), ball python + California kingsnake (pets), corn snake + eastern hognose (species), eastern garter snake (myths), ring-necked snake (habitats), rosy boa (teachers/). Each has explicit width/height, descriptive alt text, loading=lazy, decoding=async and a caption with author, licence link and a link to /credits/.
- Licences: CC BY 2.0 x3 (Judy Gallagher; Linda Tanner; Virginia State Parks staff), CC BY 3.0 x1 (Holger Krisp), CC0 1.0 x3 (5snake5 x2; Jasper Shide), Public Domain Mark x1 (Benjamin Genter). Ring-necked snake cropped 48px at the top to remove the author's name watermark. Hognose re-encoded at 640px (800px could not get under 80 KB).
- New https://snakewise.org/credits/ (WebPage JSON-LD, LLC publisher): every photo with author, Commons source/original, licence link and changes; fonts (Fredoka, OFL); original artwork/games note; rights-holder contact.
- "Credits" link added to the footer on every page and the blog post template; /credits/ added to sitemap.xml (32 URLs) and llms.txt. No URL changes. Legal footer links intact. game.html (The Slither Game) untouched per Joshua: byte-identical live.
- Verified live with single curls: /credits/, /, pets, species, myths, habitats, teachers/, WebPs, sitemap, llms.txt all HTTP 200.
- IndexNow: 8 URLs (/credits/, /, pets, species, myths, habitats, teachers/, llms.txt) -> HTTP 200.
- Build script fixes: run_after_1945.sh time guard now blocks only weekdays 14:00-19:45 Europe/London (it blocked all weekday hours before 19:45 and used the box's CEST clock), and its inner flock was removed (it re-took the same lock as the caller and would deadlock).
- Screenshots (home + /games/, 1280x800 and 390x844): NOT taken. First headless Chrome run crashed (SIGTRAP in --single-process mode; flag since removed from shots.py), then box load rose to 115-155, above the 50 stop line, so the retry was held. Pending.

## Scorecard
| Date | Window | Impressions | Clicks | CTR | Avg pos | Indexed pages | Top100/20/10/3 queries | Growing pages | Declining pages | Conversions |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-10-08 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 14 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |
| | 28d | | | | | | | | | |
| | 90d | | | | | | | | | |

## 2026-10-09 (~11:05 BST) — Daily fact article: How do sidewinder snakes move?
- New post https://snakewise.org/blog/how-do-sidewinders-move.html (target query "how do sidewinders move" / "why do sidewinders move sideways"). Answer-first lead, quick facts, 8 question H2s, 5-question FAQ, sources list. Article JSON-LD (LLC publisher, about Taxon, 6 ScholarlyArticle citations) + FAQPage JSON-LD.
- Sources opened and checked against abstracts/full text (Crossref, Europe PMC, PMC): Marvi 2014 Science; Astley 2015 PNAS (PMC4434722); Secor, Jayne & Bennett 1992 JEB (Crossref abstract); Rieser 2021 PNAS (PMC8017952); Tingle 2020 ICB; Jayne 2020 ICB; Reptile Database (range, venomous, live-bearing, etymology). No images added.
- Internal links: movement, species, habitats, safety, ID guide, shop, paradise flying snake post. Added to blog index (card + Blog JSON-LD), sitemap.xml (blog/ lastmod 2026-10-09), llms.txt.
