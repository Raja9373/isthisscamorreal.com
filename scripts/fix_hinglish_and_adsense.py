#!/usr/bin/env python3
"""
Fix:
1. AdSense TagError: No slot size for availableWidth=0 (wrapped in try/catch and width check, min-height).
2. Complete removal of Hinglish from default English HTML.
3. Added all missing keys to translations.en, translations.hi, translations.ur.
4. Quiz buttons: 🚨 Scam / ✅ Real.
"""

import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ================= 1. FIX ADSENSE ERROR =================
# Replace inline adsbygoogle pushes with safe try-catch blocks and min-height
old_ad1 = '''        <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9048615701580913" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'''

new_ad1 = '''        <ins class="adsbygoogle" style="display:block; min-height:90px; width:100%;" data-ad-client="ca-pub-9048615701580913" data-ad-slot="1234567890" data-ad-format="auto" data-full-width-responsive="true"></ins>
        <script>
          try {
            var adEl1 = document.currentScript && document.currentScript.previousElementSibling;
            if (!adEl1 || adEl1.offsetWidth > 0) {
              (adsbygoogle = window.adsbygoogle || []).push({});
            }
          } catch (e) {}
        </script>'''

old_ad2 = '''            <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-9048615701580913" data-ad-slot="9876543210" data-ad-format="auto" data-full-width-responsive="true"></ins>
            <script>(adsbygoogle = window.adsbygoogle || []).push({});</script>'''

new_ad2 = '''            <ins class="adsbygoogle" style="display:block; min-height:90px; width:100%;" data-ad-client="ca-pub-9048615701580913" data-ad-slot="9876543210" data-ad-format="auto" data-full-width-responsive="true"></ins>
            <script>
              try {
                var adEl2 = document.currentScript && document.currentScript.previousElementSibling;
                if (!adEl2 || adEl2.offsetWidth > 0) {
                  (adsbygoogle = window.adsbygoogle || []).push({});
                }
              } catch (e) {}
            </script>'''

if old_ad1 in html:
    html = html.replace(old_ad1, new_ad1)
    print("Fixed AdSense slot 1 with safe try-catch.")
else:
    print("Notice: old_ad1 not matched directly, checking regex")
    html = re.sub(
        r'<ins class="adsbygoogle"[^>]*data-ad-slot="1234567890"[^>]*></ins>\s*<script>\(adsbygoogle = window\.adsbygoogle \|\| \[\]\)\.push\(\{\}\);</script>',
        new_ad1,
        html
    )

if old_ad2 in html:
    html = html.replace(old_ad2, new_ad2)
    print("Fixed AdSense slot 2 with safe try-catch.")
else:
    print("Notice: old_ad2 not matched directly, checking regex")
    html = re.sub(
        r'<ins class="adsbygoogle"[^>]*data-ad-slot="9876543210"[^>]*></ins>\s*<script>\(adsbygoogle = window\.adsbygoogle \|\| \[\]\)\.push\(\{\}\);</script>',
        new_ad2,
        html
    )

# Add window error filter for TagError availableWidth=0 in head
tag_err_filter = '''  <!-- Suppress premature 0-width AdSense layout calculation errors -->
  <script>
    window.addEventListener('error', function(e) {
      if (e && e.message && (e.message.indexOf('availableWidth=0') !== -1 || e.message.indexOf('No slot size') !== -1)) {
        if (e.stopImmediatePropagation) e.stopImmediatePropagation();
        return true;
      }
    }, true);
  </script>
'''
if 'availableWidth=0' not in html:
    html = html.replace('<!-- Google AdSense Verification Script -->', tag_err_filter + '  <!-- Google AdSense Verification Script -->')
    print("Added AdSense error filter in head.")

# ================= 2. FIX QUIZ BUTTONS IN HTML =================
# Replace "🚨 Scam Hai (Scam)" with "🚨 Scam"
# Replace "✅ Real Hai (Legit)" with "✅ Real"
html = html.replace('<span>🚨 Scam Hai (Scam)</span>', '<span data-i18n="quizBtnScam">🚨 Scam</span>')
html = html.replace('<span>✅ Real Hai (Legit)</span>', '<span data-i18n="quizBtnReal">✅ Real</span>')
print("Updated quiz buttons in HTML.")

