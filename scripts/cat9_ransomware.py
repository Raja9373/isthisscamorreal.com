# Category 9: Ransomware / Malware / Tech Scams (22 scams)
cat9 = [
    {
        "name": "LockBit & Double Extortion Enterprise Ransomware",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 99,
        "desc": "Ransomware syndicate infiltrates enterprise network via compromised remote desktop credentials, exfiltrates corporate customer databases, encrypts all virtual machines, and demands $2,000,000 in Monero under threat of publishing patient records on dark web leak site.",
        "sample": "All your servers and customer databases are encrypted with military-grade AES-256. We also downloaded 450GB of confidential patient records. Pay $2.5M in Monero (XMR) within 7 days or everything will be published on our public dark web leak blog.",
        "source": "FBI IC3",
        "kaise": "1. Gang buys compromised VPN or Remote Desktop Protocol (RDP) credentials from initial access brokers.\n2. Silently moves laterally across corporate network over 3 weeks, disabling security software and exfiltrating gigabytes of sensitive files.\n3. Deploys ransomware binary across all domain controllers simultaneously at 2:00 AM on Sunday morning, leaving ransom notes on every desktop.",
        "flags": [
            "Desktop wallpaper replaced with alarming ransom instructions and all file extensions renamed (.lockbit, .encrypted)",
            "System shadow copies and local backup snapshots deleted via automated batch scripts",
            "Attacker provides link to proprietary dark web .onion negotiation chat portal",
            "Demands ransom payment exclusively in anonymous cryptocurrency (Monero XMR or Bitcoin)",
            "Threatens to leak proprietary intellectual property, employee SSNs, or customer financial records if ransom is unpaid"
        ],
        "actions": [
            "Maintain immutable, air-gapped, offline data backups that cannot be modified over the local network",
            "Isolate infected network subnets immediately: disconnect Ethernet cables and disable Wi-Fi to stop lateral propagation",
            "Contact FBI Cyber Division (ic3.gov) or national cybersecurity agency (CISA / CERT-In) immediately; law enforcement advises against paying ransoms"
        ],
        "icon": "🔒"
    },
    {
        "name": "Fake ChatGPT-5 & AI Voice Desktop App Trojan",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 97,
        "desc": "Sponsored Google search ads and Facebook ads promoting 'Free ChatGPT-5 Pro Offline Desktop Edition', distributing RedLine or Lumma info-stealer trojans that extract saved browser passwords, session cookies, and crypto wallet private keys within 60 seconds.",
        "sample": "Download ChatGPT-5 Pro for Windows: Free unlimited GPT-5 offline desktop assistant with voice cloning! 100% free download: https://chatgpt5-desktop-ai.org/setup.exe",
        "source": "Google News",
        "kaise": "1. Scammers purchase sponsored search results on Google for terms like 'ChatGPT desktop app download'.\n2. User downloads an executable installer (setup.exe) signed with a stolen corporate certificate.\n3. Silent stealer payload executes in background, scraping Chrome and Edge password databases and crypto wallet browser extensions, transmitting archives to attacker Telegram bot.",
        "flags": [
            "Software claims to offer non-existent AI models ('ChatGPT-5', 'Midjourney v7 Offline')",
            "Website domain is not the official OpenAI portal: chatgpt.com or openai.com",
            "Windows Defender or browser displays SmartScreen security warning on download",
            "Installer asks for Administrator privileges to install a supposedly simple text AI tool",
            "User accounts on Facebook, Gmail, and crypto exchanges show simultaneous unauthorized logins shortly after installation"
        ],
        "actions": [
            "Access ChatGPT and AI services exclusively through official verified domains: chatgpt.com or official mobile app stores",
            "Never download standalone .exe or .msi AI packages from sponsored third-party search results",
            "If infected, run a full system scan with reputable anti-malware (Malwarebytes) and immediately change all passwords from an independent clean device"
        ],
        "icon": "🤖"
    },
    {
        "name": "WannaCry SMB Exploit Worm Ransomware",
        "year": 2017,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 99,
        "desc": "Global worm exploiting Microsoft Windows SMBv1 vulnerability (EternalBlue), rapidly infecting over 200,000 computers across 150 countries within hours, locking hospitals, railways, and telecom networks demanding $300 Bitcoin.",
        "sample": "Ooops, your files are encrypted! Maybe you are busy looking for a way to recover your files, but do not waste your time. You have only 3 days to submit $300 in Bitcoin to our wallet.",
        "source": "Wikipedia",
        "kaise": "1. Scans the public internet and local networks for unpatched Windows computers with open SMB port 445.\n2. Injects NSA-leaked EternalBlue exploit code without requiring any user click or email interaction.\n3. Encrypts hard drives, replaces wallpaper with famous red lock screen, and self-propagates to all adjacent network computers.",
        "flags": [
            "Distinctive red graphical user interface window titled '@WanaDecryptor@ v2.0'",
            "Files renamed with extension '.WNCRY'",
            "Two countdown timers showing deadline before ransom doubles and before files are permanently deleted",
            "Spreads autonomously across internal enterprise local area networks without any employee interaction",
            "Affected systems running legacy, unpatched Windows operating systems (Windows XP, Windows 7, Windows Server 2003)"
        ],
        "actions": [
            "Keep all operating systems updated with the latest security patches (ensure MS17-010 patch is applied)",
            "Disable outdated SMBv1 protocol in Windows Features and block port 445 at corporate firewalls",
            "Use free decryption tools available on the official NoMoreRansom.org project"
        ],
        "icon": "🛑"
    },
    {
        "name": "AnyDesk / TeamViewer Remote Screen Control Bank Drainage",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 98,
        "desc": "Scammer posing as bank, electricity, or telecom executive convinces victim to download AnyDesk or TeamViewer QuickSupport on their phone, reciting the 9-digit remote access code. Scammer blacks out screen and empties bank accounts via netbanking.",
        "sample": "Sir, your KYC update requires digital terminal verification. Please install 'AnyDesk' from Google Play Store and tell me the 9-digit code displayed so our technical team can complete biometric synchronization.",
        "source": "I4C India",
        "kaise": "1. Convinces victim to install legitimate remote desktop software from Google Play Store.\n2. Directs victim to read out the unique 9-digit connection address and tap 'Accept' on permissions.\n3. Scammer gains complete remote touch control over victim's phone screen, instructs victim to open their banking app, and watches them enter their PIN and passwords.",
        "flags": [
            "Customer service or technical representative instructs you to install AnyDesk, TeamViewer, RustDesk, or QuickSupport on your mobile phone",
            "Caller insists on you reading aloud the 9-digit connection address shown inside the app",
            "Phone screen displays warning: 'Allow incoming connection? Third party can view and control your device'",
            "Caller asks you to log in to your mobile banking or UPI app while the remote session is active",
            "Phone screen goes black or flickers while transactions occur in the background"
        ],
        "actions": [
            "NEVER install remote control software (AnyDesk, TeamViewer, RustDesk) at the request of incoming callers",
            "If you installed it, immediately turn on Airplane Mode or power off your phone to sever the connection",
            "Uninstall the remote access application immediately and contact your bank to freeze electronic transfers"
        ],
        "icon": "📲"
    },
    {
        "name": "Juice Jacking Rogue Public USB Charging Kiosk",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 93,
        "desc": "Tampered USB charging ports in airports, train stations, or hotel lobbies secretly wired to microcomputers that install keylogger spyware or siphon photos and messages the moment phone is plugged in.",
        "sample": "Traveler plugs smartphone into free public USB wall port at airport terminal. Phone displays subtle prompt: 'Trust this computer?' Hidden micro-controller extracts contacts and installs monitoring payload.",
        "source": "FBI IC3",
        "kaise": "1. Criminals disassemble public USB charging kiosks in high-traffic transit hubs.\n2. Splice data transfer pins (D+ and D-) to a concealed Raspberry Pi microcomputer.\n3. When traveler connects charging cable, the rogue computer attempts automated media extraction and malware injection.",
        "flags": [
            "Connecting your phone to a public USB wall charging port triggers a prompt: 'Trust this computer?' or 'Allow access to device data?'",
            "Public USB port feels loose, altered, or shows signs of physical casing damage",
            "Phone heats up rapidly or shows background data transfer activity while charging",
            "Device battery discharges faster than normal following connection to public kiosk",
            "Unprompted installation of unknown configuration profiles on mobile device"
        ],
        "actions": [
            "Use an AC electrical wall outlet with your own personal power adapter block rather than public USB jacks",
            "Use a 'USB Data Blocker' (charge-only adapter) that physically disconnects data pins and allows only power flow",
            "Always tap 'Don't Trust' if a computer trust prompt appears while plugging into a wall charging port"
        ],
        "icon": "🔌"
    },
    {
        "name": "Evil Twin Rogue Public Airport Wi-Fi Packet Sniffer",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 94,
        "desc": "Attacker deploys a Wi-Fi Pineapple router in an airport lounge broadcasting an identical open Wi-Fi network named 'Free_Airport_WiFi_HighSpeed', intercepting all unencrypted web traffic, DNS requests, and login sessions.",
        "sample": "Passenger connects laptop to open Wi-Fi network matching airport lounge name. Attacker performs man-in-the-middle SSL stripping, capturing corporate session cookies and redirecting user to cloned login portals.",
        "source": "Action Fraud",
        "kaise": "1. Attacker sets up portable wireless access point cloning SSID name of legitimate venue.\n2. Broadcasts stronger signal causing traveler devices to auto-connect.\n3. Intercepts DNS queries, executes SSL stripping, and injects fake software update popups to install Trojans.",
        "flags": [
            "Two identical Wi-Fi network names appearing in your device Wi-Fi connection list (one secure, one unsecured)",
            "Network does not require the standard captive portal agreement or password displayed on the airport board",
            "Browser displays recurring SSL/TLS certificate security warning banners when visiting popular websites",
            "Unexpected prompts appear instructing user to install 'Flash Player Update' or 'Wi-Fi Driver Certificate'",
            "Webpages take abnormally long to load or redirect to obscure search engine portals"
        ],
        "actions": [
            "Use personal cellular mobile data hotspot instead of connecting to untrusted public Wi-Fi networks",
            "Always activate an encrypted Virtual Private Network (VPN) before browsing on any public network",
            "Never bypass SSL/HTTPS browser security warnings on public connections"
        ],
        "icon": "📶"
    },
    {
        "name": "Malicious Chrome Browser Extension Password Stealer",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 95,
        "desc": "Helpful Chrome extension (PDF converter, ad blocker, screenshot tool) purchased by criminal developers, pushed with automatic update injecting JavaScript that harvests credit card numbers and session tokens.",
        "sample": "Popular 'Free Color Picker' Chrome extension with 100,000 users updates in background. Silent malicious script injects DOM keylogger on all banking and crypto websites, transmitting passwords to remote server.",
        "source": "Google News",
        "kaise": "1. Scammers purchase popular, abandoned browser extensions from legitimate original developers.\n2. Push a silent extension update through the Chrome Web Store containing obfuscated malicious code.\n3. Extension reads DOM input fields across every webpage the user visits, extracting passwords and session cookies.",
        "flags": [
            "Extension suddenly requests expanded browser permissions: 'Read and change all your data on all websites'",
            "Browser performance slows down noticeably with persistent high CPU utilization",
            "Spontaneous popups or unwanted redirects to third-party affiliate shopping links",
            "Online accounts trigger security warnings regarding session cookie hijacking",
            "Extension name or branding changes subtly in Chrome extensions management page"
        ],
        "actions": [
            "Audit installed browser extensions regularly and remove any that are not strictly necessary",
            "Review extension permissions: restrict access to 'On click' rather than 'On all websites'",
            "Install extensions only from verified developers with extensive positive historical track records"
        ],
        "icon": "🧩"
    },
    {
        "name": "Pirated Software Torrent Crack & Keygen Trojan Dropper",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 96,
        "desc": "Downloading cracked versions of Adobe Photoshop, Premiere Pro, or AutoCAD from torrent sites. The included 'keygen.exe' or 'patch.exe' disables Windows Defender and installs persistent rootkit malware.",
        "sample": "Download Adobe Photoshop 2024 Full Crack + Keygen.zip. Running 'Patch.exe' prompts user to temporarily disable antivirus. Antivirus disabled: trojan installs hidden cryptocurrency miner and backdoors system.",
        "source": "Wikipedia",
        "kaise": "1. Threat actors package pirated commercial software with malicious loaders in torrent releases.\n2. Instructions strictly tell user to 'Turn off Antivirus/Windows Defender' before running patcher.\n3. Patcher establishes persistent backdoor, joins computer to malicious botnet, and harvests stored credentials.",
        "flags": [
            "Installer instructions mandate turning off your antivirus or adding installation folder to exclusion list",
            "File arrives in password-protected ZIP or RAR archive designed to evade automated virus scanner inspection",
            "Executable file has suspicious double extension (e.g. Photoshop_Crack.pdf.exe)",
            "System fan runs loudly continuously while computer is idle due to hidden background crypto mining",
            "New unrecognized administrator user accounts appear in Windows settings"
        ],
        "actions": [
            "Never download or execute cracked commercial software from torrent repositories",
            "NEVER disable antivirus or Windows Defender based on instructions from downloaded software",
            "Use open-source free software alternatives (GIMP for Photoshop, DaVinci Resolve for Premiere, Blender for 3D)"
        ],
        "icon": "🏴‍☠️"
    },
    {
        "name": "Cryptojacking Hidden Monero CPU Miner Malware",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 91,
        "desc": "Malware silently runs high-intensity Monero (XMR) cryptocurrency mining software in background, consuming 100% of CPU and GPU power, causing computer overheating and thermal hardware damage.",
        "sample": "Computer fan runs at maximum speed continuously; laptop battery drains in 30 minutes. Task Manager shows unknown process 'svchost_update.exe' consuming 98% of multi-core CPU capacity.",
        "source": "Interpol",
        "kaise": "1. Infiltrates system via drive-by download, malicious browser extension, or infected game mod.\n2. Installs lightweight XMRig mining executable disguised under legitimate Windows system process names.\n3. Program throttles CPU usage to 10% whenever user opens Task Manager to evade visual detection.",
        "flags": [
            "Computer cooling fans run at maximum speed constantly, even when no applications are open",
            "Laptop chassis becomes uncomfortably hot to the touch and battery life drops precipitously",
            "System performance stutters severely during basic web browsing or document editing",
            "Electricity utility bills show unexplained, substantial monthly increases",
            "High CPU utilization immediately drops to normal the moment Task Manager is launched"
        ],
        "actions": [
            "Scan computer using specialized anti-malware tools (Malwarebytes, HitmanPro) to detect hidden miners",
            "Inspect startup applications in Windows Task Manager > Startup tab and disable unrecognized entries",
            "Install reputable ad-blocking extensions (uBlock Origin) to prevent in-browser cryptomining scripts"
        ],
        "icon": "⛏️"
    },
    {
        "name": "Stalkerware & Mobile Spyware Surveillance App",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 97,
        "desc": "Covert surveillance app (mSpy, FlexiSPY, KidsGuard) secretly installed on victim's phone by abusive partner or stalker, recording live location, phone calls, WhatsApp messages, and microphone audio 24/7.",
        "sample": "Partner secretly borrows victim's phone for 10 minutes to 'check navigation', installs hidden monitoring app disguised as 'Device Health Service'. Partner monitors all real-time WhatsApp chats and GPS coordinates from web dashboard.",
        "source": "FTC",
        "kaise": "1. Person with physical access to victim's handset unlocks device and sideloads surveillance software.\n2. Disguises app icon under system names (e.g. 'System Update Service', 'Google Play Config').\n3. Grants Device Administrator, Accessibility, and Location permissions, transmitting continuous real-time telemetry to stalker's online portal.",
        "flags": [
            "Phone battery drains drastically faster than usual and handset feels warm when idle",
            "Mobile data consumption spikes dramatically due to continuous background video/audio uploads",
            "Location GPS indicator icon appears active in status bar even when maps are closed",
            "Device settings show unfamiliar active apps under 'Device Admin Apps' or 'Accessibility Services'",
            "Another person exhibits uncanny, exact knowledge of your private conversations and whereabouts"
        ],
        "actions": [
            "Review Android Settings > Apps > Special App Access > Device Admin Apps and revoke unknown entries",
            "Enable Google Play Protect to automatically scan and identify commercially sold stalkerware",
            "Perform a factory reset of the smartphone and change your Google/Apple account passwords from a separate device"
        ],
        "icon": "🕵️"
    },
    {
        "name": "Browser Lock Law Enforcement Warning Pop-up Ransomware",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 93,
        "desc": "Full-screen browser lockout displaying Department of Justice or FBI seal claiming illegal pornography or copyright violation was detected, demanding $500 fine paid via MoneyPak voucher to unlock computer.",
        "sample": "FBI Cyber Crime Division: Your browser has been locked due to viewing forbidden child pornography materials. Under federal penal code, you must pay $450 fine within 48h using GreenDot MoneyPak to restore access.",
        "source": "FBI IC3",
        "kaise": "1. Malicious pop-under ad triggers an infinite JavaScript fullscreen loop that disables standard close buttons.\n2. Displays alarming FBI or Interpol badges and uses laptop webcam to display victim's real-time face on screen.\n3. Convinces panicked user that federal agents have locked their computer until a prepaid cash fine is entered.",
        "flags": [
            "Browser enters forced fullscreen mode and prevents clicking back or closing tabs",
            "Displays official government agency seals (FBI, DOJ, Interpol) demanding cash fines to avoid criminal trial",
            "Demands payment via prepaid vouchers (GreenDot MoneyPak, Vanilla Visa, iTunes gift cards)",
            "Webcam light turns on and displays live video feed of your face inside the browser window",
            "Computer itself is NOT actually encrypted; only the single browser tab is locked"
        ],
        "actions": [
            "Do NOT pay; press Ctrl+Alt+Delete (or Cmd+Option+Esc on Mac) to open Task Manager and force-quit the browser",
            "When restarting browser, do NOT click 'Restore previous session' when prompted",
            "Clear browser cache and cookies, and install an ad blocker to prevent rogue redirect scripts"
        ],
        "icon": "🚨"
    },
    {
        "name": "Fake Antivirus Renewal Subscription Overcharge Scam",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 94,
        "desc": "Email receipt thanking you for renewing Norton 360 or McAfee Total Protection for $499, instructing you to call their toll-free helpline within 24 hours if you wish to dispute the charge and receive a refund.",
        "sample": "Norton LifeLock Billing Invoice: Thank you for renewing your 3-Year Family Shield Plan ($479.99). Your credit card will be debited today. If you did NOT authorize this charge, call our billing dispute center immediately at 1-888-XXX-XXXX.",
        "source": "FTC",
        "kaise": "1. Millions of deceptive email invoices sent to consumers claiming major automatic renewals.\n2. Panicked recipient dials the toll-free number to prevent the $500 charge.\n3. Call center scammer guides caller to download AnyDesk to process a 'refund', edits bank webpage HTML to show $5,000 accidental refund, and demands victim return the $4,500 difference in cash.",
        "flags": [
            "You never purchased or subscribed to Norton, McAfee, or Geek Squad security products",
            "Sender email address uses free commercial mail providers (@gmail.com, @outlook.com) rather than corporate domains",
            "Invoice is sent as an attached PDF or image file to bypass automated email security filters",
            "Representative insists on taking remote desktop control of your computer to process a refund",
            "Representative asks you to log in to your personal online bank account while they view your screen"
        ],
        "actions": [
            "Check your authentic credit card and bank statements directly; you will find no charge was ever made",
            "Never call telephone numbers provided on unverified email invoices",
            "Forward the fraudulent email to phishing@nortonlifelock.com or spam@mcafee.com and delete it"
        ],
        "icon": "🛡️"
    },
    {
        "name": "Social Media Account Hijack Session Cookie Thefts",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 96,
        "desc": "Info-stealer malware extracts active browser session cookies, allowing hackers to bypass two-factor authentication (2FA) and take over YouTube channels, Instagram accounts, and Steam profiles without knowing passwords.",
        "sample": "Victim downloads a game cheat mod from Discord. Stealer malware extracts Chrome session cookies. Attacker imports cookies into their browser, instantly logging into victim's 500k-subscriber YouTube channel and launching crypto scam livestream.",
        "source": "Google News",
        "kaise": "1. Malware (RedLine, Vidar, Raccoon) scrapes SQLite database files where browsers store active session cookies.\n2. Attacker loads stolen cookies into browser session profile.\n3. Website recognizes valid session token and allows instant login, completely bypassing 2FA prompts and password verification.",
        "flags": [
            "YouTube channel or Instagram account taken over even though two-factor authentication was active",
            "Channel profile, banner, and name suddenly changed to 'Tesla Motors' or 'MicroStrategy' streaming Elon Musk crypto videos",
            "Security logs show successful login from foreign country with NO two-factor authentication prompt triggered",
            "Account recovery email and telephone numbers changed within seconds of takeover",
            "Attacker deletes existing public videos and makes live broadcasts asking viewers to send Bitcoin"
        ],
        "actions": [
            "In your Google/Meta account security settings, click 'Sign out of all other sessions and devices' immediately",
            "Clear all browser cookies and cache to invalidate active session tokens",
            "Contact YouTube Creator Support on Twitter/X (@TeamYouTube) to initiate specialized channel recovery procedures"
        ],
        "icon": "🍪"
    },
    {
        "name": "Fake System Cleaners & PC Optimizer Scareware",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 90,
        "desc": "Free utility program (PC SpeedUp 2024, CleanMyWin) scans computer and fabricates 1,400 'critical registry errors' and 'severe security risks', requiring $49.99 paid license to repair non-existent problems.",
        "sample": "PC Speed Booster Scan Complete: 1,842 Critical System Errors Detected! Your Windows Registry is corrupted and hard drive is at imminent risk of failure. Purchase Pro Lifetime License ($49.95) to repair.",
        "source": "FTC",
        "kaise": "1. Bundled with free software downloads via deceptive marketing popups.\n2. Performs mock diagnostic scan displaying benign temporary files as catastrophic system corruptions.\n3. Terrifies non-technical computer users into purchasing useless paid software licenses.",
        "flags": [
            "Program installed itself without your explicit knowledge during another software installation",
            "Claims thousands of severe registry errors or critical virus threats on a newly formatted computer",
            "Frequent intrusive desktop popups warning of imminent system failure and crash",
            "Demands credit card payment to perform basic file deletions you can do for free with built-in Windows tools",
            "Difficult to uninstall using standard Windows Add/Remove Programs"
        ],
        "actions": [
            "Do NOT pay; Windows does NOT require third-party registry cleaners or PC optimizers",
            "Uninstall the scareware application using Windows Settings > Apps",
            "Use built-in Windows Disk Cleanup tool and Windows Defender to keep your system clean and secure"
        ],
        "icon": "🧹"
    },
    {
        "name": "Ransomware-as-a-Service (RaaS) Dark Web Affiliate Network",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 98,
        "desc": "Sophisticated cybercrime business model where ransomware core developers lease encryption payloads and payment infrastructure to independent criminal affiliates in exchange for 20% commission on all extortion payouts.",
        "sample": "Dark web RaaS recruitment advertisement: 'Join our elite ransomware affiliate network. 80/20 revenue split. Automated Tor payment portal, military-grade fast encryption, and dedicated DDoS pressure services.'",
        "source": "FBI IC3",
        "kaise": "1. Core developers maintain encryption software, automated leak portals, and cryptocurrency laundering pipelines.\n2. Recruit independent hackers ('affiliates') who breach corporate networks and deploy the ransomware.\n3. Extortion payments collected via automated Tor portals and split automatically between developers and affiliates.",
        "flags": [
            "Ransom demand directed to a sophisticated Tor dark web portal with automated ticketing customer support",
            "Victim offered 'Free trial decryption of 1 file' to prove decryption capability",
            "Professional countdown timer with dynamic price increases if deadline lapses",
            "Attackers demonstrate comprehensive understanding of victim corporate insurance policy limits",
            "Threat of Distributed Denial of Service (DDoS) attacks and customer notifications if negotiation stalls"
        ],
        "actions": [
            "Engage professional certified cybersecurity incident response firms immediately upon detection",
            "Notify law enforcement (FBI Cyber Division / CISA / Europol) before entering any communications",
            "Maintain comprehensive offline immutable backups to ensure recovery without paying criminal syndicates"
        ],
        "icon": "💻"
    },
    {
        "name": "Fake Google Meet / Zoom Conference Malware Trap",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 95,
        "desc": "Invited to a business interview or client presentation on a lookalike Google Meet or Zoom page that prompts: 'Audio driver missing. Click here to download Zoom-Audio-Plugin.exe to join the meeting.'",
        "sample": "You have been invited to an urgent project consultation on Google Meet. To join with microphone and video, install required browser media plugin: https://meet-google-conference.top/plugin.exe",
        "source": "FBI IC3",
        "kaise": "1. Attacker sends calendar invite or LinkedIn message scheduling a job interview or business partnership call.\n2. Link opens realistic clone of video conferencing interface.\n3. Fake error claims camera or microphone driver is missing, tricking user into downloading and executing info-stealer malware.",
        "flags": [
            "Joining video conference requires downloading an unexpected standalone '.exe' or '.msi' file",
            "Legitimate Google Meet runs completely natively inside standard modern web browsers with zero plugin downloads",
            "URL is not official meet.google.com or zoom.us domain",
            "Meeting host does not appear in room and interface controls are static or non-responsive",
            "Browser downloads trigger antivirus SmartScreen security warnings"
        ],
        "actions": [
            "Google Meet NEVER requires downloading desktop software plugins to join a meeting",
            "Download Zoom exclusively from the official domain: zoom.us/download",
            "Never execute downloaded files received from unverified meeting invites"
        ],
        "icon": "🎥"
    },
    {
        "name": "SIM Card PUK Code Netbanking Takeover Trap",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 96,
        "desc": "Scammer calls claiming telecom network maintenance requires your 8-digit SIM PUK code. With PUK code, scammer clones physical SIM card, hijacking mobile OTPs while victim's phone shows 'Emergency Calls Only'.",
        "sample": "Airtel / Jio Technical Desk: Your SIM card security certificate has expired. To prevent total signal block, share the 8-digit PUK code printed on your original SIM card plastic envelope.",
        "source": "I4C India",
        "kaise": "1. Scammer contacts carrier or uses social engineering to initiate SIM replacement.\n2. Convinces victim to disclose their confidential 8-digit Personal Unblocking Key (PUK).\n3. Activates new duplicate physical SIM in scammer handset, intercepting all two-factor authentication SMS codes.",
        "flags": [
            "Telecom carriers NEVER call subscribers requesting their secret 8-digit SIM PUK code",
            "PUK codes are used exclusively by users to unlock PIN-blocked SIM cards",
            "Caller claims mobile network tower maintenance requires PUK authentication",
            "Sudden permanent loss of cellular signal and network reception on your phone following the call",
            "Call received from an unverified standard mobile telephone number"
        ],
        "actions": [
            "NEVER share your SIM card PUK code with anyone over phone or text message",
            "If phone network signal disappears unexpectedly, contact your cellular carrier immediately from another handset",
            "Instruct carrier to place an immediate fraud lock on SIM replacement requests"
        ],
        "icon": "📶"
    },
    {
        "name": "Fake Cloudflare Turnstile CAPTCHA PowerShell Dropper",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 97,
        "desc": "Website shows fake Cloudflare 'Verify You Are Human' CAPTCHA instructing user to press 'Windows Key + R', paste clipboard script into Run dialog, and press Enter, executing malicious PowerShell stealer.",
        "sample": "Cloudflare Verification: To verify you are not a robot, press Win + R, then press Ctrl + V and hit Enter to complete automated browser verification.",
        "source": "Google News",
        "kaise": "1. Malicious webpage automatically copies an encoded PowerShell command to user's system clipboard.\n2. Displays convincing fake Cloudflare verification page with step-by-step instructions.\n3. User unknowingly pastes and executes remote payload download script directly into Windows Run console, bypassing all browser sandboxes.",
        "flags": [
            "Website instructs you to press keyboard shortcuts 'Win + R' (Windows Run console) to complete a CAPTCHA",
            "Page instructs you to paste ('Ctrl + V') and run code in your operating system command line",
            "Legitimate Cloudflare or reCAPTCHA verification requires ONLY clicking a checkbox or solving visual puzzles",
            "Text pasted in Run box starts with 'powershell.exe -w hidden -e ...'",
            "Browser sandboxing is completely bypassed when running commands directly in the OS shell"
        ],
        "actions": [
            "CRITICAL: NEVER press Win + R or paste unknown clipboard text into Windows Run or Terminal based on website instructions",
            "Legitimate CAPTCHA challenges NEVER ask users to execute operating system terminal commands",
            "Close the browser tab immediately and scan device for unauthorized background processes"
        ],
        "icon": "🤖"
    },
    {
        "name": "DNS Hijacking & Router Default Password Takeover",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 94,
        "desc": "Malicious ad or drive-by script accesses local home router at 192.168.1.1 using default password (admin/admin), modifying DNS server settings to redirect all home devices to phishing portals when typing bank URLs.",
        "sample": "Home Wi-Fi router DNS modified by cross-site request forgery. When user types 'chase.com' on laptop or phone, rogue DNS routes connection to identical phishing server, harvesting credentials.",
        "source": "FBI IC3",
        "kaise": "1. User visits website hosting hidden WebRTC / CSRF script targeting default router IP (192.168.1.1).\n2. Logs into router admin panel using common factory credentials (admin/admin, admin/password).\n3. Replaces legitimate ISP DNS servers with malicious rogue DNS resolvers controlled by cybercriminals.",
        "flags": [
            "Home router still uses default manufacturer administrator password (admin/admin)",
            "Websites occasionally show invalid SSL certificate errors on trusted domains",
            "Typing common web addresses occasionally redirects to foreign ad portals or phishing screens",
            "Internet speed degrades and strange advertisements appear on previously clean websites",
            "All devices on home Wi-Fi experience identical routing anomalies simultaneously"
        ],
        "actions": [
            "Change default router administrator password immediately upon installation",
            "Update router firmware regularly and disable 'Remote Management' in router settings",
            "Manually configure trusted secure DNS resolvers (e.g. Cloudflare 1.1.1.1 or Google 8.8.8.8) on your router"
        ],
        "icon": "🌐"
    },
    {
        "name": "Fake Critical Chrome / Edge Browser Security Update Pop-up",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 93,
        "desc": "Compromised website displays full-screen overlay mimicking Google Chrome: 'Your browser is out of date! A critical security update is required to view this content', downloading trojan installer.",
        "sample": "Google Chrome Update Alert: An update is required to view this webpage securely. Download Chrome-Update-v124.exe now to prevent browser vulnerability exploitation.",
        "source": "Google News",
        "kaise": "1. Legitimate WordPress websites infected with malicious redirect scripts.\n2. Visitors presented with convincing overlay mimicking authentic browser update notification.\n3. Downloaded file installs infostealer trojan or backdoors computer.",
        "flags": [
            "Webpage itself prompts you to download an executable file (.exe) to update your browser",
            "Google Chrome and Microsoft Edge update AUTOMATICALLY in background without downloading manual .exe files from random websites",
            "URL hosting the update is an obscure third-party web domain rather than google.com or microsoft.com",
            "Popup claims you cannot view the webpage content until the file is installed",
            "Antivirus triggers warning regarding suspicious dropper binary"
        ],
        "actions": [
            "Update Google Chrome exclusively via Settings > About Chrome (built-in automated updater)",
            "Never download browser update executables from random webpage banner popups",
            "Close the deceptive browser tab immediately"
        ],
        "icon": "🌐"
    },
    {
        "name": "Discord Nitro Free Gift Subscription Trojan Trap",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 92,
        "desc": "Bot messages on Discord offering 'Free 3 Months Discord Nitro', linking to a phishing domain mimicking Discord login that steals session tokens and auto-messages all user friends.",
        "sample": "Discord Bot Gift: Congratulations! You have been gifted 3 months of Discord Nitro ($29.97 value)! Claim your gift subscription here before it expires: https://dlscord-nitro-gifts.com/claim",
        "source": "Action Fraud",
        "kaise": "1. Hacked Discord accounts or bots blast direct messages across public gaming servers.\n2. Phishing link features typo-squatted domain (dlscord, disord-app) with fake QR code login.\n3. Captures Discord user token, scans for linked credit cards, and buys gift subscriptions while spamming contacts.",
        "flags": [
            "Direct message offering free Discord Nitro from unknown user or bot",
            "URL has subtle spelling error (e.g. dlscord.com, discord-app.gift)",
            "Page asks you to scan a Discord QR code with your mobile app (scanning logs the attacker into your account)",
            "Offer claims to be valid for only 24 hours to create artificial rush",
            "Legitimate Discord gifts appear as native embedded cards within the chat interface, not external web links"
        ],
        "actions": [
            "Never scan Discord QR codes on third-party websites with your mobile app",
            "Check that domain is strictly 'discord.com' or 'discord.gift'",
            "Enable Two-Factor Authentication on your Discord account and change password immediately if compromised"
        ],
        "icon": "🎮"
    },
    {
        "name": "Dark Web Credential Stuffing Automated Account Takeover",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Tech",
        "cat_slug": "tech-ransomware",
        "cat_name": "Ransomware / Malware / Tech",
        "score": 95,
        "desc": "Automated botnets use billions of username/password combinations leaked from past corporate data breaches to test logins against banks, Netflix, and shopping portals, hijacking accounts sharing identical passwords.",
        "sample": "User's password leaked in old LinkedIn breach is reused on food delivery and shopping apps. Automated bot successfully logs into Domino's and Uber accounts, ordering $350 in unauthorized food using saved credit cards.",
        "source": "FBI IC3",
        "kaise": "1. Attackers aggregate massive combo-lists containing billions of leaked credentials from past breaches.\n2. Configure automated bot suites (OpenBullet, SilverBullet) with proxy rotation to test logins against popular consumer websites.\n3. Successfully breached accounts are drained of loyalty points, stored card values, or sold on dark web marketplaces.",
        "flags": [
            "Receiving password reset or login alert emails from websites you have not visited recently",
            "Account shows orders, deliveries, or viewing history you never initiated",
            "You reuse the same primary password across multiple email, shopping, and entertainment services",
            "Your email address appears in publicly known commercial data breaches",
            "Stored reward points or digital gift card balances suddenly disappear"
        ],
        "actions": [
            "NEVER reuse passwords across multiple services: generate unique passwords for every account",
            "Use a reputable password manager (1Password, Bitwarden, Apple Keychain) to store unique credentials",
            "Enable Two-Factor Authentication (2FA) using authenticator apps on all critical accounts"
        ],
        "icon": "🔐"
    }
]

print(f"Cat9 loaded: {len(cat9)} scams")
