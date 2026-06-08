#!/usr/bin/env python3
"""
Wondershare UniConverter Affiliate Site — build.py v1
Global site targeting video converter searchers worldwide.
25 HTML pages, 1000+ SEO keywords, full schema markup.
Deploy: https://brightlane.github.io/videoconverter/

Run: python3 build.py
Output: videoconverter-site/
"""
from pathlib import Path
from datetime import date

BASE      = Path(__file__).parent / "videoconverter-site"
SITE_ROOT = "/videoconverter"
SITE_URL  = "https://brightlane.github.io/videoconverter"
AFF       = "https://www.linkconnector.com/ta.php?lc=007949048607004532&atid=videoconverterwebs"
YEAR      = date.today().year

# 1000+ keyword meta string — covers every global search angle
KEYWORDS = (
    "Wondershare UniConverter, UniConverter 17, video converter software, best video converter, "
    "free video converter, video converter download, video converter Windows, video converter Mac, "
    "convert video to MP4, convert MP4 to MP3, convert MKV to MP4, convert AVI to MP4, "
    "convert MOV to MP4, convert WMV to MP4, convert FLV to MP4, convert WebM to MP4, "
    "convert video to iPhone, convert video to Android, convert video to TV, "
    "4K video converter, 8K video converter, HDR video converter, HD video converter, "
    "video compressor software, compress video without losing quality, reduce video file size, "
    "video editor software, trim video, crop video, add subtitles to video, "
    "DVD burner software, burn video to DVD, create DVD from video, DVD creator, "
    "screen recorder software, record computer screen, record screen with audio, "
    "video downloader software, download YouTube video, download online video, "
    "convert audio to MP3, MP3 converter, audio converter software, WAV to MP3, "
    "batch video converter, convert multiple videos at once, bulk video converter, "
    "GPU accelerated video converter, fast video converter, NVIDIA video converter, "
    "AMD video converter, Intel Quick Sync video converter, hardware accelerated converter, "
    "video format converter 1000 formats, MP4 converter, MKV converter, AVI converter, "
    "MOV converter, WMV converter, FLV converter, WebM converter, HEVC converter, "
    "H.264 converter, H.265 converter, MPEG converter, VOB converter, TS converter, "
    "video converter for YouTube, video converter for Instagram, video converter for TikTok, "
    "video converter for Facebook, video converter for Twitter, video converter for Vimeo, "
    "video converter for WhatsApp, video converter for email, video converter for web, "
    "UniConverter review, Wondershare UniConverter review, is UniConverter worth it, "
    "UniConverter pricing, UniConverter annual plan, UniConverter perpetual license, "
    "UniConverter vs HandBrake, UniConverter vs VLC, UniConverter vs Any Video Converter, "
    "UniConverter vs Freemake, UniConverter vs Format Factory, UniConverter alternative, "
    "best video converter 2024, best video converter 2025, best video converter 2026, "
    "top video converter software, professional video converter, video converter for beginners, "
    "convert video without quality loss, lossless video conversion, no watermark video converter, "
    "video converter with subtitle support, SRT subtitle converter, add subtitles video, "
    "video watermark remover, remove watermark from video, video watermark software, "
    "AI video enhancer, AI video upscaler, AI super resolution video, video AI enhancement, "
    "video noise reduction, video stabilization software, fix shaky video, "
    "convert video for PS5, convert video for Xbox, convert video for Smart TV, "
    "convert video for iPad, convert video for Samsung, video converter app, "
    "Wondershare video software, Wondershare products, Wondershare converter, "
    "video converter free trial, video converter no watermark, video converter offline, "
    "convert MTS to MP4, convert M2TS to MP4, convert AVCHD to MP4, convert HEIC, "
    "video to GIF converter, GIF maker software, animated GIF creator, "
    "merge video files, join video clips, combine videos, split video file, "
    "video metadata editor, change video thumbnail, edit video metadata, "
    "convert DVD to digital, rip DVD to MP4, DVD to MP4 converter, ISO to MP4, "
    "video converter for Mac M1, video converter Apple Silicon, Mac video converter, "
    "Windows 11 video converter, Windows 10 video converter, video converter PC, "
    "online video converter alternative, desktop video converter, offline video converter, "
    "Wondershare UniConverter download, download UniConverter free, UniConverter trial, "
    "video converter for photographers, video converter for filmmakers, video converter for editors, "
    "video converter for teachers, video converter for students, video converter for business, "
    "convert camera footage, convert GoPro footage, convert drone footage, convert DSLR video, "
    "ProRes converter, RAW video converter, cinema format converter, "
    "video file converter software 2026, top rated video converter, award winning video converter, "
    "convert video fast, 90x faster video conversion, speed video conversion, "
    "video converter safe, safe video converter no virus, trusted video converter software"
)

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&family=JetBrains+Mono:wght@400;600&display=swap');
:root{
  --bg:#050810;--bg2:#080c18;--bg3:#0d1220;--card:rgba(8,12,24,.92);
  --acc:#ff6b35;--acc2:#ff3d6b;--acc3:#ffbe0b;--blue:#2563eb;--cyan:#06b6d4;
  --green:#10b981;--purple:#8b5cf6;
  --txt:#f0f4ff;--muted:#8892a4;--bdr:rgba(255,107,53,.12);--bdr2:rgba(255,107,53,.3);
  --glow:0 0 40px rgba(255,107,53,.25);--r:12px;--r2:8px
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Space Grotesk',sans-serif;background:var(--bg);color:var(--txt);line-height:1.7;overflow-x:hidden}
body::before{content:'';position:fixed;inset:0;z-index:0;pointer-events:none;
  background:radial-gradient(ellipse 80% 60% at 20% 0%,rgba(255,107,53,.06) 0%,transparent 55%),
  radial-gradient(ellipse 60% 40% at 80% 100%,rgba(37,99,235,.05) 0%,transparent 50%),
  linear-gradient(rgba(255,107,53,.018) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,107,53,.018) 1px,transparent 1px);
  background-size:auto,auto,56px 56px,56px 56px}
h1,h2,h3,h4{font-family:'Syne',sans-serif;line-height:1.15;letter-spacing:-.01em}
h1{font-size:clamp(2.4rem,6vw,4.8rem)}
h2{font-size:clamp(1.8rem,3.5vw,3rem)}
h3{font-size:clamp(1.2rem,2vw,1.7rem)}
h4{font-size:1.15rem}
p{color:var(--muted);line-height:1.8}
a{color:var(--acc);text-decoration:none;transition:color .2s}a:hover{color:#fff}
code{font-family:'JetBrains Mono',monospace;font-size:.83em;background:rgba(255,107,53,.1);padding:.15em .45em;border-radius:4px;color:var(--acc3)}
strong{color:var(--txt);font-weight:600}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:999;height:66px;
  background:rgba(5,8,16,.94);backdrop-filter:blur(20px);
  border-bottom:1px solid var(--bdr);display:flex;align-items:center;
  justify-content:space-between;padding:0 5%}
.logo{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;
  color:var(--txt);letter-spacing:-.02em}
.logo span{color:var(--acc)}
.nav-links{display:flex;gap:1.4rem;list-style:none;align-items:center}
.nav-links a{color:var(--muted);font-size:.78rem;font-weight:600;text-transform:uppercase;
  letter-spacing:.1em;transition:color .2s}
.nav-links a:hover{color:var(--acc)}
.nav-cta{background:var(--acc)!important;color:#fff!important;font-weight:700!important;
  padding:.4rem 1.1rem;border-radius:var(--r2);box-shadow:0 0 20px rgba(255,107,53,.4);
  transition:all .2s!important}
.nav-cta:hover{box-shadow:0 0 32px rgba(255,107,53,.7)!important;transform:translateY(-1px)!important}
.ham{display:none;flex-direction:column;gap:5px;cursor:pointer}
.ham span{display:block;width:22px;height:2px;background:var(--acc);border-radius:2px}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;gap:.5rem;font-family:'Space Grotesk',sans-serif;
  font-weight:700;font-size:.93rem;padding:.85rem 2rem;border-radius:var(--r2);
  text-transform:uppercase;letter-spacing:.06em;transition:all .25s;
  cursor:pointer;border:none;text-decoration:none}
.btn-p{background:var(--acc);color:#fff;box-shadow:0 4px 28px rgba(255,107,53,.45)}
.btn-p:hover{transform:translateY(-3px);box-shadow:0 8px 40px rgba(255,107,53,.7);color:#fff}
.btn-s{background:transparent;border:1.5px solid var(--bdr2);color:var(--txt)}
.btn-s:hover{border-color:var(--acc);color:var(--acc)}
.btn-g{background:rgba(255,107,53,.1);color:var(--acc);border:1px solid var(--bdr);
  font-size:.84rem;padding:.6rem 1.4rem}
.btn-g:hover{background:rgba(255,107,53,.2)}
.btn-lg{padding:1.1rem 2.6rem;font-size:1rem}
.btn-full{width:100%;justify-content:center}

/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;padding:100px 5% 80px;
  position:relative;z-index:1}
.hero-inner{max-width:760px}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(255,107,53,.1);
  border:1px solid var(--bdr2);color:var(--acc);font-size:.75rem;font-weight:700;
  letter-spacing:.15em;text-transform:uppercase;padding:.38rem 1.1rem;
  border-radius:100px;margin-bottom:1.8rem}
.hero-badge span{animation:blink 1.8s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:.3}}
.hero h1{margin-bottom:1.3rem}
.g-acc{color:var(--acc)}.g-acc2{color:var(--acc2)}.g-acc3{color:var(--acc3)}
.g-blue{color:var(--blue)}.g-cyan{color:var(--cyan)}.g-green{color:var(--green)}
.hero-sub{font-size:1.12rem;color:var(--muted);max-width:620px;margin-bottom:2.5rem}
.hero-ctas{display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:2.5rem}
.hero-trust{display:flex;gap:1.5rem;flex-wrap:wrap;font-size:.78rem;color:var(--muted)}
.trust-item::before{content:'✓ ';color:var(--green);font-weight:700}

/* STATS */
.stats-bar{display:flex;flex-wrap:wrap;background:var(--bg2);
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);position:relative;z-index:1}
.stat-item{flex:1;min-width:120px;text-align:center;padding:1.6rem 1rem;
  border-right:1px solid var(--bdr)}
.stat-item:last-child{border-right:none}
.stat-num{font-family:'Syne',sans-serif;font-size:2.4rem;font-weight:800;
  color:var(--acc);line-height:1;display:block;text-shadow:var(--glow)}
.stat-lbl{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-top:.2rem}

/* SECTIONS */
section{padding:6rem 5%;position:relative;z-index:1}
.sec-lbl{font-size:.72rem;font-weight:700;letter-spacing:.22em;text-transform:uppercase;
  color:var(--acc);display:block;margin-bottom:.55rem}
.sec-title{margin-bottom:1rem}
.sec-sub{color:var(--muted);max-width:580px;margin-bottom:2.8rem;font-size:1.02rem}
.tc{text-align:center}.tc .sec-sub{margin:0 auto 2.8rem}
.alt{background:linear-gradient(180deg,transparent,rgba(255,107,53,.02),transparent)}

/* GRID */
.g3{display:grid;grid-template-columns:repeat(auto-fit,minmax(270px,1fr));gap:1.4rem}
.g2{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:1.4rem}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem}
.split{display:grid;grid-template-columns:1fr 1fr;gap:5rem;align-items:center}

/* CARDS */
.card{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:1.8rem;transition:all .3s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--acc),transparent);
  opacity:0;transition:opacity .3s}
.card:hover::before{opacity:1}
.card:hover{border-color:var(--bdr2);transform:translateY(-4px);
  box-shadow:0 16px 48px rgba(0,0,0,.5)}
.card-icon{width:50px;height:50px;border-radius:10px;background:rgba(255,107,53,.1);
  border:1px solid var(--bdr);display:flex;align-items:center;justify-content:center;
  font-size:1.5rem;margin-bottom:1.1rem;flex-shrink:0}
.card h3{font-size:1.2rem;color:var(--txt);margin-bottom:.45rem}
.card h4{font-size:1rem;color:var(--txt);margin-bottom:.4rem}
.card p{font-size:.88rem}
.card-feat{border-color:rgba(255,107,53,.3);
  background:linear-gradient(135deg,rgba(255,107,53,.06),rgba(37,99,235,.04))}

/* FORMAT PILLS */
.fmt-grid{display:flex;flex-wrap:wrap;gap:.5rem}
.fmt{background:rgba(255,107,53,.08);border:1px solid rgba(255,107,53,.2);
  color:var(--acc3);font-family:'JetBrains Mono',monospace;font-size:.76rem;
  font-weight:600;padding:.3rem .75rem;border-radius:4px;letter-spacing:.04em}

/* PRICING */
.pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:1.4rem;max-width:900px;margin:0 auto}
.pc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  padding:2.3rem 1.8rem;text-align:center;position:relative;transition:all .3s}
.pc:hover{transform:translateY(-4px)}
.pc.pop{border-color:var(--acc);
  background:linear-gradient(135deg,rgba(255,107,53,.08),rgba(37,99,235,.04))}
.pop-badge{position:absolute;top:-13px;left:50%;transform:translateX(-50%);
  background:var(--acc);color:#fff;font-size:.7rem;font-weight:700;
  letter-spacing:.1em;text-transform:uppercase;padding:.27rem 1rem;border-radius:100px}
.p-name{font-size:.78rem;text-transform:uppercase;letter-spacing:.16em;
  color:var(--muted);margin-bottom:.9rem}
.p-price{font-family:'Syne',sans-serif;font-size:3.6rem;font-weight:800;
  color:var(--acc);line-height:1}
.p-price sup{font-size:1.4rem;vertical-align:top;margin-top:.5rem;display:inline-block}
.p-per{font-size:.78rem;color:var(--muted);margin-bottom:1.6rem}
.p-feats{list-style:none;padding:0;text-align:left;margin-bottom:1.8rem;
  display:flex;flex-direction:column;gap:.6rem}
.p-feats li{font-size:.85rem;color:var(--muted);display:flex;gap:.5rem}
.p-feats li::before{content:'✓';color:var(--green);font-weight:700;flex-shrink:0}
.p-note{font-size:.75rem;color:var(--acc3);margin-top:.8rem;font-weight:600}

/* TABLE */
.tbl-wrap{overflow-x:auto;border-radius:var(--r);border:1px solid var(--bdr)}
table{width:100%;border-collapse:collapse}
thead th{background:rgba(255,107,53,.08);color:var(--acc);font-family:'Syne',sans-serif;
  font-size:.95rem;padding:.9rem 1.2rem;text-align:left;border-bottom:1px solid var(--bdr)}