# ================= 3. FIX EMERGENCY & PREVENTION SECTION IN HTML =================
# Part A: Emergency Action Section
html = html.replace(
    'Paisa Kat Gaya? Ghabrao Mat - Abhi Ye 3 Kaam Karo (2 Minute Me)',
    "Money Lost? Don't Panic - Do These 3 Things Now (In 2 Minutes)"
)
html = html.replace(
    'Ye call bank ko paisa freeze karwata hai. Pehle ye karo.',
    'This call directly alerts the nodal bank officer to freeze the fraudulent transfer. Do this first.'
)
html = html.replace(
    '<h3 class="font-extrabold text-base text-navy dark:text-white" data-i18n="step2Title">Bank Ko Block Karwao</h3>',
    '<h3 class="font-extrabold text-base text-navy dark:text-white" data-i18n="step2Title">Block Your Bank / Card</h3>'
)
html = html.replace(
    '<span data-i18n="rbiNote">RBI Guidelines: 3 din ke andar report kiya to paisa wapas milne ke chance zyada hain.</span>',
    '<span data-i18n="rbiNote">Bank Refund Rule: Report within 3 days for the highest probability of recovering your money.</span>'
)
html = html.replace(
    '<h3 class="font-extrabold text-base text-navy dark:text-white" data-i18n="step3Title">Report Karvaayein</h3>',
    '<h3 class="font-extrabold text-base text-navy dark:text-white" data-i18n="step3Title">Report Fraud</h3>'
)
html = html.replace(
    '"1930 pe call + cybercrime.gov.in pe complaint - dono karo."',
    '"Call national helpline immediately and lodge a complaint on the official portal."'
)

# Part B: Prevention Section
html = html.replace(
    'Paisa Nahi Kata, Par Scam Tha? Kahan Block / Report Karein?',
    'Money Not Lost, But It Was a Scam? Where to Block / Report?'
)
html = html.replace(
    'Block: Domain block | Report: Isi site pe Report + cybercrime.gov.in',
    'Block: Domain block | Report: Report on this site + cybercrime.gov.in'
)
html = html.replace(
    '<span>🏛️</span> <span>Kaun Si Site Action Leti Hai? (Official Portals)</span>',
    '<span>🏛️</span> <span data-i18n="portalSectionTitle">Which Official Portal Takes Action?</span>'
)

# Modal Headings
html = html.replace(
    '<span>💡</span> <span>Kaise Hota Hai? (How the Scam Works)</span>',
    '<span>💡</span> <span data-i18n="modalHowItWorks">How This Scam Works</span>'
)
html = html.replace(
    '<span>🛡️</span> <span>Kya Karein? (Immediate Safety Actions)</span>',
    '<span>🛡️</span> <span data-i18n="modalWhatToDo">Immediate Safety Actions</span>'
)
html = html.replace(
    '<span>🏛️</span> <span>Kahan Report Karein? (Official Helplines)</span>',
    '<span>🏛️</span> <span data-i18n="modalHelplines">Official Reporting Helplines</span>'
)

print("Updated Emergency and Prevention HTML strings to clean English.")

# ================= 4. UPDATE TRANSLATIONS DICTIONARIES =================
# Let's inspect the translations object in html
# We need to add the keys to en, hi, and ur dictionaries

en_new_keys = '''        // Emergency and Prevention Keys
        victimTitle: "Money Lost? Don't Panic - Do These 3 Things Now (In 2 Minutes)",
        victimBadge: "EMERGENCY ACTION • 2 MINUTE PROTOCOL",
        victimSub: "Do not panic. Every minute counts to freeze the transaction before scammers withdraw the cash.",
        step1Label: "STEP 1: CALL HELPLINE NOW",
        step2Label: "STEP 2: BLOCK BANK / CARD",
        step2Title: "Block Your Bank / Card",
        step2Sub: "Open your bank mobile app or dial bank 24x7 emergency fraud line to freeze all active payment rails:",
        step3Label: "STEP 3: REPORT FRAUD",
        step3Title: "Report Fraud",
        step3Sub: "Formal complaint logs an official cyber acknowledgement number required for banking dispute settlements.",
        yellowBadge: "PREVENTION & REPORTING",
        yellowTitle: "Money Not Lost, But It Was a Scam? Where to Block / Report?",
        yellowSub: "Help stop the scam from spreading to friends and elderly family members by reporting it directly through official channels:",
        victimCountryLabel: "Your Country:",
        victimStep3SiteBtn: "Report on This Site",
        rbiNote: "Bank Refund Rule: Report within 3 days for the highest probability of recovering your money.",
        portalSectionTitle: "Which Official Portal Takes Action?",
        modalHowItWorks: "How This Scam Works",
        modalWhatToDo: "Immediate Safety Actions",
        modalHelplines: "Official Reporting Helplines",
        quizBtnScam: "🚨 Scam",
        quizBtnReal: "✅ Real",
'''

