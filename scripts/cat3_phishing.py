# Category 3: Phishing / Message / Link Scams (38 scams)
cat3 = [
    {
        "name": "USPS / Postal Service Incomplete Address Smishing",
        "year": 2026,
        "is_latest": True,
        "country": "USA",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "Fake SMS claiming your package cannot be delivered due to missing house number, directing to cloned postal portal demanding redelivery fee.",
        "sample": "USPS: Your package has arrived at the distribution center but cannot be delivered due to incomplete street address. Please update: https://usps-redeliver-track.top/us",
        "source": "FBI IC3",
        "kaise": "1. Automated SMS gateways mass-blast thousands of phone numbers daily.\n2. Phishing link clones genuine postal service branding and asks for address.\n3. Requires $1.99 card payment, harvesting full credit card details and CVV for carding syndicates.",
        "flags": [
            "Sent from regular mobile number or international country code instead of postal 5-digit shortcode",
            "Urgent call to action claiming parcel will be returned within 12 hours",
            "Domain has unusual extension like .top, .xyz, .cc, or hyphens (usps-redeliver-track.top)",
            "You received notification without ordering any physical items online",
            "Website prompts for debit/credit card CVV to update a residential delivery address"
        ],
        "actions": [
            "Never tap links in unexpected package delivery text messages",
            "Track packages only by opening the official USPS, FedEx or UPS app directly",
            "Forward suspicious text messages to 7726 (SPAM) to notify carriers"
        ],
        "icon": "📦"
    },
    {
        "name": "India Post Customs Detention Smishing",
        "year": 2026,
        "is_latest": True,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "Fraudsters impersonate India Post or Customs Department claiming international courier is stuck and will be returned if address/fee is not updated.",
        "sample": "India Post: Your package #IN98214912 has arrived at depot but address is incorrect. Please update within 24hrs at https://indiapost-update-address.in to avoid return.",
        "source": "I4C India",
        "kaise": "1. Victims receive SMS with forged India Post sender header.\n2. Link leads to pixel-perfect replica of the India Post tracking portal.\n3. Asks user to pay nominal charge of Rs 25, harvesting netbanking or UPI credentials via fake payment gateway.",
        "flags": [
            "Sender ID is private 10-digit mobile number rather than registered government header (e.g. DZ-INPOST)",
            "Short deadline threatening return or legal fine for unclaimed courier",
            "Demands bank details or OTP for simple postal address modification",
            "Grammatical errors in Hindi or English notification text",
            "URL does not end in official government domain '.gov.in'"
        ],
        "actions": [
            "Check tracking numbers solely on official portal indiapost.gov.in",
            "Do not pay any fee on links received via SMS or WhatsApp",
            "Report fraudulent messages on National Cyber Crime Portal cybercrime.gov.in or helpline 1930"
        ],
        "icon": "📬"
    },
    {
        "name": "Quishing - QR Code Phishing on Parking Meters & Menus",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 94,
        "desc": "Malicious QR code stickers placed over legitimate QR codes on street parking meters, restaurant tables, or electric vehicle chargers.",
        "sample": "Scan this QR code with camera to pay $2.50 for parking space #42. Avoid $60 municipal parking citation.",
        "source": "FTC",
        "kaise": "1. Criminals print physical QR stickers and overlay them on authentic municipal meter signs.\n2. Scanning redirects driver to fake parking payment website mimicking ParkMobile or PayByPhone.\n3. Driver inputs card info; parking remains unpaid, resulting in both stolen card data and real city parking ticket.",
        "flags": [
            "QR code looks like a peel-off sticker overlaid on top of existing signage",
            "URL opened in browser does not match official municipal parking provider domain",
            "Browser gives SSL warning or shows unusual generic payment processor",
            "Website prompts for account passwords or excessive personal information",
            "Physical sticker edges are peeling or misaligned with metal plate"
        ],
        "actions": [
            "Pay via the official parking mobile app downloaded directly from official app stores",
            "Inspect QR codes carefully to verify they are not stickers pasted over permanent metal printing",
            "Never input credit card info if the URL bar appears unfamiliar"
        ],
        "icon": "📱"
    },
    {
        "name": "Royal Mail Redelivery Fee Smishing",
        "year": 2025,
        "is_latest": False,
        "country": "UK",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 95,
        "desc": "Scam text pretending to be Royal Mail demanding a £1.45 unpaid shipping surcharge before delivery can proceed.",
        "sample": "Royal Mail: Your item has been held due to unpaid shipping fee (£1.45). To reschedule delivery, visit: https://royal-mail-fee-settle.co.uk",
        "source": "Action Fraud",
        "kaise": "1. SMS sent claiming a parcel has unpaid customs or handling surcharge.\n2. Phishing link requests full name, address, date of birth, and debit card number.\n3. Criminals follow up hours later with phone call pretending to be bank fraud department.",
        "flags": [
            "Royal Mail only leaves physical grey 'Something for you' cards through letterboxes for unpaid fees",
            "Website domain is not royalmail.com",
            "Text sent from standard mobile number (+44 7xxx)",
            "Requests mother's maiden name or online banking credentials during checkout",
            "Immediate threat of parcel destruction"
        ],
        "actions": [
            "Check Royal Mail official site directly for true tracking status",
            "Forward scam text messages to 7726 for UK telecommunication network investigation",
            "Report phishing attempts to Action Fraud on 0300 123 2040"
        ],
        "icon": "📮"
    },
    {
        "name": "Highway Toll Smishing (E-ZPass, SunPass, FasTrak)",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 94,
        "desc": "Urgent texts claiming you have an unpaid toll balance of $3.50 to $11.50 with threat of $50 late fee or driver's license suspension.",
        "sample": "Toll Services: You have an unpaid toll invoice of $6.25 on I-95. Settle immediately to avoid $50 late penalty: https://toll-invoices-pay.com",
        "source": "FBI IC3",
        "kaise": "1. Coordinated smishing campaigns target area codes where express toll lanes operate.\n2. Fake portal shows realistic toll agency logo and mock invoice.\n3. Steals credit card and social security details under guise of driver verification.",
        "flags": [
            "Toll agencies never send unsolicited text messages demanding immediate payment",
            "Domain is not official state toll operator website (.gov or authorized toll portal)",
            "Recipient does not drive on toll roads or own an automobile",
            "High pressure threat of immediate license suspension or credit score destruction",
            "Payment screen does not show specific timestamp, toll plaza location, or vehicle license plate"
        ],
        "actions": [
            "Log in only via your registered state toll authority account or official app",
            "File complaint with FBI IC3 at ic3.gov",
            "Block sender and delete text message without opening link"
        ],
        "icon": "🛣️"
    },
    {
        "name": "FASTag Account Suspension & Blacklist Alert",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "SMS warning that FASTag KYC is pending and toll tag will be deactivated or blacklisted within 24 hours.",
        "sample": "Dear Customer, Your NHAI FASTag KYC has expired. Your tag will be blocked on highway tolls tonight. Update now: https://fastag-kyc-nhai.top",
        "source": "I4C India",
        "kaise": "1. Exploits nationwide FASTag KYC compliance deadlines.\n2. Links to fake portal asking vehicle registration number and mobile OTP.\n3. Uses entered OTP to drain linked prepaid wallet or bank account.",
        "flags": [
            "Link uses non-government domain instead of official bank portal or ihmcl.co.in",
            "Urgent deadline threatening toll plaza denial or double toll penalty",
            "Asks for bank account password or UPI PIN to verify FASTag",
            "Message sent from personal 10-digit number",
            "Demands installation of APK file for KYC verification"
        ],
        "actions": [
            "Verify FASTag status only through issuer bank app or IHMCL portal",
            "Never enter UPI PIN or bank password to complete KYC updates",
            "Call your FASTag issuing bank customer care number on physical card"
        ],
        "icon": "🚗"
    },
    {
        "name": "Electricity Power Disconnection Tonight SMS",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "SMS warning electricity power supply will be cut off at 9:30 PM tonight due to previous month unpaid bill, providing fake electricity officer mobile number.",
        "sample": "Dear consumer, Your Electricity power will be disconnected tonight at 9.30 pm from electricity office because your previous month bill was not updated. Please immediately contact our power officer 9811XXXXXX. Thanks.",
        "source": "I4C India",
        "kaise": "1. Sends frightening text late in the afternoon so victims fear spending night in dark.\n2. Scared victim calls provided officer mobile number.\n3. Fraudster instructs victim to install AnyDesk or TeamViewer APK to pay Rs 10 test fee, draining entire bank balance.",
        "flags": [
            "Threatens imminent power disconnection within hours (electricity boards give weeks of written notice)",
            "Directs customer to call private mobile phone number rather than official discom helpline",
            "Sent from personal mobile number instead of utility sender header (e.g. BSES, TATA, MSEDCL)",
            "Officer asks caller to download APK file or screen sharing software",
            "Demands instant payment via unknown UPI link"
        ],
        "actions": [
            "Never call phone numbers provided inside suspicious SMS warnings",
            "Check true bill status on official state electricity board mobile app or consumer portal",
            "Never install remote control apps like AnyDesk, RustDesk or TeamViewer requested by callers"
        ],
        "icon": "⚡"
    },
    {
        "name": "Bank PAN / KYC Expiry Account Blocked Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 98,
        "desc": "SMS claiming bank account has been suspended or frozen due to unlinked PAN card or missing re-KYC documentation.",
        "sample": "Dear SBI/HDFC User, your bank account has been blocked due to unlinked PAN card. Kindly click https://sbi-pan-kyc-verify.com to re-activate within 24 hours.",
        "source": "I4C India",
        "kaise": "1. Mass smishing attacks trigger panic about inaccessible bank funds.\n2. Phishing link opens replica of netbanking login portal.\n3. Captures customer ID, password, date of birth, and triggers high-value transfer demanding victim's OTP.",
        "flags": [
            "Banks never send links in SMS asking customers to update KYC or PAN details",
            "Short deadline threatening immediate freeze of banking services",
            "Website domain does not match official bank URL (e.g. onlinesbi.sbi or hdfcbank.com)",
            "Webpage prompts for Internet banking password, debit card PIN, and OTP simultaneously",
            "SMS received from standard 10-digit mobile number"
        ],
        "actions": [
            "Banks mandate physical branch visit or official netbanking login for re-KYC",
            "Never click links inside SMS mentioning account suspension",
            "Call bank customer service immediately to lock netbanking if credentials entered"
        ],
        "icon": "🏦"
    },
    {
        "name": "Netflix & Streaming Subscription Suspension Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 91,
        "desc": "Emails and SMS stating your Netflix, Disney+ or Spotify membership is suspended due to billing decline, linking to fake credit card update page.",
        "sample": "Netflix: We were unable to authorize your latest membership payment. Please update your billing details here to avoid service disruption: https://netflix-account-restart.net",
        "source": "FTC",
        "kaise": "1. Mass phishing campaigns target millions of streaming subscribers.\n2. Page mirrors authentic streaming service login interface.\n3. Harvests user credentials and full credit card details including CVV and billing address.",
        "flags": [
            "Sender email address is not from @netflix.com or official brand domain",
            "Greeting is generic ('Dear Customer') instead of account holder name",
            "Link destination displays suspicious third-party URL",
            "Prompts for sensitive card data without requiring 2FA login verification",
            "Threatens immediate termination of account within 24 hours"
        ],
        "actions": [
            "Navigate directly to netflix.com in browser or open installed TV/mobile app to view billing status",
            "Forward phishing email to phishing@netflix.com",
            "Report scam URL to Google Safe Browsing and FTC"
        ],
        "icon": "📺"
    },
    {
        "name": "Apple ID / iCloud Device Lost & Found Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "Victims of stolen iPhones receive SMS pretending to be Apple Find My, stating missing device was found and requesting Apple ID login to view location.",
        "sample": "Apple Find My: Your lost iPhone 15 Pro has been located near Central Station at 14:22. View real-time location map: https://apple-findmy-location-auth.co",
        "source": "Action Fraud",
        "kaise": "1. Thieves steal iPhone and obtain owner's emergency contact number from lock screen.\n2. Automated SMS sent pretending iPhone is powered on and found.\n3. Fake iCloud login captures Apple ID password, allowing thieves to remove Activation Lock and wipe phone for resale.",
        "flags": [
            "Apple Find My never sends SMS with links to enter Apple ID password to view location",
            "Domain is not official apple.com or icloud.com",
            "Message arrives shortly after device was physically stolen or misplaced",
            "Page demands two-factor authentication verification code immediately",
            "Sender ID is random web email or international number"
        ],
        "actions": [
            "Check device status exclusively on official portal icloud.com/find",
            "Never enter Apple ID or iCloud password into links received via SMS",
            "Keep Lost Mode active on iCloud to prevent thieves from wiping device"
        ],
        "icon": "🍏"
    },
    {
        "name": "Tax Refund Phishing (IRS / HMRC / FBR)",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 95,
        "desc": "Emails or SMS claiming you are owed a large tax rebate ($480 or £650), directing to fake tax portal asking for bank account and card details to claim funds.",
        "sample": "HMRC: You have an outstanding tax refund of £485.20 from fiscal year 2024. Submit your direct deposit claim within 48h: https://gov-hmrc-rebates-claim.org",
        "source": "Action Fraud",
        "kaise": "1. Dispatched during spring and year-end annual tax filing seasons.\n2. Phishing form requests full identity details (SSN, National Insurance number, birth date).\n3. Requires debit card number, expiration, and CVV to 'deposit refund', which scammers immediately drain.",
        "flags": [
            "Tax authorities never initiate contact by email or text message to issue refunds",
            "Government websites use official top-level domains (.gov or .gov.uk)",
            "Refunds are never sent by asking for a debit card CVV number",
            "Urgent deadline warning that refund will expire or revert to treasury",
            "Spelling errors in tax authority legal disclosures"
        ],
        "actions": [
            "Check refund status directly on irs.gov or gov.uk online tax account",
            "Forward IRS phishing emails to phishing@irs.gov",
            "Forward HMRC phishing messages to phishing@hmrc.gov.uk"
        ],
        "icon": "💸"
    },
    {
        "name": "SIM Swap Verification & 5G Upgrade Trap",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "Messages claiming your 4G SIM will stop working unless you upgrade to 5G by forwarding a carrier porting code or 20-digit SIM number.",
        "sample": "Airtel/Jio: Your 4G SIM service will expire in 12 hours. To upgrade to Free 5G Unlimited, forward SIM <20-digit code> to 121 immediately.",
        "source": "I4C India",
        "kaise": "1. Scammers obtain victim's bank details or passwords via earlier breach.\n2. Tricking victim into forwarding SIM activation code transfers phone number to fraudster's physical SIM.\n3. Victim's phone shows 'No Service' while scammers intercept OTPs and empty bank accounts.",
        "flags": [
            "Telecom carriers do not require users to forward SMS codes to upgrade to 5G",
            "SMS instructs sending SIM serial number to customer service porting number",
            "Threat of immediate service termination within 12 hours",
            "Sudden loss of cellular network signal on your phone following the message",
            "Caller claims to be telecom engineer assisting with speed optimization"
        ],
        "actions": [
            "Never forward SMS codes or SIM numbers received on your handset",
            "If phone suddenly loses network connection, contact telecom provider immediately from another phone",
            "Notify bank fraud helpline immediately if SIM swap is suspected"
        ],
        "icon": "📶"
    },
    {
        "name": "WhatsApp Account Verification Code Interception",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "A friend's hacked WhatsApp account texts you asking for a 6-digit code sent to your phone by mistake, which is actually your own WhatsApp registration OTP.",
        "sample": "Hey sorry, I accidentally sent my WhatsApp 6-digit code to your phone number by mistake! Can you please send it back to me quickly? It is very urgent.",
        "source": "Action Fraud",
        "kaise": "1. Fraudster hacks user A's account and targets contacts in their address book.\n2. Fraudster attempts to register WhatsApp on a new phone using victim's phone number.\n3. Victim receives official WhatsApp SMS code and forwards it to 'friend', instantly losing account access.",
        "flags": [
            "A friend asks for a 6-digit verification code sent to your phone",
            "Official SMS clearly states: 'Do not share this code with anyone'",
            "Unusual conversational tone or desperate urgency from someone you know",
            "Request occurs out of nowhere on social messaging apps",
            "After sharing code, you are immediately logged out of WhatsApp on your phone"
        ],
        "actions": [
            "Never share verification codes or OTPs with anyone, even close family or friends",
            "Enable Two-Step Verification PIN inside WhatsApp Settings > Account",
            "Call your friend on cellular phone to inform them their account is compromised"
        ],
        "icon": "💬"
    },
    {
        "name": "Fake Airline Cancellation & Flight Reschedule SMS",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "SMS alerting that your upcoming flight is cancelled due to weather or technical fault, directing you to call a fake airline support number for refund.",
        "sample": "Delta/IndiGo Alert: Flight DL-491 has been cancelled due to technical difficulties. Call priority rebooking desk +1-888-XXX-XXXX immediately to claim refund.",
        "source": "FTC",
        "kaise": "1. Scammers track travel disruptions or blast holiday traveler pools.\n2. Call connects to fake travel call center.\n3. Operator demands cancellation fee or card details to reschedule flight tickets.",
        "flags": [
            "SMS does not include passenger name or booking reference PNR number",
            "Phone number provided is not the official airline customer care helpline",
            "Demands credit card payment to reissue ticket on cancelled flight",
            "Agent creates intense pressure claiming next flight has only 1 seat left",
            "Website or caller requests remote phone access software"
        ],
        "actions": [
            "Check flight status directly in the airline official mobile app or airport website",
            "Never dial phone numbers provided in unverified SMS alerts",
            "Verify booking using PNR on the airline's official domain"
        ],
        "icon": "✈️"
    },
    {
        "name": "Social Media Copyright Infringement Suspension DM",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 92,
        "desc": "Direct message on Instagram, Facebook or X claiming copyright violation on your post, warning account deletion within 24h unless verified via link.",
        "sample": "Meta Copyright Center: A copyright violation has been detected on your account. If you think this is a mistake, appeal here: https://meta-copyright-appeals-form.biz",
        "source": "FTC",
        "kaise": "1. Bots target creators and business pages on Instagram and Facebook.\n2. Link mimics Meta or Twitter support authentication form.\n3. Steals account login, backup codes, and changes recovery email immediately.",
        "flags": [
            "Meta and Instagram never send copyright notices via Direct Message or chat",
            "Official notices appear exclusively in Settings > Help > Support Requests",
            "Domain has unusual extensions (.biz, .cfd, .click)",
            "Sender profile has no official verification badge and has 0 posts",
            "Demands your current password and 2FA recovery backup codes"
        ],
        "actions": [
            "Ignore and report Instagram direct messages claiming copyright violations",
            "Check authentic account status inside official Instagram Settings > Support Requests",
            "Turn on two-factor authentication using authenticator apps rather than SMS"
        ],
        "icon": "📸"
    },
    {
        "name": "Credit Card Points Expiry Reward Voucher Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 95,
        "desc": "SMS claiming reward points worth Rs 8,450 on your credit card will expire today, urging you to redeem for cash into bank account via link.",
        "sample": "Dear customer, Your 9,850 HDFC/SBI credit card reward points worth Rs 9,850 are expiring today. Redeem cash directly into your account: https://reward-points-redeem.cc",
        "source": "I4C India",
        "kaise": "1. Sends enticing text during festival seasons when spending is high.\n2. Phishing link asks victim to select bank and enter credit card number, CVV, and expiry date.\n3. Scammers initiate transaction on overseas portal and prompt victim for OTP under pretense of reward credit.",
        "flags": [
            "Banks never redeem reward points for direct cash deposits via unauthenticated third-party links",
            "SMS sent from random private number instead of official bank header",
            "URL is not the official credit card reward portal (e.g. smartbuy or sbicard.com)",
            "Page asks for CVV and OTP to credit reward money",
            "Urgent deadline warning that points will lapse at midnight"
        ],
        "actions": [
            "Redeem reward points only through official mobile banking app or card statement portal",
            "Never enter CVV or card details to receive rewards or cashback",
            "Forward fraudulent SMS to 1930 and report to bank fraud department"
        ],
        "icon": "💳"
    },
    {
        "name": "Healthcare / NHS Prescription Fee Phishing",
        "year": 2024,
        "is_latest": False,
        "country": "UK",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 91,
        "desc": "Fake NHS SMS stating prescription or medical survey is pending with a small delivery charge of £2.10.",
        "sample": "NHS: You have a pending prescription delivery from your GP surgery. Confirm delivery and pay handling fee (£2.10) at: https://nhs-prescription-verify.org",
        "source": "Action Fraud",
        "kaise": "1. Targets elderly or vulnerable individuals expecting medication.\n2. Link mimics authentic NHS portal design.\n3. Collects debit card details and health information for identity theft.",
        "flags": [
            "NHS never asks for payment via links sent in SMS messages",
            "Website domain does not end in '.nhs.uk'",
            "Sender number is a standard international or mobile number",
            "Prompts for mother's maiden name or banking password",
            "Received without any recent GP appointment or consultation"
        ],
        "actions": [
            "Contact your local GP surgery or pharmacy directly using their verified number",
            "Forward scam SMS to 7726",
            "Report NHS impersonation to Action Fraud"
        ],
        "icon": "🩺"
    },
    {
        "name": "Gas Subsidy / LPG Cylinder KYC Suspension SMS",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "SMS warning that subsidized cooking gas cylinder deliveries will be suspended unless e-KYC is completed on third-party link.",
        "sample": "Indane/HP Gas: Your LPG subsidy is blocked due to incomplete biometric KYC. Update documents now to avoid commercial rates: https://lpg-kyc-subsidy.top",
        "source": "I4C India",
        "kaise": "1. Exploits government mandates regarding LPG cylinder biometric verification.\n2. Link asks for Aadhaar number, bank details, and installs malicious APK.\n3. APK intercepts incoming banking SMS to authorize fraudulent transactions.",
        "flags": [
            "Gas agencies mandate biometric KYC in person at the local distributor agency",
            "Domain has unusual extension like .top or .xyz",
            "Webpage prompts user to download an Android APK file",
            "Threatens loss of cooking gas supply or subsidy within 24 hours",
            "Sent from private mobile number"
        ],
        "actions": [
            "Complete LPG KYC in person at your authorized gas distributor showroom",
            "Never download APK files sent over WhatsApp or SMS links",
            "Check official subsidy status on mylpg.in portal"
        ],
        "icon": "🔥"
    },
    {
        "name": "eChallan Traffic Violation Fine Scam",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "SMS stating traffic violation fine of Rs 1,000 recorded against your vehicle with threat of court summons if not paid via link within 24 hours.",
        "sample": "Traffic Police: Challan #DL5912 has been issued against vehicle DL01XX for overspeeding. Pay Rs 1000 within 24h to avoid court notice: https://echallan-parivahan-gov.in.top",
        "source": "I4C India",
        "kaise": "1. Fraudsters obtain vehicle numbers from parking lots or public databases.\n2. Phishing link clones national Parivahan eChallan portal.\n3. Download button installs malware APK or routes to fake payment gateway stealing card credentials.",
        "flags": [
            "Official traffic police notices are sent from authorized sender IDs (e.g. TRF-POL)",
            "URL does not end in '.gov.in' (e.g. uses spoofed domain echallan-parivahan.top)",
            "Message does not mention exact location, photo proof of violation, or vehicle registration",
            "Prompts download of APK file named 'eChallan.apk'",
            "Demands instant payment to avoid immediate arrest warrant"
        ],
        "actions": [
            "Check traffic challans only on official Ministry portal: echallan.parivahan.gov.in",
            "Never download .apk files to pay traffic fines",
            "Report spoofed SMS to cybercrime.gov.in and National Cyber Helpline 1930"
        ],
        "icon": "🚨"
    },
    {
        "name": "WhatsApp Pink / WhatsApp Gold APK Phishing",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "Viral message offering exclusive pink or gold WhatsApp theme with secret new features, installing trojan malware that spreads itself to all contacts.",
        "sample": "WhatsApp Pink launched with exciting new features! Download official update now: https://whatsapp-pink-theme.download/update.apk",
        "source": "I4C India",
        "kaise": "1. Viral forward shared across group chats promising aesthetic redesign.\n2. User downloads APK and grants Accessibility and Notification permissions.\n3. Malware hijacks SMS and WhatsApp, automatically texting malicious download link to all phone contacts.",
        "flags": [
            "Prompts user to install an APK file from outside the Google Play Store or Apple App Store",
            "Promises unofficial cosmetic themes (Pink, Gold, Transparent) for WhatsApp",
            "Requests sensitive permissions: Accessibility Services, Read SMS, and Notification Access",
            "Auto-forwards itself to other WhatsApp contacts and groups without user consent",
            "Meta has never released any separate colored editions of WhatsApp"
        ],
        "actions": [
            "Uninstall suspicious apps immediately under Android Settings > Apps",
            "Revoke Accessibility permissions for unfamiliar applications",
            "Download WhatsApp updates exclusively from official Google Play Store or Apple App Store"
        ],
        "icon": "🌸"
    },
    {
        "name": "Fake Charitable Donation & Disaster Relief Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 92,
        "desc": "Crowdfunding links claiming to raise emergency medical funds for earthquake victims or injured children, pocketing 100% of donations.",
        "sample": "Urgent: Thousands displaced in tragic earthquake. Every $10 feeds a family of four. Donate through official relief fund: https://emergency-relief-aid.org/donate",
        "source": "FTC",
        "kaise": "1. Scammers launch emotional campaigns within 2 hours of breaking natural disaster news.\n2. Phishing websites use stolen news photos and tragic testimonials.\n3. Donations via credit card or crypto flow directly into criminal offshore wallets.",
        "flags": [
            "Domain created within hours or days of the disaster breaking in news",
            "Charity is not registered with Charity Navigator, GiveWell, or GuideStar",
            "Demands payment via cryptocurrency, gift cards, or direct wire transfer",
            "Vague descriptions of how relief funds will be distributed on the ground",
            "High emotional pressure demanding immediate contribution"
        ],
        "actions": [
            "Donate exclusively through well-established registered charities (Red Cross, UNICEF, Doctors Without Borders)",
            "Check charity legitimacy on charitynavigator.org or give.org",
            "Never donate via untraceable methods like crypto or prepaid gift cards"
        ],
        "icon": "🕊️"
    },
    {
        "name": "Fake University Exam / Degree Verification Fee Phishing",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 90,
        "desc": "SMS to college students claiming examination admit card is withheld due to pending document verification fee.",
        "sample": "University Notice: Your Semester exam admit card is blocked. Pay Rs 450 verification fee before 5 PM today to download: https://university-admit-card-fee.in",
        "source": "I4C India",
        "kaise": "1. Scammers harvest student rolls or broadcast during exam seasons.\n2. Fake college portal requests roll number and bank credentials.\n3. Empties student savings accounts via fraudulent debit card transactions.",
        "flags": [
            "University never sends fee payment links via private SMS",
            "URL does not match official university domain (.ac.in or .edu)",
            "Short deadline threatening exam disqualification",
            "Demands card PIN or netbanking password on payment page",
            "Sender is an unverified mobile phone number"
        ],
        "actions": [
            "Verify exam notifications directly on your college official website or notice board",
            "Contact your college examination branch in person",
            "Never pay exam fees through unverified WhatsApp or SMS links"
        ],
        "icon": "🎓"
    },
    {
        "name": "Postal Forwarding Redirection Fee Smishing",
        "year": 2025,
        "is_latest": False,
        "country": "Australia",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 94,
        "desc": "SMS impersonating Australia Post stating mail forwarding request requires credit card verification fee.",
        "sample": "AusPost: Your mail redirection service is suspended due to invalid billing details. Update payment here: https://auspost-redirection-settle.top",
        "source": "Scamwatch",
        "kaise": "1. SMS sent across Australian mobile prefixes.\n2. Phishing link clones AusPost myPost portal.\n3. Steals credit card number, CVV, and mobile banking login details.",
        "flags": [
            "Australia Post will never email or text asking for personal information or payment for mail delivery",
            "Sender number is not official 13-POST service",
            "URL does not end in '.auspost.com.au'",
            "Prompts for credit card CVV and expiration date",
            "Urgent deadline threatening return of all postal mail"
        ],
        "actions": [
            "Log in directly to official myPost account at auspost.com.au",
            "Report scam messages to Scamwatch at scamwatch.gov.au",
            "Forward suspicious texts to Australian cyber authority"
        ],
        "icon": "🦘"
    },
    {
        "name": "Airline Frequent Flyer Points Expiration Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 91,
        "desc": "Emails claiming your Emirates Skywards, British Airways Avios, or United MileagePlus miles will expire unless you log in to redeem a free flight voucher.",
        "sample": "Emirates Skywards: 45,000 miles in your account will expire on Friday. Redeem for a complimentary round-trip voucher now: https://skywards-miles-renewal.com",
        "source": "FTC",
        "kaise": "1. Spoofs airline loyalty communication branding.\n2. Login page captures frequent flyer credentials.\n3. Criminals immediately transfer accumulated airline points or book resale flight tickets.",
        "flags": [
            "Sender address is not from official airline domain (e.g. emirates.com)",
            "Directs to an unverified third-party web domain",
            "Offers unrealistic free business class vouchers for expiring miles",
            "Prompts for account password and credit card number to 're-activate' miles",
            "Account number or loyalty tier not mentioned in email body"
        ],
        "actions": [
            "Log in to frequent flyer accounts only via official airline mobile app or verified website",
            "Enable multi-factor authentication on all travel and loyalty accounts",
            "Report loyalty phishing to airline security team"
        ],
        "icon": "✈️"
    },
    {
        "name": "Cloud Storage Quota Full Deletion Warning Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "Emails warning your Google Drive, OneDrive, or iCloud storage is 99% full and all photos and files will be deleted within 24 hours unless you pay $1.99.",
        "sample": "Google Storage Alert: Your Google Drive and Photos storage is 99.8% full. Files will be permanently deleted in 24h. Upgrade 100GB for $0.99: https://storage-google-upgrade.top",
        "source": "FTC",
        "kaise": "1. Mass emails exploit anxiety over losing irreplaceable family photos and documents.\n2. Phishing link clones Google or Microsoft login page.\n3. Captures account password and credit card number.",
        "flags": [
            "Sender email address is random webmail rather than @google.com or @microsoft.com",
            "Domain has unusual URL extension like .top or .shop",
            "Extreme threat of total data deletion within 24 hours (providers give months of grace period)",
            "Login screen does not recognize your saved browser credentials",
            "Prompts for debit card details on unencrypted page"
        ],
        "actions": [
            "Check true storage usage directly in Google Drive or Microsoft account settings",
            "Never click payment links inside alarming storage warning emails",
            "Report phishing email using Gmail 'Report Phishing' button"
        ],
        "icon": "☁️"
    },
    {
        "name": "WhatsApp Group Ban Appeal Phishing",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 92,
        "desc": "SMS or WhatsApp message claiming your phone number has been flagged for violating community guidelines and will be banned in 12 hours.",
        "sample": "WhatsApp Support: Your phone number +91-XXXXX has been reported for spam activity. Appeal your permanent suspension here: https://whatsapp-support-appeals.me",
        "source": "Action Fraud",
        "kaise": "1. Targets heavy WhatsApp users and community group admins.\n2. Link asks for phone number, 6-digit registration code, and 2FA PIN.\n3. Hijacks account and extorts user or asks group members for emergency cash.",
        "flags": [
            "WhatsApp never communicates policy bans via private text messages or third-party links",
            "Official ban appeals are submitted inside the official app on the ban screen",
            "Domain is not whatsapp.com",
            "Prompts for 6-digit SMS verification code",
            "Urgent 12-hour deadline threatening permanent loss of contacts"
        ],
        "actions": [
            "Submit support tickets only through WhatsApp App > Settings > Help > Contact Us",
            "Never enter 6-digit verification codes into web forms",
            "Enable Two-Step Verification inside WhatsApp settings"
        ],
        "icon": "🛑"
    },
    {
        "name": "eSIM Profile Download Phishing Trap",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "Victims are guided to scan a malicious eSIM QR code under guise of network speed upgrade, immediately transferring their cellular phone number to attacker's device.",
        "sample": "Verizon/Jio: Your complimentary 5G Ultra eSIM profile is ready for activation. Scan this QR code in phone cellular settings to activate high-speed data: [QR Code]",
        "source": "FBI IC3",
        "kaise": "1. Attacker purchases victim's personal data or impersonates carrier customer care.\n2. Sends eSIM QR code via email or WhatsApp pretending it is an upgrade profile.\n3. Scanning code instantly ports phone number to attacker's handset, giving full OTP access to bank accounts.",
        "flags": [
            "Carrier never emails unrequested eSIM QR codes without verified customer portal request",
            "Scanning unknown eSIM QR code from email or WhatsApp will transfer your cellular line",
            "Caller claims eSIM download is mandatory to retain existing phone service",
            "Phone cellular network disconnects shortly after scanning",
            "Sender uses free email domain (e.g. jiosupport@gmail.com)"
        ],
        "actions": [
            "Never scan eSIM QR codes unless you personally requested eSIM transfer inside carrier store or official app",
            "If your cellular service disconnects unexpectedly, contact carrier fraud desk immediately",
            "Freeze linked netbanking and UPI accounts immediately if unauthorized eSIM transfer occurs"
        ],
        "icon": "📲"
    },
    {
        "name": "Tinder / Dating App Verification Code Scam",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 91,
        "desc": "A match on Tinder, Bumble or Hinge asks you to click a link to verify your identity on a 'dating safety site' before they will agree to meet in person.",
        "sample": "Before we meet for coffee, can you get free safety verification? It protects both of us. It only takes 1 minute: https://dating-safety-id-check.com",
        "source": "FTC",
        "kaise": "1. Catfish profile matches with victim and suggests meeting for a date.\n2. Refuses to meet unless victim verifies identity on fake 'Dating Safety Registry'.\n3. Verification page demands credit card for $1.95 trial, signing victim up for recurring monthly $49.99 subscription charges.",
        "flags": [
            "Match refuses to meet in public coffee shop without third-party website verification",
            "Site claims to be mandatory government or police safety verification system",
            "Demands credit card details for a supposedly free background check",
            "Match profile disappears after credit card details are submitted",
            "Site terms hidden in tiny print bill high recurring monthly charges"
        ],
        "actions": [
            "Never enter credit card details on third-party verification sites recommended by dating app matches",
            "Real dating safety features (like photo verification) are free and built directly into Tinder and Bumble",
            "Report match profile to dating app moderators"
        ],
        "icon": "❤️"
    },
    {
        "name": "Fake Booking.com Hotel Payment Confirmation Link",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 96,
        "desc": "Messages received inside official Booking.com app from actual booked hotel (compromised account) claiming reservation will be cancelled unless card is re-verified via external link.",
        "sample": "Booking.com Hotel Desk: Due to updated security policies, your reservation #89214 at Grand Hotel requires card re-authorization within 12h: https://booking-reservation-auth.net",
        "source": "Action Fraud",
        "kaise": "1. Hackers compromise hotel's official Booking.com partner extranet account.\n2. Send phishing messages directly through authentic Booking.com in-app messaging system.\n3. Link directs guest to clone payment gateway stealing credit card funds.",
        "flags": [
            "Message directs you to pay through an external web link rather than within Booking.com official app",
            "Urgent 12 or 24 hour cancellation threat for a booking already confirmed with valid credit card",
            "External payment domain is not booking.com",
            "Hotel staff claims payment declined even though bank shows funds reserved",
            "Demands credit card verification via instant debit"
        ],
        "actions": [
            "Never click payment links sent inside chat messages, even from verified hotel accounts",
            "Pay for reservations exclusively through official Booking.com checkout page",
            "Call hotel directly using phone number listed on official hotel website"
        ],
        "icon": "🏨"
    },
    {
        "name": "Customs Duty Gift Parcel Ransom Phishing",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 95,
        "desc": "SMS or WhatsApp from fake customs officer claiming a foreign friend has sent valuable gifts (gold, iPhones, dollars) detained at airport customs requiring clearance fee.",
        "sample": "Customs Delhi Airport: Parcel from UK containing electronic items and currency is on hold. Clear customs fee Rs 28,500 to account 91823XXXXX within 6 hours.",
        "source": "I4C India",
        "kaise": "1. Romance scammer tells victim they sent expensive gifts or jewelry from abroad.\n2. Accomplice calls or texts pretending to be airport customs commissioner.\n3. Demands clearance fee, then anti-money laundering fee, siphoning lakhs from victim.",
        "flags": [
            "Customs department never asks individuals to transfer customs duty into personal savings accounts",
            "Customs duty is never payable via UPI or personal IMPS transfers",
            "Foreign gifts containing currency or bullion are illegal to import without prior declarations",
            "Caller threatens immediate arrest by CBI or Police if money is not transferred within hours",
            "Sender cannot provide official Customs Bill of Entry document"
        ],
        "actions": [
            "Never pay money to claim surprise parcels or overseas gifts from internet acquaintances",
            "Customs duty is collected exclusively by official courier companies on delivery with printed tax receipts",
            "Report syndicate numbers to cybercrime.gov.in"
        ],
        "icon": "🛃"
    },
    {
        "name": "Fake Loan Approval & Disbursal Fee SMS",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 94,
        "desc": "SMS promising pre-approved instant loan of Rs 5,00,000 at 2% interest with zero collateral, requiring upfront processing fee of Rs 2,500 to release loan amount.",
        "sample": "Congratulations! Loan of Rs 5,00,000 pre-approved under PM Mudra Scheme at 2% interest. No cibil score required. Pay Rs 2,499 file charge to disburse: https://mudra-loan-apply.in",
        "source": "I4C India",
        "kaise": "1. Targets individuals seeking quick financial assistance or low credit borrowers.\n2. Phishing portal asks for PAN, Aadhaar, and upfront documentation/processing fee.\n3. After processing fee is paid, scammers demand insurance fee and GST fee, never disbursing any loan.",
        "flags": [
            "Legitimate banks never demand advance processing fees transferred via UPI or personal accounts",
            "Processing fees are deducted directly from the disbursed loan amount",
            "Unrealistically low interest rate (2% - 3%) with no credit check required",
            "Sent from personal mobile number rather than bank shortcode",
            "Uses government scheme names (Mudra, PMEGP) to mislead victims"
        ],
        "actions": [
            "Apply for loans exclusively through RBI-registered banks and verified NBFC branches",
            "Never pay advance money to get a loan sanctioned or disbursed",
            "Check NBFC registration status on official RBI portal rbi.org.in"
        ],
        "icon": "💰"
    },
    {
        "name": "Fake E-Commerce Order Cancellation SMS",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 92,
        "desc": "Text message alerting that your Amazon or Flipkart order for an expensive item ($999 laptop) has been confirmed, instructing you to click link to cancel if unauthorized.",
        "sample": "Amazon: Your order for Apple MacBook Pro ($1,299) has been processed. If you did NOT place this order, cancel immediately at: https://amazon-orders-dispute.top",
        "source": "FTC",
        "kaise": "1. Sends fake purchase confirmation causing victim to panic about stolen credit card.\n2. Victim clicks link to cancel the non-existent order.\n3. Phishing page captures Amazon login credentials and credit card information.",
        "flags": [
            "No order appears when checking your real Amazon or Flipkart account in app",
            "Link domain is not amazon.com or flipkart.com",
            "Message sent from random phone number instead of official brand SMS sender",
            "Page demands credit card number and CVV to 'cancel the transaction'",
            "Grammar or punctuation mistakes in SMS alert text"
        ],
        "actions": [
            "Check 'Your Orders' tab directly inside the official Amazon or retailer app",
            "Never click cancellation links received via SMS or email",
            "Report phishing attempt to stop-spoofing@amazon.com"
        ],
        "icon": "📦"
    },
    {
        "name": "Toll Tag Low Balance Auto-Debit Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "SMS warning your transponder has negative balance and daily penalties will accrue unless replenished via link.",
        "sample": "SunPass Notice: Your toll balance is -$4.20. Auto-replenishment failed. Settle now to prevent daily $25 penalties: https://sunpass-toll-settle.net",
        "source": "FBI IC3",
        "kaise": "1. Automated bots text millions of phone numbers across state lines.\n2. Phishing link opens replica of state toll payment system.\n3. Harvests full billing address and debit card information.",
        "flags": [
            "State toll authorities do not text drivers from 10-digit telephone numbers",
            "Unusual domain extension (.net, .top) instead of official state authority domain",
            "Threat of immediate exponential daily penalties",
            "Recipient does not have a registered vehicle or transponder tag",
            "No specific toll plaza timestamp or license plate provided"
        ],
        "actions": [
            "Log in only via official toll transponder account portal or app",
            "Report toll phishing text to FBI IC3 at ic3.gov",
            "Block sender phone number immediately"
        ],
        "icon": "💳"
    },
    {
        "name": "Social Security Number / National ID Suspension Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "SMS warning your Social Security Number has been linked to drug trafficking in Texas and will be suspended unless verified on link.",
        "sample": "SSA Alert: Your Social Security Number has been suspended due to suspicious activity. Verify identity to avoid federal arrest warrant: https://ssa-gov-identity-verify.org",
        "source": "FTC",
        "kaise": "1. Exploits fear of federal law enforcement and criminal prosecution.\n2. Form collects full Social Security Number, mother's maiden name, address, and bank routing numbers.\n3. Used to file fraudulent tax returns and take out loans in victim's name.",
        "flags": [
            "Social Security Administration never contacts citizens via SMS threatening SSN suspension",
            "The government cannot 'suspend' your Social Security Number",
            "Threatens imminent federal arrest or sheriff dispatch",
            "Domain does not end in '.gov'",
            "Demands full 9-digit SSN and financial account details"
        ],
        "actions": [
            "Report Social Security impersonations to SSA OIG at oig.ssa.gov",
            "Never share your SSN or National ID on unverified web portals",
            "Freeze credit bureaus (Equifax, Experian, TransUnion) if SSN compromised"
        ],
        "icon": "🏛️"
    },
    {
        "name": "Fake Free Wi-Fi Portal Credential Harvester",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 93,
        "desc": "Rogue Wi-Fi hotspot in airports or cafes showing captive portal asking users to log in with Google, Facebook, or phone number OTP to get free internet.",
        "sample": "Connect to Airport Free High-Speed Wi-Fi: Log in with your Google or Facebook account to enjoy 2 hours free browsing.",
        "source": "Interpol",
        "kaise": "1. Attacker sets up portable Wi-Fi router named 'Free_Airport_WiFi' in busy public area.\n2. When user connects, captive portal pops up requesting social login credentials.\n3. Captures cleartext usernames, passwords, and session cookies.",
        "flags": [
            "Open unencrypted Wi-Fi network with generic name (Free_Public_WiFi, Airport_Guest)",
            "Captive portal demands full password login to Google, Apple ID, or Facebook to browse web",
            "SSL certificate warning appears when connecting to the login page",
            "Prompts to install a security certificate or configuration profile on your device",
            "Legitimate airport Wi-Fi usually requires only accepting terms of service"
        ],
        "actions": [
            "Use cellular data or personal hotspot instead of untrusted public Wi-Fi networks",
            "Use a reputable Virtual Private Network (VPN) when browsing on public connections",
            "Never enter passwords into captive Wi-Fi login pages"
        ],
        "icon": "📶"
    },
    {
        "name": "Job Offer WhatsApp Group Invite Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 94,
        "desc": "SMS or WhatsApp inviting you to join a private VIP job group where admins share daily part-time tasks earning Rs 3,000 to Rs 8,000.",
        "sample": "Greetings from Amazon HR! You have been selected for online work. Daily payout Rs 3500-8000. Join official hiring WhatsApp group: https://chat.whatsapp.com/invitelink",
        "source": "I4C India",
        "kaise": "1. Bot invites victim to WhatsApp group with 50 fake members.\n2. Group admins post fabricated payment screenshots and celebrate high payouts.\n3. Victim is gradually lured into paying crypto deposits for VIP task tiers.",
        "flags": [
            "Reputable companies like Amazon or Google do not hire employees through public WhatsApp group invite links",
            "Unsolicited job offer without submitting an application or resume",
            "Group members post identical scripted praise and bank transfer screenshots",
            "Admin phone numbers have unusual foreign country codes (+234, +62, +84)",
            "Demands small registration fee or task deposit to start earning"
        ],
        "actions": [
            "Exit and report the WhatsApp group immediately using 'Report and Exit'",
            "Adjust WhatsApp privacy settings: Settings > Privacy > Groups > 'My Contacts' to prevent strangers from adding you",
            "Apply for employment exclusively through company career portals"
        ],
        "icon": "💼"
    },
    {
        "name": "Fake Bank Beneficiary Added Alert Phishing",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 97,
        "desc": "SMS warning that a new beneficiary has been successfully added to your netbanking account, prompting you to click link to cancel if unauthorized.",
        "sample": "HDFC Alert: Beneficiary 'Rahul Sharma' has been added to your A/c ending 4912. If not requested by you, cancel transfer within 30 mins: https://hdfc-beneficiary-cancel.com",
        "source": "I4C India",
        "kaise": "1. Scammers spoof bank notification templates to induce sudden panic.\n2. Victim clicks link to immediately prevent money transfer.\n3. Phishing portal captures netbanking customer ID, IPIN, and OTP to actually add a criminal beneficiary.",
        "flags": [
            "Banks do not provide direct cancellation links inside beneficiary notification messages",
            "SMS sent from personal 10-digit number instead of authorized bank alphabetic sender header",
            "URL is not the verified netbanking portal of your bank",
            "Page prompts for login password, debit card PIN, and OTP simultaneously",
            "Creating intense 30-minute urgency deadline"
        ],
        "actions": [
            "Log in only through your official bank mobile app to verify registered beneficiaries",
            "Never tap cancellation links received via SMS",
            "Call bank fraud hotline immediately to freeze netbanking access if credentials were submitted"
        ],
        "icon": "⚠️"
    },
    {
        "name": "Fake Invoice / Geek Squad Auto-Renewal Phishing Email",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Message",
        "cat_slug": "phishing-message",
        "cat_name": "Phishing / Message / Link",
        "score": 95,
        "desc": "Email invoice showing auto-charge of $499.99 for Best Buy Geek Squad or Norton Antivirus renewal, providing a toll-free number to cancel within 24 hours.",
        "sample": "Geek Squad Invoice #GS-9821: Thank you for renewing your Total Tech Support 3-Year Plan ($499.99). Call +1-888-XXX-XXXX to cancel if you did not authorize this charge.",
        "source": "FTC",
        "kaise": "1. Fraudulent PDF invoice sent to thousands of email addresses.\n2. Victim panics at $500 unauthorized charge and calls provided telephone number.\n3. Call center scammer instructs victim to install AnyDesk to process a refund, editing HTML to show fake overpayment and extorting thousands.",
        "flags": [
            "You never purchased Geek Squad, Norton, or McAfee tech support subscriptions",
            "Sender email address is a free Gmail or Outlook address (e.g. billingdept892@gmail.com)",
            "Invoice is an attached image or PDF designed to bypass email spam filters",
            "Customer service number connects directly to call center with heavy background noise",
            "Representative asks you to download remote desktop software to give a refund"
        ],
        "actions": [
            "Check your credit card or bank account directly to verify if any charge actually occurred",
            "Never call phone numbers listed on unverified email invoices",
            "Forward phishing email to reportphishing@apwg.org and mark as spam"
        ],
        "icon": "🧾"
    }
]

print(f"Cat3 loaded: {len(cat3)} scams")
