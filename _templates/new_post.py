#!/usr/bin/env python3
"""Create a blog post from _templates/blog-post.html (includes the #safety-warning box near the top; footer: Contact form link + legal links (no copyright line; copyright appears only on legal pages); per 23 Oct rule the LLC/owner name appears only on legal pages).
Usage: python3 _templates/new_post.py SLUG "Title" "Meta description" "Answer-first lead" body.html [IMAGE_BASENAME "Alt text"]
IMAGE: a hyper-realistic, photographic, on-topic WebP (<=150 KB, 1152x864) saved as img/ai/IMAGE_BASENAME.webp. It is inserted after the safety box, lazy-loaded, with width/height, alt text and the small caption "AI-generated image for illustration, not for identification." Use mood/habitat photos only, never for species or venom identification; no cartoons, real people or events. If no image is given the figure is omitted.
Then add https://snakewise.org/blog/SLUG.html to sitemap.xml and run ./indexnow.sh <url>."""
import sys,os,html,datetime,json
d=datetime.date.today();M=["Jan.","Feb.","Mar.","Apr.","May","June","July","Aug.","Sept.","Oct.","Nov.","Dec."]
slug,title,desc,lead,bodyf=sys.argv[1:6]
img=sys.argv[6] if len(sys.argv)>6 else None; alt=sys.argv[7] if len(sys.argv)>7 else ""
assert not img or alt, "alt text required with image"
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t=open(os.path.join(root,"_templates/blog-post.html")).read()
import re
if img: assert os.path.exists(os.path.join(root,"img/ai",img+".webp")), "missing img/ai/"+img+".webp"; t=t.replace("{{IMAGE}}",img).replace("{{IMAGE_ALT}}",html.escape(alt,quote=True))
else: t=re.sub(r'<figure class="photo ai">.*?</figure>',"",t,flags=re.S)
for k,v in {"SLUG":slug,"TITLE":html.escape(title),"DESCRIPTION":html.escape(desc),"LEAD":html.escape(lead),"BODY":open(bodyf).read(),"DATE_LONG":f"{d.day} {d:%B %Y}","DATE_APA":f"{d.year}, {d:%B} {d.day}","DATE_MLA":f"{d.day} {M[d.month-1]} {d.year}","DATE_CHI":f"{d:%B} {d.day}, {d.year}"}.items(): t=t.replace("{{"+k+"}}",v)
assert "©" not in t and not any(b in t for b in ("Jos"+"hua","Ventures "+"LLC")) and "/contact.html" in t and "/disclaimer.html" in t and "/terms.html" in t and "/privacy.html" in t
# Legal-hold gate (RULE.md, 27 Oct 2026): check BEFORE anything enters the published tree.
sys.path.insert(0,os.path.join(root,"_templates")); import hold_check as hc
os.makedirs(hc.DR,exist_ok=True); tmp=os.path.join(hc.DR,slug+".html"); open(tmp,"w").write(t)
R=hc.check(tmp)
FIX=os.environ.get("SW_MODERATE_FIX","")  # describe the fix made; MODERATE tripwire items then go to the independent reviewer
if R and not hc.approved(tmp) and hc.sev(R)=="MODERATE" and FIX:
    ok,v=hc.moderate_review(tmp,FIX,title); print("MODERATE review:",json.dumps(v)[:400])
    if ok: R=[]
if R and not hc.approved(tmp) and not hc.moderate_cleared(tmp,R):
    print("SEVERITY:",hc.sev(R),"(HIGH = Joshua only; MODERATE = fix, then rerun with SW_MODERATE_FIX=\"what you fixed\")")
    d,l=hc.hold(tmp,title,R); print("HOLD_REVIEW: NOT published. Draft:",d)
    for n,f,s in R: print(f"  rule {n}: {f!r} - {s}")
    sys.exit(3)
os.makedirs(os.path.join(root,"blog"),exist_ok=True); os.replace(tmp,os.path.join(root,"blog",slug+".html")); print("PASS blog/"+slug+".html")
