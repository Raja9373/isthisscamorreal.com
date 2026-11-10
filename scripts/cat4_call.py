# Category 4: Call & Impersonation Scams (32 scams)
cat4 = [
    {
        "name": "Digital Arrest Police & CBI Video Intimidation Scam",
        "year": 2026,
        "is_latest": True,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 99,
        "desc": "Victims are called on Skype or WhatsApp video by fraudsters wearing fake police or CBI uniforms against simulated police station backdrops, ordering 24/7 video surveillance and transfer of life savings to 'RBI verification accounts'.",
        "sample": "This is Inspector Vijay from Cyber Crime Delhi. A parcel in your name with 5 passports and MDMA drugs was seized at airport. You are placed under Digital Arrest on Skype right now.",
        "source": "I4C India",
        "kaise": "1. Scammer calls stating passport or SIM registered in victim's name is involved in high-profile money laundering.\n2. Transfers call to 'investigating officer' on Skype or WhatsApp video with fake police station setup and uniforms.\n3. Orders victim to stay on camera continuously ('Digital Arrest') and transfer all bank deposits to 'RBI Supreme Court Escrow Accounts' for verification, which are drained instantly.",
        "flags": [
            "Indian law enforcement has no legal concept of 'Digital Arrest' via video call",
            "Demands 24/7 continuous video call monitoring forbidding talking to family or lawyers",
            "Orders victim to transfer money to private bank accounts for 'government fund verification'",
            "Displays forged arrest warrants, Supreme Court seals, or fake police ID cards over WhatsApp",
            "Call initiated on WhatsApp, Telegram, or Skype from numbers starting with +92, +855 or VOIP"
        ],
        "actions": [
            "Disconnect the call immediately; police or CBI never conduct interrogations via Skype or WhatsApp",
            "Never transfer money to any 'safe account' or 'RBI verification escrow'",
            "Report immediately to National Cyber Crime Helpline 1930 and file complaint at cybercrime.gov.in"
        ],
        "icon": "👮"
    },
    {
        "name": "AI Voice Clone CEO / Executive Emergency Transfer Call",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 98,
        "desc": "Using short audio clips from podcasts or earnings calls, AI models clone corporate CEO or finance director's voice to instruct finance staff to wire urgent acquisition funds.",
        "sample": "Hey David, it's Mark. We're finalizing an offshore acquisition today. I need an urgent wire of $185,000 to the escrow account details I just emailed. Please expedite right away.",
        "source": "FBI IC3",
        "kaise": "1. Criminals scrape executive voice samples from YouTube, interviews, and public webinars.\n2. Generative voice synthesis software replicates vocal timbre, breathing, and pitch in real time.\n3. Calls company accountant with high urgency instructing immediate wire transfer to criminal mule accounts.",
        "flags": [
            "Executive insists on bypassing standard two-person internal financial approval procedures",
            "Caller claims they are in a noisy boardroom or airport boarding lounge to avoid back-and-forth questioning",
            "Urgent demand for wire transfer or cryptocurrency transfer within hours",
            "Receiving bank account is at an unfamiliar institution or overseas jurisdiction",
            "Executive refuses follow-up callback on their registered corporate desk or mobile phone"
        ],
        "actions": [
            "Enforce strict multi-channel out-of-band verbal confirmation protocol for all wire transfers",
            "Call the executive back on their verified internal phone extension",
            "Implement multi-signature authorization controls for treasury disbursements"
        ],
        "icon": "🎙️"
    },
    {
        "name": "Grandparent Emergency Distress Bail Phone Scam",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 97,
        "desc": "Scammer calls an elderly person crying and claiming to be their grandchild who was arrested after a car accident, pleading for immediate cash bail dispatched via courier.",
        "sample": "Grandma, it's me! I was in a terrible car crash and the police arrested me because someone was hurt. A court courier will come to your house to collect $9,500 cash for bail. Please don't tell mom!",
        "source": "FTC",
        "kaise": "1. Scammers scrape family relations from social media (Facebook, Instagram).\n2. Fraudster calls elderly victim crying, disguising voice as grandson or granddaughter in jail.\n3. Hand-off to fake defense attorney who sends an in-person courier or rideshare driver to collect cash from the victim's porch.",
        "flags": [
            "Caller begs grandparent not to tell other family members ('Don't tell mom and dad')",
            "Intense emotional crisis claiming jail, car crash, or hospital emergency",
            "Court bail is requested in cash, gold bars, or prepaid gift cards",
            "Courier or rideshare driver sent to victim's home address to collect physical envelope of money",
            "Caller becomes aggressive or panics if victim asks clarifying personal trivia questions"
        ],
        "actions": [
            "Hang up immediately and call your grandchild or their parents directly on their known cell phone",
            "Establish a secret family emergency passphrase that only close relatives know",
            "Never hand cash envelopes or valuables to couriers arriving at your residence"
        ],
        "icon": "👵"
    },
    {
        "name": "Microsoft & Windows Tech Support Blue Screen Phone Scam",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 96,
        "desc": "Browser lock pop-up or phone call pretending to be Microsoft Windows Security claiming computer is infected with Trojan spyware, directing caller to pay for lifetime security.",
        "sample": "Warning: Microsoft Security Alert! Your computer is locked due to Zeus Trojan infection. Call Microsoft Certified Technicians immediately at 1-800-XXX-XXXX to prevent hard drive wipe.",
        "source": "FTC",
        "kaise": "1. Malicious ad triggers full-screen browser lock showing fake Windows Blue Screen error.\n2. Alarmed victim calls the toll-free number on screen.\n3. Indian call center technician instructs victim to download AnyDesk, opens Windows Event Viewer to show normal warnings as 'severe viruses', and charges $499.",
        "flags": [
            "Microsoft error messages NEVER include a telephone support number to call",
            "Full-screen browser message prevents closing tab (press Esc or Alt+F4 to exit)",
            "Technician demands remote desktop control via AnyDesk, TeamViewer or UltraViewer",
            "Technician opens normal Windows Event Viewer or dir/s in CMD claiming every line is a hacker virus",
            "Demands payment via Apple gift cards, Google Play cards, or wire transfer"
        ],
        "actions": [
            "Press Esc key or use Task Manager (Ctrl+Shift+Esc) to close the locked browser window",
            "Microsoft will never proactively cold-call or show phone numbers on blue screens",
            "Never grant remote desktop access to unsolicited callers"
        ],
        "icon": "💻"
    },
    {
        "name": "FedEx / DHL Illegal Narcotics Courier Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 98,
        "desc": "Automated IVR call stating your parcel containing 140 grams of MDMA drugs and fake passports sent to Taiwan has been intercepted by customs, patching to fake cyber police.",
        "sample": "FedEx Customer Notice: Your parcel sent from Mumbai to Taiwan containing 140g MDMA and 5 fake passports has been seized. Press 1 to connect to Narcotics Control Bureau officer.",
        "source": "I4C India",
        "kaise": "1. Robocall plays automated courier alert message.\n2. Pressing 1 connects to call center scammer posing as Mumbai Police or Customs Officer.\n3. Threatens victim with immediate non-bailable arrest unless they transfer bank balances to verify legitimate source of funds.",
        "flags": [
            "Courier companies do not connect customers directly to police or narcotics officers on telephone calls",
            "You never shipped any parcel abroad",
            "Caller demands immediate Skype or WhatsApp video conference",
            "Demands bank fund transfer to clear victim from money laundering FIR",
            "Threatens that police teams are outside victim's residence"
        ],
        "actions": [
            "Hang up immediately; it is 100% a criminal call center syndicate",
            "Call authentic FedEx/DHL customer care from their official website to verify no parcel exists",
            "Dial 1930 to report the calling numbers to cybercrime authorities"
        ],
        "icon": "📦"
    },
    {
        "name": "IRS / Tax Collector Law Enforcement Arrest Call",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 97,
        "desc": "Robocall claiming to be Internal Revenue Service stating federal arrest warrant is issued for tax evasion and local sheriff will arrive within 45 minutes unless back taxes are paid immediately.",
        "sample": "This is Officer John Miller from the Internal Revenue Service. We have filed a federal warrant against your name. Pay your $3,450 back taxes within 45 minutes or local police will arrest you.",
        "source": "FTC",
        "kaise": "1. Caller ID spoofing shows official IRS or police department phone numbers.\n2. Aggressive scammer reads fake badge number and federal case citation.\n3. Demands payment through prepaid Target gift cards, Bitcoin ATM, or Western Union to cancel the warrant.",
        "flags": [
            "IRS always initiates contact about unpaid taxes by official mail through the postal service, never phone calls",
            "IRS never demands payment using gift cards, cryptocurrency, or wire transfer",
            "IRS does not threaten to dispatch local police or sheriffs for immediate arrest",
            "Caller demands that you stay on the phone while driving to the grocery store or Bitcoin ATM",
            "Refuses to allow taxpayer to appeal or review bill through official tax portal"
        ],
        "actions": [
            "Hang up the phone immediately; the IRS never conducts business this way",
            "Report the call to Treasury Inspector General (TIGTA) at tigta.gov",
            "Check real tax status online at irs.gov/account"
        ],
        "icon": "🏛️"
    },
    {
        "name": "Virtual Kidnapping Extortion Phone Scam",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 99,
        "desc": "Scammer calls parents screaming that their son or daughter has been kidnapped, playing fake screams or AI voice in the background demanding ransom before the child is harmed.",
        "sample": "We have your daughter! She was involved in a car accident with my gang and we have her at gunpoint. Wire $5,000 to this account in 20 minutes or you'll never see her alive again!",
        "source": "FBI IC3",
        "kaise": "1. Perpetrators browse social media to identify children on vacations or at concerts away from parents.\n2. Call parent with terrifying screaming sounds in background.\n3. Keep parent on line to prevent them from calling child directly, demanding immediate wire transfer or money order.",
        "flags": [
            "Call comes from unfamiliar phone number or international country code",
            "Caller refuses to let victim speak directly with the supposedly kidnapped family member",
            "Background screams sound muffled, repetitive, or generic ('Help me mom!')",
            "Demands wire transfer or digital payment within an extremely short time window (15-30 minutes)",
            "Forbids hanging up the phone to prevent contacting other relatives"
        ],
        "actions": [
            "Stay calm; attempt to reach your family member on another phone or message their friends",
            "Ask the caller specific questions only your loved one would know (pet's name, childhood memory)",
            "Call 911 or local police immediately from a secondary phone"
        ],
        "icon": "😱"
    },
    {
        "name": "Bank Fraud Department 'Safe Account' Transfer Call",
        "year": 2025,
        "is_latest": False,
        "country": "UK",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 98,
        "desc": "Caller claims to be from your bank's fraud prevention team, warning your account is compromised by corrupt branch staff and instructing you to move money to a 'safe holding account'.",
        "sample": "This is HSBC Fraud Prevention. We have detected suspicious transactions from our Newcastle branch. To safeguard your savings, transfer your balance of £14,200 to our safe holding account.",
        "source": "Action Fraud",
        "kaise": "1. Scammer spoofs official bank phone number shown on back of payment card.\n2. Convinces victim that an insider fraud ring at the local branch is stealing money.\n3. Instructs victim to make high-value online transfer to 'safeguard account' controlled by the criminal syndicate.",
        "flags": [
            "Your bank will NEVER ask you to transfer money to another account for fraud prevention or 'safekeeping'",
            "Caller urges you to lie to bank branch staff if they question the purpose of the transfer",
            "High urgency insisting transfer must occur while remaining on the telephone line",
            "Caller asks for your online banking password, card PIN, or secure token code",
            "Claims that corrupt bank employees are watching your account"
        ],
        "actions": [
            "Hang up immediately; genuine banks never use 'safe holding accounts'",
            "Wait 5 minutes to clear the phone line, or use a different phone to call the number printed on back of bank card",
            "Report scam attempt to your bank fraud department and Action Fraud"
        ],
        "icon": "🏦"
    },
    {
        "name": "Department of Telecom (DoT) 2-Hour Mobile Disconnection Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 96,
        "desc": "Automated IVR call claiming all mobile numbers registered on your Aadhaar will be disconnected within 2 hours due to illegal advertisements and spam complaints.",
        "sample": "This is Department of Telecommunications (DoT). All mobile numbers linked to your Aadhaar card will be blocked in 2 hours due to 1,200 illegal spam SMS. Press 9 for customer care.",
        "source": "I4C India",
        "kaise": "1. Robocall plays official-sounding DoT warning message.\n2. Pressing 9 transfers to fake telecommunications officer.\n3. Officer claims another SIM in victim's name in Assam or Mumbai was used for harassment and demands bribe or banking credentials to issue NOC.",
        "flags": [
            "Department of Telecommunications (DoT) never makes automated calls to citizens threatening phone line disconnections",
            "Robocall asks you to press a digit to speak to a telecommunication officer",
            "Officer claims multiple SIMs registered on your Aadhaar were used in illegal activities",
            "Demands Aadhaar OTP or bank details to issue 'police clearance certificate'",
            "Threatens immediate telecom blacklisting across all national carriers"
        ],
        "actions": [
            "Hang up immediately; DoT does not make disconnection calls",
            "Check total SIM cards registered in your name on official DoT portal: tafcop.sancharsaathi.gov.in",
            "Report fraudulent numbers on Sanchar Saathi Chakshu portal sancharsaathi.gov.in/sfc"
        ],
        "icon": "📞"
    },
    {
        "name": "Amazon Customer Support Unauthorized Purchase Call",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 93,
        "desc": "Robocall stating your Amazon account was charged $999 for an iPhone 16 Pro, asking you to press 1 to speak with security to dispute transaction.",
        "sample": "Amazon Security: An order for Apple iPhone 16 ($999) has been charged to your card. If you did not make this purchase, press 1 now to connect to fraud department.",
        "source": "FTC",
        "kaise": "1. Automated dialers blast millions of landlines and mobile phones.\n2. Connecting to representative leads to scammer asking victim to download AnyDesk or TeamViewer.\n3. Scammer opens mock bank transfer screen to process refund, tricking victim into sending money.",
        "flags": [
            "Amazon never calls customers via robocalls about suspicious orders without prior customer request",
            "Order does not appear in your authentic Amazon account order history",
            "Caller insists on installing remote desktop software on your computer or phone",
            "Representative asks for your banking login to issue a refund",
            "Demands gift cards to reverse the fraudulent transaction"
        ],
        "actions": [
            "Hang up and check your authentic Amazon order history at amazon.com/orders",
            "Never download screen sharing tools recommended by incoming callers",
            "Report scam call to FTC at reportfraud.ftc.gov"
        ],
        "icon": "📦"
    },
    {
        "name": "Australian Taxation Office (ATO) Arrest Phone Scam",
        "year": 2025,
        "is_latest": False,
        "country": "Australia",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 95,
        "desc": "Robocall impersonating Australian Taxation Office stating arrest warrant has been filed with Federal Police for unpaid tax debt.",
        "sample": "This is the Australian Taxation Office. A warrant for your arrest has been registered with the Australian Federal Police. To avoid immediate detention, press 1 to speak with an investigator.",
        "source": "Scamwatch",
        "kaise": "1. Automated calls spoof Canberra or Sydney telephone prefixes.\n2. Operator demands immediate payment using Bitcoin ATM, iTunes gift cards, or bank transfer.\n3. Victims threatened with immediate cancellation of Tax File Number (TFN) or deportation.",
        "flags": [
            "ATO will never threaten immediate arrest, jail, or deportation over the phone",
            "ATO never demands payment via gift cards, prepaid vouchers, or cryptocurrency",
            "Demands you stay on phone while traveling to retail stores to buy gift vouchers",
            "Caller becomes aggressive, abusive, or uses foul language when questioned",
            "Refuses to provide written notice via official myGov inbox"
        ],
        "actions": [
            "Hang up the phone immediately; the ATO never operates in this manner",
            "Check your true tax account status securely by logging into myGov",
            "Report the scam call to Scamwatch at scamwatch.gov.au"
        ],
        "icon": "🦘"
    },
    {
        "name": "CBI / ED Hawala Money Laundering Raid Threat Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 98,
        "desc": "Caller claims to be Enforcement Directorate (ED) or CBI Joint Director stating victim's bank account was used in Rs 200 Crore hawala laundering by a corrupt politician.",
        "sample": "I am ED Joint Director Sharma from New Delhi. In the interrogation of hawala broker Naresh Goyal, your bank account details were found. An ED search warrant is signed for your home.",
        "source": "I4C India",
        "kaise": "1. Sends forged legal seizure notices bearing national emblem via WhatsApp.\n2. Conducts multi-hour interrogation warning of immediate home raid and asset freezing.\n3. Demands victim transfer deposits into 'Government Verification Vault' to prove funds are legitimate.",
        "flags": [
            "Enforcement Directorate and CBI do not conduct official interrogations via WhatsApp calls",
            "Government agencies never require citizens to transfer personal savings for 'fund verification'",
            "Legal notices sent as low-resolution PDFs over WhatsApp with fake seals and spelling mistakes",
            "Caller commands victim to remain confined in room with doors locked",
            "Threatens to notify national television news channels of victim's 'arrest'"
        ],
        "actions": [
            "Disconnect call immediately; legitimate summons are served in person by uniformed officers",
            "Never transfer funds to any bank account provided over the telephone",
            "Call local police station or Cyber Crime Helpline 1930 to report the extortion attempt"
        ],
        "icon": "🏛️"
    },
    {
        "name": "Social Security Administration (SSA) Benefit Termination Call",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 96,
        "desc": "Robocall stating your Social Security Number has been linked to an abandoned rental car filled with drugs in Texas and monthly benefits will be terminated today.",
        "sample": "This is Officer Michael Robinson from the Social Security Administration. An abandoned vehicle with 25kg of drugs was recovered in El Paso registered to your SSN. Press 1 immediately.",
        "source": "FTC",
        "kaise": "1. Spoofs phone number of local SSA field office.\n2. Demands victim confirm their full 9-digit SSN, date of birth, and mother's maiden name.\n3. Instructs victim to convert bank balances into retail gift cards to safeguard against federal seizure.",
        "flags": [
            "SSA never calls citizens threatening benefit termination or arrest",
            "Government cannot cancel or suspend your Social Security Number",
            "Caller demands payment through retail store gift cards or Bitcoin kiosks",
            "Caller ID shows 1-800-772-1213 (spoofed number)",
            "Insists on total secrecy from bank tellers or family members"
        ],
        "actions": [
            "Hang up immediately; do not press 1 to speak with anyone",
            "Report SSA phone scams to Social Security Office of the Inspector General at oig.ssa.gov",
            "Check authentic benefit records at ssa.gov/myaccount"
        ],
        "icon": "🇺🇸"
    },
    {
        "name": "Courier Delivery Confirmation OTP Refund Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 95,
        "desc": "Delivery boy calls claiming he is outside your apartment with an expensive cash-on-delivery package you didn't order, offering to cancel if you share cancellation OTP.",
        "sample": "Hello sir, I am Bluedart delivery executive. I have your parcel of Rs 4,999 cash on delivery. You didn't order? Okay, I will cancel it. Just tell me the 6-digit cancellation OTP sent to your phone.",
        "source": "I4C India",
        "kaise": "1. Scammer triggers netbanking or UPI password reset on victim's phone number.\n2. Concurrently calls pretending to be delivery agent needing 'cancellation code'.\n3. Victim shares OTP thinking it cancels the unwanted parcel, allowing scammer to take over bank account.",
        "flags": [
            "Delivery boys do not require OTPs to cancel orders you did not place",
            "The SMS OTP text clearly mentions: 'OTP for Netbanking Login' or 'UPI PIN Reset'",
            "Delivery boy becomes overly persistent or helpful about canceling quickly",
            "No delivery vehicle or courier executive is physically visible outside your residence",
            "Caller asks you to click a link or forward an SMS code"
        ],
        "actions": [
            "Never share any SMS OTP with delivery personnel, especially for packages you never ordered",
            "Simply tell the delivery boy to return the package to sender as 'Refused by Customer'",
            "Read SMS text carefully to see what the OTP is actually authorizing before reading it aloud"
        ],
        "icon": "🚚"
    },
    {
        "name": "Utility Water & Gas Emergency Shutoff Phone Scam",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 94,
        "desc": "Caller claims your municipal water or gas service will be turned off in 30 minutes due to unpaid commercial meter inspection fee.",
        "sample": "City Water & Power: A service technician is en route to shut off your water meter due to unpaid past-due invoice. Pay $195 immediately over the phone with Zelle to cancel technician dispatch.",
        "source": "FTC",
        "kaise": "1. Targets restaurants, small businesses, and homeowners during busy operating hours.\n2. Threatens catastrophic immediate utility shutoff disrupting operations.\n3. Demands instant electronic payment via Zelle, Venmo, or GreenDot MoneyPak card.",
        "flags": [
            "Municipal utilities provide written past-due warnings by mail weeks before disconnection",
            "Utilities do not accept payment via Zelle, Cash App, or GreenDot prepaid cards",
            "Extreme urgency demanding payment within 30-45 minutes",
            "Caller claims technician is already on the road to your property",
            "Payment request directed to private individual's phone number or email"
        ],
        "actions": [
            "Hang up and check your utility account balance directly on the official municipal website",
            "Call the customer service phone number printed on your physical monthly water/gas bill",
            "Report fraudulent utility collection attempts to the state public utilities commission"
        ],
        "icon": "💧"
    },
    {
        "name": "Google Maps Business Listing Verification Extortion Call",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 92,
        "desc": "Robocall targeting small business owners stating their Google Business Profile is unverified and will be marked permanently closed unless they pay $299 maintenance fee.",
        "sample": "Your Google Maps business listing has not been renewed and will be marked as permanently closed on Google search results within 24 hours. Press 1 to speak with a Google listing specialist.",
        "source": "FTC",
        "kaise": "1. Automated dialer scrapes business phone numbers from Google Maps.\n2. Scammer claims to be an authorized Google representative.\n3. Pressures shop owner into paying recurring monthly fee to maintain their free Google Business profile.",
        "flags": [
            "Google never charges fees to maintain or verify a standard Google Business Profile",
            "Google does not place unsolicited robocalls threatening to delete business listings",
            "Caller demands credit card number over the phone to 'keep profile active'",
            "Representative cannot email you from an authentic @google.com email address",
            "Threatens loss of search rankings and customer reviews within 24 hours"
        ],
        "actions": [
            "Hang up immediately; managing your Google Business Profile is 100% free",
            "Manage your listing directly at business.google.com",
            "File complaint with FTC at reportfraud.ftc.gov"
        ],
        "icon": "📍"
    },
    {
        "name": "Customs Drug Parcel Skype Video Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 98,
        "desc": "Fraudsters initiate Skype video call wearing police uniforms, showing fake CBI arrest warrants claiming victim's Aadhaar was used to send illegal packages to Cambodia.",
        "sample": "We are calling from Crime Branch Cyber Cell. Your Aadhaar card #XXXX was used to open an illicit account in Canara Bank transferring money to Cambodia. Connect on Skype room CBI_Official_Room right now.",
        "source": "I4C India",
        "kaise": "1. Victim receives intimidating IVR call transferred to fake police inspector.\n2. Ordered to install Skype on desktop or mobile.\n3. Fraudster wears genuine-looking uniform and presents fabricated Supreme Court seizure notices, coercing victim into breaking fixed deposits.",
        "flags": [
            "Government law enforcement officers never use Skype or WhatsApp video for official procedures",
            "Arrest warrants or FIRs are never served via chat applications",
            "Victim ordered not to inform spouse, children, or local police station",
            "Officer demands screen sharing to inspect bank balances",
            "Demands liquidation of mutual funds, stocks, and fixed deposits into RTGS accounts"
        ],
        "actions": [
            "Never connect to Skype or video calls with strangers claiming to be police officers",
            "Walk into your nearest local police station to verify any genuine summons",
            "Lodge complaint on cybercrime.gov.in and dial 1930"
        ],
        "icon": "👮"
    },
    {
        "name": "Jury Duty Failure to Appear Arrest Warrant Call",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 95,
        "desc": "Caller claims to be deputy sheriff stating you failed to report for federal jury duty and a bench warrant for contempt of court is active with a $1,500 fine payable via cash voucher.",
        "sample": "This is Deputy Collins from the County Sheriff's Department. You failed to appear for federal grand jury duty this morning. Judge Davis issued a bench warrant. Settle the $1,500 bond immediately.",
        "source": "FBI IC3",
        "kaise": "1. Scammers spoof local sheriff office or county courthouse caller ID.\n2. Provide real names of local judges and courthouse addresses.\n3. Instruct victim to purchase MoneyPak or reloadable debit cards to pay the citation bond over the phone.",
        "flags": [
            "Courts never notify citizens about missed jury duty via unexpected telephone calls",
            "Deputies never demand payment of fines or bonds over the telephone using cash cards",
            "Threatens that squad cars are currently dispatched to your workplace",
            "Demands that you remain on the line while driving to purchase retail gift cards",
            "Refuses to allow in-person payment at the county clerk office"
        ],
        "actions": [
            "Hang up and call the official clerk of courts office using the verified telephone directory",
            "Never purchase gift cards or wire money to cancel an arrest warrant",
            "Report jury scam calls to local sheriff department and FBI IC3"
        ],
        "icon": "⚖️"
    },
    {
        "name": "Health Insurance Policy Renewal Lapse Extortion Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 92,
        "desc": "Caller claims to be from Insurance Regulatory and Development Authority (IRDAI) stating your lapsed policy bonus of Rs 3,50,000 can be released upon paying GST registration fee.",
        "sample": "I am calling from IRDAI Grievance Redressal Cell. You have an unclaimed bonus of Rs 3,45,000 against your old lapsed insurance policy. Pay 18% GST (Rs 32,000) to release the cheque.",
        "source": "I4C India",
        "kaise": "1. Fraudsters buy leaked customer data from insurance lead aggregators.\n2. Quote genuine past policy numbers to build immediate trust.\n3. Convince victim to pay multiple advance charges (GST, NOC fee, legal clearance) to release non-existent bonuses.",
        "flags": [
            "IRDAI does not sell insurance policies, collect fees, or distribute bonus payouts to citizens",
            "Unclaimed bonuses are never released by paying upfront GST fees via personal UPI transfers",
            "Caller promises lakhs of rupees against policies lapsed years ago",
            "Demands that fees be transferred to individual bank accounts rather than the insurance company",
            "Threatens that bonus funds will be confiscated by government if not claimed today"
        ],
        "actions": [
            "Never pay money to claim bonuses on lapsed life or health insurance policies",
            "Contact your original insurance company directly via their official customer service email or branch",
            "Verify facts with IRDAI consumer portal at bimaverosa.irdai.gov.in"
        ],
        "icon": "🏥"
    },
    {
        "name": "Canadian Border Services Agency (CBSA) Seizure Call",
        "year": 2024,
        "is_latest": False,
        "country": "Canada",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 96,
        "desc": "Robocall stating Canada Border Services Agency has intercepted a suspicious parcel with illicit weapons and cash addressed to you, threatening revocation of permanent residency or arrest.",
        "sample": "This is Canada Border Services Agency. A package with illegal weapons and unverified cash registered under your name was seized at Vancouver border. Press 1 to speak with border security.",
        "source": "Canadian Anti-Fraud Centre",
        "kaise": "1. Targets newcomers, international students, and Canadian residents.\n2. Pressing 1 connects to fake CBSA investigator.\n3. Demands Social Insurance Number (SIN) and tells victim to deposit funds into Bitcoin ATM to avoid deportation.",
        "flags": [
            "CBSA never contacts individuals by robocalls demanding money or Social Insurance Numbers",
            "Government of Canada does not accept Bitcoin or prepaid gift cards for penalties or legal bail",
            "Threatens immediate deportation or revocation of Canadian PR status over the phone",
            "Caller demands that victim tell no one and stay on the line until payment is confirmed",
            "Number is spoofed to look like a Canadian government department"
        ],
        "actions": [
            "Hang up the phone immediately; it is an organized extortion scam",
            "Report the call to Canadian Anti-Fraud Centre (CAFC) at 1-888-495-8501 or antifraudcentre.ca",
            "Never disclose your Social Insurance Number to unverified callers"
        ],
        "icon": "🍁"
    },
    {
        "name": "Immigration & Passport Revocation Deportation Call",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 97,
        "desc": "Caller pretending to be USCIS immigration officer telling visa holders (H-1B, F-1) there are critical errors on their I-94 arrival record and ICE agents will deport them unless they pay fine.",
        "sample": "This is Officer Martinez from US Citizenship and Immigration Services. There is a discrepancy on your alien registration file. ICE has an open deportation order unless a $2,200 bond is paid.",
        "source": "FTC",
        "kaise": "1. Scammers exploit vulnerable visa holders and green card applicants.\n2. Threaten immediate immigration detention and career ruin.\n3. Instruct victim to pay bond via wire transfer or cryptocurrency.",
        "flags": [
            "USCIS never calls individuals threatening deportation or demanding immediate telephone bond payments",
            "USCIS issues official paper correspondence (Form I-797) by certified mail",
            "Immigration bonds are never paid via wire transfer, gift cards, or crypto",
            "Caller orders student or worker not to speak with their university DSO or company immigration attorney",
            "Caller ID spoofed to display USCIS customer service 1-800 number"
        ],
        "actions": [
            "Hang up immediately; USCIS does not conduct business by telephone threats",
            "Contact your designated school official (DSO) or company immigration counsel",
            "Check true immigration case status exclusively at egov.uscis.gov"
        ],
        "icon": "🗽"
    },
    {
        "name": "Credit Card APR Rate Reduction Robocall",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 93,
        "desc": "Robocall offering to lower credit card interest rates down to 0% with all major banks, charging upfront service fee of $1,500 that delivers zero interest rate reduction.",
        "sample": "This is Cardholder Services. We can lower your credit card interest rate to 1.9% guaranteed on all major cards. Press 1 now to speak with a credit specialist before this promotion expires.",
        "source": "FTC",
        "kaise": "1. Mass automated robocalls target debt-burdened consumers.\n2. Specialist asks for card numbers, expiration dates, and 3-digit security codes.\n3. Charges $1,500 upfront fee to victim's card; either disappears or performs basic balance transfer victim could do for free.",
        "flags": [
            "Robocall uses vague company name ('Cardholder Services', 'Credit Department')",
            "Guarantees that credit card companies will drop APR to near-zero rates",
            "Demands high upfront processing fee before performing any service",
            "Demands your full 16-digit credit card number and CVV over the phone",
            "Claims to have a special relationship or legal arrangement with Visa or Mastercard"
        ],
        "actions": [
            "Hang up; robocalls pitching credit rate reductions are illegal under FTC Telemarketing Sales Rule",
            "Call your credit card issuer directly using the number on your card to negotiate your own interest rate",
            "Report telemarketing violators to the National Do Not Call Registry at donotcall.gov"
        ],
        "icon": "💳"
    },
    {
        "name": "Flight Ticket Booking Cancellation & Fare Refund Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 94,
        "desc": "After victim searches for airline helpline on Google and dials a spoofed SEO customer care number, scammer claims ticket is cancelled and instructs installing remote desktop to issue refund.",
        "sample": "Yes sir, this is MakeMyTrip / Air India customer desk. Your ticket cancellation refund of Rs 7,200 is approved. Please install QuickSupport app so we can credit money to your UPI.",
        "source": "I4C India",
        "kaise": "1. Cybercriminals create fake Google My Business listings and ads for airline support numbers.\n2. Desperate passenger dials top Google result.\n3. Scammer guides caller to download AnyDesk or enter Rs 7,200 into UPI 'Pay' request instead of receiving money.",
        "flags": [
            "Phone number found on random search engine results instead of official airline contact page",
            "Executive insists that receiving a refund requires downloading AnyDesk or QuickSupport",
            "Executive asks caller to approve a payment request in Google Pay or PhonePe to 'receive money'",
            "Demands debit card number and OTP to initiate customer refund",
            "Call center has noisy domestic background with television or family chatter"
        ],
        "actions": [
            "Obtain customer care numbers exclusively from the airline's official mobile app or ticket booking PDF",
            "Remember: Entering UPI PIN ALWAYS DEBITS money from your account, never credits it",
            "Never install remote screen-sharing tools for travel customer service"
        ],
        "icon": "✈️"
    },
    {
        "name": "Smart Electricity Meter Upgrade Fee Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 95,
        "desc": "Caller claims power company is mandatory-replacing existing meter with digital smart meter, demanding Rs 1,499 installation fee payable via UPI link before electricity is cut off.",
        "sample": "Sir, I am calling from Tata Power / BSES meter department. Your analog meter must be replaced with smart prepaid meter today. Pay Rs 1,499 installation fee on this link or power will be disconnected.",
        "source": "I4C India",
        "kaise": "1. Scammers exploit government smart electricity meter rollout programs.\n2. Threaten power supply disconnection if meter upgrade fee is not paid immediately.\n3. Link directs to phishing payment page harvesting netbanking credentials.",
        "flags": [
            "Power utility companies do not demand online payments via WhatsApp links for meter replacements",
            "Government smart meter installations are funded through utility capital programs and do not require on-the-spot UPI fees",
            "Threatens immediate power outage within 2 hours",
            "Caller reaches from an unverified mobile phone number",
            "Refuses to provide written consumer service order number"
        ],
        "actions": [
            "Check electricity account status in the official discom consumer mobile application",
            "Never pay meter installation fees via private UPI links",
            "Call authorized electricity board helpline to verify technician orders"
        ],
        "icon": "⚡"
    },
    {
        "name": "Social Media Account Recovery 'Hacker' Phone Trap",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 93,
        "desc": "Fraudsters advertise fake phone numbers claiming to be Instagram or Facebook live customer care, charging $200 upfront to 'recover hacked accounts' and stealing remaining accounts.",
        "sample": "Meta Live Support: Account recovery specialist assigned. Pay $150 recovery server fee and share your WhatsApp backup code to restore your locked Instagram page.",
        "source": "FTC",
        "kaise": "1. Victims of hacked social accounts desperately search Google for 'Instagram customer care phone number'.\n2. Call scam call center pretending to be Meta tech engineers.\n3. Scammer charges $150 and tricks victim into revealing 2FA codes for WhatsApp and email, compromising everything.",
        "flags": [
            "Meta, Instagram, and Facebook DO NOT offer incoming telephone customer support for regular accounts",
            "Any phone number claiming to be 'Instagram Live Support' is 100% fraudulent",
            "Caller demands payment via Cash App, Zelle, or gift cards to unlock an account",
            "Asks for SMS verification codes sent to your phone or recovery email password",
            "Guarantees 100% account recovery within 30 minutes"
        ],
        "actions": [
            "Submit account recovery requests exclusively through official in-app recovery flows (instagram.com/hacked)",
            "Never call phone numbers discovered on search engine forums or YouTube comments",
            "Never share 2FA backup codes with third-party callers"
        ],
        "icon": "📸"
    },
    {
        "name": "Pre-Approved Gold Loan at 1% Interest Call",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 91,
        "desc": "Telemarketer offering pre-approved gold loan at 1% annual interest with doorstep gold collection, stealing physical jewelry with fabricated valuation documents.",
        "sample": "Greetings from Muthoot/Manappuram Gold Finance. Special festival offer: 1% annual interest on gold loan with home pickup! Our valuer will visit your home today to weigh gold and disburse cash.",
        "source": "I4C India",
        "kaise": "1. Telemarketer pitches unrealistically cheap loan interest rate with home convenience.\n2. Accomplice arrives at home wearing branded lanyard with fake receipt book.\n3. Takes victim's gold ornaments for 'purity testing at branch' and flees.",
        "flags": [
            "Reputable gold loan NBFCs require borrowers to bring physical jewelry to authorized branches for testing and safe custody",
            "1% annual interest rate is far below prevailing market rates",
            "Representative insists on taking jewelry away without disbursing immediate bank transfer",
            "Receipt provided has spelling errors or lacks registered NBFC branch stamp",
            "Caller reached from personal mobile phone rather than registered corporate line"
        ],
        "actions": [
            "Pledge gold jewelry exclusively inside authorized physical bank or NBFC branch premises",
            "Never hand over gold ornaments to strangers visiting your home",
            "Verify company credentials on official Reserve Bank of India register"
        ],
        "icon": "🪙"
    },
    {
        "name": "High Court Legal Notice Whatsapp Video Extortion",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 97,
        "desc": "Fraudsters initiate WhatsApp video call showing realistic courtroom setup with an actor dressed in lawyer gown claiming a cheque bounce non-bailable warrant is issued against victim.",
        "sample": "I am Advocate K.R. Sharma representing High Court. Under Section 138 NI Act, a non-bailable arrest warrant is in my hand. Transfer Rs 45,000 compromise fee now to stop police dispatch.",
        "source": "I4C India",
        "kaise": "1. Calls victim with background showing Indian courtroom bench and legal emblems.\n2. Shows fabricated PDF notice with fake stamps of High Court and judicial magistrate.\n3. Threatens that local police are en route unless out-of-court settlement fee is paid via UPI immediately.",
        "flags": [
            "Courts and lawyers never issue or serve arrest warrants over WhatsApp video calls",
            "Judicial warrants are physically served by police officers in uniform with official court seal",
            "Cheque bounce settlements under Section 138 require formal written compromise petitions in open court",
            "Demands immediate payment to a private individual UPI ID",
            "Caller uses aggressive intimidatory language to prevent victim from consulting a personal lawyer"
        ],
        "actions": [
            "Hang up the video call immediately; no legal process operates over WhatsApp video",
            "Consult your own independent lawyer to verify any genuine legal disputes",
            "File complaint with Cyber Police on helpline 1930 and cybercrime.gov.in"
        ],
        "icon": "⚖️"
    },
    {
        "name": "Vehicle Insurance Policy Renewal Lapse Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 92,
        "desc": "Caller claims to be from PolicyBazaar or insurance company stating car insurance policy expired yesterday and vehicle will be impounded unless renewed via their payment link.",
        "sample": "Sir, your Maruti Swift insurance expired yesterday. Traffic police has flagged your RC. Renew right now on 40% discount for Rs 4,200: I am sending payment link on WhatsApp.",
        "source": "I4C India",
        "kaise": "1. Telemarketers harvest vehicle registration data from state transport databases.\n2. Call vehicle owners near actual policy expiration dates.\n3. Send phishing link or take payment via personal UPI, providing completely fake PDF policy certificate with non-existent policy number.",
        "flags": [
            "Caller asks for payment to private UPI ID instead of official insurance aggregator gateway",
            "Offers massive discounts (40% - 60%) that violate IRDAI tariff regulations",
            "Payment link destination is not the official insurer domain (e.g. icicilombard.com)",
            "Policy PDF issued has invalid QR code and does not reflect in Parivahan mParivahan app",
            "Caller creates false panic claiming vehicle is already blacklisted on highway cameras"
        ],
        "actions": [
            "Renew vehicle insurance directly through official insurer website or authorized mobile app",
            "Verify policy details immediately on the national transport portal: parivahan.gov.in",
            "Never send insurance premiums to personal UPI mobile numbers"
        ],
        "icon": "🚗"
    },
    {
        "name": "Foreign University Admission Processing Fee Call",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 93,
        "desc": "Scammer calls students aspiring to study abroad claiming an elite UK or Canadian university has accepted their profile with 80% scholarship, demanding Rs 75,000 visa letter fee.",
        "sample": "Congratulations! University of Manchester has selected your application for MS Computer Science with £15,000 scholarship. Pay Rs 75,000 CAS letter deposit before 5 PM to confirm your seat.",
        "source": "I4C India",
        "kaise": "1. Fraudulent education consultancy collects student contact details from education fairs.\n2. Issues fabricated university admission offer letter with forged seals.\n3. Takes tuition and visa processing fee into domestic shell accounts and shuts down office.",
        "flags": [
            "Student never formally applied to the university or took mandatory English tests (IELTS/TOEFL)",
            "University never asks international tuition deposits into private Indian bank accounts",
            "Unrealistic 80% - 100% scholarship offered with low academic test scores",
            "High pressure requiring payment within hours to 'hold international quota'",
            "Consultant refuses to let student communicate directly with university admissions office"
        ],
        "actions": [
            "Verify admission offers directly with the university international admissions office via their .ac.uk or .edu email",
            "Pay tuition fees exclusively through official university international wire platforms (Flywire, Convera)",
            "Check consultancy registration on official education department portals"
        ],
        "icon": "🎓"
    },
    {
        "name": "ATM Card Expiry & Microchip Upgrade Robocall",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 96,
        "desc": "Caller claims to be bank card department manager stating ATM magnetic stripe card will stop functioning tonight unless upgraded to EVM microchip over phone.",
        "sample": "Dear customer, your SBI ATM card is expiring today. To upgrade to new free microchip card without visiting branch, verify your 16-digit card number and CVV on this call.",
        "source": "I4C India",
        "kaise": "1. Caller pretends to be bank card manager assisting busy customer.\n2. Convinces victim to read out 16-digit card number, expiration date, and CVV on back of card.\n3. Scammer triggers online shopping transaction and asks victim for incoming 6-digit 'upgrade code' (which is the purchase OTP), looting bank account.",
        "flags": [
            "Bank employees NEVER ask for card CVV, expiry date, or ATM PIN under any circumstances",
            "New chip cards are automatically dispatched to customer's registered home address by post",
            "Caller claims card will be permanently cancelled within 24 hours if not verified on phone",
            "Caller asks for the OTP received on SMS, falsely calling it a 'card verification code'",
            "Call comes from standard 10-digit mobile number"
        ],
        "actions": [
            "Never share 16-digit card number, CVV, or SMS OTP over any phone call",
            "Hang up and block the phone number immediately",
            "If details were shared, lock card immediately via your official mobile banking app"
        ],
        "icon": "💳"
    },
    {
        "name": "Mobile Tower Installation Advance Rent Scam Call",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 94,
        "desc": "Caller offers Rs 50,000 monthly rent plus Rs 30 Lakh advance to install Jio or Airtel mobile tower on victim's empty plot or rooftop, demanding registration tax upfront.",
        "sample": "Jio Tower Division: Your plot has been approved for 5G mobile tower. You will get Rs 45,000 monthly rent + Rs 25 Lakh advance cheque. Deposit Rs 18,500 government environmental tax to start installation.",
        "source": "I4C India",
        "kaise": "1. Sends official-looking forged approval letters bearing Department of Telecom logo.\n2. Promises lucrative recurring monthly rental income and one family member employment.\n3. Extracts multiple advance fees (survey fee, environmental clearance, NOC tax) before disappearing.",
        "flags": [
            "Telecom carriers and tower companies (Indus Towers) do NOT charge property owners fees to install towers",
            "Promises unrealistically high monthly rent (Rs 40,000 - Rs 70,000) for residential rooftops",
            "Demands government clearance fee or environmental tax transferred into private bank account",
            "Approval letter sent via WhatsApp or email filled with spelling and grammar mistakes",
            "Uses telecom brand logos (Jio, Airtel) without corporate authorization"
        ],
        "actions": [
            "Never pay advance money to get a mobile tower installed on your property",
            "Check guidelines on official Department of Telecom website: dot.gov.in",
            "Apply directly through verified portals of genuine infrastructure providers like Indus Towers"
        ],
        "icon": "🗼"
    },
    {
        "name": "Fake Police FIR Compromise Settlement Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Call",
        "cat_slug": "call-impersonation",
        "cat_name": "Call & Impersonation",
        "score": 97,
        "desc": "Caller claims to be Station House Officer (SHO) from another state stating an FIR for sexual harassment or cheating has been registered against victim, demanding bribe to quash case.",
        "sample": "I am SHO Arvind Kumar from Gomti Nagar Police Station Lucknow. A girl has filed an FIR #281/24 against your phone number for criminal intimidation. Pay Rs 50,000 settlement to settle matter out of court.",
        "source": "I4C India",
        "kaise": "1. Criminals obtain victim's name, phone number, and workplace from LinkedIn or Truecaller.\n2. Call with high aggression, yelling legal IPC sections and threatening public embarrassment.\n3. Demand immediate UPI transfer to 'compromise' the fabricated complaint before arrest team departs.",
        "flags": [
            "Genuine police officers never call accused individuals demanding money to cancel an FIR",
            "Refuses to provide certified copy of FIR or station diary entry number",
            "Demands immediate payment via PhonePe, Google Pay or Paytm to private numbers",
            "Threatens to contact victim's employer or parents to destroy their reputation",
            "Pressures victim not to contact a local lawyer"
        ],
        "actions": [
            "Do not panic and never transfer any money over the phone",
            "Tell caller you are visiting your local city police station to verify the FIR with their senior officers",
            "Lodge complaint immediately with Cyber Crime Helpline 1930"
        ],
        "icon": "👮"
    }
]

print(f"Cat4 loaded: {len(cat4)} scams")
