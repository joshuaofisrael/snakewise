(function(){var K='mtm-analytics-consent',G='G-1CZBLC5B5V',d=document,L=false;
function load(){if(L)return;L=true;gtag('consent','update',{analytics_storage:'granted'});var s=d.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id='+G;d.head.appendChild(s);gtag('js',new Date());gtag('config',G);}
function get(){try{return localStorage.getItem(K)}catch(e){return null}}
function set(v){try{localStorage.setItem(K,v)}catch(e){}}
function close(){var b=d.getElementById('mtm-consent');if(b)b.remove();}
function show(){if(d.getElementById('mtm-consent'))return;var b=d.createElement('div');b.id='mtm-consent';b.setAttribute('role','dialog');b.setAttribute('aria-label','Analytics consent');
b.style.cssText='position:fixed;left:8px;right:8px;bottom:8px;z-index:9999;max-width:560px;margin:0 auto;background:#1f2a1f;color:#fff;padding:10px 12px;border-radius:8px;font:14px/1.4 system-ui,sans-serif;box-shadow:0 2px 10px rgba(0,0,0,.3)';
b.innerHTML='May we use Google Analytics cookies to see how the site is used? <a href="/privacy.html#analytics" style="color:#cfe8a9">Details</a> <span style="white-space:nowrap"><button class="acc" type="button" style="margin-left:6px;padding:4px 10px">Accept</button> <button class="rej" type="button" style="padding:4px 10px">Decline</button></span>';
b.querySelector('.acc').onclick=function(){set('granted');close();load();};
b.querySelector('.rej').onclick=function(){set('denied');close();gtag('consent','update',{analytics_storage:'denied'});var x=d.cookie.split(';');for(var i=0;i<x.length;i++){var n=x[i].split('=')[0].trim();if(n.indexOf('_ga')===0){d.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;domain=.'+location.hostname.replace(/^www\./,'');d.cookie=n+'=;expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/';}}};
d.body.appendChild(b);}
d.addEventListener('click',function(e){var t=e.target.closest&&e.target.closest('[data-consent-open]');if(t){e.preventDefault();try{localStorage.removeItem(K)}catch(x){}show();}});
var c=get();if(c==='granted')load();else if(c!=='denied')show();})();