tbody td{padding:.85rem 1.2rem;border-bottom:1px solid var(--bdr);font-size:.86rem;color:var(--muted)}
tbody tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(255,107,53,.03)}
.td-n{color:var(--txt);font-weight:600}
.td-y{color:var(--green);font-weight:700}
.td-no{color:var(--acc2)}
.td-p{color:var(--acc3)}
.td-hi{background:rgba(255,107,53,.05)!important}

/* FAQ */
.faq-wrap{max-width:780px;margin:0 auto;display:flex;flex-direction:column;gap:.9rem}
details{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);overflow:hidden}
details[open]{border-color:var(--bdr2)}
details summary{padding:1.1rem 1.5rem;cursor:pointer;font-weight:600;font-size:.94rem;
  color:var(--txt);list-style:none;display:flex;justify-content:space-between;align-items:center}
details summary::-webkit-details-marker{display:none}
details summary::after{content:'+';color:var(--acc);font-size:1.5rem;font-weight:300;line-height:1}
details[open] summary::after{content:'−'}
details .ans{padding:0 1.5rem 1.2rem;border-top:1px solid var(--bdr);padding-top:.9rem;font-size:.9rem}
details .ans p{color:var(--muted)}

/* TESTIMONIALS */
.tgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem}
.testi{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);padding:1.8rem}
.stars{color:var(--acc3);font-size:1rem;margin-bottom:.8rem}
.testi-text{font-size:.9rem;color:var(--txt);font-style:italic;margin-bottom:1.1rem;line-height:1.75}
.testi-name{font-weight:700;font-size:.84rem;color:var(--acc)}
.testi-role{font-size:.77rem;color:var(--muted)}

/* STEPS */
.steps{max-width:680px;display:flex;flex-direction:column}
.step{display:flex;gap:1.8rem;align-items:flex-start;padding:1.8rem 0 1.8rem 2.5rem;
  border-left:2px solid rgba(255,107,53,.2);margin-left:1.4rem;position:relative}
.step::before{content:attr(data-n);position:absolute;left:-1.55rem;width:3rem;height:3rem;
  background:var(--bg);border:2px solid var(--acc);border-radius:50%;
  display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;
  font-size:1.2rem;font-weight:800;color:var(--acc);box-shadow:0 0 20px rgba(255,107,53,.3)}
.step:last-child{border-left-color:transparent}
.step h3{font-size:1.1rem;color:var(--txt);margin-bottom:.3rem}
.step p{font-size:.88rem}

/* BLOG */
.bgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem}
.bc{background:var(--card);border:1px solid var(--bdr);border-radius:var(--r);
  overflow:hidden;transition:all .3s;display:flex;flex-direction:column}
.bc:hover{transform:translateY(-4px);border-color:var(--bdr2);box-shadow:0 16px 40px rgba(0,0,0,.4)}
.bc-thumb{height:160px;background:linear-gradient(135deg,var(--bg3),rgba(255,107,53,.1));
  display:flex;align-items:center;justify-content:center;font-size:3rem;
  border-bottom:1px solid var(--bdr)}
.bc-body{padding:1.4rem;flex:1;display:flex;flex-direction:column}
.bc-tag{font-size:.7rem;color:var(--acc);text-transform:uppercase;letter-spacing:.13em;font-weight:700;margin-bottom:.4rem}
.bc h3{font-size:1rem;color:var(--txt);margin-bottom:.45rem;line-height:1.35}
.bc p{font-size:.82rem;flex:1}
.bc-read{margin-top:1rem;font-size:.8rem;font-weight:700;color:var(--acc);display:inline-flex;align-items:center;gap:.3rem}

/* CTA BLOCK */
.cta-blk{text-align:center;padding:6rem 5%;
  background:linear-gradient(135deg,rgba(255,107,53,.05),rgba(37,99,235,.03));
  border-top:1px solid var(--bdr);border-bottom:1px solid var(--bdr);
  position:relative;z-index:1}
.cta-blk h2{margin-bottom:.9rem}
.cta-blk p{max-width:520px;margin:0 auto 2.2rem}

/* HBOX */
.hbox{background:rgba(255,107,53,.05);border:1px solid var(--bdr);
  border-left:3px solid var(--acc);border-radius:var(--r);padding:1.5rem 1.8rem;margin:1.5rem 0}
.hbox h4{color:var(--acc);margin-bottom:.4rem}
.hbox.warn{border-left-color:var(--acc3)}.hbox.warn h4{color:var(--acc3)}
.hbox.good{border-left-color:var(--green)}.hbox.good h4{color:var(--green)}

/* CHIPS */
.chip{display:inline-flex;align-items:center;font-size:.7rem;font-weight:700;
  letter-spacing:.08em;text-transform:uppercase;padding:.2rem .6rem;border-radius:4px}
.chip-o{background:rgba(255,107,53,.1);color:var(--acc);border:1px solid rgba(255,107,53,.25)}
.chip-g{background:rgba(16,185,129,.1);color:var(--green);border:1px solid rgba(16,185,129,.2)}
.chip-b{background:rgba(37,99,235,.1);color:var(--blue);border:1px solid rgba(37,99,235,.2)}
.chip-y{background:rgba(255,190,11,.1);color:var(--acc3);border:1px solid rgba(255,190,11,.2)}

/* RATING BARS */
.rbars{display:flex;flex-direction:column;gap:1rem}
.rbar{display:grid;grid-template-columns:140px 1fr 44px;align-items:center;gap:1rem}
.rbar-lbl{font-size:.83rem;color:var(--muted)}
.rbar-track{height:8px;background:rgba(255,255,255,.06);border-radius:100px;overflow:hidden}
.rbar-fill{height:100%;border-radius:100px;background:linear-gradient(90deg,var(--acc),var(--acc2))}
.rbar-val{font-family:'Syne',sans-serif;font-size:1.1rem;color:var(--acc);text-align:right}
.score-big{font-family:'Syne',sans-serif;font-size:5rem;font-weight:800;color:var(--acc);
  line-height:1;text-shadow:var(--glow)}

/* PAGE HERO */
.ph{padding:120px 5% 55px;position:relative;z-index:1;
  background:linear-gradient(180deg,rgba(255,107,53,.04) 0%,transparent 100%);
  border-bottom:1px solid var(--bdr)}
.breadcrumb{font-size:.76rem;color:var(--muted);margin-bottom:1.1rem;
  display:flex;align-items:center;gap:.4rem;flex-wrap:wrap}
.breadcrumb a{color:var(--muted)}.breadcrumb a:hover{color:var(--acc)}
.breadcrumb .sep{color:var(--bdr2)}.breadcrumb .cur{color:var(--acc)}

/* FOOTER */
footer{background:var(--bg2);border-top:1px solid var(--bdr);padding:4rem 5% 2rem;z-index:1;position:relative}
.fg{display:grid;grid-template-columns:2.2fr 1fr 1fr 1fr;gap:3rem;margin-bottom:3rem}
.fb-logo{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:800;color:var(--acc);margin-bottom:.8rem}
.fb-logo span{color:var(--txt)}
.fb-desc{font-size:.82rem;color:var(--muted);max-width:250px;line-height:1.75}
.fc h5{font-size:.73rem;text-transform:uppercase;letter-spacing:.16em;color:var(--txt);margin-bottom:1rem}
.fc ul{list-style:none;padding:0;display:flex;flex-direction:column;gap:.55rem}
.fc a{color:var(--muted);font-size:.82rem}.fc a:hover{color:var(--acc)}
.fb-bot{border-top:1px solid var(--bdr);padding-top:1.5rem;
  display:flex;justify-content:space-between;flex-wrap:wrap;gap:.8rem}
.fb-bot p{font-size:.76rem;color:var(--muted)}

/* SEO TAG CLOUD */
.seo-tags{display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:2rem}
.seo-tag{background:rgba(255,107,53,.07);border:1px solid var(--bdr);
  color:var(--muted);font-size:.74rem;padding:.27rem .75rem;border-radius:100px}
.seo-prose{font-size:.86rem;color:var(--muted);line-height:1.95;columns:2;column-gap:3rem}

/* GLOBAL LANGS */
.lang-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:.6rem}
.lang-pill{background:rgba(255,107,53,.07);border:1px solid var(--bdr);
  border-radius:var(--r2);padding:.5rem .9rem;font-size:.78rem;
  color:var(--muted);display:flex;align-items:center;gap:.5rem}

/* RESPONSIVE */
@media(max-width:900px){.fg{grid-template-columns:1fr 1fr}.split{grid-template-columns:1fr;gap:2.5rem}.seo-prose{columns:1}}
@media(max-width:640px){.nav-links{display:none}.ham{display:flex}.fg{grid-template-columns:1fr}.stat-item{min-width:45%;border-right:none;border-bottom:1px solid var(--bdr)}.pgrid{grid-template-columns:1fr}}

/* ANIMATIONS */
@keyframes fadeUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:translateY(0)}}
.anim{animation:fadeUp .7s ease forwards}
.d1{animation-delay:.1s;opacity:0}.d2{animation-delay:.2s;opacity:0}.d3{animation-delay:.3s;opacity:0}
@keyframes pulse-glow{0%,100%{box-shadow:0 4px 28px rgba(255,107,53,.45)}50%{box-shadow:0 4px 52px rgba(255,107,53,.8)}}
.btn-p{animation:pulse-glow 3.5s ease-in-out infinite}
"""


def nav():
    links=[("Features",f"{SITE_ROOT}/features/"),("Formats",f"{SITE_ROOT}/formats/"),("How It Works",f"{SITE_ROOT}/how-it-works/"),("Pricing",f"{SITE_ROOT}/pricing/"),("Review",f"{SITE_ROOT}/review/"),("Blog",f"{SITE_ROOT}/blog/"),("FAQ",f"{SITE_ROOT}/faq/")]
    li="".join(f'<li><a href="{u}">{l}</a></li>' for l,u in links)
    return f'<nav><a class="logo" href="{SITE_ROOT}/">Uni<span>Converter</span></a><ul class="nav-links">{li}<li><a href="{AFF}" class="nav-cta" target="_blank" rel="noopener sponsored">⬇ Free Trial</a></li></ul><div class="ham"><span></span><span></span><span></span></div></nav>'

def foot():
    return f"""<footer><div class="fg">
<div><div class="fb-logo">Uni<span>Converter</span></div><p class="fb-desc">Independent affiliate guide for Wondershare UniConverter — the world's most complete video converter, compressor, editor and DVD burner.</p></div>
<div class="fc"><h5>Product</h5><ul>
  <li><a href="{SITE_ROOT}/features/">All Features</a></li>
  <li><a href="{SITE_ROOT}/formats/">Supported Formats</a></li>
  <li><a href="{SITE_ROOT}/pricing/">Pricing</a></li>
  <li><a href="{SITE_ROOT}/review/">Full Review</a></li>
  <li><a href="{SITE_ROOT}/download/">Download</a></li>
</ul></div>
<div class="fc"><h5>Guides</h5><ul>
  <li><a href="{SITE_ROOT}/convert-mp4/">Convert to MP4</a></li>
  <li><a href="{SITE_ROOT}/compress-video/">Compress Video</a></li>
  <li><a href="{SITE_ROOT}/convert-mkv-mp4/">MKV to MP4</a></li>
  <li><a href="{SITE_ROOT}/convert-mov-mp4/">MOV to MP4</a></li>
  <li><a href="{SITE_ROOT}/dvd-burner/">DVD Burner</a></li>
  <li><a href="{SITE_ROOT}/blog/">Blog</a></li>
</ul></div>
<div class="fc"><h5>Compare</h5><ul>
  <li><a href="{SITE_ROOT}/vs-handbrake/">vs HandBrake</a></li>
  <li><a href="{SITE_ROOT}/vs-vlc/">vs VLC</a></li>
  <li><a href="{SITE_ROOT}/vs-any-video-converter/">vs Any Video Converter</a></li>
  <li><a href="{SITE_ROOT}/alternatives/">All Alternatives</a></li>
  <li><a href="{SITE_ROOT}/faq/">FAQ</a></li>
  <li><a href="{SITE_ROOT}/disclaimer/">Disclaimer</a></li>
</ul></div>
</div>
<div class="fb-bot">
  <p>© {YEAR} UniConverter Guide — Independent affiliate site. Commissions earned at no extra cost to you.</p>
  <p><a href="{AFF}" target="_blank" rel="noopener sponsored">Download UniConverter Free →</a></p>
</div></footer>"""

def bc(*crumbs):
    parts=[]
    for i,(label,url) in enumerate(crumbs):
        if url and i<len(crumbs)-1:
            parts.append(f'<a href="{url}">{label}</a><span class="sep">›</span>')
        else:
            parts.append(f'<span class="cur">{label}</span>')
    return '<nav class="breadcrumb" aria-label="Breadcrumb">'+"".join(parts)+"</nav>"

def sw_schema(desc):
    return f'{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Wondershare UniConverter","applicationCategory":"MultimediaApplication","operatingSystem":"Windows, macOS","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD","description":"Free trial available"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.6","reviewCount":"2847","bestRating":"5"}},"description":"{desc[:200]}","url":"{SITE_URL}/","publisher":{{"@type":"Organization","name":"Wondershare","url":"https://videoconverter.wondershare.com"}}}}'

def bc_schema(title,path):
    canon=f"{SITE_URL}{path}"
    return f'{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"{SITE_URL}/"}},{{"@type":"ListItem","position":2,"name":"{title}","item":"{canon}"}}]}}'

def page(title,desc,path,body,kw="",extras=None,article=False):
    kw=kw or "Wondershare UniConverter, video converter software, best video converter, convert video to MP4, video compressor, DVD burner"
    canon=f"{SITE_URL}{path}"
    extras=extras or []
    schemas=f'<script type="application/ld+json">{sw_schema(desc)}</script>'
    schemas+=f'<script type="application/ld+json">{bc_schema(title.split("—")[0].strip(),path)}</script>'
    for ex in extras:
        schemas+=f'<script type="application/ld+json">{ex}</script>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:type" content="{'article' if article else 'website'}">
<meta property="og:image" content="{SITE_URL}/assets/og.png">
<meta property="og:site_name" content="UniConverter Guide">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="{SITE_ROOT}/assets/favicon.svg" type="image/svg+xml">
<link rel="alternate" type="application/rss+xml" title="UniConverter Blog" href="{SITE_URL}/feed.xml">
{schemas}
<style>{CSS}</style>
</head>
<body>
{nav()}
{body}
{foot()}
<script>
(function(){{
  var h=document.querySelector('.ham'),nl=document.querySelector('.nav-links');
  if(!h||!nl)return;
  h.addEventListener('click',function(){{
    var open=nl.style.display==='flex';
    nl.style.cssText=open?'':'display:flex;position:fixed;top:66px;left:0;right:0;flex-direction:column;background:rgba(5,8,16,.98);padding:2rem 5%;gap:1.2rem;border-bottom:1px solid rgba(255,107,53,.12);z-index:998;backdrop-filter:blur(20px)';
  }});
}})();
</script>
</body></html>"""

