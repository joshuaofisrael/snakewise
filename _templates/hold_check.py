#!/usr/bin/env python3
"""SnakeWise pre-publish legal-hold gate (JI Ventures rule, Joshua 27 Oct 2026; /workspace/content-review/RULE.md).
Usage:
  hold_check.py check FILE...          exit 0 = pass, 3 = HOLD_REVIEW (prints reasons)
  hold_check.py hold FILE TITLE        move FILE to drafts as HOLD_REVIEW + append queue.jsonl
Approval: a held item may publish only if /workspace/content-review/approvals.jsonl has a line with
{"site":"snakewise.org","sha256":<sha256 of the exact file>} - written by Joshua's approval, never by a bot.
CODE-ENFORCED: 2 (contact/address/phone patterns), 3 (every <img> needs a licence record), 4 (must cite >=1
external source link; no source = hold), 6 (any election wording), 8 (embargo/notice wording + restrictions list),
plus keyword tripwires for 1, 5, 7. Rules 1, 5, 7 (and source accuracy under 4) still need judgement."""
import sys,os,re,json,hashlib,datetime,shutil
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CR="/workspace/content-review"; Q=CR+"/queue.jsonl"; AP=CR+"/approvals.jsonl"; DR=CR+"/drafts/snakewise"
RESTRICT=CR+"/restrictions-snakewise.txt"  # one slug/path per line: blocked from (re)publication
OWN_DOMAINS=("snakewise.org","schema.org","googletagmanager.com","googlesyndication.com","google.com","formsubmit.co","fonts.googleapis.com","fonts.gstatic.com","w3.org","cloudflareinsights.com")
SITE_EMAIL_OK=("@snakewise.org","joshuaofisrael@gmail.com")  # site's published owner contact on legal/contact pages
def txt(h): return re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",re.sub(r"<(script|style)[^>]*>.*?</\1>"," ",h,flags=re.S|re.I)))
def sha(p): return hashlib.sha256(open(p,"rb").read()).hexdigest()
def approved(p):
    if not os.path.exists(AP): return False
    h=sha(p)
    for l in open(AP):
        try: j=json.loads(l)
        except: continue
        if j.get("sha256")==h and j.get("site") in ("snakewise.org","SnakeWise") and j.get("approved_by","").lower().startswith("joshua"): return True
    return False
