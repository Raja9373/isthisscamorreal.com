#!/usr/bin/env python3
"""
Fix tools and UI:
1. Rename "Message" -> "WhatsApp / SMS" in pill and dictionaries.
2. Ensure 1 tool = 1 input box (Link Checker, Number Lookup, Company, Crypto Alert, Job Scan, Shop Checker all show a single dedicated input box; Message shows SMS/WhatsApp & Email tabs; Email Checker shows 3 fields).
3. Result box appears below form with circular score first, red flags second, next steps third, and clears on reset/new check.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Rename catMessage in translations
text = text.replace('catMessage: "Message"', 'catMessage: "WhatsApp / SMS"')

# 2. Add singleToolInputSection in HTML before smsFormSection
old_sms_sec = '          <!-- SMS / WHATSAPP FORM SECTION -->'
single_tool_html = '''          <!-- SINGLE TOOL INPUT SECTION (For Link, Number, Company, Crypto, Job, Shop) -->
          <div id="singleToolInputSection" class="hidden mb-4">
            <div class="mb-2">
              <label id="singleToolLabel" class="block text-sm font-extrabold text-navy mb-1.5">Enter details...</label>
              <div class="relative">
                <input type="text" id="singleToolInput" class="w-full border-2 border-slate-200 rounded-2xl p-4 text-sm bg-[#FBFFFC] light-bg focus:border-vgreen focus:ring-4 focus:ring-emerald-100 outline-none shadow-sm" placeholder="Paste or type here..." />
              </div>
            </div>
          </div>

          <!-- SMS / WHATSAPP FORM SECTION -->'''

if old_sms_sec in text and 'singleToolInputSection' not in text:
    text = text.replace(old_sms_sec, single_tool_html)
    print("Added singleToolInputSection to HTML.")

# Also wrap tabs container with id="checkerTabsContainer" if not already
old_tabs = '          <!-- Tabs -->\n          <div class="flex gap-2 mb-5 bg-[#EEF6F0] light-bg p-1.5 rounded-full w-full sm:w-[360px]">'
new_tabs = '          <!-- Tabs -->\n          <div id="checkerTabsContainer" class="flex gap-2 mb-5 bg-[#EEF6F0] light-bg p-1.5 rounded-full w-full sm:w-[360px]">'
if old_tabs in text and 'checkerTabsContainer' not in text:
    text = text.replace(old_tabs, new_tabs)
    print("Added checkerTabsContainer id.")

# 3. Replace setCategory implementation
old_set_cat = '''    function setCategory(cat) {
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
    }'''

new_set_cat = '''    let activeToolCategory = 'message';
    function setCategory(cat) {
      showView('home');
      activeToolCategory = cat;
      document.querySelectorAll('.tool-pill').forEach(p => {
        p.classList.remove('bg-vgreen', 'text-white', 'border-vgreenDark', 'shadow-md');
        p.classList.add('bg-white', 'text-slate-700', 'border-slate-200');
      });
      const btn = document.getElementById('pill-' + cat);
      if (btn) {
        btn.classList.remove('bg-white', 'text-slate-700', 'border-slate-200');
        btn.classList.add('bg-vgreen', 'text-white', 'border-vgreenDark', 'shadow-md');
      }

      const tabsEl = document.getElementById('checkerTabsContainer');
      const smsSec = document.getElementById('smsFormSection');
      const emailSec = document.getElementById('emailFormSection');
      const singleSec = document.getElementById('singleToolInputSection');
      const singleInput = document.getElementById('singleToolInput');
      const singleLabel = document.getElementById('singleToolLabel');

      if (cat === 'message') {
        if (tabsEl) tabsEl.classList.remove('hidden');
        switchTab('sms');
        if (smsSec) smsSec.classList.remove('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        if (singleSec) singleSec.classList.add('hidden');
        const msgInput = document.getElementById('messageInput');
        if (msgInput) msgInput.value = 'Congratulations! You have won $25,000 in KBC lottery. Claim now.';
      } else if (cat === 'email') {
        if (tabsEl) tabsEl.classList.add('hidden');
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.remove('hidden');
        if (singleSec) singleSec.classList.add('hidden');
        document.getElementById('emailSenderInput').value = 'support@amaz0n-support.com';
        document.getElementById('emailSubjectInput').value = 'Your account will be closed in 24 hours';
        document.getElementById('emailBodyInput').value = 'PayPal Security Alert: Unusual login detected. Confirm card details here.';
      } else {
        if (tabsEl) tabsEl.classList.add('hidden');
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        if (singleSec) singleSec.classList.remove('hidden');

        if (cat === 'link') {
          if (singleLabel) singleLabel.textContent = 'Paste Link / URL Here...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. https://sbi-update-verify.com or bit.ly/3xyz';
            singleInput.value = 'https://sbi-update-verify.com/login-kyc';
          }
        } else if (cat === 'number') {
          if (singleLabel) singleLabel.textContent = 'Enter Phone Number / Sender ID...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. +91 98765 43210 or 91040';
            singleInput.value = '+91 98765 43210';
          }
        } else if (cat === 'company') {
          if (singleLabel) singleLabel.textContent = 'Enter Company / Website Name...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. Amaz0n Support or Fake Bank Ltd';
            singleInput.value = 'Amaz0n Secure Support';
          }
        } else if (cat === 'crypto') {
          if (singleLabel) singleLabel.textContent = 'Enter Crypto Coin / Website / Wallet Address...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. bitcoin-cloud-mining.net or 0x9812...';
            singleInput.value = 'bitcoin-cloud-mining-vip.net';
          }
        } else if (cat === 'job') {
          if (singleLabel) singleLabel.textContent = 'Paste Job Offer / Company Name...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. Telegram video liking job or work from home offer';
            singleInput.value = 'Earn $500 per day liking YouTube videos. Telegram contact @hr_manager.';
          }
        } else if (cat === 'shop') {
          if (singleLabel) singleLabel.textContent = 'Paste Shop / Website Link...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. instagram.com/luxury_store_90_off';
            singleInput.value = 'https://instagram.com/stanley_warehouse_90_off';
          }
        }
      }
      document.getElementById('checker').scrollIntoView({ behavior: 'smooth' });
    }'''

if old_set_cat in text:
    text = text.replace(old_set_cat, new_set_cat)
    print("Updated setCategory implementation.")

# 4. Update switchTab function
old_switch_tab = '''    function switchTab(tab) {
      currentTab = tab;
      const smsSec = document.getElementById('smsFormSection');
      const emailSec = document.getElementById('emailFormSection');
      if (tab === 'sms') {
        if (smsSec) smsSec.classList.remove('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
      } else {
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.remove('hidden');
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
      }
    }'''

new_switch_tab = '''    function switchTab(tab) {
      currentTab = tab;
      activeToolCategory = 'message';
      const smsSec = document.getElementById('smsFormSection');
      const emailSec = document.getElementById('emailFormSection');
      const singleSec = document.getElementById('singleToolInputSection');
      if (singleSec) singleSec.classList.add('hidden');
      if (tab === 'sms') {
        if (smsSec) smsSec.classList.remove('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
      } else {
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.remove('hidden');
        document.getElementById('tabEmailBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold bg-[#0A1931] text-white shadow';
        document.getElementById('tabSmsBtn').className = 'flex-1 py-2.5 rounded-full text-xs font-bold text-slate-600 hover:bg-white/50';
      }
    }'''

if old_switch_tab in text:
    text = text.replace(old_switch_tab, new_switch_tab)
    print("Updated switchTab implementation.")

# 5. Update runCheck input reading
old_run_check_start = '''    function runCheck() {
      let textToCheck = '';
      if (currentTab === 'sms') {
        textToCheck = document.getElementById('messageInput').value.trim();
        if (!textToCheck) {
          document.getElementById('messageInput').focus();
          return;
        }
      } else {'''

new_run_check_start = '''    function runCheck() {
      let textToCheck = '';
      if (activeToolCategory !== 'message' && activeToolCategory !== 'email') {
        const singleInput = document.getElementById('singleToolInput');
        textToCheck = singleInput ? singleInput.value.trim() : '';
        if (!textToCheck) {
          if (singleInput) singleInput.focus();
          return;
        }
      } else if (currentTab === 'sms') {
        textToCheck = document.getElementById('messageInput').value.trim();
        if (!textToCheck) {
          document.getElementById('messageInput').focus();
          return;
        }
      } else {'''

if old_run_check_start in text:
    text = text.replace(old_run_check_start, new_run_check_start)
    print("Updated runCheck input reading.")

# 6. Update resetChecker to clear singleToolInput
old_reset = '''    function resetChecker() {
      const msgInput = document.getElementById('messageInput');
      if (msgInput) msgInput.value = '';
      document.getElementById('emailSenderInput').value = '';
      document.getElementById('emailSubjectInput').value = '';
      document.getElementById('emailBodyInput').value = '';
      const box = document.getElementById('resultBox');
      if (box) box.classList.add('hidden');
      const warning = document.getElementById('sensitiveInputWarning');
      if (warning) warning.classList.add('hidden');
    }'''

new_reset = '''    function resetChecker() {
      const msgInput = document.getElementById('messageInput');
      if (msgInput) msgInput.value = '';
      const singleInput = document.getElementById('singleToolInput');
      if (singleInput) singleInput.value = '';
      document.getElementById('emailSenderInput').value = '';
      document.getElementById('emailSubjectInput').value = '';
      document.getElementById('emailBodyInput').value = '';
      const box = document.getElementById('resultBox');
      if (box) box.classList.add('hidden');
      const warning = document.getElementById('sensitiveInputWarning');
      if (warning) warning.classList.add('hidden');
    }'''

if old_reset in text:
    text = text.replace(old_reset, new_reset)
    print("Updated resetChecker implementation.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Patch applied successfully!")