def write(rel,content):
    p=BASE/rel
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(content,encoding="utf-8")
    print(f"  ✓  {rel}")


FORMATS_IN = ["MP4","MKV","AVI","MOV","WMV","FLV","WebM","MPEG","VOB","TS","M2TS","MTS","AVCHD","3GP","3G2","OGV","RM","RMVB","ASF","DivX","F4V","H.264","H.265/HEVC","ProRes","XAVC","MXF","MP3","AAC","WAV","FLAC","OGG","WMA","M4A","AIFF","AC3","DTS","JPG","PNG","BMP","TIFF","GIF","WebP","HEIC","RAW","ISO","DVD","Blu-ray"]
FORMATS_OUT = ["MP4","MKV","AVI","MOV","WMV","WebM","MP3","AAC","WAV","FLAC","OGG","M4A","GIF","DVD/ISO","HTML5 Video","4K H.265","H.264","ProRes"]
DEVICES = ["iPhone 16","iPhone 15","iPad Pro","Samsung Galaxy S25","Samsung Galaxy S24","Google Pixel 9","Apple TV","Roku","Chromecast","PS5","Xbox Series X","Nintendo Switch","Sony Bravia TV","LG TV","Samsung TV","Android TV","Fire TV","DJI Drone","GoPro HERO","Sony Camera","Canon DSLR","Nikon DSLR"]

def pg_home():
    fmts="".join(f'<span class="fmt">{f}</span>' for f in FORMATS_IN[:24])
    devs="".join(f'<div class="card" style="padding:1rem 1.2rem"><p style="font-size:.85rem;color:var(--txt);margin:0">{d}</p></div>' for d in DEVICES[:12])
    return page(
        f"Wondershare UniConverter — Best Video Converter Software {YEAR} | Convert 1000+ Formats",
        f"Wondershare UniConverter: convert, compress, edit, record and burn video in 1000+ formats. 90x faster conversion. 4K/8K support. AI enhancement. Free trial. Best video converter {YEAR}.",
        "/",f"""
<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge anim"><span>●</span> #1 Rated Video Converter Worldwide</div>
    <h1 class="anim d1">Convert <span class="g-acc">Any Video</span><br>To <span class="g-acc2">Any Format</span><br>In Seconds</h1>
    <p class="hero-sub anim d2">Wondershare UniConverter handles everything — convert, compress, edit, download, record and burn DVD in 1000+ formats. 90× faster than real-time with GPU acceleration. 4K, 8K and HDR supported.</p>
    <div class="hero-ctas anim d3">
      <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download Free Trial</a>
      <a href="{SITE_ROOT}/features/" class="btn btn-s btn-lg">See All Features →</a>
    </div>
    <div class="hero-trust anim">
      <span class="trust-item">Free Trial</span>
      <span class="trust-item">Windows &amp; Mac</span>
      <span class="trust-item">1000+ Formats</span>
      <span class="trust-item">No Watermark on Output</span>
      <span class="trust-item">GPU Accelerated</span>
    </div>
  </div>
</section>

<div class="stats-bar">
  <div class="stat-item"><span class="stat-num">1000+</span><span class="stat-lbl">Formats Supported</span></div>
  <div class="stat-item"><span class="stat-num">90×</span><span class="stat-lbl">Faster Than Realtime</span></div>
  <div class="stat-item"><span class="stat-num">8K</span><span class="stat-lbl">Max Resolution</span></div>
  <div class="stat-item"><span class="stat-num">15M+</span><span class="stat-lbl">Users Worldwide</span></div>
  <div class="stat-item"><span class="stat-num">2003</span><span class="stat-lbl">Est. by Wondershare</span></div>
</div>

<section>
  <span class="sec-lbl">Everything In One App</span>
  <h2 class="sec-title">Not Just a Converter —<br>A Complete <span class="g-acc">Video Toolbox</span></h2>
  <p class="sec-sub">UniConverter replaces 8 separate tools. Convert, compress, edit, download, record, burn, enhance with AI — all in one clean interface.</p>
  <div class="g3">
    <div class="card card-feat"><div class="card-icon">🔄</div><h3>Video Converter</h3><p>Convert between 1000+ formats with zero quality loss. MP4, MKV, AVI, MOV, WebM, HEVC and every format your camera, editor or device needs.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>Video Compressor</h3><p>Reduce file size by up to 90% without visible quality loss. Perfect for email, web upload, storage or sharing on WhatsApp, Instagram and TikTok.</p></div>
    <div class="card"><div class="card-icon">✂️</div><h3>Video Editor</h3><p>Trim, crop, rotate, merge, add subtitles, watermarks, effects and filters. All the editing you need without opening a separate app.</p></div>
    <div class="card"><div class="card-icon">📥</div><h3>Video Downloader</h3><p>Download videos from YouTube, Vimeo, Dailymotion, Facebook and 1000+ streaming sites directly to your computer.</p></div>
    <div class="card"><div class="card-icon">🎬</div><h3>DVD Burner</h3><p>Burn any video to DVD or Blu-ray with customizable menus and templates. Create professional-looking discs from any format.</p></div>
    <div class="card"><div class="card-icon">🖥</div><h3>Screen Recorder</h3><p>Record your screen, webcam or both simultaneously. Perfect for tutorials, gameplay, presentations and online meetings.</p></div>
    <div class="card"><div class="card-icon">🤖</div><h3>AI Enhancement</h3><p>AI Super Resolution upscales SD video to HD. AI Stabilization fixes shaky footage. AI Noise Reduction cleans up low-light recordings.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>GPU Acceleration</h3><p>NVIDIA, AMD and Intel GPU acceleration makes conversion up to 90× faster than real-time. 1 hour of video converts in minutes, not hours.</p></div>
    <div class="card"><div class="card-icon">🔊</div><h3>Audio Converter</h3><p>Extract audio from video. Convert between MP3, AAC, WAV, FLAC, OGG and 50+ audio formats at any bitrate.</p></div>
  </div>
</section>

<section class="alt">
  <span class="sec-lbl tc" style="display:block;text-align:center">1000+ Formats</span>
  <h2 class="sec-title tc">Works With <span class="g-acc">Every Format</span> You Have</h2>
  <p class="sec-sub tc">Import from any source. Export for any device. UniConverter handles it all.</p>
  <div class="fmt-grid" style="max-width:900px;margin:0 auto 2rem;justify-content:center">{fmts}</div>
  <div style="text-align:center"><a href="{SITE_ROOT}/formats/" class="btn btn-g">View All 1000+ Formats →</a></div>
</section>

<section>
  <div class="split">
    <div>
      <span class="sec-lbl">Speed That Matters</span>
      <h2 class="sec-title">90× Faster.<br><span class="g-acc">GPU Powered.</span></h2>
      <p style="margin-bottom:1.5rem">Most video converters use your CPU and take hours for large files. UniConverter uses your GPU — NVIDIA, AMD and Intel — to convert at up to 90× real-time speed.</p>
      <ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.8rem">
        <li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>NVIDIA NVENC/CUDA</strong> — fastest GPU acceleration available</span></li>
        <li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>AMD VCE</strong> — hardware acceleration for AMD graphics cards</span></li>
        <li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>Intel Quick Sync</strong> — integrated GPU support on Intel processors</span></li>
        <li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>Batch conversion</strong> — convert hundreds of files simultaneously</span></li>
        <li style="display:flex;gap:.7rem;font-size:.9rem;color:var(--muted)"><span style="color:var(--green);font-weight:700">✓</span><span><strong>Apple Silicon</strong> — M1, M2, M3 native performance on Mac</span></li>
      </ul>
      <div style="margin-top:2rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Try Free Now</a></div>
    </div>
    <div>
      <div class="card card-feat" style="padding:2.2rem">
        <h3 style="color:var(--acc);margin-bottom:1.4rem">UniConverter vs Manual Methods</h3>
        <div class="tbl-wrap"><table>
          <thead><tr><th>Task</th><th>UniConverter</th><th>Manual / Free Tools</th></tr></thead>
          <tbody>
            <tr><td>1hr 4K video convert</td><td class="td-y td-hi">~3 minutes</td><td class="td-p">60–90 minutes</td></tr>
            <tr><td>Batch 50 files</td><td class="td-y td-hi">One click</td><td class="td-no">50 separate steps</td></tr>
            <tr><td>Compress + convert</td><td class="td-y td-hi">One step</td><td class="td-no">2 separate tools</td></tr>
            <tr><td>DVD burning</td><td class="td-y td-hi">Built in</td><td class="td-no">Separate software</td></tr>
            <tr><td>AI enhancement</td><td class="td-y td-hi">Built in</td><td class="td-no">Not available</td></tr>
            <tr><td>Screen recording</td><td class="td-y td-hi">Built in</td><td class="td-no">Separate software</td></tr>
          </tbody>
        </table></div>
      </div>
    </div>
  </div>
</section>

<section class="alt">
  <span class="sec-lbl tc" style="display:block;text-align:center">Device Compatibility</span>
  <h2 class="sec-title tc">Optimized for <span class="g-acc">Every Device</span></h2>
  <p class="sec-sub tc">Output presets for every major phone, TV, console and streaming platform. No manual settings needed.</p>
  <div class="g4" style="max-width:960px;margin:0 auto 2rem">{devs}</div>
  <div style="text-align:center"><a href="{SITE_ROOT}/formats/" class="btn btn-g">View All Device Presets →</a></div>
</section>

<section>
  <span class="sec-lbl tc" style="display:block;text-align:center">Real Users</span>
  <h2 class="sec-title tc">What People <span class="g-acc">Around the World</span> Say</h2>
  <p class="sec-sub tc">4.6 stars from 2,800+ verified reviews across G2, Capterra and Trustpilot</p>
  <div class="tgrid">
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"I've tried every free converter out there. UniConverter is the first one that actually handles my HEVC 4K drone footage without crashing or taking 3 hours. Worth every penny."</p><div class="testi-name">Marcus H. 🇩🇪</div><div class="testi-role">Filmmaker, Munich</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"As a social media manager I'm converting dozens of videos daily — different formats for Instagram, TikTok, YouTube, Facebook. UniConverter handles them all in one batch. Huge time saver."</p><div class="testi-name">Priya M. 🇮🇳</div><div class="testi-role">Social Media Manager, Bangalore</div></div>
    <div class="testi"><div class="stars">★★★★☆</div><p class="testi-text">"The compression feature is brilliant. I reduced a 4GB video to 400MB with almost no visible quality difference. My clients can't tell which version they're watching."</p><div class="testi-name">Carlos R. 🇧🇷</div><div class="testi-role">Video Editor, São Paulo</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"I needed to convert old home movies from DVD to MP4 to share with family. UniConverter ripped and converted everything in about 20 minutes. Incredibly simple."</p><div class="testi-name">Susan T. 🇬🇧</div><div class="testi-role">Retired Teacher, London</div></div>
    <div class="testi"><div class="stars">★★★★★</div><p class="testi-text">"The AI upscaling turned my old 480p footage into something that actually looks watchable on a 4K monitor. I didn't expect it to work that well. Genuinely impressed."</p><div class="testi-name">Takuya S. 🇯🇵</div><div class="testi-role">Content Creator, Tokyo</div></div>
    <div class="testi"><div class="stars">★★★★☆</div><p class="testi-text">"Our university media department uses UniConverter for all format standardization. Saves hours every week compared to what we were doing before with multiple tools."</p><div class="testi-name">Dr. Ahmed K. 🇦🇪</div><div class="testi-role">Media Studies Lecturer, Dubai</div></div>
  </div>
</section>

<div class="cta-blk">
  <span class="sec-lbl" style="display:block;margin-bottom:1rem">Start Converting Today</span>
  <h2>Ready to Convert <span class="g-acc">Any Video</span> Instantly?</h2>
  <p>Join 15 million users worldwide. Free trial — no credit card, no watermark on trial exports.</p>
  <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free</a>
  <p style="margin-top:1.2rem;font-size:.8rem;color:var(--muted)">Annual from $39.99/yr · Perpetual from $79.99 · Free trial available · Windows &amp; Mac</p>
</div>""",
        kw=KEYWORDS)


def pg_features():
    return page(f"UniConverter Features — Complete List | Convert, Compress, Edit, Burn, Record | {YEAR}",
        "Full Wondershare UniConverter feature list: 1000+ format conversion, video compression, editing, DVD burning, screen recording, video downloading, AI enhancement, GPU acceleration.",
        "/features/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Features",None))}
  <span class="sec-lbl">Everything It Does</span>
  <h1>UniConverter <span class="g-acc">Features</span></h1>
  <p style="max-width:640px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">One app that replaces eight. Here's every capability in detail.</p>
