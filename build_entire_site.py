import os
import random
from datetime import datetime

def get_base_css():
    """Returns a centralized, high-conversion design system tailored for B2B fintech conversions."""
    return """<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ef4444; /* High-CTR Alert Coral */
            --primary-dark: #dc2626;
            --secondary: #0f172a; /* Slate Black Executive Accents */
            --accent: #10b981; /* High CTR Native Merchant Green */
            --accent-dark: #059669;
            --text-main: #334155;
            --text-dark: #0f172a;
            --bg-light: #f8fafc;
            --border: #e2e8f0;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Plus Jakarta Sans', system-ui, sans-serif; line-height: 1.6; color: var(--text-main); background: #ffffff; -webkit-font-smoothing: antialiased; }
        .container { max-width: 1000px; margin: 0 auto; padding: 0 24px; }
        .hero { padding: 80px 0 60px 0; text-align: center; background: linear-gradient(135deg, #f59e0b, #ef4444); color: white; border-bottom: 1px solid var(--border); border-radius: 0 0 24px 24px; }
        .hero h1 { font-size: 3rem; font-weight: 800; margin-bottom: 20px; letter-spacing: -0.03em; color: white; }
        .hero-lead { font-size: 1.25rem; color: rgba(255, 255, 255, 0.9); max-width: 750px; margin: 0 auto 32px auto; }
        .cta-btn { display: inline-flex; align-items: center; background: var(--accent); color: white; padding: 16px 36px; font-size: 1.2rem; font-weight: 700; text-decoration: none; border-radius: 12px; box-shadow: 0 10px 25px rgba(16,185,129,0.35); transition: all 0.2s ease; }
        .cta-btn:hover { background: var(--accent-dark); transform: translateY(-2px); box-shadow: 0 12px 30px rgba(16,185,129,0.45); }
        .disclosure { font-size: 0.85rem; color: rgba(255,255,255,0.8); margin-top: 16px; }
        h2 { font-size: 2.2rem; color: var(--text-dark); margin: 44px 0 20px 0; letter-spacing: -0.02em; }
        .card-matrix { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin: 32px 0; }
        .feature-card { background: white; border: 1px solid var(--border); padding: 24px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }
        .feature-card h3 { color: var(--text-dark); font-size: 1.25rem; margin-bottom: 10px; }
        table { width: 100%; border-collapse: collapse; margin: 24px 0; font-size: 1rem; }
        th, td { border: 1px solid var(--border); padding: 14px; text-align: left; }
        th { background: var(--bg-light); color: var(--text-dark); font-weight: 700; }
        .calc-box { background: var(--secondary); color: white; padding: 40px; border-radius: 24px; margin: 48px 0; }
        .calc-box h3 { color: white; font-size: 1.6rem; margin-bottom: 8px; }
        .slider-container { margin: 32px 0; }
        input[type=range] { width: 100%; accent-color: var(--primary); margin: 12px 0; cursor: pointer; }
        .calc-results { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; background: rgba(255,255,255,0.05); padding: 24px; border-radius: 16px; }
        .stat-label { font-size: 0.85rem; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em; }
        .stat-val { font-size: 1.8rem; font-weight: 800; margin-top: 4px; }
        .blog-list { list-style: none; margin: 24px 0; display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
        .related-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; margin: 24px 0; list-style: none; }
        @media (max-width: 768px) { .blog-list, .related-grid { grid-template-columns: 1fr; } }
        .blog-list li, .related-grid li { background: var(--bg-light); border: 1px solid var(--border); padding: 20px; border-radius: 12px; transition: transform 0.2s ease; }
        .blog-list li:hover { transform: translateY(-2px); }
        .blog-list a, .related-grid a { color: var(--text-dark); font-weight: 700; text-decoration: none; font-size: 1.1rem; display: block; margin-bottom: 4px; }
        .blog-list a:hover, .related-grid a:hover { color: var(--primary); }
        .affiliate-disclosure { background: #fffbeb; border-left: 4px solid #f59e0b; padding: 15px; margin: 20px 0; font-size: 0.9em; border-radius: 4px; color: #78350f; }
        footer { border-top: 1px solid var(--border); padding: 40px 0; text-align: center; font-size: 0.9rem; color: #64748b; background: var(--bg-light); margin-top: 80px; }
        @media (max-width: 768px) { .calc-results { grid-template-columns: 1fr; } .hero h1 { font-size: 2.2rem; } }
    </style>"""

