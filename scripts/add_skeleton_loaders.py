#!/usr/bin/env python3
"""
Adds skeleton loaders to scam database rendering function.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find function renderScamDatabase and replace it
import re

skeleton_code = '''    function renderScamDatabaseSkeleton() {
      const container = document.getElementById('dbCardsContainer');
      if (!container) return;
      let html = '<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">';
      for (let i = 0; i < 6; i++) {
        html += `
          <div class="bg-white dark:bg-[#0E1E38] rounded-[22px] p-5 border border-slate-200 dark:border-white/15 animate-pulse space-y-3 shadow-sm">
            <div class="flex items-center justify-between">
              <div class="w-20 h-5 bg-slate-200 dark:bg-white/10 rounded-full"></div>
              <div class="w-12 h-5 bg-slate-200 dark:bg-white/10 rounded-full"></div>
            </div>
            <div class="w-3/4 h-6 bg-slate-200 dark:bg-white/10 rounded-lg"></div>
            <div class="w-full h-12 bg-slate-100 dark:bg-white/5 rounded-xl"></div>
            <div class="flex items-center justify-between pt-2">
              <div class="w-24 h-4 bg-slate-200 dark:bg-white/10 rounded"></div>
              <div class="w-20 h-8 bg-slate-200 dark:bg-white/10 rounded-xl"></div>
            </div>
          </div>
        `;
      }
      html += '</div>';
      container.innerHTML = html;
    }

    function renderScamDatabase(list, isTimeline) {
      const container = document.getElementById('dbCardsContainer');
      if (!container) return;
      
      // Render skeleton loaders for perceived performance
      renderScamDatabaseSkeleton();

      setTimeout(() => {
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
      }, 180);
    }'''

# Replace old renderScamDatabase function
pattern = re.compile(r'function renderScamDatabase\(.*?\n    \}', re.DOTALL)
if pattern.search(text):
    text = pattern.sub(skeleton_code, text, count=1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Successfully added skeleton loaders script!")
else:
    print("Error: renderScamDatabase pattern not found.")
