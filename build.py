# -*- coding: utf-8 -*-
"""
Toolnex site builder - regenerates every page of the site.
All pages share one design system, one brand (Toolnex), and one rule:
every game is playable ON SITE, every page carries original written content.
"""
import os, datetime

from gen.games1 import GAMES_A
from gen.games2 import GAMES_B

GAMES = GAMES_A + GAMES_B
BASE = "https://www.toolnex.xyz"
TODAY = datetime.date.today().isoformat()
CATS = ["arcade", "racing", "puzzle", "match3", "sports", "simulation", "strategy"]

CSS = """
:root{--primary:#1E3A8A;--primary-light:#2563EB;--bg:#F1F5F9;--card:#FFF;--text:#0F172A;
--muted:#475569;--border:#E2E8F0;--shadow:0 4px 20px rgba(15,23,42,.06);--radius:16px}
*{margin:0;padding:0;box-sizing:border-box;font-family:Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif}
body{background:var(--bg);color:var(--text);line-height:1.65}
.container{max-width:1080px;margin:0 auto;padding:0 20px}
header{background:rgba(255,255,255,.92);border-bottom:1px solid var(--border);position:sticky;top:0;z-index:99;backdrop-filter:blur(8px)}
.header-inner{display:flex;justify-content:space-between;align-items:center;padding:14px 0;gap:16px;flex-wrap:wrap}
.logo{font-size:23px;font-weight:800;color:var(--primary);text-decoration:none;letter-spacing:-.5px}
.logo span{color:#D4AF37}
nav ul{display:flex;list-style:none;gap:22px;flex-wrap:wrap}
nav a{text-decoration:none;color:var(--text);font-weight:500;font-size:14px}
nav a:hover{color:var(--primary-light)}
.hero{padding:42px 0 26px;text-align:center}
.hero h1{font-size:34px;letter-spacing:-.8px;line-height:1.25}
.hero p{color:var(--muted);max-width:640px;margin:12px auto 0}
.btn{display:inline-block;background:var(--primary-light);color:#fff;padding:11px 24px;border-radius:12px;text-decoration:none;font-weight:600;font-size:14px;border:none;cursor:pointer}
.btn:hover{background:var(--primary)}
.btn.ghost{background:#fff;color:var(--primary-light);border:1px solid var(--border)}
section{padding:26px 0}
h2{font-size:24px;letter-spacing:-.4px;margin-bottom:14px}
h3{font-size:17px;margin:18px 0 8px}
.card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);padding:26px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:18px}
.game-card{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:22px;text-decoration:none;color:var(--text);box-shadow:var(--shadow);transition:transform .15s,box-shadow .15s;display:block}
.game-card:hover{transform:translateY(-4px);box-shadow:0 12px 34px rgba(15,23,42,.12)}
.game-card .icon{font-size:34px}
.game-card .name{font-weight:700;margin:10px 0 4px}
.game-card .cat{display:inline-block;background:#EFF6FF;color:var(--primary-light);font-size:12px;font-weight:600;padding:2px 10px;border-radius:99px}
.game-card p{color:var(--muted);font-size:13.5px;margin-top:8px}
/* game stage */
.stage{background:#0F172A;border-radius:var(--radius);padding:18px;box-shadow:var(--shadow)}
.stage-head{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;color:#E2E8F0;margin-bottom:12px}
.stage-head .stat{background:#1E293B;border-radius:10px;padding:6px 14px;font-size:14px}
.stage-head .stat b{color:#FBBF24}
.stage canvas{width:100%;max-width:720px;display:block;margin:0 auto;background:#111C33;border-radius:12px;touch-action:none}
.stage .dom-game{max-width:720px;margin:0 auto}
.stage button{background:var(--primary-light);border:none;color:#fff;font-weight:600;padding:9px 20px;border-radius:10px;cursor:pointer;font-size:14px}
.stage button:hover{background:#3B82F6}
.stage .hint{color:#94A3B8;font-size:13px;margin-top:10px;text-align:center}
/* dom game shared */
.g-board{display:grid;gap:6px;justify-content:center;margin:0 auto}
.g-cell{display:flex;align-items:center;justify-content:center;font-weight:700;border-radius:8px;user-select:none;cursor:pointer}
.msg{color:#E2E8F0;text-align:center;min-height:24px;font-weight:600;margin-top:10px}
/* faq */
.faq details{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:16px 20px;margin-bottom:10px}
.faq summary{font-weight:600;cursor:pointer}
.faq p{color:var(--muted);margin-top:10px;font-size:14.5px}
footer{background:var(--card);border-top:1px solid var(--border);margin-top:40px}
.footer-inner{display:flex;justify-content:space-between;flex-wrap:wrap;gap:14px;padding:26px 0;font-size:13.5px;color:var(--muted)}
.footer-inner a{color:var(--muted);text-decoration:none;margin-right:16px}
.footer-inner a:hover{color:var(--primary-light)}
.prose p{margin-bottom:12px;color:#334155}
.prose ul,.prose ol{margin:0 0 12px 22px;color:#334155}
.prose li{margin-bottom:6px}
.badge{display:inline-block;background:#EFF6FF;color:var(--primary-light);font-size:12.5px;font-weight:600;padding:4px 14px;border-radius:99px;margin-bottom:12px}
@media(max-width:640px){.hero h1{font-size:26px}h2{font-size:20px}}
"""

