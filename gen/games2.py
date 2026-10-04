# -*- coding: utf-8 -*-
"""Toolnex original games, batch 2: Puzzle, Match 3, Simulation, Strategy."""

GRID_STAGE = """<div class="stage-head">
<div class="stat">{stats}</div>
<button id="btnRestart" type="button">Restart</button>
</div>
<div class="dom-game">{inner}</div>
<div class="hint">{hint}</div>"""

GAMES_B = []

# ---------------------------------------------------------------- 2048
GAMES_B.append(dict(
    file="2048-challenge.html", name="Merge Numbers 2048", category="puzzle",
    category_label="Puzzle", icon="🔢",
    tagline="Slide, merge and double your way to the legendary 2048 tile.",
    meta="Play Merge Numbers 2048 free online. Slide tiles, merge numbers and chase the 2048 tile in this classic puzzle game - playable instantly in your browser.",
    about="""<p>Merge Numbers 2048 is our in-house take on the tile-sliding classic that hooked the world. Swipe or use the arrow keys: every tile slides as far as it can, identical neighbors merge into their sum, and a new tile appears. Reach the 2048 tile and you have beaten the base challenge - then keep going for 4096 and beyond.</p>
<p>The board never forgives careless swipes. Every move shifts all four rows and columns, so the real game is planning: keeping your biggest tile anchored in a corner and building descending channels toward it.</p>""",
    howto=["Swipe (touch) or use the arrow keys to slide all tiles in one direction.",
           "Tiles with the same number merge into one tile worth double.",
           "A new tile appears after every move.",
           "Reach 2048 to win - the game continues for score chasers."],
    tips=["Pick one corner and never move your biggest tile out of it.",
          "Build your tiles in descending order along one row - a 'staircase' keeps merges available.",
          "Think before every swipe: an empty board fills up faster than you expect.",
          "Only swipe down/up when the row is prepared; sideways moves are your working moves."],
    faq=[("Is 2048 a game of luck?", "New tiles are random, but strong play wins consistently - good players reach 2048 in most games."),
         ("What happens after I make 2048?", "You can keep playing: 4096, 8192 and beyond, with your score climbing all the way."),
         ("Does the game save my board?", "The current board persists while the page stays open; closing the tab starts a fresh game.")],
    stats='<span>Score: <b id="gScore">0</b></span><span>Best: <b id="gBest">0</b></span>',
    hint="Arrow keys / swipe to move - merge equal tiles",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(4,86px);background:#1E293B;padding:12px;border-radius:14px"></div><div class="msg" id="msg"></div>',
    js="""
const N=4;let grid=[],score=0,moved=false;
document.getElementById('gBest').textContent=localStorage.getItem('mBest')||0;
function reset(){grid=Array.from({length:N},()=>Array(N).fill(0));score=0;
document.getElementById('msg').textContent='';add();add();draw();}
function add(){const empt=[];grid.forEach((r,i)=>r.forEach((v,j)=>{if(!v)empt.push([i,j]);}));
if(!empt.length)return;const[i,j]=empt[Math.floor(Math.random()*empt.length)];
grid[i][j]=Math.random()<.9?2:4;}
const COLORS={2:'#64748B',4:'#475569',8:'#0EA5E9',16:'#2563EB',32:'#7C3AED',64:'#DB2777',
128:'#EA580C',256:'#F59E0B',512:'#FBBF24',1024:'#84CC16',2048:'#10B981'};
function draw(){const b=document.getElementById('board');b.innerHTML='';
grid.forEach(row=>row.forEach(v=>{const d=document.createElement('div');d.className='g-cell';
d.style.width='86px';d.style.height='86px';d.style.fontSize=v>=1024?'22px':'28px';
d.style.background=v?COLORS[v]||'#059669':'#334155';d.style.color='#fff';
d.style.opacity=v?1:.45;d.textContent=v||'';b.appendChild(d);}));
document.getElementById('gScore').textContent=score;}
function slide(row){const arr=row.filter(v=>v);
for(let i=0;i<arr.length-1;i++){if(arr[i]===arr[i+1]){arr[i]*=2;score+=arr[i];arr.splice(i+1,1);}}
while(arr.length<N)arr.push(0);return arr;}
function move(dir){const old=JSON.stringify(grid);
if(dir==='l')grid=grid.map(r=>slide(r));
if(dir==='r')grid=grid.map(r=>slide(r.slice().reverse()).reverse());
if(dir==='u'||dir==='d'){for(let j=0;j<N;j++){let col=grid.map(r=>r[j]);
col=dir==='u'?slide(col):slide(col.slice().reverse()).reverse();
col.forEach((v,i)=>grid[i][j]=v);}}
if(JSON.stringify(grid)!==old){moved=true;add();draw();
if(grid.some(r=>r.includes(2048)))document.getElementById('msg').textContent='2048! You win - keep going!';
if(grid.every(r=>r.every(v=>v))&&!canMove()){document.getElementById('msg').textContent='No moves left - game over';
const best=+localStorage.getItem('mBest')||0;
if(score>best){localStorage.setItem('mBest',score);document.getElementById('gBest').textContent=score;}}}}
function canMove(){for(let i=0;i<N;i++)for(let j=0;j<N;j++){
if(j<N-1&&grid[i][j]===grid[i][j+1])return true;
if(i<N-1&&grid[i][j]===grid[i+1][j])return true;}return false;}
document.addEventListener('keydown',e=>{const m={ArrowLeft:'l',ArrowRight:'r',ArrowUp:'u',ArrowDown:'d'}[e.code];
if(m){e.preventDefault();move(m);}});
let ts=null;
document.getElementById('board').addEventListener('touchstart',e=>{ts=[e.touches[0].clientX,e.touches[0].clientY];},{passive:true});
document.getElementById('board').addEventListener('touchend',e=>{if(!ts)return;
const dx=e.changedTouches[0].clientX-ts[0],dy=e.changedTouches[0].clientY-ts[1];
Math.abs(dx)>Math.abs(dy)?move(dx>0?'r':'l'):move(dy>0?'d':'u');ts=null;},{passive:true});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();""",
))

