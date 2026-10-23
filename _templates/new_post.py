#!/usr/bin/env python3
"""Create a blog post from _templates/blog-post.html (includes the #safety-warning box near the top; footer includes Contact us + LLC ownership line + legal links).
Usage: python3 _templates/new_post.py SLUG "Title" "Meta description" "Answer-first lead" body.html [IMAGE_BASENAME "Alt text"]
IMAGE: a hyper-realistic, photographic, on-topic WebP (<=150 KB, 1152x864) saved as img/ai/IMAGE_BASENAME.webp. It is inserted after the safety box, lazy-loaded, with width/height, alt text and the small caption "AI-generated image for illustration, not for identification." Use mood/habitat photos only, never for species or venom identification; no cartoons, real people or events. If no image is given the figure is omitted.
Then add https://snakewise.org/blog/SLUG.html to sitemap.xml and run ./indexnow.sh <url>."""
import sys,os,html,datetime
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
assert "mailto:joshuaofisrael@gmail.com" in t and "SnakeWise is owned and operated by Joshua Israel Ventures LLC." in t and "/terms.html" in t and "/privacy.html" in t
os.makedirs(os.path.join(root,"blog"),exist_ok=True); open(os.path.join(root,"blog",slug+".html"),"w").write(t); print("blog/"+slug+".html")
