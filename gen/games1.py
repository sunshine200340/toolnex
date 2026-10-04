# -*- coding: utf-8 -*-
"""Toolnex original games, batch 1: Arcade, Racing, Sports."""

CANVAS_STAGE = """<div class="stage-head">
<div class="stat">{stats}</div>
<button id="btnRestart" type="button">Restart</button>
</div>
<canvas id="gameCanvas" width="720" height="480"></canvas>
<div class="hint">{hint}</div>"""

GAMES_A = []

# ---------------------------------------------------------------- Color Rush
GAMES_A.append(dict(
    file="block-puzzle.html", name="Color Rush Reflex", category="arcade",
    category_label="Arcade", icon="🎨",
    tagline="Spot the target color in a shifting grid and tap it before your streak resets.",
    meta="Play Color Rush Reflex free on Toolnex. Test your color recognition speed in this fast, family-friendly browser game - no download, no sign-up.",
    about="""<p>Color Rush Reflex is a pure reaction game built around one of the hardest things for the human eye: telling near-identical colors apart under time pressure. Each round shows you a target color at the top of the board; your job is to find and tap the matching tile before the clock eats your streak.</p>
<p>It sounds easy - until the palette starts sneaking in shades that are only a few steps apart. Rounds get faster as your score climbs, so the game stays challenging whether you are on your first run or your fiftieth.</p>""",
    howto=["Look at the target color shown above the grid.",
           "Click or tap the tile that matches it exactly.",
           "Each correct tap scores a point and reshuffles the board.",
           "Three wrong taps end the run - the grid also speeds up as you score."],
    tips=["Name the color out loud in your head - verbalizing beats eyeballing under pressure.",
          "Scan by rows instead of jumping around the grid.",
          "Warm up on slower runs before chasing a high score; reaction time improves noticeably after a few rounds.",
          "On mobile, hold the phone slightly further away so more tiles stay in your field of view."],
    faq=[("Is Color Rush Reflex free to play?", "Yes - it runs entirely in your browser with no downloads, accounts or payments."),
         ("Does the game work on phones and tablets?", "Yes. The grid resizes automatically and supports touch input."),
         ("How is my score saved?", "Your best score is stored locally in your browser, so you can chase your record any time.")],
    stats='<span>Score: <b id="crScore">0</b></span><span>Lives: <b id="crLives">3</b></span><span>Time: <b id="crTime">60</b>s</span>',
    hint="Click / tap the tile matching the target color",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const COLORS=[['Coral','#ff6b6b'],['Mint','#34d399'],['Amber','#f59e0b'],['Ocean','#38bdf8'],['Violet','#8b5cf6'],['Teal','#14b8a6'],['Rose','#fb7185'],['Lime','#a3e635']];
let grid=[],target=null,score=0,lives=3,t=60,running=false,timer=null;
function shuffle(){grid=[];const pool=[...COLORS].sort(()=>Math.random()-.5);for(let i=0;i<8;i++)grid.push(pool[i]);grid.sort(()=>Math.random()-.5);target=grid[Math.floor(Math.random()*8)];}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#E2E8F0';cx.font='bold 26px Inter';cx.textAlign='center';cx.fillText('Find: '+target[0],360,56);
cx.fillStyle=target[1];cx.fillRect(320,70,80,18);
const s=140,g=14,x0=(720-4*s-3*g)/2,y0=120;
grid.forEach((c,i)=>{const x=x0+(i%4)*(s+g),y=y0+Math.floor(i/4)*(s+g);cx.fillStyle=c[1];
cx.beginPath();cx.roundRect(x,y,s,s,16);cx.fill();});}
function pos(e){const r=cv.getBoundingClientRect();const p=e.touches?e.touches[0]:e;return[(p.clientX-r.left)*(720/r.width),(p.clientY-r.top)*(480/r.height)];}
function pick(ev){if(!running)return;const[mx,my]=pos(ev);const s=140,g=14,x0=(720-4*s-3*g)/2,y0=120;
const col=Math.floor((mx-x0)/(s+g)),row=Math.floor((my-y0)/(s+g));
if(col<0||col>3||row<0||row>3)return;const c=grid[row*4+col];
if(c[1]===target[1]){score++;document.getElementById('crScore').textContent=score;shuffle();draw();}
else{lives--;document.getElementById('crLives').textContent=lives;if(lives<=0)end();}}
function end(){running=false;clearInterval(timer);cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#E2E8F0';cx.font='bold 34px Inter';cx.textAlign='center';cx.fillText('Time! Score: '+score,360,220);
const best=+localStorage.getItem('crBest')||0;if(score>best)localStorage.setItem('crBest',score);
cx.font='18px Inter';cx.fillStyle='#94A3B8';cx.fillText('Best: '+Math.max(best,score)+' - press Restart to play again',360,260);}
function start(){score=0;lives=3;t=60;running=true;document.getElementById('crScore').textContent=0;
document.getElementById('crLives').textContent=3;shuffle();draw();
clearInterval(timer);timer=setInterval(()=>{t--;document.getElementById('crTime').textContent=t;if(t<=0)end();},1000);}
cv.addEventListener('mousedown',pick);cv.addEventListener('touchstart',e=>{e.preventDefault();pick(e);},{passive:false});
document.getElementById('btnRestart').addEventListener('click',start);start();""",
))

# ---------------------------------------------------------------- Neon Dash
GAMES_A.append(dict(
    file="neon-runner.html", name="Neon Dash", category="arcade",
    category_label="Arcade", icon="⚡",
    tagline="An endless neon runner - jump the obstacles, chase your best distance.",
    meta="Play Neon Dash free in your browser. A fast one-button neon runner with rising speed and local high scores. No download needed.",
    about="""<p>Neon Dash is a one-button runner distilled to its essentials: you are a glowing square, the city scrolls past, and obstacles keep coming faster. One tap makes you jump; your timing decides everything.</p>
<p>The challenge curve is deliberately honest - the first few obstacles arrive at a jog, and the game only reveals its real pace once you have proven you can keep up. Most players' first run ends around 200 meters. Beating 1,000 means you have real rhythm.</p>""",
    howto=["Press Space / click / tap to jump.",
           "Hold the jump slightly longer for a higher leap (jump height scales with hold time).",
           "Clear every obstacle - hitting one ends the run.",
           "Distance is your score; the world speeds up the further you go."],
    tips=["Jump late, not early - most beginners bail out too soon and clip the obstacle's far edge.",
          "Listen to the rhythm of obstacles: they arrive in patterns, not randomly.",
          "When the speed steps up, focus on the ground line rather than the obstacle itself.",
          "Short taps for low blocks, held taps for tall ones."],
    faq=[("Is there a way to pause?", "The run is deliberately short (most last under a minute) - use the Restart button between runs."),
         ("Why did my high score reset?", "Scores live in your browser's local storage; clearing site data resets them."),
         ("Does Neon Dash work offline?", "Once the page has loaded, the game itself runs without a connection.")],
    stats='<span>Distance: <b id="ndDist">0</b>m</span><span>Best: <b id="ndBest">0</b>m</span>',
    hint="Space / click / tap to jump - hold for a higher jump",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const G=0.55,LIFT=-11.5,FLOOR=400;
let y=FLOOR-40,vy=0,holding=false,speed=6,dist=0,obs=[],spawn=60,alive=true,frame=0;
document.getElementById('ndBest').textContent=localStorage.getItem('ndBest')||0;
function reset(){y=FLOOR-40;vy=0;speed=6;dist=0;obs=[];spawn=40;alive=true;}
function jump(){if(!alive){reset();return;}if(y>=FLOOR-41){vy=LIFT;holding=true;}}
function step(){if(!alive)return;frame++;dist+=speed/10;speed=Math.min(14,6+dist/400);
document.getElementById('ndDist').textContent=Math.floor(dist);
if(holding&&vy<-4)vy+=0.32;else holding=false;
vy+=G;y=Math.min(FLOOR-40,y+vy);
if(--spawn<=0){const h=30+Math.random()*40,w=22+Math.random()*26;
obs.push({x:760,w,h});spawn=55+Math.random()*50-speed;}
obs.forEach(o=>o.x-=speed);obs=obs.filter(o=>o.x>-60);
for(const o of obs){if(700-40<o.x+o.w&&700+o.w*0>o.x&&y+40>FLOOR-o.h){alive=false;
const best=+localStorage.getItem('ndBest')||0;
if(dist>best){localStorage.setItem('ndBest',Math.floor(dist));document.getElementById('ndBest').textContent=Math.floor(dist);}
break;}}
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.strokeStyle='#1E3A8A';cx.lineWidth=2;
for(let i=0;i<8;i++){const yy=80+i*45;cx.beginPath();cx.moveTo(0,yy);cx.lineTo(720,yy);cx.globalAlpha=.12;cx.stroke();}
cx.globalAlpha=1;cx.fillStyle='#38BDF8';cx.fillRect(0,FLOOR,720,3);
obs.forEach(o=>{cx.fillStyle='#F472B6';cx.fillRect(o.x,FLOOR-o.h,o.w,o.h);
cx.fillStyle='rgba(244,114,182,.25)';cx.fillRect(o.x,FLOOR-o.h,o.w,6);});
cx.fillStyle='#FBBF24';cx.shadowColor='#FBBF24';cx.shadowBlur=18;cx.fillRect(700-40,y,40,40);cx.shadowBlur=0;
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Crashed at '+Math.floor(dist)+'m',360,200);cx.font='16px Inter';cx.fillStyle='#94A3B8';
cx.fillText('Press Space or tap to run again',360,235);}}
setInterval(()=>{if(alive)draw();},1000/60);
cv.addEventListener('mousedown',jump);cv.addEventListener('touchstart',e=>{e.preventDefault();jump();},{passive:false});
document.addEventListener('keydown',e=>{if(e.code==='Space'){e.preventDefault();jump();}});
document.getElementById('btnRestart').addEventListener('click',()=>{reset();});
requestAnimationFrame(step);""",
))

# ---------------------------------------------------------------- Bubble Pop
GAMES_A.append(dict(
    file="bubble-pop.html", name="Bubble Pop Adventure", category="arcade",
    category_label="Arcade", icon="🫧",
    tagline="Aim, bounce and pop matching bubbles before the wall closes in.",
    meta="Play Bubble Pop Adventure free online. Aim and shoot bubbles to match three and clear the board in this classic casual browser game.",
    about="""<p>Bubble Pop Adventure is a compact take on the classic bubble-shooter formula. A wall of colored bubbles hangs over your cannon; fire bubbles upward, cluster three or more of a color, and the whole group pops.</p>
