# Complete updater for index.html
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update title and meta if needed
content = content.replace(
    '<title>Is This a Scam? Free Scam Checker - Check Message, Link, Number, Email | IsThisScamOrReal.com</title>',
    '<title>Is This a Scam? Free Scam Checker & World Scampedia (300+ Scams) | IsThisScamOrReal.com</title>'
)

# 2. Update navigation link text
content = re.sub(
    r'<a href="#scam-database" onclick="showView\(\'scam-database\'\)" class="hover:text-white transition" data-i18n="navDatabase">[^<]+</a>',
    r'<a href="#scam-database" onclick="showView(\'scam-database\')" class="hover:text-white transition" data-i18n="navDatabase">Scampedia (300+)</a>',
    content
)

# 3. Update prominent button at bottom of section #scams
content = re.sub(
    r'View All 150\+ Scams in Database \(2016-2026\)',
    r'Explore World Scampedia (300+ Scams Database)',
    content
)

# 4. In section #scams header, update the auto-update badge:
content = re.sub(
    r'<div class="inline-flex items-center gap-2 px-3\.5 py-1\.5 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 rounded-full text-xs font-bold border border-emerald-200 dark:border-emerald-800 mb-3">\s*<span class="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>\s*<span>Last Updated: Today</span>\s*<span class="text-slate-300">•</span>\s*<span>⚡ New Scam Reported: 2 hours ago</span>\s*</div>',
    r'''<div class="inline-flex items-center gap-2 px-3.5 py-1.5 bg-emerald-50 dark:bg-emerald-950/40 text-emerald-700 dark:text-emerald-300 rounded-full text-xs font-bold border border-emerald-200 dark:border-emerald-800 mb-3">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>● Auto-Update ON - Last checked: <span id="homeAutoUpdateTime">Today</span></span>
              <span class="text-slate-300">•</span>
              <span id="homeScamCountBadge">300+ Verified Scams</span>
            </div>''',
    content
)

# 5. Trending searches row below checker or ticker:
trending_html = '''
        <!-- AUTO TRENDING SEARCHES TICKER (Feature) -->
        <div class="mt-4 flex flex-wrap items-center justify-center gap-2 text-xs">
          <span class="font-extrabold text-navy dark:text-white flex items-center gap-1">🔥 <span data-i18n="trendingLabel">Trending Searches:</span></span>
          <div id="trendingSearchesGroup" class="flex flex-wrap gap-1.5">
            <button onclick="quickSearchCheck('USPS: Your package cannot be delivered due to incomplete street address. Please update: https://usps-redeliver-track.top')" class="px-2.5 py-1 rounded-full bg-white dark:bg-black/20 border border-slate-200 dark:border-white/10 hover:border-vgreen text-slate-700 dark:text-slate-300 text-[11px] font-semibold transition">📦 USPS Parcel Smishing</button>
            <button onclick="quickSearchCheck('Police Cyber Crime: A parcel with drugs in your name was seized. You are placed under Digital Arrest on Skype right now.')" class="px-2.5 py-1 rounded-full bg-white dark:bg-black/20 border border-slate-200 dark:border-white/10 hover:border-vgreen text-slate-700 dark:text-slate-300 text-[11px] font-semibold transition">👮 Digital Arrest</button>
            <button onclick="quickSearchCheck('Emergency: I lost my wallet abroad, send $2,500 immediately to this account. Don not call me, signal is bad.')" class="px-2.5 py-1 rounded-full bg-white dark:bg-black/20 border border-slate-200 dark:border-white/10 hover:border-vgreen text-slate-700 dark:text-slate-300 text-[11px] font-semibold transition">🎙️ AI Voice Clone</button>
            <button onclick="quickSearchCheck('Electricity Notice: Your power will be disconnected at 9:30 PM tonight due to unpaid bill. Call officer 9811XXXXXX immediately.')" class="px-2.5 py-1 rounded-full bg-white dark:bg-black/20 border border-slate-200 dark:border-white/10 hover:border-vgreen text-slate-700 dark:text-slate-300 text-[11px] font-semibold transition">⚡ Electricity Disconnect</button>
            <button onclick="quickSearchCheck('YouTube Partner: Earn Rs 50 for every video like and subscribe! Contact HR manager on Telegram @Task_VIP to start.')" class="px-2.5 py-1 rounded-full bg-white dark:bg-black/20 border border-slate-200 dark:border-white/10 hover:border-vgreen text-slate-700 dark:text-slate-300 text-[11px] font-semibold transition">💼 Telegram Job Task</button>
          </div>
        </div>
'''

