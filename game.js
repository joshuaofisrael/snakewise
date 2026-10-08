(()=>{const c=document.getElementById('c'),x=c.getContext('2d'),N=20,S=c.width/N,sc=document.getElementById('score'),be=document.getElementById('best');
let snake,dir,next,food,score,over,paused,best=+localStorage.getItem('slitherBest')||0;be.textContent=best;
const D={up:[0,-1],down:[0,1],left:[-1,0],right:[1,0]};
function place(){do{food=[Math.random()*N|0,Math.random()*N|0]}while(snake.some(p=>p[0]==food[0]&&p[1]==food[1]))}
function reset(){snake=[[10,10],[9,10],[8,10]];dir=next=D.right;score=0;over=paused=false;sc.textContent=0;place();draw()}
function turn(d){const v=D[d];if(v&&!(v[0]==-dir[0]&&v[1]==-dir[1]))next=v}
function step(){if(over||paused)return;dir=next;const h=[snake[0][0]+dir[0],snake[0][1]+dir[1]];
if(h[0]<0||h[1]<0||h[0]>=N||h[1]>=N||snake.some(p=>p[0]==h[0]&&p[1]==h[1])){over=true;if(score>best){best=score;localStorage.setItem('slitherBest',best);be.textContent=best}draw();return}
snake.unshift(h);if(h[0]==food[0]&&h[1]==food[1]){score++;sc.textContent=score;place()}else snake.pop();draw()}
function draw(){x.fillStyle='#fbfff0';x.fillRect(0,0,c.width,c.height);x.fillStyle='#f1fbe0';for(let i=0;i<N;i++)for(let j=(i%2);j<N;j+=2)x.fillRect(i*S,j*S,S,S);x.fillStyle='#ff3ec8';x.beginPath();x.arc(food[0]*S+S/2,food[1]*S+S/2,S/2.4,0,7);x.fill();
snake.forEach((p,i)=>{x.fillStyle=i?(i%2?'#6cc400':'#8be000'):'#7a2cff';x.fillRect(p[0]*S+1,p[1]*S+1,S-2,S-2)});
if(over||paused){x.fillStyle='rgba(255,255,255,.82)';x.fillRect(0,0,c.width,c.height);x.fillStyle='#163b31';x.font='600 30px Fredoka,system-ui';x.textAlign='center';x.fillText(over?'Game over':'Paused',c.width/2,c.height/2);x.font='16px system-ui';x.fillText(over?'Press Restart or Enter':'Press Space',c.width/2,c.height/2+30)}}
const K={ArrowUp:'up',ArrowDown:'down',ArrowLeft:'left',ArrowRight:'right',w:'up',s:'down',a:'left',d:'right'};
addEventListener('keydown',e=>{if(K[e.key]){e.preventDefault();turn(K[e.key])}else if(e.key==' '){e.preventDefault();if(!over){paused=!paused;draw()}}else if(e.key=='Enter'&&over)reset()});
let t0;c.addEventListener('touchstart',e=>{t0=e.touches[0]},{passive:true});c.addEventListener('touchend',e=>{if(!t0)return;const t=e.changedTouches[0],dx=t.clientX-t0.clientX,dy=t.clientY-t0.clientY;if(Math.max(Math.abs(dx),Math.abs(dy))>20)turn(Math.abs(dx)>Math.abs(dy)?(dx>0?'right':'left'):(dy>0?'down':'up'));t0=null});
document.querySelectorAll('.pad button').forEach(b=>b.onclick=()=>turn(b.dataset.d));document.getElementById('restart').onclick=reset;
reset();setInterval(step,120)})();
