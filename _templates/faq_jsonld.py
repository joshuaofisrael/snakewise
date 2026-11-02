#!/usr/bin/env python3
"""Generate FAQPage JSON-LD from a page's own visible FAQ section, so the structured data can
never drift from (or be forgotten for) the on-page Q&A.

A "visible FAQ section" is the pattern already used across the site: a <section> whose first
heading is an <h2> containing "FAQ" (e.g. "FAQ", "Snake habitat FAQ"), followed by one or more
<h3>question</h3><p>answer</p> pairs. This module only reads that markup; it never invents or
rewords content.

Usage:
  faq_jsonld.py check FILE...   exit 1 and print any FILE with a visible FAQ but no FAQPage JSON-LD
  faq_jsonld.py build FILE      print the <script type="application/ld+json"> FAQPage tag (or
                                 nothing, exit 1, if the page has no visible FAQ section)
"""
import sys, re, json, html

TAG = re.compile(r"<[^>]+>")
SECTION = re.compile(r"<section[^>]*>\s*<h2[^>]*>([^<]*)</h2>(.*?)</section>", re.S | re.I)
QA = re.compile(r"<h3[^>]*>(.*?)</h3>\s*<p[^>]*>(.*?)</p>", re.S | re.I)
LDJSON = re.compile(r'<script type="application/ld\+json">(.*?)</script>', re.S)


def strip_tags(s):
    return re.sub(r"\s+", " ", TAG.sub("", html.unescape(s))).strip()


def find_faq_section(h):
    for m in SECTION.finditer(h):
        if "faq" in m.group(1).lower():
            return m.group(2)
    return None


def extract_qa(section_html):
    pairs = []
    for m in QA.finditer(section_html):
        q, a = strip_tags(m.group(1)), strip_tags(m.group(2))
        if q and a:
            pairs.append((q, a))
    return pairs


def faqpage_jsonld(h):
    """Return the FAQPage dict for this page's visible FAQ, or None if it has none."""
    section = find_faq_section(h)
    if not section:
        return None
    qa = extract_qa(section)
    if not qa:
        return None
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qa
        ],
    }


def build(path):
    data = faqpage_jsonld(open(path, encoding="utf-8").read())
    if not data:
        return None
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def has_faqpage(h):
    return any('"@type": "FAQPage"' in m.group(1) for m in LDJSON.finditer(h))


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "check":
        bad = 0
        for p in args[1:]:
            h = open(p, encoding="utf-8").read()
            if find_faq_section(h) and not has_faqpage(h):
                bad = 1
                print("MISSING FAQPage JSON-LD:", p)
        sys.exit(1 if bad else 0)
    if args and args[0] == "build" and len(args) > 1:
        tag = build(args[1])
        print(tag or "", end="")
        sys.exit(0 if tag else 1)
    print(__doc__)
    sys.exit(2)