if 'id="trendingSearchesGroup"' not in content:
    # insert before </section> of checker
    content = content.replace('</section>\n\n        <!-- RECENT CHECKS (Feature 4 - LocalStorage History) -->', trending_html + '\n        </section>\n\n        <!-- RECENT CHECKS (Feature 4 - LocalStorage History) -->')

# 6. Replace `view-scam-database` completely with Scampedia 300+ UI
scampedia_replacement = '''      <!-- ================= VIEW 2: SCAMPEDIA - WORLD SCAM DATABASE (300+ SCAMS) ================= -->
      <div id="view-scam-database" class="view-section hidden">
        <div class="bg-white dark:bg-[#0E1E38] rounded-[24px] p-6 sm:p-10 card3d mt-4 border border-slate-100 dark:border-white/10 space-y-8">
          <!-- Breadcrumb -->
          <nav class="text-xs text-slate-400 font-bold flex items-center gap-1.5" aria-label="Breadcrumb">
            <a href="#top" onclick="showView('home')" class="hover:text-vgreen">Home</a>
            <span>›</span>
            <span class="text-navy dark:text-emerald-400">Scampedia - World Scam Database (300+ Scams)</span>
          </nav>

          <!-- Header -->
          <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 pb-6 border-b border-slate-100 dark:border-white/10">
            <div>
              <span class="inline-flex items-center gap-1.5 text-xs font-extrabold tracking-widest text-vgreen uppercase bg-emerald-50 dark:bg-emerald-950/40 px-3 py-1 rounded-full border border-emerald-200 dark:border-emerald-800">
                <span>🛡️</span> <span>WORLD SCAMPEDIA • 300+ VERIFIED SCAMS ARCHIVE</span>
              </span>
              <h1 class="text-2xl sm:text-4xl font-extrabold text-navy dark:text-white mt-2.5">
                Scampedia <span class="text-vgreen">(300+ World Scams Database)</span>
              </h1>
              <p class="text-slate-500 dark:text-slate-400 mt-2 text-xs sm:text-sm max-w-[820px] leading-relaxed">
                The ultimate global encyclopedia of online fraud, imposter calls, investment traps, smishing, romance sextortion, and classic confidence tricks. Sourced from <b>Wikipedia</b>, <b>FBI IC3</b>, <b>FTC</b>, <b>Action Fraud (UK)</b>, <b>I4C / Cybercrime.gov.in (India)</b>, <b>Scamwatch (Australia)</b>, <b>CAFC (Canada)</b>, and <b>Interpol</b>.
              </p>
            </div>
            <div class="flex flex-wrap items-center gap-2.5 shrink-0">
              <button onclick="openAddMissingScamModal()" class="bg-[#0A1931] hover:bg-[#12284C] text-white font-extrabold text-xs px-5 py-3 rounded-full transition shadow-md border border-white/20 flex items-center gap-1.5">
                <span>➕</span> <span>Add Missing Scam</span>
              </button>
              <button onclick="showView('home')" class="bg-vgreen hover:bg-vgreenDark text-white font-extrabold text-xs px-5 py-3 rounded-full transition shadow-md">
                ⚡ Test in Scanner
              </button>
            </div>
          </div>

          <!-- Real-Time Counter & Live Auto-Update Badge -->
          <div class="flex flex-wrap items-center justify-between gap-3 p-3.5 rounded-2xl bg-emerald-50/80 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-900/40 text-xs font-bold text-emerald-900 dark:text-emerald-300">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              <span>Showing <span id="dbFilterCount" class="font-extrabold text-base text-navy dark:text-white">303</span> Scams</span>
              <span class="text-slate-300">•</span>
              <span>● Auto-Update ON - Last checked: <span id="dbAutoUpdateTime">Today</span></span>
            </div>
            <div class="flex items-center gap-3 text-[11px] text-emerald-800 dark:text-emerald-300/80">
              <span>📚 10 World Categories</span>
              <span>•</span>
              <span>🌐 Sources: Wikipedia, FBI IC3, FTC, Action Fraud, I4C India, Scamwatch</span>
            </div>
          </div>

          <!-- 10 CATEGORY CARDS GRID ON TOP (Feature 1 of Scampedia) -->
          <div>
            <div class="flex items-center justify-between mb-3">
              <h2 class="text-sm font-extrabold uppercase tracking-wider text-slate-400 flex items-center gap-1.5">
                <span>🏷️</span> <span>Browse by Category (10 Major Threat Domains):</span>
              </h2>
              <span class="text-xs text-vgreen font-bold">Click any category to filter</span>
            </div>
            <div id="scampediaCategoriesGrid" class="grid grid-cols-2 sm:grid-cols-5 gap-3">
              <!-- Rendered by renderScampediaCategories() -->
            </div>
          </div>

          <!-- AUTO SCAM OF THE DAY BANNER (Feature 4 of Auto-Update) -->
          <div id="scamOfTheDayCard" class="p-4 sm:p-5 rounded-2xl bg-gradient-to-r from-[#0A1931] via-[#122F5A] to-[#009624] text-white card3d shadow-lg border border-white/10 relative overflow-hidden">
            <!-- Rendered by renderScamOfTheDay() -->
          </div>

          <!-- SEARCH BAR -->
          <div>
            <div class="relative">
              <input
                id="dbSearchInput"
                type="text"
                placeholder="Search All 300+ Scams - e.g. Parcel, Ponzi, AI Voice, Digital Arrest, WhatsApp Pink, Task Job, Quishing, Loan App..."
                oninput="filterScamsDatabase()"
                class="w-full pl-11 pr-24 py-3.5 rounded-2xl border border-slate-200 dark:border-white/10 bg-[#FBFFFC] dark:bg-black/25 text-xs sm:text-sm text-navy dark:text-white font-medium focus:border-vgreen outline-none shadow-sm"
              />
              <span class="absolute left-4 top-3.5 text-base text-slate-400">🔍</span>
              <button
                onclick="clearDbFilters()"
                class="absolute right-3 top-2.5 bg-slate-100 hover:bg-slate-200 dark:bg-white/10 dark:hover:bg-white/20 text-slate-600 dark:text-slate-300 text-xs font-bold px-3 py-1.5 rounded-xl transition"
              >
                Reset
              </button>
            </div>
          </div>

          <!-- FILTER BARS (Source, Year, Country, Category) -->
          <div class="space-y-3.5">
            <!-- Filter 1: By Source (New Requirement) -->
            <div class="flex flex-col sm:flex-row sm:items-center gap-2 text-xs">
              <span class="font-extrabold text-navy dark:text-white min-w-[75px] shrink-0">🏛️ Source:</span>
              <div id="sourceFilterGroup" class="flex flex-wrap gap-1.5">
                <button onclick="setDbSourceFilter('all', this)" class="db-filter-source active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition">All Sources</button>
                <button onclick="setDbSourceFilter('Wikipedia', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">Wikipedia</button>
                <button onclick="setDbSourceFilter('FBI IC3', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">FBI IC3 (USA)</button>
                <button onclick="setDbSourceFilter('FTC', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">FTC (USA)</button>
                <button onclick="setDbSourceFilter('Action Fraud', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">Action Fraud (UK)</button>
                <button onclick="setDbSourceFilter('I4C India', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">I4C / Cybercrime.gov.in</button>
                <button onclick="setDbSourceFilter('Scamwatch', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">Scamwatch (Australia)</button>
                <button onclick="setDbSourceFilter('Canadian Anti-Fraud Centre', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">CAFC (Canada)</button>
                <button onclick="setDbSourceFilter('Interpol', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">Interpol / Europol</button>
                <button onclick="setDbSourceFilter('Google News', this)" class="db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">Google News (2026)</button>
              </div>
            </div>

            <!-- Filter 2: By Year -->
            <div class="flex flex-col sm:flex-row sm:items-center gap-2 text-xs">
              <span class="font-extrabold text-navy dark:text-white min-w-[75px] shrink-0">📅 Year:</span>
              <div id="yearFilterGroup" class="flex flex-wrap gap-1.5">
                <button onclick="setDbYearFilter('all', this)" class="db-filter-year active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition">All Years</button>
                <button onclick="setDbYearFilter('2026', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-red-500 bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300 text-[11px] transition">2026 (🔴 Latest)</button>
                <button onclick="setDbYearFilter('2025', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2025</button>
                <button onclick="setDbYearFilter('2024', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2024</button>
                <button onclick="setDbYearFilter('2023', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2023</button>
                <button onclick="setDbYearFilter('2022', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2022</button>
                <button onclick="setDbYearFilter('2021', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2021</button>
                <button onclick="setDbYearFilter('2020', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2020</button>
                <button onclick="setDbYearFilter('2019', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2019</button>
                <button onclick="setDbYearFilter('2018', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2018</button>
                <button onclick="setDbYearFilter('2017', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">2017</button>
                <button onclick="setDbYearFilter('Classic', this)" class="db-filter-year px-3 py-1.5 rounded-full font-bold border border-amber-500 bg-amber-50 text-amber-800 dark:bg-amber-950 dark:text-amber-300 text-[11px] transition">Classic (Wikipedia)</button>
              </div>
            </div>

            <!-- Filter 3: By Country -->
            <div class="flex flex-col sm:flex-row sm:items-center gap-2 text-xs">
              <span class="font-extrabold text-navy dark:text-white min-w-[75px] shrink-0">🌍 Country:</span>
              <div id="countryFilterGroup" class="flex flex-wrap gap-1.5">
                <button onclick="setDbCountryFilter('all', this)" class="db-filter-country active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition">All Countries</button>
                <button onclick="setDbCountryFilter('India', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇮🇳 India</button>
                <button onclick="setDbCountryFilter('USA', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇺🇸 USA</button>
                <button onclick="setDbCountryFilter('UK', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇬🇧 UK</button>
                <button onclick="setDbCountryFilter('Australia', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇦🇺 Australia</button>
                <button onclick="setDbCountryFilter('Canada', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇨🇦 Canada</button>
                <button onclick="setDbCountryFilter('Pakistan', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇵🇰 Pakistan</button>
                <button onclick="setDbCountryFilter('UAE', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🇦🇪 UAE</button>
                <button onclick="setDbCountryFilter('Global', this)" class="db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition">🌐 Global</button>
              </div>
            </div>
          </div>

          <!-- View Mode Switcher: Cards Grid vs Timeline -->
          <div class="pt-4 border-t border-slate-100 dark:border-white/10 flex flex-wrap items-center justify-between gap-3">
            <div class="flex items-center gap-2">
              <span class="text-xs font-bold text-slate-400">View Mode:</span>
              <div class="inline-flex p-1 rounded-xl bg-slate-100 dark:bg-black/30 border border-slate-200 dark:border-white/10 text-xs font-bold">
                <button id="viewModeGridBtn" onclick="setDbViewMode('grid')" class="px-3 py-1 rounded-lg bg-white dark:bg-navy text-navy dark:text-white shadow-sm transition">Grid Cards</button>
                <button id="viewModeTimelineBtn" onclick="setDbViewMode('timeline')" class="px-3 py-1 rounded-lg text-slate-600 dark:text-slate-400 hover:text-navy dark:hover:text-white transition">Timeline View</button>
              </div>
            </div>
            <div class="text-xs text-slate-500 dark:text-slate-400 font-medium">
              Click any card to inspect full Wikipedia-style Infobox, Red Flags & Helplines.
            </div>
          </div>

          <!-- DYNAMIC SCAM CARDS / TIMELINE CONTAINER -->
          <div id="dbCardsContainer" class="mt-6">
            <!-- Rendered by renderScamDatabase() -->
          </div>

          <!-- PAGINATION CONTAINER (Feature: Fast rendering 30 at a time) -->
          <div id="dbPaginationContainer" class="text-center pt-4">
            <button id="dbLoadMoreBtn" onclick="loadMoreScams()" class="bg-[#0A1931] hover:bg-[#12284C] text-white font-extrabold text-xs sm:text-sm px-8 py-3.5 rounded-full shadow-lg border border-vgreen transition transform hover:-translate-y-0.5">
              <span>Load More Scams (30 more) ↓</span>
            </button>
          </div>

          <!-- EMPTY STATE (Hidden by default) -->
          <div id="dbEmptyState" class="hidden text-center py-12 px-4 rounded-2xl bg-slate-50 dark:bg-black/20 border border-slate-200 dark:border-white/10 my-6">
            <span class="text-4xl">🔍</span>
            <h3 class="text-lg font-extrabold text-navy dark:text-white mt-3">No Scams Match Your Current Filters</h3>
            <p class="text-xs text-slate-500 dark:text-slate-400 mt-1 max-w-[460px] mx-auto">Try clearing your search query or selecting "All Sources" / "All Years".</p>
            <button onclick="clearDbFilters()" class="mt-4 bg-vgreen hover:bg-vgreenDark text-white font-extrabold text-xs px-5 py-2.5 rounded-full transition">Reset All Filters</button>
          </div>

          <!-- SOURCE ATTRIBUTION DISCLAIMER (Must mention sources in Scampedia) -->
          <div class="p-4 rounded-2xl bg-emerald-50/80 dark:bg-emerald-950/20 border border-emerald-200 dark:border-emerald-900/30 text-center text-xs text-emerald-900 dark:text-emerald-300 font-medium">
            Sources: <b>Wikipedia</b>, <b>FBI IC3</b>, <b>FTC</b>, <b>Action Fraud</b>, <b>I4C India</b>, <b>Scamwatch</b> - For education and threat intelligence only.
          </div>

          <!-- Footer Action Navigation -->
          <div class="pt-6 border-t border-slate-100 dark:border-white/10 flex flex-col sm:flex-row items-center justify-between gap-4">
            <button onclick="showView('home')" class="bg-vgreen hover:bg-vgreenDark text-white font-bold px-6 py-3 rounded-full text-xs sm:text-sm transition flex items-center gap-2">
              <span>← Back to Main Scam Checker</span>
            </button>
            <div class="text-xs text-slate-400">
              Need to test a custom message? Paste in our scanner anytime for free.
            </div>
          </div>
        </div>
      </div>'''