FOOT_NAV = """<a href="about.html">About</a><a href="contact.html">Contact</a>
<a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms of Use</a><a href="cookie-policy.html">Cookie Policy</a>"""

def header(active=""):
    def a(href, label, key):
        cls = ' class="active"' if key == active else ""
        return f'<a href="{href}"{cls}>{label}</a>'
    return f"""<header><div class="container header-inner">
<a class="logo" href="index.html">Tool<span>nex</span></a>
<nav><ul>{a('index.html','Home','home')}{a('games.html','Categories','cats')}{a('about.html','About','about')}{a('contact.html','Contact','contact')}</ul></nav>
</div></header>"""

def footer():
    return f"""<footer><div class="container footer-inner">
<div>{FOOT_NAV}</div>
<div>&copy; 2026 Toolnex &middot; Free browser games, playable instantly.</div>
</div></footer>"""

def game_card(g):
    return f"""<a class="game-card" href="{g['file']}">
<div class="icon">{g['icon']}</div>
<div class="name">{g['name']}</div>
<span class="cat">{g['category_label']}</span>
<p>{g['tagline']}</p></a>"""

def faq_html(g):
    items = "".join(
        f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in g["faq"])
    return f'<section class="faq"><div class="container"><h2>Frequently Asked Questions</h2>{items}</div></section>'