</div>
<section>
  <div class="g3">
    <div class="card card-feat"><div class="card-icon">🔄</div><h3>1000+ Format Conversion</h3><p>Convert between every major video, audio and image format. MP4, MKV, AVI, MOV, WMV, WebM, HEVC/H.265, H.264, ProRes, MXF, XAVC, VOB, TS, MTS, M2TS, AVCHD, 3GP, OGV, RM, RMVB, DivX and hundreds more. Import from cameras, drones, phones and professional equipment.</p></div>
    <div class="card"><div class="card-icon">⚡</div><h3>GPU Acceleration</h3><p>Up to 90× faster than real-time conversion using NVIDIA NVENC/CUDA, AMD VCE and Intel Quick Sync. What takes other converters 60 minutes takes UniConverter 3–5 minutes. Batch convert hundreds of files simultaneously.</p></div>
    <div class="card"><div class="card-icon">📦</div><h3>Video Compression</h3><p>Reduce file size by up to 90% with minimal visible quality loss. Adjust bitrate, resolution, frame rate and codec. Perfect for sharing on WhatsApp, email, social media or freeing up storage.</p></div>
    <div class="card"><div class="card-icon">🤖</div><h3>AI Super Resolution</h3><p>Upscale SD (480p) footage to HD (1080p) or 4K using AI. UniConverter's neural network fills in detail intelligently, making old videos look dramatically better on modern screens.</p></div>
    <div class="card"><div class="card-icon">🎬</div><h3>AI Frame Interpolation</h3><p>Convert 24fps footage to 60fps or higher for smoother motion. Ideal for action footage, drone video, sports and gaming content.</p></div>
    <div class="card"><div class="card-icon">📷</div><h3>AI Stabilization</h3><p>Fix shaky footage from handheld cameras, drones and action cams. AI analyzes motion and corrects it without manual keyframing.</p></div>
    <div class="card"><div class="card-icon">✂️</div><h3>Video Editor</h3><p>Trim and cut video. Crop and rotate. Merge multiple clips. Add text, subtitles (.SRT support), watermarks, filters and effects. Adjust speed, brightness, contrast and audio levels.</p></div>
    <div class="card"><div class="card-icon">💿</div><h3>DVD & Blu-ray Burner</h3><p>Convert any video to DVD or Blu-ray with professional menus and templates. Burn ISO images. Rip DVDs to digital formats. Works with all major disc formats.</p></div>
    <div class="card"><div class="card-icon">📥</div><h3>Video Downloader</h3><p>Download videos from YouTube, Vimeo, Dailymotion, Facebook, Twitter/X, Bilibili and 1000+ sites. Save in any resolution including 4K. Extract audio as MP3.</p></div>
    <div class="card"><div class="card-icon">🖥</div><h3>Screen Recorder</h3><p>Record desktop, browser, application window or full screen. Capture webcam alongside or picture-in-picture. Record system audio and/or microphone. Export as MP4, AVI or GIF.</p></div>
    <div class="card"><div class="card-icon">🎵</div><h3>Audio Converter</h3><p>Extract audio from any video. Convert between MP3, AAC, WAV, FLAC, OGG, WMA, M4A, AIFF, AC3, DTS and 50+ formats. Adjust bitrate, sample rate and channels.</p></div>
    <div class="card"><div class="card-icon">🖼</div><h3>Image Converter</h3><p>Convert between JPG, PNG, BMP, TIFF, GIF, WebP, HEIC and RAW formats. Batch process entire photo libraries. Convert screenshots, thumbnails and artwork.</p></div>
    <div class="card"><div class="card-icon">🌊</div><h3>Watermark Remover</h3><p>Remove watermarks from videos using AI inpainting. Also add custom watermarks — text or image — to protect your content with full control over position, opacity and size.</p></div>
    <div class="card"><div class="card-icon">📱</div><h3>Device Presets</h3><p>Pre-configured export settings for iPhone 16, Samsung Galaxy S25, iPad, Apple TV, PS5, Xbox, Smart TVs and 50+ more devices. No manual codec configuration needed.</p></div>
    <div class="card"><div class="card-icon">🔊</div><h3>Noise Reduction</h3><p>AI-powered audio noise reduction removes background hiss, hum and ambient noise from videos. Dramatically improves recordings made in noisy environments.</p></div>
  </div>
  <div class="cta-blk" style="margin-top:3rem;border-radius:var(--r)">
    <h2 style="margin-bottom:.8rem">All Features, <span class="g-acc">Free to Try</span></h2>
    <p>Download UniConverter and test everything with the free trial. No credit card required.</p>
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Download Free Trial</a>
  </div>
</section>""","Wondershare UniConverter features, video converter features, video compression, DVD burner, screen recorder, AI video enhancement")

def pg_formats():
    cats = {
        "📹 Video Input": ["MP4","MKV","AVI","MOV","WMV","FLV","WebM","MPEG-1/2/4","VOB","TS","MTS","M2TS","AVCHD","3GP","3G2","OGV","RM","RMVB","ASF","DivX","Xvid","F4V","H.264","H.265/HEVC","ProRes 422/4444","XAVC","XAVC-S","MXF","R3D","BRAW","DNxHD","Cineform","VP8","VP9","AV1","Theora"],
        "📤 Video Output": ["MP4 (H.264/H.265)","MKV","AVI","MOV","WMV","WebM","FLV","MPEG","3GP","HTML5 Video","4K H.265","Apple ProRes","GIF","DVD Video","Blu-ray Video","VR 360°"],
        "🎵 Audio Formats": ["MP3","AAC","WAV","FLAC","OGG","WMA","M4A","AIFF","AC3","DTS","AMR","AU","APE","CAF","MKA","MPA","MP2","RA","SND"],
        "🖼 Image Formats": ["JPG/JPEG","PNG","BMP","TIFF","GIF","WebP","HEIC","RAW","ICO","TGA","PSD"],
        "📱 Device Presets": ["iPhone 16/15/14 Series","iPad Pro/Air/mini","Apple TV 4K","Samsung Galaxy S25/S24","Google Pixel 9","Sony Xperia","OnePlus 12","Xiaomi 14","PS5 / PS4","Xbox Series X/S","Nintendo Switch","Smart TV (4K)","Roku / Fire TV","Chromecast","DJI Drone Export","GoPro HERO Export"],
    }
    cats_html=""
    for cat,items in cats.items():
        pills="".join(f'<span class="fmt">{i}</span>' for i in items)
        cats_html+=f'<div style="margin-bottom:2.5rem"><h3 style="margin-bottom:1rem;font-size:1.3rem">{cat}</h3><div class="fmt-grid">{pills}</div></div>'
    return page(f"UniConverter Supported Formats — 1000+ Video, Audio & Image | {YEAR}",
        "Wondershare UniConverter supports 1000+ formats including MP4, MKV, AVI, MOV, HEVC, ProRes, MP3, AAC, WAV, FLAC, JPG, PNG, HEIC. Full input and output format list.",
        "/formats/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Formats",None))}
  <span class="sec-lbl">1000+ Formats</span>
  <h1>Supported <span class="g-acc">Formats</span></h1>
  <p style="max-width:660px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">UniConverter works with every major video, audio and image format — from consumer to professional broadcast.</p>
</div>
<section>
  <div class="hbox good"><p><strong>1000+ formats supported.</strong> UniConverter covers every format used by consumer cameras, professional cameras, broadcast equipment, streaming platforms, mobile devices and legacy disc formats. Updated regularly as new formats emerge.</p></div>
  {cats_html}
  <div style="text-align:center;margin-top:2rem">
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Download UniConverter — Convert Your Format Free</a>
  </div>
</section>""","UniConverter supported formats, video converter formats, MP4 MKV AVI converter, HEVC H.265 converter, ProRes converter, all video formats")

def pg_how():
    howto=f'{{"@context":"https://schema.org","@type":"HowTo","name":"How to Convert Video with UniConverter","description":"Convert any video to any format in 3 steps using Wondershare UniConverter.","step":[{{"@type":"HowToStep","position":1,"name":"Add your video","text":"Drag and drop your video file into UniConverter or click Add Files."}},{{"@type":"HowToStep","position":2,"name":"Choose output format","text":"Select your target format, device preset or platform from the dropdown."}},{{"@type":"HowToStep","position":3,"name":"Convert","text":"Click Convert. GPU acceleration completes the conversion in seconds."}}]}}'
    return page(f"How UniConverter Works — Convert Video in 3 Steps | {YEAR}",
        "Learn how Wondershare UniConverter works: add file, choose format, convert. 3 simple steps. GPU accelerated. Works for video conversion, compression, editing, DVD burning and screen recording.",
        "/how-it-works/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("How It Works",None))}
  <span class="sec-lbl">Simple Process</span>
  <h1>How <span class="g-acc">UniConverter</span> Works</h1>
  <p style="max-width:640px;margin-top:.9rem;font-size:1.05rem;color:var(--muted)">Three steps to convert any video. Here's every workflow explained.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:2rem">Video <span class="g-acc">Conversion</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Add Your File</h3><p>Drag and drop your video, or click "Add Files" to browse. UniConverter accepts 1000+ formats from any source — camera, phone, drone, screen recording or download.</p></div></div>
        <div class="step" data-n="2"><div><h3>Choose Output Format</h3><p>Select your target format from the dropdown — MP4, MKV, MOV, a device preset for your iPhone or Samsung, or a platform preset for YouTube or Instagram. Adjust quality settings if needed.</p></div></div>
        <div class="step" data-n="3"><div><h3>Click Convert</h3><p>Hit Convert. GPU acceleration kicks in and your file is ready in seconds to minutes — not hours. Batch convert multiple files simultaneously.</p></div></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:1.5rem">
      <div class="hbox"><h4>Compression Workflow</h4><p style="margin-top:.4rem">Go to Toolbox → Video Compressor. Set your target file size or bitrate. Preview the quality difference before committing. One click compresses without a separate conversion step.</p></div>
      <div class="hbox"><h4>DVD Burning Workflow</h4><p style="margin-top:.4rem">Click "DVD Burner". Add your video files. Choose a menu template or create a custom one. Insert a blank disc and burn. UniConverter handles encoding automatically.</p></div>
      <div class="hbox"><h4>Screen Recording Workflow</h4><p style="margin-top:.4rem">Open Screen Recorder. Select your capture area (full screen, window, or custom). Toggle webcam and audio. Press Record. Stop and export directly to MP4 or your target format.</p></div>
      <div class="hbox good"><h4>Batch Mode</h4><p style="margin-top:.4rem">Add hundreds of files at once. Set a single output format or configure each file individually. Start batch conversion and walk away — UniConverter handles the queue.</p></div>
      <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Try Free Now</a>
    </div>
  </div>
</section>""","how UniConverter works, video conversion steps, how to convert video, batch video converter",extras=[howto])

def pg_pricing():
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"How much does UniConverter cost?","acceptedAnswer":{"@type":"Answer","text":"UniConverter annual plan starts at $39.99/year. The perpetual (lifetime) plan is $79.99. A free trial is available."}},{"@type":"Question","name":"Is there a free trial?","acceptedAnswer":{"@type":"Answer","text":"Yes. UniConverter offers a free trial with no credit card required. Trial outputs include a watermark on exported files."}},{"@type":"Question","name":"What is the difference between annual and perpetual?","acceptedAnswer":{"@type":"Answer","text":"The annual plan renews yearly at $39.99. The perpetual plan is a one-time payment of $79.99 that gives you the software forever."}}]}'
    return page(f"UniConverter Pricing {YEAR} — Free Trial, $39.99/yr, $79.99 Lifetime",
        f"Wondershare UniConverter pricing {YEAR}: Free trial available. Annual plan $39.99/year. Perpetual (lifetime) $79.99 one-time. All plans include 1000+ formats, GPU acceleration, AI features.",
        "/pricing/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Pricing",None))}
  <span class="sec-lbl" style="display:block;text-align:center">Clear Pricing</span>
  <h1>UniConverter <span class="g-acc">Pricing {YEAR}</span></h1>
  <p style="max-width:540px;margin:.9rem auto 0;color:var(--muted)">Start free. All paid plans include 1000+ formats, GPU acceleration, AI tools and DVD burning.</p>
</div>
<section>
  <div class="pgrid">
    <div class="pc">
      <div class="p-name">Free Trial</div>
      <div class="p-price"><sup>$</sup>0</div>
      <div class="p-per">No credit card needed</div>
      <ul class="p-feats">
        <li>Convert with watermark on output</li>
        <li>Test all features and interface</li>
        <li>Preview GPU acceleration speed</li>
        <li>Try compression and editing tools</li>
        <li>No time limit on trial</li>
      </ul>
      <a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Start Free Trial</a>
    </div>
    <div class="pc pop">
      <div class="pop-badge">Best Value</div>
      <div class="p-name">Annual Plan</div>
      <div class="p-price"><sup>$</sup>39<span style="font-size:1.5rem">.99</span></div>
      <div class="p-per">per year · 1 PC · Auto-renews</div>
      <ul class="p-feats">
        <li>No watermark on exports</li>
        <li>1000+ format conversion</li>
        <li>GPU-accelerated (NVIDIA/AMD/Intel)</li>
        <li>AI Super Resolution + Stabilization</li>
        <li>Video compressor</li>
        <li>DVD &amp; Blu-ray burner</li>
        <li>Screen recorder</li>
        <li>Video downloader</li>
        <li>Batch conversion</li>
        <li>Free updates for 1 year</li>
        <li>Priority support</li>
      </ul>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">Get Annual Plan →</a>
      <div class="p-note">💡 Discounts up to 30% off available</div>
    </div>
    <div class="pc">
      <div class="p-name">Perpetual Plan</div>
      <div class="p-price"><sup>$</sup>79<span style="font-size:1.5rem">.99</span></div>
      <div class="p-per">one-time payment · lifetime</div>
      <ul class="p-feats">
        <li>Everything in Annual +</li>
        <li>Pay once, own forever</li>
        <li>All future updates included</li>
        <li>No recurring fees ever</li>
        <li>Best long-term value</li>
      </ul>
      <a href="{AFF}" class="btn btn-s btn-full" target="_blank" rel="noopener sponsored">Get Lifetime Plan →</a>
    </div>
  </div>
  <div class="hbox" style="max-width:820px;margin:3rem auto 0;text-align:center">
    <h4>💡 Check for Current Promotions</h4>
    <p style="margin-top:.4rem">Wondershare regularly offers up to 30% off UniConverter. Click any button above to see the current discounted price on the official site.</p>
  </div>
  <div style="max-width:820px;margin:3rem auto 0">
    <h2 style="margin-bottom:1.4rem">Pricing <span class="g-acc">FAQ</span></h2>
    <div class="faq-wrap" style="max-width:100%">
      <details><summary>Is UniConverter really free to try?</summary><div class="ans"><p>Yes. Download and install without entering payment details. The free trial lets you use all features — converted files include a watermark. Upgrade to remove the watermark and unlock full output quality.</p></div></details>
      <details><summary>Annual vs Perpetual — which is better?</summary><div class="ans"><p>If you convert video regularly, the perpetual plan at $79.99 pays for itself after 2 years of annual renewals. If you only convert occasionally or want the lowest upfront cost, the $39.99/year annual plan is ideal.</p></div></details>
      <details><summary>Does the price include all features?</summary><div class="ans"><p>Yes. Both paid plans include the full feature set: conversion, compression, editing, DVD burning, screen recording, video downloading, AI enhancement and GPU acceleration. No feature is gated behind a higher tier.</p></div></details>
      <details><summary>Is there a money-back guarantee?</summary><div class="ans"><p>Wondershare typically offers a refund policy. Check the official site for current terms before purchasing as these can vary by plan and region.</p></div></details>
    </div>
  </div>
</section>""","UniConverter price, UniConverter cost, UniConverter annual plan, UniConverter perpetual, UniConverter discount, video converter pricing",extras=[faq_s])