# Replace from line `<div id="view-scam-database"` to the next view section
old_scam_db_pattern = r'<!-- ================= VIEW 2: SCAM DATABASE.*?<div id="view-scam-database".*?</div>\s*</div>\s*(?=<!-- ================= VIEW 3: BLOG)'
content = re.sub(old_scam_db_pattern, scampedia_replacement + '\n\n', content, flags=re.DOTALL)

# 7. Add Admin view right before footer
admin_view_html = '''
      <!-- ================= VIEW: ADMIN DASHBOARD (THREAT INTEL & USER REPORTS) ================= -->
      <div id="view-admin" class="view-section hidden">
        <div class="bg-white dark:bg-[#0E1E38] rounded-[24px] p-6 sm:p-10 card3d mt-4 border border-slate-100 dark:border-white/10 space-y-8">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-100 dark:border-white/10">
            <div>
              <span class="inline-flex items-center gap-1.5 text-xs font-extrabold tracking-widest text-vgreen uppercase bg-emerald-50 dark:bg-emerald-950/40 px-3 py-1 rounded-full border border-emerald-200 dark:border-emerald-800">
                ⚙️ THREAT INTELLIGENCE & COMMUNITY ADMIN
              </span>
              <h1 class="text-2xl sm:text-3xl font-extrabold text-navy dark:text-white mt-2">
                Admin Threat Feed & Database Manager
              </h1>
              <p class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1">
                Monitor live threat updates, inspect user submissions, export intelligence datasets, and verify auto-moderation.
              </p>
            </div>
            <div class="flex flex-wrap items-center gap-2">
              <button onclick="exportScamsJson()" class="bg-[#0A1931] hover:bg-[#12284C] text-white text-xs font-bold px-4 py-2.5 rounded-xl border border-white/20 transition flex items-center gap-1.5 shadow-sm">
                <span>📥 Export Scams as JSON</span>
              </button>
            </div>
          </div>

          <!-- Quick Metrics Cards -->
          <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="p-4 rounded-2xl bg-emerald-50 dark:bg-emerald-950/30 border border-emerald-200 dark:border-emerald-800">
              <div class="text-xs font-bold text-emerald-800 dark:text-emerald-300">Total Scams in Database</div>
              <div id="adminTotalScams" class="text-2xl sm:text-3xl font-extrabold text-navy dark:text-white mt-1">303</div>
              <div class="text-[10px] text-emerald-700 dark:text-emerald-400 mt-1 font-semibold">10 Global Categories</div>
            </div>
            <div class="p-4 rounded-2xl bg-blue-50 dark:bg-blue-950/30 border border-blue-200 dark:border-blue-800">
              <div class="text-xs font-bold text-blue-800 dark:text-blue-300">User Community Reports</div>
              <div id="adminUserReportsCount" class="text-2xl sm:text-3xl font-extrabold text-navy dark:text-white mt-1">0</div>
              <div class="text-[10px] text-blue-700 dark:text-blue-400 mt-1 font-semibold">Auto-Moderated & Safe</div>
            </div>
            <div class="p-4 rounded-2xl bg-purple-50 dark:bg-purple-950/30 border border-purple-200 dark:border-purple-800">
              <div class="text-xs font-bold text-purple-800 dark:text-purple-300">Auto-Update Engine</div>
              <div class="text-lg sm:text-xl font-extrabold text-emerald-600 dark:text-emerald-400 mt-1 flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                <span>Active (6h)</span>
              </div>
              <div id="adminLastCheckedTime" class="text-[10px] text-purple-700 dark:text-purple-400 mt-1 font-semibold">Today</div>
            </div>
            <div class="p-4 rounded-2xl bg-amber-50 dark:bg-amber-950/30 border border-amber-200 dark:border-amber-800">
              <div class="text-xs font-bold text-amber-800 dark:text-amber-300">Official Sources</div>
              <div class="text-2xl sm:text-3xl font-extrabold text-navy dark:text-white mt-1">9</div>
              <div class="text-[10px] text-amber-700 dark:text-amber-400 mt-1 font-semibold">Wikipedia, FBI, FTC, I4C, etc.</div>
            </div>
          </div>

          <!-- User-Submitted Scams Table -->
          <div class="bg-slate-50 dark:bg-black/25 rounded-2xl p-5 border border-slate-200 dark:border-white/10 space-y-4">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <h3 class="font-extrabold text-navy dark:text-white text-base flex items-center gap-2">
                <span>👥</span> <span>User Submitted Reports (LocalStorage & Community)</span>
              </h3>
              <button onclick="clearUserReports()" class="text-xs font-bold text-red-600 hover:text-red-700 bg-red-100 hover:bg-red-200 dark:bg-red-950 dark:text-red-300 px-3 py-1.5 rounded-xl transition">
                🗑️ Clear All User Reports
              </button>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full text-left text-xs">
                <thead>
                  <tr class="border-b border-slate-200 dark:border-white/10 text-slate-400">
                    <th class="py-2.5 px-3">Scam Name</th>
                    <th class="py-2.5 px-3">Category</th>
                    <th class="py-2.5 px-3">City / Country</th>
                    <th class="py-2.5 px-3">Sample Text</th>
                    <th class="py-2.5 px-3">Status</th>
                  </tr>
                </thead>
                <tbody id="adminUserReportsTable">
                  <tr>
                    <td colspan="5" class="py-6 text-center text-slate-400 italic">No user reports yet. Test the "Add Missing Scam" form in Scampedia!</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Live Threat Feed Log -->
          <div class="bg-slate-50 dark:bg-black/25 rounded-2xl p-5 border border-slate-200 dark:border-white/10 space-y-4">
            <div class="flex items-center justify-between flex-wrap gap-2">
              <h3 class="font-extrabold text-navy dark:text-white text-base flex items-center gap-2">
                <span>📡</span> <span>Latest Threat Feed Log (Google News & FTC RSS Cache)</span>
              </h3>
              <button onclick="fetchLiveScamFeeds(true)" class="text-xs font-bold text-vgreen hover:underline">
                🔄 Force Refresh RSS
              </button>
            </div>
            <div id="adminLiveFeedsLog" class="space-y-2.5 text-xs">
              <!-- Rendered by renderAdminLiveFeeds() -->
            </div>
          </div>
        </div>
      </div>
'''