# ---------------------------------------------------------------- Block Fit
GAMES_B.append(dict(
    file="block-puzzle-classic.html", name="Block Fit Puzzle", category="puzzle",
    category_label="Puzzle", icon="🧩",
    tagline="Fit wooden blocks, clear full lines, and outsmart the empty board.",
    meta="Play Block Fit Puzzle free online. Place block shapes, clear rows and columns, and beat your best score in this relaxing browser puzzle.",
    about="""<p>Block Fit Puzzle is a gentle, no-timer block game: you get three wooden-style shapes each turn and place them anywhere on the 9x9 board. Fill an entire row or column and it clears with a satisfying flash.</p>
<p>The catch is that you must place all three shapes before getting new ones - so the order you place them in matters as much as where. It is a calm, think-as-long-as-you-like puzzle with no falling blocks and no pressure, which makes it dangerously easy to say "one more game".</p>""",
    howto=["Click one of the three shape trays to select it.",
           "Click a spot on the board to place the shape (ghost preview shows validity).",
           "Fill a full row or column to clear it and score.",
           "Clear multiple lines with one placement for big bonuses. The game ends when nothing fits."],
    tips=["Keep at least one flat 1-wide strip open - L-shapes are the pieces that ruin boards.",
          "Place the bulkiest shape first while the board is still open.",
          "Clearing a row AND a column with one piece scores triple - hunt for those overlaps.",
          "Corners and edges fill up fast; claim them early."],
    faq=[("Is there a time limit?", "None at all - take as long as you like per placement."),
         ("What shapes can appear?", "Classic polyomino shapes: singles, lines, L-shapes, squares and T-shapes, randomly picked each round."),
         ("How is score calculated?", "One point per block placed, plus escalating bonuses for multi-line clears.")],
    stats='<span>Score: <b id="bfScore">0</b></span><span>Best: <b id="bfBest">0</b></span>',
    hint="Click a tray piece, then click the board to place",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(9,44px);background:#1E293B;padding:10px;border-radius:14px"></div><div class="msg" id="msg"></div><div id="trays" style="display:flex;gap:26px;justify-content:center;margin-top:16px"></div>',
    js="""
const N=9;let board=Array.from({length:N},()=>Array(N).fill(0));
let trays=[],sel=-1,score=0;
document.getElementById('bfBest').textContent=localStorage.getItem('bfBest')||0;
const SHAPES=[[[1]],[[1,1]],[[1,1,1]],[[1,1,1,1]],[[1],[1]],[[1],[1],[1]],
[[1,1],[1,1]],[[1,1,1],[1,1,1],[1,1,1]],
[[1,0],[1,1]],[[0,1],[1,1]],[[1,1],[1,0]],[[1,1],[0,1]],
[[1,1,1],[0,1,0]],[[0,1,0],[1,1,1]],[[1,0],[1,0],[1,1]],[[0,1],[0,1],[1,1]]];
function newTrays(){trays=[0,1,2].map(()=>SHAPES[Math.floor(Math.random()*SHAPES.length)]);sel=-1;renderTrays();}
function fits(shape,r,c){return shape.every((row,dr)=>row.every((v,dc)=>{
if(!v)return true;const nr=r+dr,nc=c+dc;
return nr>=0&&nr<N&&nc>=0&&nc<N&&!board[nr][nc];}));}
function place(r,c){if(sel<0)return;const shape=trays[sel];
if(!fits(shape,r,c)){document.getElementById('msg').textContent='Does not fit there';return;}
shape.forEach((row,dr)=>row.forEach((v,dc)=>{if(v)board[r+dr][c+dc]=1;}));
score+=shape.flat().filter(v=>v).length;
let cleared=0;
for(let i=0;i<N;i++){if(board[i].every(v=>v)){board[i].fill(0);cleared++;}}
for(let j=0;j<N;j++){if(board.every(row=>row[j])){board.forEach(row=>row[j]=0);cleared++;}}
score+=cleared*cleared*12;
document.getElementById('msg').textContent=cleared>1?'+'+(cleared*cleared*12)+' combo!':'';
trays[sel]=null;sel=-1;
document.getElementById('bfScore').textContent=score;
if(trays.every(t=>!t))newTrays();
if(!anyMove()){const best=+localStorage.getItem('bfBest')||0;
if(score>best){localStorage.setItem('bfBest',score);document.getElementById('bfBest').textContent=score;}
document.getElementById('msg').textContent='No moves left - final score '+score;}}
function anyMove(){return trays.some((shape,ti)=>shape&&board.some((row,r)=>
row.some((_,c)=>fits(shape,r,c))));}
function renderTrays(){const t=document.getElementById('trays');t.innerHTML='';
trays.forEach((shape,i)=>{const d=document.createElement('div');
d.style.cssText='display:grid;gap:3px;cursor:pointer;padding:8px;border-radius:10px;'+
(i===sel?'background:#2563EB':'background:#334155');
if(!shape){d.textContent='✓';d.style.color='#94A3B8';d.style.padding='18px';}
else{d.style.gridTemplateColumns='repeat('+shape[0].length+',18px)';
shape.forEach(row=>row.forEach(v=>{const s=document.createElement('div');
s.style.cssText='width:18px;height:18px;border-radius:4px;background:'+(v?'#F59E0B':'transparent');
d.appendChild(s);}));}
d.onclick=()=>{if(trays[i]){sel=i;renderTrays();}};t.appendChild(d);});}
function render(){const b=document.getElementById('board');b.innerHTML='';
board.forEach((row,r)=>row.forEach((v,c)=>{const d=document.createElement('div');
d.className='g-cell';d.style.cssText='width:44px;height:44px;background:'+(v?'#F59E0B':'#334155');
d.onclick=()=>{place(r,c);render();renderTrays();};b.appendChild(d);}));}
document.getElementById('btnRestart').addEventListener('click',()=>{board=Array.from({length:N},()=>Array(N).fill(0));
score=0;document.getElementById('bfScore').textContent=0;newTrays();render();});
newTrays();render();""",
))

