# Category 8: Financial / Banking Scams (32 scams)
cat8 = [
    {
        "name": "UPI 'Collect Request' PIN Reverse Trap (Pay to Receive Scam)",
        "year": 2026,
        "is_latest": True,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 99,
        "desc": "Fraudster posing as buyer on OLX sends a UPI 'Collect Request' of Rs 15,000 to the seller, falsely claiming entering UPI PIN will credit the money into seller's bank account. Entering PIN immediately deducts money.",
        "sample": "Sir, I am sending you Rs 15,000 for your old refrigerator on Google Pay. You will get a notification on PhonePe / GPay. Just click 'Pay' and enter your 4-digit UPI PIN to receive the money into your account.",
        "source": "I4C India",
        "kaise": "1. Scammer contacts OLX seller agreeing immediately to full asking price without bargaining.\n2. Sends a 'Collect' request in PhonePe or Google Pay instead of initiating a payment transfer.\n3. Convinces victim that UPI technology requires entering their secret PIN to 'receive and verify' incoming deposits, instantly transferring funds to the scammer.",
        "flags": [
            "Entering your secret UPI PIN ALWAYS DEBITS money from your account — PIN is NEVER required to receive money",
            "Notification in payment app displays 'Collect Request' or 'Pay' button instead of showing money credited",
            "Buyer agrees to purchase high-value furniture or electronics without physical inspection",
            "Buyer refuses to meet in person or conduct standard cash exchange",
            "Buyer insists you stay on phone while accepting the payment notification"
        ],
        "actions": [
            "GOLDEN UPI RULE: You NEVER need to enter your UPI PIN to receive money. PIN is used ONLY to send money.",
            "Decline all incoming 'Collect' requests from unfamiliar individuals on Google Pay, PhonePe, and Paytm",
            "Report fraudulent UPI IDs immediately on the National Cyber Crime Reporting Portal (cybercrime.gov.in) and dial 1930"
        ],
        "icon": "💸"
    },
    {
        "name": "Predatory Instant Loan Apps & Contact List Blackmail Syndicate",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 99,
        "desc": "Unregistered instant loan apps (Lightning Loan, CashPark) offer quick Rs 5,000 loans with zero documents, disbursing only Rs 3,000 after deductions. After 6 days, syndicates morph victim's photos with pornography and broadcast them to their entire phone contact list demanding extortionate payments.",
        "sample": "Need emergency cash? Get Rs 10,000 instant loan in 2 minutes without CIBIL score! Install Cash-Express.apk now. After 6 days: Gang texts all contacts: 'This person is a fraud defaulter and sex offender [attached morphed explicit photo]'.",
        "source": "I4C India",
        "kaise": "1. Victims install unverified APK files advertised on social media promising instant collateral-free microloans.\n2. App mandates permissions for complete Contacts, Gallery, and Call Logs.\n3. Disburses partial loan (Rs 2,800 on Rs 5,000 loan) with 50% interest due in 6 days; if unpaid, call center agents harass elderly parents and female colleagues with obscene edited photos.",
        "flags": [
            "Loan app is downloaded as an APK file from web links or obscure third-party websites outside Google Play Store",
            "App demands permissions completely irrelevant to lending: full Contacts book, Camera, and Photo Gallery access",
            "Tenure of the loan is extremely short (5 to 7 days) instead of standard statutory minimums (90 days)",
            "Astronomical processing fees deducted upfront (taking Rs 2,000 out of Rs 5,000 loan)",
            "Lending company has no official Non-Banking Financial Company (NBFC) license registered with the Reserve Bank of India"
        ],
        "actions": [
            "Borrow exclusively from RBI-registered banks and licensed NBFCs (verify company on rbi.org.in)",
            "Never grant Contacts or Media Storage permissions to financial applications",
            "If blackmailed, do NOT pay; file immediate police report under IPC Section 506/509 and dial 1930"
        ],
        "icon": "📱"
    },
    {
        "name": "Business Email Compromise (BEC) Wire Redirection Fraud",
        "year": 2026,
        "is_latest": True,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 98,
        "desc": "Hackers compromise corporate email accounts of a major vendor or supplier, monitor invoice threads, and send updated wire instructions directing a $250,000 invoice payment to a criminal offshore bank account.",
        "sample": "Dear Accounts Payable Team, Please note our primary bank account is undergoing corporate year-end audit. For Invoice #INV-8921 ($185,000), remit payment to our secondary escrow account at Wells Fargo: [New Account Details].",
        "source": "FBI IC3",
        "kaise": "1. Attackers gain access to vendor's email system via spear-phishing or credential theft.\n2. Set up hidden inbox forwarding rules and monitor pending multi-million dollar transactions.\n3. At the exact moment payment is due, inject an email from the vendor's real address (or lookalike domain) providing 'updated banking coordinates'.",
        "flags": [
            "Sudden last-minute modification of standard wire transfer routing coordinates or bank names",
            "Supplier claims urgent financial audit, tax restructuring, or banking migration necessitates new account details",
            "Email domain has subtle character substitution (e.g. @supp1ier.com instead of @supplier.com)",
            "Sender urges accounts payable staff to bypass standard dual-control phone confirmation protocols",
            "Telephone number listed in the new invoice footer differs from the established vendor contract directory"
        ],
        "actions": [
            "MANDATORY VERIFICATION: Always verify any bank account modification via known, out-of-band telephone contact with the vendor's chief financial officer",
            "Establish strict dual-signature verbal verification policies for all electronic wire transfers exceeding $5,000",
            "If fraudulent transfer occurred within 48 hours, contact your bank immediately and request a Federal Reserve Financial Fraud Kill Chain recall"
        ],
        "icon": "💼"
    },
    {
        "name": "ATM Skimming & Deep-Insert Reader Card Data Theft",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 96,
        "desc": "Criminals install microscopic magnetic stripe reader inserts inside ATM card slots and hidden pinhole spy cameras or false keypads above keypad, cloning cards and stealing PINs for overnight cash withdrawals.",
        "sample": "Customer inserts debit card into standalone outdoor ATM at gas station. Deep-insert skimmer records magnetic stripe; micro-camera disguised as brochure holder records 4-digit PIN. Card cloned for $1,000 cash withdrawals in Mexico.",
        "source": "FBI IC3",
        "kaise": "1. Gang attaches ultra-thin wafer skimmer deep inside the motorized ATM throat mechanism.\n2. Pinhole camera positioned above keyboard records customer fingers entering PIN.\n3. Data transmitted via Bluetooth to nearby vehicle; gang burns cloned magnetic cards and drains daily limits.",
        "flags": [
            "ATM card slot bezel feels loose, unusually bulky, or wobbly when physically manipulated",
            "Keypad feels spongy, misaligned, or raised higher than the surrounding metal console",
            "Unusual plastic attachments, fake mirrors, or brochure holders mounted directly above the keypad",
            "ATM is located in poorly lit, unmonitored standalone outdoor location (convenience stores, gas stations)",
            "Card insertion feels unusually tight or encounters abnormal mechanical resistance"
        ],
        "actions": [
            "Always cover the keypad completely with your other hand or wallet while typing your PIN",
            "Use ATMs physically located inside well-lit, camera-monitored bank branch vestibules",
            "Use contactless NFC card tapping (Apple Pay / Google Wallet / contactless chip) at ATMs instead of inserting magnetic cards"
        ],
        "icon": "🏧"
    },
    {
        "name": "Fake Spoofed UPI Payment Screenshot Trick",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 94,
        "desc": "Customer in retail shop or taxi shows a realistic fake Paytm or Google Pay app on their phone displaying 'Paid Rs 1,800 to [Shop Name]' with animated green tick mark and mock soundbox audio, walking away with goods without real money ever being transferred.",
        "sample": "Customer purchases branded shoes worth Rs 3,500. Shows shopkeeper screen of 'Paytm Spoof' app displaying green checkmark: 'Payment Successful: Rs 3,500'. Shopkeeper checks phone 10 minutes later: zero money received in bank account.",
        "source": "I4C India",
        "kaise": "1. Scammer installs rogue Android app named 'Paytm Spoof' or 'GPay Prank' from APK repositories.\n2. Inputs shopkeeper's business name, phone number, and exact purchase amount.\n3. App generates pixel-perfect imitation of successful payment screen complete with realistic tick animation and synthetic voice chime.",
        "flags": [
            "Customer shows payment screen on their phone screen but your authentic bank SMS or merchant soundbox did NOT chime",
            "Customer rushes to leave shop immediately without waiting for your personal confirmation",
            "Customer claims: 'Server is slow, bank SMS takes 15 minutes, look at my successful screenshot!'",
            "Transaction reference number (UTR) is missing or has incorrect digit length",
            "Shopkeeper's own merchant business app shows zero new transactions"
        ],
        "actions": [
            "Never release goods based on customer's phone screen; verify payment solely on YOUR OWN phone or registered Soundbox speaker",
            "Install a verified merchant voice alert device (Paytm / PhonePe Soundbox) that announces successful deposits in real time",
            "If customer insists payment went through, ask them to wait until credit is reflected in your merchant dashboard"
        ],
        "icon": "📱"
    },
    {
        "name": "Cheque Washing & Chemical Alteration Signature Fraud",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 95,
        "desc": "Thieves fish outgoing paper checks from blue USPS postal collection boxes, erase the payee name and dollar amount using acetone chemical solvent, and rewrite check to a criminal mule for $12,500.",
        "sample": "Homeowner mails $45 water utility paper check from neighborhood blue postal box. Thieves steal mail, wash check with nail polish remover, change payee to 'Marcus Williams' and amount to '$8,450', and cash at check cashing store.",
        "source": "FTC",
        "kaise": "1. Criminals use stolen universal postal collection keys or adhesive string traps to fish envelopes from street mailboxes.\n2. Use household solvents (acetone, bleach) to chemically dissolve standard ballpoint pen ink while preserving original signature.\n3. Rewrite payee and inflated dollar amount in indelible gel pen and deposit into newly opened mule accounts.",
        "flags": [
            "Checks written to utilities or landlords are not credited to your billing account despite showing cleared at bank",
            "Digital check image in online banking shows altered, mismatched, or trembling handwriting in payee line",
            "Check cleared for significantly higher amount than recorded in your personal checkbook register",
            "Paper check had been dropped inside a street collection box rather than inside a postal facility",
            "Payee name does not match the invoice or merchant you intended to pay"
        ],
        "actions": [
            "Use indelible pigmented gel ink pens (e.g. Uni-ball 207) which chemically bond with paper fibers and resist solvents",
            "Drop outgoing mail containing checks directly inside the postal lobby rather than outdoor street boxes",
            "Switch to electronic online bill pay services instead of mailing paper checks through the mail"
        ],
        "icon": "✍️"
    },
    {
        "name": "Credit Card Limit Enhancement OTP Phishing Call",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 97,
        "desc": "Caller claims to be credit card division manager offering to double credit card limit from Rs 1,50,000 to Rs 3,00,000 with zero charges and lifetime waiver of annual fees, requesting card details and OTP.",
        "sample": "Good afternoon sir, I am calling from ICICI/HDFC Credit Card Upgrade Department. Your card has been upgraded to Platinum with limit increased to Rs 3,50,000. Just verify your 16-digit card number and OTP to activate new limit.",
        "source": "I4C India",
        "kaise": "1. Telemarketer speaks with professional executive authority quoting victim's name and partial card type.\n2. Convinces victim to read out 16-digit card number, expiry date, and CVV on back of card.\n3. Triggers international e-commerce transaction and asks for incoming SMS 'limit authorization code' (which is the actual purchase OTP).",
        "flags": [
            "Banks NEVER call customers asking for card CVV, expiry date, or OTP to increase credit limits",
            "Genuine credit card limit increases are offered and accepted directly inside your official mobile banking app with a single click",
            "Caller claims card will be downgraded if you refuse the free limit enhancement offer today",
            "Caller asks you to read out the 6-digit OTP received on your mobile phone",
            "Call is received from standard mobile number instead of verified bank corporate contact lines"
        ],
        "actions": [
            "Hang up immediately; genuine banks NEVER ask for card numbers or OTPs over phone calls",
            "Accept legitimate limit enhancement offers only through your official mobile banking app under 'Card Services'",
            "If details were disclosed, immediately lock card using bank mobile app and call fraud hotline to block"
        ],
        "icon": "💳"
    },
    {
        "name": "Aadhaar Enabled Payment System (AePS) Biometric Cash Drain",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 98,
        "desc": "Criminals obtain leaked biometric fingerprint scans from property registration deeds, clone fingerprints onto silicone gummy molds, and make unauthorized cash withdrawals from victim's bank account via AePS micro-ATMs without requiring OTP or ATM card.",
        "sample": "Victim wakes up to SMS: 'Rs 10,000 withdrawn from your bank account via AePS Micro-ATM at 3:15 AM'. Victim still has ATM card in wallet and received no SMS OTP.",
        "source": "I4C India",
        "kaise": "1. Fraudsters scrape land registry and deed documents containing scanned biometric fingerprints from state revenue portals.\n2. Fabricate 3D silicone copies of victim's thumbprint.\n3. Approach corrupt or unaware business correspondents (BC) operating AePS micro-ATMs in remote districts, withdrawing daily cash limits using cloned fingerprints and victim's Aadhaar number.",
        "flags": [
            "Unauthorized cash withdrawal occurs without physical ATM card usage or incoming SMS OTP",
            "SMS notification mentions transaction mode as 'AePS Cash Withdrawal' or 'Micro-ATM'",
            "Victim recently completed property registration, land sale, or SIM card KYC where fingerprints were collected",
            "Multiple rapid withdrawals occurring in Rs 10,000 increments (statutory AePS transaction ceiling)",
            "Transactions originate from unfamiliar rural customer service points in other states"
        ],
        "actions": [
            "CRITICAL PROTECTION: Lock your Aadhaar biometrics immediately using the official mAadhaar app or myaadhaar.uidai.gov.in (biometrics stay locked until temporarily unlocked for 10 minutes when needed)",
            "File complaint with National Cyber Crime Helpline 1930 and notify your bank's branch manager to disable AePS facility",
            "Check Bank-Aadhaar linking status on UIDAI portal to manage linked bank accounts"
        ],
        "icon": "🖐️"
    },
    {
        "name": "Mandate Fraud & Direct Debit Account Hijack",
        "year": 2024,
        "is_latest": False,
        "country": "UK",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 94,
        "desc": "Criminals contact a business or consumer pretending to be an organization to which regular payments are made (supplier, landlord, sports club), instructing them to redirect standing orders or direct debits to a new bank account.",
        "sample": "Notice from Property Management: Our rental collection account has changed to Barclays Bank. Please cancel your existing standing order of £1,450/month and setup new recurring transfer to account #891241.",
        "source": "Action Fraud",
        "kaise": "1. Scammers identify regular recurring payment obligations from discarded mail or intercepted statements.\n2. Contact paying party with formal forged letterhead announcing new banking coordinates.\n3. Recurring monthly lease or supplier payments flow to criminal accounts for months before discovery.",
        "flags": [
            "Notification of changes to bank details received out of the blue by email or standard postal letter",
            "Urgent request to alter recurring standing order instructions before the next billing cycle",
            "New bank account is held in an individual's name rather than the corporate business name",
            "Contact phone number on the letterhead differs from previous agreements",
            "No formal notice was provided on the company's official customer portal"
        ],
        "actions": [
            "Never amend recurring payment mandates or direct debits without independently verifying the change with the payee using trusted historical phone numbers",
            "Check with your bank to verify if payments fall under the Direct Debit Guarantee scheme",
            "Report mandate fraud attempts immediately to Action Fraud"
        ],
        "icon": "📄"
    },
    {
        "name": "Cardless ATM Cash Withdrawal OTP Interception",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 96,
        "desc": "Scammer initiates cardless cash withdrawal (SBI YONO Cash / ICICI Cardless Cash) from compromised netbanking account, calling victim pretending to be security officer asking for 'system security code' to complete cash withdrawal at physical ATM.",
        "sample": "Sir, this is Bank Security. We are locking an unauthorized login on your YONO account. A 6-digit cancellation reference was sent to your phone. Read it immediately to prevent hacker withdrawal.",
        "source": "I4C India",
        "kaise": "1. Scammer acquires victim's netbanking login credentials via phishing.\n2. Generates an instant Cardless Cash Withdrawal transaction for Rs 20,000 on mobile banking app.\n3. Bank texts a 6-digit transaction PIN; scammer tricks victim into revealing it over phone while standing directly in front of an ATM, dispensing physical currency.",
        "flags": [
            "Incoming SMS explicitly states: 'Cardless Cash Withdrawal Reference Code for ATM'",
            "Caller claims code is for 'security lockdown' or 'cancellation' when the text clearly states cash withdrawal",
            "High urgency demanding code within 3 minutes before reference expires",
            "Caller refuses to allow customer to contact local branch",
            "Transaction initiated during late night or early morning hours"
        ],
        "actions": [
            "NEVER share cardless ATM cash withdrawal codes or reference numbers with anyone",
            "Read SMS messages carefully: never confuse a cash withdrawal authorization code with a cancellation token",
            "Freeze netbanking access immediately via your bank mobile app if credentials are compromised"
        ],
        "icon": "🏧"
    },
    {
        "name": "Debit Card Cash-Back Credit Reversal Scam",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 93,
        "desc": "Fraudster calls offering a Rs 5,000 cashback credit on your debit card from Diwali shopping, directing you to open your mobile banking app and approve an IMPS transaction to receive credit.",
        "sample": "Dear customer, you won Rs 4,800 cashback on your festive debit card spends! Open your bank mobile app, go to 'Funds Transfer' and enter this verification merchant code 098214 to receive cash in your account.",
        "source": "I4C India",
        "kaise": "1. Scammer plays on greed for free festive cash rewards.\n2. Convinces victim that inputting numbers into 'Funds Transfer' or 'Pay' tab deposits money.\n3. The 'verification merchant code' is actually the scammer's bank account or UPI ID, transferring victim's savings out.",
        "flags": [
            "Banks NEVER ask customers to initiate outgoing fund transfers or enter account numbers to receive cashback",
            "Legitimate cashback is credited automatically to your account statement with zero customer interaction",
            "Caller guides you step-by-step through outgoing transfer menus in your mobile banking app",
            "Caller uses misleading terms like 'credit validation code' to disguise an outgoing account number",
            "Demands transaction approval via biometric fingerprint or transaction PIN"
        ],
        "actions": [
            "Legitimate cashback rewards are automatically deposited without requiring manual transfers",
            "Never initiate outgoing fund transfers based on instructions from incoming telephone callers",
            "Hang up and check official reward points balance directly in your bank mobile application"
        ],
        "icon": "🎁"
    },
    {
        "name": "Zelle / Venmo Bank Account Drainage Phishing Call",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 97,
        "desc": "Caller impersonating Chase or Bank of America Fraud Department texts asking if you authorized a $1,200 Zelle payment. When you reply 'NO', they call you immediately, instructing you to 'reverse the payment' by sending Zelle to your own phone number, which actually transfers funds to the scammer.",
        "sample": "Chase Fraud Alert: Did you authorize a Zelle payment of $1,400 to 'Zelle Transfer'? Reply YES or NO. [User replies NO]. Caller ID 'Chase Bank' calls: 'To reverse this fraud, send $1,400 to your own phone number via Zelle.'",
        "source": "FTC",
        "kaise": "1. Scammer links victim's phone number to a criminal Zelle account in their own bank profile.\n2. Calls victim using spoofed bank telephone numbers claiming to stop an active fraud in progress.\n3. Guides victim to send money to 'themselves' via Zelle, which deposits directly into the scammer's linked institution.",
        "flags": [
            "Bank fraud representatives NEVER ask you to send money to yourself or anyone else via Zelle to reverse a transaction",
            "High urgency claiming funds will be permanently lost if you do not complete the transfer while on the line",
            "Caller asks for the one-time passcode sent to your phone to 'verify your identity'",
            "Caller instructs you to ignore warning prompts in the banking app ('Recipient is a new contact')",
            "Caller claims internal bank software will automatically bounce the test transaction back"
        ],
        "actions": [
            "Hang up immediately; your bank will NEVER ask you to make a Zelle transfer to stop fraud",
            "Call your bank directly using the telephone number printed on the back of your debit card",
            "Report fraudulent Zelle activity to your financial institution and file a report at reportfraud.ftc.gov"
        ],
        "icon": "🏦"
    },
    {
        "name": "Foreign Currency Wire Transfer Intermediary Fee Trap",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 92,
        "desc": "Victim receives a notification from a fake international commercial bank stating an incoming wire transfer of $500,000 is on hold pending payment of an IMF / World Bank currency conversion stamp.",
        "sample": "Geneva Private Bank: Inward wire transfer of $750,000 is currently held in our clearing vault. To release SWIFT MT103 transmission to your local bank, pay $3,500 International Monetary Clearance Stamp.",
        "source": "Interpol",
        "kaise": "1. Combines elements of commercial business fraud and inheritance schemes.\n2. Sends fabricated SWIFT transmission slips and central bank clearance documents.\n3. Collects sequential fees for imaginary international regulatory certifications.",
        "flags": [
            "You are not legitimately expecting any large international commercial wire transfer",
            "Central banks, the IMF, and SWIFT do NOT hold funds or demand fees from individual citizens",
            "Legitimate international wire processing fees are deducted directly from the transmitted principal amount",
            "Documents feature fake gold seals, national crests, and forged signatures of finance ministers",
            "Payment of fees is demanded via cryptocurrency or wire transfer to private accounts"
        ],
        "actions": [
            "Never pay advance clearance fees or tax deposits to receive international wire transfers",
            "Consult the international wire department at your local bank to inspect any suspicious SWIFT documentation",
            "Report international wire fraud attempts to Interpol and national police authorities"
        ],
        "icon": "🌐"
    },
    {
        "name": "Overdraft Protection Fee Refund Phone Trap",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 91,
        "desc": "Caller claims your bank was fined by federal regulators for illegal overdraft fee overcharges and you are entitled to a $450 direct compensation refund if you confirm your routing and account number.",
        "sample": "Consumer Financial Protection Bureau Settlement: You have $480 in refunded bank overdraft penalty fees ready for direct deposit into your checking account. Press 1 to verify your routing and account numbers.",
        "source": "FTC",
        "kaise": "1. Telemarketers exploit consumer resentment over high bank overdraft penalty fees.\n2. Claim federal class action or regulatory enforcement requires immediate refund distribution.\n3. Collects bank routing numbers, account numbers, and debit card credentials to initiate unauthorized ACH debits.",
        "flags": [
            "Regulatory agencies (CFPB, FDIC) never call consumers asking for bank details to distribute settlement funds",
            "Official class action settlements are administered via formal postal notices and dedicated settlement portals",
            "Caller asks for full checking account details, debit card CVV, or online banking passwords",
            "Robocall uses vague agency names like 'Consumer Settlement Claims Division'",
            "Demands immediate response claiming unclaimed settlement funds will revert to the state treasury"
        ],
        "actions": [
            "Hang up the phone; do not disclose banking details to unsolicited callers",
            "Verify legitimate class action settlement information on consumeraction.org or ftc.gov/enforcement/refunds",
            "Report imposter calls to the Consumer Financial Protection Bureau (CFPB) at consumerfinance.gov"
        ],
        "icon": "⚖️"
    },
    {
        "name": "Dormant Bank Account Unclaimed Balance Release Scam",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 93,
        "desc": "Caller claims an old forgotten savings account opened in your name has an unclaimed balance of Rs 1,85,000 under RBI UDGAM portal, requiring Rs 12,000 stamp duty fee to transfer to your active account.",
        "sample": "RBI UDGAM Cell: Unclaimed deposit of Rs 1,85,000 detected under your PAN in an old Punjab National Bank account. Pay Rs 11,500 Stamp Duty Clearance to transfer funds directly to your active SBI account.",
        "source": "I4C India",
        "kaise": "1. Scammers exploit awareness of the Reserve Bank of India's genuine UDGAM unclaimed deposits portal.\n2. Forge official RBI letterheads showing large unclaimed balances against victim's name.\n3. Demand upfront processing and legal clearance fees before disappearing.",
        "flags": [
            "The RBI UDGAM portal is 100% FREE to search and claim unclaimed deposits",
            "The Reserve Bank of India NEVER calls citizens, holds personal funds, or demands clearance fees",
            "Claims on dormant bank accounts are processed directly and free of charge by the holding commercial bank",
            "Payment requested via UPI to a private individual account rather than official government treasury",
            "Threatens that unclaimed funds will be permanently confiscated by government if not claimed today"
        ],
        "actions": [
            "Search for genuine unclaimed deposits for free on the official RBI UDGAM portal: udgam.rbi.org.in",
            "Visit the nearest branch of the bank where you previously held an account to file a free claim",
            "Never pay third parties or agents to claim your own dormant bank deposits"
        ],
        "icon": "🏦"
    },
    {
        "name": "Cryptocurrency Exchange Account Freeze Wire Extortion",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 96,
        "desc": "Victim receives email mimicking Coinbase or Binance stating account is flagged for international money laundering and all cryptocurrency will be forfeited unless $5,000 security collateral is wired.",
        "sample": "Coinbase Compliance Alert: Your account has been flagged for AML Section 314 violation. To prevent total asset forfeiture and federal referral, transfer $5,000 security deposit to our compliance escrow wallet within 24h.",
        "source": "FBI IC3",
        "kaise": "1. Spear-phishing email uses official exchange branding and authoritative regulatory terminology.\n2. Link opens fake compliance portal demanding security collateral.\n3. Scammers siphon wired collateral and demand additional 'unfreeze fees'.",
        "flags": [
            "Legitimate crypto exchanges NEVER require users to deposit additional collateral to resolve AML compliance reviews",
            "Sender email address is not from official corporate domain (e.g. uses @coinbase-compliance.net instead of @coinbase.com)",
            "Threatens total asset forfeiture within arbitrary short deadline (24 hours)",
            "Requires transfer of funds into an external unhosted cryptocurrency wallet address",
            "Refuses in-app customer support ticketing verification"
        ],
        "actions": [
            "Log in to your cryptocurrency exchange account exclusively by typing the official URL directly in your browser",
            "Contact exchange customer support solely through the verified in-app help center",
            "Report compliance phishing emails to security@coinbase.com or security@binance.com"
        ],
        "icon": "🪙"
    },
    {
        "name": "Deceased Relative Estate Probate Bank Account Wire Trap",
        "year": 2024,
        "is_latest": False,
        "country": "UK",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 92,
        "desc": "Letter from fake probate solicitor in London claiming an estranged wealthy relative with your identical surname died intestate leaving £4.8M in Barclays Bank, asking for £3,000 legal fee to release inheritance.",
        "sample": "Chancery Chambers London: Following the untimely passing of Sir Arthur [Your Surname], we have identified you as the surviving next-of-kin to his £4,800,000 estate. Pay £2,850 probate administration fee to file claim.",
        "source": "Action Fraud",
        "kaise": "1. Scammers scrape phone directories to match common surnames with probate legal notices.\n2. Mail formal letters with impressive legal terminology and fake Law Society stamps.\n3. Request sequential administrative fees for probate filing, inheritance tax bonds, and overseas wire release.",
        "flags": [
            "You have never heard of or met the wealthy relative mentioned in the letter",
            "Solicitor asks for payment of legal fees to a private overseas bank account or via money transfer",
            "Solicitor uses a free webmail address or newly registered domain not listed on the Solicitors Regulation Authority (SRA)",
            "Urges complete secrecy and demands you do not consult your personal family lawyer",
            "Offers to split the estate 50/50 between you and the law firm"
        ],
        "actions": [
            "Verify any UK solicitor's credentials on the official Solicitors Regulation Authority directory: sra.org.uk",
            "Legitimate estate probate fees are deducted from the estate assets, never paid out-of-pocket by beneficiaries in advance",
            "Report fraudulent inheritance letters to Action Fraud"
        ],
        "icon": "📜"
    },
    {
        "name": "Credit Card Skimming Gas Pump Overlay Trap",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 95,
        "desc": "Thieves install external Bluetooth overlay skimmers over outdoor gas station payment terminals, recording magnetic stripe data and PINs as drivers fuel up, creating counterfeit cards overnight.",
        "sample": "Driver swipes debit card at gas pump #4. Concealed overlay skimmer reads card track data; Bluetooth transmitter beams card details to criminal vehicle parked across street. $800 drained from checking account next day.",
        "source": "FTC",
        "kaise": "1. Gang opens pump dispenser cabinet with universal master key or snaps molded overlay over reader.\n2. Skimmer stores card data or broadcasts it via Bluetooth to fraudsters sitting in nearby parked car.\n3. Drains victim bank accounts via ATM withdrawals and gift card purchases at big-box retailers.",
        "flags": [
            "The card reader protruding from the pump looks loose, crooked, or different from adjacent fuel pumps",
            "Security seal tape across the pump cabinet door is broken, cut, or shows the word 'VOID'",
            "Card insertion slot feels unnaturally thick or requires excessive physical force to push card in",
            "Gas pump is located at the furthest perimeter edge away from the attendant window and security cameras",
            "Keypad feels thicker than standard metal keypad"
        ],
        "actions": [
            "Pay inside with the station cashier or use modern contactless tapping (Apple Pay / Google Pay) at the pump",
            "Choose fuel pumps closest to the cashier window, which are least likely to be tampered with",
            "Use credit cards rather than debit cards at fuel pumps to avoid direct exposure of checking account funds"
        ],
        "icon": "⛽"
    },
    {
        "name": "Fixed Deposit (FD) Premature Liquidation Phishing Trap",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 98,
        "desc": "Victim receives SMS that their Rs 10 Lakh Bank Fixed Deposit has been prematurely broken and credited to savings account. Moments later, caller guides victim to 'cancel the liquidation' by clicking a link that actually wires funds away.",
        "sample": "SBI Alert: Your Term Deposit #FD8921 for Rs 8,00,000 has been closed prematurely and credited to savings A/c. If unauthorized, click immediately to lock transaction: https://sbi-fd-secure.top",
        "source": "I4C India",
        "kaise": "1. Hackers access victim netbanking via past data breaches or malware.\n2. Liquidate legitimate fixed deposits into victim's own checking account, triggering genuine bank SMS alerts.\n3. Terrified victim clicks phishing link to 'cancel liquidation', providing OTP that authorizes transfer of the newly freed cash to scammer accounts.",
        "flags": [
            "SMS received regarding liquidation of fixed deposits that you never initiated",
            "Cancellation link destination is an unfamiliar third-party URL rather than official bank netbanking portal",
            "Incoming caller claims to be senior bank manager assisting with emergency fund recovery",
            "Page prompts for high-value transaction OTP while claiming it is an 'account freeze code'",
            "High emotional panic manipulated to prevent victim from calling local branch manager"
        ],
        "actions": [
            "Never click links inside SMS alerts regarding account transactions",
            "If fixed deposits were prematurely broken, immediately open your official mobile banking app and FREEZE all outward transactions / lock netbanking",
            "Visit your home bank branch immediately in person to have netbanking credentials reset by staff"
        ],
        "icon": "🏦"
    },
    {
        "name": "Fake Check Cashing Mystery Shopper Financial Scam",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 94,
        "desc": "Victim is hired as a 'Secret Mystery Shopper' evaluating Walmart and Western Union services, receiving a $2,800 cashier's check to deposit, keep $400 commission, and evaluate Western Union by wiring $2,400.",
        "sample": "Mystery Shopper Assignment: Welcome to Premier Consumer Research! Enclosed is your first evaluation assignment and $2,850 corporate check. Deposit check in your bank, keep $450 pay, and test Western Union by wiring $2,400 to evaluator address.",
        "source": "FTC",
        "kaise": "1. Sends official-looking employment packet with authentic-looking cashier's check.\n2. Instructs victim to deposit check; bank makes funds available within 24 hours under federal law.\n3. Victim wires real cash via Western Union; two weeks later, the counterfeit check bounces, leaving victim liable for the entire $2,850 deficit.",
        "flags": [
            "You are hired for a job without an interview or formal application process",
            "Employer sends you a check and instructs you to wire money back via Western Union, MoneyGram, or gift cards",
            "Checks arrive from an unrelated third-party corporate entity",
            "Company insists you complete the evaluation within 48 hours before the check has time to clear",
            "Legitimate mystery shopping companies NEVER require shoppers to wire money as part of an assignment"
        ],
        "actions": [
            "Tear up the check; legitimate mystery shopping agencies (MSPA members) never ask workers to wire funds",
            "Understand check clearing rules: funds showing 'available' does NOT mean the check has genuinely cleared",
            "Report fraudulent check cashing scams to the FTC and US Postal Inspection Service"
        ],
        "icon": "🕵️"
    },
    {
        "name": "Account Takeover (ATO) Multi-Factor Authentication Push Fatigue",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 97,
        "desc": "Attackers obtain bank password and trigger dozens of 2FA push notifications to the victim's phone at 3:00 AM ('MFA Fatigue'), then call pretending to be security support telling victim to press 'Approve' to stop the notification spam.",
        "sample": "Phone chimes with 40 consecutive bank 2FA login approval pop-ups at 3:30 AM. Phone rings: 'This is Bank Fraud Support. Your account is being attacked by Russian IP. Tap Approve on the next prompt to lock your account.'",
        "source": "FBI IC3",
        "kaise": "1. Attackers acquire corporate or banking password from dark web leaks.\n2. Script automated bot to bombard victim's mobile authentication app with continuous push approvals.\n3. Exhausted or confused victim either taps 'Approve' accidentally to stop the ringing or complies with social engineer caller.",
        "flags": [
            "Receiving dozens of unprompted 2FA login approval requests when you are not actively logging in",
            "Notifications occurring during unusual middle-of-the-night hours",
            "Incoming caller claims that pressing 'Approve' or sharing a 2FA prompt will lock or protect your account",
            "Banking app prompt displays login attempt from unfamiliar city, state, or foreign IP address",
            "Caller urges you to accept the prompt to stop the notification spamming"
        ],
        "actions": [
            "NEVER tap 'Approve' on two-factor authentication prompts you did not personally trigger",
            "Select 'Deny' or 'Report Fraud' directly within the authentication prompt",
            "Change your primary banking password immediately using an independent, secure device"
        ],
        "icon": "🔔"
    },
    {
        "name": "Fake Tax Deducted at Source (TDS) Refund Credit Scam",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 95,
        "desc": "SMS claiming excess TDS of Rs 18,450 deducted on your salary has been approved for instant credit into your bank account, linking to fake Income Tax e-Filing portal.",
        "sample": "Income Tax Dept: Excess TDS refund of Rs 18,450 for Assessment Year 2024-25 has been approved. Update your bank account details here to receive direct transfer: https://incometax-tds-refund.top",
        "source": "I4C India",
        "kaise": "1. Dispatched during corporate quarterly TDS filing windows.\n2. Phishing link clones national Income Tax e-Filing login portal.\n3. Captures PAN, netbanking password, debit card credentials, and OTP under pretense of refund processing.",
        "flags": [
            "Official Income Tax Department portal is incometax.gov.in (ends strictly in '.gov.in')",
            "Income tax refunds are processed automatically into pre-validated bank accounts without third-party links",
            "SMS sent from private 10-digit mobile number rather than registered government header (e.g. ITDEPT)",
            "Page prompts for debit card PIN and CVV to 'credit' refund amount",
            "Threatens that unclaimed TDS refund will lapse at the end of the month"
        ],
        "actions": [
            "Check tax refund status exclusively by logging into the official portal: incometax.gov.in",
            "Never click on refund links received via SMS or WhatsApp",
            "Forward fraudulent tax phishing communications to webmanager@incometax.gov.in"
        ],
        "icon": "🧾"
    },
    {
        "name": "De-Risking / Safe Holding Escrow Account Wire Fraud",
        "year": 2025,
        "is_latest": False,
        "country": "Australia",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 98,
        "desc": "Caller pretending to be from Commonwealth Bank or ANZ fraud operations tells customer that rogue bank employees are stealing funds, instructing them to transfer $65,000 to a 'Reserve Bank Safe Holding Facility'.",
        "sample": "This is Commonwealth Bank Fraud Operations. An internal data leak at our Sydney branch has compromised your accounts. To protect your home loan equity, transfer $45,000 to our Reserve Bank holding facility.",
        "source": "Scamwatch",
        "kaise": "1. Scammers spoof Australian major bank customer service phone numbers.\n2. Convince customer that banking systems are unsafe due to criminal internal staff.\n3. Guide customer through transferring high-value sums via PayID or Osko to money mule accounts.",
        "flags": [
            "Australian banks will NEVER ask customers to move money to another account to keep it safe",
            "Caller claims that bank branch staff cannot be trusted and tells customer to lie about transfer purpose",
            "High urgency requiring payment while remaining continuously on the telephone call",
            "Payment instructions use PayID or Osko transfer to personal individual account names",
            "Caller claims funds will be returned within 24 hours once security patch is installed"
        ],
        "actions": [
            "Hang up immediately; Australian banks NEVER utilize 'safe holding accounts'",
            "Wait several minutes or use another phone to call your bank's verified fraud number",
            "Report imposter bank calls to Scamwatch and the Australian Cyber Security Centre (cyber.gov.au)"
        ],
        "icon": "🦘"
    },
    {
        "name": "Credit Card Chargeback Dispute Processing Fee Trap",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 92,
        "desc": "Consumer disputes a charge online, then receives call from fake 'Mastercard Dispute Resolution Bureau' stating dispute is approved but requires a $75 administrative processing fee to release chargeback.",
        "sample": "Mastercard Chargeback Services: Your $850 fraud dispute with merchant has been resolved in your favor! To release the credit reversal to your card, pay the $75 mandatory dispute processing charge.",
        "source": "FTC",
        "kaise": "1. Scammers harvest consumer dispute complaints posted on public social media forums.\n2. Call consumer posing as payment card network dispute department.\n3. Demands payment of administrative processing fees before issuing refund credit.",
        "flags": [
            "Credit card networks (Visa, Mastercard, Amex) NEVER charge cardholders fees to process legitimate fraud disputes",
            "Federal Fair Credit Billing Act guarantees free investigation of disputed billing errors",
            "Caller demands fee payment via gift cards, wire transfer, or peer-to-peer apps",
            "Caller cannot confirm the original 16-digit card number on file",
            "Dispute department calls from a blocked or unverified telephone number"
        ],
        "actions": [
            "Cardholder dispute investigations are 100% free under federal consumer credit protection laws",
            "Manage all billing disputes exclusively through your issuing bank customer service portal",
            "Report fraudulent chargeback fee solicitations to the FTC"
        ],
        "icon": "💳"
    },
    {
        "name": "Merchant POS Terminal Fraudulent Return Credit Trap",
        "year": 2024,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 93,
        "desc": "Shady customer enters retail shop, creates distraction with accomplice while asking to return an item, grabs countertop credit card terminal, and processes a manual $2,500 refund to their own debit card.",
        "sample": "Accomplice spills hot coffee across retail checkout counter creating commotion. Second suspect accesses unattended countertop POS terminal, keys in manager refund override PIN 0000, and swipes debit card for $2,500 refund.",
        "source": "FBI IC3",
        "kaise": "1. Thieves target retail stores with countertop POS terminals facing customer side.\n2. Create deliberate physical distraction occupying all cashiers and staff.\n3. Use default factory supervisor passwords (0000, 1234) on terminal to execute manual refund transaction to stolen debit card.",
        "flags": [
            "Customer insists on handling or manipulating the merchant payment terminal directly",
            "Accomplice creates sudden loud physical disturbance, argument, or spill in checkout area",
            "Customer attempts to process high-value return without presenting original store receipt or merchandise",
            "Merchant terminal supervisor PIN has never been changed from default manufacturer factory setting",
            "Customer appears nervous and watches staff positions intently"
        ],
        "actions": [
            "Change all default merchant POS terminal supervisor and refund passwords immediately upon installation",
            "Keep payment terminal physically behind the counter or tethered out of customer reach",
            "Require dual-manager authorization for all electronic customer refunds exceeding $100"
        ],
        "icon": "💳"
    },
    {
        "name": "Fake Cheque Clearance Hold Advance Fee Trap",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 94,
        "desc": "Victim receives a high-value cheque of Rs 4,50,000 for consulting services. Bank branch manager imposter calls stating the outstation cheque is on hold and requires Rs 15,000 clearing house surcharge to pass.",
        "sample": "Sir, I am clearing officer from CTS Clearing House Mumbai. Cheque #491204 for Rs 4,50,000 deposited in your account is held in inter-bank clearing. Pay Rs 14,800 speed clearing tax to clear funds today.",
        "source": "I4C India",
        "kaise": "1. Scammer issues worthless or forged cheque for legitimate services rendered.\n2. Concurrently calls victim impersonating clearing house or RBI official.\n3. Extracts cash clearance fees before victim realizes the original paper cheque bounced due to insufficient funds.",
        "flags": [
            "Cheque Clearing Houses (CTS) do NOT contact individual payees directly demanding clearance fees",
            "Cheque clearing charges, if applicable, are deducted automatically from bank balances, never paid via UPI",
            "Caller claims cheque will be permanently cancelled unless clearance fee is paid within 2 hours",
            "Payment directed to private personal UPI handle",
            "Original drawer of cheque becomes unreachable by telephone"
        ],
        "actions": [
            "Never pay money to have an incoming cheque cleared or processed",
            "Wait for the standard statutory clearing cycle (1-2 business days) for funds to be formally credited",
            "Contact your home branch customer service desk to inspect true clearing status"
        ],
        "icon": "🏦"
    },
    {
        "name": "Unauthorized Auto-Debit Recurring Standing Mandate Fraud",
        "year": 2025,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 95,
        "desc": "Victim approves a Rs 1 test transaction on a gaming or loan website, which secretly registers an e-NACH auto-debit standing mandate deducting Rs 9,999 every month from their bank account automatically.",
        "sample": "Play Online Fantasy Cricket: Verify bank account with Rs 1 refundable deposit. Hidden in terms: Authorizes e-NACH recurring monthly mandate of Rs 8,500. Next month: Rs 8,500 automatically debited from salary.",
        "source": "I4C India",
        "kaise": "1. Rogue merchants trick user into completing netbanking or debit card verification for Rs 1.\n2. Authorization screen conceals registration of recurring e-NACH / UPI Autopay mandate.\n3. Merchant initiates recurring automated debits on monthly schedule without further customer notification.",
        "flags": [
            "Netbanking authentication screen mentions 'Mandate Registration' or 'Maximum Amount: Rs 10,000'",
            "SMS OTP mentions 'e-NACH Mandate Approval' rather than simple one-time payment",
            "Unfamiliar recurring monthly debits appearing on bank statement under merchant aggregator names",
            "Website does not provide customer dashboard to cancel or view active subscriptions",
            "Customer service ignores cancellation and refund requests"
        ],
        "actions": [
            "Always inspect bank authentication screens carefully: verify if you are approving a one-time charge or a recurring standing mandate",
            "Cancel unauthorized standing mandates directly in your bank mobile app under 'e-NACH / Mandate Management' or 'UPI Autopay'",
            "Notify your bank manager to place a stop-payment order on rogue merchant billing IDs"
        ],
        "icon": "🔄"
    },
    {
        "name": "Corporate Payroll Imposter Direct Deposit Change Scam",
        "year": 2025,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 96,
        "desc": "Scammer sends email to corporate HR/payroll department impersonating an executive or employee, requesting direct deposit salary instructions be switched to a new GreenDot prepaid card account.",
        "sample": "Hi Payroll, I recently switched banks and need to update my direct deposit information for this Friday's paycheck. Attached is my new voided check. Please update my routing and account number immediately.",
        "source": "FBI IC3",
        "kaise": "1. Attacker spoofs employee email address or uses lookalike executive domain.\n2. Requests direct deposit payroll change right before scheduled company pay cycle.\n3. Payroll processor updates records without verbal confirmation, routing thousands in salary to criminal prepaid account.",
        "flags": [
            "Employee requests direct deposit change via informal email rather than secure employee self-service portal",
            "Sender urges payroll staff to process change immediately to meet impending pay cycle deadline",
            "New bank account is with an online fintech or prepaid card provider (Chime, GreenDot, Netspend)",
            "Sender claims they are unavailable for phone or video confirmation due to medical leave or family travel",
            "Email sender address has subtle typographical difference from official company corporate directory"
        ],
        "actions": [
            "Mandate that all direct deposit changes be submitted through password-protected, 2FA employee self-service portals",
            "Require payroll staff to perform out-of-band verbal confirmation using employee's verified internal telephone number",
            "Report payroll diversion attacks immediately to company information security officer and FBI IC3"
        ],
        "icon": "💼"
    },
    {
        "name": "Debit Card Skimming at Drive-Through Fast Food Windows",
        "year": 2024,
        "is_latest": False,
        "country": "USA",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 93,
        "desc": "Dishonest drive-through cashier takes customer's physical debit card out of sight, swipes it through a handheld pocket magnetic card skimmer hidden under counter, cloning card for unauthorized retail sprees.",
        "sample": "Customer hands debit card to drive-through attendant for $8 hamburger order. Cashier walks card out of driver's view for 45 seconds, swiping through pocket skimmer. Counterfeit card used for $600 Best Buy purchase 2 hours later.",
        "source": "FTC",
        "kaise": "1. Rogue employee recruited by criminal carding syndicate for $20 per skimmed card.\n2. Uses palm-sized battery-powered magnetic reader concealed under counter or in apron pocket.\n3. Sells captured track data to fraud networks that encode counterfeit plastic cards.",
        "flags": [
            "Cashier walks your payment card out of physical eyesight or under the counter ledge",
            "Payment transaction takes abnormally long (more than 30 seconds) for a simple fast-food charge",
            "Cashier swipes card twice claiming the first swipe encountered terminal error",
            "Cashier appears nervous, fidgety, or turns back completely away from drive-through window",
            "Unauthorized retail charges begin appearing on card within hours of visiting the restaurant"
        ],
        "actions": [
            "Never allow service workers to take your physical payment card out of your line of sight",
            "Use mobile contactless payments (Apple Pay / Google Pay / Samsung Pay) which generate tokenized one-time virtual numbers",
            "Review bank checking account transactions daily and set up instant push alerts for all card expenditures"
        ],
        "icon": "🍔"
    },
    {
        "name": "Fake Loan Foreclosure Clearance Certificate Fee",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 94,
        "desc": "Borrower looking to close home or auto loan receives call from fake bank recovery agent offering 50% discount on final foreclosure balance, pocketing Rs 1,20,000 and issuing forged No-Objection Certificate.",
        "sample": "Dear customer, settle your outstanding ICICI auto loan of Rs 2,40,000 for a one-time settlement of only Rs 1,15,000 today! Pay on this official collection link to receive digital loan closure NOC certificate.",
        "source": "I4C India",
        "kaise": "1. Corrupt data brokers leak overdue borrower lists from collection agencies.\n2. Scammer contacts borrower offering lucrative one-time settlement discount.\n3. Takes payment via personal UPI, issues forged bank NOC PDF, while actual bank loan remains unpaid and accrues penalties.",
        "flags": [
            "Settlement payment demanded via private individual UPI ID or unverified payment link",
            "Unrealistic 50% - 70% debt waiver without formal written settlement letter from the bank branch",
            "Agent refuses to meet inside the bank branch or conduct formal paperwork across branch counters",
            "NOC certificate issued features incorrect bank branch IFSC codes and fake digital signatures",
            "Actual bank continues calling for loan installments weeks after alleged settlement"
        ],
        "actions": [
            "Execute loan settlements and foreclosures ONLY inside the physical bank branch with authorized bank officers",
            "Pay settlement amounts solely into your specific loan account number, never to individual agent accounts",
            "Demand original stamped No-Objection Certificate (NOC) and return of property documents directly from branch custody"
        ],
        "icon": "🚗"
    },
    {
        "name": "International Remittance Currency Exchange Lock Scam",
        "year": 2025,
        "is_latest": False,
        "country": "Global",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 95,
        "desc": "Expatriates sending money home (Dubai to India, UK to Pakistan) use informal online hawala exchange groups offering 5% higher exchange rates, transferring funds that are stolen immediately.",
        "sample": "Best AED to INR Exchange Rate: Get Rs 23.80 per Dirham (Bank rate is Rs 22.50)! Zero transfer fee, instant IMPS deposit into Indian bank account. WhatsApp money exchange desk: +971-50-XXXXXXX.",
        "source": "Interpol",
        "kaise": "1. Operates informal currency transfer groups on Facebook and WhatsApp targeting migrant workers.\n2. Offers exchange rates significantly higher than official banking central bank rates.\n3. Expatriate transfers local currency in UAE or UK; scammers send fake transfer screenshot to family back home and disappear.",
        "flags": [
            "Exchange rate offered is substantially higher than the official interbank market foreign exchange rate",
            "Informal operator has no registered money service business (MSB) or central bank financial license",
            "Transactions conducted entirely via WhatsApp messages and personal peer-to-peer transfers",
            "Operator claims to bypass standard statutory international tax reporting rules",
            "Sends fabricated payment receipts while beneficiary bank account shows zero incoming deposit"
        ],
        "actions": [
            "Remit international funds exclusively through licensed, regulated money transfer operators (Wise, Western Union, official banks)",
            "Informal hawala / hundi transfers are illegal under foreign exchange management regulations and carry zero consumer protection",
            "Report fraudulent remittance syndicates to local financial regulatory authorities"
        ],
        "icon": "💱"
    },
    {
        "name": "Fake Cheque Stop-Payment Cancellation Fee Trap",
        "year": 2024,
        "is_latest": False,
        "country": "India",
        "cat": "Banking",
        "cat_slug": "banking-financial",
        "cat_name": "Financial / Banking",
        "score": 93,
        "desc": "Customer loses chequebook and calls a fake bank customer care phone number found on Google. Scammer pretends to be branch officer, demanding Rs 1,500 'emergency stop-payment fee' paid via UPI.",
        "sample": "Customer searches 'Canara Bank customer care number' on Google and calls top ad result. Scammer answers: 'To place an urgent stop-payment on your lost cheque #89124, transfer Rs 1,500 stop fee to bank UPI id: canarabank-help@upi'.",
        "source": "I4C India",
        "kaise": "1. Scammers flood search engine ads with fake bank customer care phone numbers.\n2. Customer dials number in panic after losing physical chequebook or wallet.\n3. Scammer charges fake fee and tricks customer into revealing netbanking passwords.",
        "flags": [
            "Bank customer service number found on unverified third-party search engine results or blog posts",
            "Bank representative asks you to pay stop-payment fees via personal UPI handles",
            "Representative asks for your netbanking password, debit card PIN, or OTP to execute stop payment",
            "Stop-payment fees on legitimate bank accounts are deducted automatically from account balances",
            "Customer service representative uses an informal Gmail or personal WhatsApp account"
        ],
        "actions": [
            "Place stop-payment orders on cheques yourself securely inside your official bank mobile app under 'Cheque Services'",
            "Obtain genuine bank telephone helplines exclusively from your physical bank passbook or official website (e.g. sbi.co.in)",
            "Never transfer money via UPI to customer service executives on phone calls"
        ],
        "icon": "✍️"
    }
]

print(f"Cat8 loaded: {len(cat8)} scams")