<p>Every few shots, a fresh row pushes the wall downward. Clear the entire board to win the round; let the wall reach the firing line and the run is over. The bounce mechanic - firing off the side walls - is where the skill lives.</p>""",
    howto=["Move your mouse (or drag) to aim the cannon; a dotted guide shows your line.",
           "Click or release to fire the current bubble.",
           "Match 3+ connected bubbles of the same color to pop them.",
           "Clear all bubbles to win; every 3 shots add a new row at the top."],
    tips=["Bank shots off the side walls reach clusters that have no direct line.",
          "Pop from the bottom of a group - everything left hanging above gets cleared with it.",
          "Think two shots ahead: the next bubble color is always shown next to the cannon.",
          "Prioritize colors with the fewest bubbles left on the board to unlock corners."],
    faq=[("How many levels are there?", "Each cleared board deals a fresh, harder layout - the game continues as a score chase."),
         ("Can I play with a keyboard?", "Bubble Pop is designed around aiming, so mouse or touch is required."),
         ("Is it suitable for young children?", "Yes - there is no timer pressure in the aiming phase, making it a calm pick-up-and-play game.")],
    stats='<span>Score: <b id="bpScore">0</b></span><span>Shots until new row: <b id="bpRow">3</b></span>',
    hint="Move to aim - click to fire",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const COLORS=['#ff6b6b','#34d399','#38bdf8','#f59e0b','#8b5cf6'];
const R=18,ROWS=5,COLS=16,LINE=430;
let board,cannon={x:360,y:445},cur,nxt,score=0,shots=0,proj=null,angle=-Math.PI/2,alive=true;
function newBoard(){board=[];for(let r=0;r<ROWS;r++){const row=[];const off=r%2;
for(let c=0;c<COLS-off;c++)row.push(COLORS[Math.floor(Math.random()*COLORS.length)]);board.push(row);}}
function reset(){newBoard();score=0;shots=0;proj=null;alive=true;cur=randC();nxt=randC();
document.getElementById('bpScore').textContent=0;}
function randC(){return COLORS[Math.floor(Math.random()*COLORS.length)];}
function drawBoard(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
board.forEach((row,r)=>{const off=r%2;row.forEach((col,c)=>{if(!col)return;
const x=c*2*R+R+off*R,y=r*2*R+R+10;
cx.fillStyle=col;cx.beginPath();cx.arc(x,y,R,0,7);cx.fill();
cx.fillStyle='rgba(255,255,255,.35)';cx.beginPath();cx.arc(x-R/3,y-R/3,R/3.2,0,7);cx.fill();});});
cx.strokeStyle='rgba(244,63,94,.6)';cx.setLineDash([8,6]);cx.beginPath();cx.moveTo(0,LINE);cx.lineTo(720,LINE);cx.stroke();cx.setLineDash([]);
cx.strokeStyle='rgba(148,163,184,.5)';cx.setLineDash([4,8]);
cx.beginPath();cx.moveTo(cannon.x,cannon.y);
cx.lineTo(cannon.x+Math.cos(angle)*160,cannon.y+Math.sin(angle)*160);cx.stroke();cx.setLineDash([]);
cx.fillStyle=cur;cx.beginPath();cx.arc(cannon.x,cannon.y,R,0,7);cx.fill();
cx.fillStyle=nxt;cx.beginPath();cx.arc(cannon.x+42,cannon.y+8,10,0,7);cx.fill();
cx.fillStyle='#E2E8F0';cx.font='13px Inter';cx.textAlign='left';
cx.fillText('next',cannon.x+28,cannon.y+30);}
function neighbors(r,c){const off=r%2,res=[];
[[0,-1],[0,1],[-1,-1],[-1,0],[1,-1],[1,0]].forEach(d=>{let nc=c+d[1];let nr=r+d[0];
if(nr%2)nc=c+Math.max(d[1],0);if(d[1]===0)nc=c+d[1];
res.push([nr,nc]);});
return res.filter(([nr,nc])=>nr>=0&&nr<board.length&&nc>=0&&nc<(board[nr].length)&&board[nr][nc]);}
function fire(){if(proj||!alive)return;proj={x:cannon.x,y:cannon.y,vx:Math.cos(angle)*11,vy:Math.sin(angle)*11,col:cur};
cur=nxt;nxt=randC();}
function land(x,y){const r=Math.floor((y-10)/(2*R)),off=r%2;
const c=Math.floor((x-off*R)/(2*R));
if(!board[r])board[r]=[];board[r][c]=proj.col;proj=null;resolve(r,c);}
function resolve(r,c){const col=board[r][c],grp=[[r,c]],seen=new Set([r+','+c]),stack=[[r,c]];
while(stack.length){const[cr,cc]=stack.pop();
[[0,-1],[0,1],[-1,-1],[-1,0],[1,-1],[1,0],[1,1]].forEach(d=>{let nr=cr+d[0],nc=cc+d[1];
if(nr%2&&d[1]!==0)nc=cc+d[1]-(d[1]<0?0:0);
if(nr%2===0&&d[1]!==0)nc=cc+d[1];
if(nr<0||nr>=board.length||nc<0||nc>=(board[nr]?board[nr].length:0))return;
if(!board[nr][nc]||board[nr][nc]!==col)return;
const k=nr+','+nc;if(seen.has(k))return;seen.add(k);grp.push([nr,nc]);stack.push([nr,nc]);});}
if(grp.length>=3){grp.forEach(([gr,gc])=>{if(board[gr])board[gr][gc]=null;});
score+=grp.length*10;document.getElementById('bpScore').textContent=score;
if(board.every(row=>row.every(v=>!v))){win();return;}}
shots++;const left=3-(shots%3);document.getElementById('bpRow').textContent=left===3?3:left;
if(shots%3===0){board.unshift(Array.from({length:COLS},()=>Math.random()<.85?COLORS[Math.floor(Math.random()*COLORS.length)]:null));
board.forEach(row=>{while(row.length<COLS)row.push(null);});
let maxR=0;board.forEach((row,r)=>{if(row.some(v=>v))maxR=r;});
if((maxR+1)*2*R+10>=LINE){alive=false;msg('Game over - the wall got too low!');}}
if(board.flat().every(v=>!v))win();}
function win(){alive=false;score+=200;document.getElementById('bpScore').textContent=score;msg('Board cleared! +200 bonus');}
function msg(t){cx.fillStyle='#E2E8F0';cx.font='bold 26px Inter';cx.textAlign='center';cx.fillText(t,360,240);}
function loop(){if(!alive){drawBoard();msg(proj===null&&!alive?'Game over - press Restart':'');return;}
if(proj){proj.x+=proj.vx;proj.y+=proj.vy;
if(proj.x<R||proj.x>720-R){proj.vx*=-1;proj.x=Math.max(R,Math.min(720-R,proj.x));}
if(proj.y<=10+R){land(proj.x,10+R);}
else{outer:for(let r=0;r<board.length;r++){const off=r%2;
for(let c=0;c<board[r].length;c++){if(!board[r][c])continue;
const bx=c*2*R+R+off*R,by=r*2*R+R+10;
if((proj.x-bx)**2+(proj.y-by)**2<(2*R-4)**2){land(proj.x,proj.y);break outer;}}}}}
drawBoard();if(proj){cx.fillStyle=proj.col;cx.beginPath();cx.arc(proj.x,proj.y,R,0,7);cx.fill();}
requestAnimationFrame(loop);}
function aim(e){const r=cv.getBoundingClientRect();const p=e.touches?e.touches[0]:e;
const mx=(p.clientX-r.left)*(720/r.width),my=(p.clientY-r.top)*(480/r.height);
angle=Math.atan2(my-cannon.y,mx-cannon.x);angle=Math.max(-Math.PI+.35,Math.min(-.35,angle));}
cv.addEventListener('mousemove',aim);
cv.addEventListener('mousedown',e=>{aim(e);fire();});
cv.addEventListener('touchstart',e=>{e.preventDefault();aim(e);fire();},{passive:false});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();loop();""",
))