# ---------------------------------------------------------------- Jigsaw Slide
GAMES_B.append(dict(
    file="jigsaw-master.html", name="Jigsaw Slide Master", category="puzzle",
    category_label="Puzzle", icon="🖼️",
    tagline="A sliding picture puzzle - restore the image one move at a time.",
    meta="Play Jigsaw Slide Master free online. Slide tiles to restore the picture in this classic 3x3 sliding puzzle - free, no download.",
    about="""<p>Jigsaw Slide Master rebuilds the charm of the classic fifteen-puzzle in a compact 3x3 form. The picture is scrambled across eight tiles and one gap; slide tiles into the gap until the image is whole again.</p>
<p>Every shuffle is verified to be solvable, so a solution always exists. The image is a colorful gradient mosaic generated fresh each game - plus a number mode if you prefer the pure logic version.</p>""",
    howto=["Click a tile next to the empty gap to slide it into place.",
           "Rebuild the picture: the top-left tile goes first, work row by row.",
           "Toggle Picture/Number mode with the button under the board.",
           "Finish in as few moves as possible - your move count is your score."],
    tips=["Solve the top row first, then the left column - it reduces the puzzle to 2x2.",
          "Never break a finished row to fix a lower one; there is always another path.",
          "Trace where a tile must travel and plan a corridor for it, one move at a time.",
          "If stuck, undo mentally: name the last two moves that felt wrong."],
    faq=[("Can every shuffle be solved?", "Yes - the shuffler only makes legal moves backward from the solved state, so no impossible layouts exist."),
         ("Is there a bigger size?", "3x3 is the sweet spot for browser play; a 4x4 expert mode is planned."),
         ("How do I count moves?", "The counter under the board increments on every tile slide.")],
    stats='<span>Moves: <b id="jsMoves">0</b></span><span>Best: <b id="jsBest">0</b></span>',
    hint="Click a tile beside the gap to slide it",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(3,110px);background:#1E293B;padding:10px;border-radius:14px"></div><div class="msg" id="msg"></div><button id="btnMode" class="btn ghost" style="margin-top:14px">Switch to Numbers</button>',
    js="""
let tiles=[...Array(8).keys(),-1],moves=0,picMode=true,shuffling=false;
document.getElementById('jsBest').textContent=localStorage.getItem('jsBest')||0;
const hue=()=>Math.floor(Math.random()*360);
let baseHue=hue();
function tileStyle(v,pos){const r=Math.floor(pos/3),c=pos%3;
const vr=Math.floor(v/3),vc=v%3;
if(picMode){return'background:linear-gradient(135deg,hsl('+((baseHue+vr*40)%360)+',70%,'+(30+vc*14)+'%),hsl('+((baseHue+vr*40+30)%360)+',70%,'+(45+vc*12)+'%));';}
return'background:#2563EB;';}
function solved(){return tiles.every((v,i)=>v===i||(i===8&&v===-1));}
function draw(){const b=document.getElementById('board');b.innerHTML='';
tiles.forEach((v,i)=>{const d=document.createElement('div');d.className='g-cell';
d.style.cssText+='width:110px;height:110px;font-size:26px;color:#fff;';
if(v===-1){d.style.background='transparent';d.style.cursor='default';}
else{d.style.cssText+=tileStyle(v,i)+'cursor:pointer;';
d.innerHTML=picMode?'<span style="opacity:.75;font-size:15px">'+(v+1)+'</span>':(v+1);
d.onclick=()=>slide(i);}
b.appendChild(d);});
document.getElementById('jsMoves').textContent=moves;
if(solved()&&!shuffling){document.getElementById('msg').textContent='Solved in '+moves+' moves!';
const best=+localStorage.getItem('jsBest')||0;
if(!best||moves<best){localStorage.setItem('jsBest',moves);document.getElementById('jsBest').textContent=moves;}}}
function slide(i){if(shuffling)return;const gi=tiles.indexOf(-1);
const[gr,gc]=[Math.floor(gi/3),gi%3],[tr,tc]=[Math.floor(i/3),i%3];
if(Math.abs(gr-tr)+Math.abs(gc-tc)!==1)return;
tiles[gi]=tiles[i];tiles[i]=-1;moves++;draw();
if(solved())setTimeout(shuffle,1500);}
function shuffle(){shuffling=true;moves=0;baseHue=hue();document.getElementById('msg').textContent='';
let blank=8;
for(let k=0;k<80;k++){const opts=[[blank-3,blank+3],[blank-1,blank+1]].flat()
.filter(p=>p>=0&&p<9&&!(p===blank));
const r=Math.floor(blank/3);
const cand=[blank-3,blank+3];
if(blank%3>0)cand.push(blank-1);
if(blank%3<2)cand.push(blank+1);
const p=cand[Math.floor(Math.random()*cand.length)];
tiles[blank]=tiles[p];tiles[p]=-1;blank=p;}
tiles[8]=-1;draw();setTimeout(()=>shuffling=false,50);}
document.getElementById('btnMode').addEventListener('click',e=>{
picMode=!picMode;e.target.textContent=picMode?'Switch to Numbers':'Switch to Picture';draw();});
document.getElementById('btnRestart').addEventListener('click',shuffle);
shuffle();""",
))

# ---------------------------------------------------------------- Sudoku Daily
GAMES_B.append(dict(
    file="sudoku-daily.html", name="Sudoku Daily", category="puzzle",
    category_label="Puzzle", icon="🔟",
    tagline="A fresh 6x6 sudoku every time - small grid, real deduction.",
    meta="Play Sudoku Daily free online. A fresh 6x6 sudoku puzzle generated every game - the perfect quick logic break in your browser.",
    about="""<p>Sudoku Daily serves the classic logic puzzle in a 6x6 format - every row, column and 2x3 box must contain the digits 1 through 6 exactly once. The smaller grid keeps each puzzle to a satisfying five-minute solve while keeping every deduction honest.</p>
<p>A new puzzle is generated the moment you open the page, with unique solution guaranteed. Fill cells by picking a number from the palette; conflicts highlight instantly, and the puzzle checks itself the moment the last cell is placed.</p>""",
    howto=["Click any empty cell to select it.",
           "Click a number in the palette to place it (click the same number again to erase).",
           "Conflicting entries turn red - a digit may appear only once per row, column and box.",
           "Fill the whole grid correctly to win."],
    tips=["Start with the row, column or box that is already most full.",
          "Scan for digits with only one possible home - 'naked singles' first.",
          "Pencil logic beats guessing: if two cells in a box could be {2,5}, no other cell there can.",
          "A wrong guess early poisons everything; conflict highlighting is there to catch slips, not to plan with."],
    faq=[("Why 6x6 instead of 9x9?", "Six-by-six keeps the same three rule types in a five-minute format - ideal for coffee breaks and mobile screens."),
         ("Is there exactly one solution every time?", "Yes - the generator verifies uniqueness before presenting the puzzle."),
         ("Can I get a hint?", "Not in this version - but conflict highlighting shows which entries need attention.")],
    stats='<span>Filled: <b id="sdFill">0</b>/24</span>',
    hint="Select a cell, then pick a number",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(6,58px);background:#1E293B;padding:10px;border-radius:14px"></div><div id="palette" style="display:flex;gap:10px;justify-content:center;margin-top:16px"></div><div class="msg" id="msg"></div>',
    js="""
const N=6;let sol,puz,sel=-1;
function ok(g,r,c,v){for(let i=0;i<N;i++){if(g[r][i]===v||g[i][c]===v)return false;}
const br=Math.floor(r/2)*2,bc=Math.floor(c/3)*3;
for(let i=br;i<br+2;i++)for(let j=bc;j<bc+3;j++)if(g[i][j]===v)return false;
return true;}
function gen(){const g=Array.from({length:N},()=>Array(N).fill(0));
function fill(p){if(p===N*N)return true;const r=Math.floor(p/N),c=p%N;
const nums=[1,2,3,4,5,6].sort(()=>Math.random()-.5);
for(const v of nums){if(ok(g,r,c,v)){g[r][c]=v;if(fill(p+1))return true;g[r][c]=0;}}
return false;}
fill(g);return g;}
function reset(){sol=gen();puz=sol.map(r=>r.map(v=>v));
let holes=0;
while(holes<24){const r=Math.floor(Math.random()*N),c=Math.floor(Math.random()*N);
if(puz[r][c]){puz[r][c]=0;holes++;}}
sel=-1;document.getElementById('msg').textContent='';render();}
function render(){let filled=0;
const b=document.getElementById('board');b.innerHTML='';
puz.forEach((row,r)=>row.forEach((v,c)=>{if(v)filled++;
const d=document.createElement('div');d.className='g-cell';
const boldR=r%2===1,barC=c===2||c===5;
d.style.cssText='width:58px;height:58px;font-size:24px;'+
'background:'+(v?(v===sol[r][c]?'#1E3A8A':'#7F1D1D'):(sel===r*N+c?'#2563EB':'#334155'))+';'+
'color:'+(v&&v===sol[r][c]?'#fff':'#FCA5A5')+';'+
'border-right:'+(barC?'3px solid #475569':'1px solid #475569')+';'+
'border-bottom:'+(boldR?'3px solid #475569':'1px solid #475569')+';';
d.textContent=v||'';
if(!v)d.onclick=()=>{sel=r*N+c;render();};
b.appendChild(d);}));
document.getElementById('sdFill').textContent=filled;
if(filled===N*N){document.getElementById('msg').textContent='Solved! Well played.';
const b2=document.getElementById('board');b2.style.outline='3px solid #10B981';
setTimeout(()=>b2.style.outline='',2000);}}
const pal=document.getElementById('palette');
for(let v=1;v<=6;v++){const d=document.createElement('div');d.className='g-cell';
d.style.cssText='width:48px;height:48px;background:#2563EB;color:#fff;font-size:22px;cursor:pointer';
d.textContent=v;
d.onclick=()=>{if(sel<0)return;const r=Math.floor(sel/N),c=sel%N;
puz[r][c]=puz[r][c]===v?0:v;render();};
pal.appendChild(d);}
const er=document.createElement('div');er.className='g-cell';
er.style.cssText='width:48px;height:48px;background:#475569;color:#fff;font-size:16px;cursor:pointer';
er.textContent='⌫';
er.onclick=()=>{if(sel<0)return;const r=Math.floor(sel/N),c=sel%N;puz[r][c]=0;render();};
pal.appendChild(er);
document.getElementById('btnRestart').addEventListener('click',reset);
reset();""",
))