def generate_programmatic_data():
    """Generates 100 distinct layout configurations across niches targeting high-volume B2B channels."""
    niches = [
        {"name": "SEO Agencies", "action": "paying 50+ independent global contractors weekly", "pain": "per-transaction premium overheads"},
        {"name": "E-commerce Brands", "name_alt": "Ecommerce Brands", "action": "settling high-volume overseas supplier balances", "pain": "unexpected transaction micro-batch delays"},
        {"name": "Roofing Contractors", "action": "purchasing major raw material drop shipments", "pain": "restrictive daily card settlement caps"},
        {"name": "Construction Suppliers", "action": "managing commercial client trade credit applications", "pain": "manual invoice reconciliation bottlenecks"},
        {"name": "Digital Marketing Agencies", "action": "distributing ad campaign spend reimbursements", "pain": "hidden accounts payable transaction fees"},
        {"name": "B2B SaaS Startups", "action": "reconciling automated recurring software vendor charges", "pain": "broken double-entry accounting records"},
        {"name": "Real Estate Brokers", "action": "wiring structural escrow and agent commission options", "pain": "failed security and clearing verification layers"},
        {"name": "Fitness Networks", "action": "paying specialized satellite gym facility trainers", "pain": "manual spreadsheet upload processing delays"},
        {"name": "Financial Advisory Squads", "action": "disbursing verified client investment capital routes", "pain": "unreliable consumer-grade direct apps"},
        {"name": "Insurance Brokers", "action": "routing premium payment balances to carriers", "pain": "slow next-day ledger validation updates"},
        {"name": "Mortgage Lenders", "action": "processing corporate escrow and loan funding items", "pain": "restrictive transaction verification limits"},
        {"name": "Online Educators", "action": "compensating content creators and curriculum designers", "pain": "exorbitant mass payout processing tools"},
        {"name": "B2B Sales Teams", "action": "distributing high-volume tiered performance bonuses", "pain": "clunky payment interface tools"},
        {"name": "Conversion Optimizers", "action": "funding software tools across multiple test suites", "pain": "untracked business operations billing"},
        {"name": "Affiliate Marketers", "action": "issuing mass payment distributions to traffic sub-networks", "pain": "expensive bank wire execution fees"},
        {"name": "Local Service Businesses", "action": "disbursing payments for wholesale inventory parts", "pain": "lost physical mail check delivery delays"},
        {"name": "Creative Agencies", "action": "settling monthly design subcontractor invoices", "pain": "clunky manual QuickBooks CSV data syncs"},
        {"name": "Crypto Platforms", "action": "clearing institutional operational corporate balances", "pain": "unreasonable flat-rate payment gateway surcharges"},
        {"name": "Healthcare Recruiters", "action": "processing weekly travel nurse payroll distribution profiles", "pain": "unreliable third-party contractor payment rails"},
        {"name": "Legal Consultants", "action": "managing corporate settlement distribution outlays", "pain": "chargeback penalties and hidden fee penalties"}
    ]
    
    topics = [
        {"pattern": "nickel-review-for-{slug}", "title": "Nickel.com Review 2026: The Ultimate Payments Architecture for {niche}"},
        {"pattern": "how-to-automate-ach-for-{slug}", "title": "How to Eliminate Cashflow Transaction Fees for {niche} Instantly"},
        {"pattern": "nickel-pricing-guide-for-{slug}", "title": "Nickel Pricing Deep-Dive: Can a Growing {niche} Save Thousands Monthly?"},
        {"pattern": "nickel-vs-melio-for-{slug}", "title": "Nickel vs Melio for {niche}: Which Business Payment Rail Wins?"},
        {"pattern": "quickbooks-payment-automation-for-{slug}", "title": "Top 5 Accounts Payable Integration Strategies for an Active {niche}"}
    ]
    
    posts = []
    for item in niches:
        niche = item["name"]
        niche_slug = item.get("name_alt", niche).lower().replace(" ", "-")
        for topic in topics:
            slug = topic["pattern"].format(slug=niche_slug)
            title = topic["title"].format(niche=niche)
            desc = f"Discover how switching to Nickel's free B2B accounts payable framework helps a modern {niche} bypass tracking fees completely."
            content = (
                f"For any modern, scaling {niche}, traditional banking rails and consumer-grade apps introduce severe operational drag. "
                f"When you are actively tasked with {item['action']}, falling prey to {item['pain']} can deeply damage your corporate margins. "
                f"By moving your corporate ledger management over to Nickel, an active {niche} can drop processing expenses down to absolute zero using permanent, unlimited free ACH networks. "
                f"Whether you need to generate high-capacity payment links up to $1,000,000, route auto-synced invoices directly into QuickBooks Online, or implement secure vendor approval workflows, "
                f"Nickel eliminates manual financial friction so your scaling business operating pipeline updates flawlessly in real time."
            )
            posts.append({"slug": slug, "title": title, "desc": desc, "content": content})
    return posts

