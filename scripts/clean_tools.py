#!/usr/bin/env python3
"""
Clean up tools and UI:
1. Fix heading overlap by adding scroll-margin-top and pt to #checker and main container.
2. Remove duplicate tabs container entirely (#checkerTabsContainer).
3. 8 tools, each showing strictly its needed form (1 button = 1 form format).
4. Rename catMessage to "WhatsApp / SMS".
5. Ensure result box appears cleanly below form.
"""

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix heading overlap: add scroll-margin-top and padding-top to #checker
old_checker_open = '<id="checker" class="bg-white rounded-[24px] card3d mt-6 relative z-10 p-5 sm:p-8">' # wait, let's check exact tag
# Let's search for id="checker" in index.html
import re
m_checker = re.search(r'<div id=\"checker\"[^>]*>', text)
if m_checker:
    print("Found checker tag:", m_checker.group(0))
    new_checker_tag = '<div id="checker" class="bg-white rounded-[24px] card3d mt-8 relative z-10 p-5 sm:p-8 scroll-mt-28" style="scroll-margin-top: 100px;">'
    text = text.replace(m_checker.group(0), new_checker_tag)

# Also ensure main has enough top padding
old_main = '<main id="top"'
new_main = '<main id="top" class="max-w-[1100px] mx-auto px-4 pb-16 pt-6 sm:pt-8"'
text = text.replace('<main id="top" class="max-w-[1100px] mx-auto px-4 pb-16">', new_main)

# 2. Remove duplicate tabs container from HTML entirely
# The tabs div:
tabs_pattern = re.compile(r'<!-- Tabs -->\s*<div id=\"checkerTabsContainer\"[^>]*>.*?</div>', re.DOTALL)
text = tabs_pattern.sub('', text)

# 3. Update setCategory function to handle all 8 tools cleanly without tabs
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

      const smsSec = document.getElementById('smsFormSection');
      const emailSec = document.getElementById('emailFormSection');
      const singleSec = document.getElementById('singleToolInputSection');
      const singleInput = document.getElementById('singleToolInput');
      const singleLabel = document.getElementById('singleToolLabel');

      if (cat === 'message') {
        if (smsSec) smsSec.classList.remove('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        if (singleSec) singleSec.classList.add('hidden');
        const msgInput = document.getElementById('messageInput');
        if (msgInput) msgInput.value = 'Congratulations! You have won $25,000 in KBC lottery. Claim now.';
      } else if (cat === 'email') {
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.remove('hidden');
        if (singleSec) singleSec.classList.add('hidden');
        document.getElementById('emailSenderInput').value = 'support@amaz0n-support.com';
        document.getElementById('emailSubjectInput').value = 'Your account will be closed in 24 hours';
        document.getElementById('emailBodyInput').value = 'PayPal Security Alert: Unusual login detected. Confirm card details here.';
      } else {
        if (smsSec) smsSec.classList.add('hidden');
        if (emailSec) emailSec.classList.add('hidden');
        if (singleSec) singleSec.classList.remove('hidden');

        if (cat === 'link') {
          if (singleLabel) singleLabel.textContent = 'Paste Link / URL Here...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. https://sbi-update-verify.com';
            singleInput.value = 'https://sbi-update-verify.com/login-kyc';
          }
        } else if (cat === 'number') {
          if (singleLabel) singleLabel.textContent = 'Enter Number...';
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
          if (singleLabel) singleLabel.textContent = 'Enter Coin / Website / Wallet...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. bitcoin-cloud-mining.net or 0x9812...';
            singleInput.value = 'bitcoin-cloud-mining-vip.net';
          }
        } else if (cat === 'job') {
          if (singleLabel) singleLabel.textContent = 'Paste Job Offer...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. Telegram video liking job or work from home offer';
            singleInput.value = 'Earn $500 per day liking YouTube videos. Telegram contact @hr_manager.';
          }
        } else if (cat === 'shop') {
          if (singleLabel) singleLabel.textContent = 'Paste Shop Link...';
          if (singleInput) {
            singleInput.placeholder = 'e.g. instagram.com/luxury_store_90_off';
            singleInput.value = 'https://instagram.com/stanley_warehouse_90_off';
          }
        }
      }
      document.getElementById('checker').scrollIntoView({ behavior: 'smooth' });
    }'''

# Replace setCategory function using regex
set_cat_pattern = re.compile(r'function setCategory\(.*?\n    \}', re.DOTALL)
if set_cat_pattern.search(text):
    text = set_cat_pattern.sub(new_set_cat, text, count=1)
    print("Replaced setCategory successfully.")

# 4. Update runCheck function
new_run_check = '''    function runCheck() {
      let textToCheck = '';
      if (activeToolCategory === 'email') {
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
      } else if (activeToolCategory === 'message') {
        textToCheck = document.getElementById('messageInput').value.trim();
        if (!textToCheck) {
          document.getElementById('messageInput').focus();
          return;
        }
      } else {
        const singleInput = document.getElementById('singleToolInput');
        textToCheck = singleInput ? singleInput.value.trim() : '';
        if (!textToCheck) {
          if (singleInput) singleInput.focus();
          return;
        }
      }

      const box = document.getElementById('resultBox');
      const loading = document.getElementById('resultLoading');
      const content = document.getElementById('resultContent');
      box.classList.remove('hidden');
      box.classList.add('result-box-animate');
      loading.classList.remove('hidden');
      content.classList.add('hidden');
      box.scrollIntoView({ behavior: 'smooth' });

      setTimeout(() => {
        loading.classList.add('hidden');
        content.classList.remove('hidden');
        const lower = textToCheck.toLowerCase();
        let score = 15;
        let redFlags = [];
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

        saveCheckToHistory({
          text: textToCheck.slice(0, 80),
          score: score,
          verdict: score > 70 ? 'High Risk' : score >= 40 ? 'Moderate' : 'Safe',
          date: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        });
      }, 700);
    }'''

run_check_pattern = re.compile(r'function runCheck\(.*?\n    \}', re.DOTALL)
if run_check_pattern.search(text):
    text = run_check_pattern.sub(new_run_check, text, count=1)
    print("Replaced runCheck successfully.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Tools clean up script completed successfully!")