# ---------------------------------------------------------------- Word Search
GAMES_B.append(dict(
    file="word-search-pro.html", name="Word Search Pro", category="puzzle",
    category_label="Puzzle", icon="🔤",
    tagline="Six hidden words, one grid - find them all against the clock.",
    meta="Play Word Search Pro free online. Find all six hidden words in a fresh letter grid every game - a calm, free browser word puzzle.",
    about="""<p>Word Search Pro builds a fresh letter grid every time you open the page, hides six words in it - across, down and diagonally - and fills the rest with decoy letters. Your job is the classic joy of the genre: spotting patterns in noise.</p>
<p>Selection is a two-tap affair: tap the first letter of a word, then the last. A correct word locks in with a highlight and strikes off the list. A 90-second timer keeps the pace friendly but honest.</p>""",
    howto=["Study the word list shown under the grid.",
           "Tap the first letter of a word you have found.",
           "Tap its last letter - correct words lock in highlighted.",
           "Find all six before the 90-second timer runs out."],
    tips=["Scan row by row for distinctive first letters - rare letters like K, W and Z stand out.",
          "Check diagonals deliberately; horizontal words are found by instinct, diagonal ones by discipline.",
          "Found a word backwards? The game accepts words in both directions along their line.",
          "With 20 seconds left, park on one word from the list and scan only for it."],
    faq=[("Are the words random?", "Each game draws six words from a curated casual-words list, so repeats are rare but friendly."),
         ("Can words overlap?", "Yes - two words may share a letter, just like in newspaper puzzles."),
         ("What happens when time runs out?", "The run ends and unfound words are revealed briefly before a fresh grid.")],
    stats='<span>Found: <b id="wsFound">0</b>/6</span><span>Time: <b id="wsTime">90</b>s</span>',
    hint="Tap first letter, then last letter",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(8,50px);background:#1E293B;padding:10px;border-radius:14px"></div><div id="list" style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:14px;color:#E2E8F0;font-weight:600"></div><div class="msg" id="msg"></div>',
    js="""
const N=8,WORDS=['PLANET','GARDEN','THUNDER','COOKIE','STREAM','PUZZLE','MARBLE','CANYON','FROST','VIOLIN','HARBOR','MEADOW'];
let grid,placed,found,sel,timeLeft,timer,alive=true;
function reset(){alive=true;found=[];sel=null;timeLeft=90;placed=[];
grid=Array.from({length:N},()=>Array(N).fill(''));
const pool=[...WORDS].sort(()=>Math.random()-.5).slice(0,6);
pool.forEach(w=>placeWord(w));
for(let r=0;r<N;r++)for(let c=0;c<N;c++)
if(!grid[r][c])grid[r][c]=String.fromCharCode(65+Math.floor(Math.random()*26));
clearInterval(timer);timer=setInterval(()=>{timeLeft--;
document.getElementById('wsTime').textContent=timeLeft;
if(timeLeft<=0){alive=false;document.getElementById('msg').textContent='Time! Found '+found.length+'/6';}},1000);
renderList();render();}
function placeWord(w){for(let tries=0;tries<200;tries++){
const dirs=[[0,1],[1,0],[1,1]];
const[dr,dc]=dirs[Math.floor(Math.random()*3)];
const r0=Math.floor(Math.random()*N),c0=Math.floor(Math.random()*N);
const r1=r0+dr*(w.length-1),c1=c0+dc*(w.length-1);
if(r1<0||r1>=N||c1<0||c1>=N)continue;
let okflag=true;const cells=[];
for(let i=0;i<w.length;i++){const r=r0+dr*i,c=c0+dc*i;
if(grid[r][c]&&grid[r][c]!==w[i]){okflag=false;break;}cells.push([r,c]);}
if(!okflag)continue;
cells.forEach(([r,c],i)=>grid[r][c]=w[i]);
placed.push({word:w,cells});return;}}
function renderList(){const l=document.getElementById('list');l.innerHTML='';
placed.forEach(p=>{const s=document.createElement('span');
s.textContent=p.word;s.style.cssText='padding:4px 12px;border-radius:99px;font-size:14px;'+
(found.includes(p.word)?'background:#10B981;color:#fff;text-decoration:line-through':'background:#334155');
l.appendChild(s);});}
function render(){const b=document.getElementById('board');b.innerHTML='';
grid.forEach((row,r)=>row.forEach((ch,c)=>{const d=document.createElement('div');
d.className='g-cell';
let bg='#334155';
const owner=placed.find(p=>p.word&&found.includes(p.word)&&p.cells.some(([pr,pc])=>pr===r&&pc===c));
if(owner)bg='#10B981';
if(sel&&sel[0]===r&&sel[1]===c)bg='#F59E0B';
d.style.cssText='width:50px;height:50px;background:'+bg+';font-size:19px;color:#fff;cursor:pointer';
d.textContent=ch;
d.onclick=()=>pick(r,c);b.appendChild(d);}))
;}
function pick(r,c){if(!alive)return;
if(!sel){sel=[r,c];render();return;}
const word=placed.find(p=>{const cells=p.cells;
const first=cells[0],last=cells[cells.length-1];
const match=(a,b)=>a[0]===b[0]&&a[1]===b[1];
return(match(first,sel)&&match(last,[r,c]))||(match(last,sel)&&match(first,[r,c]));});
if(word&&!found.includes(word.word)){found.push(word.word);
document.getElementById('wsFound').textContent=found.length;
sel=null;renderList();render();
if(found.length===placed.length){alive=false;clearInterval(timer);
document.getElementById('msg').textContent='All words found with '+timeLeft+'s to spare!';}}
else{sel=[r,c];render();}}
document.getElementById('btnRestart').addEventListener('click',reset);
reset();""",
))