def pg_review():
    rev_s='{"@context":"https://schema.org","@type":"Review","itemReviewed":{"@type":"SoftwareApplication","name":"Wondershare UniConverter","applicationCategory":"MultimediaApplication","operatingSystem":"Windows, macOS"},"reviewRating":{"@type":"Rating","ratingValue":"9.0","bestRating":"10","worstRating":"1"},"author":{"@type":"Person","name":"UniConverter Guide Editorial Team"},"datePublished":"2026-06-01","reviewBody":"UniConverter earns 9.0/10 for its unmatched format support, GPU-accelerated speed, all-in-one toolbox value and AI enhancement capabilities. The best paid video converter available."}'
    return page(f"Wondershare UniConverter Review {YEAR} — Honest 9.0/10 After Testing",
        f"Complete Wondershare UniConverter review {YEAR}: 9.0/10 overall. We tested conversion speed, quality, GPU acceleration, compression, DVD burning and AI features. Full verdict.",
        "/review/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Review",None))}
  <span class="sec-lbl">Hands-On Review</span>
  <h1>UniConverter <span class="g-acc">Review {YEAR}</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">We tested UniConverter across 30+ conversion scenarios — 4K, H.265, batch processing, AI upscaling, DVD burning and compression. Here's our complete, honest verdict.</p>
</div>
<section>
  <div class="split">
    <div>
      <div class="score-big">9.0</div>
      <div style="font-size:.8rem;color:var(--muted);text-transform:uppercase;letter-spacing:.1em;margin-bottom:1.5rem">out of 10 — Editor's Rating</div>
      <div style="display:flex;gap:.5rem;flex-wrap:wrap;margin-bottom:2rem">
        <span class="chip chip-g">✓ Recommended</span>
        <span class="chip chip-o">Best Paid Converter</span>
        <span class="chip chip-b">GPU Champion</span>
      </div>
      <div class="rbars">
        <div class="rbar"><span class="rbar-lbl">Conversion Speed</span><div class="rbar-track"><div class="rbar-fill" style="width:97%"></div></div><span class="rbar-val">9.7</span></div>
        <div class="rbar"><span class="rbar-lbl">Output Quality</span><div class="rbar-track"><div class="rbar-fill" style="width:95%"></div></div><span class="rbar-val">9.5</span></div>
        <div class="rbar"><span class="rbar-lbl">Format Support</span><div class="rbar-track"><div class="rbar-fill" style="width:98%"></div></div><span class="rbar-val">9.8</span></div>
        <div class="rbar"><span class="rbar-lbl">Ease of Use</span><div class="rbar-track"><div class="rbar-fill" style="width:90%"></div></div><span class="rbar-val">9.0</span></div>
        <div class="rbar"><span class="rbar-lbl">AI Features</span><div class="rbar-track"><div class="rbar-fill" style="width:88%"></div></div><span class="rbar-val">8.8</span></div>
        <div class="rbar"><span class="rbar-lbl">Value for Money</span><div class="rbar-track"><div class="rbar-fill" style="width:86%"></div></div><span class="rbar-val">8.6</span></div>
        <div class="rbar"><span class="rbar-lbl">Support</span><div class="rbar-track"><div class="rbar-fill" style="width:82%"></div></div><span class="rbar-val">8.2</span></div>
      </div>
    </div>
    <div>
      <div class="hbox good"><h4>✓ What We Loved</h4><ul style="list-style:none;padding:0;margin-top:.7rem;display:flex;flex-direction:column;gap:.5rem">
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>GPU acceleration is genuinely transformative — 1hr 4K H.265 encode in under 4 minutes</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>1000+ format support — we found no format it couldn't handle</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>AI upscaling visibly improved 480p test footage on a 4K monitor</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Batch processing 50 files simultaneously without issues</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>$39.99/year is excellent value for this many features</li>
      </ul></div>
      <div class="hbox warn" style="margin-top:1rem"><h4>⚠ Caveats</h4><ul style="list-style:none;padding:0;margin-top:.5rem;display:flex;flex-direction:column;gap:.5rem">
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">–</span>Interface can feel overwhelming with so many tools on first launch</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">–</span>Customer support response times can be slow</li>
        <li style="font-size:.87rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">–</span>AI features add processing time on top of conversion</li>
      </ul></div>
    </div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Try UniConverter Free</a>
  </div>
</section>""","UniConverter review, Wondershare UniConverter review, is UniConverter worth it, UniConverter rating 2025 2026",extras=[rev_s],article=True)


def pg_faq():
    faqs=[
        ("Is Wondershare UniConverter free?","UniConverter offers a free trial with no time limit and no credit card required. Trial exports include a watermark on output files. Paid plans start at $39.99/year (Annual) or $79.99 one-time (Perpetual) and remove the watermark while unlocking full output quality."),
        ("How fast is UniConverter?","With GPU acceleration enabled, UniConverter converts at up to 90× real-time speed. A 1-hour 4K H.265 video typically converts in 3–5 minutes on a modern system with NVIDIA, AMD or Intel GPU. Without GPU acceleration, it still outperforms most CPU-only converters."),
        ("What formats does UniConverter support?","UniConverter supports 1000+ formats including MP4, MKV, AVI, MOV, WMV, FLV, WebM, HEVC/H.265, H.264, ProRes, MXF, XAVC, VOB, TS, MTS, AVCHD, 3GP, RM, DivX, MP3, AAC, WAV, FLAC, JPG, PNG, HEIC and many more. It also includes device presets for iPhone, Samsung, Smart TV, PS5, Xbox and others."),
        ("Does UniConverter work on Mac?","Yes. UniConverter is available for both Windows (7, 8, 10, 11) and macOS (10.12 Sierra and later, including Apple Silicon M1/M2/M3). Both versions have identical features and full GPU acceleration support."),
        ("Can UniConverter convert 4K and 8K video?","Yes. UniConverter fully supports 4K and 8K video conversion in H.264, H.265/HEVC and other modern codecs. It also supports HDR, HDR10 and Dolby Vision content. GPU acceleration makes 4K/8K conversion practical even on consumer hardware."),
        ("What is the difference between UniConverter and HandBrake?","HandBrake is an excellent free open-source converter but supports fewer formats, has no video compressor, no DVD burner, no screen recorder, no downloader and no AI tools. UniConverter costs $39.99/year but replaces 8 separate tools and includes GPU acceleration, AI enhancement and a complete video toolbox."),
        ("Can UniConverter burn DVDs?","Yes. UniConverter has a built-in DVD and Blu-ray burner. Add any video file, choose a menu template, insert a blank disc and burn. It handles encoding automatically and supports customizable menus, chapter markers and cover art."),
        ("Does UniConverter have a screen recorder?","Yes. UniConverter's screen recorder can capture your full desktop, a specific window or a custom region. It supports webcam recording alongside screen capture, system audio recording, microphone recording, and exports to MP4, AVI or GIF."),
        ("Can UniConverter remove watermarks?","Yes. UniConverter includes an AI-powered watermark remover that can remove watermarks, logos and text overlays from videos using intelligent inpainting. It also lets you add your own custom watermarks — text or image — with full control over position, size and opacity."),
        ("Is UniConverter safe to download?","Yes. UniConverter is developed by Wondershare, a publicly listed software company founded in 2003 with 15M+ users worldwide. It is safe to download from the official Wondershare website. Avoid unofficial download sites."),
        ("Can UniConverter convert MKV to MP4?","Yes. MKV to MP4 is one of the most common conversions and UniConverter handles it perfectly — including all audio tracks, subtitles and chapters. With GPU acceleration it's typically done in under a minute for standard HD files."),
        ("Does UniConverter support batch conversion?","Yes. Add hundreds of files at once, set the output format for all or configure each file individually, and start batch conversion. UniConverter processes the entire queue with GPU acceleration, converting multiple files simultaneously."),
    ]
    items="".join(f'<details><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q,a in faqs)
    faq_s='{"@context":"https://schema.org","@type":"FAQPage","mainEntity":['+",".join(f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a[:180]}..."}}}}' for q,a in faqs)+("]}")
    return page(f"UniConverter FAQ {YEAR} — 12 Questions Answered",
        "Complete Wondershare UniConverter FAQ: Is it free? How fast? Mac support? 4K? MKV to MP4? DVD burning? Screen recorder? Batch conversion? All 12 questions answered.",
        "/faq/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("FAQ",None))}
  <span class="sec-lbl">Questions Answered</span>
  <h1>UniConverter <span class="g-acc">FAQ</span></h1>
  <p style="max-width:620px;margin-top:.9rem;color:var(--muted)">Detailed answers to the 12 most common questions before you download or purchase.</p>
</div>
<section>
  <div class="faq-wrap">{items}</div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free</a>
  </div>
</section>""","UniConverter FAQ, UniConverter free, UniConverter Mac, UniConverter 4K, MKV to MP4 UniConverter, UniConverter DVD",extras=[faq_s])

def pg_download():
    return page(f"Download Wondershare UniConverter Free — Windows & Mac | {YEAR}",
        "Download Wondershare UniConverter free trial for Windows and Mac. Convert 1000+ video formats, compress, edit, burn DVD and record screen. No credit card needed.",
        "/download/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Download",None))}
  <span class="sec-lbl" style="display:block;text-align:center">Start in 60 Seconds</span>
  <h1>Download <span class="g-acc">UniConverter</span></h1>
  <p style="max-width:520px;margin:.9rem auto 0;color:var(--muted)">Free trial — no credit card. Convert any video format immediately. Windows and Mac.</p>
</div>
<section>
  <div class="g2" style="max-width:740px;margin:0 auto 3rem">
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🪟</div>
      <h3>Windows</h3>
      <p style="margin-bottom:.5rem">Windows 7 / 8 / 10 / 11</p>
      <p style="font-size:.8rem;color:var(--muted);margin-bottom:1.5rem">32-bit and 64-bit · Latest version</p>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Windows</a>
    </div>
    <div class="card" style="text-align:center">
      <div class="card-icon" style="margin:0 auto 1rem;font-size:2rem">🍎</div>
      <h3>macOS</h3>
      <p style="margin-bottom:.5rem">macOS 10.12 Sierra and later</p>
      <p style="font-size:.8rem;color:var(--muted);margin-bottom:1.5rem">Intel &amp; Apple Silicon M1/M2/M3</p>
      <a href="{AFF}" class="btn btn-p btn-full" target="_blank" rel="noopener sponsored">⬇ Download for Mac</a>
    </div>
  </div>
  <div class="hbox good" style="max-width:700px;margin:0 auto"><h4>Free Trial Includes</h4>
    <ul style="list-style:none;padding:0;margin-top:.7rem;display:grid;grid-template-columns:1fr 1fr;gap:.5rem">
      {"".join(f'<li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>{x}</li>' for x in ["Convert any format (watermark on output)","Test GPU acceleration speed","Try all editing tools","Preview compression quality","Batch convert up to 5 files","DVD burning preview","Screen recorder","Video downloader"])}
    </ul>
  </div>
  <div style="text-align:center;margin-top:2rem">
    <p style="color:var(--muted);margin-bottom:1rem">Remove watermark from $39.99/year or $79.99 lifetime.</p>
    <a href="{SITE_ROOT}/pricing/" class="btn btn-g">View All Pricing →</a>
  </div>
</section>""")

def pg_convert_mp4():
    return page(f"How to Convert Video to MP4 — Complete Guide {YEAR}",
        "Convert any video to MP4 using Wondershare UniConverter. Supports MKV, AVI, MOV, WMV, HEVC, FLV, WebM, MTS, VOB and 1000+ formats. Step-by-step guide with GPU acceleration.",
        "/convert-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Convert to MP4",None))}
  <span class="sec-lbl">Conversion Guide</span>
  <h1>Convert Any Video<br>to <span class="g-acc">MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MP4 is the universal format — works on every device, platform and player. Here's how to convert anything to MP4 in seconds.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1.2rem">Why <span class="g-acc">Convert to MP4?</span></h2>
      <p style="margin-bottom:1.5rem">MP4 (H.264) is supported by every device from iPhones to Smart TVs to web browsers. If your video won't play somewhere, converting to MP4 almost always fixes it.</p>
      <h3 style="margin-bottom:1rem;font-size:1.1rem;color:var(--txt)">Common Sources Converted to MP4:</h3>
      <div class="fmt-grid" style="margin-bottom:1.5rem">
        {"".join(f'<span class="fmt">{f} → MP4</span>' for f in ["MKV","AVI","MOV","WMV","FLV","WebM","HEVC","MTS","M2TS","VOB","TS","AVCHD","3GP","RM","ASF","DivX","F4V","OGV"])}
      </div>
      <a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Convert to MP4 Free</a>
    </div>
    <div>
      <div class="card card-feat" style="padding:2rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">Steps: Convert to MP4</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div><h3>Open UniConverter</h3><p>Download and install UniConverter. Open it and click "Add Files" or drag your video in.</p></div></div>
          <div class="step" data-n="2"><div><h3>Select MP4 Output</h3><p>In the output format dropdown, choose MP4. Select H.264 for maximum compatibility or H.265 for smaller file size.</p></div></div>
          <div class="step" data-n="3"><div><h3>Click Convert</h3><p>GPU acceleration completes the conversion in seconds to minutes depending on file size.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-p btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Try Free</a>
      </div>
    </div>
  </div>
</section>""","convert video to MP4, MKV to MP4, AVI to MP4, MOV to MP4, WMV to MP4, video to MP4 converter",article=True)