def build_entire_site():
    base_url = "https://brightlane.github.io/nickel.com"
    affiliate_url = "https://partners.app.nickel.com/qkyes0hyd28v?utm_source=deploy"
    today_str = datetime.today().strftime('%Y-%m-%d')

    blog_posts = generate_programmatic_data()
    os.makedirs("blog", exist_ok=True)
    
    urls_for_sitemap = [f"{base_url}/index.html"]
    for post in blog_posts:
        urls_for_sitemap.append(f"{base_url}/blog/{post['slug']}.html")

    # ==========================================
    # 1. BUILD THE CENTRAL HUB NODE
    # ==========================================
    index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nickel.com Review 2026: Best Business Payments Platform - Free to Start</title>
    <meta name="description" content="Nickel.com: FREE accounts + unlimited ACH + QuickBooks integration + bill pay + vendor management. Perfect for agencies, ecommerce, SMBs managing payments & cashflow.">
    <link rel="canonical" href="{base_url}/index.html" />
    {get_base_css()}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Product",
      "name": "Nickel Payments Platform",
      "description": "Comprehensive corporate payment, invoicing, and free ACH network infrastructure built for modern industry scale.",
      "brand": {{"@type": "Brand", "name": "Nickel"}},
      "offers": {{
        "@type": "AggregateOffer",
        "priceCurrency": "USD",
        "lowPrice": "0",
        "highPrice": "35",
        "offerCount": "2"
      }}
    }}
    </script>