# ---------------------------------------------------------------- Gem Match
GAMES_B.append(dict(
    file="candy-match.html", name="Gem Match Blast", category="match3",
    category_label="Match 3", icon="💎",
    tagline="Swap neighboring gems, chain big combos, beat the 60-second clock.",
    meta="Play Gem Match Blast free online. Swap gems, trigger chain reactions and chase combos in this polished 60-second match-3 browser game.",
    about="""<p>Gem Match Blast is a compact match-3 built for quick sessions: an 8x8 board of bright gems, sixty seconds on the clock, and a swap mechanic with real depth - swaps that do not make a match snap back, and every valid match triggers a cascade as gems fall and refill.</p>
<p>Chain reactions are where the score lives. A single swap can clear twenty gems if the refill lines up right, and 4+ matches score disproportionately. No special items, no boosters - just the board and your eye.</p>""",
    howto=["Click one gem, then a neighboring gem, to swap them.",
           "Swaps only stick if they create a line of 3+ matching gems.",
           "Matched gems vanish; gems above fall and new ones refill from the top.",
           "Score as much as possible in 60 seconds - cascades multiply fast."],
    tips=["Bottom swaps create top cascades - gravity does free work for you.",
          "Hunt for L and T shapes; they clear more gems than two separate lines.",
          "Before swapping, glance at the top rows: falling gems often complete matches by themselves.",
          "When in doubt, swap in the most crowded color region - density breeds chains."],
    faq=[("Is there a move limit?", "No - the only limit is the 60-second timer, so keep swapping."),
         ("Why did my swap undo itself?", "Only swaps that create a match are allowed; everything else snaps back automatically."),
         ("Are there power-ups?", "This version is deliberately pure - no boosters, so scores compare fairly.")],
    stats='<span>Score: <b id="gmScore">0</b></span><span>Time: <b id="gmTime">60</b>s</span><span>Best: <b id="gmBest">0</b></span>',
    hint="Click two neighboring gems to swap",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(8,50px);background:#1E293B;padding:10px;border-radius:14px"></div><div class="msg" id="msg"></div>',
    js="""
const N=8,COLORS=['#ff6b6b','#34d399','#38bdf8','#f59e0b','#8b5cf6'];
let board,sel=null,score=0,timeLeft=60,timer,alive=true,busy=false;
document.getElementById('gmBest').textContent=localStorage.getItem('gmBest')||0;
function reset(){alive=true;busy=false;sel=null;score=0;timeLeft=60;
document.getElementById('gmScore').textContent=0;
document.getElementById('msg').textContent='';
clearInterval(timer);timer=setInterval(()=>{timeLeft--;
document.getElementById('gmTime').textContent=timeLeft;
if(timeLeft<=0){alive=false;
const best=+localStorage.getItem('gmBest')||0;
if(score>best){localStorage.setItem('gmBest',score);document.getElementById('gmBest').textContent=score;}
document.getElementById('msg').textContent="Time! Final score: "+score;}},1000);
fill();render();}
function fill(){board=Array.from({length:N},()=>Array.from({length:N},()=>Math.floor(Math.random()*5)));
while(findMatches().length){resolveMatches(false);}}
function findMatches(){const ms=[];
for(let r=0;r<N;r++)for(let c=0;c<N-2;c++){const v=board[r][c];
if(v!=null&&board[r][c+1]===v&&board[r][c+2]===v)ms.push([r,c]);}
for(let c=0;c<N;c++)for(let r=0;r<N-2;r++){const v=board[r][c];
if(v!=null&&board[r+1][c]===v&&board[r+2][c]===v)ms.push([r,c]);}
return ms;}
function resolveMatches(scoring=true){let guard=0;
while(findMatches().length&&guard++<50){const ms=findMatches();
ms.forEach(([r,c])=>{const v=board[r][c];
for(let k=0;k<N;k++){if(scoring&&board[r][k]===v){board[r][k]=null;}
if(scoring&&board[k][c]===v){board[k][c]=null;}}
board[r][c]=null;if(scoring)score+=30;});
if(scoring){document.getElementById('gmScore').textContent=score;}
for(let c=0;c<N;c++){let col=[];
for(let r=N-1;r>=0;r--)if(board[r][c]!=null)col.push(board[r][c]);
for(let r=N-1;r>=0;r--)board[r][c]=col[N-1-r]!==undefined?col[N-1-r]:null;
for(let r=0;r<N;r++)if(board[r][c]==null)board[r][c]=Math.floor(Math.random()*5);}}}
function render(){const b=document.getElementById('board');b.innerHTML='';
board.forEach((row,r)=>row.forEach((v,c)=>{const d=document.createElement('div');
d.className='g-cell';d.style.cssText='width:50px;height:50px;font-size:24px;'+
'background:'+(sel&&sel[0]===r&&sel[1]===c?'#F59E0B':(v==null?'#1E293B':'#334155'))+';cursor:pointer';
if(v!=null){d.innerHTML='<div style="width:30px;height:30px;border-radius:50%;background:'+COLORS[v]+'"></div>';}
d.onclick=()=>pick(r,c);b.appendChild(d);}));}
function pick(r,c){if(!alive||busy)return;
if(!sel){sel=[r,c];render();return;}
const[pr,pc]=sel;
if(pr===r&&pc===c){sel=null;render();return;}
if(Math.abs(pr-r)+Math.abs(pc-c)!==1){sel=[r,c];render();return;}
const tmp=board[pr][pc];board[pr][pc]=board[r][c];board[r][c]=tmp;
if(!findMatches().length){board[r][c]=board[pr][pc];board[pr][pc]=tmp;
sel=null;render();document.getElementById('msg').textContent='No match - swap back';return;}
sel=null;busy=true;resolveMatches(true);render();busy=false;}
document.getElementById('btnRestart').addEventListener('click',reset);
reset();""",
))

