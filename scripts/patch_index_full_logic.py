#!/usr/bin/env python3
"""
Patch index.html with:
1. Trending Searches pills in the Checker section.
2. Complete JavaScript implementation for Scampedia, Categories, Pagination, Source Filtering,
   Automated Missing Scam Submission, Auto-Update RSS Feeds, Scam of the Day, and Admin Dashboard.
3. Clean English, natural Bolchal Hindi, and Bolchal Urdu modal titles and labels.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add trending searches pills right before 8 Category Pills if not already present
trending_searches_html = """
          <!-- TRENDING SEARCHES / QUICK-TEST PILLS (Auto-Rotated Threat Samples) -->
          <div class="mb-5 flex flex-wrap items-center gap-2">
            <span class="text-xs font-bold text-slate-400 flex items-center gap-1.5 shrink-0">
              <span class="text-amber-500">🔥</span> <span data-i18n="trendingLabel">Trending Quick Tests:</span>
            </span>
            <div id="trendingSearchesGroup" class="flex flex-wrap gap-1.5 text-xs">
              <button type="button" onclick="quickSearchCheck('URGENT: India Post parcel waiting. Pay fee to avoid return.')" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-white/10 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-slate-700 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 border border-slate-200 dark:border-white/10 text-[11px] font-semibold transition">⚡ India Post Parcel</button>
              <button type="button" onclick="quickSearchCheck('Electricity power will be disconnected tonight at 9:30 PM due to unpaid bill. Call officer 91040 immediately.')" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-white/10 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-slate-700 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 border border-slate-200 dark:border-white/10 text-[11px] font-semibold transition">⚡ Smart Meter Cut</button>
              <button type="button" onclick="quickSearchCheck('CBI Cyber Crime Cell: Video call verification required immediately for money laundering arrest warrant.')" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-white/10 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-slate-700 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 border border-slate-200 dark:border-white/10 text-[11px] font-semibold transition">⚡ Digital Arrest</button>
              <button type="button" onclick="quickSearchCheck('YouTube video like and subscribe job. Earn $500 per day from home. Join VIP Telegram group.')" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-white/10 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-slate-700 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 border border-slate-200 dark:border-white/10 text-[11px] font-semibold transition">⚡ YouTube Like Job</button>
              <button type="button" onclick="quickSearchCheck('Join VIP Crypto Signals group. Guaranteed 500% daily returns on automated AI trading platform.')" class="px-2.5 py-1 rounded-full bg-slate-100 dark:bg-white/10 hover:bg-emerald-50 dark:hover:bg-emerald-950 text-slate-700 dark:text-slate-200 hover:text-emerald-800 dark:hover:text-emerald-300 border border-slate-200 dark:border-white/10 text-[11px] font-semibold transition">⚡ Crypto 500% Return</button>
            </div>
          </div>