if 'id="view-admin"' not in content:
    content = content.replace('    <!-- FOOTER WITH EEAT & OFFICIAL EMAIL -->', admin_view_html + '\n    <!-- FOOTER WITH EEAT & OFFICIAL EMAIL -->')

# 8. Add link to Admin Dashboard in footer
admin_footer_link = '<a href="#admin" onclick="showView(\'admin\')" class="hover:underline text-slate-400">Admin (Threat Intel)</a>'
if 'showView(\'admin\')' not in content:
    content = content.replace(
        '<a href="#backlink-outreach" onclick="showView(\'backlink-outreach\')" class="hover:underline text-emerald-300 font-bold">Media Kit & Outreach</a>',
        '<a href="#backlink-outreach" onclick="showView(\'backlink-outreach\')" class="hover:underline text-emerald-300 font-bold">Media Kit & Outreach</a>\n            ' + admin_footer_link
    )

# 9. Add `#addMissingScamModal` right before `</body>` or next to `addToHomeModal`
add_scam_modal_html = '''  <!-- ================= ADD MISSING SCAM MODAL (Feature for Scampedia Community) ================= -->
  <div id="addMissingScamModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 bg-black/75 backdrop-blur-md overflow-y-auto" onclick="onAddScamBackdropClick(event)">
    <div class="bg-white dark:bg-[#0A1931] text-navy dark:text-white rounded-[28px] max-w-lg w-full p-6 sm:p-8 card3d shadow-2xl border border-slate-200 dark:border-white/10 relative my-auto">
      <button onclick="closeAddMissingScamModal()" class="absolute top-5 right-5 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 dark:bg-white/10 text-slate-500 hover:text-black dark:hover:text-white flex items-center justify-center font-bold text-sm transition">✕</button>
      
      <div class="flex items-center gap-3 mb-4">
        <span class="w-10 h-10 rounded-2xl bg-vgreen text-white text-xl grid place-items-center shadow-md">✍️</span>
        <div>
          <h3 class="text-xl font-extrabold text-navy dark:text-white">Add Missing Scam to Scampedia</h3>
          <p class="text-xs text-slate-500 dark:text-slate-400">Help the global community. Your scam will appear instantly.</p>
        </div>
      </div>

      <form onsubmit="submitMissingScam(event)" class="space-y-3.5 text-xs">
        <div>
          <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Scam Name *</label>
          <input type="text" id="addScamName" required placeholder="e.g. Electricity Bill Disconnection Tonight" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen" />
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Category *</label>
            <select id="addScamCategory" required class="w-full px-3 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen">
              <option value="Message">📩 Phishing / Message</option>
              <option value="Call">📞 Call / Impersonation</option>
              <option value="Investment">🪙 Investment & Crypto</option>
              <option value="Job">💼 Job & Employment</option>
              <option value="Romance">💔 Romance & Sextortion</option>
              <option value="Shop">🛒 Shopping & Order</option>
              <option value="Govt">🏛️ Govt & Subsidy</option>
              <option value="Banking">🏦 Banking & UPI</option>
              <option value="Tech">💻 Ransomware / Tech</option>
              <option value="Classic">🎭 Classic / Confidence Trick</option>
            </select>
          </div>
          <div>
            <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">City / Country *</label>
            <input type="text" id="addScamCountry" required placeholder="e.g. Mumbai, India / Global" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen" />
          </div>
        </div>

        <div>
          <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Short Description *</label>
          <textarea id="addScamDesc" rows="2" required placeholder="Explain in 1-2 lines what the fraudsters do..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen"></textarea>
        </div>

        <div>
          <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Sample Message / Link *</label>
          <textarea id="addScamSample" rows="2" required placeholder="Paste sample message text or phone script here (Do not include real OTPs or passwords)..." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen"></textarea>
        </div>

        <div>
          <label class="block font-bold text-slate-700 dark:text-slate-300 mb-1">Your Name / First Name (Optional)</label>
          <input type="text" id="addScamAuthor" placeholder="e.g. Anonymous / Rahul" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-200 dark:border-white/10 bg-slate-50 dark:bg-black/25 text-navy dark:text-white font-medium outline-none focus:border-vgreen" />
        </div>

        <div class="p-3 rounded-xl bg-amber-50 dark:bg-amber-950/20 border border-amber-200 dark:border-amber-900/40 text-[11px] text-amber-900 dark:text-amber-300">
          🛡️ <b>Automated Safety Filter Active:</b> Submissions containing credit card numbers, OTPs, or abusive words will be automatically rejected.
        </div>

        <button type="submit" class="w-full bg-vgreen hover:bg-vgreenDark text-white font-extrabold py-3 rounded-xl transition shadow-md flex items-center justify-center gap-2">
          <span>🚀 Add to Scampedia & Publish</span>
        </button>
      </form>
    </div>
  </div>'''