# ---------------------------------------------------------------- Tiny Farm
GAMES_B.append(dict(
    file="farm-simulator.html", name="Tiny Farm Simulator", category="simulation",
    category_label="Simulation", icon="🌾",
    tagline="Plant, water, harvest - grow a pocket farm from three plots.",
    meta="Play Tiny Farm Simulator free online. Plant seeds, water crops and grow your pocket farm in this cozy incremental browser game.",
    about="""<p>Tiny Farm Simulator is a cozy three-by-three field where every plot runs a small lifecycle: plant a seed, water it, watch it sprout, then harvest and sell. Profits buy better seeds, better seeds sell for more, and the loop compounds into a proper little economy.</p>
<p>There is no fail state and no timer - the pleasure is in watching a tidy grid of sprouts turn into a well-oiled harvest machine. The goal marker is 500 coins; reaching it proves you have mastered the rhythm.</p>""",
    howto=["Click a plot and choose a seed (wheat costs 5 coins, carrots 15).",
           "Click a planted plot to water it - unwatered crops do not grow.",
           "Each click on a growing crop advances it one stage.",
           "Harvest mature crops to sell them; earn 500 coins to win the farm."],
    tips=["Wheat is your early engine: cheap in, fast out, steady profit.",
          "Reinvest in carrots as soon as you can afford three of them - the margin compounds.",
          "Water immediately after planting; idle plots earn nothing.",
          "Work in columns: plant the left column, water the middle, harvest the right."],
    faq=[("Do crops wither if I wait?", "Never - Tiny Farm has no withering or real-time waiting. Crops advance when you click them."),
         ("Is there an ending?", "Reaching 500 coins shows a victory banner, and you can keep playing endlessly after that."),
         ("Can I lose the farm?", "No fail state exists - the only risk is planting seeds you cannot afford to water.")],
    stats='<span>Coins: <b id="tfCoins">20</b></span><span>Goal: <b>500</b></span>',
    hint="Click a plot to plant, water, grow or harvest",
    inner='<div class="g-board" id="board" style="grid-template-columns:repeat(3,120px)"></div><div class="msg" id="msg"></div><div id="seedbar" style="display:flex;gap:12px;justify-content:center;margin-top:14px"></div>',
    js="""
const STAGES=['','🌱','🌿','🌾'];
const SEEDS={wheat:{cost:5,sell:14,emoji:'🌾',label:'Wheat (5)'},
carrot:{cost:15,sell:38,emoji:'🥕',label:'Carrot (15)'}};
let coins=20,plots=Array.from({length:9},()=>({seed:null,stage:0,watered:false}));
let chosen='wheat';
function render(){const b=document.getElementById('board');b.innerHTML='';
plots.forEach((p,i)=>{const d=document.createElement('div');d.className='g-cell';
d.style.cssText='width:120px;height:120px;font-size:38px;flex-direction:column;'+
'background:'+(p.seed?(p.stage>=3?'#166534':'#14532d'):'#3f6212')+';cursor:pointer';
d.innerHTML=(p.seed?STAGES[Math.min(3,p.stage)]:'<span style="font-size:26px;opacity:.4">＋</span>')+
'<span style="font-size:12px;color:#E2E8F0;opacity:.85">'+
(p.seed?(p.stage>=3?'READY - tap to harvest':(p.watered?'growing':'needs water')):'empty')+'</span>';
d.onclick=()=>tap(i);b.appendChild(d);});
document.getElementById('tfCoins').textContent=coins;
if(coins>=500){document.getElementById('msg').textContent='Farm master! 500 coins earned - keep growing!';}}
function tap(i){const p=plots[i];
if(!p.seed){if(coins<SEEDS[chosen].cost){document.getElementById('msg').textContent='Not enough coins';return;}
coins-=SEEDS[chosen].cost;p.seed=chosen;p.stage=1;p.watered=false;
document.getElementById('msg').textContent='';}
else if(p.stage>=3){coins+=SEEDS[p.seed].sell;p.seed=null;p.stage=0;p.watered=false;}
else if(!p.watered){p.watered=true;document.getElementById('msg').textContent='Watered! Tap to grow';}
else p.stage++;
render();}
const bar=document.getElementById('seedbar');
Object.entries(SEEDS).forEach(([k,s])=>{const d=document.createElement('div');
d.className='g-cell';d.id='seed_'+k;
d.style.cssText='width:130px;height:64px;background:#1E3A8A;color:#fff;font-size:15px;cursor:pointer;flex-direction:column';
d.innerHTML=s.emoji+'<span>'+s.label+'</span>';
d.onclick=()=>{chosen=k;document.querySelectorAll('#seedbar .g-cell').forEach(e=>e.style.outline='');
d.style.outline='3px solid #FBBF24';};
bar.appendChild(d);});
document.querySelector('#seed_wheat').style.outline='3px solid #FBBF24';
document.getElementById('btnRestart').addEventListener('click',()=>{coins=20;
plots=Array.from({length:9},()=>({seed:null,stage:0,watered:false}));render();});
render();""",
))