# ---------------------------------------------------------------- Fruit Slice
GAMES_A.append(dict(
    file="fruit-ninja.html", name="Fruit Slice Challenge", category="arcade",
    category_label="Arcade", icon="🍉",
    tagline="Swipe to slice flying fruit - but never touch the bombs.",
    meta="Play Fruit Slice Challenge free online. Swipe to slice fruit and dodge bombs in this fast arcade browser game for all ages.",
    about="""<p>Fruit Slice Challenge takes the satisfying feel of swiping through fruit and packs it into a light, family-friendly browser game. Fruit arcs across the screen in bunches; drag your cursor (or finger) through them to slice, and chain multiple fruits in one swipe for combo bonuses.</p>
<p>The catch: every few throws hides a bomb. Slicing a bomb costs a life, and so does letting fruit fall uncut. Three mistakes and the run ends.</p>""",
    howto=["Drag across a flying fruit to slice it - a single swipe can cut several.",
           "Each sliced fruit scores one point; cutting 4+ in one swipe doubles the bonus.",
           "Avoid the black bombs - slicing one costs a life.",
           "Missing fruit (letting it fall) also costs a life. Three lives total."],
    tips=["Wait for fruit to cluster near the top of their arc before swiping - one motion, several fruits.",
          "Small circles are safer than long slashes when bombs are on screen.",
          "Watch the shadows: fruit that is about to fall shows a dropping shadow first.",
          "Stay calm with combos - a greedy slash near a bomb is how runs end."],
    faq=[("Is Fruit Slice Challenge violent?", "Not at all - fruit simply splits into bright pieces with a pop effect. It is suitable for all ages."),
         ("Can I play on a touchscreen?", "Yes - the game was designed touch-first; a finger swipe works exactly like the mouse."),
         ("Why do some fruits give more points?", "Golden fruits appear rarely and are worth 5 points each - always prioritize them.")],
    stats='<span>Score: <b id="fsScore">0</b></span><span>Lives: <b id="fsLives">3</b></span>',
    hint="Drag across fruit to slice - avoid bombs",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const FRUIT=[['🍎','#ef4444'],['🍊','#f97316'],['🍋','#eab308'],['🥝','#84cc16'],['🍑','#f472b6']];
let items=[],score=0,lives=3,alive=true,spawn=30,frame=0,trail=[],combo=0,comboT=0;
function reset(){items=[];score=0;lives=3;alive=true;spawn=20;frame=0;
document.getElementById('fsScore').textContent=0;document.getElementById('fsLives').textContent=3;}
function spawnItem(){const isBomb=Math.random()<.16;
const isGold=!isBomb&&Math.random()<.08;
const[emoji,col]=FRUIT[Math.floor(Math.random()*FRUIT.length)];
items.push({x:60+Math.random()*600,y:500,vx:(Math.random()-.5)*4,vy:-13-Math.random()*3,
r:isBomb?24:26,bomb:isBomb,gold:isGold,emoji:isBomb?'💣':(isGold?'🌟':emoji),col:isBomb?'#111':col,sliced:false});}
function step(){frame++;
if(alive&&--spawn<=0){const n=1+Math.floor(Math.random()*3);
for(let i=0;i<n;i++)spawnItem();spawn=45+Math.random()*40;}
items.forEach(it=>{it.x+=it.vx;it.y+=it.vy;it.vy+=0.32;});
items.forEach(it=>{if(!it.sliced&&it.y>560){if(!it.bomb){miss();}it.dead=true;}});
items=items.filter(i=>!i.dead);
comboT--;if(comboT<=0)combo=0;
draw();requestAnimationFrame(step);}
function miss(){lives--;document.getElementById('fsLives').textContent=lives;
if(lives<=0){alive=false;}}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.strokeStyle='rgba(56,189,248,.25)';cx.lineWidth=1;
for(let i=1;i<6;i++){cx.beginPath();cx.moveTo(0,i*80);cx.lineTo(720,i*80);cx.stroke();}
trail.forEach((p,i)=>{cx.strokeStyle='rgba(251,191,36,'+(i/trail.length)+')';
cx.lineWidth=4;cx.beginPath();cx.moveTo(p[0],p[1]);if(trail[i+1])cx.lineTo(trail[i+1][0],trail[i+1][1]);cx.stroke();});
items.forEach(it=>{cx.font=it.r*2+'px serif';cx.textAlign='center';cx.textBaseline='middle';
cx.fillText(it.emoji,it.x,it.y);});
if(combo>1){cx.fillStyle='#FBBF24';cx.font='bold 24px Inter';cx.textAlign='center';
cx.fillText('Combo x'+combo+'!',360,60);}
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Run over - score: '+score,360,220);cx.font='16px Inter';cx.fillStyle='#94A3B8';
cx.fillText('Press Restart to play again',360,255);}}
function slice(e){if(!alive)return;const r=cv.getBoundingClientRect();const p=e.touches?e.touches[0]:e;
const mx=(p.clientX-r.left)*(720/r.width),my=(p.clientY-r.top)*(480/r.height);
trail.push([mx,my]);if(trail.length>12)trail.shift();
let hit=0;
items.forEach(it=>{if(it.sliced)return;
if((mx-it.x)**2+(my-it.y)**2<(it.r+14)**2){it.sliced=true;it.dead=true;
if(it.bomb){miss();}else{hit++;score+=it.gold?5:1;}}});
if(hit>0){combo++;comboT=40;if(combo>=4){score+=combo;}}
if(hit>0){document.getElementById('fsScore').textContent=score;}}
setInterval(()=>{if(trail.length)trail.shift();},50);
cv.addEventListener('mousemove',e=>{if(e.buttons)slice(e);});
cv.addEventListener('touchmove',e=>{e.preventDefault();slice(e);},{passive:false});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))

