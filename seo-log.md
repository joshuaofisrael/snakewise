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
- Legal: footer on every page now reads "© 2026 the LLC. All rights reserved. SnakeWise is owned and operated by the LLC." with Terms, Privacy, Disclaimer, About and Contact (mailto). New pages: /terms.html, /privacy.html, /disclaimer.html, /about.html (aadb939). Florida LLC, Florida governing law and venue (eba4fc4). JSON-LD publisher = the LLC (brand SnakeWise).
- Games (908583b): /games/ hub plus Lookalike Lab, Scale Snap and Shed Shuffle (original code and art, VideoGame JSON-LD, LLC publisher; credits at /games/CREDITS.md). game.html unchanged.
- Teachers (68d5dbc): /teachers/ hub, fact sheet, adaptations worksheet, answer keys, vocabulary, NGSS lesson ideas (PE codes checked on nextgenscience.org); /research/ with DOIs checked via Crossref and doi.org; cite boxes and last-reviewed dates; Teachers in nav and home tile.
- sitemap.xml now 31 URLs; llms.txt has About & legal, Games and For teachers sections.
- IndexNow HTTP 200 for legal pages, the Florida fix, games set, and the teachers/research set (11 URLs, 8 Oct). All new URLs verified 200 live with the LLC footer.
- Pending: photos and a /credits/ page (after 19:45, under the heavy-build lock); screenshots after 19:45.

## 2026-10-08 (late, ~23:20 BST) — Photos + /credits/ (commit 68ff5e9)
- 8 freely licensed Wikimedia Commons snake photos added as WebP (all <=800px wide, all <80 KB): rough green snake (home hero), ball python + California kingsnake (pets), corn snake + eastern hognose (species), eastern garter snake (myths), ring-necked snake (habitats), rosy boa (teachers/). Each has explicit width/height, descriptive alt text, loading=lazy, decoding=async and a caption with author, licence link and a link to /credits/.
- Licences: CC BY 2.0 x3 (Judy Gallagher; Linda Tanner; Virginia State Parks staff), CC BY 3.0 x1 (Holger Krisp), CC0 1.0 x3 (5snake5 x2; Jasper Shide), Public Domain Mark x1 (Benjamin Genter). Ring-necked snake cropped 48px at the top to remove the author's name watermark. Hognose re-encoded at 640px (800px could not get under 80 KB).
- New https://snakewise.org/credits/ (WebPage JSON-LD, LLC publisher): every photo with author, Commons source/original, licence link and changes; fonts (Fredoka, OFL); original artwork/games note; rights-holder contact.
- "Credits" link added to the footer on every page and the blog post template; /credits/ added to sitemap.xml (32 URLs) and llms.txt. No URL changes. Legal footer links intact. game.html (The Slither Game) untouched per the owner: byte-identical live.
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
- Live HTTP 200; IndexNow ping (post, /blog/, sitemap, llms.txt) done.