</head>
<body>
    <header class="hero">
        <div class="container">
            <h1>💳 Nickel.com 2026: #1 Business Payments Platform</h1>
            <p class="hero-lead">FREE accounts + unlimited ACH + QuickBooks integration + automated bill pay + vendor management. Perfect for agencies paying contractors & ecommerce managing suppliers.</p>
            <div>
                <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Start FREE Account</a>
            </div>
            <p class="disclosure">Links earn commissions at no extra cost or platform operational premium to your account ledger setup.</p>
        </div>
    </header>

    <main class="container">
        <div class="affiliate-disclosure">
            <strong>Affiliate Disclosure:</strong> Links earn commissions at no extra cost to your corporate account parameters.
        </div>

        <h2>Why Nickel.com Wins for Agencies & SMBs</h2>
        <p>No monthly fees + unlimited ACH transfers + native QuickBooks sync. Pay contractors, vendors, and freelancers instantly. Track every business dollar live in one dashboard.</p>

        <div class="card-matrix">
            <div class="feature-card">
                <h3>💸 Unlimited FREE ACH</h3>
                <p>Pay vendors/contractors instantly. No hidden transaction-level fees.</p>
            </div>
            <div class="feature-card">
                <h3>⚡ QuickBooks Native</h3>
                <p>Automatic background transaction sync. Eliminate manual CSV imports.</p>
            </div>
            <div class="feature-card">
                <h3>📋 Automated Bill Pay</h3>
                <p>Schedule recurring vendor settlements with multi-user approval workflows.</p>
            </div>
            <div class="feature-card">
                <h3>👥 Vendor Profiles</h3>
                <p>Onboard contractors safely. Issue dynamic payment collection web links up to $1M.</p>
            </div>
        </div>

        <section class="calc-box">
            <h3>Calculate Your Payment Processing Waste</h3>
            <div class="slider-container">
                <label for="transRange" style="font-weight: 600; display: block; margin-bottom: 8px;">Estimated Monthly External Payments: <span id="transLabel" style="color: var(--primary); font-weight:800;">150</span> transactions</label>
                <input type="range" id="transRange" min="10" max="1000" step="10" value="150" oninput="updateCalculations(this.value)">
            </div>
            <div class="calc-results">
                <div>
                    <div class="stat-label">Traditional Bank Fees (Avg $1.50/ACH)</div>
                    <div id="standardVal" class="stat-val" style="color: #ef4444;">$225.00</div>
                </div>
                <div>
                    <div class="stat-label">Nickel Infrastructure Fees</div>
                    <div id="interactiveVal" class="stat-val" style="color: var(--accent);">$0.00</div>
                </div>
            </div>
        </section>

        <h2>Nickel.com Pricing 2026</h2>
        <table>
            <tr><th>Feature</th><th>Core Plan</th><th>Plus Plan (Annual)</th></tr>
            <tr><td>Monthly Access Fee</td><td>$0 / mo</td><td>$35 / mo</td></tr>
            <tr><td>ACH Transfers</td><td>FREE (Unlimited)</td><td>FREE (Faster 2-Day processing)</td></tr>
            <tr><td>QuickBooks Online Sync</td><td>✅ Included</td><td>✅ Included</td></tr>
            <tr><td>User Seats Available</td><td>Up to 3 Seats</td><td>✅ Unlimited Seats</td></tr>
            <tr><td>Card Processing Rates</td><td>Flat 2.9%</td><td>Next-day card settlement processing</td></tr>
        </table>
        <p style="margin-bottom: 30px;"><strong>Activate completely free</strong>. No minimum initial balances required.</p>

        <h2>Nickel vs QuickBooks Payments vs Melio</h2>
        <table>
            <tr><th>Operational Vector</th><th>Nickel Payments</th><th>QuickBooks Payments</th><th>Melio Basic</th></tr>
            <tr><td>Monthly Entry Fee</td><td>✅ $0 Core</td><td>$15 - $50 / mo</td><td>$0</td></tr>
            <tr><td>Digital ACH Transfers</td><td>✅ $0 (Unlimited)</td><td>$1.00 - $3.00 each</td><td>Tiered volumes limit</td></tr>
            <tr><td>Transaction Ceiling</td><td>✅ Up to $1,000,000</td><td>Strict compliance limits</td><td>Standard SMB ceilings</td></tr>
            <tr><td>Fee Pass-Through</td><td>✅ Built-in option</td><td>❌ No</td><td>Requires manual add-on</td></tr>
        </table>

        <h2>Perfect Agency Use Cases</h2>
        <ul style="margin: 20px 0; padding-left: 20px;">
            <li><strong>SEO Agencies:</strong> Pay 50+ remote delivery contractors weekly with zero per-transaction overhead.</li>
            <li><strong>PPC Specialists:</strong> Automate ad balance replenishment and map outputs directly to client profiles.</li>
            <li><strong>Affiliate Networks:</strong> Scale out clean corporate publisher payout parameters predictably.</li>
            <li><strong>Industrial Providers:</strong> Shift card transaction processing margins to the buyer securely.</li>
        </ul>

        <div style="background: #e8f5e8; padding: 35px; text-align: center; border-radius: 16px; margin: 40px 0; border: 1px solid #c2e7c2;">
            <h2 style="margin-top: 0;">Eliminate Outbound Payment Fees Forever</h2>
            <p style="margin-bottom: 20px; color: var(--text-main);">Join thousands of business networks scaling operations with clean digital ledger systems.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Get Free Business Account</a>
        </div>

        <h2>Deep-Dive Niche Optimization Directives</h2>
        <ul class="blog-list">"""
        
    for post in blog_posts:
        index_html += f'\n            <li><a href="blog/{post["slug"]}.html">→ {post["title"]}</a><p style="color:#64748b; font-size:0.9rem; margin-top:4px;">{post["desc"]}</p></li>'
        
    index_html += f"""
        </ul>
    </main>

    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA | B2B Cashflow & Operational Optimization</p>
        </div>
    </footer>

    <script>
        function updateCalculations(val) {{
            const transactions = parseInt(val);
            document.getElementById('transLabel').innerText = transactions.toLocaleString();
            const bankFees = transactions * 1.50;
            document.getElementById('standardVal').innerText = '$' + bankFees.toFixed(2);
            document.getElementById('interactiveVal').innerText = '$0.00';
        }}
        updateCalculations(150);
    </script>