# ---------------------------------------------------------------- Skyline Speed
GAMES_A.append(dict(
    file="speed-race.html", name="Skyline Speed Race", category="racing",
    category_label="Racing", icon="🏎️",
    tagline="Weave through city traffic, grab stars, and push your speed to the limit.",
    meta="Play Skyline Speed Race free online. Dodge traffic and collect stars in this fast 3-lane racing game - playable instantly in your browser.",
    about="""<p>Skyline Speed Race puts you in the driver's seat of a city racer with one job: survive the traffic. Three lanes of oncoming cars, collectible stars that boost your score multiplier, and a speedometer that only ever goes up.</p>
<p>Unlike endless runners, the challenge here is lane discipline - the game punishes panic-swerving, because the car in front of you is often slower than the one about to appear beside it. Clean, patient driving beats reflex mashing.</p>""",
    howto=["Use ← → (or A/D, or tap the left/right half of the screen) to change lanes.",
           "Avoid every traffic car - a collision ends the run.",
           "Collect stars for bonus points and a brief speed shield.",
           "Your speed climbs the longer you survive; distance is your base score."],
    tips=["Look two cars ahead, not at your own bumper - the game shows upcoming traffic early.",
          "Pick the lane with the widest gap, not the closest star.",
          "The shield from a star absorbs exactly one collision - use it deliberately on the busiest lanes.",
          "On touch screens, tap early: lane changes animate for a moment and cannot be cancelled."],
    faq=[("How do I get a higher score?", "Distance sets the base; stars multiply it. A star collected at high speed is worth triple."),
         ("Are there different cars?", "The current release focuses on one finely-tuned car; more garages are planned."),
         ("Can I pause mid-run?", "Runs are short by design - use Restart between runs to reset cleanly.")],
    stats='<span>Distance: <b id="srDist">0</b></span><span>Score: <b id="srScore">0</b></span><span>Speed: <b id="srSpeed">180</b> km/h</span>',
    hint="← → / A D to change lanes - on touch, tap left or right side",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const LANES=[180,360,540],CARW=64,CARH=104;
let lane=1,x=LANES[1],traffic=[],stars=[],dist=0,score=0,speed=5,alive=true,spawnT=40,frame=0;
function reset(){lane=1;x=LANES[1];traffic=[];stars=[];dist=0;score=0;speed=5;alive=true;spawnT=30;
document.getElementById('srDist').textContent=0;document.getElementById('srScore').textContent=0;}
function move(d){if(!alive){reset();return;}lane=Math.max(0,Math.min(2,lane+d));}
function step(){frame++;if(!alive){draw();return;}
x+=(LANES[lane]-x)*.18;dist+=speed;speed=Math.min(11,5+dist/4000);
document.getElementById('srDist').textContent=Math.floor(dist/10)+'m';
document.getElementById('srSpeed').textContent=Math.floor(140+speed*22);
if(--spawnT<=0){const l=Math.floor(Math.random()*3);
if(Math.random()<.28)stars.push({x:LANES[l],y:-40,lane:l});
else traffic.push({x:LANES[l],y:-CARH,lane:l,speed:.6+Math.random()*.5});
spawnT=Math.max(22,60-Math.floor(speed*3));}
traffic.forEach(t=>t.y+=speed*t.speed);stars.forEach(s=>s.y+=speed*.8);
traffic=traffic.filter(t=>t.y<560);stars=stars.filter(s=>s.y<560);
const py=380;
traffic.forEach(t=>{if(t.lane===lane&&Math.abs(t.y-py)<CARH-14){alive=false;
cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Crashed! Score: '+score,360,200);}});
stars.forEach((s,i)=>{if(s.lane===lane&&Math.abs(s.y-py)<70){stars.splice(i,1);score+=Math.floor(10+speed*3);
document.getElementById('srScore').textContent=score;}});
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#1E293B';cx.fillRect(80,0,560,480);
cx.strokeStyle='#475569';cx.setLineDash([26,26]);cx.lineWidth=4;
[270,450].forEach(lx=>{cx.beginPath();cx.moveTo(lx,0);cx.lineTo(lx,480);cx.stroke();});cx.setLineDash([]);
traffic.forEach(t=>{cx.fillStyle='#EF4444';cx.beginPath();cx.roundRect(t.x-CARW/2,t.y,CARW,CARH,12);cx.fill();
cx.fillStyle='#FCA5A5';cx.fillRect(t.x-CARW/2+8,t.y+8,CARW-16,26);});
stars.forEach(s=>{cx.font='30px serif';cx.textAlign='center';cx.fillText('⭐',s.x,s.y);});
cx.fillStyle='#38BDF8';cx.beginPath();cx.roundRect(x-CARW/2,380,CARW,CARH,12);cx.fill();
cx.fillStyle='#0EA5E9';cx.fillRect(x-CARW/2+8,388,CARW-16,26);
cx.fillStyle='#FDE68A';cx.fillRect(x-14,470,28,10);}
document.addEventListener('keydown',e=>{
if(e.code==='ArrowLeft'||e.code==='KeyA')move(-1);
if(e.code==='ArrowRight'||e.code==='KeyD')move(1);});
cv.addEventListener('mousedown',e=>{const r=cv.getBoundingClientRect();
(e.clientX-r.left)<r.width/2?move(-1):move(1);});
cv.addEventListener('touchstart',e=>{e.preventDefault();const r=cv.getBoundingClientRect();
(e.touches[0].clientX-r.left)<r.width/2?move(-1):move(1);},{passive:false});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))

# ---------------------------------------------------------------- Highway Racer
GAMES_A.append(dict(
    file="highway-racer.html", name="Highway Racer", category="racing",
    category_label="Racing", icon="🛣️",
    tagline="Pure highway speed: four lanes, no brakes, one distance record.",
    meta="Play Highway Racer free online. A fast four-lane highway dodging game with rising speed and local high scores - instant browser play.",
    about="""<p>Highway Racer strips racing down to the tension of a single decision: which gap do you take? Four lanes of faster-and-faster traffic scroll beneath you, and the only control is left and right.</p>
<p>What makes it different from lane-dodge games is the near-miss bonus. Slide past a car closely and the game rewards you with extra points and a brief slow-motion pulse - skilled players deliberately thread the needle instead of playing it safe.</p>""",
    howto=["Steer with ← → or A/D; on touch, tap the side you want to move to.",
           "Overtake as many cars as you can - each overtake adds points.",
           "A near miss (passing within a whisker) scores triple.",
           "One collision ends the run. Speed increases every 500 meters."],
    tips=["Commit to a gap before you get there - last-instant swerves rarely fit.",
          "Near misses are worth the risk early; play conservative once past 2,000 m.",
          "The far-left lane has the fastest traffic but the fewest cars - high risk, high pace.",
          "Keep your eyes on the horizon line, not the car beside you."],
    faq=[("How is score calculated?", "Meters traveled plus overtake bonuses; near misses count triple."),
         ("Does the game get harder forever?", "Speed caps at around 240 km/h - after that, only traffic density keeps rising."),
         ("Can two people play?", "The game is single-player; compare high scores on the same device instead.")],
    stats='<span>Meters: <b id="hrDist">0</b></span><span>Score: <b id="hrScore">0</b></span><span>Best: <b id="hrBest">0</b></span>',
    hint="← → / A D to steer - thread near misses for triple points",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const LANES=[120,280,440,600],CARW=58,CARH=96;
let lane=1,x=LANES[1],cars=[],dist=0,score=0,speed=6,alive=true,spawnT=30;
document.getElementById('hrBest').textContent=localStorage.getItem('hrBest')||0;
function reset(){lane=1;x=LANES[1];cars=[];dist=0;score=0;speed=6;alive=true;spawnT=30;
document.getElementById('hrDist').textContent=0;document.getElementById('hrScore').textContent=0;}
function move(d){if(!alive){reset();return;}lane=Math.max(0,Math.min(3,lane+d));}
function step(){if(alive){dist+=speed;speed=Math.min(12,6+dist/2500);
document.getElementById('hrDist').textContent=Math.floor(dist)+'m';
if(--spawnT<=0){const used=new Set();const n=1+Math.floor(Math.random()*2);
for(let i=0;i<n;i++){let l=Math.floor(Math.random()*4);let guard=0;
while(used.has(l)&&guard++<8)l=Math.floor(Math.random()*4);used.add(l);
cars.push({x:LANES[l],y:-CARH,lane:l,counted:false});}
spawnT=Math.max(16,44-Math.floor(speed*2));}
cars.forEach(c=>c.y+=speed*.55);cars=cars.filter(c=>c.y<560);
x+=(LANES[lane]-x)*.2;
cars.forEach(c=>{if(!c.counted&&c.y>380+CARH){c.counted=true;score+=10;}});
cars.forEach(c=>{if(c.lane===lane&&Math.abs(c.y-380)<CARH-12){alive=false;
const best=+localStorage.getItem('hrBest')||0;
if(score>best){localStorage.setItem('hrBest',score);document.getElementById('hrBest').textContent=score;}}});}
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#1E293B';cx.fillRect(40,0,640,480);
cx.strokeStyle='#475569';cx.setLineDash([30,30]);cx.lineWidth=4;
[200,360,520].forEach(lx=>{cx.beginPath();cx.moveTo(lx,0);cx.lineTo(lx,480);cx.stroke();});cx.setLineDash([]);
cars.forEach(c=>{cx.fillStyle='#64748B';cx.beginPath();cx.roundRect(c.x-CARW/2,c.y,CARW,CARH,10);cx.fill();
cx.fillStyle='#94A3B8';cx.fillRect(c.x-CARW/2+7,c.y+8,CARW-14,22);});
cx.fillStyle='#A78BFA';cx.beginPath();cx.roundRect(x-CARW/2,380,CARW,CARH,10);cx.fill();
cx.fillStyle='#C4B5FD';cx.fillRect(x-CARW/2+7,388,CARW-14,22);
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Wrecked at '+Math.floor(dist)+'m',360,200);cx.font='16px Inter';cx.fillStyle='#94A3B8';
cx.fillText('Score '+score+' - press Restart',360,235);}}
document.addEventListener('keydown',e=>{
if(e.code==='ArrowLeft'||e.code==='KeyA')move(-1);
if(e.code==='ArrowRight'||e.code==='KeyD')move(1);});
cv.addEventListener('mousedown',e=>{const r=cv.getBoundingClientRect();
(e.clientX-r.left)<r.width/2?move(-1):move(1);});
cv.addEventListener('touchstart',e=>{e.preventDefault();const r=cv.getBoundingClientRect();
(e.touches[0].clientX-r.left)<r.width/2?move(-1):move(1);},{passive:false});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))

# ---------------------------------------------------------------- Moto Hill Jump
GAMES_A.append(dict(
    file="moto-x3m.html", name="Moto Hill Jump", category="racing",
    category_label="Racing", icon="🏍️",
    tagline="Hold the throttle, hit the ramps, and stick the landing.",
    meta="Play Moto Hill Jump free online. Hold the throttle, launch off hills and stick the landing in this physics bike game - free in your browser.",
    about="""<p>Moto Hill Jump is a side-scrolling physics ride: hold the throttle to build speed over rolling hills, launch off the crests, and tilt your bike in the air so the wheels - not the helmet - land first.</p>
<p>The hills follow a real sine-wave terrain, so every jump is readable: wide valleys make big air, sharp bumps make quick hops. Distance is your score, but only clean landings keep the run alive.</p>""",
    howto=["Hold Space / click / touch to apply throttle.",
           "Release before a crest to avoid launching flat and heavy.",
           "In the air, hold the same button to rotate the bike forward.",
           "Land wheels-first. A flat or nose-first landing ends the run."],
    tips=["Speed is safety: a faster takeoff means a more stable rotation in the air.",
          "Start rotating only after the apex - rotating too early flattens your arc.",
          "Short bumps need almost no rotation; save dramatic flips for the big valley jumps.",
          "If a landing looks bad, release the throttle - cutting speed slightly improves the angle."],
    faq=[("Is the bike physics realistic?", "It is simplified arcade physics - enough to make every jump feel earned, without a learning cliff."),
         ("How far can you get?", "The terrain is endless and slowly steepens; past 1,500 m the valleys get seriously wide."),
         ("Are there checkpoints?", "No - runs are meant to be short and replayable. Your best distance is saved locally.")],
    stats='<span>Distance: <b id="mjDist">0</b></span><span>Best: <b id="mjBest">0</b></span>',
    hint="Hold Space / press to throttle - hold in air to rotate",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const G=0.5;
let px=0,py=0,vx=0,vy=0,rot=0,vrot=0,onGround=false,alive=true,throttle=false,frame=0;
document.getElementById('mjBest').textContent=localStorage.getItem('mjBest')||0;
const terrain=x=>340+90*Math.sin(x/160)+40*Math.sin(x/53);
function reset(){px=0;py=terrain(0)-20;vx=0;vy=0;rot=0;vrot=0;onGround=true;alive=true;}
function down(){if(!alive){reset();return;}throttle=true;}
function up(){throttle=false;}
function step(){frame++;
if(alive){vx=Math.min(11,vx+(throttle?0.14:-0.02));
px+=vx;vy+=G;py+=vy;
const gy=terrain(px)-20;
if(py>=gy){const impact=Math.abs(vy);
const wheelAngle=Math.atan2(terrain(px+30)-terrain(px-30),60);
const bikeTilt=Math.atan2(Math.sin(rot),Math.cos(rot));
if(impact>10||Math.abs(bikeTilt-wheelAngle)>0.9){alive=false;
const best=+localStorage.getItem('mjBest')||0;
if(px>best){localStorage.setItem('mjBest',Math.floor(px));document.getElementById('mjBest').textContent=Math.floor(px);}}
else{py=gy;vy=0;onGround=true;rot=wheelAngle;vrot=0;}
}else onGround=false;
if(!onGround&&throttle)vrot+=0.004;rot+=vrot*(onGround?0:1);
document.getElementById('mjDist').textContent=Math.floor(px);}}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#0EA5E9';cx.globalAlpha=.15;
for(let i=0;i<3;i++)cx.fillRect(0,60+i*40,720,20);cx.globalAlpha=1;
cx.fillStyle='#052E16';cx.beginPath();cx.moveTo(0,480);
for(let x=0;x<=720;x+=8)cx.lineTo(x,terrain(px+x-200)+200-200);
for(let x=720;x>=0;x-=8)cx.lineTo(x,terrain(px+x-200));
cx.closePath();cx.fill();
cx.strokeStyle='#16A34A';cx.lineWidth=3;cx.beginPath();
for(let x=0;x<=720;x+=8){const y=terrain(px+x-200);x===0?cx.moveTo(x,y):cx.lineTo(x,y);}cx.stroke();
const bx=200,by=terrain(px)-20;
cx.save();cx.translate(bx,by-14);cx.rotate(rot-(Math.atan2(Math.sin(rot),Math.cos(rot))-rot));
cx.fillStyle='#F59E0B';cx.beginPath();cx.roundRect(-30,-12,60,18,8);cx.fill();
cx.fillStyle='#111C33';cx.fillRect(-8,-26,20,12);
cx.restore();
cx.fillStyle='#E2E8F0';cx.beginPath();cx.arc(bx-20,by,11,0,7);cx.fill();
cx.beginPath();cx.arc(bx+20,by,11,0,7);cx.fill();
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 30px Inter';cx.textAlign='center';
cx.fillText('Crashed at '+Math.floor(px)+'m',360,200);
cx.font='16px Inter';cx.fillStyle='#94A3B8';cx.fillText('Press Restart or tap to ride again',360,235);}}
setInterval(()=>{step();draw();},1000/60);
cv.addEventListener('mousedown',down);cv.addEventListener('mouseup',up);
cv.addEventListener('touchstart',e=>{e.preventDefault();down();},{passive:false});
cv.addEventListener('touchend',up);
document.addEventListener('keydown',e=>{if(e.code==='Space'){e.preventDefault();down();}});
document.addEventListener('keyup',e=>{if(e.code==='Space')up();});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();""",
))

# ---------------------------------------------------------------- Drift Master
GAMES_A.append(dict(
    file="drift-hunters.html", name="Drift Master", category="racing",
    category_label="Racing", icon="🏁",
    tagline="Slide through checkpoints on a midnight circuit - style earns points.",
    meta="Play Drift Master free online. Slide your car around a midnight circuit, chain drifts and beat your best lap in this arcade browser game.",
    about="""<p>Drift Master is an arcade top-down circuit where the brake pedal matters as much as the gas. Your car carries momentum through corners; enter a turn too hot and you slide - which is exactly the point, because drifting through checkpoints is how you score.</p>
<p>Each lap passes four gates. Cross them cleanly and the timer extends; drift while doing it and style points stack up. The steering is deliberately loose, so after two or three laps you stop fighting the slide and start steering with it.</p>""",
    howto=["Steer with ← → (or A/D); hold ↑ for throttle.",
           "Tap ↓ (or S) into a corner to break traction and drift.",
           "Pass all four gates to complete a lap - the timer resets each lap.",
           "Drifting through a gate multiplies its points; runs last 90 seconds."],
    tips=["Brake before the corner, throttle through it - braking mid-corner kills your drift angle.",
          "Wider entry, tighter exit: start drifts from the outside of a bend.",
          "Gates give a position hint arrow - plan the next gate while drifting the current one.",
          "Small steering corrections beat big swings once the car is sideways."],
    faq=[("Is there automatic transmission?", "Yes - throttle and brake are all you manage; gears are abstracted away."),
         ("Can I use a gamepad?", "Keyboard and touch are supported; gamepad support is on the roadmap."),
         ("Why did my drift end early?", "Drift score needs sustained sliding - tapping the brake repeatedly resets the chain.")],
    stats='<span>Score: <b id="dmScore">0</b></span><span>Laps: <b id="dmLaps">0</b></span><span>Time: <b id="dmTime">90</b>s</span>',
    hint="↑ throttle - ↓ brake/drift - ← → steer",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const C={x:360,y:240,r1:150,r2:95};
let car={x:C.x,y:C.y-C.r1-30,a:0,v:0,dir:0},score=0,laps=0,t=90,alive=true,gate=0,timer=null;
const GATES=[0,Math.PI/2,Math.PI,Math.PI*1.5];
function gatePos(i){const a=GATES[i];return[C.x+Math.cos(a)*(C.r1+34),C.y+Math.sin(a)*(C.r1+34)];}
function reset(){car={x:C.x,y:C.y-C.r1-30,a:0,v:0,dir:0};score=0;laps=0;t=90;alive=true;gate=0;
document.getElementById('dmScore').textContent=0;document.getElementById('dmLaps').textContent=0;
clearInterval(timer);timer=setInterval(()=>{t--;document.getElementById('dmTime').textContent=t;if(t<=0)alive=false;},1000);}
const keys={};
document.addEventListener('keydown',e=>keys[e.code]=true);
document.addEventListener('keyup',e=>keys[e.code]=false);
function step(){if(alive){
if(keys.ArrowUp||keys.KeyW)car.v=Math.min(5.2,car.v+.12);
else if(keys.ArrowDown||keys.KeyS)car.v=Math.max(-2,car.v-.18);
else car.v*=.985;
const steer=((keys.ArrowLeft||keys.KeyA)?-1:0)+((keys.ArrowRight||keys.KeyD)?1:0);
car.dir+=steer*(.032+Math.abs(car.v)*.006)*(car.v<0?-1:1);
car.a+=car.dir*Math.min(1,Math.abs(car.v)/3)*.16;
const drift=steer!==0&&Math.abs(car.v)>2.4;
car.x+=Math.sin(car.a)*car.v*(drift?1.12:1);
car.y-=Math.cos(car.a)*car.v*(drift?1.12:1);
const dx=car.x-C.x,dy=car.y-C.y,d=Math.hypot(dx,dy);
if(d>C.r1+48||d<C.r2-46){car.x=C.x+dx/d*(C.r1+46);car.y=C.y+dy/d*(C.r1+46);car.v*=.6;}
const[gcx,gcy]=gatePos(gate);
if(Math.hypot(car.x-gcx,car.y-gcy)<38){score+=drift?50:20;
if(drift)car.v=Math.min(5.5,car.v+.4);
gate++;if(gate>3){gate=0;laps++;document.getElementById('dmLaps').textContent=laps;}
document.getElementById('dmScore').textContent=score;}}
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.strokeStyle='#334155';cx.lineWidth=C.r1-C.r2;
cx.beginPath();cx.ellipse(C.x,C.y,C.r1,C.r1,0,0,7);cx.stroke();
cx.strokeStyle='#475569';cx.lineWidth=2;cx.setLineDash([14,18]);
cx.beginPath();cx.ellipse(C.x,C.y,(C.r1+C.r2)/2,(C.r1+C.r2)/2,0,0,7);cx.stroke();cx.setLineDash([]);
for(let i=0;i<4;i++){const[gx,gy]=gatePos(i);cx.fillStyle=i===gate?'#FBBF24':'#1E3A8A';
cx.beginPath();cx.arc(gx,gy,i===gate?16:10,0,7);cx.fill();}
cx.save();cx.translate(car.x,car.y);cx.rotate(car.a+Math.PI/2);
cx.fillStyle='#F472B6';cx.beginPath();cx.roundRect(-11,-20,22,40,7);cx.fill();
cx.fillStyle='#111C33';cx.fillRect(-7,-14,14,10);
cx.restore();
const[gcx,gcy]=gatePos(gate);
cx.strokeStyle='#FBBF24';cx.lineWidth=2;cx.beginPath();
cx.moveTo(car.x,car.y);cx.lineTo(gcx,gcy);cx.globalAlpha=.25;cx.stroke();cx.globalAlpha=1;
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText("Time! Score: "+score,360,220);cx.font='16px Inter';cx.fillStyle='#94A3B8';
cx.fillText('Press Restart for a new session',360,255);}}
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))

# ---------------------------------------------------------------- Mini Hoops
GAMES_A.append(dict(
    file="basketball.html", name="Mini Hoops Basketball", category="sports",
    category_label="Sports", icon="🏀",
    tagline="Drag, release, swish - a pocket arcade of pure shooting touch.",
    meta="Play Mini Hoops Basketball free online. Drag and flick to sink baskets against the clock in this satisfying arcade shooting game.",
    about="""<p>Mini Hoops distills basketball into its most addictive moment: the shot. Drag back on the ball, watch the dotted arc preview bend as you pull further, and release. The ball flies with real parabolic physics - power and angle both matter, and the rim is unforgiving.</p>
<p>Sixty seconds on the clock, unlimited balls, one hoop that drifts to new positions after every make. Swishes (clean shots that never touch the rim) score three; rattled-in shots score two.</p>""",
    howto=["Press and hold the ball, then drag down and back to set power and angle.",
           "A dotted preview arc shows your trajectory while dragging.",
           "Release to shoot - the ball flies with real arc physics.",
           "Score as many baskets as you can in 60 seconds; the hoop moves after each make."],
    tips=["Aim for just above the rim's center - high arcs drop in far more reliably than flat ones.",
          "Use the full drag length: most misses come from under-powered shots.",
          "The hoop moves after every make - glance at its new spot before reseting your aim.",
          "Consistency beats speed: a repeatable shot motion scores more than rushed heaves."],
    faq=[("Does the ball obey real physics?", "Yes - gravity, release angle and velocity all behave the way a real arc would."),
         ("Why does the hoop move?", "Moving targets keep the 60-second run varied; the hoop repositions only after a made basket."),
         ("Can I play with one hand on mobile?", "Yes - hold and drag with your thumb, release to shoot.")],
    stats='<span>Score: <b id="mhScore">0</b></span><span>Time: <b id="mhTime">60</b>s</span><span>Best: <b id="mhBest">0</b></span>',
    hint="Drag from the ball to aim - release to shoot",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const G=0.34,FLOOR=452;
let ball={x:140,y:FLOOR-14,vx:0,vy:0,live:false},drag=null,hoop={x:560,y:170},score=0,t=60,alive=true,timer=null;
document.getElementById('mhBest').textContent=localStorage.getItem('mhBest')||0;
function reset(){score=0;t=60;alive=true;ball={x:140,y:FLOOR-14,vx:0,vy:0,live:false};hoop={x:560,y:170};
document.getElementById('mhScore').textContent=0;
clearInterval(timer);timer=setInterval(()=>{t--;document.getElementById('mhTime').textContent=t;if(t<=0)end();},1000);}
function end(){alive=false;clearInterval(timer);
const best=+localStorage.getItem('mhBest')||0;
if(score>best){localStorage.setItem('mhBest',score);document.getElementById('mhBest').textContent=score;}}
function pos(e){const r=cv.getBoundingClientRect();const p=e.touches?e.touches[0]:e;
return[(p.clientX-r.left)*(720/r.width),(p.clientY-r.top)*(480/r.height)];}
function down(e){if(!alive)return;const[mx,my]=pos(e);
if(!ball.live&&Math.hypot(mx-ball.x,my-ball.y)<48)drag=[mx,my];}
function move(e){if(!drag)return;[drag[2],drag[3]]=pos(e);}
function up(e){if(!drag||drag.length<4){drag=null;return;}
const dx=ball.x-drag[2],dy=ball.y-drag[3];
const pow=Math.min(19,Math.hypot(dx,dy)*.22);
ball.vx=dx/Math.hypot(dx,dy)*pow;ball.vy=dy/Math.hypot(dx,dy)*pow;
ball.live=true;drag=null;}
function step(){if(ball.live){ball.vy+=G;ball.x+=ball.vx;ball.y+=ball.vy;
const rimY=hoop.y,rimL=hoop.x-34,rimR=hoop.x+34;
if(ball.y>rimY-6&&ball.y<rimY+14){
if(ball.x>rimL+6&&ball.x<rimR-6&&ball.vy>0){
const swish=!ball.touched;score+=swish?3:2;
document.getElementById('mhScore').textContent=score;
ball.live=false;ball={x:140+Math.random()*80,y:FLOOR-14,vx:0,vy:0,live:false};
hoop.x=200+Math.random()*420;hoop.y=140+Math.random()*110;}
else if(Math.abs(ball.x-rimL)<8||Math.abs(ball.x-rimR)<8){ball.vx*=-.4;ball.vy*=.6;ball.touched=true;}}
if(ball.x<12||ball.x>708){ball.vx*=-.7;ball.x=Math.max(12,Math.min(708,ball.x));}
if(ball.y>FLOOR){ball.live=false;ball={x:140+Math.random()*80,y:FLOOR-14,vx:0,vy:0,live:false};}}
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#1E293B';cx.fillRect(0,FLOOR,720,28);
cx.strokeStyle='#334155';cx.lineWidth=8;cx.beginPath();cx.moveTo(hoop.x,hoop.y-120);cx.lineTo(hoop.x,hoop.y);cx.stroke();
cx.strokeStyle='#F97316';cx.lineWidth=6;cx.beginPath();cx.moveTo(hoop.x-34,hoop.y);cx.lineTo(hoop.x+34,hoop.y);cx.stroke();
cx.strokeStyle='rgba(249,115,22,.5)';cx.lineWidth=2;
for(let i=1;i<4;i++){cx.beginPath();cx.moveTo(hoop.x-34+i*17,hoop.y);cx.lineTo(hoop.x-34+i*17,hoop.y+22);cx.stroke();}
cx.beginPath();cx.moveTo(hoop.x-34,hoop.y);cx.lineTo(hoop.x-30,hoop.y+22);
cx.moveTo(hoop.x+34,hoop.y);cx.lineTo(hoop.x+30,hoop.y+22);cx.stroke();
if(drag&&drag.length>=4){cx.setLineDash([5,7]);cx.strokeStyle='rgba(251,191,36,.8)';cx.lineWidth=2;
let sx=ball.x,sy=ball.y,vx=(ball.x-drag[2])/Math.hypot(ball.x-drag[2],ball.y-drag[3])*Math.min(19,Math.hypot(ball.x-drag[2],ball.y-drag[3])*.22);
let vy=(ball.y-drag[3])/Math.hypot(ball.x-drag[2],ball.y-drag[3])*Math.min(19,Math.hypot(ball.x-drag[2],ball.y-drag[3])*.22);
for(let i=0;i<26;i++){vy+=G;sx+=vx;sy+=vy;
i%3===0?cx.fillRect(sx,sy,3,3):0;}
cx.setLineDash([]);}
cx.fillStyle='#F59E0B';cx.beginPath();cx.arc(ball.x,ball.y,14,0,7);cx.fill();
cx.strokeStyle='#B45309';cx.lineWidth=2;cx.beginPath();cx.arc(ball.x,ball.y,14,0,7);cx.stroke();
cx.beginPath();cx.moveTo(ball.x-14,ball.y);cx.lineTo(ball.x+14,ball.y);cx.stroke();
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Time! Final score: '+score,360,220);cx.font='16px Inter';cx.fillStyle='#94A3B8';
cx.fillText('Press Restart for a new run',360,255);}}
cv.addEventListener('mousedown',down);cv.addEventListener('mousemove',move);cv.addEventListener('mouseup',up);
cv.addEventListener('touchstart',e=>{e.preventDefault();down(e);},{passive:false});
cv.addEventListener('touchmove',e=>{e.preventDefault();move(e);},{passive:false});
cv.addEventListener('touchend',up);
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))