hi_new_keys = '''        // Emergency and Prevention Keys (Natural Bolchal Hindi)
        victimTitle: "Paisa Kat Gaya? Ghabrao Mat - Abhi Ye 3 Kaam Karo (2 Minute Me)",
        victimBadge: "EMERGENCY ACTION • 2 MINUTE ME KAREIN",
        victimSub: "Ghabrayein nahi. Fraudster paisa nikalne se pehle transfer freeze karwana zaroori hai.",
        step1Label: "STEP 1: TURANT CALL KAREIN",
        step2Label: "STEP 2: BANK / CARD BLOCK KAREIN",
        step2Title: "Bank Aur Card Block Karayein",
        step2Sub: "Apne bank app ya emergency helpline par call karke saare payments freeze karein:",
        step3Label: "STEP 3: COMPLAINT REGISTER KAREIN",
        step3Title: "Official Report Darj Karein",
        step3Sub: "Cyber complaint se official acknowledgement number milta hai jo bank dispute ke liye zaroori hai.",
        yellowBadge: "BACHAV AUR REPORT",
        yellowTitle: "Paisa Nahi Kata, Par Scam Tha? Kahan Block / Report Karein?",
        yellowSub: "Doosron ko bachane ke liye aur number block karwane ke liye official tareeqe se report karein:",
        victimCountryLabel: "Aapka Desh:",
        victimStep3SiteBtn: "Isi Site Par Report Karein",
        rbiNote: "Bank Niyam: 3 din ke andar report karne par paisa wapas milne ke chance sabse zyada hote hain.",
        portalSectionTitle: "Kaun Si Site Action Leti Hai?",
        modalHowItWorks: "Kaise Hota Hai? (Scam Ka Tareeqa)",
        modalWhatToDo: "Abhi Kya Karein? (Zaroori Qadam)",
        modalHelplines: "Official Helplines Aur Complaints",
        quizBtnScam: "🚨 Scam Hai",
        quizBtnReal: "✅ Asli Hai",
'''

ur_new_keys = '''        // Emergency and Prevention Keys (Bolchal Urdu)
        victimTitle: "Paisa Kat Gaya? Pareshan Na Hon - Foran Ye 3 Kaam Karein (2 Minute Me)",
        victimBadge: "EMERGENCY ACTION • 2 MINUTE PROTOCOL",
        victimSub: "Pareshan na hon. Fraudster raqam nikalne se pehle transfer rokna zaroori hai.",
        step1Label: "STEP 1: FORAN CALL KAREIN",
        step2Label: "STEP 2: BANK / CARD BLOCK KAREIN",
        step2Title: "Bank Aur Card Block Karwayein",
        step2Sub: "Apne bank app ya emergency helpline par call karke saare payments freeze karein:",
        step3Label: "STEP 3: COMPLAINT REGISTER KAREIN",
        step3Title: "Official Report Darj Karein",
        step3Sub: "Cyber complaint se official acknowledgement number milta hai jo bank dispute ke liye zaroori hai.",
        yellowBadge: "BACHAV AUR REPORT",
        yellowTitle: "Raqam Nahi Katti, Magar Scam Tha? Kahan Block / Report Karein?",
        yellowSub: "Doosron ko bachane ke liye aur number block karwane ke liye official tareeqe se report karein:",
        victimCountryLabel: "Aapka Mulk:",
        victimStep3SiteBtn: "Isi Site Par Report Karein",
        rbiNote: "Bank Qanoon: 3 din ke andar report karne par raqam wapas milne ke chance sabse zyada hote hain.",
        portalSectionTitle: "Kaun Si Site Action Leti Hai?",
        modalHowItWorks: "Yeh Fraud Kaise Hota Hai?",
        modalWhatToDo: "Foran Kya Karein?",
        modalHelplines: "Official Reporting Helplines",
        quizBtnScam: "🚨 Scam Hai",
        quizBtnReal: "✅ Asli Hai",
'''

# Insert keys into en:
html = html.replace('en: {\n        seoTitle:', 'en: {\n' + en_new_keys + '        seoTitle:')
# Insert keys into hi:
html = html.replace('hi: {\n        seoTitle:', 'hi: {\n' + hi_new_keys + '        seoTitle:')
# Insert keys into ur:
html = html.replace('ur: {\n        seoTitle:', 'ur: {\n' + ur_new_keys + '        seoTitle:')

print("Added all keys to translations dictionaries.")

# Save modified index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated and saved!")