if 'id="addMissingScamModal"' not in content:
    content = content.replace('  <!-- ADD TO HOME SCREEN / APP MODAL (Feature 8) -->', add_scam_modal_html + '\n\n  <!-- ADD TO HOME SCREEN / APP MODAL (Feature 8) -->')

# 10. Update scamDetailModal with Wikipedia Infobox & Australia Helpline & Sources Note
infobox_modal_header = '''      <!-- Modal Header with Wikipedia-style Infobox -->
      <div class="flex items-start gap-4 pr-8">
        <span id="modalScamIcon" class="text-3xl sm:text-4xl shrink-0 p-3 rounded-2xl bg-slate-50 dark:bg-black/30 border border-slate-200 dark:border-white/10">🎙️</span>
        <div>
          <div class="flex items-center gap-2 flex-wrap mb-1.5">
            <span id="modalScamYear" class="px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-red-600 text-white">2026</span>
            <span id="modalScamCountry" class="px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-navy text-white">Global</span>
            <span id="modalScamCategory" class="px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-slate-100 dark:bg-white/10 text-slate-700 dark:text-slate-300">Call</span>
            <span id="modalScamSource" class="px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300">Source: FBI IC3</span>
            <span id="modalScamScore" class="px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300">Score: 98/100</span>
          </div>
          <h2 id="modalScamTitle" class="text-xl sm:text-2xl font-extrabold text-navy dark:text-white leading-tight">
            AI Voice Clone / Deepfake Boss Call
          </h2>
          <p id="modalScamDesc" class="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-1"></p>
        </div>
      </div>'''

