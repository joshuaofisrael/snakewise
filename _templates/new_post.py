#!/usr/bin/env python3
"""Create a blog post from _templates/blog-post.html (footer includes Contact us + LLC ownership line + legal links).
Usage: python3 _templates/new_post.py SLUG "Title" "Meta description" "Answer-first lead" body.html
Then add https://snakewise.org/blog/SLUG.html to sitemap.xml and run ./indexnow.sh <url>."""
import sys,os,html
slug,title,desc,lead,bodyf=sys.argv[1:6]
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t=open(os.path.join(root,"_templates/blog-post.html")).read()
for k,v in {"SLUG":slug,"TITLE":html.escape(title),"DESCRIPTION":html.escape(desc),"LEAD":html.escape(lead),"BODY":open(bodyf).read()}.items(): t=t.replace("{{"+k+"}}",v)
assert "mailto:joshuaofisrael@gmail.com" in t and "SnakeWise is owned and operated by Joshua Israel Ventures LLC." in t and "/terms.html" in t and "/privacy.html" in t
os.makedirs(os.path.join(root,"blog"),exist_ok=True); open(os.path.join(root,"blog",slug+".html"),"w").write(t); print("blog/"+slug+".html")