</body>
</html>"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html.strip())

    # ==========================================
    # 2. BUILD THE 100 ENHANCED SUB-PAGES WITH CROSSLINKS
    # ==========================================
    for idx, post in enumerate(blog_posts):
        slug = post["slug"]
        
        # Pull 3 related articles sequentially to form a perfect inner silo loop
        related_links = []
        for offset in [1, 2, 3]:
            related_post = blog_posts[(idx + offset) % len(blog_posts)]
            related_links.append(f'<li><a href="{related_post["slug"]}.html">{related_post["title"]}</a></li>')
        related_html_str = "\n".join(related_links)

        post_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{post["title"]}</title>
    <meta name="description" content="{post["desc"]}">
    <link rel="canonical" href="{base_url}/blog/{slug}.html" />
    {get_base_css()}
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "{post["title"]}",
      "description": "{post["desc"]}",
      "datePublished": "{today_str}",
      "author": {{
        "@type": "Person",
        "name": "Benny Palmarino"
      }}
    }}
    </script>
</head>
<body>
    <div class="container" style="padding-top: 50px;">
        <div style="margin-bottom: 24px;"><a href="../index.html" style="color: var(--primary); text-decoration:none; font-weight:700;">← Back to Main Hub</a></div>
        <h1>{post["title"]}</h1>
        
        <article class="feature-card" style="background:#ffffff; margin-top:24px; border-left: 4px solid var(--primary); line-height:1.8;">
            <p style="font-size:1.15rem; color:var(--text-dark);">{post["content"]}</p>
        </article>

        <section class="calc-box" style="text-align:center; background: linear-gradient(135deg, var(--secondary) 0%, #1e293b 100%); margin: 40px 0;">
            <h3 style="margin-bottom:12px;">Optimize Your B2B Financial Architecture Today</h3>
            <p style="color:#cbd5e1; margin-bottom:24px; max-width:600px; margin-left:auto; margin-right:auto;">Stop tossing capital away on standard transaction processing tools. Switch over to unlimited fee-free ACH transfers and seamless QuickBooks automation loops.</p>
            <a href="{affiliate_url}" class="cta-btn" rel="sponsored">Claim Your Free Core Nickel Account</a>
        </section>

        <h3 style="margin-top: 40px;">Related Financial Architecture Guides</h3>
        <ul class="related-grid">
            {related_html_str}
        </ul>
    </div>
    <footer>
        <div class="container">
            <p>© 2026 Benny Palmarino | Langhorne, PA</p>
        </div>
    </footer>
</body>
</html>"""
        with open(f"blog/{slug}.html", "w", encoding="utf-8") as f:
            f.write(post_html.strip())

    # ==========================================
    # 3. BUILD AGENT COMPONENT: LLMS.TXT
    # ==========================================
    llms_txt = f"# Nickel Payments Automated Integration Mapping Directory\n> Structured programmatic indexes for LLM parsers, spiders, and indexing architectures.\n\n## Platform Nodes\n"
    llms_txt += f"- [Nickel Performance Platform Overview 2026]({base_url}/index.html): Pricing schedules, free core tiers, and platform performance parameters.\n"
    for post in blog_posts:
        llms_txt += f"- [{post['title']}]({base_url}/blog/{post['slug']}.html): {post['desc']}\n"
    with open("llms.txt", "w", encoding="utf-8") as f:
        f.write(llms_txt.strip())

    # ==========================================
    # 4. BUILD ACCESS COMPONENT: ROBOTS.TXT
    # ==========================================
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {base_url}/sitemap.xml")

    # ==========================================
    # 5. BUILD SEO DATA INDEX: SITEMAP.XML
    # ==========================================
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in urls_for_sitemap:
        sitemap_xml += f"    <url>\n        <loc>{url}</loc>\n        <lastmod>{today_str}</lastmod>\n        <changefreq>daily</changefreq>\n        <priority>0.8</priority>\n    </url>\n"
    sitemap_xml += "</urlset>"
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_xml.strip())
        
    print(f"Success! Built 1 Core Hub, {len(blog_posts)} Cross-Linked Sub-pages, robots.txt, llms.txt, and sitemap.xml layouts successfully.")

if __name__ == "__main__":
    build_entire_site()