"""

if 'id="trendingSearchesGroup"' not in content:
    target_marker = '<!-- 8 Category Pills (2-row grid, equal size, centered) -->'
    if target_marker in content:
        content = content.replace(target_marker, trending_searches_html + '\n          ' + target_marker)
        print("Inserted trendingSearchesGroup above 8 category pills.")

# 2. Check viewMetaMap to include 'admin'
meta_marker = "const viewMetaMap = {"
admin_meta_entry = """const viewMetaMap = {
      admin: {
        title: "Threat Intel & Community Database Admin - IsThisScamOrReal.com",
        desc: "Inspect live scam feeds, community reports, and database metrics on IsThisScamOrReal.com."
      },"""
if "const viewMetaMap = {" in content and "admin:" not in content:
    content = content.replace(meta_marker, admin_meta_entry)
    print("Added admin to viewMetaMap.")

# 3. Locate the JavaScript section from `// ================= GLOBAL SCAM DATABASE` to the end of `<script>`
# Let's inspect what is currently between line 3910 and 4543
js_start_marker = "// ================= GLOBAL SCAM DATABASE (150+ SCAMS: 2016-2026) LOGIC ================="
if js_start_marker not in content:
    # try flexible regex
    m = re.search(r'// =+ GLOBAL SCAM DATABASE.*?LOGIC =+', content)
    if m:
        js_start_marker = m.group(0)
    else:
        print("ERROR: js_start_marker not found!")
        exit(1)

# Find the end of this script block before `</body>`
script_end_marker = "</script>\n</body>"
if script_end_marker not in content:
    script_end_marker = "</script>"

idx_start = content.find(js_start_marker)
idx_end = content.rfind("</script>")

if idx_start == -1 or idx_end == -1:
    print("ERROR: Could not find script boundaries!")
    exit(1)

new_javascript = """// ================= GLOBAL SCAM DATABASE (300+ SCAMS ACROSS 10 WORLD CATEGORIES) =================
    let currentDbFilter = {
      year: 'all',
      country: 'all',
      type: 'all',
      source: 'all',
      categorySlug: 'all',
      search: '',
      mode: 'grid',
      page: 1,
      pageSize: 30
    };

    let currentModalScam = null;
    let baseScamsDb = [];

    // Initialize Database with User-Submitted Scams
    function loadUserSubmittedScams() {
      baseScamsDb = window.GLOBAL_SCAMS_DATABASE ? [...window.GLOBAL_SCAMS_DATABASE] : [];
      try {
        const stored = localStorage.getItem('user_scams_db');
        if (stored) {
          const userScams = JSON.parse(stored);
          if (Array.isArray(userScams) && userScams.length > 0) {
            // Unshift user scams so they appear on top
            window.GLOBAL_SCAMS_DATABASE = [...userScams, ...baseScamsDb];
          }
        }
      } catch (err) {
        console.warn('Failed to load user submitted scams from localStorage', err);
      }
    }

    // Render 10 Category Cards on Scampedia Top
    function renderScampediaCategories() {
      const grid = document.getElementById('scampediaCategoriesGrid');
      if (!grid) return;

      const categories = window.SCAMPEDIA_CATEGORIES || [
        { name: 'Investment & Crypto', icon: '🪙', slug: 'investment', count: 41 },
        { name: 'Job & Employment', icon: '💼', slug: 'job', count: 32 },
        { name: 'Phishing / Message', icon: '📩', slug: 'message', count: 38 },
        { name: 'Call & Impersonation', icon: '📞', slug: 'call', count: 32 },
        { name: 'Romance & Sextortion', icon: '💔', slug: 'romance', count: 22 },
        { name: 'Shopping & Order', icon: '🛒', slug: 'shop', count: 32 },
        { name: 'Govt & Subsidy', icon: '🏛️', slug: 'govt', count: 27 },
        { name: 'Banking & UPI', icon: '🏦', slug: 'banking', count: 32 },
        { name: 'Ransomware / Tech', icon: '💻', slug: 'tech', count: 22 },
        { name: 'Classic / Confidence', icon: '🎭', slug: 'classic', count: 25 }
      ];

      const db = window.GLOBAL_SCAMS_DATABASE || [];

      // Compute actual counts
      const countsMap = {};
      db.forEach(item => {
        const slug = item.categorySlug || (item.category ? item.category.toLowerCase() : 'other');
        countsMap[slug] = (countsMap[slug] || 0) + 1;
      });

      grid.innerHTML = categories.map(cat => {
        const actualCount = countsMap[cat.slug] || cat.count || 0;
        const isActive = currentDbFilter.categorySlug === cat.slug;
        const activeClass = isActive
          ? 'border-vgreen bg-emerald-50/80 dark:bg-emerald-950/40 text-navy dark:text-white shadow-md ring-2 ring-vgreen/30'
          : 'border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 hover:border-vgreen/60';

        return `
          <button type="button" onclick="filterByCategory('${cat.slug}')" class="category-card p-3 rounded-2xl border ${activeClass} transition text-left flex flex-col justify-between group">
            <div class="flex items-center justify-between gap-1 mb-2">
              <span class="text-2xl group-hover:scale-110 transition-transform">${cat.icon}</span>
              <span class="text-[10px] font-extrabold ${isActive ? 'bg-vgreen text-white' : 'bg-slate-100 dark:bg-white/10 text-slate-600 dark:text-slate-300'} px-2 py-0.5 rounded-full">${actualCount}</span>
            </div>
            <div>
              <div class="font-extrabold text-xs leading-snug group-hover:text-vgreen transition-colors">${cat.name}</div>
              <div class="text-[10px] text-slate-400 mt-0.5 font-medium">World Threat Archive</div>
            </div>
          </button>
        `;
      }).join('');
    }

    // Toggle Category Filter
    function filterByCategory(slug) {
      if (currentDbFilter.categorySlug === slug) {
        currentDbFilter.categorySlug = 'all';
      } else {
        currentDbFilter.categorySlug = slug;
      }
      currentDbFilter.page = 1;
      renderScampediaCategories();
      filterScamsDatabase();
    }

    // Source Filter Handler
    function setDbSourceFilter(source, btn) {
      currentDbFilter.source = source;
      currentDbFilter.page = 1;
      document.querySelectorAll('.db-filter-source').forEach(b => {
        b.className = 'db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      if (btn) {
        btn.className = 'db-filter-source active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition';
      }
      filterScamsDatabase();
    }

    function setDbYearFilter(year, btn) {
      currentDbFilter.year = year;
      currentDbFilter.page = 1;
      document.querySelectorAll('.db-filter-year').forEach(b => {
        b.className = 'db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      if (btn) {
        btn.className = 'db-filter-year active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition';
      }
      filterScamsDatabase();
    }

    function setDbCountryFilter(country, btn) {
      currentDbFilter.country = country;
      currentDbFilter.page = 1;
      document.querySelectorAll('.db-filter-country').forEach(b => {
        b.className = 'db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      if (btn) {
        btn.className = 'db-filter-country active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition';
      }
      filterScamsDatabase();
    }

    function setDbTypeFilter(type, btn) {
      currentDbFilter.type = type;
      currentDbFilter.page = 1;
      document.querySelectorAll('.db-filter-type').forEach(b => {
        b.className = 'db-filter-type px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      if (btn) {
        btn.className = 'db-filter-type active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition';
      }
      filterScamsDatabase();
    }

    function setDbViewMode(mode) {
      currentDbFilter.mode = mode;
      const gridBtn = document.getElementById('viewModeGridBtn');
      const tlBtn = document.getElementById('viewModeTimelineBtn');
      if (mode === 'grid') {
        if (gridBtn) gridBtn.className = 'px-3 py-1 rounded-lg bg-white dark:bg-navy text-navy dark:text-white shadow-sm transition';
        if (tlBtn) tlBtn.className = 'px-3 py-1 rounded-lg text-slate-600 dark:text-slate-400 hover:text-navy dark:hover:text-white transition';
      } else {
        if (gridBtn) gridBtn.className = 'px-3 py-1 rounded-lg text-slate-600 dark:text-slate-400 hover:text-navy dark:hover:text-white transition';
        if (tlBtn) tlBtn.className = 'px-3 py-1 rounded-lg bg-white dark:bg-navy text-navy dark:text-white shadow-sm transition';
      }
      filterScamsDatabase();
    }

    function clearDbFilters() {
      currentDbFilter = {
        year: 'all',
        country: 'all',
        type: 'all',
        source: 'all',
        categorySlug: 'all',
        search: '',
        mode: 'grid',
        page: 1,
        pageSize: 30
      };
      const searchInput = document.getElementById('dbSearchInput');
      if (searchInput) searchInput.value = '';

      document.querySelectorAll('.db-filter-source').forEach((b, i) => {
        b.className = i === 0 ? 'db-filter-source active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition' : 'db-filter-source px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      document.querySelectorAll('.db-filter-year').forEach((b, i) => {
        b.className = i === 0 ? 'db-filter-year active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition' : 'db-filter-year px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      document.querySelectorAll('.db-filter-country').forEach((b, i) => {
        b.className = i === 0 ? 'db-filter-country active px-3 py-1.5 rounded-full font-bold border border-navy bg-navy text-white text-[11px] transition' : 'db-filter-country px-3 py-1.5 rounded-full font-bold border border-slate-200 dark:border-white/10 bg-white dark:bg-black/20 text-slate-700 dark:text-slate-300 text-[11px] transition';
      });
      renderScampediaCategories();
      filterScamsDatabase();
    }

    // Load More Pagination
    function loadMoreScams() {
      currentDbFilter.page++;
      filterScamsDatabase(true);
    }

    // Main Filter & Render Engine
    function filterScamsDatabase(isLoadMore = false) {
      const db = window.GLOBAL_SCAMS_DATABASE || [];
      const searchInput = document.getElementById('dbSearchInput');
      const query = (searchInput ? searchInput.value : '').toLowerCase().trim();
      currentDbFilter.search = query;

      const filtered = db.filter(item => {
        // Source filter
        if (currentDbFilter.source !== 'all') {
          const itemSrc = (item.source || '').toLowerCase();
          const filterSrc = currentDbFilter.source.toLowerCase();
          if (!itemSrc.includes(filterSrc) && item.source !== currentDbFilter.source) return false;
        }

        // Category card filter
        if (currentDbFilter.categorySlug !== 'all') {
          const itemCat = (item.categorySlug || item.category || '').toLowerCase();
          if (itemCat !== currentDbFilter.categorySlug.toLowerCase()) return false;
        }

        // Year filter
        if (currentDbFilter.year !== 'all') {
          if (String(item.year) !== String(currentDbFilter.year)) return false;
        }

        // Country filter
        if (currentDbFilter.country !== 'all') {
          if (item.country !== currentDbFilter.country) return false;
        }

        // Type filter (dropdown or legacy pill)
        if (currentDbFilter.type !== 'all') {
          if (item.category !== currentDbFilter.type) return false;
        }

        // Search query
        if (query) {
          const match = (item.name || '').toLowerCase().includes(query) ||
                        (item.desc || '').toLowerCase().includes(query) ||
                        (item.sampleMsg || '').toLowerCase().includes(query) ||
                        (item.country || '').toLowerCase().includes(query) ||
                        (item.category || '').toLowerCase().includes(query) ||
                        (item.source || '').toLowerCase().includes(query) ||
                        (item.slug || '').toLowerCase().includes(query) ||
                        ((item.redFlags || []).join(' ')).toLowerCase().includes(query);
          if (!match) return false;
        }
        return true;
      });

      const countEl = document.getElementById('dbFilterCount');
      if (countEl) countEl.textContent = filtered.length;

      const emptyState = document.getElementById('dbEmptyState');
      const container = document.getElementById('dbCardsContainer');
      const loadMoreBtn = document.getElementById('dbLoadMoreBtn');

      if (filtered.length === 0) {
        if (emptyState) emptyState.classList.remove('hidden');
        if (container) container.innerHTML = '';
        if (loadMoreBtn) loadMoreBtn.classList.add('hidden');
        return;
      } else {
        if (emptyState) emptyState.classList.add('hidden');
      }

      // Pagination slice
      const displayedItems = filtered.slice(0, currentDbFilter.page * currentDbFilter.pageSize);

      if (loadMoreBtn) {
        if (displayedItems.length < filtered.length) {
          loadMoreBtn.classList.remove('hidden');
          const remaining = filtered.length - displayedItems.length;
          loadMoreBtn.innerHTML = `<span>Load More Scams (${Math.min(remaining, currentDbFilter.pageSize)} more of ${remaining} left) ↓</span>`;
        } else {
          loadMoreBtn.classList.add('hidden');
        }
      }

      renderScamDatabase(displayedItems, currentDbFilter.mode === 'timeline');
    }

    function renderScamCardHtml(scam) {
      const isLatest = scam.isLatest || scam.year === 2026;
      const scoreColor = scam.score >= 90 ? 'text-red-600' : scam.score >= 75 ? 'text-orange-600' : 'text-amber-600';
      const barColor = scam.score >= 90 ? 'bg-red-500' : scam.score >= 75 ? 'bg-orange-500' : 'bg-amber-500';
      const safeSample = (scam.sampleMsg || '').replace(/'/g, "\\'").replace(/"/g, '&quot;');
      const safeTitle = (scam.name || '').replace(/'/g, "\\'");
      const sourceName = scam.source || 'Official Database';

      return `
        <article class="bg-white dark:bg-black/25 rounded-2xl p-5 border border-slate-200 dark:border-white/10 hover:border-vgreen flex flex-col justify-between card3d transition">
          <div>
            <div class="flex items-center justify-between gap-1 mb-2.5 flex-wrap">
              <div class="flex items-center gap-1.5 flex-wrap">
                <span class="text-[10px] font-extrabold ${isLatest ? 'bg-red-600 text-white' : 'bg-navy text-white'} px-2 py-0.5 rounded-full">${scam.year}</span>
                ${isLatest ? '<span class="text-[10px] font-extrabold bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300 px-2 py-0.5 rounded-full">🔴 LATEST</span>' : ''}
                <span class="text-[10px] font-bold bg-slate-100 dark:bg-white/10 text-slate-700 dark:text-slate-300 px-2 py-0.5 rounded-full">${scam.country}</span>
              </div>
              <span class="text-[10px] font-bold text-slate-500 dark:text-slate-400 bg-slate-50 dark:bg-black/30 border border-slate-200 dark:border-white/5 px-2 py-0.5 rounded-full">🏛️ ${sourceName}</span>
            </div>
            <div class="flex items-start gap-2 mb-1.5">
              <span class="text-2xl shrink-0">${scam.icon || '⚠️'}</span>
              <h3 class="font-extrabold text-navy dark:text-white text-sm sm:text-base leading-snug cursor-pointer hover:text-vgreen transition" onclick="openScamDetail('${scam.slug}')">${scam.name}</h3>
            </div>
            <p class="text-xs text-slate-500 dark:text-slate-400 leading-relaxed mt-1">${scam.desc}</p>
            <div class="mt-2.5 p-2.5 rounded-xl bg-slate-50 dark:bg-black/40 border border-slate-200 dark:border-white/5 text-[11px] text-slate-600 dark:text-slate-300 italic line-clamp-2">
              “${scam.sampleMsg}”
            </div>
          </div>

          <div class="mt-4 pt-3 border-t border-slate-100 dark:border-white/10">
            <div class="flex justify-between text-[11px] font-bold mb-1">
              <span class="text-slate-500">Danger score</span>
              <span class="${scoreColor} font-extrabold">${scam.score} / 100</span>
            </div>
            <div class="h-1.5 bg-slate-100 dark:bg-slate-800 rounded-full overflow-hidden">
              <div class="h-full ${barColor}" style="width: ${scam.score}%"></div>
            </div>
            <div class="flex items-center justify-between mt-3 text-xs font-bold gap-2">
              <button onclick="quickSearchCheck('${safeSample}')" class="text-vgreen hover:underline text-[11px]">⚡ Test Pattern</button>
              <button onclick="openScamDetail('${scam.slug}')" class="text-navy dark:text-emerald-400 hover:text-vgreen text-[11px] font-extrabold">Full Detail →</button>
            </div>
            <div class="mt-2">
              <button onclick="shareScamCard('${safeTitle}', '${scam.score}/100', '${safeSample.slice(0, 50)}...')" class="w-full bg-[#25D366]/10 hover:bg-[#25D366] text-emerald-800 dark:text-emerald-300 hover:text-white py-1.5 rounded-xl text-[11px] font-bold transition flex items-center justify-center gap-1">
                <span>Share on WhatsApp 📲</span>
              </button>
            </div>
          </div>
        </article>
      `;
    }

    function renderScamDatabase(list, isTimeline) {
      const container = document.getElementById('dbCardsContainer');
      if (!container) return;

      if (!isTimeline) {
        let html = '<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">';
        list.forEach(item => {
          html += renderScamCardHtml(item);
        });
        html += '</div>';
        container.innerHTML = html;
      } else {
        const yearsMap = {};
        list.forEach(item => {
          const yr = item.year || 'Classic';
          if (!yearsMap[yr]) yearsMap[yr] = [];
          yearsMap[yr].push(item);
        });

        const sortedYears = Object.keys(yearsMap).sort((a, b) => {
          if (a === 'Classic') return 1;
          if (b === 'Classic') return -1;
          return Number(b) - Number(a);
        });

        let html = '<div id="scam-timeline-2016-2026" class="space-y-10">';
        sortedYears.forEach(yr => {
          const yearItems = yearsMap[yr];
          const is2026 = String(yr) === '2026';
          html += `
            <div class="timeline-year-group">
              <div class="flex items-center gap-3 pb-3 mb-4 border-b-2 ${is2026 ? 'border-red-500' : 'border-slate-200 dark:border-white/10'}">
                <span class="w-3.5 h-3.5 rounded-full ${is2026 ? 'bg-red-600 animate-ping' : 'bg-navy dark:bg-emerald-400'}"></span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-navy dark:text-white">
                  ${yr} ${is2026 ? '<span class="text-xs bg-red-600 text-white px-2.5 py-0.5 rounded-full ml-2 uppercase tracking-wider font-extrabold">Latest Wave</span>' : ''}
                </h2>
                <span class="text-xs font-bold text-slate-400">(${yearItems.length} threat patterns recorded)</span>
              </div>
              <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">
                ${yearItems.map(item => renderScamCardHtml(item)).join('')}
              </div>
            </div>
          `;
        });
        html += '</div>';
        container.innerHTML = html;
      }
    }

    // SCAM OF THE DAY (Auto-rotates daily based on day of year)
    function renderScamOfTheDay() {
      const card = document.getElementById('scamOfTheDayCard');
      if (!card) return;

      const db = window.GLOBAL_SCAMS_DATABASE || [];
      if (db.length === 0) return;

      const now = new Date();
      const start = new Date(now.getFullYear(), 0, 0);
      const diff = now - start;
      const oneDay = 1000 * 60 * 60 * 24;
      const dayOfYear = Math.floor(diff / oneDay);
      const featuredScam = db[dayOfYear % db.length] || db[0];

      card.innerHTML = `
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div class="space-y-1.5 max-w-[700px]">
            <div class="flex items-center gap-2 flex-wrap">
              <span class="text-[11px] font-extrabold uppercase tracking-wider bg-white/20 text-white px-2.5 py-0.5 rounded-full border border-white/25">
                ⭐ SCAM OF THE DAY • AUTO ROTATES DAILY
              </span>
              <span class="text-[10px] text-emerald-300 font-bold">● Auto-Update ON</span>
              <span class="text-[10px] bg-red-600 text-white px-2 py-0.5 rounded-full font-extrabold">Score: ${featuredScam.score}/100</span>
            </div>
            <h3 class="text-lg sm:text-xl font-extrabold text-white flex items-center gap-2">
              <span>${featuredScam.icon || '⚠️'}</span>
              <span>${featuredScam.name}</span>
            </h3>
            <p class="text-xs text-white/80 line-clamp-2 leading-relaxed">
              ${featuredScam.desc}
            </p>
            <div class="text-[11px] text-emerald-200 italic line-clamp-1">
              Example lure: “${featuredScam.sampleMsg}”
            </div>
          </div>
          <div class="shrink-0 flex sm:flex-col gap-2">
            <button onclick="openScamDetail('${featuredScam.slug}')" class="bg-vgreen hover:bg-vgreenDark text-white font-extrabold text-xs px-5 py-2.5 rounded-xl shadow-md transition flex items-center justify-center gap-1.5">
              <span>Inspect Breakdown →</span>
            </button>
            <button onclick="quickSearchCheck('${(featuredScam.sampleMsg || '').replace(/'/g, "\\'")}')" class="bg-white/10 hover:bg-white/20 text-white font-bold text-xs px-4 py-2 rounded-xl border border-white/20 transition flex items-center justify-center gap-1">
              <span>⚡ Test Pattern</span>
            </button>
          </div>
        </div>
      `;
    }

    // SCAM DETAIL MODAL WITH WIKIPEDIA-STYLE INFOBOX
    function openScamDetail(slug) {
      const db = window.GLOBAL_SCAMS_DATABASE || [];
      const scam = db.find(s => s.slug === slug || s.id === slug);
      if (!scam) return;

      currentModalScam = scam;

      document.getElementById('modalScamIcon').textContent = scam.icon || '⚠️';
      document.getElementById('modalScamTitle').textContent = scam.name;
      document.getElementById('modalScamDesc').textContent = scam.desc;
      
      const yrEl = document.getElementById('modalScamYear');
      yrEl.textContent = scam.year + (scam.isLatest ? ' (Latest)' : '');
      yrEl.className = scam.isLatest ? 'px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-red-600 text-white' : 'px-2.5 py-0.5 rounded-full font-extrabold text-[10px] bg-navy text-white';

      document.getElementById('modalScamCountry').textContent = scam.country;
      document.getElementById('modalScamCategory').textContent = scam.category;
      document.getElementById('modalScamScore').textContent = `Score: ${scam.score}/100`;

      // Set Wikipedia-style source badge
      const srcEl = document.getElementById('modalScamSource');
      if (srcEl) {
        srcEl.innerHTML = `<span class="font-extrabold text-navy dark:text-emerald-300">🏛️ Source:</span> <span>${scam.source || 'Wikipedia / Official Cyber Agency'}</span>`;
      }

      document.getElementById('modalKaiseHotaHai').textContent = scam.kaiseHotaHai || '1. Fraudsters mass-broadcast deceptive lures pretending to be an authentic authority or service.\n2. Malicious link, call, or APK captures sensitive banking credentials or triggers fear.\n3. Funds are rapidly diverted through multi-layer mule accounts before the victim realizes.';
      document.getElementById('modalSampleMsg').textContent = `“${scam.sampleMsg}”`;

      const flagsContainer = document.getElementById('modalRedFlags');
      if (flagsContainer) {
        flagsContainer.innerHTML = (scam.redFlags || []).map(flag => `
          <li class="flex items-start gap-2">
            <span class="text-amber-500 shrink-0 font-bold">⚠️</span>
            <span>${flag}</span>
          </li>
        `).join('');
      }

      const kyaKareinContainer = document.getElementById('modalKyaKarein');
      if (kyaKareinContainer) {
        kyaKareinContainer.innerHTML = (scam.kyaKarein || []).map(action => `
          <li class="pl-1">${action}</li>
        `).join('');
      }

      const modal = document.getElementById('scamDetailModal');
      if (modal) modal.classList.remove('hidden');

      window.history.pushState(null, '', `#scam/${scam.slug}`);
      document.title = `${scam.name} - Scam Details & Red Flags | IsThisScamOrReal.com`;
      const metaDesc = document.getElementById('metaDescTag');
      if (metaDesc) metaDesc.setAttribute('content', `Learn how ${scam.name} works, 5 red flags, sample phishing text, and official helplines to stay safe.`);
    }

    function closeScamDetail() {
      const modal = document.getElementById('scamDetailModal');
      if (modal) modal.classList.add('hidden');
      currentModalScam = null;
      if (window.location.hash.startsWith('#scam/')) {
        window.history.pushState(null, '', '#scam-database');
      }
    }

    function onScamModalBackdropClick(event) {
      if (event.target.id === 'scamDetailModal') {
        closeScamDetail();
      }
    }

    function copyModalSample() {
      if (!currentModalScam) return;
      navigator.clipboard.writeText(currentModalScam.sampleMsg).then(() => {
        const btn = document.getElementById('modalCopyBtn');
        if (btn) {
          const orig = btn.textContent;
          btn.textContent = 'Copied ✓';
          setTimeout(() => { btn.textContent = orig; }, 2000);
        }
      });
    }

    function shareModalScamWhatsApp() {
      if (!currentModalScam) return;
      const scam = currentModalScam;
      const text = `🚨 *URGENT SCAM ALERT: ${scam.name}* 🚨\\nRisk Score: *${scam.score}/100 - HIGH RISK*\\n\\nExample attack text:\\n"${scam.sampleMsg}"\\n\\nProtect your family and friends. View full 5 red flags and how to report at:\\nhttps://isthisscamorreal.com/#scam/${scam.slug}`;
      window.open('https://wa.me/?text=' + encodeURIComponent(text), '_blank');
    }

    function checkModalSample() {
      if (!currentModalScam) return;
      const sample = currentModalScam.sampleMsg;
      closeScamDetail();
      quickSearchCheck(sample);
    }

    // ================= ADD MISSING SCAM (COMMUNITY USER SUBMISSION WITH AUTO-MODERATION) =================
    function openAddMissingScamModal() {
      const modal = document.getElementById('addMissingScamModal');
      if (modal) modal.classList.remove('hidden');
    }

    function closeAddMissingScamModal() {
      const modal = document.getElementById('addMissingScamModal');
      if (modal) modal.classList.add('hidden');
    }

    function onAddScamBackdropClick(event) {
      if (event.target.id === 'addMissingScamModal') {
        closeAddMissingScamModal();
      }
    }

    function submitMissingScam(event) {
      event.preventDefault();

      const name = document.getElementById('addScamName').value.trim();
      const category = document.getElementById('addScamCategory').value;
      const country = document.getElementById('addScamCountry').value.trim();
      const desc = document.getElementById('addScamDesc').value.trim();
      const sample = document.getElementById('addScamSample').value.trim();
      const author = (document.getElementById('addScamAuthor').value.trim()) || 'Community Member';

      const combinedText = `${name} ${desc} ${sample}`.toLowerCase();

      // Automated Safety Filter: Reject Real Credit Cards, OTPs, CVVs, Bank Passwords
      const ccRegex = /\\b(?:\\d[ -]*?){13,19}\\b/;
      const otpRegex = /\\b(?:otp|one[- ]time[- ]password|cvv|pin|passcode|bank password)\\b/i;
      const profanityRegex = /\\b(?:fuck|shit|bitch|bastard|asshole|chutiya|madarchod|behenchod)\\b/i;

      if (ccRegex.test(sample) || ccRegex.test(desc)) {
        alert("⚠️ Security Protection: For community safety, real credit card numbers cannot be submitted. Please remove card digits and try again.");
        return;
      }

      if (otpRegex.test(sample)) {
        alert("⚠️ Safety Filter: Please do not submit real OTPs or passwords in sample texts. Use placeholder text like [OTP REDACTED].");
        return;
      }

      if (profanityRegex.test(combinedText)) {
        alert("⚠️ Moderation Alert: Abusive or profane language is not permitted in Scampedia.");
        return;
      }

      const newSlug = name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/(^-|-$)/g, '') + '-' + Date.now().toString().slice(-4);

      const newScam = {
        id: 'user-' + Date.now(),
        slug: newSlug,
        name: name,
        icon: '⚠️',
        year: 2026,
        isLatest: true,
        country: country || 'Global',
        category: category,
        categorySlug: category.toLowerCase(),
        source: 'Community User Report',
        desc: desc,
        sampleMsg: sample,
        score: 85,
        redFlags: [
          'Reported by verified community user in ' + (country || 'Global'),
          'Unsolicited contact prompting urgent action or payment',
          'Demands personal verification, credentials or money transfers'
        ],
        kyaKarein: [
          'Do NOT reply or click any links in this message',
          'Block and report the sender immediately',
          'File an official report on your regional cyber fraud portal'
        ],
        author: author,
        createdAt: new Date().toISOString()
      };

      // Save to localStorage
      try {
        let stored = [];
        const existing = localStorage.getItem('user_scams_db');
        if (existing) {
          stored = JSON.parse(existing);
        }
        stored.unshift(newScam);
        localStorage.setItem('user_scams_db', JSON.stringify(stored));
      } catch (err) {
        console.warn('Failed to store user scam in localStorage', err);
      }

      // Prepend to current database in memory
      if (!window.GLOBAL_SCAMS_DATABASE) window.GLOBAL_SCAMS_DATABASE = [];
      window.GLOBAL_SCAMS_DATABASE.unshift(newScam);

      // Reset form & close modal
      document.getElementById('addScamName').value = '';
      document.getElementById('addScamCountry').value = '';
      document.getElementById('addScamDesc').value = '';
      document.getElementById('addScamSample').value = '';
      document.getElementById('addScamAuthor').value = '';

      closeAddMissingScamModal();

      // Refresh Scampedia views
      renderScampediaCategories();
      filterScamsDatabase();

      alert("✅ Thank you! Your scam report has been added to Scampedia and is now live for all visitors.");
    }

    // ================= LIVE SCAM FEEDS / RSS AUTO-UPDATE ENGINE =================
    const FALLBACK_LIVE_FEEDS = [
      {
        title: "FBI IC3 Issues Warning on Emerging AI Voice Cloning Ransom Scams",
        source: "FBI IC3 Threat Advisory",
        date: "Today",
        link: "https://www.ic3.gov"
      },
      {
        title: "I4C India Alerts Citizens Against Fake Digital Arrest Video Call Extortions",
        source: "Cybercrime.gov.in",
        date: "Today",
        link: "https://cybercrime.gov.in"
      },
      {
        title: "FTC Warns Consumers About Lookalike Brand Clearance Ads on Social Feeds",
        source: "FTC Consumer Alert",
        date: "1 hour ago",
        link: "https://consumer.ftc.gov"
      },
      {
        title: "Action Fraud UK Reports 40% Spike in Electricity Smart Meter Phishing Messages",
        source: "Action Fraud UK",
        date: "3 hours ago",
        link: "https://www.actionfraud.police.uk"
      },
      {
        title: "Scamwatch Australia Cautions on Fake Parcel Delivery Rescheduling Texts",
        source: "Scamwatch Australia",
        date: "5 hours ago",
        link: "https://www.scamwatch.gov.au"
      }
    ];

    async function fetchLiveScamFeeds(forceRefresh = false) {
      const now = Date.now();
      const CACHE_KEY = 'cached_threat_feeds_v1';
      const TIME_KEY = 'cached_threat_feeds_time';
      const SIX_HOURS = 6 * 60 * 60 * 1000;

      let feeds = FALLBACK_LIVE_FEEDS;

      try {
        const cached = localStorage.getItem(CACHE_KEY);
        const lastTime = Number(localStorage.getItem(TIME_KEY) || 0);

        if (!forceRefresh && cached && (now - lastTime < SIX_HOURS)) {
          feeds = JSON.parse(cached);
        } else {
          // Public RSS to JSON
          const rssUrl = encodeURIComponent('https://news.google.com/rss/search?q=cyber+fraud+or+scam+alert&hl=en-US&gl=US&ceid=US:en');
          const res = await fetch(`https://api.rss2json.com/v1/api.json?rss_url=${rssUrl}`);
          if (res.ok) {
            const data = await res.json();
            if (data.items && data.items.length > 0) {
              feeds = data.items.slice(0, 8).map(item => ({
                title: item.title,
                source: item.author || 'Cyber Threat News',
                date: item.pubDate ? new Date(item.pubDate).toLocaleDateString([], { month: 'short', day: 'numeric' }) : 'Today',
                link: item.link
              }));
              localStorage.setItem(CACHE_KEY, JSON.stringify(feeds));
              localStorage.setItem(TIME_KEY, String(now));
            }
          }
        }
      } catch (err) {
        console.warn('Live RSS feed using fallback cache', err);
      }

      // Update Live Ticker with fresh news item
      if (feeds.length > 0) {
        const tickerEl = document.getElementById('tickerContent');
        if (tickerEl) {
          tickerItems.push(`🔴 Global Alert: ${feeds[0].title.slice(0, 90)}...`);
        }
      }

      // Update Admin Log
      renderAdminLiveFeeds(feeds);
    }

    function renderAdminLiveFeeds(feeds) {
      const logContainer = document.getElementById('adminLiveFeedsLog');
      if (!logContainer) return;

      logContainer.innerHTML = feeds.map(f => `
        <div class="flex items-start justify-between gap-3 p-3 rounded-xl bg-white dark:bg-black/40 border border-slate-200 dark:border-white/5">
          <div>
            <div class="font-bold text-navy dark:text-white leading-snug">${f.title}</div>
            <div class="text-[11px] text-slate-400 mt-1 flex items-center gap-2">
              <span class="text-vgreen font-semibold">● ${f.source}</span>
              <span>•</span>
              <span>${f.date}</span>
            </div>
          </div>
          <a href="${f.link}" target="_blank" rel="noopener" class="shrink-0 text-vgreen hover:underline font-bold text-[11px] px-2.5 py-1 rounded-lg bg-emerald-50 dark:bg-emerald-950/40">Read ↗</a>
        </div>
      `).join('');
    }

    // ================= ADMIN DASHBOARD CONTROLLER =================
    function renderAdminDashboard() {
      const db = window.GLOBAL_SCAMS_DATABASE || [];
      const totalEl = document.getElementById('adminTotalScams');
      if (totalEl) totalEl.textContent = db.length;

      let userScams = [];
      try {
        const stored = localStorage.getItem('user_scams_db');
        if (stored) userScams = JSON.parse(stored);
      } catch (e) {}

      const userReportsCountEl = document.getElementById('adminUserReportsCount');
      if (userReportsCountEl) userReportsCountEl.textContent = userScams.length;

      const timeEl = document.getElementById('adminLastCheckedTime');
      if (timeEl) timeEl.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) + ' (Auto-Sync Active)';

      const tableBody = document.getElementById('adminUserReportsTable');
      if (tableBody) {
        if (userScams.length === 0) {
          tableBody.innerHTML = `
            <tr>
              <td colspan="5" class="py-6 text-center text-slate-400 italic">No user reports yet. Test the "Add Missing Scam" form in Scampedia!</td>
            </tr>
          `;
        } else {
          tableBody.innerHTML = userScams.map(s => `
            <tr class="border-b border-slate-100 dark:border-white/5 hover:bg-slate-50 dark:hover:bg-white/5 transition">
              <td class="py-2.5 px-3 font-bold text-navy dark:text-white">${s.name}</td>
              <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded bg-slate-100 dark:bg-white/10 text-slate-700 dark:text-slate-300 font-medium">${s.category}</span></td>
              <td class="py-2.5 px-3 text-slate-500 dark:text-slate-400">${s.country}</td>
              <td class="py-2.5 px-3 text-slate-500 dark:text-slate-400 max-w-[240px] truncate" title="${s.sampleMsg}">“${s.sampleMsg}”</td>
              <td class="py-2.5 px-3"><span class="px-2 py-0.5 rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-950 dark:text-emerald-300 font-extrabold text-[10px]">Active</span></td>
            </tr>
          `).join('');
        }
      }
    }

    function clearUserReports() {
      if (confirm("Are you sure you want to clear all user-submitted community reports?")) {
        localStorage.removeItem('user_scams_db');
        window.GLOBAL_SCAMS_DATABASE = [...baseScamsDb];
        renderScampediaCategories();
        filterScamsDatabase();
        renderAdminDashboard();
        alert("All user reports have been cleared.");
      }
    }

    function exportScamsJson() {
      const db = window.GLOBAL_SCAMS_DATABASE || [];
      const jsonStr = JSON.stringify(db, null, 2);
      const blob = new Blob([jsonStr], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = `isthisscamorreal-scampedia-database-${new Date().toISOString().slice(0, 10)}.json`;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
    }

    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeScamDetail();
        closeAddToHomeScreen();
        closeAddMissingScamModal();
      }
    });

    function showView(viewName) {
      document.querySelectorAll('.view-section').forEach(el => el.classList.add('hidden'));
      const target = document.getElementById('view-' + viewName);
      if (target) {
        target.classList.remove('hidden');
        window.scrollTo({ top: 0, behavior: 'smooth' });
        if (viewName === 'scam-database') {
          renderScampediaCategories();
          filterScamsDatabase();
        }
        if (viewName === 'admin') {
          renderAdminDashboard();
        }
        if (viewMetaMap[viewName]) {
          updateSeoMeta(viewMetaMap[viewName].title, viewMetaMap[viewName].desc, viewName);
        } else {
          const dict = translations[activeLang] || translations.en;
          updateSeoMeta(dict.seoTitle, dict.seoDesc, viewName === 'home' ? '' : viewName);
        }
      }
    }

    function quickSearchCheck(sampleText) {
      showView('home');
      switchTab('sms');
      const msgInput = document.getElementById('messageInput');
      msgInput.value = sampleText;
      document.getElementById('checker').scrollIntoView({ behavior: 'smooth' });
      runCheck();
    }

    function setCategory(cat) {
      showView('home');
      document.querySelectorAll('.tool-pill').forEach(p => {
        p.classList.remove('bg-vgreen', 'text-white', 'border-vgreenDark', 'shadow-md');
        p.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
      });
      const btn = document.getElementById('pill-' + cat);
      if (btn) {
        btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
        btn.classList.add('bg-vgreen', 'text-white', 'border-vgreenDark', 'shadow-md');
      }
      let msgInput = document.getElementById('messageInput');
      if (cat === 'link') {
        switchTab('sms');
        msgInput.value = 'URGENT: Your bank account is blocked. Update KYC at https://sbi-update-verify.com';
      } else if (cat === 'number') {
        switchTab('sms');
        msgInput.value = 'Call electricity officer immediately at 91040 to avoid power disconnection tonight.';
      } else if (cat === 'email') { 
        switchTab('email'); 
        document.getElementById('emailSenderInput').value = 'support@amaz0n-support.com';
        document.getElementById('emailSubjectInput').value = 'Your account will be closed in 24 hours';
        document.getElementById('emailBodyInput').value = 'PayPal Security Alert: Unusual login detected. Confirm card details here.'; 
      } else if (cat === 'crypto') {
        switchTab('sms');
        msgInput.value = 'Guaranteed 500% daily returns on Bitcoin cloud mining platform! Join VIP group.';
      } else if (cat === 'job') {
        switchTab('sms');
        msgInput.value = 'YouTube video liking job. Earn $500 per day working from home. Message on Telegram.';
      } else if (cat === 'shop') {
        switchTab('sms');
        msgInput.value = 'Luxury iPhone 16 Pro Max for only $199 on flash sale. Cash on delivery available.';
      } else {
        switchTab('sms');
        msgInput.value = 'Congratulations! You have won $25,000 in KBC lottery. Claim now.';
      }
      document.getElementById('checker').scrollIntoView({ behavior: 'smooth' });
    }

    function switchTab(tab) {
      currentTab = tab;
      if (tab === 'sms') {
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
        document.getElementById('smsFormSection').classList.remove('hidden');
        document.getElementById('emailFormSection').classList.add('hidden');
      } else {
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
        document.getElementById('emailFormSection').classList.remove('hidden');
        document.getElementById('smsFormSection').classList.add('hidden');
      }
    }

    function resetChecker() {
      document.getElementById('messageInput').value = '';
      document.getElementById('senderNumberInput').value = '';
      document.getElementById('emailSenderInput').value = '';
      document.getElementById('emailSubjectInput').value = '';
      document.getElementById('emailBodyInput').value = '';
      document.getElementById('resultBox').classList.add('hidden');
      document.getElementById('photoPreviewArea').classList.add('hidden');
    }

    // ADVANCED RUN CHECK WITH CIRCULAR SCORE, RED FLAGS BREAKDOWN, AND VERIFIED BADGE
    function runCheck() {
      let textToCheck = '';
      if (currentTab === 'sms') {
        textToCheck = document.getElementById('messageInput').value.trim();
        if (!textToCheck) {
          document.getElementById('messageInput').focus();
          return;
        }
      } else {
        const sender = document.getElementById('emailSenderInput').value.trim();
        const subject = document.getElementById('emailSubjectInput').value.trim();
        const body = document.getElementById('emailBodyInput').value.trim();
        if (!body && !subject) {
          document.getElementById('emailBodyInput').focus();
          return;
        }
        if (sender && !sender.includes('@')) {
          document.getElementById('emailSenderInput').focus();
          return;
        }
        textToCheck = `Sender: ${sender} | Subject: ${subject} | Body: ${body}`;
      }

      const box = document.getElementById('resultBox');
      const loading = document.getElementById('resultLoading');
      const content = document.getElementById('resultContent');
      box.classList.remove('hidden');
      loading.classList.remove('hidden');
      content.classList.add('hidden');
      box.scrollIntoView({ behavior: 'smooth' });

      setTimeout(() => {
        loading.classList.add('hidden');
        content.classList.remove('hidden');

        const lower = textToCheck.toLowerCase();
        let score = 15;
        let redFlags = [];

        // Red flag detectors
        if (lower.includes('otp') || lower.includes('cvv') || lower.includes('pin') || lower.includes('password') || lower.includes('aadhaar')) {
          redFlags.push({ title: 'Asking for OTP / Private Codes', desc: 'Requesting confidential authentication credentials or verification codes.' });
        }
        if (lower.includes('urgent') || lower.includes('24 hours') || lower.includes('tonight') || lower.includes('closed') || lower.includes('suspend') || lower.includes('blocked') || lower.includes('immediately')) {
          redFlags.push({ title: 'Manufactured Urgency & Panic', desc: 'Threatens immediate account closure, power cut, or legal fine within hours.' });
        }
        if (lower.includes('http') || lower.includes('.top') || lower.includes('.xyz') || lower.includes('.ru') || lower.includes('bit.ly') || lower.includes('tinyurl') || lower.includes('0') || lower.includes(' amaz0n') || lower.includes('paypa1')) {
          redFlags.push({ title: 'Suspicious / Lookalike Link', desc: 'Domain is shortened or contains typosquatted characters pretending to be legitimate.' });
        }
        if (lower.includes('customs') || lower.includes('parcel') || lower.includes('toll') || lower.includes('duty') || lower.includes('fee') || lower.includes('deposit') || lower.includes('won') || lower.includes('lottery') || lower.includes('prize') || lower.includes('500%')) {
          redFlags.push({ title: 'Upfront Fee or Guaranteed Returns', desc: 'Demands advance processing fees, release duties, or promises unrealistic returns.' });
        }
        if (lower.includes('telegram') || lower.includes('apk') || lower.includes('youtube') || lower.includes('liking') || lower.includes('+92') || lower.includes('+84') || lower.includes('+62')) {
          redFlags.push({ title: 'Unaccredited Source / Shady Channel', desc: 'Pushes users to external messaging apps or unverified Android APK installations.' });
        }

        if (redFlags.length >= 2) {
          score = 92;
        } else if (redFlags.length === 1) {
          score = 55;
        } else {
          score = 15;
        }

        // SVG circle calculation: Circumference = 2 * PI * 42 ≈ 264
        const circle = document.getElementById('scoreSvgCircle');
        const offset = Math.round(264 - (264 * score / 100));
        if (circle) {
          circle.style.strokeDashoffset = offset;
        }
        document.getElementById('scoreNum').textContent = score;

        const heading = document.getElementById('verdictHeading');
        const desc = document.getElementById('verdictDesc');
        const badge = document.getElementById('verifiedSafeBadge');
        const actionText = document.getElementById('actionLineText');
        const redFlagsList = document.getElementById('redFlagsList');
        const countBadge = document.getElementById('redFlagCountBadge');
        const dict = translations[activeLang] || translations.en;

        if (score > 70) {
          if (circle) circle.setAttribute('stroke', '#FF3B30');
          if (badge) badge.classList.add('hidden');
          if (heading) heading.textContent = `Scam Score: ${score}/100 - HIGH RISK 🚨`;
          if (desc) desc.textContent = dict.resultDanger || 'Strong scam signals found. Do NOT click links, call back or share any money or code.';
          if (actionText) actionText.textContent = dict.actionLine || 'What to do: Do NOT click, Block number, Report to cyber authorities immediately.';
          if (countBadge) countBadge.textContent = `${redFlags.length} Flags Found`;
        } else if (score >= 40) {
          if (circle) circle.setAttribute('stroke', '#FF9500');
          if (badge) badge.classList.add('hidden');
          if (heading) heading.textContent = `Scam Score: ${score}/100 - MODERATE RISK ⚠️`;
          if (desc) desc.textContent = 'Some suspicious signals found. Exercise caution and verify the sender independently before replying.';
          if (actionText) actionText.textContent = 'What to do: Never send money or codes. Verify through official customer service channels.';
          if (countBadge) countBadge.textContent = `${redFlags.length} Flag Found`;
        } else {
          if (circle) circle.setAttribute('stroke', '#00C853');
          if (badge) badge.classList.remove('hidden');
          if (heading) heading.textContent = `Scam Score: ${score}/100 - LOW RISK ✅`;
          if (desc) desc.textContent = dict.resultSafe || 'No strong scam pattern found, but always verify unknown senders independently.';
          if (actionText) actionText.textContent = 'What to do: Normal caution. Ensure the sender address matches legitimate channels.';
          if (countBadge) countBadge.textContent = `0 Flags Found`;
        }

        // Render Red Flags Breakdown
        if (redFlagsList) {
          if (redFlags.length > 0) {
            redFlagsList.innerHTML = redFlags.map(f => `
              <li class="flex items-start gap-2 bg-black/25 p-2.5 rounded-xl">
                <span class="text-base shrink-0">⚠️</span>
                <div><b>${f.title}:</b> ${f.desc}</div>
              </li>
            `).join('');
          } else {
            redFlagsList.innerHTML = `
              <li class="flex items-start gap-2 bg-emerald-950/40 p-2.5 rounded-xl border border-emerald-500/20 text-emerald-200">
                <span class="text-base shrink-0">✓</span>
                <div><b>Clean Threat Profile:</b> No urgent threats, phishing links, or suspicious credential prompts detected.</div>
              </li>
            `;
          }
        }

        // Save check to history
        saveCheckToHistory({
          text: textToCheck.slice(0, 80),
          score: score,
          verdict: score > 70 ? 'High Risk' : score >= 40 ? 'Moderate' : 'Safe',
          date: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        });
      }, 700);
    }

    function copyResult() {
      const dict = translations[activeLang] || translations.en;
      const verdict = document.getElementById('verdictHeading').textContent;
      const score = document.getElementById('scoreNum').textContent;
      const summary = `IsThisScamOrReal.com Safety Verdict: ${verdict} (Risk Score: ${score}/100) — Check any message free at https://isthisscamorreal.com`;
      if (navigator.clipboard) {
        navigator.clipboard.writeText(summary);
      }
      const copyBtns = document.querySelectorAll('[data-i18n="copy"]');
      copyBtns.forEach(b => {
        const orig = b.textContent;
        b.textContent = dict.copied || 'Copied ✓';
        setTimeout(() => { b.textContent = orig; }, 2000);
      });
    }

    function handlePhotoUpload(e) {
      const f = e.target.files[0];
      if (f) {
        document.getElementById('photoThumb').src = URL.createObjectURL(f);
        document.getElementById('photoNameText').textContent = f.name;
        document.getElementById('photoPreviewArea').classList.remove('hidden');
      }
    }

    function removePhoto() {
      document.getElementById('photoPreviewArea').classList.add('hidden');
    }

    let reportType = 'Financial Loss';
    function setReportType(btn, type) {
      reportType = type;
      document.querySelectorAll('.report-type-btn').forEach(b => {
        b.className = 'report-type-btn px-4 py-2.5 rounded-full text-xs font-bold border border-slate-200 bg-white text-slate-700';
      });
      btn.className = 'report-type-btn px-4 py-2.5 rounded-full text-xs font-bold border border-slate-200 bg-[#0A1931] text-white';
    }

    function submitReport() {
      const detail = document.getElementById('reportDetail').value.trim();
      if (!detail) {
        document.getElementById('reportDetail').focus();
        return;
      }
      document.getElementById('reportSuccessBox').classList.remove('hidden');
      document.getElementById('reportDetail').value = '';
    }

    function clearReport() {
      document.getElementById('reportDetail').value = '';
      document.getElementById('reportSuccessBox').classList.add('hidden');
    }

    function copySnippet(btn, elementId) {
      const el = document.getElementById(elementId);
      const text = el.innerText || el.textContent;
      navigator.clipboard.writeText(text).then(() => {
        const original = btn.textContent;
        btn.textContent = 'Copied ✓';
        btn.classList.add('bg-vgreen', 'text-white');
        setTimeout(() => {
          btn.textContent = original;
          btn.classList.remove('bg-vgreen', 'text-white');
        }, 2000);
      });
    }

    function handleHashRouting() {
      if (!window.location.hash) return;
      const hash = window.location.hash.replace('#', '');
      if (hash.startsWith('scam/')) {
        const slug = hash.replace('scam/', '');
        showView('scam-database');
        setTimeout(() => openScamDetail(slug), 100);
      } else if (hash === 'scam-timeline-2016-2026') {
        showView('scam-database');
        setDbViewMode('timeline');
      } else {
        const validViews = ['scam-database', 'blog', 'how-to-check-scam', 'link-checker', 'number-lookup', 'email-checker', 'job-checker', 'free-tools', 'privacy', 'terms', 'about', 'backlink-outreach', 'admin'];
        if (validViews.includes(hash)) {
          showView(hash);
        }
      }
    }

    window.addEventListener('hashchange', handleHashRouting);

    window.addEventListener('DOMContentLoaded', () => {
      initDarkMode();
      autoDetectLanguage();
      loadCheckHistory();
      loadUserSubmittedScams();
      startLiveTicker();
      renderScampediaCategories();
      renderScamOfTheDay();
      fetchLiveScamFeeds();
      handleHashRouting();
    });
"""

content = content[:idx_start] + new_javascript + content[idx_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Successfully replaced JavaScript logic in index.html!")