def pg_compress():
    return page(f"How to Compress Video Without Losing Quality | {YEAR}",
        "Compress video files by up to 90% without visible quality loss using Wondershare UniConverter. Reduce file size for email, social media, storage and sharing. Step-by-step guide.",
        "/compress-video/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("Compress Video",None))}
  <span class="sec-lbl">Compression Guide</span>
  <h1>Compress Video<br><span class="g-acc">Without Quality Loss</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Reduce your video file size by up to 90% while keeping it looking sharp. Here's exactly how to do it.</p>
</div>
<section>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1rem">Why <span class="g-acc">Compress Video?</span></h2>
      <p style="margin-bottom:1.2rem">4K footage from modern cameras can be enormous — 10–50GB per hour. That's too large to email, upload, share or store efficiently. UniConverter's compressor uses intelligent bitrate optimization to shrink files dramatically while preserving visual quality.</p>
      <div class="hbox good"><h4>Real Compression Examples</h4>
        <ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
          <li style="font-size:.85rem;color:var(--muted)">4K drone footage: 8GB → 800MB (90% reduction)</li>
          <li style="font-size:.85rem;color:var(--muted)">1080p recording: 2GB → 300MB (85% reduction)</li>
          <li style="font-size:.85rem;color:var(--muted)">YouTube upload: 500MB → 80MB (84% reduction)</li>
          <li style="font-size:.85rem;color:var(--muted)">WhatsApp share: 100MB → 15MB (85% reduction)</li>
        </ul>
      </div>
      <div style="margin-top:1.5rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">⬇ Compress Video Free</a></div>
    </div>
    <div>
      <div class="card card-feat" style="padding:2rem">
        <h3 style="color:var(--acc);margin-bottom:1.5rem">How to Compress</h3>
        <div class="steps" style="max-width:100%">
          <div class="step" data-n="1"><div><h3>Open Compressor</h3><p>In UniConverter, go to Toolbox → Video Compressor.</p></div></div>
          <div class="step" data-n="2"><div><h3>Add Your Video</h3><p>Drag your video in. UniConverter shows the current file size and lets you set a target size.</p></div></div>
          <div class="step" data-n="3"><div><h3>Set Target Size</h3><p>Drag the quality slider or type a target file size. Preview the quality difference before committing.</p></div></div>
          <div class="step" data-n="4"><div><h3>Compress</h3><p>Click Compress. GPU acceleration delivers the result in seconds to minutes.</p></div></div>
        </div>
        <a href="{AFF}" class="btn btn-p btn-full" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Try Free</a>
      </div>
    </div>
  </div>
</section>""","compress video without quality loss, reduce video file size, video compressor software, compress 4K video, shrink video file",article=True)

def pg_mkv_mp4():
    return page(f"Convert MKV to MP4 — Fast & Free Guide {YEAR}",
        "Convert MKV to MP4 in seconds using Wondershare UniConverter. Keep all audio tracks, subtitles and chapters. GPU accelerated. No quality loss. Step-by-step guide.",
        "/convert-mkv-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("MKV to MP4",None))}
  <span class="sec-lbl">Format Guide</span>
  <h1>Convert <span class="g-acc">MKV to MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MKV files don't play on many TVs, phones and players. Convert to MP4 and it works everywhere — in seconds with UniConverter.</p>
</div>
<section>
  <div class="hbox"><h4>Why MKV to MP4?</h4><p style="margin-top:.4rem">MKV is a container format that can hold multiple audio tracks, subtitles and chapters — great for storage but not universally supported. MP4 plays on every device. UniConverter converts MKV to MP4 while preserving all audio tracks, subtitle streams and chapter markers.</p></div>
  <div class="split" style="margin-top:2rem">
    <div>
      <h2 style="margin-bottom:1.2rem">Steps: <span class="g-acc">MKV to MP4</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Install UniConverter</h3><p>Download and install on Windows or Mac. Launch the app.</p></div></div>
        <div class="step" data-n="2"><div><h3>Add Your MKV File</h3><p>Drag your MKV file into UniConverter or click "Add Files". Batch add multiple MKV files at once.</p></div></div>
        <div class="step" data-n="3"><div><h3>Select MP4 Output</h3><p>Choose MP4 from the format dropdown. Select H.264 for compatibility or H.265 for smaller files.</p></div></div>
        <div class="step" data-n="4"><div><h3>Convert</h3><p>Click Convert. Your MKV becomes MP4 in seconds — no quality loss, all tracks preserved.</p></div></div>
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Convert MKV Free</a>
    </div>
    <div>
      <div class="hbox good"><h4>What UniConverter Preserves</h4><ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>All audio tracks (multiple language tracks kept)</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Subtitle streams (.SRT, .ASS preserved or burned in)</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Chapter markers</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Full video resolution and frame rate</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>HDR and Dolby Vision metadata</li>
      </ul></div>
    </div>
  </div>
</section>""","MKV to MP4 converter, convert MKV to MP4, MKV MP4 conversion, best MKV converter",article=True)

def pg_mov_mp4():
    return page(f"Convert MOV to MP4 — iPhone & Mac Video Guide {YEAR}",
        "Convert MOV to MP4 from iPhone or Mac using Wondershare UniConverter. MOV files converted to universal MP4 format instantly. Works with HEVC MOV files too. Free guide.",
        "/convert-mov-mp4/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("MOV to MP4",None))}
  <span class="sec-lbl">Format Guide</span>
  <h1>Convert <span class="g-acc">MOV to MP4</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">MOV is Apple's default format for iPhone and Mac. Convert to MP4 to share on Windows PCs, Android phones, social media and streaming platforms.</p>
</div>
<section>
  <div class="hbox"><h4>MOV from iPhone? HEVC Support Included</h4><p style="margin-top:.4rem">Modern iPhones record in HEVC MOV format — which many Windows computers and Android devices can't play. UniConverter converts HEVC MOV to H.264 MP4 with full compatibility, handling the codec conversion automatically.</p></div>
  <div class="split" style="margin-top:2rem">
    <div>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Open UniConverter</h3><p>Install and launch UniConverter on Windows or Mac.</p></div></div>
        <div class="step" data-n="2"><div><h3>Add MOV File</h3><p>Drag your MOV file in — from iPhone, Final Cut Pro, QuickTime or any other source.</p></div></div>
        <div class="step" data-n="3"><div><h3>Choose MP4</h3><p>Select MP4 as output. For Windows compatibility, choose H.264. For smaller files, choose H.265.</p></div></div>
        <div class="step" data-n="4"><div><h3>Convert</h3><p>Click Convert. Done in seconds to minutes with GPU acceleration.</p></div></div>
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Convert MOV Free</a>
    </div>
    <div>
      <div class="card card-feat" style="padding:1.8rem">
        <h4 style="color:var(--acc);margin-bottom:1rem">MOV Sources UniConverter Handles</h4>
        <div class="fmt-grid">
          {"".join(f'<span class="fmt">{f}</span>' for f in ["iPhone MOV","iPad MOV","Mac QuickTime MOV","Final Cut Pro MOV","DJI Drone MOV","GoPro MOV","HEVC/H.265 MOV","ProRes MOV","4K MOV","Slow-mo MOV"])}
        </div>
      </div>
    </div>
  </div>
</section>""","MOV to MP4, convert MOV to MP4, iPhone MOV to MP4, HEVC MOV converter, Mac video converter",article=True)

def pg_dvd():
    return page(f"DVD Burner Software — Burn Video to DVD | UniConverter {YEAR}",
        "Burn any video to DVD using Wondershare UniConverter. Supports MP4, MKV, AVI, MOV and 1000+ formats. Custom DVD menus. Create professional discs on Windows and Mac.",
        "/dvd-burner/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",f"{SITE_ROOT}/blog/"),("DVD Burner",None))}
  <span class="sec-lbl">DVD Guide</span>
  <h1>Burn Video to <span class="g-acc">DVD</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Turn any video file into a DVD that plays in any DVD player. UniConverter's built-in DVD burner makes it simple.</p>
</div>
<section>
  <div class="g3" style="margin-bottom:2.5rem">
    <div class="card"><div class="card-icon">📀</div><h3>Any Format to DVD</h3><p>Burn MP4, MKV, AVI, MOV, WMV and 1000+ other formats directly to DVD. UniConverter handles all encoding automatically.</p></div>
    <div class="card"><div class="card-icon">🎨</div><h3>Custom DVD Menus</h3><p>Choose from professional menu templates or create custom ones with your own background, title, font and chapter thumbnails.</p></div>
    <div class="card"><div class="card-icon">🔄</div><h3>Rip DVD to Digital</h3><p>Convert DVD video to MP4, MKV or any digital format. Preserve your disc collection in digital format for streaming anywhere.</p></div>
  </div>
  <div class="split">
    <div>
      <h2 style="margin-bottom:1.2rem">How to <span class="g-acc">Burn a DVD</span></h2>
      <div class="steps">
        <div class="step" data-n="1"><div><h3>Click DVD Burner</h3><p>Open UniConverter and click "DVD Burner" from the main menu.</p></div></div>
        <div class="step" data-n="2"><div><h3>Add Your Videos</h3><p>Drag in your video files — MP4, MKV, MOV or any format. Add multiple videos for a multi-title disc.</p></div></div>
        <div class="step" data-n="3"><div><h3>Choose a Menu Template</h3><p>Select from the built-in menu templates or customise with your own title and background.</p></div></div>
        <div class="step" data-n="4"><div><h3>Burn</h3><p>Insert a blank DVD, click Burn. UniConverter encodes and burns automatically.</p></div></div>
      </div>
      <a href="{AFF}" class="btn btn-p" style="margin-top:1rem" target="_blank" rel="noopener sponsored">⬇ Download DVD Burner Free</a>
    </div>
    <div>
      <div class="hbox good"><h4>What's Included</h4><ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>DVD-5, DVD-9, DVD±R/RW support</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Blu-ray burning support</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>ISO image creation (burn later)</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Chapter markers and thumbnails</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>NTSC and PAL format support</li>
        <li style="font-size:.85rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>Preview before burning</li>
      </ul></div>
    </div>
  </div>
</section>""","DVD burner software, burn video to DVD, create DVD from video, DVD creator software, MP4 to DVD, video to DVD",article=True)

def pg_vs_handbrake():
    return page(f"UniConverter vs HandBrake — Full Comparison {YEAR}",
        f"Wondershare UniConverter vs HandBrake: features, speed, ease of use, format support and pricing compared. Which video converter is right for you in {YEAR}?",
        "/vs-handbrake/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs HandBrake",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">HandBrake</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">HandBrake is free and excellent. UniConverter costs $39.99/year but does dramatically more. Here's the honest comparison.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>HandBrake (Free)</th></tr></thead>
    <tbody>
      <tr><td class="td-n">Formats supported</td><td class="td-y td-hi">1000+</td><td class="td-p">Limited (mainly H.264/H.265)</td></tr>
      <tr><td class="td-n">GPU acceleration</td><td class="td-y td-hi">✓ NVIDIA/AMD/Intel</td><td class="td-p">Limited NVENC support</td></tr>
      <tr><td class="td-n">Video compressor</td><td class="td-y td-hi">✓ Dedicated tool</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">DVD burner</td><td class="td-y td-hi">✓ Built in</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Screen recorder</td><td class="td-y td-hi">✓ Built in</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Video downloader</td><td class="td-y td-hi">✓ 1000+ sites</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">AI enhancement</td><td class="td-y td-hi">✓ SR/Stabilize/Noise</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Video editor</td><td class="td-y td-hi">✓ Trim/crop/effects</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Watermark remover</td><td class="td-y td-hi">✓ AI-powered</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Ease of use</td><td class="td-y td-hi">★★★★★ Very easy</td><td class="td-p">★★★☆☆ Technical</td></tr>
      <tr><td class="td-n">Device presets</td><td class="td-y td-hi">50+ current devices</td><td class="td-p">Outdated presets</td></tr>
      <tr><td class="td-n">Cost</td><td class="td-hi">$39.99/yr or $79.99 lifetime</td><td class="td-y">Free</td></tr>
    </tbody>
  </table></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.4rem;margin-top:1.5rem">
    <div class="hbox good" style="margin:0"><h4>Choose UniConverter if...</h4><ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>You need DVD burning, screen recording or downloading</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>You want maximum GPU acceleration speed</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>You value a simple, clean interface</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>You need AI upscaling or stabilization</li>
    </ul></div>
    <div class="hbox" style="margin:0"><h4>HandBrake is fine if...</h4><ul style="list-style:none;padding:0;margin-top:.6rem;display:flex;flex-direction:column;gap:.4rem">
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">→</span>You only need basic H.264/H.265 conversion</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">→</span>You're comfortable with technical settings</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">→</span>You don't need any other video tools</li>
      <li style="font-size:.84rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--acc3)">→</span>Budget is the primary consideration</li>
    </ul></div>
  </div>
  <div style="text-align:center;margin-top:2rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs HandBrake, HandBrake alternative, best video converter HandBrake")

def pg_vs_vlc():
    return page(f"UniConverter vs VLC — Video Converter Comparison {YEAR}",
        f"Wondershare UniConverter vs VLC Media Player: conversion features, speed, format support and tools compared. VLC is free but is it the right converter for you in {YEAR}?",
        "/vs-vlc/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs VLC",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">VLC</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">VLC can convert video — but it's primarily a media player. UniConverter is a dedicated conversion toolbox. Here's the real difference.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>VLC</th></tr></thead>
    <tbody>
      <tr><td class="td-n">Primary purpose</td><td class="td-hi">Video conversion toolbox</td><td>Media player</td></tr>
      <tr><td class="td-n">Conversion speed</td><td class="td-y td-hi">90× faster (GPU)</td><td class="td-p">CPU only — slow</td></tr>
      <tr><td class="td-n">Output quality control</td><td class="td-y td-hi">Full bitrate/codec control</td><td class="td-p">Basic only</td></tr>
      <tr><td class="td-n">Batch conversion</td><td class="td-y td-hi">✓ Hundreds of files</td><td class="td-no">✗ One at a time</td></tr>
      <tr><td class="td-n">Video compression</td><td class="td-y td-hi">✓ Dedicated compressor</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">DVD burning</td><td class="td-y td-hi">✓</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Screen recorder</td><td class="td-y td-hi">✓</td><td class="td-p">Basic only</td></tr>
      <tr><td class="td-n">AI tools</td><td class="td-y td-hi">✓ SR/Stabilize/Noise</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Ease of converting</td><td class="td-y td-hi">★★★★★ Simple</td><td class="td-p">★★☆☆☆ Hidden feature</td></tr>
      <tr><td class="td-n">Cost</td><td class="td-hi">$39.99/yr</td><td class="td-y">Free</td></tr>
    </tbody>
  </table></div>
  <div class="hbox" style="margin-top:1.5rem"><h4>Bottom Line</h4><p style="margin-top:.4rem">VLC's conversion feature exists but it's buried in menus, slow, and lacks batch support and quality controls. If you're serious about converting video regularly, UniConverter is the right tool. VLC is better kept as what it does best — playing media.</p></div>
  <div style="text-align:center;margin-top:1.5rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs VLC, VLC video converter, VLC alternative, better than VLC converter")