KW={
 1:r"\b(fraud\w*|scam\w*|corrupt\w*|embezzl\w*|arrested|indicted|charged with|convicted|lawsuit|sued|misconduct|abus(e|ed|ive)|dishonest\w*|cover-?up|criminal)\b",
 5:r"\b(you should (take|inject|stop|start)|(recommended|safe|antivenom|human) dos(e|age)|take \d+ ?mg|invest(ment|ing)?|guaranteed returns?|tax advice|legal advice|how to (milk|extract) venom|handle (a )?venomous snake yourself|suck (out )?the venom|apply a tourniquet)\b",
 6:r"\b(election|ballot|polling (place|station)|voter registration|vote by|voting day|certified results?|electoral)\b",
 7:r"\b(official partner|endorsed by|in partnership with|certified by|approved by the|proves that|miracle|cure[sd]? (for )?snakebite|100% (safe|accurate))\b",
 8:r"\b(embargo(ed)?|cease and desist|dmca|takedown notice|legal notice|reporting restriction|correction request)\b",
}
def check(path,title=None):
    h=open(path,encoding="utf-8",errors="replace").read(); t=txt(h); R=[]
    body=t
    for n,rx in KW.items():
        for m in re.finditer(rx,body,re.I):
            if n==5 and re.search(r"\b(not|never|don'?t|do not|avoid)\b[^.]{0,25}$",body[max(0,m.start()-40):m.start()],re.I): continue
            R.append((n,m.group(0),"keyword tripwire; human review")); break
    # 2 sensitive personal info
    for m in re.finditer(r"[\w.+-]+@[\w-]+\.[\w.]+",t):
        if not m.group(0).lower().endswith(SITE_EMAIL_OK): R.append((2,m.group(0),"personal email address")); break
    for m in re.finditer(r"(?<![\w/.:-])(\+\d{1,3}[\s-]?)?\(?\d{3}\)?[\s-]\d{3}[\s-]\d{4}(?![\w-])",t):
        R.append((2,m.group(0).strip(),"possible phone number")); break
    m=re.search(r"\b\d{1,5}\s+[A-Z][a-z]+(\s[A-Z][a-z]+)*\s(Street|St|Road|Rd|Drive|Dr|Avenue|Ave|Lane|Ln|Court|Ct|Boulevard|Blvd)\b",t)
    if m: R.append((2,m.group(0),"possible street address"))
    # 3 content rights
    lic=json.load(open(os.path.join(ROOT,"img/ai/licence-record.json"))) if os.path.exists(os.path.join(ROOT,"img/ai/licence-record.json")) else {}
    cred=open(os.path.join(ROOT,"credits/index.html")).read()
    for src in re.findall(r"<(?:img|source|video)[^>]+src(?:set)?=\"([^\" ]+)",h,re.I):
        s=re.sub(r"^https?://snakewise\.org","",src)
        if s.startswith("data:image/svg"): continue
        if s.startswith("http") or not (s in lic or s in cred): R.append((3,src,"no documented licence record (add to credits/index.html or img/ai/licence-record.json, or drop the image)"))
    for src in re.findall(r"<iframe[^>]+src=\"([^\"]+)",h,re.I): R.append((3,src,"embedded third-party media"))
    # 4 unsupported claims: posts must cite an accessed external source
    if os.path.basename(path)!="index.html" and ("/blog/" in os.path.abspath(path) or os.path.abspath(path).startswith(DR)):
        ext=[u for u in re.findall(r"href=\"(https?://[^\"]+)",h) if not any(d in u for d in OWN_DOMAINS)]
        if not ext: R.append((4,"(no external source links)","post cites no source actually accessed"))
    # 8 restrictions list
    if os.path.exists(RESTRICT):
        b=os.path.basename(path)
        for l in open(RESTRICT):
            l=l.strip()
            if l and not l.startswith("#") and (l in path or l==b.rsplit(".",1)[0]): R.append((8,l,"listed restriction/complaint")); break
    return R
def hold(path,title,R,move=True):
    os.makedirs(DR,exist_ok=True); dst=os.path.join(DR,os.path.basename(path).replace(".html",".HOLD_REVIEW.html"))
    if os.path.abspath(path)!=os.path.abspath(dst): (shutil.move if move else shutil.copy)(path,dst)
    h=open(dst).read(); src=sorted(set(u for u in re.findall(r"href=\"(https?://[^\"]+)",h) if not any(d in u for d in OWN_DOMAINS)))[:20]
    line={"ts":datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),"site":"snakewise.org","bot":"SnakeWise bot","title":title,
          "flagged":"; ".join(f"[{n}] {f}" for n,f,_ in R),"rule":sorted(set(n for n,_,_ in R)),"sources":src,
          "suggestion":"; ".join(sorted(set(s for _,_,s in R))),"draft_path":dst,"sha256":sha(dst),"status":"HOLD_REVIEW"}
    open(Q,"a").write(json.dumps(line,ensure_ascii=False)+"\n"); return dst,line
if __name__=="__main__":
    a=sys.argv[1:]
    if a and a[0]=="check":
        bad=0
        for p in a[1:]:
            R=check(p)
            if R and not approved(p):
                bad=1; print("HOLD_REVIEW",p); [print(f"  rule {n}: {f!r} - {s}") for n,f,s in R]
            else: print("PASS" if not R else "PASS (Joshua-approved hash)",p)
        sys.exit(3 if bad else 0)
    if a and a[0]=="hold":
        R=check(a[1]) or [(0,"manual","held by bot judgement")]
        d,l=hold(a[1],a[2],R); print(json.dumps(l)); sys.exit(3)
    print(__doc__); sys.exit(2)