## 2026-10-10 (~02:00 BST) — Daily SEO: internal links to the two blog deep-dives
Data: still no Search Console query data (Personal assistant hasn't shared any). Crawl: every sitemap URL HTTP 200 with the Bingbot UA; repo in sync with origin.
Finding: the two cited blog deep-dives (sidewinder, paradise flying snake) were only linked from the blog index and species.html. movement.html, the closest topic page ("how do snakes move"), didn't link to either one, so the topic cluster wasn't connected.
Pick (priority 7, internal architecture; nothing in priorities 1 to 3 is actionable without GSC data): contextual links.
- movement.html: the Sidewinding card links to /blog/how-do-sidewinders-move.html, the Specialists (gliding) card links to /blog/paradise-flying-snake.html, and "Keep exploring" gains Snake fact blog.
- habitats.html: "Sidewinders" in the Deserts card links to the sidewinder post.
- Commit 3f27f9d. Verified live; IndexNow for movement + habitats returned HTTP 200. LLC footer untouched.
Why: it passes topical relevance and crawl paths from the hub page to the deep pages and strengthens the movement cluster.
Next: once GSC data shows up, update the scorecard; if the movement queries show impressions, expand movement.html (it's thin, about 5 short cards) with research-backed detail on each mode.

| 2026-10-10 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 33 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |

## 2026-10-11 (~02:05 BST) — Daily SEO: myths page restructured for question queries
Data: still no Search Console query data. Crawl/audit: all pages have a canonical and a title/meta; myths.html stood out as the weakest-structured core page (generic title "Snake Myths vs Facts", H1 "Myths vs facts", no subheadings, nine myths only as bold paragraphs, so none could match a question query or be linked individually).
Pick (priority 2/7, on-page structure for a core evergreen page; no GSC data to rank by winners yet): restructure myths.html without adding new factual claims.
- Each myth now has a question H2 and stable id (#slimy, #jaws, #head-shape, #baby-snakes, #chase, #first-aid, #deaf, #rattles, #eggs) plus a "Jump to" row (same style as the ID guide).
- FAQPage JSON-LD question names now match the H2s (were "Is it true that ..."); JSON parses.
- Contextual links: jaws/deaf → anatomy, head-shape → ID guide, chasing/first aid → safety; Keep exploring adds ID guide and Blog.
- Title "Snake Myths vs Facts: 9 Common Beliefs Debunked | SnakeWise", new question-led meta description, H1 "Snake myths vs facts"; sitemap lastmod 2026-10-11; llms.txt entry expanded.
- Commit 9fb0e6e. Verified live (HTTP 200, Bingbot UA), LLC footer intact. IndexNow ping for myths, sitemap, llms.txt sent.
Why: question-shaped headings target long-tail "do snakes chase people / are snakes slimy / are baby snakes more dangerous" queries and give AI search engines citable sections.
Next: same treatment for glossary.html (no per-term anchors) and pets.html title ("best pet snakes for beginners" intent) if GSC still shows nothing; expand movement.html once movement queries show impressions.

| 2026-10-11 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 33 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |

## 2026-10-11 (~10:50 BST) — Daily fact article: how long can a snake go without eating?
- New post /blog/how-long-can-a-snake-go-without-eating.html (question query "how long can a snake go without eating"), Burmese python profile: fasting strategies (McCue 2007: 168-day fast, resting metabolism down up to 72%, fat burned, protein spared), post-meal gut response (Secor & Diamond 1995), heart growth and regression (Andersen 2005, Riquelme 2011, Martin 2024). All six papers checked against PubMed/Crossref abstracts.
- Article + FAQPage JSON-LD (5 Qs, citations, Taxon), og:type article, internal links to anatomy, venom-constriction, species, habitats, safety, pets, shop and both earlier posts.
- Added to blog index, sitemap (lastmod 2026-10-11), llms.txt. Commit b9b94d5. Live HTTP 200, LLC footer present. IndexNow HTTP 200 (post, blog index, sitemap, llms.txt).
- Group post skipped: Animal Sites group chat no longer exists (since 9 Oct).

## 2026-10-12 (~02:00 BST) — Daily SEO: pets page retargeted to beginner pet snake questions
Data: still no Search Console query data. Crawl/audit: pets.html had the generic title "Snakes as Pets: The Basics", six label-style H2s and no anchors or FAQ markup, though "best pet snake for beginners" style queries carry the most commercial intent on the site (links to the future gear shop).
Pick (priority 2/7, on-page structure for a core evergreen page with commercial intent): restructure pets.html without adding new factual claims (Reptile Database fetch for size data came back empty, so no new numbers were added).
- Title "Pet Snakes for Beginners: Species, Setup, Feeding and Health | SnakeWise", question-led meta and og tags, H1 "Pet snakes for beginners", Article JSON-LD headline + dateModified.
- Six question H2s with ids (#right-for-you, #species, #enclosure, #heat, #feeding, #health), a "Jump to" nav (same markup as myths), FAQPage JSON-LD built from the existing answers (parses).
- Contextual links: species, safety, the fasting blog post; Keep exploring adds myths and blog. Sitemap lastmod 2026-10-12; llms.txt entry expanded.
- Commit b08c875. Live HTTP 200 (Bingbot UA), LLC footer intact. IndexNow ping for pets, sitemap, llms.txt.
Next: glossary.html per-term anchors and DefinedTermSet; later add a sourced beginner species comparison table (adult size, lifespan, origin) to pets.html once sources are opened and checked.

| 2026-10-12 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 33 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |

## 2026-10-12 (~10:50 BST) — Daily fact article: can snakes reproduce without mating?
- New post /blog/can-snakes-reproduce-without-mating.html (question query "can snakes reproduce without mating" / flowerpot snake), Brahminy blind snake (Indotyphlops braminus): obligate parthenogenesis, all-female, triploid 42 chromosomes (Wynn 1987, Ota 1991), draft and chromosome-level genomes (Khedkar 2022, Lv 2025). Papers opened and checked (Science Advances, Scientific Data, Amphibia-Reptilia abstract/DOI, AMNH Novitates abstract, Reptile Database).
- Article + FAQPage JSON-LD (5 Qs, citations, Taxon), og:type article, internal links to species, habitats, anatomy, myths, venomous-or-not, safety, shop and earlier posts; species.html Brahminy card now links here.
- Added to blog index, sitemap (lastmod 2026-10-12), llms.txt, fact-reports.md. No new photo (no PD/CC blind-snake asset on hand). Group post skipped: Animal Sites group chat no longer exists.

## 2026-10-12
- robots.txt: added explicit Allow groups for anthropic-ai, CCBot, Bytespider, Meta-ExternalAgent, cohere-ai (others already present).
- privacy.html, disclaimer.html: added Florida governing-law section (matches terms.html).
- Cloudflare Web Analytics: NOT added; box token valid but has no account access (accounts list empty, RUM API auth error). Site is not proxied by Cloudflare (GitHub Pages IPs, Namecheap DNS).
- IndexNow pinged for changed URLs.

## 2026-10-13 (~02:00 BST) — Daily SEO: glossary per-term anchors and DefinedTermSet
Data: still no Search Console query data. Audit: glossary.html was the weakest-structured evergreen page left (generic title "Snake Glossary", H1 "Glossary", 18 terms in a bare `<dl>` with no anchors, no links out, Article-only JSON-LD), so no single definition could be linked to or matched to a "what is ecdysis / what is a scute" style query. teachers/vocabulary.html mirrors the same term list as a printable and already links back to the glossary; both kept.
Pick (priority 2/7, on-page structure for a core evergreen page, continuing the 11 Oct myths / 12 Oct pets pattern): restructure glossary.html with no new definitions or factual claims (all 18 terms and their wording kept).
- Title "Snake Glossary: Brumation, Ecdysis, Elapid and More | SnakeWise", definition-led meta + og tags, H1 "Snake glossary"; lead paragraph unchanged.
- Every `<dt>` has a stable id (#brumation, #colubrid, #constriction, #ecdysis, #ectotherm, #elapid, #fang, #heat-pit, #herpetology, #jacobsons-organ, #neurotoxin, #oviparous, #viviparous, #ophiophagous, #scute, #spectacle, #venom, #viper) plus a "Jump to" nav (same markup as myths/pets).
- JSON-LD: Article (headline, dateModified 2026-10-13, LLC publisher, hasPart → set) + DefinedTermSet (#terms) with 18 DefinedTerm entries (name, existing description, url with #anchor, spectacle alternateName "brille"); both parse.
- Contextual links inside definitions only where the wording already points there: brumation → habitats, colubrid "most are harmless" → ID guide, constriction/elapid/neurotoxin → venom-constriction, ecdysis/heat pit/Jacobson's organ/scute/spectacle → anatomy, ectotherm → pets#heat, viviparous → habitats, venom → safety, fang → #venom, viper → #fang. Keep exploring adds myths, blog and the printable vocabulary list.
- Sitemap lastmod 2026-10-13; llms.txt glossary line lists the terms and anchor format.
- Commit 3afc97a. Live HTTP 200 (Bingbot UA): new title, #jacobsons-organ anchor, DefinedTermSet and LLC footer present. All 35 sitemap URLs return 200. IndexNow HTTP 200 (glossary, sitemap, llms.txt).
Why: per-term anchors + DefinedTerm markup let search and AI engines cite and deep-link an individual definition for short "what is X snake term" queries, and the in-definition links pass relevance to anatomy/venom pages.
Next: link term mentions on anatomy, venom-constriction and blog posts to glossary anchors (e.g. "ecdysis" → glossary.html#ecdysis) for a two-way internal link graph; then give movement.html or habitats.html the question-H2 + FAQ treatment; sourced beginner species table on pets.html once sources are checked.

| 2026-10-13 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 35 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |

## 2026-10-13 (~10:55 BST) — Daily fact article: Can snakes hear?
- Published /blog/can-snakes-hear.html ("Can Snakes Hear? How Snakes Hear Without Ears"), answer-first, ~1,150 words, quick facts, question H2s, 4-question FAQ, sources list. Targets "can snakes hear", "do snakes have ears", "how do snakes hear", "are snakes deaf".
- Sources opened and checked against abstracts/full text: Zdenek et al. 2023 PLOS ONE; Christensen et al. 2012 JEB; Young & Aguiar 2002 JEB; Friedel et al. 2008 PRL; Young 2003 Q Rev Biol. Hartline 1971 JEB dropped (could not open past Cloudflare).
- Article + FAQPage JSON-LD with 5 ScholarlyArticle citations; internal links to anatomy, safety, ID guide, pets, myths, species, shop and the sidewinder post. No images.
- Added to blog index (card + BlogPosting), sitemap (blog/ lastmod 2026-10-13), llms.txt. Commit da56f86. Live HTTP 200 with LLC footer. IndexNow pinged (post, blog/, sitemap, llms.txt).
- Animal Sites group chat no longer exists, so no group post.

## 2026-10-14 (~01:55 BST) — Daily SEO: anatomy and venom terms linked to glossary anchors
Data: still no Search Console query data. Crawl: all 36 sitemap URLs return HTTP 200 with the Bingbot UA; repo in sync with origin.
Pick (priority 7, internal architecture; follows the 13 Oct glossary restructure): make the glossary's new per-term anchors reachable from the topic pages that use those terms, so the link graph runs both ways. No wording or factual changes, only links on existing words.
- anatomy.html: Jacobson's → #jacobsons-organ, ventral scutes → #scute, ecdysis → #ecdysis, heat-sensing pits → #heat-pit.
- venom-constriction.html: neurotoxic → #neurotoxin, elapids → #elapid, Vipers → #viper, colubrids → #colubrid.
- Sitemap lastmod 2026-10-14 added for both pages. Commit 4ef9fe9. Live HTTP 200, 4 glossary anchor links on each page, LLC footer intact. IndexNow ping (anatomy, venom-constriction, sitemap).
- Blog posts checked: none use glossary terms in body text except "viper" in the sidewinder post (species context, not a definition need), so left alone.
- Daily news post: none (no news search done in this slot; no relevant story queued).
- Outreach: no emails sent; this routine's saved instruction doesn't cover sending outreach mail, so the 5/day allotment still needs a dedicated, approved outreach routine.
Next: question-H2 + FAQ treatment for movement.html or habitats.html; sourced beginner species table on pets.html once sources are checked.

| 2026-10-14 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 36 URLs in sitemap, all 200 | n/a | n/a | n/a | 0 (shop not live) |

## 2026-10-14 (~10:55 BST) — Daily fact article: How do king cobras build nests?
- Published /blog/how-do-king-cobras-build-nests.html ("How Do King Cobras Build Nests?"), answer-first, ~1,050–1,170 words, quick facts, question H2s, 4-question FAQ, sources list. Targets "how do king cobras build nests", "king cobra nest", "do king cobras build nests".
- Sources opened and checked: Dolia, Das & Kelkar 2023 Journal of Thermal Biology (ScienceDirect abstract + introduction; doi:10.1016/j.jtherbio.2023.103468) — 25 Himalayan nests ~3 °C warmer inside, nest temp predicts hatching success and hatchling length; Koirala & Tshering 2021 Reptiles & Amphibians full PDF (doi:10.17161/randa.v28i3.15786) — nest materials, 82.7×125 cm nest, guarding, 37 eggs / 34 hatch, 60–64 day incubation; Dolia 2018 Herpetology Notes full PDF — pine nest, nest sanitation, short guarding. Whitaker et al. 2013 Hamadryad not opened (no accessible PDF), so not cited as a primary source.
- Article + FAQPage JSON-LD with 3 ScholarlyArticle citations; internal links to species, habitats, safety, ID guide, venom-constriction, anatomy, shop, sidewinder and hearing posts. No images (licence unclear).
- Also linked the king cobra card on species.html to this post. Added to blog index (card + BlogPosting), sitemap (blog/ lastmod 2026-10-14), llms.txt, fact-reports.md.
- Animal Sites group chat no longer exists, so no group post; handoff draft prepared for parent.
- Commit 3ed51d5. Live HTTP 200 (Bingbot UA): title, FAQPage, doi:10.1016/j.jtherbio.2023.103468, LLC footer present. IndexNow HTTP 200 (post, blog/, sitemap, llms.txt, species).

## 2026-10-15 (~02:00 BST) — Daily SEO: movement page question H2s + FAQ; news post on venom and warning colours
Data: still no Search Console query data. Repo in sync with origin; old home address grep clean.
Pick (priority 2/7, on-page structure for a core evergreen page, same pattern as myths/pets/glossary): movement.html had a generic H1 "How Snakes Move", label-only H2s, no anchors, no FAQ, Article-only JSON-LD. No new facts added; FAQ answers reuse the page's existing wording.
- H1 "How do snakes move?"; question-led meta + og description.
- Section ids (#lateral-undulation, #concertina, #rectilinear, #sidewinding, #specialists) with descriptive question-style H2s and a "Jump to" nav (myths markup).
- 6-question FAQ section (#faq) + FAQPage JSON-LD; Article dateModified 2026-10-15; both parse.
- "Belly scales" linked to glossary.html#scute; Keep exploring adds glossary and games.
- Sitemap lastmod 2026-10-15; llms.txt line lists anchors and FAQ. Commit 1f5cda5. Live HTTP 200 (Bingbot UA) with #faq.
Daily news post: /blog/venomous-snakes-stand-out-colour-study.html ("Study: Venomous Snakes Are More Likely to Stand Out From Their Surroundings"), published 15 Oct.
- Sources: Duclaux, Dugon & Healy 2026, Journal of Animal Ecology, online 4 Oct 2026, doi:10.1111/1365-2656.70351 (title, authors, date and abstract checked via Crossref; Wiley page 403); University of Galway press release 5 Oct 2026 (opened, quotes taken from it). Facts used: 458 species, iNaturalist images, contextual conspicuousness metric, venomous significantly more conspicuous, red/yellow effective, no association with potency or pain.
- Own words, short attributed quotes, no images. NewsArticle JSON-LD with citations; visible publish date; internal links to ID guide, safety, myths, venom-constriction, Lookalike Lab, glossary#venom. Safety framing: colour alone is not an ID rule.
- Blog index card + BlogPosting, sitemap (post + blog/ lastmod), llms.txt. Commit 4e5e3fd. Live HTTP 200 with DOI and LLC footer.
- IndexNow HTTP 200 (movement, post, blog/, sitemap, llms.txt).
Outreach: 3 personalised pitches prepared and validated, not sent (see outreach-log.md); handed to the owner to send.
Next: link this news post from venomous-or-not.html; give habitats.html the question-H2 + FAQ treatment.

| 2026-10-15 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 37 URLs in sitemap | n/a | n/a | 0 | 0 (shop not live) |

## 2026-10-15 (~10:55 BST) — Daily fact article: How do sea snakes breathe through their skin?
- Published /blog/how-do-sea-snakes-breathe-through-their-skin.html ("How Do Sea Snakes Breathe Through Their Skin?"), answer-first, ~1,160 words, quick facts, question H2s, 4-question FAQ, sources list. Targets "can sea snakes breathe through their skin", "yellow-bellied sea snake breathing", "how long can sea snakes stay underwater".
- Sources opened and checked (abstracts via ScienceDirect, Springer, Crossref, PubMed E-utilities): Graham 1974 (skin O2 up to 33%, CO2 up to 94%, four benefits); Heatwole & Seymour 1975 (0–22% skin O2, all CO2 may leave via skin); Rubinoff, Graham & Motta 1986 (15 tagged snakes, 87% time underwater, 50 m, 213 min, dives exceed O2 stores, cutaneous uptake and/or low metabolism); Cook & Brischoux 2014 (S-shaped ~55 min dives, turbulence avoidance); Seymour & Webster 1975 (shunting limits skin O2 loss, may prevent bends); Graham, Gee & Robison 1975 (lung buoyancy); Heatwole & Seymour 1978 (skin uptake tracks aquatic adaptation); Shine et al. 2019 (sea snake skin often ~50% thicker); Lillywhite et al. 2014 (dehydrate at sea, drink freshwater lens). Reptile Database account; IUCN LC confirmed via SeaLifeBase (IUCN site needs login).
- Article + FAQPage JSON-LD with 9 ScholarlyArticle citations; original inline SVG diagram (no photos); internal links to anatomy, habitats, species, safety, ID guide, venom-constriction, movement, shop and three earlier posts. Linked the sea snake card on species.html to the post.
- Blog index card + BlogPosting, sitemap (post + species lastmod), llms.txt, fact-reports.md. Animal Sites group no longer exists; handoff text prepared for parent.
- Commit bd4c55f. Live HTTP 200 (Bingbot UA + plain): FAQPage, doi:10.1016/0034-5687(74)90002-4, LLC footer present. IndexNow HTTP 200 (post, blog/, sitemap, llms.txt, species).

## 2026-10-16 (~02:00 BST) — Daily SEO: habitats page question H2s + FAQ; news post on spectacled cobra genetics
Data: still no Search Console query data. Repo in sync with origin. The 15 Oct "Next" item to link the colour-study news post from venomous-or-not.html was already done (commit 29cd91b), so today's pick is the habitats page. Repo grep for the old home address: clean (only this log's earlier "grep clean" note matches).
Pick (priority 2/7, on-page structure for a core evergreen page, same pattern as movement/myths/pets/glossary): habitats.html had a generic H1, label-only H2s, no anchors, no FAQ, Article-only JSON-LD. No new facts added; FAQ answers reuse the page's existing wording.
- Title "Where Do Snakes Live? Snake Habitats Around the World"; H1 "Where do snakes live?"; question-led meta + og description.
- Section ids (#distribution, #rainforests, #deserts, #grasslands, #wetlands, #oceans, #cold-climates) with descriptive H2s and a "Jump to" nav (movement markup).
- 6-question FAQ (#faq) + FAQPage JSON-LD; Article headline updated, dateModified 2026-10-16; both parse.
- Contextual links on existing words: brumating → glossary#brumation, give birth to live young → glossary#viviparous; Oceans section links the sea snake skin-breathing article; Keep exploring adds glossary and blog.
- Sitemap lastmod 2026-10-16 (habitats was missing a lastmod); llms.txt line lists anchors and FAQ. Commit 86d608f. Live HTTP 200 with new H1, #faq, FAQPage and LLC footer.
Daily news post: /blog/sri-lankan-spectacled-cobras-distinct-lineage-study.html ("Study: Sri Lanka's Spectacled Cobras Form a Distinct Genetic Lineage"), published 16 Oct.
- Sources: Kanunjna, Gond, Unawane … Sunagar 2026, Molecular Phylogenetics and Evolution 223:108654, doi:10.1016/j.ympev.2026.108654 (title, journal, authors checked via Crossref; Elsevier page not opened); Mongabay, Malaka Rodrigo, 13 Oct 2026 (opened; Sunagar quotes); Phys.org, Krystal Kasal, 15 Oct 2026 (opened; paper quotes). Both reports agree on: 67 cobras, nine mito + nuclear markers, mainland largely panmictic, Sri Lankan lineage ~2 Mya with sea level a plausible (not proven) driver, African origin of Naja via Middle East in the Miocene, not declared a separate species. Background: Wüster & Tillack 2023 Zootaxa lectotype paper (cited via Mongabay).
- Own words, short attributed quotes, no images. NewsArticle JSON-LD with 4 citations; visible publish date; internal links to king cobra post, glossary#elapid, habitats#distribution, safety, ID guide #south-asia, venom-constriction, species, colour-study post.
- Blog index card + BlogPosting, sitemap (post + blog/ lastmod), llms.txt. Commits 6720bc6 + follow-up (ID guide anchor). Live HTTP 200 with DOI, NewsArticle and LLC footer.
- IndexNow HTTP 200 (habitats, cobra post, blog/, sitemap, llms.txt).
Outreach: 3 new personalised pitches prepared and validated, not sent (Australian Herpetological Society, Canadian Herpetological Society broken-link pitch, Tennessee Herpetological Society); see outreach-drafts-2026-10-16.md and outreach-log.md. Handed to the owner to send.
Next: species.html (core hub) question-H2 + FAQ treatment or a sourced comparison-table refresh; link the cobra news post from the spectacled cobra mention if species.html gains one; sourced beginner species table on pets.html once sources are checked.

| 2026-10-16 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 40 URLs in sitemap | n/a | n/a | 0 | 0 (shop not live) |

## 2026-10-16 (~10:55 BST) — Daily fact article: What is the smallest snake in the world?
- Published /blog/what-is-the-smallest-snake-in-the-world.html ("What Is the Smallest Snake in the World? Meet the Barbados Threadsnake"), answer-first, ~1,190 words incl. quick facts and FAQ, question H2s, 5-question FAQ, sources list. Targets "what is the smallest snake in the world", "barbados threadsnake", "how small is the smallest snake".
- Sources opened and checked: Hedges 2008 Zootaxa 1841 (full PDF via hedgeslab.org: max TOL 104 mm, holotype 0.60 g, single 2.2 × 13.7 mm egg, L. tanae males only, 193-species egg-shape analysis, hatchlings ~40–50 mm, ~40 km² sub-reef area, museum specimens 1889/1963/1918, flowerpot snake competitor); Adalsteinsson et al. 2009 (Crossref abstract: 116 spp., smallest/thinnest, Tetracheilostoma); Kley & Brainerd 1999 (Nature page abstract); Webb et al. 2000 (OpenAlex abstract: ant larvae/pupae, up to 350 items); Watkins et al. 1969 (OpenAlex abstract); Gehlbach & Baldridge 1987 (Springer summary); IUCN CR via Crossref DOI record + GBIF IUCN checklist (Daltry, Powell & Henderson 2016); Barbados Ministry of Environment pages (rediscovery 20 Mar 2025, ID differences); Re:wild 23 Jul 2025 release; Reptile Database account.
- Article + FAQPage JSON-LD (publisher LLC, 6 ScholarlyArticle + IUCN citations), og:type article; original inline SVG scale diagram (no photos); internal links to species, anatomy, glossary#oviparous, venom-constriction, habitats, ID guide, research, shop, flowerpot snake and sea snake posts. Linked the Barbados threadsnake card on species.html to the post.
- Blog index card + BlogPosting, sitemap (post + species lastmod), llms.txt, fact-reports.md (ideas line updated).
- Commit 0bfbaa9. Live HTTP 200 at ~10:58 BST (plain + Bingbot UA), FAQPage and LLC footer present. IndexNow HTTP 200 (post, blog/, sitemap, llms.txt, species).

## 2026-10-17 (~02:00 BST) — Daily SEO: species hub question-led title/H1, anchors + FAQ; news post on snake warning sounds
Data: still no Search Console query data. Repo in sync with origin. Repo grep for the old home address: clean (only this log's earlier notes match). Box RAM was low (~1.4 GB available), so no browser work was done; everything ran over curl and git.
Pick (priority 2/7, the 16 Oct "Next" item, same pattern as movement/myths/habitats): species.html is a core hub that answers high-volume superlative queries (longest, heaviest, most venomous, smallest snake) but had a label-style title/H1, no anchors and no FAQ. No new facts added; FAQ answers reuse the page's existing wording.
- Title "Snake Species Facts: Longest, Heaviest & Most Venomous Snakes"; H1 "Snake species facts: the longest, heaviest and most venomous snakes"; question-led meta + og description.
- Ids on the comparison table (#comparison) and all 12 species cards (#king-cobra … #barbados-threadsnake); table species names now link to their cards; "Jump to" nav (Comparison, Longest, Heaviest, Most toxic venom, Smallest, FAQ).
- 7-question FAQ (#faq) + FAQPage JSON-LD; Article headline updated, dateModified 2026-10-17; JSON parses. Keep exploring gains ID guide, glossary and blog links.
- Sitemap lastmod 2026-10-17; llms.txt line rewritten with anchors and FAQ. Commit 7b93758. Live HTTP 200 with FAQPage and LLC footer.
Daily news post: /blog/snakes-escalate-warnings-before-biting-study.html ("Study: Snakes Escalate Their Warning Sounds Before Biting, Across 73 Species"), published 17 Oct.
- Sources: Van Zele, Baeckens, Millet, Daniaud, Ksas, Jaeger, Calvez, Lengagne & Lourdais 2026, Functional Ecology, online 6 Oct 2026, doi:10.1111/1365-2435.70452, CC BY-NC 4.0 (title, authors, affiliations, date, licence and full abstract checked via Crossref; Wiley page 403); Figshare data record doi:10.6084/m9.figshare.32598069 (abstract matches); context: Van Zele et al. 2026 Proc R Soc B 293, doi:10.1098/rspb.2025.2698 (nose-horned viper hissing as honest signal; Crossref record + abstract). Facts used: 220 snakes, 73 species, four sound modes, three threat phases, signals longer/more intense with threat, biting mainly at high threat, mode-specific escalation, larger snakes less likely to confront.
- Own words, short attributed quotes from the abstract, no images. NewsArticle JSON-LD with 3 citations; visible publish date; internal links to safety, ID guide, myths#rattles, can-snakes-hear, venom-constriction, glossary#viper, colour-study post, species#eastern-diamondback, research. Framed as test-setting research, not a rule for human encounters.
- Blog index card + BlogPosting, sitemap (post + blog/ + safety lastmod), llms.txt. Safety page "If you see a snake" gains one sentence linking the post. Commit 32e1ae2. Live HTTP 200 with DOI, NewsArticle and LLC footer.
- IndexNow HTTP 200 (species, post, blog/, safety, sitemap, llms.txt).
Outreach: 2 new personalised pitches prepared and validated, not sent (PARC education resources; Georgia Reptile Society conservation page); see outreach-drafts-2026-10-17.md and outreach-log.md. Only 2 targets met the bar, so no third was forced. Handed to the owner to send after Shabbat.
Next: link the warning-sounds post from myths.html#rattles or the anatomy senses section if it fits; sourced beginner species table on pets.html once sources are checked; consider a short species.html note linking the spectacled cobra news post if a cobra comparison row is added with sources.

| 2026-10-17 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 42 URLs in sitemap | n/a | n/a | 0 | 0 (shop not live) |

## 2026-10-18 (~02:05 BST) — Daily SEO: BreadcrumbList structured data sitewide; myths internal links; news post on snake fungal disease
Data: still no Search Console query data, and still no analytics beacon. Re-tested the Cloudflare Web Analytics API: both box tokens (CLOUDFLARE_API_TOKEN, CLOUDFLARE_ANALYTICS_TOKEN) still return "Authentication error" (code 10000) on rum/site_info/list for account 8cd83313…, so a bot can't create the snakewise.org site; a beacon token is still needed from Personal assistant / the owner (privacy page must be updated when it's added). Repo in sync with origin. Repo grep for the old home address: clean. Following the 18 Oct SEO max directive (/workspace/seo/seo-max-directive-2026-10-18.md).
Pick (directive item 2, structured data; priority 7 architecture): no page had BreadcrumbList JSON-LD. Added Home > [Blog|Teachers|Games] > Page breadcrumbs to all 40 non-home pages (names from each page's H1; section index pages as Blog/Teachers/Games/Research/Credits) and to _templates/blog-post.html so future posts get it. All JSON-LD on the site parses (0 errors). Schema-only change, so sitemap lastmod was not bumped for those pages (no manufactured freshness).
- myths.html (the 17 Oct "Next" item): #deaf now links /blog/can-snakes-hear.html; #rattles gains one sentence restating the warning-sound study's already-published findings with a link to the post. Myths page previously linked no blog posts. Sitemap lastmod 2026-10-18.
- Commit e5de109. Live HTTP 200, BreadcrumbList present on sampled pages.
Daily news post: /blog/snake-fungal-disease-australia-biosecurity-study.html ("Study: Simple Hygiene Could Stop People Spreading Snake Fungal Disease"), published 18 Oct.
- Sources: Champagne, Butcher, Bourke, Seneci & Grogan 2026, Conservation Biology e70391, doi:10.1111/cobi.70391, 26 Sep 2026, CC BY 4.0 (title, authors, date, licence, abstract checked via Crossref); authors' article in The Conversation, 12 Oct 2026 (opened via Phys.org republication of 13 Oct; UQ Faculty of Science republication returns 200); background Butcher et al. 2026, Australian Veterinary Journal 104(6):376-384, doi:10.1111/avj.70060 (Crossref abstract: 10 cases, 5 species, Australia Zoo Wildlife Hospital 2023-24, first wild Australian O. ophidiicola cases, first N. barbatae in a snake, 9 of 10 PCR-confirmed died/euthanised).
- Own words, short attributed quotes, no images, hygiene steps framed as the researchers' guidance for trained handlers (not veterinary advice); includes the authors' caveat that there's no evidence yet of people spreading it between wild Australian populations. NewsArticle JSON-LD (3 citations) + BreadcrumbList; visible publish date; internal links to glossary#ecdysis, glossary#herpetology, safety, pets#health, venomous-or-not#australia, anatomy, habitats, cobra post, research, blog.
- pets.html#health gains one sentence (keep captive and wild reptiles and equipment apart) linking the post; sitemap lastmod 2026-10-18.
- Blog index card + BlogPosting, sitemap (post + blog/ + pets + myths lastmod), llms.txt. Commit b35aee3. Live HTTP 200 with LLC footer.
- IndexNow HTTP 200 (post, blog/, myths, pets, sitemap, llms.txt).
Outreach: 2 new personalised pitches prepared and validated, not sent (Gatorland Helpful Links broken-link pitch; Virginia Herpetological Society Educational Materials); see outreach-drafts-2026-10-18.md and outreach-log.md. Only 2 targets met the bar, so no third was forced.
Next: visible HTML breadcrumbs matching the JSON-LD (small nav above H1, styled in style.css); WebSite + Organization JSON-LD check on the homepage; sourced beginner species table on pets.html; add the CF beacon as soon as a token arrives.

| 2026-10-18 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 43 URLs in sitemap | n/a | n/a | 0 | 0 (shop not live) |

## 2026-10-18 (~09:50 BST) — Cloudflare Web Analytics beacon sitewide
Token confirmed: `94a41346ff174502afd7023a0a4c1c39` for snakewise.org in `/workspace/seo/cf-web-analytics-tokens-2026-10-18.json` (account JI Ventures Analytics 2). `audit-2026-10-18/audit.py` has no CF beacon token map (only IndexNow keys), so no mismatch; used the token file / Trends-bot value.
- Added `<script defer src='https://static.cloudflareinsights.com/beacon.min.js' data-cf-beacon='{"token": "94a41346ff174502afd7023a0a4c1c39"}'></script>` just before `</body>` on all 44 HTML files (every page, games, blog posts, 404.html, and `_templates/blog-post.html`). game.html game logic untouched (game.js still loads; beacon only inserted).
- privacy.html: replaced "no analytics" wording with cookieless Cloudflare Web Analytics disclosure; last updated 18 October 2026; dateModified 2026-10-18.
- IndexNow: homepage + privacy.html.
- Commit fc15051. Live curls: homepage, sea-snake blog post, and lookalike-lab game each contain beacon.min.js with token 94a41346ff174502afd7023a0a4c1c39. IndexNow HTTP accepted for / and privacy.html.

## 2026-10-18 (~11:00 BST) — Daily snake article: Which snake has the longest fangs? (Gaboon viper)
- Post: /blog/which-snake-has-the-longest-fangs.html ("Which Snake Has the Longest Fangs? The Gaboon Viper Explained"), ~1,190 words incl. FAQ, answer-first, question-style query. Original SVG fang-vs-ruler diagram (no photos).
- Sources (abstracts opened via PubMed/OpenAlex/Crossref; Broeckhoven 2017 and Spinner 2013 full text via PMC): Cundall 2009 doi:10.1086/594380; Broeckhoven & du Plessis 2017 doi:10.1098/rsbl.2017.0293; Marsh & Whaler 1984 doi:10.1016/0041-0101(84)90152-1; Marsh, DeRoos & Touger 2007 doi:10.1080/15563650600795693; Spinner et al. 2013 doi:10.1038/srep01846; Luiselli & Akani 2003 doi:10.1080/21564574.2003.9635485; Glaudas et al. 2017 doi:10.1111/jzo.12450; Jackson 2003 doi:10.1046/j.1096-3642.2003.00052.x; Vonk et al. 2008 doi:10.1038/nature07178; Kuch et al. 2006 doi:10.1007/s00114-005-0065-y; Smithsonian National Zoo, Saint Louis Zoo, Guinness and Reptile Database pages opened. Author names in JSON-LD checked against Crossref.
- Article JSON-LD (10 ScholarlyArticle citations) + FAQPage (5 Qs) + BreadcrumbList; internal links to species#gaboon-viper, glossary#fang, glossary#viper, venom-constriction, habitats, safety, venomous-or-not, research, shop, king cobra and smallest-snake posts.
- species.html Gaboon viper card links the post (lastmod 2026-10-18). Blog index card + BlogPosting, sitemap, llms.txt. Commit 22d3c0e. Live HTTP 200 with DOI, FAQPage and LLC footer.
- IndexNow HTTP 200 (post, blog/, species, sitemap, llms.txt).
- Animal Sites group chat no longer exists (since 9 Oct), so no group post; handed to parent as the routine directs.

## 2026-10-18 13:10 BST: contact page with working FormSubmit form
- Added /contact.html (neon style, ContactPage + BreadcrumbList JSON-LD, canonical, indexable, LLC footer, CF beacon). Form POSTs to https://formsubmit.co/joshuaofisrael@gmail.com with _subject "SnakeWise contact form", _template table, _captcha false (matches catwise/dogfieldguide/promptframed/smarttirepicks/noravelle), _next https://snakewise.org/thanks.html, _honey honeypot (display:none), labelled name/email/message fields.
- Added /thanks.html (noindex, follow; not in sitemap).
- Footer "Contact" link on every page (44 existing) + _templates/blog-post.html + new_post.py now points to /contact.html; footer email link kept and "or use our contact form" added.
- privacy.html updated: describes the contact form and FormSubmit (was "no contact form"). sitemap.xml + llms.txt updated.
- Commit 2cb89dd, live (200), IndexNow HTTP 200 (contact, privacy, sitemap, llms.txt).
- FormSubmit: test 1 at 13:09:46 BST triggered activation email ("Action Required: Activate FormSubmit on https://snakewise.org/contact.html"); activation link opened once 13:10 BST -> "Form Activated". Gmail received "SnakeWise contact form" at 13:10:17 BST and 13:10:24 BST from submissions@formsubmit.co. No emails sent or replied.

## 2026-10-19 (~01:55–02:15 BST) — Daily SEO: visible breadcrumbs sitewide; news post on Burmese python removal study
Data: still no Search Console query data; CF Web Analytics beacon present (token 94a41346…) and checked on the new post. Repo in sync with origin. Repo grep for the old home address: clean. Following the 18 Oct SEO max directive.
Pick (directive items 3/5, on-page + internal architecture; 18 Oct "Next" item): added visible HTML breadcrumbs (`<nav class="crumbs" aria-label="Breadcrumb"><ol>…`, last item aria-current="page") generated from each page's existing BreadcrumbList JSON-LD, so the visible trail matches the structured data exactly. Inserted at the top of `<main>` on all 43 inner pages + `_templates/blog-post.html` (index, 404 and thanks have no BreadcrumbList and were skipped). Styles appended to style.css (.crumbs, small muted text, › separators; hidden in print via existing nav rule). No content changes, so no lastmod bumps. Commit b1c4bd3; live (myths.html contains crumbs, style.css serves .crumbs).
Daily news post: /blog/burmese-python-removal-index-large-females-study.html ("Study: Removing Large Female Burmese Pythons Has the Biggest Impact"), published 19 Oct. First Burmese python content on the site (gap: big Florida invasive-species topic).
- Sources: Romer, Miller, Balaguera-Reina, Bassis, Welty, Kirkland, Peters, Metzger, Cole, Rodgers & Mazzotti 2026, Ecological Applications 36(6) e70317, doi:10.1002/eap.70317, first published 21 Sep 2026, CC BY 4.0 (title, authors, issue, licence, abstract checked via Crossref; Wiley page abstract); UF/IFAS News release by Lourdes Mederos, 28 Sep 2026 (HTTP 200), republished by Phys.org 1 Oct 2026 (opened). Story is ~3 weeks old; chosen because no newer snake news met the bar that wasn't already covered (cobra lineage, warning colour, fungal disease all done).
- Own words; short attributed quotes (Romer, Miller); framed as a researchers' decision-support tool, not an agency rule change; no images. NewsArticle JSON-LD (2 citations) + BreadcrumbList + visible crumbs; visible publish date; links to glossary#constriction, venom-constriction, safety, venomous-or-not#north-america, species#reticulated-python, habitats, fasting post, fungal post, research, blog.
- habitats.html#wetlands gains one sentence on invasive Burmese pythons in South Florida linking the post (lastmod 2026-10-19).
- Blog index card + BlogPosting, sitemap (post, blog/, habitats), llms.txt. Commit ad2fe01. Live HTTP 200 with DOI, LLC footer and beacon.
- IndexNow HTTP 200 (post, blog/, habitats, sitemap, llms.txt, myths, species, teachers/, games/, research/).
Outreach: see outreach-log.md (1 Yahoo pitch sent 01:55 London to the Australian Herpetological Society, confirmed in Sent). No new pitches drafted: candidates checked (Calusa Herp Society links page, site down; Gopher Tortoise Council Upland Snake Initiative, contact form only; SREL herp site, only an ID-request address) had no suitable published role address. Unsent queue is now short (Gmail: Gatorland; Yahoo: Tennessee HS, Georgia RS, Virginia HS), so the next run should draft 2–3, Gmail first.
Next: Burmese python card on species.html (only with verified, cited facts); WebSite + Organization JSON-LD check on the homepage; sourced beginner species table on pets.html; draft new Gmail pitches.

| 2026-10-19 | 7d | n/a (no GSC data yet) | n/a | n/a | n/a | 44 URLs in sitemap | n/a | n/a | 0 | 0 (shop not live) |

## 2026-10-19 10:45 slot: daily fact article
- Published https://snakewise.org/blog/how-do-egg-eating-snakes-eat-eggs.html (target query "how do egg-eating snakes eat eggs"), ~1,170 words, answer-first, original SVG diagram, Article (6 ScholarlyArticle citations) + FAQPage + BreadcrumbList JSON-LD, internal links to anatomy, species, habitats, ID guide, safety, research, shop and two blog posts. All 6 papers verified via Crossref/PubMed plus full text (Gartner & Greene 2008, Topper et al. 2026 PNAS) or abstracts (Barends & Maritz 2021/2025, Krupa & Slabach 2023, de Queiroz & Rodríguez-Robles 2006). Gans 1952 mentioned only as summarised by Gartner & Greene (not opened).
- Added to blog index, sitemap.xml, llms.txt; live 200 confirmed; IndexNow HTTP 200 (post, blog/, sitemap, llms.txt).
- Animal Sites group chat no longer exists (since 9 Oct), so the group post was handed to the parent.

## 2026-10-20 (~01:46–02:10 BST) — Daily SEO: sitewide social share image + og:url; news post on cartwheeling dwarf reed snakes
Data: still no Search Console query data; CF beacon present on all pages incl. the new post. Repo in sync. Old home address grep: clean (only mentioned in this log). Following 18 Oct SEO max directive (items 3 on-page/OG and 5 internal links today).
Pick: no page had og:image, so link shares on social/chat apps showed no preview. Made an original 1200x630 share card (/img/og-default.png, PIL-generated neon SnakeWise wordmark + snake; no third-party assets) and added og:image (+width/height/alt), twitter:image, og:url (from each page's canonical) and switched twitter:card to summary_large_image on all 49 HTML files incl. _templates/blog-post.html. anatomy.html related links gained 3 blog posts (egg-eating snakes, longest fangs, can snakes hear); egg-eating post had only 1 internal inlink. Commits ffeb892, aeb6e73. Live: homepage og:image tag served, image 200 image/png.
Daily news post: /blog/dwarf-reed-snakes-cartwheel-escape-study.html ("Study: Tiny Dwarf Reed Snakes Cartwheel to Escape, and Keep Their Heads Steady"), published 20 Oct.
- Sources: Kojima, Fukuyama, Hossman, Kaliang & Nishikawa 2026, Current Biology 36(20) R1061–R1063, doi:10.1016/j.cub.2026.08.057 (Crossref record checked; ScienceDirect blocked the box, abstract snippet only); Quah, Grismer & Anuar 2023 Biotropica doi:10.1111/btp.13213 (Crossref + abstract); Science News, Maria Temming, 19 Oct 2026 (opened in full). Facts used: 3 Pseudorabdion species (11 P. saravacense, 1 P. collaris, 1 P. longiceps) + 6 Calamaria from Kubah NP, Sarawak; 11–28 cm; 2.2 m racetrack; 1.7–3.7 m/s; all Pseudorabdion rolled, no Calamaria; heads held steady. Short attributed quotes (Kojima, Tingle). No images.
- NewsArticle JSON-LD (3 citations) + BreadcrumbList + visible crumbs; links to movement (+#lateral-undulation, #sidewinding), paradise flying snake, sidewinder post, myths, anatomy, research, blog. movement.html#specialists links the post (lastmod 2026-10-20).
- Blog index card + BlogPosting, sitemap, llms.txt. Commit 796cc6d. Live HTTP 200 with DOI, LLC footer and beacon.
- IndexNow HTTP 200 (14 URLs: post, blog/, movement, anatomy, sitemap, llms.txt, home, species, safety, ID guide, myths, habitats, teachers/, research/).
Outreach: see outreach-log.md. New-pitch research: Hoosier Herp Society Links & Materials (contact form only, no published address) and Chicago Herpetological Society (only a named officer's personal address) dropped; state DNR/extension snake pages had no external links section. No new drafts; Gmail queue is empty.
Next: Burmese python card on species.html (verified, cited); sourced beginner species table on pets.html; draft new Gmail pitches (zoo education/nature centre resource pages).

## 2026-10-20 — Safety warning box
- Added verbatim '⚠️ Safety Warning & Disclaimer' box (#safety-warning, role=note) under the H1/lead on species.html, venomous-or-not.html, Lookalike Lab, 14 species blog posts and _templates/blog-post.html (new_post.py inherits it). Added venom-caveat line linking #safety-warning beside the species table, all 6 regional ID tables and the Lookalike quiz. CSS in style.css (amber/red, AA contrast, mobile rule).
- Skipped: blog/index.html (listing), can-snakes-hear, snake-fungal-disease study (general topics, not species profiles).

## 2026-10-20 (~10:55–11:15 BST) — Daily fact article: garter snake mating balls
- Post: /blog/why-do-garter-snakes-form-mating-balls.html ("Why Do Garter Snakes Form Mating Balls? The Narcisse Snake Dens Explained"), ~1,200 words, answer-first, 5-question FAQ, safety warning box (template) + venom-caveat line, no images.
- Query targets: "why do garter snakes form mating balls", "garter snake mating ball", "Narcisse snake dens", "she-male garter snake".
- Sources (each opened via abstract/full text; claims limited to what they state): Shine et al. 2001 Nature doi:10.1038/35104687 (Nature page summary); Mason et al. 1989 Science doi:10.1126/science.2749261; Mason & Crews 1985 Nature doi:10.1038/316059a0; Shine, O'Connor & Mason 2000 Can J Zool doi:10.1139/z00-089; Shine et al. 2001 Evolution doi:10.1554/0014-3820(2001)055[0598:BITSDE]2.0.CO;2; Shine, Olsson & Mason 2000 BJLS doi:10.1111/j.1095-8312.2000.tb01229.x; Friesen et al. 2013 BJLS doi:10.1111/bij.12089; Shine et al. 2003 BES doi:10.1007/s00265-003-0620-5 (title claim only); Shine et al. 2004 Ecology and Society doi:10.5751/ES-00624-090109 (full text); Manitoba Natural Resources Narcisse page; Canadian Geographic.
- Article + FAQPage JSON-LD (9 ScholarlyArticle citations, about Taxon), og:type article, BreadcrumbList. Blog index card + BlogPosting, sitemap (blog/ lastmod 20 Oct), llms.txt. Commit b27ca1b. Live HTTP 200.
- IndexNow pinged (post, blog/, sitemap, llms.txt).
- Group post skipped: Animal Sites group chat no longer exists (since 9 Oct).
- Next: no pillar page mentions garter snakes yet; add a red-sided garter snake card on species.html linking this post (SEO run).

## 2026-10-21 (~01:55–02:05 BST) — Daily SEO (lean, scarce mode)
- species.html: added a red-sided garter snake profile card (#red-sided-garter-snake) using only facts already verified in the 20 Oct mating-balls post, linking to it; added a jump link; lead reworded so the "12 species" count matches the table. Sitemap lastmod 2026-10-21. Commit 7cc2f9d, live confirmed. IndexNow pinged (species, sitemap).
- Beacon check: all tracked HTML pages have the CF beacon. Old home address grep: clean.
- Daily news post: skipped (lean mode until 22 Oct reset; no can't-miss snake news).
- Outreach: Yahoo send skipped (scarce mode, browser sessions cut to a quarter); no new drafts (Yahoo queue: Georgia RS, Virginia HS; Gmail queue empty).

## 2026-10-23 (~01:10–01:30 BST) — Photos, design polish, contact check (the owner's rules via PA)
- 11 hyper-realistic AI photos (WebP, 89–150 KB each, 1.42 MB total) in /img/ai/, each checked visually (no cartoons/anatomy errors). Mood/habitat only, small caption "AI-generated image for illustration, not for identification." Lazy-loaded below the fold (hero images eager), width/height + descriptive alt. None on venomous-or-not.html, Lookalike Lab or other ID pages.
- Pages: index.html (hero + 3-up row), species.html, blog/index.html, 5 newest posts (garter mating balls, dwarf reed snakes, egg-eating snakes, Burmese python removal, longest fangs). Template + new_post.py updated (optional IMAGE + ALT args, figure omitted if none).
- style.css only: rounded corners, soft shadows, hover states, focus-visible, reduced-motion respected.
- Contact: /contact.html FormSubmit form to joshuaofisrael@gmail.com verified (honeypot, privacy line + link, _next=/thanks.html, thanks page indexable). Footer link to /contact.html present on all 51 HTML pages. Removed a duplicate breadcrumb on contact.html. Test AJAX POST ("SnakeWise contact form test") returned success:true; no new activation needed. Endpoint alias NOT switched (would need a new activation click).
- IndexNow pinged for changed URLs.

## 2026-10-23 (~01:50 BST) — Daily SEO

- **On-page (commit 8017224):** species.html gets a new "Burmese python (Python bivittatus), Invasive in South Florida" card (#burmese-python) and jump link. It uses only facts already verified in the 19 Oct Burmese python removal-index post, which it links to. A new FAQ, "Are Burmese pythons invasive in Florida?", is in both the visible FAQ and the FAQPage JSON-LD (8 Qs), with Article dateModified 2026-10-23. The Burmese post now links both the Burmese and reticulated python profiles. JSON-LD validated, live verified.
- **News post (commit 2af136d):** /blog/rattlesnake-venom-personality-study.html covers Martin & Hayes 2026, Frontiers in Ethology, doi:10.3389/fetho.2026.1918065 (published 8 Oct 2026; full text opened). Secondary source is the Phys.org Frontiers Dialog piece (21 Oct 2026). The study is 48 southern Pacific rattlesnakes with 3 voluntary-bite trials each, and all 5 measures were repeatable (R about 0.26–0.47). Original wording, no quotes, limits stated, no image. The AI macro had a round pupil, which would mislead on a pit viper. It carries NewsArticle JSON-LD, a visible date, the safety box, the LLC footer and the beacon. It's added to the blog index (card + BlogPosting), sitemap and llms.txt, with a contextual link from myths.html#baby-snakes (lastmod 2026-10-23). Live verified (HTTP 200, DOI, beacon).
- **IndexNow:** HTTP 200 for 7 URLs: species, the Burmese post, the rattlesnake post, blog/, myths, sitemap.xml, llms.txt.
- **Beacon check:** the Cloudflare Web Analytics beacon is on every HTML page, and new_post.py uses _templates/blog-post.html, which has it.
- **Address grep:** the old-address grep had 1 occurrence, a wording mention in this log (line 178), replaced with "old home address grep clean". The repo, including _templates, is now clean. Confirmed live on seo-log.md.
- **Outreach:** 0 new drafts (none met the bar), details in outreach-drafts-2026-10-23.md. Nothing sent.
- **Next:** a sourced beginner species table on pets.html, and a WebSite+Organization JSON-LD check on the homepage.

## 2026-10-23 AdSense site code
- Commit 9b42964: AdSense script + google-adsense-account meta in <head> of all 52 HTML pages (incl. _templates/blog-post.html); /ads.txt added; privacy.html Advertising section + cookie wording; no-ads claims neutralised (disclaimer, games, teachers, fact sheet). No ad units, no consent banner script.
- IndexNow: HTTP 200 for 49 URLs (all changed indexable pages).

## 2026-10-24 (~01:50–02:10 BST) — LLC rule + deferred one-time audit
- **LLC rule (commit 6fb1f71):** owner/LLC name now appears only on legal pages (terms, privacy, disclaimer, contact body). Footer on all 52 pages: "© 2026 SnakeWise. All rights reserved." + Terms/Privacy/Disclaimer/About/Credits/Contact links; footer contact line now points to the contact form (no email address in footer). JSON-LD author/publisher/copyrightHolder/about = Organization "SnakeWise" (92 objects). Cite-this-page blocks credit SnakeWise. About "Who runs" card replaced with a link to legal pages; about/credits/teachers email links replaced with contact-form links. llms.txt, games/CREDITS.md, blog template and new_post.py updated (new_post.py now asserts the footer and that no owner/LLC name is present). Added _config.yml excluding internal working files (seo-log.md, fact-reports.md, indexnow.sh, etc.) from Pages. Post-fix grep outside legal pages: 0 hits in tracked files. Beacon (52), AdSense tag (52), Safety Warning box (20) all retained. Verified live: /, /about.html, /shop.html, /blog/can-snakes-hear.html.
- **Audit (commit 7807c8c):** technical scan of 51 pages found no broken internal links, no canonical/og:url mismatches, all JSON-LD parses, sitemap complete; thanks.html given noindex; lastmod added to the 4 sitemap URLs that lacked it and bumped for changed pages. Added bite-emergency note on 10 pages, herpetologist/exotic-vet note on 4 pages (venomous-or-not, Lookalike Lab, pets, species), "Last reviewed" lines on 5 pages from their existing JSON-LD dateModified (glossary, habitats, movement, pets, species); pages with no date skipped (anatomy, myths, safety, venom-constriction, venomous-or-not, games, home, shop). IUCN claims: sea snake (Least Concern) and Barbados threadsnake (Critically Endangered, 2016 assessment) wording softened/dated; king cobra already cites Koirala & Tshering 2021. Titles over 65 chars / long descriptions left unchanged (not errors; avoid churning ranking titles). IndexNow pinged for all sitemap URLs.
- Daily news post: skipped (budget/Shabbat). No outreach.

## 2026-10-25 (~01:50 GMT) — Daily SEO
- Deferred items: none open (LLC rule + audit done 24 Oct).
- **Technical (commit 93618db):** the site had no favicon. Added /favicon.svg (the SnakeWise logo on a dark rounded square) and `<link rel="icon">` on all 52 HTML pages incl. _templates/blog-post.html, so new posts inherit it. Homepage WebSite + Organization JSON-LD merged into one linked @graph (@id refs, inLanguage, description, Organization logo). JSON validated; beacon 52/52, AdSense 52/52 retained. Live verified (/, /favicon.svg, /about.html all 200).
- IndexNow pinged for all sitemap URLs.
- Daily news post: skipped. Search only surfaced Catalogue of Life index entries for new Dendrelaphis/Lycodon/Oligodon species, not opened primary papers with confirmed dates; not enough to meet the verified-source bar this run.
- Outreach: paused per standing order; nothing sent or drafted. Old-address grep: clean.
- Next: sourced beginner species table on pets.html; consider a 48px PNG favicon fallback once an image converter is available.

## 2026-10-25 (~10:47–11:05 GMT) — Daily snake fact article
- **New post (commit a9509e5):** /blog/how-venomous-is-the-inland-taipan.html, "How Venomous Is the Inland Taipan? The World's Most Toxic Snake Venom" (~1,150 words, answer-first, FAQ). Built with _templates/new_post.py; Article JSON-LD enriched (description, dates, about Taxon, 9 ScholarlyArticle citations) + FAQPage; og:type article; Safety Warning box, venom-label caveat, bite-emergency note; footer matches garter post (no copyright line, no owner/LLC name). Beacon and AdSense tag retained. No image.
- Added to blog/index.html (card + BlogPosting), sitemap.xml (lastmod 2026-10-25, blog/ lastmod bumped), llms.txt. JSON-LD and sitemap XML validated.
- Live: HTTP 200 with new content. IndexNow pinged (post, blog/, sitemap.xml, llms.txt).
- Sources opened: PubMed abstracts for Morrison 1983, Hodgson 2007, Bell 1998, Tan 1993, Mirtschin 1984, Weinstein 2017, Weinstein 2025, Johnston 2017; PMC full text for Paz 2025; Australian Museum and Reptile Database pages. Broad et al. 1979 LD50 table not used (no abstract reachable).
- No outreach, no spend.


## 2026-10-26 (~01:50 GMT) — Daily SEO
- **Deferred items:** NamedScan fixes (Joshua via PA, 25 Oct) DONE.
- **Technical (commit 2078db1):** homepage "Snake FAQ" card (#faq, before </main>) with 6 Qs + separate FAQPage JSON-LD (@id https://snakewise.org/#faq); visible Q/A text verified identical to JSON-LD by script. Each answer has a Sources line. Bite and venom answers carry "Call local emergency services or poison control; don't rely on this site." Qs: snake bite first aid (NHS snake bites page, reviewed 17 Jul 2026; /safety.html); global snakebite burden (WHO fact sheet, 17 Sep 2026); most toxic venom (Morrison et al. 1983, PMID 6676477; taipan post); can snakes hear (Christensen et al. 2012, PMID 22189777; hearing post); fasting (McCue 2007, PMID 17644357; fasting post); smallest snake (Hedges 2008, Zootaxa 1841, Crossref abstract; smallest-snake post). All sources opened this run.
- sameAs: none. No SnakeWise social profiles exist (repo grep for x/twitter/instagram/facebook/pinterest/youtube/tiktok/bsky/reddit was empty), so it was skipped.
- AdSense head tags, beacon and site styling unchanged. Both JSON-LD blocks parse. Sitemap homepage lastmod is now 2026-10-26. Live on snakewise.org (FAQPage + #faq present).
- IndexNow: HTTP 200 (homepage + sitemap.xml).
- Daily news post: skipped. The best candidate (white-throated egg-eater Dasypeltis albigularis, Mongabay 9 Oct) is about 17 days old, its primary paper wasn't opened, and an egg-eating snake post already exists.
- Outreach: paused; nothing sent or drafted. No spend. Grep for "38609 Horton Drive": clean. No owner/LLC name and no © outside the legal pages.
- Next: sourced beginner species table on pets.html.

## 2026-10-26 (~10:50–11:00 GMT) — Daily snake fact article
- **New post (commit 025ba2c):** /blog/what-is-the-longest-snake-in-the-world.html, "What Is the Longest Snake in the World? The Reticulated Python Explained" (~1,100 words of body before FAQ, answer-first, 5-Q FAQ). Built with _templates/new_post.py; Article JSON-LD enriched (description, dates, about Taxa, 8 ScholarlyArticle citations) + FAQPage; og:type article; Safety Warning box, venom-label caveat, constriction/bite emergency note; no copyright line, no owner/LLC name. Beacon and AdSense tag retained. No image.
- Added to blog/index.html (card + BlogPosting), sitemap.xml (lastmod 2026-10-26, blog/ lastmod bumped), llms.txt. JSON-LD and sitemap XML validated.
- Live: HTTP 200 after ~2 min Pages build. IndexNow HTTP 200 (post, blog/, sitemap.xml, llms.txt).
- Sources opened: Natusch 2016 PLOS ONE full text; Headland & Greene 2011 PMC full text; Head 2009 PubMed abstract; Rivas 2023 abstract; Rivas 2024 Diversity full text; Rivas 2008 abstract; Barker 2012 (docslib text) + Foxon 2023 Bull CHS PDF; Smithsonian National Zoo and Reptile Database pages; Crossref metadata for all DOIs. Dropped: Shine 1999 (no abstract reachable), Guinness, ADW figures, Reynolds 2014 (abstract doesn't name Malayopython).
- No outreach, no spend.

## 2026-10-26 (~13:50–14:05 GMT) — SEO push (Joshua via PA: 1 view yesterday)
- **New page:** /blog/baby-copperhead-identification.html, "Baby Copperhead Identification: Yellow Tail, Bands and Look-Alikes" (targets "baby copperhead", "baby copperhead vs corn snake"; not previously covered). Answer-first, quick facts, copperhead vs corn snake table, bite-risk section, 5-Q FAQ. Article + FAQPage + Breadcrumb JSON-LD (validated), og:type article, Safety Warning box, venom-label caveat, bite emergency note; AdSense, beacon, favicon from template; no © / owner name.
- Sources opened: Pisani & Riedle 2018 (doi 10.1660/062.121.0417 abstract); R. Soc. Open Sci. 2022 fetal caudal luring (doi 10.1098/rsos.220218 abstract); Greene et al. 2021 (PMID 33046301); Parrish & Carr 1967 JAMA abstract; Walker & Morrison 2011 (PMID 21463771); Seifert et al. 2009 (PMID 19514880); UGA SREL copperhead page; Missouri DOC field guide. Not claimed: "babies more dangerous" myth (no peer-reviewed support found; said so).
- **Internal links:** new page linked from venomous-or-not.html (copperhead row), species.html (corn snake card), safety.html (If you see a snake), blog/snakes-escalate-warnings…, blog/rattlesnake-venom-personality…. Weakly linked posts fixed: species.html reticulated-python card → longest-snake post; inland-taipan card → taipan post.
- **Meta descriptions tightened (≤160 chars, meta+og/twitter):** safety, venom-constriction, anatomy, burmese-python-removal, dwarf-reed-snakes, snake-fungal-disease, snakes-escalate-warnings, sri-lankan-cobras (8; most were truncating at 180–220 chars). Titles untouched.
- blog/index.html (card + BlogPosting), sitemap.xml (new URL + lastmod bumps), llms.txt updated.
- Noted, not changed: privacy.html still says "no accounts or forms" though contact form exists (legal page; flag for review).
- No outreach, no spend, no heavy jobs.
- Live verified by curl (page, species.html link, sitemap). IndexNow HTTP 200 (15 URLs).
2026-10-26 16:22 | privacy.html: fixed 'no accounts or forms' meta wording, added not-sold/no-marketing + honeypot disclosure, dates 26 Oct (Joshua approved)

## 2026-10-27 (daily SEO, 01:45 slot)
- On-page: added a sourced "Beginner species at a glance" table to /pets.html (corn snake, ball python, California kingsnake, Kenyan sand boa; length and lifespan from Smithsonian's National Zoo, ADW and BGSU Herpetarium, checked 27 Oct). Last reviewed and dateModified bumped; sitemap lastmod 2026-10-27. Commit aa92558, live.
- News post: /blog/global-snakebite-burden-2026-study.html on Ediriweera et al. 2026 PLOS Medicine (doi:10.1371/journal.pmed.1005201), with Kasturiratne et al. 2008 for comparison; disability figure labelled as the authors' assumption. No image. Blog index card + BlogPosting JSON-LD, sitemap, llms.txt updated. Commit 9c0c73c, live. Safety box, beacon, AdSense present.
- IndexNow pinged for pets, new post, /blog/, sitemap, llms.txt.
- Outreach paused (standing order); nothing sent or drafted. 38609 Horton Drive grep clean on site pages. No spend.

## 2026-10-27 (daily article, 10:45 slot)
- Published /blog/can-snakes-see-heat.html, "Can Snakes See Heat? How Pit Vipers Sense Infrared" (~1,200 words, Article with 11 citations + FAQPage + Breadcrumb JSON-LD, safety box, internal links to species, anatomy, habitats, safety, ID guide, shop, can-snakes-hear, sidewinders). Main source Gracheva et al. 2010 Nature doi:10.1038/nature08943; all 11 papers' abstracts read on PubMed. No image. Added to blog index, sitemap.xml, llms.txt, fact-reports.md. Group post skipped (Animal Sites chat no longer exists). No spend.

- Live check: /blog/can-snakes-see-heat.html returned 200; IndexNow HTTP 200 (4 URLs).

## 2026-10-27 21:10 London: credits AI disclosure + legal-hold severity tiers
- credits/: removed the inaccurate "we do not use ... AI-generated images" line; now discloses that some illustrative images are AI-generated and captioned as such, with a table of the 11 img/ai files and the pages using them. Other credits unchanged. Joshua approved directly 27 Oct 21:03 London ("Reword the credits page to disclose the labelled AI images"); approvals.jsonl sha256 ad50a4ba6874500cfdc61aaed905460dc55f00247024d183a893cbc133a55730. Commit 5c8e02a; verified live; sitemap lastmod 2026-10-27; IndexNow pinged.
- hold_check.py/new_post.py: severity tiers per RULE.md amendment (HIGH 1/2/6/8 Joshua-only; MODERATE 3/4/5/7 fix, then independent chatgpt_review.py, clearance logged to moderate-clearances.jsonl by sha256).

## 2026-10-28 (daily SEO, 01:45 slot)
- On-page: tightened 18 over-long meta descriptions (164–197 chars, truncating in results) to 134–153 chars on 12 blog posts plus species, movement, credits, games, research and teachers; meta + og/twitter updated, wording trimmed from existing text only, no new facts. Legal pages (privacy, terms, disclaimer) left as is. Site-wide check: 0 broken internal links, all images have alt + width/height.
- News post: /blog/krait-cobra-bite-rapid-test-study.html on Thumtecho et al. 2026 Scientific Reports (open access, 17 Oct 2026), a prototype nanobody strip test for krait α-bungarotoxin; framed as lab proof of concept, spiked samples only, competing interests noted, bite emergency note. Abstract and declarations opened. No image. hold_check PASS via new_post.py. Blog index card + BlogPosting JSON-LD, sitemap, llms.txt updated.
- Outreach paused; nothing sent or drafted. 38609 Horton Drive and owner/LLC grep clean outside legal pages. No spend.
- Live verified (200); IndexNow pinged (12 URLs). Commit 8354ab9.