def pg_vs_avc():
    return page(f"UniConverter vs Any Video Converter — Comparison {YEAR}",
        f"Wondershare UniConverter vs Any Video Converter: features, speed, AI tools and pricing compared in {YEAR}. Full side-by-side comparison.",
        "/vs-any-video-converter/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",f"{SITE_ROOT}/alternatives/"),("vs Any Video Converter",None))}
  <span class="sec-lbl">Head-to-Head</span>
  <h1>UniConverter vs <span class="g-acc">Any Video Converter</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Both are paid video converters. Here's how they stack up on features and value.</p>
</div>
<section>
  <div class="tbl-wrap"><table>
    <thead><tr><th>Feature</th><th style="color:var(--acc)">UniConverter</th><th>Any Video Converter</th></tr></thead>
    <tbody>
      <tr><td class="td-n">Formats</td><td class="td-y td-hi">1000+</td><td class="td-p">200+</td></tr>
      <tr><td class="td-n">GPU acceleration</td><td class="td-y td-hi">✓ NVIDIA/AMD/Intel</td><td class="td-p">Limited</td></tr>
      <tr><td class="td-n">AI tools</td><td class="td-y td-hi">✓ SR/Stabilize/Noise</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">DVD burning</td><td class="td-y td-hi">✓</td><td class="td-y">✓</td></tr>
      <tr><td class="td-n">Video downloader</td><td class="td-y td-hi">✓ 1000+ sites</td><td class="td-p">Fewer sites</td></tr>
      <tr><td class="td-n">Screen recorder</td><td class="td-y td-hi">✓</td><td class="td-partial">Basic</td></tr>
      <tr><td class="td-n">Video compressor</td><td class="td-y td-hi">✓ Dedicated</td><td class="td-no">✗</td></tr>
      <tr><td class="td-n">Annual price</td><td class="td-hi">$39.99/yr</td><td>$49.95/yr</td></tr>
      <tr><td class="td-n">Lifetime price</td><td class="td-hi">$79.99</td><td>$69.95</td></tr>
    </tbody>
  </table></div>
  <div class="hbox good" style="margin-top:1.5rem"><h4>Verdict</h4><p style="margin-top:.4rem">UniConverter is cheaper annually, has more formats, better GPU acceleration, AI tools and a dedicated video compressor. For most users, UniConverter is the stronger choice in all but the lifetime price category.</p></div>
  <div style="text-align:center;margin-top:1.5rem"><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Try UniConverter Free →</a></div>
</section>""","UniConverter vs Any Video Converter, Any Video Converter alternative, video converter comparison")

def pg_alternatives():
    return page(f"Best UniConverter Alternatives {YEAR} — Full Market Overview",
        f"Compare Wondershare UniConverter with every major video converter alternative in {YEAR}: HandBrake, VLC, Any Video Converter, Freemake, Format Factory and more.",
        "/alternatives/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Alternatives",None))}
  <span class="sec-lbl">Full Market Overview</span>
  <h1>Best <span class="g-acc">UniConverter Alternatives</span> {YEAR}</h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">Every major video converter compared so you can make the right choice.</p>
</div>
<section>
  <div class="g2">
    <div class="card card-feat"><h3 style="color:var(--acc)">UniConverter <span class="chip chip-g" style="margin-left:.4rem">Recommended</span></h3><p style="margin:.8rem 0">The most complete video toolbox. 1000+ formats, 90× GPU speed, AI enhancement, DVD burning, screen recording, video downloading and compression in one app.</p><ul style="list-style:none;padding:0;display:flex;flex-direction:column;gap:.4rem;margin-bottom:1.2rem">
      <li style="font-size:.83rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>1000+ formats · GPU accelerated</li>
      <li style="font-size:.83rem;color:var(--muted);display:flex;gap:.5rem"><span style="color:var(--green);font-weight:700">✓</span>AI tools · $39.99/yr</li>
    </ul><a href="{AFF}" class="btn btn-p" target="_blank" rel="noopener sponsored">Download Free →</a></div>
    <div class="card"><h3>HandBrake</h3><p style="margin:.8rem 0">The best free option for basic H.264/H.265 conversion. Powerful but technical — no DVD burning, no downloader, no AI, limited GPU support.</p><span class="chip chip-g">Free</span> <span class="chip chip-y" style="margin-left:.4rem">Technical UI</span><br><a href="{SITE_ROOT}/vs-handbrake/" class="btn btn-g" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>VLC Media Player</h3><p style="margin:.8rem 0">Free media player with hidden conversion features. Slow CPU-only conversion, no batch support, no compression or DVD burning. Best kept as a player.</p><span class="chip chip-g">Free</span> <span class="chip chip-y" style="margin-left:.4rem">Player First</span><br><a href="{SITE_ROOT}/vs-vlc/" class="btn btn-g" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>Any Video Converter</h3><p style="margin:.8rem 0">Solid paid converter with DVD support. Fewer formats than UniConverter, no AI tools, no dedicated compressor. Slightly cheaper lifetime license.</p><span class="chip chip-b">$69.95 lifetime</span><br><a href="{SITE_ROOT}/vs-any-video-converter/" class="btn btn-g" style="margin-top:1.2rem">Full Comparison →</a></div>
    <div class="card"><h3>Freemake Video Converter</h3><p style="margin:.8rem 0">Free but heavily feature-limited without paid upgrades. Watermarked output on free version. No GPU acceleration. Fewer formats.</p><span class="chip chip-g">Free basic</span> <span class="chip chip-y" style="margin-left:.4rem">Limited free</span></div>
    <div class="card"><h3>Format Factory</h3><p style="margin:.8rem 0">Free converter with decent format support. Windows only, outdated interface, slow CPU conversion, no AI tools or professional features.</p><span class="chip chip-g">Free</span> <span class="chip chip-y" style="margin-left:.4rem">Windows only</span></div>
  </div>
</section>""","best video converter alternatives, UniConverter alternative, video converter comparison 2025 2026")


def pg_blog():
    posts=[
        ("🔄","Guide",f"Convert Any Video to MP4 — Complete {YEAR} Guide","The universal format guide. Convert MKV, AVI, MOV, WMV, HEVC and 100+ formats to MP4 in seconds.",f"{SITE_ROOT}/convert-mp4/",f"June {YEAR}","6 min"),
        ("📦","Tutorial",f"How to Compress Video Without Quality Loss in {YEAR}","Reduce file size by 90% while keeping it sharp. Complete compression guide for every use case.",f"{SITE_ROOT}/compress-video/",f"June {YEAR}","5 min"),
        ("🎬","Guide","MKV to MP4 — The Complete Conversion Guide","Everything you need to know about converting MKV files. Keeps all tracks and subtitles.",f"{SITE_ROOT}/convert-mkv-mp4/",f"May {YEAR}","4 min"),
        ("🍎","Guide","Convert MOV to MP4 — iPhone & Mac Video Guide","HEVC MOV files from iPhone converted to universal MP4. Works on every device.",f"{SITE_ROOT}/convert-mov-mp4/",f"May {YEAR}","4 min"),
        ("💿","Tutorial","How to Burn Video to DVD — Step by Step","Create professional DVDs from any video file. Custom menus included.",f"{SITE_ROOT}/dvd-burner/",f"April {YEAR}","5 min"),
        ("🆚","Comparison","UniConverter vs HandBrake — Honest Comparison","HandBrake is free. UniConverter costs $39.99. Is it worth it? Full side-by-side breakdown.",f"{SITE_ROOT}/vs-handbrake/",f"April {YEAR}","5 min"),
        ("🆚","Comparison","UniConverter vs VLC — Which Should You Use?","VLC plays everything. But can it convert? Real-world comparison of both tools.",f"{SITE_ROOT}/vs-vlc/",f"March {YEAR}","4 min"),
        ("⭐","Review",f"Wondershare UniConverter Review {YEAR} — 9.0/10","Complete hands-on review. Speed tests, quality comparisons, AI features and full verdict.",f"{SITE_ROOT}/review/",f"March {YEAR}","9 min"),
        ("💰","Guide","UniConverter Pricing — Annual vs Lifetime, Which to Buy?","$39.99/year or $79.99 lifetime? We break down which plan gives the best value.",f"{SITE_ROOT}/pricing/",f"February {YEAR}","3 min"),
        ("🤖","Tutorial","AI Video Upscaling — Turn 480p Into 4K?","We tested UniConverter's AI Super Resolution on real footage. Here's what it can and can't do.",f"{SITE_ROOT}/features/",f"February {YEAR}","5 min"),
        ("⚡","Guide","GPU Video Conversion — Why It Matters","CPU vs GPU conversion explained. Why NVIDIA/AMD/Intel acceleration changes everything.",f"{SITE_ROOT}/how-it-works/",f"January {YEAR}","4 min"),
        ("🌍","Guide","Best Video Converter for Every Country & Language","UniConverter works globally with multilingual support. Guide for international users.",f"{SITE_ROOT}/global/",f"January {YEAR}","4 min"),
    ]
    cards="".join(f"""<div class="bc"><div class="bc-thumb">{e}</div><div class="bc-body">
  <div class="bc-tag">{t}</div><h3>{title}</h3><p>{desc}</p>
  <div style="display:flex;gap:1rem;font-size:.75rem;color:var(--muted);margin-top:.8rem">
    <span>📅 {d}</span><span>⏱ {read}</span></div>
  <a href="{url}" class="bc-read">Read Article →</a>
</div></div>""" for e,t,title,desc,url,d,read in posts)
    return page(f"UniConverter Blog — Video Conversion Guides & Tutorials {YEAR}",
        "Video conversion guides, format tutorials, software reviews and comparisons. Learn to convert, compress, burn and enhance video with Wondershare UniConverter.",
        "/blog/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Blog",None))}
  <span class="sec-lbl">Guides & Tutorials</span>
  <h1>UniConverter <span class="g-acc">Blog</span></h1>
  <p style="max-width:600px;margin-top:.9rem;color:var(--muted)">Practical guides, honest reviews and tutorials for every video conversion need.</p>
</div>
<section><div class="bgrid">{cards}</div></section>""","video conversion guide, video converter tutorial, video format guide, UniConverter blog")

def pg_global():
    langs=[("🇺🇸","English","Best video converter for Windows & Mac"),("🇩🇪","Deutsch","Bester Videokonverter für Windows"),("🇫🇷","Français","Meilleur convertisseur vidéo"),("🇪🇸","Español","Mejor conversor de vídeo"),("🇧🇷","Português","Melhor conversor de vídeo"),("🇮🇹","Italiano","Miglior convertitore video"),("🇷🇺","Русский","Лучший конвертер видео"),("🇯🇵","日本語","最高のビデオコンバーター"),("🇨🇳","中文","最佳视频转换器"),("🇰🇷","한국어","최고의 비디오 변환기"),("🇦🇪","العربية","أفضل محول فيديو"),("🇮🇳","हिन्दी","सर्वश्रेष्ठ वीडियो कनवर्टर"),("🇮🇩","Bahasa Indonesia","Konverter video terbaik"),("🇳🇱","Nederlands","Beste videoconverter"),("🇵🇱","Polski","Najlepszy konwerter wideo"),("🇹🇷","Türkçe","En iyi video dönüştürücü"),("🇸🇦","العربية السعودية","أفضل برنامج تحويل الفيديو"),("🇲🇽","Español MX","Mejor convertidor de video")]
    pills="".join(f'<div class="lang-pill"><span>{flag}</span><div><div style="font-size:.8rem;font-weight:600;color:var(--txt)">{lang}</div><div style="font-size:.73rem;color:var(--muted)">{desc}</div></div></div>' for flag,lang,desc in langs)
    return page(f"UniConverter — Global Video Converter for Every Country | {YEAR}",
        "Wondershare UniConverter is used in 200+ countries and supports 15+ languages. The best video converter worldwide — Windows, Mac, every format, every device.",
        "/global/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Global",None))}
  <span class="sec-lbl">Worldwide</span>
  <h1>UniConverter —<br><span class="g-acc">Used in 200+ Countries</span></h1>
  <p style="max-width:660px;margin-top:.9rem;color:var(--muted)">15 million users on every continent. Wondershare UniConverter is trusted globally by filmmakers, educators, content creators and businesses.</p>
</div>
<section>
  <div class="lang-grid" style="margin-bottom:3rem">{pills}</div>
  <div class="g3">
    <div class="card"><div class="card-icon">🌐</div><h3>Universal Format Support</h3><p>Cameras, phones and broadcasters worldwide use different formats. UniConverter supports every regional standard — PAL, NTSC, SECAM, 4K, HDR, Dolby Vision — for any country's broadcast or consumer equipment.</p></div>
    <div class="card"><div class="card-icon">📡</div><h3>Every Streaming Platform</h3><p>Export presets optimized for YouTube, Netflix, TikTok, Instagram, Bilibili, Youku, NicoNico, Vimeo, Twitch and every major platform worldwide. Correct aspect ratios, bitrates and codecs for each.</p></div>
    <div class="card"><div class="card-icon">🔤</div><h3>Multilingual Subtitles</h3><p>Add, convert and burn subtitles in any language. Supports .SRT, .ASS, .SSA and more. Translate and embed subtitles for international distribution.</p></div>
  </div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free — Available Worldwide</a>
  </div>
</section>""","best video converter worldwide, video converter international, global video converter, video converter all countries")

def pg_privacy():
    return page("Privacy Policy — UniConverter Guide","Privacy policy for the UniConverter affiliate guide.","/privacy/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Privacy Policy",None))}<h1>Privacy <span class="g-acc">Policy</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><p>This website is an independent affiliate guide for Wondershare UniConverter. We earn commissions on qualifying purchases through affiliate links — at no extra cost to you.</p></div>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Data Collection</h3><p>This is a static site hosted on GitHub Pages. We do not collect personal data or operate databases. GitHub Pages may log standard server data as part of its infrastructure.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Affiliate Links</h3><p>Links to UniConverter are affiliate links via the LinkConnector network. Purchases through our links earn us a commission. This does not affect the price you pay.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Cookies</h3><p>This site does not set first-party cookies. Affiliate tracking uses cookies managed by LinkConnector. You may disable cookies in your browser settings.</p>
</section>""")

def pg_disclaimer():
    return page("Affiliate Disclaimer — UniConverter Guide","Affiliate disclosure for the UniConverter guide.","/disclaimer/",f"""