content = re.sub(
    r'<!-- Modal Header -->\s*<div class="flex items-start gap-4 pr-8">.*?<h2 id="modalScamTitle".*?</h2>\s*<p id="modalScamDesc".*?</p>\s*</div>\s*</div>',
    infobox_modal_header,
    content,
    flags=re.DOTALL
)

# 11. Add Australia Scamwatch to helplines in modal if not present
helpline_addon = '''            <div class="p-2.5 rounded-xl bg-white dark:bg-black/20 border border-slate-200 dark:border-white/5 sm:col-span-2">
              <b class="text-navy dark:text-emerald-300 block">🇦🇺 Australia:</b>
              <span>Report to Scamwatch at <a href="https://scamwatch.gov.au" target="_blank" rel="noopener noreferrer" class="text-vgreen underline font-bold">scamwatch.gov.au</a> (National Anti-Scam Centre)</span>
            </div>
            <div class="sm:col-span-2 pt-2 text-[11px] text-slate-400 dark:text-slate-500 italic text-center">
              Sources: Wikipedia, FBI IC3, FTC, Action Fraud, I4C India, Scamwatch - For education only.
            </div>'''

if 'scamwatch.gov.au' not in content:
    content = content.replace(
        '<span>Dubai Police <a href="https://ecrime.ae" target="_blank" rel="noopener noreferrer" class="text-vgreen underline">ecrime.ae</a> or dial 901 for non-emergencies</span>\n            </div>',
        '<span>Dubai Police <a href="https://ecrime.ae" target="_blank" rel="noopener noreferrer" class="text-vgreen underline">ecrime.ae</a> or dial 901 for non-emergencies</span>\n            </div>\n' + helpline_addon
    )

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML structural replacement completed successfully.")
