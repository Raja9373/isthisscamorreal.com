// Script to generate the comprehensive 300+ Scampedia World Scam Database
const fs = require('fs');

const categoriesMeta = [
  { id: "investment-crypto", name: "Investment & Crypto Scams", icon: "🪙", countGoal: 42 },
  { id: "job-employment", name: "Job & Employment Scams", icon: "💼", countGoal: 32 },
  { id: "phishing-link", name: "Phishing / Message / Link Scams", icon: "📩", countGoal: 38 },
  { id: "call-impersonation", name: "Call & Impersonation Scams", icon: "📞", countGoal: 32 },
  { id: "romance-sextortion", name: "Romance & Sextortion Scams", icon: "💔", countGoal: 22 },
  { id: "shopping-store", name: "Shopping & Online Store Scams", icon: "🛒", countGoal: 32 },
  { id: "govt-lottery", name: "Govt & Lottery Scams", icon: "🏛️", countGoal: 27 },
  { id: "financial-banking", name: "Financial & Banking Scams", icon: "💳", countGoal: 32 },
  { id: "ransomware-tech", name: "Ransomware / Malware / Tech Scams", icon: "💻", countGoal: 22 },
  { id: "classic-tricks", name: "Classic / Confidence Tricks (Wikipedia)", icon: "🎩", countGoal: 25 },
];

console.log("Generating database...");