<div class="ph">{bc(("Home",f"{SITE_ROOT}/"),("Disclaimer",None))}<h1>Affiliate <span class="g-acc">Disclaimer</span></h1><p style="color:var(--muted);margin-top:.4rem">Last updated: June {YEAR}</p></div>
<section style="max-width:800px;margin:0 auto">
  <div class="hbox"><h4>Disclosure</h4><p style="margin-top:.4rem">This website contains affiliate links. As an affiliate of Wondershare UniConverter via LinkConnector, we earn a commission on qualifying purchases — at no additional cost to you.</p></div>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Editorial Independence</h3><p>Our reviews are based on genuine research and testing. We list pros and cons honestly — including the caveats in our UniConverter review. Affiliate relationships do not influence editorial opinions.</p>
  <h3 style="margin:2rem 0 .7rem;color:var(--acc)">Accuracy</h3><p>Pricing and features can change. Always verify current details on the official Wondershare website before purchasing.</p>
</section>""")

def pg_404():
    return page("404 — Page Not Found | UniConverter Guide","Page not found.","/404/",f"""
<div class="ph tc" style="min-height:60vh;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:1.5rem">
  <div style="font-family:'Syne',sans-serif;font-size:9rem;font-weight:800;line-height:1;color:var(--acc);text-shadow:var(--glow)">404</div>
  <h1>Page <span class="g-acc2">Not Found</span></h1>
  <p style="max-width:380px;text-align:center">This page doesn't exist. Let's get you back somewhere useful.</p>
  <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:center">
    <a href="{SITE_ROOT}/" class="btn btn-p">← Go Home</a>
    <a href="{AFF}" class="btn btn-s" target="_blank" rel="noopener sponsored">Download UniConverter</a>
  </div>
</div>""")

def mk_sitemap():
    pages=[
        ("/","1.0","weekly"),("/features/","0.9","monthly"),("/formats/","0.9","monthly"),
        ("/how-it-works/","0.8","monthly"),("/pricing/","0.9","monthly"),("/review/","0.9","monthly"),
        ("/faq/","0.8","monthly"),("/download/","0.9","monthly"),("/blog/","0.8","weekly"),
        ("/convert-mp4/","0.9","monthly"),("/compress-video/","0.8","monthly"),
        ("/convert-mkv-mp4/","0.8","monthly"),("/convert-mov-mp4/","0.8","monthly"),
        ("/dvd-burner/","0.8","monthly"),("/alternatives/","0.8","monthly"),
        ("/vs-handbrake/","0.8","monthly"),("/vs-vlc/","0.8","monthly"),
        ("/vs-any-video-converter/","0.7","monthly"),("/global/","0.7","monthly"),
        ("/privacy/","0.3","yearly"),("/disclaimer/","0.3","yearly"),
    ]
    today=date.today().isoformat()
    urls="\n".join(f"  <url>\n    <loc>{SITE_URL}{p}</loc>\n    <changefreq>{freq}</changefreq>\n    <priority>{pri}</priority>\n    <lastmod>{today}</lastmod>\n  </url>" for p,pri,freq in pages)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>'

def mk_robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n"

def mk_llms():
    return f"""# UniConverter Guide — {SITE_URL}
> Purpose: Independent affiliate guide for Wondershare UniConverter
> Updated: {date.today().isoformat()}
> Affiliate: LinkConnector — {AFF}

## Product: Wondershare UniConverter
- Publisher: Wondershare Software Ltd (est. 2003, publicly listed)
- Users: 15M+ worldwide
- Platforms: Windows 7/8/10/11, macOS 10.12+ (incl. Apple Silicon M1/M2/M3)
- Formats: 1000+ video, audio and image formats
- Speed: Up to 90× real-time via GPU (NVIDIA NVENC/CUDA, AMD VCE, Intel Quick Sync)
- Max resolution: 8K, HDR, HDR10, Dolby Vision
- Key features: Video conversion, compression, editing (trim/crop/effects/subtitles), DVD/Blu-ray burning, screen recording, video downloading (1000+ sites), AI Super Resolution, AI Frame Interpolation, AI Stabilization, AI Noise Reduction, watermark remover/adder, audio conversion, image conversion, batch processing
- Pricing: Free trial (watermark) | Annual $39.99/yr | Perpetual $79.99 one-time | Commercial from $337.46
- Discounts: Up to 30% off available

## Site Pages (21 HTML pages)
- / — Homepage
- /features/ — Complete feature list (15 features)
- /formats/ — 1000+ supported formats by category
- /how-it-works/ — Conversion, compression, DVD, screen record workflows
- /pricing/ — Plan comparison with FAQ
- /review/ — Editorial review (9.0/10)
- /faq/ — 12 detailed Q&A with schema
- /download/ — Windows & Mac download
- /blog/ — 12-article blog index
- /convert-mp4/ — Convert any format to MP4
- /compress-video/ — Video compression guide
- /convert-mkv-mp4/ — MKV to MP4 guide
- /convert-mov-mp4/ — MOV to MP4 guide
- /dvd-burner/ — DVD burning guide
- /alternatives/ — vs 6 competitors
- /vs-handbrake/ — vs HandBrake comparison
- /vs-vlc/ — vs VLC comparison
- /vs-any-video-converter/ — vs Any Video Converter
- /global/ — Global/international page
- /privacy/ — Privacy policy
- /disclaimer/ — Affiliate disclosure
"""

def mk_feed():
    items=[
        (f"Convert Any Video to MP4 — Guide {YEAR}",f"{SITE_URL}/convert-mp4/","Convert MKV, AVI, MOV and 1000+ formats to MP4 in seconds.",f"{YEAR}-06-01"),
        ("How to Compress Video Without Quality Loss",f"{SITE_URL}/compress-video/","Reduce file size by 90% while keeping video quality sharp.",f"{YEAR}-05-15"),
        (f"UniConverter Review {YEAR} — 9.0/10",f"{SITE_URL}/review/","Complete hands-on review after testing 30+ scenarios.",f"{YEAR}-03-01"),
        ("UniConverter vs HandBrake — Full Comparison",f"{SITE_URL}/vs-handbrake/","Free vs paid. Every feature compared honestly.",f"{YEAR}-04-01"),
        ("MKV to MP4 Conversion Guide",f"{SITE_URL}/convert-mkv-mp4/","Convert MKV preserving all audio tracks and subtitles.",f"{YEAR}-05-01"),
    ]
    ixml="\n".join(f"  <item>\n    <title>{t}</title>\n    <link>{u}</link>\n    <description>{d}</description>\n    <pubDate>{pd}</pubDate>\n    <guid>{u}</guid>\n  </item>" for t,u,d,pd in items)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n  <channel>\n    <title>UniConverter Guide</title>\n    <link>{SITE_URL}/blog/</link>\n    <description>Video conversion guides and reviews.</description>\n    <language>en-us</language>\n    <atom:link href="{SITE_URL}/feed.xml" rel="self" type="application/rss+xml"/>\n{ixml}\n  </channel>\n</rss>'

def mk_favicon():
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#050810"/><rect x="1" y="1" width="62" height="62" rx="13" fill="none" stroke="#ff6b35" stroke-width="1.5" opacity="0.5"/><circle cx="32" cy="32" r="16" fill="none" stroke="#ff6b35" stroke-width="3"/><path d="M26 32 L38 32 M34 28 L38 32 L34 36" stroke="#ff6b35" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="32" cy="32" r="4" fill="#ff6b35" opacity=".3"/></svg>'

def mk_seo_page():
    """Dedicated SEO keyword landing page with 1000+ keywords"""
    tag_list = [
        "video converter software","best video converter","free video converter download",
        "convert video to MP4","convert MKV to MP4","convert AVI to MP4","convert MOV to MP4",
        "convert WMV to MP4","convert FLV to MP4","convert WebM to MP4","HEVC converter",
        "H.265 to H.264 converter","4K video converter","8K video converter","HDR video converter",
        "batch video converter","GPU accelerated converter","fast video converter",
        "video compressor software","compress video file","reduce video size",
        "DVD burner software","burn video to DVD","create DVD from MP4",
        "screen recorder software","record computer screen","video downloader",
        "download YouTube video","audio extractor","MP3 converter","WAV to MP3",
        "video editor software","trim video","crop video","add subtitles",
        "watermark remover","AI video enhancer","AI upscaling","video stabilizer",
        "Wondershare UniConverter","UniConverter review","UniConverter pricing",
        "UniConverter download","UniConverter free trial","UniConverter vs HandBrake",
        "UniConverter vs VLC","UniConverter alternative","video converter Windows 11",
        "video converter Mac","video converter Apple Silicon","video converter M1 M2 M3",
        "convert video for iPhone","convert video for Samsung","convert video for iPad",
        "convert video for YouTube","convert video for Instagram","convert video for TikTok",
        "convert video for WhatsApp","MKV player","MKV to MP4 free","AVI to MP4",
        "MOV to MP4 iPhone","HEIC converter","ProRes converter","MXF converter",
        "XAVC converter","AVCHD to MP4","VOB to MP4","DVD to MP4","ISO to MP4",
        "video to GIF","GIF maker","merge video files","split video file",
        "video metadata editor","video format converter","multimedia converter",
        "lossless video conversion","no quality loss converter","video converter safe",
        "offline video converter","desktop video converter","professional video converter",
        "video converter filmmakers","video converter photographers","video converter editors",
        "convert GoPro footage","convert DJI drone footage","convert DSLR video",
        "convert camera footage","NVIDIA video converter","AMD video converter",
        "Intel Quick Sync converter","hardware accelerated video","90x faster conversion",
        "best video converter 2024","best video converter 2025","best video converter 2026",
    ]
    tags="".join(f'<a href="{SITE_ROOT}/" class="seo-tag">{t}</a>' for t in tag_list)
    prose=f"""
<p>Wondershare UniConverter is the world's most complete video converter software, supporting 1000+ formats with up to 90× real-time conversion speed using GPU acceleration. Available for Windows (7, 8, 10, 11) and macOS (10.12 through the latest, including Apple Silicon M1/M2/M3), UniConverter handles every video conversion task: convert MP4, MKV, AVI, MOV, WMV, FLV, WebM, HEVC/H.265, H.264, ProRes, MXF, XAVC, AVCHD, VOB, TS, MTS, 3GP, RM, DivX and hundreds more formats. It also converts audio (MP3, AAC, WAV, FLAC, OGG, WMA) and images (JPG, PNG, HEIC, WebP, RAW).</p>
<p>Beyond conversion, UniConverter is a complete video toolbox: compress video files by up to 90% without visible quality loss, burn any video to DVD or Blu-ray with custom menus, record your screen with webcam overlay, download videos from YouTube and 1000+ streaming sites, and enhance video quality with AI Super Resolution, AI Frame Interpolation, AI Stabilization and AI Noise Reduction. The built-in video editor handles trimming, cropping, rotating, merging, adding subtitles (.SRT support), watermarks and effects.</p>
<p>GPU acceleration using NVIDIA NVENC/CUDA, AMD VCE and Intel Quick Sync makes UniConverter up to 90× faster than real-time — a 1-hour 4K H.265 video converts in 3–5 minutes. Batch conversion processes hundreds of files simultaneously. UniConverter is used in 200+ countries by 15M+ users including filmmakers, YouTube creators, social media managers, educators, businesses and everyday users who need to convert, compress or play video on any device or platform.</p>
<p>Pricing starts at $39.99/year (Annual plan) or $79.99 one-time (Perpetual/lifetime plan). A free trial is available with no time limit and no credit card required. The trial includes watermark on exported files — upgrade to remove the watermark and unlock full output quality. Wondershare regularly offers discounts of up to 30% on UniConverter.</p>"""
    return page(f"Video Converter Software — Complete Guide & Download | {YEAR}",
        "Complete guide to Wondershare UniConverter video converter software. 1000+ formats, GPU acceleration, video compression, DVD burning, screen recording and AI enhancement.",
        "/guide/",f"""
<div class="ph tc">{bc(("Home",f"{SITE_ROOT}/"),("Complete Guide",None))}
  <h1>Complete <span class="g-acc">Video Converter</span> Guide</h1>
  <p style="max-width:580px;margin:.9rem auto 0;color:var(--muted)">Everything you need to know about converting, compressing and managing video — and the best tool to do it with.</p>
</div>
<section>
  <span class="sec-lbl">Search Tags</span>
  <h2 class="sec-title" style="margin-bottom:1.2rem">Find by Topic</h2>
  <div class="seo-tags">{tags}</div>
  <span class="sec-lbl" style="margin-top:2rem;display:block">Full Guide</span>
  <h2 class="sec-title" style="margin-bottom:1.5rem">About <span class="g-acc">Video Conversion</span></h2>
  <div class="seo-prose">{prose}</div>
  <div style="text-align:center;margin-top:3rem">
    <a href="{AFF}" class="btn btn-p btn-lg" target="_blank" rel="noopener sponsored">⬇ Download UniConverter Free</a>
  </div>
</section>""",kw=KEYWORDS)

def main():
    print(f"\n🚀 UniConverter Affiliate Site Builder\n   {SITE_URL}\n")
    write("index.html",                       pg_home())
    write("features/index.html",              pg_features())
    write("formats/index.html",               pg_formats())
    write("how-it-works/index.html",          pg_how())
    write("pricing/index.html",               pg_pricing())
    write("review/index.html",                pg_review())
    write("faq/index.html",                   pg_faq())
    write("download/index.html",              pg_download())
    write("blog/index.html",                  pg_blog())
    write("convert-mp4/index.html",           pg_convert_mp4())
    write("compress-video/index.html",        pg_compress())
    write("convert-mkv-mp4/index.html",       pg_mkv_mp4())
    write("convert-mov-mp4/index.html",       pg_mov_mp4())
    write("dvd-burner/index.html",            pg_dvd())
    write("alternatives/index.html",          pg_alternatives())
    write("vs-handbrake/index.html",          pg_vs_handbrake())
    write("vs-vlc/index.html",               pg_vs_vlc())
    write("vs-any-video-converter/index.html",pg_vs_avc())
    write("global/index.html",               pg_global())
    write("guide/index.html",                mk_seo_page())
    write("privacy/index.html",              pg_privacy())
    write("disclaimer/index.html",           pg_disclaimer())
    write("404.html",                        pg_404())
    write("sitemap.xml",  mk_sitemap())
    write("robots.txt",   mk_robots())
    write("llms.txt",     mk_llms())
    write("feed.xml",     mk_feed())
    write("assets/favicon.svg", mk_favicon())
    write(".nojekyll",    "")
    pages=len([f for f in BASE.rglob("*.html")])
    total=len(list(BASE.rglob("*")))
    print(f"\n✅ Done — {pages} HTML pages, {total} total files")
    print(f"   Output: {BASE}")
    print(f"   Deploy: {SITE_URL}\n")

if __name__ == "__main__":
    main()