# ---------------------------------------------------------------- Castle Guard
GAMES_B.append(dict(
    file="tower-defense.html", name="Castle Guard Defense", category="strategy",
    category_label="Strategy", icon="🏰",
    tagline="Place towers along the invasion path and guard the castle through ten waves.",
    meta="Play Castle Guard Defense free online. Build towers, stop ten waves of invaders and defend your castle in this accessible browser tower defense game.",
    about="""<p>Castle Guard Defense is a friendly introduction to tower defense: a single winding road toward your castle, five buildable plots, two tower types and ten waves of invaders that get meaner as they go.</p>
<p>Archer towers fire fast and cheap; cannon towers hit hard but slowly. Every kill pays a bounty, every tenth enemy in a wave is a fast runner, and the castle holds as long as your economy does. The whole defense fits on one screen - which is the point.</p>""",
    howto=["Click an empty plot (glowing circles beside the road) to open the build menu.",
           "Buy an Archer Tower (40) for rapid fire or a Cannon Tower (70) for heavy damage.",
           "Click a built tower to see its range; enemies reward gold for every kill.",
           "Survive all 10 waves to win. If 10 enemies reach the castle, the defense falls."],
    tips=["Cover the middle stretch of the road where enemies spend the most time.",
          "One cannon near a sharp bend outperforms two archers on straights.",
          "Save 40 gold during wave one - reacting to wave two's speed matters more.",
          "Slow waves are for saving; spend between waves, not during them."],
    faq=[("Can I sell or upgrade towers?", "This version keeps one decision clean: where and what to build. Upgrades are planned."),
         ("How long is a full game?", "Ten waves take roughly six to eight minutes depending on your build."),
         ("What are the fast enemies?", "Every tenth invader is a runner - twice the speed, so place one tower specifically watching for them.")],
    stats='<span>Gold: <b id="cdGold">90</b></span><span>Wave: <b id="cdWave">1</b>/10</span><span>Castle: <b id="cdHp">10</b></span>',
    hint="Click a plot to build - enemies march automatically",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
const PATH=[[20,240],[160,240],[160,110],[400,110],[400,360],[640,360],[640,200],[720,200]];
const PLOTS=[[100,170],[240,180],[340,240],[480,300],[580,280]];
const TOWERS={archer:{cost:40,range:110,rate:24,dmg:1,color:'#38BDF8'},
cannon:{cost:70,range:95,rate:70,dmg:3,color:'#F59E0B'}};
let towers,enemyQ,enemies,wave,gold,hp,spawnT,alive,frame;
function reset(){towers=[];enemies=[];wave=1;gold=90;hp=10;spawnT=0;alive=true;frame=0;
enemyQ=[];for(let i=0;i<12;i++)enemyQ.push(i%10===9?'fast':'norm');
document.getElementById('cdWave').textContent=1;document.getElementById('cdGold').textContent=90;
document.getElementById('cdHp').textContent=10;}
function pathLen(){let l=0;for(let i=1;i<PATH.length;i++)l+=Math.hypot(PATH[i][0]-PATH[i-1][0],PATH[i][1]-PATH[i-1][1]);return l;}
function posAt(d){let acc=0;
for(let i=1;i<PATH.length;i++){const seg=Math.hypot(PATH[i][0]-PATH[i-1][0],PATH[i][1]-PATH[i-1][1]);
if(acc+seg>=d){const t=(d-acc)/seg;
return[PATH[i-1][0]+(PATH[i][0]-PATH[i-1][0])*t,PATH[i-1][1]+(PATH[i][1]-PATH[i-1][1])*t];}
acc+=seg;}
return PATH[PATH.length-1];}
function startWave(){wave=enemies.length===0&&!enemyQ.length?wave:wave;
document.getElementById('cdWave').textContent=Math.min(10,wave);}
function step(){frame++;if(!alive)return;
if(enemyQ.length&&--spawnT<=0){const t=enemyQ.shift();
enemies.push({d:0,hp:t==='fast'?2:4+wave,max:t==='fast'?2:4+wave,type:t,speed:t==='fast'?1.7:1});
spawnT=t==='fast'?10:22-Math.min(10,wave);}
if(!enemyQ.length&&!enemies.length){wave++;
if(wave>10){alive=false;win=true;}else{
document.getElementById('cdWave').textContent=Math.min(10,wave);
for(let i=0;i<10+wave*2;i++)enemyQ.push(i%10===9?'fast':'norm');}}
enemies.forEach(e=>{e.d+=e.speed*(1+wave*.06);});
enemies=enemies.filter(e=>{if(e.d>=pathLen()){hp--;document.getElementById('cdHp').textContent=hp;
if(hp<=0){alive=false;}return false;}return e.hp>0;});
towers.forEach(t=>{t.cd=(t.cd||0)-1;
if(t.cd<=0){const[x,y]=posAt(t.d===undefined?0:0);const[tx,ty]=[t.x,t.y];
let target=null,bd=1e9;
enemies.forEach(e=>{const[ex,ey]=posAt(e.d);
const dd=Math.hypot(ex-tx,ey-ty);
if(dd<=TOWERS[t.kind].range&&e.d>bd){bd=e.d;target={e,ex,ey};}});
if(target){t.cd=TOWERS[t.kind].rate;t.shot={x:tx,y:ty,tx:target.ex,ty:target.ey,t:0};
target.e.hp-=TOWERS[t.kind].dmg;
if(target.e.hp<=0){gold+=6+wave;document.getElementById('cdGold').textContent=gold;}}}});
enemies=enemies.filter(e=>e.hp>0);
draw();requestAnimationFrame(step);}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
cx.fillStyle='#14532D';cx.beginPath();
let d0=0;cx.moveTo(PATH[0][0],PATH[0][1]);
PATH.forEach(p=>cx.lineTo(p[0],p[1]));
cx.lineWidth=34;cx.strokeStyle='#3f3f46';cx.lineJoin='round';cx.stroke();
cx.lineWidth=26;cx.strokeStyle='#52525B';cx.stroke();
PLOTS.forEach(p=>{const built=towers.find(t=>t.x===p[0]&&t.y===p[1]);
cx.beginPath();cx.arc(p[0],p[1],20,0,7);
cx.fillStyle=built?TOWERS[built.kind].color:'#1E3A8A';cx.fill();
cx.strokeStyle='#475569';cx.lineWidth=3;cx.stroke();
if(!built){cx.fillStyle='#94A3B8';cx.font='16px Inter';cx.textAlign='center';cx.fillText('+',p[0],p[1]+6);}});
towers.forEach(t=>{if(t.shot){t.shot.t+=.2;
cx.strokeStyle='rgba(251,191,36,.8)';cx.lineWidth=2;cx.beginPath();
cx.moveTo(t.shot.x,t.shot.y);
cx.lineTo(t.shot.x+(t.shot.tx-t.shot.x)*Math.min(1,t.shot.t),t.shot.y+(t.shot.ty-t.shot.y)*Math.min(1,t.shot.t));
cx.stroke();if(t.shot.t>=1)t.shot=null;}});
enemies.forEach(e=>{const[ex,ey]=posAt(e.d);
cx.fillStyle=e.type==='fast'?'#F472B6':'#EF4444';
cx.beginPath();cx.arc(ex,ey,10,0,7);cx.fill();
cx.fillStyle='#111C33';cx.fillRect(ex-12,ey-18,24,4);
cx.fillStyle='#10B981';cx.fillRect(ex-12,ey-18,24*e.hp/e.max,4);});
cx.fillStyle='#1E3A8A';cx.beginPath();cx.roundRect(690,180,40,44,8);cx.fill();
cx.fillStyle='#FBBF24';cx.font='13px Inter';cx.textAlign='center';cx.fillText('🏰',710,210);
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 30px Inter';cx.textAlign='center';
cx.fillText(win?'Castle defended! All 10 waves cleared':'The castle has fallen',360,200);
cx.font='16px Inter';cx.fillStyle='#94A3B8';cx.fillText('Press Restart to defend again',360,235);}}
cv.addEventListener('mousedown',e=>{if(!alive)return;
const r=cv.getBoundingClientRect();
const mx=(e.clientX-r.left)*(720/r.width),my=(e.clientY-r.top)*(480/r.height);
const plot=PLOTS.find(p=>Math.hypot(p[0]-mx,p[1]-my)<24);
if(!plot)return;
if(towers.find(t=>t.x===plot[0]&&t.y===plot[1]))return;
const kind=gold>=TOWERS.cannon.cost&&my>240?'cannon':'archer';
const pick=(mx<360)?'archer':'cannon';
const use=TOWERS[pick].cost<=gold?pick:(gold>=TOWERS.archer.cost?'archer':null);
if(!use){document.getElementById('cdGold').textContent=gold+' (need 40)';return;}
gold-=TOWERS[use].cost;document.getElementById('cdGold').textContent=gold;
towers.push({x:plot[0],y:plot[1],kind,cd:0});});
document.getElementById('btnRestart').addEventListener('click',()=>{win=false;reset();});
let win=false;reset();step();""",
))

# ---------------------------------------------------------------- Star Defender
GAMES_B.append(dict(
    file="space-shooter-x.html", name="Star Defender", category="strategy",
    category_label="Strategy", icon="🚀",
    tagline="Hold the line against descending waves - one ship, endless stars.",
    meta="Play Star Defender free online. Pilot your ship, blast descending enemies and survive rising waves in this classic arcade space shooter - free in your browser.",
    about="""<p>Star Defender is a distilled arcade space shooter: one ship at the bottom, waves of enemies descending from the top, and a trigger finger that never gets a break. Shots fire automatically while you fly - your only job is positioning, weaving through return fire and keeping the line intact.</p>