def faq_schema(g, url):
    import json
    ents = [{"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in g["faq"]]
    data = {"@context": "https://schema.org", "@type": "FAQPage", "url": url, "mainEntity": ents}
    return json.dumps(data, ensure_ascii=False)

def stage_html(g):
    head = ('<div class="stage-head">\n<div class="stat">{stats}</div>\n'
            '<button id="btnRestart" type="button">Restart</button>\n</div>\n')
    if "inner" in g:  # DOM-grid game
        return (head + '<div class="dom-game">' + g["inner"] + "</div>\n"
                + '<div class="hint">' + g["hint"] + "</div>").format(
                    stats=g.get("stats", ""))
    return (head + '<canvas id="gameCanvas" width="720" height="480"></canvas>\n'
            + '<div class="hint">' + g["hint"] + "</div>").format(
                stats=g.get("stats", ""))

def game_page(g):
    url = f"{BASE}/{g['file']}"
    related = [x for x in GAMES if x["category"] == g["category"] and x is not g][:3]
    if not related:
        related = [x for x in GAMES if x is not g][:3]
    related_html = "".join(game_card(r) for r in related)
    howto = "".join(f"<li>{s}</li>" for s in g["howto"])
    tips = "".join(f"<li>{t}</li>" for t in g["tips"])
    st = stage_html(g)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{g['name']} - Play Free Online | Toolnex</title>
<meta name="description" content="{g['meta']}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{g['name']} | Toolnex">
<meta property="og:description" content="{g['meta']}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{faq_schema(g, url)}</script>
</head>
<body>
{header('game')}
<div class="hero container" style="text-align:left;max-width:1080px">
<span class="badge">{g['category_label']} &middot; Free &middot; No download</span>
<h1>{g['name']}</h1>
<p>{g['tagline']}</p>
</div>
<section><div class="container">
<div class="stage">
{st}
</div>
</div></section>
<section class="prose"><div class="container card">
<h2>About This Game</h2>
{g['about']}
<h3>How to Play</h3>
<ol>{howto}</ol>
<h3>Tips &amp; Strategy</h3>
<ul>{tips}</ul>
</div></section>
{faq_html(g)}
<section><div class="container">
<h2>More {g['category_label']} Games</h2>
<div class="grid">{related_html}</div>
</div></section>
{footer()}
<script>
"use strict";
{g['js']}
</script>
</body>
</html>"""

def index_page():
    cards = "".join(game_card(g) for g in GAMES)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Toolnex - Play Free Online Games Instantly | No Downloads</title>
<meta name="description" content="Toolnex is a free browser-game portal: puzzle, racing, arcade, strategy and sports games you can play instantly in your browser. No downloads, no sign-ups, no install.">
<link rel="canonical" href="{BASE}/">
<meta property="og:title" content="Toolnex - Play Free Online Games Instantly">
<meta property="og:description" content="Free browser games across arcade, racing, puzzle, match-3, sports, simulation and strategy. Play instantly, no downloads.">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}/">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header('home')}
<div class="hero">
<div class="container">
<h1>Play Free Online Games, Instantly in Your Browser</h1>
<p>Toolnex brings together {len(GAMES)} original browser games across seven categories - arcade, racing, puzzle, match-3, sports, simulation and strategy. Every game runs directly on this page's link: no downloads, no accounts, no waiting.</p>
<a class="btn" href="#games">Browse All Games</a>
<a class="btn ghost" href="games.html">Explore by Category</a>
</div>
</div>
<section id="games"><div class="container">
<h2>All Games</h2>
<div class="grid">{cards}</div>
</div></section>
<section><div class="container card prose">
<h2>Why Play on Toolnex?</h2>
<p>We built Toolnex around a simple idea: a games site should respect your time. Every title here was designed (and is hosted) by us, so what you click is what you play - there are no redirects to other portals, no "open in a new window" detours, and no installs of any kind.</p>
<ul>
<li><b>Instant play.</b> Every game loads in under a second on desktop and mobile, right inside the page.</li>
<li><b>Truly free.</b> No accounts, no paywalls, no energy timers. Your progress is saved locally in your browser.</li>
<li><b>Family friendly.</b> Clean, colorful visuals and gentle difficulty curves make every title suitable for players of all ages.</li>
<li><b>Original design.</b> Our games are built in-house with HTML5, so the guides and tips you read here come straight from the people who made them.</li>
</ul>
<p>New titles are added regularly. If you enjoy a game, bookmark its page - your high scores are stored on your device so you can chase your own records any time.</p>
</div></section>
<section class="faq"><div class="container">
<h2>Frequently Asked Questions</h2>
<details><summary>Do I need to download or install anything?</summary><p>No. Every game on Toolnex is built with HTML5 and runs directly in your browser - Chrome, Edge, Firefox and Safari are all supported, on desktop and mobile alike.</p></details>
<details><summary>Is Toolnex really free?</summary><p>Yes, completely. There are no accounts, subscriptions or in-game purchases. The site is supported by unobtrusive advertising, which keeps every game free for everyone.</p></details>
<details><summary>Are the games safe for kids?</summary><p>All games on Toolnex are family friendly: no violence beyond cartoon-style action, no chat, no user-generated content and no external links inside gameplay.</p></details>
<details><summary>How do I save my high score?</summary><p>Scores are stored automatically in your browser's local storage. If you clear your browser data or switch devices, scores start fresh.</p></details>
</div></section>
{footer()}
</body>
</html>"""

def categories_page():
    blocks = []
    for cat in CATS:
        games = [g for g in GAMES if g["category"] == cat]
        if not games:
            continue
        label = games[0]["category_label"]
        cards = "".join(game_card(g) for g in games)
        blocks.append(f'<section id="{cat}"><div class="container"><h2>{label}</h2><div class="grid">{cards}</div></div></section>')
    body = "".join(blocks)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Game Categories | Toolnex</title>
<meta name="description" content="Browse all Toolnex games by category: arcade, racing, puzzle, match-3, sports, simulation and strategy. Free browser games, playable instantly.">
<link rel="canonical" href="{BASE}/games.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header('cats')}
<div class="hero"><div class="container">
<h1>Browse Games by Category</h1>
<p>Seven categories, {len(GAMES)} games, zero downloads. Pick a lane and start playing.</p>
</div></div>
{body}
{footer()}
</body>
</html>"""

ABOUT_BODY = """
<p>Toolnex is a free online games portal for people who want to play immediately. Every game on this site was designed and built in-house with HTML5, which means when you open a game page, the game is already there - no redirects, no downloads, no accounts.</p>
<h3>Our Mission</h3>
<p>The web used to be full of places where you could click a game and just play. We want Toolnex to be that kind of place again: clean pages, fast loads, honest descriptions and original games that respect your time. We add new titles regularly and keep improving the existing ones based on player feedback.</p>
<h3>What Makes Us Different</h3>
<ul>
<li><b>Everything is playable on site.</b> We do not link out to other portals or embed games we do not control.</li>
<li><b>Original content.</b> The guides, tips and FAQs on every game page are written by the team that built the game - not scraped or auto-generated.</li>
<li><b>Family friendly by design.</b> No chat, no user-generated content, no dark patterns.</li>
</ul>
<h3>Get in Touch</h3>
<p>Found a bug, have an idea for a new game, or just want to say hi? Visit the <a href="contact.html">contact page</a> - we read every message.</p>
"""

def about_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>About Us | Toolnex</title>
<meta name="description" content="Learn about Toolnex: a free browser-games portal where every game is built in-house and playable instantly. Our mission, our standards, and how to reach us.">
<link rel="canonical" href="{BASE}/about.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header('about')}
<div class="hero"><div class="container"><h1>About Toolnex</h1></div></div>
<section><div class="container card prose">{ABOUT_BODY}</div></section>
{footer()}
</body>
</html>"""

PRIVACY_BODY = """
<p><i>Last updated: {today}</i></p>
<p>This Privacy Policy explains what information Toolnex ("we", "us", "this website") collects when you visit www.toolnex.xyz, how we use it, and the choices you have. By using the site you agree to this policy.</p>
<h3>1. Information We Collect</h3>
<ul>
<li><b>Information you give us:</b> if you contact us by email or through our contact form, we receive your name, email address and the contents of your message.</li>
<li><b>Local storage:</b> your game scores and settings are stored only in your own browser (local storage) and are never transmitted to us.</li>
<li><b>Server logs:</b> like most websites, our hosting provider automatically records basic technical data (IP address, browser type, pages requested, date and time) for security and performance purposes.</li>
</ul>
<h3>2. Cookies and Advertising</h3>
<p>This site is supported by advertising. We use Google AdSense to display ads, and third-party vendors including Google use cookies to serve ads based on your prior visits to this and other websites.</p>
<ul>
<li>Google's use of advertising cookies enables it and its partners to serve ads to you based on your visit to this site and/or other sites on the Internet.</li>
<li>You may opt out of personalised advertising by visiting <a href="https://www.google.com/settings/ads" rel="noopener nofollow" target="_blank">Google Ads Settings</a>.</li>
<li>You can also opt out of third-party vendor cookies for personalised advertising at <a href="https://www.aboutads.info" rel="noopener nofollow" target="_blank">www.aboutads.info</a>.</li>
</ul>
<p>For more details, see our <a href="cookie-policy.html">Cookie Policy</a>.</p>
<h3>3. How We Use Information</h3>
<ul>
<li>To operate, maintain and improve the website and its games.</li>
<li>To respond to your questions and feedback.</li>
<li>To monitor for abuse, fraud and technical issues.</li>
</ul>
<h3>4. Children's Privacy</h3>
<p>Toolnex is family friendly and does not knowingly collect personal information from children under 13. If you believe a child has provided us personal information, contact us and we will delete it.</p>
<h3>5. Data Sharing</h3>
<p>We do not sell your personal information. We share data only with the service providers listed above (hosting and advertising), as required by law, or with your consent.</p>
<h3>6. Your Rights</h3>
<p>Depending on where you live (for example the EU/EEA or California), you may have the right to access, correct or delete personal data we hold about you, and to object to or restrict certain processing. To exercise these rights, contact us at the address on our <a href="contact.html">contact page</a>.</p>
<h3>7. Changes to This Policy</h3>
<p>We may update this policy from time to time. Changes are posted on this page with an updated date.</p>
<h3>8. Contact</h3>
<p>Questions about this policy? Reach us through the <a href="contact.html">contact page</a>.</p>
"""

def privacy_page():
    body = PRIVACY_BODY.replace("{today}", TODAY)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Privacy Policy | Toolnex</title>
<meta name="description" content="Toolnex privacy policy: what data we collect, how cookies and advertising work, and the rights you have over your information.">
<link rel="canonical" href="{BASE}/privacy.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header()}
<div class="hero"><div class="container"><h1>Privacy Policy</h1></div></div>
<section><div class="container card prose">{body}</div></section>
{footer()}
</body>
</html>"""

TERMS_BODY = """
<p><i>Last updated: {today}</i></p>
<p>Welcome to Toolnex. By accessing or using www.toolnex.xyz you agree to these Terms of Use. If you do not agree, please do not use the site.</p>
<h3>1. Use of the Site</h3>
<p>Toolnex provides free browser games for personal, non-commercial entertainment. You may play any game, on any device, as often as you like. You agree not to misuse the site - for example by attempting to hack it, scrape it at scale, or interfere with other visitors' enjoyment.</p>
<h3>2. Intellectual Property</h3>
<p>All games, artwork, text and design on Toolnex are created by and owned by Toolnex unless otherwise stated. You may not copy, republish, sell or redistribute our games or content without written permission. Deep-linking or embedding our game pages inside other websites or apps is not permitted.</p>
<h3>3. User-Provided Content</h3>
<p>If you send us feedback, ideas or suggestions, you grant us a non-exclusive, royalty-free right to use them to improve the site. Do not send us confidential information.</p>
<h3>4. Availability</h3>
<p>We work hard to keep the site available and bug-free, but Toolnex is provided "as is" without warranties of any kind. We may add, change, suspend or remove games or features at any time.</p>
<h3>5. Limitation of Liability</h3>
<p>To the maximum extent permitted by law, Toolnex and its operators are not liable for any indirect, incidental or consequential damages arising from your use of the site.</p>
<h3>6. Advertising</h3>
<p>The site displays advertising (including Google AdSense). Ad content is provided by third parties; we are not responsible for the products or services advertised. See our <a href="privacy.html">Privacy Policy</a> for details on advertising cookies.</p>
<h3>7. Changes to These Terms</h3>
<p>We may update these terms occasionally. Continued use of the site after changes means you accept the updated terms.</p>
<h3>8. Contact</h3>
<p>Questions about these terms? Reach us through the <a href="contact.html">contact page</a>.</p>
"""

def terms_page():
    body = TERMS_BODY.replace("{today}", TODAY)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Terms of Use | Toolnex</title>
<meta name="description" content="Toolnex terms of use: how our free games may be used, our intellectual property, advertising and liability terms.">
<link rel="canonical" href="{BASE}/terms.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header()}
<div class="hero"><div class="container"><h1>Terms of Use</h1></div></div>
<section><div class="container card prose">{body}</div></section>
{footer()}
</body>
</html>"""

COOKIE_BODY = """
<p><i>Last updated: {today}</i></p>
<h3>What Are Cookies?</h3>
<p>Cookies are small text files that websites store on your device. They are widely used to make sites work, remember preferences, and measure how the site is used.</p>
<h3>Cookies We Use</h3>
<ul>
<li><b>Essential local storage:</b> your game scores and settings are kept in your browser's local storage so your progress survives a page refresh. This data never leaves your device.</li>
<li><b>Advertising cookies:</b> we use Google AdSense. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google may use the DoubleClick cookie to serve ads based on your visit to our site and other sites on the internet.</li>
</ul>
<h3>Managing Cookies</h3>
<p>You can control or delete cookies through your browser settings - every major browser lets you block or remove cookies per site. Opting out of personalised advertising does not mean you will see fewer ads, only that the ads you see will be less relevant.</p>
<ul>
<li>Opt out of Google personalised ads: <a href="https://www.google.com/settings/ads" rel="noopener nofollow" target="_blank">Google Ads Settings</a></li>
<li>Opt out of many third-party ad cookies: <a href="https://www.aboutads.info" rel="noopener nofollow" target="_blank">www.aboutads.info</a></li>
</ul>
<p>See also our <a href="privacy.html">Privacy Policy</a>.</p>
"""

def cookie_page():
    body = COOKIE_BODY.replace("{today}", TODAY)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cookie Policy | Toolnex</title>
<meta name="description" content="How Toolnex uses cookies and local storage, including advertising cookies, and how to control them.">
<link rel="canonical" href="{BASE}/cookie-policy.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header()}
<div class="hero"><div class="container"><h1>Cookie Policy</h1></div></div>
<section><div class="container card prose">{body}</div></section>
{footer()}
</body>
</html>"""

CONTACT_BODY = """
<p>Questions, bug reports, game ideas or partnership inquiries - we would love to hear from you.</p>
<h3>Email</h3>
<p>Write to us at <b>support@toolnex.xyz</b> and we will reply within 1-2 business days.</p>
<h3>Before You Write</h3>
<ul>
<li><b>Game not loading?</b> Try refreshing the page, disabling aggressive ad blockers for this site, or switching to Chrome or Edge.</li>
<li><b>Lost your high score?</b> Scores are stored in your browser's local storage - clearing browser data removes them.</li>
<li><b>Suggestion?</b> Tell us the genre you want more of. Player requests directly shape our release schedule.</li>
</ul>
<h3>Contact Form</h3>
<form class="contact-form" action="mailto:support@toolnex.xyz" method="post" enctype="text/plain" onsubmit="this.querySelector('.sent').style.display='block'">
<label>Your name<br><input type="text" name="name" required style="width:100%;max-width:420px;padding:10px;border:1px solid var(--border);border-radius:10px;font-size:14px"></label><br><br>
<label>Your email<br><input type="email" name="email" required style="width:100%;max-width:420px;padding:10px;border:1px solid var(--border);border-radius:10px;font-size:14px"></label><br><br>
<label>Message<br><textarea name="message" rows="5" required style="width:100%;max-width:420px;padding:10px;border:1px solid var(--border);border-radius:10px;font-size:14px;font-family:inherit"></textarea></label><br><br>
<button class="btn" type="submit">Send Message</button>
<span class="sent" style="display:none;color:#16A34A;font-weight:600;margin-left:12px">Your email app should open now - just hit send!</span>
</form>
"""

def contact_page():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Contact Us | Toolnex</title>
<meta name="description" content="Contact the Toolnex team: support@toolnex.xyz. Questions, bug reports, game ideas and partnership inquiries are all welcome.">
<link rel="canonical" href="{BASE}/contact.html">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{header('contact')}
<div class="hero"><div class="container"><h1>Contact Us</h1></div></div>
<section><div class="container card prose">{CONTACT_BODY}</div></section>
{footer()}
</body>
</html>"""

ROBOTS = """User-agent: *
Allow: /

Sitemap: https://www.toolnex.xyz/sitemap.xml
"""

def sitemap():
    pages = ["/"] + [f"/{g['file']}" for g in GAMES] + [
        "/categories.html", "/about.html", "/contact.html",
        "/privacy.html", "/terms.html", "/cookie-policy.html"]
    urls = []
    for p in pages:
        loc = BASE + p
        prio = "1.0" if p == "/" else ("0.9" if p.endswith(".html") and p.count("/") == 1 and not p[1:].split(".")[0] in ("about","contact","privacy","terms","cookie-policy","games") else "0.6")
        urls.append(f"<url><loc>{loc}</loc><lastmod>{TODAY}</lastmod><priority>{prio}</priority></url>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "\n".join(urls) + "\n</urlset>\n")

def main():
    root = os.path.dirname(os.path.abspath(__file__))
    out = lambda name, content: open(os.path.join(root, name), "w", encoding="utf-8").write(content)
    out("index.html", index_page())
    out("games.html", categories_page())
    out("about.html", about_page())
    out("privacy.html", privacy_page())
    out("terms.html", terms_page())
    out("cookie-policy.html", cookie_page())
    out("contact.html", contact_page())
    out("robots.txt", ROBOTS)
    out("sitemap.xml", sitemap())
    for g in GAMES:
        out(g["file"], game_page(g))
    print(f"Built {len(GAMES)} game pages + 6 static pages + robots.txt + sitemap.xml")

if __name__ == "__main__":
    main()