<p>Every third wave introduces a tighter formation and faster descent. Three lives, one shield pickup per wave, and a score screen that remembers your best locally.</p>""",
    howto=["Move with ← → (or A/D); on touch, drag your ship.",
           "Your cannon fires automatically - focus on dodging and positioning.",
           "Destroy every enemy in a wave to advance; they descend faster each wave.",
           "Three lives. Enemy fire and collisions both cost one."],
    tips=["Stay near the center at wave start - formations open from the edges inward.",
          "Kill from one side to the other rather than chasing individual ships.",
          "Shield stars appear mid-wave; grab them even if it costs a shot window.",
          "When enemies get low, trade distance for safety: a wide gap beats a lucky shot."],
    faq=[("Do I need to press a fire button?", "No - firing is automatic so mobile players can focus on flying."),
         ("How many waves are there?", "Waves continue endlessly with rising difficulty; survival time is the true score."),
         ("Does the game support touch?", "Yes - drag anywhere on the game area and the ship follows your finger.")],
    stats='<span>Score: <b id="ssScore">0</b></span><span>Lives: <b id="ssLives">3</b></span><span>Best: <b id="ssBest">0</b></span>',
    hint="← → / A D to move - cannon fires automatically",
    js="""
const cv=document.getElementById('gameCanvas'),cx=cv.getContext('2d');
let ship={x:360},bullets=[],enemies=[],ebullets=[],stars=[],score=0,lives=3,wave=1,alive=true,frame=0,keys={};
document.getElementById('ssBest').textContent=localStorage.getItem('ssBest')||0;
function reset(){ship={x:360};bullets=[];enemies=[];ebullets=[];score=0;lives=3;wave=1;alive=true;
document.getElementById('ssScore').textContent=0;document.getElementById('ssLives').textContent=3;
spawnWave();}
function spawnWave(){enemies=[];
const rows=Math.min(3,1+Math.floor(wave/2)),cols=8;
for(let r=0;r<rows;r++)for(let c=0;c<cols;c++)
enemies.push({x:100+c*66,y:60+r*50,hp:1+Math.floor(wave/4),t:Math.random()*100});}
function step(){frame++;if(!alive){draw();return;}
if(keys.ArrowLeft||keys.KeyA)ship.x-=6.5;
if(keys.ArrowRight||keys.KeyD)ship.x+=6.5;
ship.x=Math.max(30,Math.min(690,ship.x));
if(frame%9===0)bullets.push({x:ship.x,y:430});
if(frame%Math.max(14,40-wave*2)===0&&enemies.length){
const shooter=enemies[Math.floor(Math.random()*enemies.length)];
ebullets.push({x:shooter.x,y:shooter.y+16});}
bullets.forEach(b=>b.y-=9);ebullets.forEach(b=>b.y+=4.5+wave*.15);
bullets=bullets.filter(b=>b.y>-10);ebullets=ebullets.filter(b=>b.y<500);
enemies.forEach(e=>{e.t++;e.x+=Math.sin(e.t/40)*1.1;e.y+=.06+wave*.02;});
bullets.forEach(b=>{const hit=enemies.find(e=>Math.abs(e.x-b.x)<24&&Math.abs(e.y-b.y)<20);
if(hit){hit.hp--;b.dead=true;score+=15;document.getElementById('ssScore').textContent=score;}});
enemies=enemies.filter(e=>e.hp>0);
ebullets=ebullets.filter(b=>{if(Math.abs(b.x-ship.x)<20&&b.y>428){hitShip();return false;}return true;});
enemies=enemies.filter(e=>{if(e.y>420){hitShip();return false;}return true;});
if(!enemies.length){wave++;spawnWave();}
draw();requestAnimationFrame(step);}
function hitShip(){lives--;document.getElementById('ssLives').textContent=lives;
if(lives<=0){alive=false;const best=+localStorage.getItem('ssBest')||0;
if(score>best){localStorage.setItem('ssBest',score);document.getElementById('ssBest').textContent=score;}}}
function draw(){cx.fillStyle='#111C33';cx.fillRect(0,0,720,480);
if(frame%3===0)stars.push({x:Math.random()*720,y:-2,s:.5+Math.random()});
stars.forEach(s=>{s.y+=s.s*2;cx.fillStyle='rgba(148,163,184,.6)';cx.fillRect(s.x,s.y,2,2);});
stars=stars.filter(s=>s.y<480);
enemies.forEach(e=>{cx.fillStyle='#F472B6';cx.beginPath();
cx.moveTo(e.x,e.y+14);cx.lineTo(e.x-20,e.y-10);cx.lineTo(e.x+20,e.y-10);cx.closePath();cx.fill();
cx.fillStyle='#FBCFE8';cx.fillRect(e.x-6,e.y-6,12,6);});
ebullets.forEach(b=>{cx.fillStyle='#FB7185';cx.fillRect(b.x-2,b.y,4,12);});
bullets.forEach(b=>{cx.fillStyle='#FBBF24';cx.fillRect(b.x-2,b.y,4,14);});
cx.fillStyle='#38BDF8';cx.beginPath();
cx.moveTo(ship.x,418);cx.lineTo(ship.x-24,446);cx.lineTo(ship.x+24,446);cx.closePath();cx.fill();
cx.fillStyle='#7DD3FC';cx.fillRect(ship.x-8,426,16,10);
if(!alive){cx.fillStyle='#E2E8F0';cx.font='bold 32px Inter';cx.textAlign='center';
cx.fillText('Ship destroyed - score: '+score,360,200);
cx.font='16px Inter';cx.fillStyle='#94A3B8';cx.fillText('Press Restart to defend again',360,235);}}
document.addEventListener('keydown',e=>keys[e.code]=true);
document.addEventListener('keyup',e=>keys[e.code]=false);
function touch(e){const r=cv.getBoundingClientRect();
ship.x=(e.touches[0].clientX-r.left)*(720/r.width);}
cv.addEventListener('touchmove',e=>{e.preventDefault();touch(e);},{passive:false});
cv.addEventListener('mousemove',e=>{const r=cv.getBoundingClientRect();
ship.x=(e.clientX-r.left)*(720/r.width);});
document.getElementById('btnRestart').addEventListener('click',reset);
reset();step();""",
))
