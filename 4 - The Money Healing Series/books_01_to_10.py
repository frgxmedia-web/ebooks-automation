import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generate_ebook import generate_ebook

OUT = os.path.dirname(__file__)
ACCENT = "#F7B731"
BG = "#FFFDF0"
SERIES = "The Money Healing Series"

DISCLAIMER = """This book is intended for educational and informational purposes only. The content does not constitute financial, investment, legal, or professional advice of any kind. The author and publisher are not licensed financial advisors or therapists.

Nothing in this book should be interpreted as personalized financial guidance. Always consult a qualified financial professional before making decisions about your money, investments, or financial situation.

Results mentioned are illustrative only. Individual circumstances vary significantly. The publisher assumes no liability for actions taken based on information in this book."""

# ── Book 1 ────────────────────────────────────────────────────────────────────
b1 = {
    "title": "The Scarcity Mindset Fix",
    "subtitle": "Rewire Your Relationship with Money from the Inside Out",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {
            "title": "Why Your Brain Treats Money Like a Threat",
            "intro": "Scarcity isn't just a bank balance — it's a mental operating system. And like any system, it can be updated.",
            "sections": [
                {"heading": "The Neuroscience of Not Enough", "body": [
                    "When researchers at Princeton scanned the brains of people thinking about financial problems, something striking happened: the same neural pathways lit up as those associated with physical pain. Your brain does not distinguish well between a broken bone and a broken budget. Both read as danger.",
                    "This matters because it explains something most financial advice completely ignores — why knowing what to do and actually doing it are two entirely different things. You can read every budgeting book ever written, understand compound interest, know that you should save 20% — and still find yourself at a drive-through at 11pm buying things you don't need with money you don't have.",
                    "That's not weakness. That's a nervous system doing its job.",
                ]},
                {"heading": "Where Scarcity Gets Installed", "body": [
                    "Most money beliefs are formed before age seven. Not from explicit lessons — kids rarely sit through financial literacy lectures — but from the emotional texture of what they observed. Overheard arguments about bills. A parent's face when the car broke down. The way 'we can't afford that' was said, not just the words themselves.",
                    "Those early impressions encode as survival rules. And survival rules don't respond to logic. They respond to repetition, safety, and new evidence gathered over time.",
                    "Before you can change your financial behavior, you have to understand what your nervous system thinks money means.",
                ]},
            ],
            "callout": "You can't budget your way out of a belief system."
        },
        {
            "title": "Mapping Your Money Story",
            "intro": "Every financial pattern you have today has a origin point. Finding it doesn't excuse the pattern — it explains it, which is the first step to changing it.",
            "sections": [
                {"heading": "The Five Core Money Wounds", "body": [
                    "Through years of work in financial therapy and behavioral economics, researchers have identified five recurring patterns that show up across cultures and income levels. Most people carry at least two.",
                    "• The Hoarder: Safety feels like accumulation. Spending — even on necessities — triggers anxiety. The bank balance is emotional armor.",
                    "• The Avoider: Looking at accounts, opening statements, checking balances — all feel threatening. Avoidance is a protective mechanism.",
                    "• The Overspender: Money is comfort. Spending soothes emotional discomfort in the short term. The relief is real, the consequences are delayed.",
                    "• The Under-earner: Staying small with money feels safer than having more. More money means more visibility, more judgment, more responsibility.",
                    "• The Giver: Money flows out to others before self-needs are met. Generosity is genuine but also a way to feel worthy or avoid conflict.",
                    "None of these are character flaws. All of them are adaptations that once made sense.",
                ]},
                {"heading": "Writing Your Financial Autobiography", "body": [
                    "Get a notebook — not your phone, a physical notebook — and answer these without editing yourself:",
                    "What is your earliest memory that involved money? What feeling did it carry?",
                    "What did your parents believe about money? Did they say it out loud or did you just absorb it?",
                    "What is the most financially ashamed you have ever felt?",
                    "What does being truly financially secure look like to you — and does any part of you feel like you don't deserve it?",
                    "These aren't rhetorical. They are diagnostic. Your answers will reveal which wounds are most active in your current life.",
                ]},
            ],
            "callout": "The story you carry about money is not the truth. It's just the first story you were told."
        },
        {
            "title": "Breaking the Shame Loop",
            "intro": "Financial shame is one of the most corrosive forces in personal finance — and almost no one talks about it.",
            "sections": [
                {"heading": "How Shame Makes Things Worse", "body": [
                    "Shame operates in a cruel loop. You feel bad about your financial situation. Feeling bad makes it harder to look at the situation clearly. Not looking at it clearly makes it harder to improve. Not improving deepens the shame.",
                    "Research by Brené Brown and others shows that shame shrinks our cognitive bandwidth — literally making us worse at problem-solving, planning, and follow-through. You cannot think your way out of debt when shame is flooding the circuits you need to think with.",
                    "The path out is not self-discipline. It's self-compassion followed by self-honesty. In that order.",
                ]},
                {"heading": "The Audit Without Judgment Practice", "body": [
                    "Set a timer for 20 minutes. Open every account. Write down every balance — checking, savings, debt, credit cards, everything. Do not editorialize. No 'I can't believe I let this happen.' Just numbers on a page.",
                    "Then close everything and write: 'This is where I am. Not where I will always be.'",
                    "Do this once a week for four weeks. The goal isn't to fix anything yet. The goal is to build tolerance for looking. Most financial transformation starts with the simple act of being willing to see.",
                ]},
            ],
            "callout": "Shame is not a motivator. It's a paralytic."
        },
        {
            "title": "Rewiring the Automatic Responses",
            "intro": "Between stimulus and response, there is a gap. Building that gap around money decisions is the entire game.",
            "sections": [
                {"heading": "The 24-Hour Rule and Why It Works", "body": [
                    "Impulse purchases — and impulsive financial decisions in general — almost always feel urgent. The urgency is almost always manufactured, either by a sale timer or by your own emotional state seeking relief.",
                    "The 24-hour rule is simple: for any non-essential purchase over a threshold you set (start with $30), wait 24 hours. Not to deprive yourself, but to let the emotional charge dissipate and let your actual judgment run the decision.",
                    "After 24 hours, if you still want the thing and can genuinely afford it, buy it without guilt. What you'll find is that 60-70% of the time, the urgency vanishes. The item stops feeling necessary. The emotional need that drove the impulse has been met some other way — or just dissolved.",
                ]},
                {"heading": "Building a Spending Pause Practice", "body": [
                    "Before opening a shopping app or clicking 'add to cart,' pause for 60 seconds. Ask: what am I actually feeling right now? Bored? Anxious? Tired? Lonely?",
                    "Name the feeling out loud or in writing. Then ask: what does this feeling actually need? Sometimes the answer is the purchase. More often it's water, a walk, a conversation, or sleep.",
                    "This isn't about never buying anything. It's about making conscious choices instead of automatic ones. Consciousness, not deprivation, is the goal.",
                ]},
            ],
            "callout": "Every automatic behavior was once a conscious choice. Consciousness is how you get it back."
        },
        {
            "title": "Building Abundance Habits on a Real Budget",
            "intro": "Abundance isn't a number in your account. It's a relationship with what you have.",
            "sections": [
                {"heading": "The Percentage System", "body": [
                    "Forget rigid budget categories for now. Start with one simple rule: whatever comes in, five percent goes to a separate account immediately. Not later. Immediately, via automatic transfer on payday.",
                    "Five percent feels insignificant. That's the point. It needs to feel easy enough that you actually do it, and consistent enough that it becomes identity-level behavior. You are someone who saves. Even when the amount is small.",
                    "After three months of not touching it, increase to seven percent. Then ten. The amount is secondary to the habit.",
                ]},
                {"heading": "Tracking as a Form of Respect", "body": [
                    "Every dollar you track is a dollar you respect. Most people who feel broke are spending money they have no memory of spending — on subscriptions they forgot, on convenience they don't notice, on small purchases that feel negligible individually but add up to several hundred dollars monthly.",
                    "Track every outflow for 30 days. Not to judge it. To see it. Awareness is the precursor to choice, and choice is the precursor to change.",
                    "At the end of 30 days, you'll have a clear picture of what your money actually values — and whether that matches what you say you value.",
                ]},
            ],
            "callout": "Abundance begins with noticing what you already have."
        },
        {
            "title": "Rebuilding Trust with Yourself Around Money",
            "intro": "Financial recovery is, at its core, a trust rebuilding project — and you are both parties in the negotiation.",
            "sections": [
                {"heading": "Small Promises, Kept", "body": [
                    "The fastest way to rebuild financial self-trust is to make micro-commitments and keep them. Not a 12-week transformation plan. A single commitment this week.",
                    "Maybe it's: I will transfer $10 to savings on Friday. I will check my account balance every morning before opening social media. I will wait 24 hours before one purchase this week.",
                    "Keep it. Then make another one next week. This is how trust is rebuilt after it's been broken — not through dramatic gestures, but through boring, consistent follow-through on small things.",
                ]},
                {"heading": "Celebrating the Unsexy Wins", "body": [
                    "Our culture celebrates financial milestones — the first $10k saved, the debt paid off, the raise. But the real wins happen in the invisible moments: the impulse you didn't act on, the conversation you had about money that you used to avoid, the account you checked even though it scared you.",
                    "Write those down. Acknowledge them. The nervous system responds to positive reinforcement, and most of us are starving our new financial behaviors of the recognition they need to stick.",
                    "You are not trying to become a different person. You are trying to help the person you already are relate to money differently. That deserves acknowledgment.",
                ]},
            ],
            "callout": "You don't fix your relationship with money. You build a new one."
        },
    ]
}

# ── Book 2 ────────────────────────────────────────────────────────────────────
b2 = {
    "title": "Debt Without Shame",
    "subtitle": "A Practical and Emotional Guide to Getting Out and Staying Out",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "The Weight of What You Owe", "intro": "Debt is not a moral failing. It's a math problem with an emotional wrapper.", "sections": [
            {"heading": "Separating the Number from the Story", "body": ["The balance on your credit card is a number. The story you've built around that number — about what it says about you, your worth, your intelligence, your future — is a separate thing entirely, and it's doing far more damage than the interest rate.", "Shame about debt is nearly universal, and nearly universally counterproductive. People who feel deep shame about debt are statistically less likely to open statements, make a plan, or seek help. The very emotion designed to motivate action produces paralysis instead.", "The first step in getting out of debt is making it impersonal. It's not a verdict. It's a situation."]},
            {"heading": "A Complete Inventory", "body": ["List every debt: creditor, balance, interest rate, minimum payment. Everything. Then add it up.", "Most people estimate their total debt wrong — usually low. The act of seeing the actual number is uncomfortable, but it is also a relief. The unknown is always scarier than the known. Once you know, you can plan.", "Tape this list somewhere you can see it. Not as punishment — as orientation. You need to know where you are before you can navigate anywhere else."]},
        ], "callout": "Debt is a problem to solve, not a sentence to serve."},
        {"title": "Avalanche, Snowball, or Hybrid", "intro": "There is no universally correct debt payoff strategy. There's the one you'll actually stick to.", "sections": [
            {"heading": "The Math vs. The Psychology", "body": ["The debt avalanche method — paying minimums on everything and throwing extra money at the highest interest rate — is mathematically optimal. You pay less interest overall. Finance textbooks love it.", "The debt snowball method — paying off the smallest balance first regardless of rate — is psychologically effective. Early wins build momentum. Behavioral economists love it.", "Neither method works if you abandon it. The best strategy is the one that keeps you engaged. For high-earners with strong analytical brains, avalanche often wins. For people who need wins to stay motivated, snowball works better. Honest self-knowledge here saves money long-term."]},
            {"heading": "The Hybrid Approach", "body": ["Start with one small debt to build momentum (snowball). Then switch to the highest interest rate (avalanche). This gives you a psychological win upfront while optimizing mathematically for the larger balances.", "Combine this with a visual tracker — a hand-drawn chart, a printed spreadsheet, a debt-payoff app. Visual progress activates the reward circuitry in ways that spreadsheet math alone doesn't.", "Review progress monthly, not weekly. Weekly can feel discouraging. Monthly shows meaningful movement."]},
        ], "callout": "Progress you can see is progress you'll continue."},
        {"title": "Negotiating With Creditors", "intro": "Most people don't know they can negotiate their debt. Most creditors don't advertise that they prefer it.", "sections": [
            {"heading": "Hardship Programs and Interest Reductions", "body": ["Nearly every major credit card company has a hardship program. These programs temporarily reduce interest rates, waive fees, and lower minimum payments for people experiencing genuine financial difficulty. They are rarely advertised.", "The process: call the number on the back of your card. Ask to speak with the hardship or financial assistance department. Briefly explain your situation. Ask specifically: 'Can you lower my interest rate or enroll me in a hardship program?'", "You may be told no. Call back. Ask a different representative. Persistence yields disproportionate results in creditor negotiations."]},
            {"heading": "Settlements and Collections", "body": ["If an account has gone to collections, you have more negotiating power than you think. Collection agencies purchase debts for cents on the dollar and can settle for significantly less than the full balance while still turning a profit.", "Always get any settlement agreement in writing before making a payment. Never give collectors access to your checking account. Request a pay-for-delete agreement in writing — many collectors will remove the account from your credit report entirely in exchange for payment.", "Consult a nonprofit credit counselor (NFCC member agencies offer free or low-cost help) before making major decisions about collections or settlements."]},
        ], "callout": "Creditors negotiate every day. You just need to ask."},
        {"title": "Preventing the Relapse", "intro": "Getting out of debt is one achievement. Staying out is a different skill set.", "sections": [
            {"heading": "Understanding Your Debt Triggers", "body": ["Debt doesn't usually accumulate through grand disasters — it accumulates through repeated small emotional responses. Boredom. Stress. Social pressure. The need to appear okay when you're not.", "Map your personal triggers. When do you spend emotionally? What circumstances precede impulse purchases or charges you later regret? Knowing your pattern is the only way to interrupt it.", "Build specific if/then plans: 'If I feel the urge to online shop after 9pm, I will open a book instead.' The specificity is what makes these plans work. Vague intentions dissolve under emotional pressure."]},
            {"heading": "Building a Cash Buffer", "body": ["Most debt cycles begin with an emergency that has no cushion. The car breaks down, there's no savings, the credit card fills the gap. Then the balance sits there accruing interest, and the minimum payment prevents real saving, making the next emergency equally dangerous.", "The priority after debt payoff is a starter emergency fund — $1,000 minimum, ideally one month of expenses. Not in a checking account. In a separate savings account with no debit card attached.", "This buffer is not glamorous. It won't make you rich. But it will break the cycle."]},
        ], "callout": "The goal isn't just zero balance. It's zero return trips."},
        {"title": "Rebuilding Credit With Intention", "intro": "Credit is a tool. Like any tool, understanding how it works means you use it — it doesn't use you.", "sections": [
            {"heading": "How the Score Actually Works", "body": ["Your FICO score is calculated from five factors: payment history (35%), amounts owed (30%), length of credit history (15%), new credit inquiries (10%), and credit mix (10%).", "The single most impactful thing you can do is pay on time, every time. Even a single 30-day late payment can drop a score by 80-100 points and stays on your report for seven years.", "The second most impactful: keep your credit utilization — the percentage of your available credit you're using — below 30%. Below 10% is ideal. This is why paying down balances improves scores even if you haven't changed your behavior."]},
            {"heading": "Secured Cards and Credit-Builder Loans", "body": ["If your credit is severely damaged or nonexistent, secured credit cards and credit-builder loans are the standard rebuild tools.", "A secured card requires a cash deposit that becomes your credit limit. Use it for one recurring bill. Pay it in full every month. After 12-18 months of on-time payments, many issuers will upgrade you to an unsecured card and return your deposit.", "Credit-builder loans, offered by many credit unions and community banks, work in reverse — you pay first, receive the money after. Both instruments build payment history efficiently."]},
        ], "callout": "Credit is not the enemy. Misunderstanding it is."},
        {"title": "Creating a Debt-Free Identity", "intro": "The last step in financial recovery is deciding who you are now — not just what your balance shows.", "sections": [
            {"heading": "Values-Based Spending", "body": ["Once debt is gone and credit is rebuilding, the real work begins: figuring out what you actually value and building your financial life around that. This is harder than it sounds, because most of us have never done it consciously.", "List ten things that genuinely matter to you — experiences, relationships, creative pursuits, health, security. Then look at your last three months of spending. Is the money going toward the list? Or is it going toward things that didn't even make the list?", "The gap between stated values and spending patterns is where most financial dissatisfaction lives. Closing that gap is the whole project."]},
            {"heading": "The Annual Financial Review", "body": ["Once a year, set aside two hours to review your full financial picture: what you earned, what you spent, what you saved, what your net worth is, and whether you're moving toward the life you said you wanted.", "This isn't a guilt exercise. It's a calibration. Life changes. Priorities shift. Your financial plan should reflect the person you're becoming, not the one who made the plan three years ago.", "You've done the hard part. Now you're building on top of solid ground."]},
        ], "callout": "Your past debt does not define your future wealth."},
    ]
}

# ── Book 3 ────────────────────────────────────────────────────────────────────
b3 = {
    "title": "First-Generation Wealth",
    "subtitle": "Building Generational Money When No One Taught You How",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Starting From Scratch — and That's Okay", "intro": "Not having a financial blueprint handed to you is a disadvantage. It's also, strangely, a freedom.", "sections": [
            {"heading": "What First-Gen Actually Means", "body": ["Being first-generation with wealth doesn't necessarily mean your family was poor — it means no one showed you the mechanics. It means money was either avoided as a topic, treated as shameful, or handled in ways that worked for one generation's circumstances but not yours.", "You may have grown up in a household that was comfortable but cash-based — no investment accounts, no estate planning, no conversations about retirement beyond 'we'll figure it out.' Or one where money was genuinely scarce and survival was the only mode.", "Either way: you are building without a template. That's harder. It also means you get to build it right."]},
            {"heading": "The Knowledge Gap vs. The Access Gap", "body": ["Two different things hold first-generation wealth builders back: not knowing what to do, and not having access to the systems that make it possible.", "The knowledge gap is closeable fast. The information exists — in books, in free online resources, in communities. The harder gap is access: not having parents to co-sign loans, no family home to borrow against, no informal network of people who know how the game is played.", "This book focuses on both. Knowing is only half of it."]},
        ], "callout": "You're not behind. You're just starting without a head start."},
        {"title": "The Basics Nobody Taught You", "intro": "A quick, judgment-free introduction to the financial fundamentals that wealthy families pass down at the dinner table.", "sections": [
            {"heading": "Compound Interest — Both Directions", "body": ["Compound interest is the force that makes debt crushing and savings remarkable. On debt: you pay interest on your balance, and if you don't pay it off, you next pay interest on the interest. A $5,000 credit card balance at 24% APR, making only minimum payments, takes over 20 years to pay off and costs more than $12,000 total.", "On savings and investments: the same force works in your favor. $10,000 invested at 7% annual return (the historical stock market average, roughly) becomes $76,000 in 30 years without you adding another dollar. Add $200/month and it becomes $270,000.", "The lesson isn't complexity. It's time. Time is the ingredient wealthy families give their children by starting early. You start now."]},
            {"heading": "Net Worth and Why It Matters More Than Income", "body": ["Net worth is what you own minus what you owe. Assets minus liabilities. It's the most honest measure of financial health, and it's almost never discussed in households where building wealth is not the norm.", "High income with high spending and no savings produces zero net worth. Modest income with consistent investing produces real wealth over time. The difference between earning a lot and having a lot is entirely a function of what you keep.", "Track your net worth quarterly using a simple spreadsheet. Watching it grow — even slowly — is more motivating than tracking income."]},
        ], "callout": "Income is what you earn. Wealth is what you keep and grow."},
        {"title": "Investing Without Fear", "intro": "The stock market feels intimidating from the outside. Once you understand the basic mechanics, it becomes a very boring, very effective machine.", "sections": [
            {"heading": "Index Funds: The Unsexy Winner", "body": ["Index funds are baskets of stocks that track a market index — the S&P 500, for example, which represents the 500 largest US companies. When you buy an index fund, you own a tiny piece of all of them.", "The case for index funds is overwhelming and backed by decades of research: they outperform the vast majority of actively managed funds over 15-year periods, charge the lowest fees, require no expertise to use, and can be bought through any brokerage in minutes.", "Vanguard, Fidelity, and Schwab all offer index funds with expense ratios under 0.05%. Start with a total market or S&P 500 index fund and add to it consistently. That's the strategy."]},
            {"heading": "Retirement Accounts First", "body": ["If your employer offers a 401(k) with a match, contribute at least enough to get the full match. This is free money with a guaranteed 50-100% instant return. Nothing else in finance offers this.", "Then open a Roth IRA — you contribute after-tax dollars, the money grows tax-free, and withdrawals in retirement are tax-free. In 2024, you can contribute up to $7,000 per year if you're under 50.", "These accounts exist specifically to help people build wealth. Use them first, before taxable investment accounts."]},
        ], "callout": "You don't need to understand the market. You need to be in it."},
        {"title": "Homeownership — The Reality Check", "intro": "Buying a home is often called the cornerstone of wealth-building. The truth is more nuanced.", "sections": [
            {"heading": "When It Builds Wealth and When It Doesn't", "body": ["A home builds wealth when you stay in it long enough for appreciation and principal paydown to outpace transaction costs (typically 5-7 years minimum), in a market with healthy demand, bought at a price you can genuinely afford.", "A home destroys wealth when it's overleveraged, bought at the peak of a local market, in an area with declining population, or when the total housing cost — mortgage, taxes, insurance, maintenance — exceeds 30% of gross income.", "Rent is not throwing money away. Renting in a flexible life phase, while investing the difference, often outperforms buying financially. Make the decision with numbers, not cultural pressure."]},
            {"heading": "The Path to a First Mortgage Without Family Help", "body": ["Down payment assistance programs exist in most states — for first-time buyers, for certain income levels, for specific neighborhoods. HUD.gov maintains a searchable directory. Many people who assume they can't afford to buy haven't checked these programs.", "FHA loans require 3.5% down with a credit score above 580. Conventional loans with PMI require as little as 3% down. Neither requires a family gift.", "Build the credit score first (see Book 2), save the down payment consistently, and get pre-approved before looking at houses so you negotiate from a position of real readiness."]},
        ], "callout": "Ownership is a tool, not a mandate."},
        {"title": "Protecting What You Build", "intro": "Wealth without protection is fragile. This is the chapter wealthy families always discuss and most others never do.", "sections": [
            {"heading": "Insurance as a Wealth Tool", "body": ["Health insurance prevents medical debt from erasing savings. Term life insurance ensures your family isn't financially devastated if you die early. Disability insurance — often overlooked — replaces income if illness or injury prevents you from working, which is statistically far more likely than early death.", "Renters insurance costs less than $20/month and covers your belongings plus liability. If you own a car, adequate liability coverage protects against a single accident destroying your financial progress.", "Insurance is not exciting. It is the floor that keeps a bad year from becoming a decade of financial recovery."]},
            {"heading": "Basic Estate Planning", "body": ["A will is not just for the wealthy. If you have children, assets, or opinions about what happens to your money when you die, you need a will. Dying without one (intestate) means the state decides — which often isn't what you'd have chosen.", "A healthcare directive and durable power of attorney are equally important and take one afternoon to set up through a local estate attorney or legal service. These documents ensure that someone you trust makes decisions if you're incapacitated.", "Free resources exist through your state's legal aid office. LegalZoom and similar services offer basic documents affordably. Get it done."]},
        ], "callout": "Building wealth and protecting it are the same job."},
        {"title": "Breaking the Cycle, Starting the Legacy", "intro": "The most powerful thing about building first-generation wealth is what it makes possible for the people after you.", "sections": [
            {"heading": "Teaching Your Children Without Overwhelming Them", "body": ["You don't have to become a finance expert to raise financially literate children. You just have to be one level ahead and honest about it.", "Talk about money openly. Explain what things cost. Let children make small spending decisions and experience the results. Give them a savings goal to work toward. Frame money as a tool for choice and security, not as something shameful or mysterious.", "The children of parents who talk openly about money make measurably better financial decisions as adults, even when those parents don't have much money. The conversation matters more than the balance."]},
            {"heading": "Your Own North Star", "body": ["Define what financial freedom means to you — specifically. Not a vague 'I want to be rich.' What number, what lifestyle, what level of security, what options for your time?", "Then calculate backwards. How much do you need invested to generate that income passively? How many years at your current savings rate does that take? What would it take to cut that time in half?", "You started without a blueprint. You're building one now — not just for yourself, but for everyone who comes after you. That's a different kind of wealth than any number in an account."]},
        ], "callout": "You are not just building wealth. You are changing what your family's future looks like."},
    ]
}

# ── Book 4 ────────────────────────────────────────────────────────────────────
b4 = {
    "title": "The Emotional Spender",
    "subtitle": "Understanding and Changing the Habits That Keep You Broke",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Spending as a Coping Mechanism", "intro": "Nobody buys a $200 candle because they need light. They buy it because something else isn't working.", "sections": [
            {"heading": "The Loop You Don't See", "body": ["Emotional spending follows a predictable loop: uncomfortable feeling → urge to relieve it → purchase → brief relief → return of discomfort (often worse) → repeat. The loop is invisible until you slow it down enough to see the individual frames.", "Stress, loneliness, boredom, social comparison, anxiety, and genuine sadness are the most common triggers. Not weakness — just unaddressed emotional needs seeking the fastest available relief. And in a society built around purchasing, shopping is always available."]},
        ], "callout": "The purchase isn't the problem. It's the answer to a question worth asking."},
        {"title": "Identifying Your Spending Moods", "intro": "Self-knowledge is cheaper than therapy and more actionable than willpower.", "sections": [
            {"heading": "The Spending Journal", "body": ["For 30 days, log every purchase with the emotional state that preceded it. Not the justification — the actual feeling. Tired. Stressed. Bored. Excited. Sad. Resentful.", "At the end of the month, patterns emerge. Most emotional spenders have two or three specific emotional states that do the majority of the damage.", "Once you know your triggers, you can build specific alternatives. Not 'be more disciplined' — specific competing responses to specific emotional triggers."]},
        ], "callout": "You can't fight a pattern you haven't identified."},
        {"title": "Building Your Alternative Menu", "intro": "Willpower is a finite resource. Alternative responses are a renewable one.", "sections": [
            {"heading": "The Replacement Strategy", "body": ["For each identified trigger, create a list of three alternative responses that genuinely address the underlying need. Not punishments — actual alternatives that provide relief.", "Bored at 9pm and reaching for the shopping app: alternatives might be a 20-minute walk, texting a friend, or starting a creative project. Stressed after work: alternatives might be a bath, a workout, or cooking an elaborate meal.", "The alternatives won't feel as immediately satisfying as shopping at first. That's tolerance building. After 4-6 weeks of consistent redirection, the new responses begin to feel natural."]},
        ], "callout": "You're not stopping a behavior. You're replacing it."},
        {"title": "The Social Media Trap", "intro": "Comparison is the oldest driver of unnecessary spending. Social media has supercharged it.", "sections": [
            {"heading": "Curating Your Financial Environment", "body": ["Your feed is a spending environment, not a neutral information stream. Every aspirational image, every haul video, every 'link in bio' is a spending prompt carefully engineered by people who profit from your impulse.", "Unfollow accounts that consistently trigger desire for things you don't need. Follow accounts that celebrate simplicity, financial independence, creativity. This isn't about becoming a minimalist — it's about controlling what seeds your desire loop.", "Audit your subscriptions, your notification settings, and the apps on your phone's home screen. What you see first shapes what you want first."]},
        ], "callout": "Your feed is your financial environment. Design it on purpose."},
        {"title": "Creating Spending That Satisfies", "intro": "The goal is never spending nothing. It's spending on things that actually fill you.", "sections": [
            {"heading": "Experience vs. Object", "body": ["Decades of happiness research converge on a consistent finding: experiences provide more lasting satisfaction than objects, even when objects cost more. The new thing depreciates quickly; the memory of a trip, a concert, a meal with people you love, appreciates over time.", "This doesn't mean never buy things. It means build your discretionary spending toward experiences and consumables that are genuinely enjoyed, not toward accumulation that needs to be stored, insured, and eventually discarded.", "Deliberate spending on things that genuinely matter to you is the opposite of emotional spending — and it feels completely different."]},
        ], "callout": "Spend less on what you want and more on what you love."},
        {"title": "The Long Game", "intro": "Financial change is not a sprint. It's a practice with compound returns.", "sections": [
            {"heading": "Progress Over Perfection", "body": ["You will have bad weeks. You will make impulsive purchases even after months of progress. This is normal, and it does not undo your work.", "The metric that matters isn't perfection — it's the trend. Are you spending more intentionally this month than last? Are your emotional triggers getting slightly smaller? Is the gap between impulse and action growing?", "Those improvements compound. The version of you that exists in three years of this practice is almost unrecognizably different from where you started. Not because you became a different person — because you understood yourself better."]},
        ], "callout": "Consistency beats intensity every single time."},
    ]
}

# ── Book 5 ────────────────────────────────────────────────────────────────────
b5 = {
    "title": "Side Income Without Burnout",
    "subtitle": "Real Ways to Earn More Without Wrecking Your Life",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "The Honest Case for a Side Income", "intro": "A second income stream is not a hustle culture status symbol. It's a financial buffer with real-life consequences.", "sections": [
            {"heading": "Why One Income Is Fragile", "body": ["Single-income dependency is a structural risk most employed people don't think about until something breaks. A layoff, a medical emergency, a divorce — any of these can turn a 'comfortable' financial situation into crisis in weeks.", "A side income doesn't have to be large to matter. An extra $500/month is $6,000/year — that's an emergency fund built in a year, accelerated debt payoff, or the difference between affording and not affording an unexpected expense.", "The goal isn't a second career. It's resilience."]},
        ], "callout": "A side income is not about greed. It's about options."},
        {"title": "Finding Your Leverage Point", "intro": "The best side income uses what you already know or who you already are.", "sections": [
            {"heading": "Skills Inventory", "body": ["Make a list of everything you know how to do — professionally, recreationally, informally. Writing, design, spreadsheets, cooking, teaching, fixing things, organizing, researching, speaking, coaching, crafting. All of it.", "Then mark which ones other people pay for. Then mark which ones you enjoy enough to do for an extra 5-10 hours per week. The overlap between paid, doable, and tolerable is your leverage point.", "You don't need a unique skill. You need to be reliably available and competent in something people already pay for."]},
        ], "callout": "You already have more leverage than you think."},
        {"title": "Service-Based Income: Fastest to Start", "intro": "Services pay immediately. Products take time. When you need money, start with services.", "sections": [
            {"heading": "What Works Now", "body": ["Freelance writing, virtual assistance, social media management, bookkeeping, tutoring, resume writing, transcription, graphic design, web design, translation — these are all services with active demand and low startup costs.", "Platforms like Upwork, Fiverr, and LinkedIn are functional starting points. Local Facebook groups, Nextdoor, and direct outreach to small businesses work even better for most people.", "First clients are almost always the hardest to get. The strategy: lower your rate slightly to earn reviews, then raise it once you have a track record."]},
        ], "callout": "Services are the fastest path from zero to paid."},
        {"title": "Passive Income — The Realistic Version", "intro": "Passive income is real. The 'wake up and check your earnings' version takes years to build and isn't free to create.", "sections": [
            {"heading": "What's Actually Passive (and What Isn't)", "body": ["True passive income requires a significant upfront investment of time, money, or both. A digital product — a course, a template pack, a pattern, an ebook — takes substantial creation time before generating any income.", "The realistic version: build one modest digital product in a niche you know, list it on a platform with existing traffic (Etsy, Gumroad, Teachers Pay Teachers, Udemy), and accept that it will earn modestly for months before it earns meaningfully.", "One product earning $300/month is more valuable than ten products earning nothing — and it funds the development of the next one."]},
        ], "callout": "Passive income starts passive-ish and becomes passive over time."},
        {"title": "Managing the Second Income Without Burning Out", "intro": "The side income that destroys your health isn't an asset. It's just a different kind of debt.", "sections": [
            {"heading": "The 10-Hour Rule", "body": ["Set a firm ceiling on side income hours per week — 10 hours is a sustainable baseline for most people with full-time jobs or significant family responsibilities. More is possible in short bursts, but not as a default.", "Protect your sleep above all else. Cognitive performance, emotional regulation, and actual productivity all degrade significantly under sleep deprivation — meaning you work more hours for less output and worse decisions.", "The side income that fits sustainably into your life is more valuable in the long run than the one that earns more for six months and then collapses you."]},
        ], "callout": "The income that lasts is the one that works within your life."},
        {"title": "Taxes, Structure, and Not Getting Surprised", "intro": "Side income is real income, and the IRS is aware of this.", "sections": [
            {"heading": "Self-Employment Tax Basics", "body": ["Side income is subject to self-employment tax (15.3% on net earnings) on top of regular income tax. Many first-time earners are shocked by this. Planning for it isn't complicated — set aside 25-30% of gross side income in a separate account until tax time.", "If you expect to owe more than $1,000 in taxes for the year, the IRS requires quarterly estimated tax payments (typically April 15, June 15, September 15, January 15).", "Deductible business expenses — software, equipment, home office percentage, professional development — reduce your taxable self-employment income. Keep records. Consult a tax professional once your side income is meaningful."]},
        ], "callout": "Plan for taxes in advance. The surprise is worse than the amount."},
    ]
}

# ── Book 6 ────────────────────────────────────────────────────────────────────
b6 = {
    "title": "Money and Mental Health",
    "subtitle": "The Hidden Link Between Your Finances and Your Wellbeing",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "The Financial Stress Spiral", "intro": "Financial stress doesn't just feel bad. It measurably impairs the cognitive functions you need to fix it.", "sections": [
            {"heading": "What Stress Does to Financial Decisions", "body": ["The landmark research by Sendhil Mullainathan and Eldar Shafir, published in their book Scarcity, demonstrated something that feels intuitive once you hear it but has profound implications: financial stress consumes cognitive bandwidth. When your mind is preoccupied with how to pay a bill, that preoccupation actively reduces your IQ-equivalent performance on other tasks.", "This creates a trap. Financial stress degrades your decision-making precisely when good decisions are most important. The person who most needs to think clearly about money is the person least equipped to do so.", "Understanding this is not an excuse — it's a design principle. Systems that work even under stress are more valuable than perfect plans that require your best self."]},
        ], "callout": "Financial stress is not a character failure. It's a cognitive tax."},
        {"title": "Depression, Anxiety, and the Bank Account", "intro": "Mental health and financial health move together. Treating them separately is inefficient.", "sections": [
            {"heading": "When Mental Health Drives Financial Behavior", "body": ["Depression frequently manifests financially as avoidance: not opening mail, not checking accounts, not making calls, letting bills slide not from negligence but from an inability to generate the energy or hope required to act.", "Anxiety frequently manifests as hypervigilance or paralysis: obsessive checking of accounts, inability to spend even on necessities, or conversely, compulsive spending as a tension-relief mechanism.", "ADHD — covered more fully in another series — affects financial behavior through impulsivity, difficulty with future planning, and executive function challenges that make budgeting mechanically harder.", "None of these are moral failures. All of them have practical workarounds."]},
        ], "callout": "Your mental health is a financial variable. Account for it."},
        {"title": "Automating Around Your Worst Days", "intro": "Build your financial systems for your Tuesday-at-10pm self, not your best Saturday morning self.", "sections": [
            {"heading": "The Power of Automation", "body": ["Automatic transfers, automatic savings, automatic bill payments — these are not just conveniences. For people with mental health challenges, they are essential infrastructure.", "Every decision you automate is a decision your depressed or anxious self cannot sabotage. The money moves before you can talk yourself out of it, spend it on something else, or simply forget.", "Set up: automatic transfer to savings on payday, automatic minimum payments on all debt (to prevent late fees even during hard months), automatic contributions to retirement accounts. Then build from there."]},
        ], "callout": "Automation is compassion for your future self."},
        {"title": "Financial Therapy — What It Is and When to Seek It", "intro": "Therapy for money feels indulgent to many people. The cost of not getting it is usually much higher.", "sections": [
            {"heading": "The Financial Therapist's Role", "body": ["Financial therapy sits at the intersection of emotional counseling and financial planning. A financial therapist helps you understand the emotional roots of your financial behaviors — not just what to do with money, but why you do what you already do.", "It is different from a financial planner, who focuses on strategy and products. And it's different from a general therapist, who may not have specific training in money psychology.", "The Financial Therapy Association (financialtherapy.org) maintains a directory. Many therapists offer sliding scale fees. Some financial coaches incorporate therapeutic techniques without charging therapy rates."]},
        ], "callout": "Understanding the why changes what you do with the what."},
        {"title": "Finding Stability in Uncertainty", "intro": "Financial certainty is rare. Financial resilience is learnable.", "sections": [
            {"heading": "The Minimum Viable Financial Safety Net", "body": ["In a period of mental health challenge, the goal isn't optimization. It's stability. Stability means: housing is covered, utilities are on, food is available, debt isn't actively growing, something small is being saved.", "This is enough. When you're in a hard season, maintaining stability is a genuine achievement — not a consolation prize.", "The more ambitious goals exist. They can wait. Stability first, then growth."]},
        ], "callout": "Stability is not the floor. It's the foundation."},
        {"title": "Building a Financial Safety Team", "intro": "Money problems that feel private are often better solved with help.", "sections": [
            {"heading": "Who Should Be on Your Team", "body": ["Nonprofit credit counselors (NFCC members) offer free financial counseling and debt management plans. They are not trying to sell you anything.", "Community organizations, credit unions, and many employers offer free financial wellness programs that most people never access.", "A trusted friend or family member who will look at your finances with you — not to judge but to witness — can make the invisible visible in ways that solo review cannot.", "You don't have to figure this out alone. That belief is part of what keeps the spiral spinning."]},
        ], "callout": "Financial health is a team sport masquerading as a solo one."},
    ]
}

# ── Book 7 ────────────────────────────────────────────────────────────────────
b7 = {
    "title": "Negotiating Your Worth",
    "subtitle": "How to Ask for More — and Actually Get It",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Why Most People Underearn", "intro": "The wage gap between what most people earn and what they could earn is not a skill gap. It's a negotiation gap.", "sections": [
            {"heading": "The Research on Asking", "body": ["A Carnegie Mellon study found that people who consistently negotiate their salary earn $1 million more over a 45-year career than those who don't. That's not a rounding error. That's a retirement.", "And yet most people don't negotiate. Fear of rejection. Fear of seeming greedy. Fear of the offer being rescinded. Fear that the number they want is somehow unreasonable.", "None of these fears are grounded in typical reality. Most employers expect negotiation. Many actually lose respect for candidates who don't negotiate — interpreting it as low self-confidence or lack of market awareness."]},
        ], "callout": "Not asking is the most expensive thing most people do."},
        {"title": "Knowing Your Number", "intro": "You cannot negotiate well without research. Research takes 45 minutes and changes everything.", "sections": [
            {"heading": "Salary Research Tools", "body": ["Glassdoor, Levels.fyi (for tech), LinkedIn Salary, Payscale, and the Bureau of Labor Statistics Occupational Outlook Handbook all provide salary data by role, location, experience level, and industry.", "Use at least three sources. Build a range: the floor (below which you won't accept), the target (what you actually want), and the stretch (what the role is worth at the high end of the market).", "Factor in your specific experience, certifications, location premium or discount, industry sector, and company size. A marketing manager at a 20-person startup is paid differently than one at a Fortune 500. Research comparables, not averages."]},
        ], "callout": "Data is confidence. Confidence is negotiating power."},
        {"title": "The Negotiation Conversation", "intro": "Most negotiation advice focuses on tactics. The most important thing is tone.", "sections": [
            {"heading": "Collaborative, Not Combative", "body": ["The most effective salary negotiations feel like conversations between aligned parties, not adversarial standoffs. Your framing: 'I'm very excited about this role and I want to make this work. Based on my research and experience, I was expecting something closer to [number]. Is there flexibility there?'", "Notice what this does: it expresses genuine enthusiasm (you're not bluffing), anchors to a researched number (not a feeling), and opens a dialogue (it's a question, not a demand).", "Let silence do work. After stating your number, stop talking. The discomfort of silence is a powerful force, and most people fill it by negotiating against themselves."]},
        ], "callout": "The negotiator who speaks next often loses."},
        {"title": "Negotiating Beyond Salary", "intro": "Compensation is a package. Most people negotiate one item and leave the rest on the table.", "sections": [
            {"heading": "The Full Compensation Menu", "body": ["When salary has reached its ceiling, the negotiation can continue: remote work flexibility, additional vacation days, professional development budget, signing bonus, early performance review, title adjustment, equity or profit-sharing, flexible start date.", "A signing bonus is often easier for companies to grant than a salary increase because it's a one-time cost that doesn't compound. Ask for it specifically if salary is immovable.", "Remote work has a financial value — two fewer commuting days per week can save $3,000-$8,000 annually in transportation, lunches, and childcare costs. Factor this into total compensation comparisons."]},
        ], "callout": "If the salary won't move, everything else is still negotiable."},
        {"title": "Asking for a Raise", "intro": "The raise conversation is the negotiation most people avoid longest. It is also the most straightforward.", "sections": [
            {"heading": "Building the Business Case", "body": ["A raise request is a business case, not a personal appeal. 'I need more money' is weak. 'Here is the specific value I've created and here is the market rate for this contribution' is strong.", "Document your wins: revenue generated, costs reduced, projects delivered, problems solved, teams led. Put dollar amounts where possible. Then research the market rate for your role as it has evolved (not as it was when you were hired).", "Request a formal meeting — not a hallway conversation. Come with a one-page summary. Ask for a specific number. Then be quiet."]},
        ], "callout": "A raise request is a presentation, not a prayer."},
        {"title": "Walking Away and What That Makes Possible", "intro": "The most powerful negotiating position is genuine willingness to leave.", "sections": [
            {"heading": "Building Your Walk-Away Power", "body": ["Walk-away power is not about being cavalier about your job. It's about maintaining enough financial stability and professional optionality that staying isn't compelled by desperation.", "This means: an emergency fund that buys you time, skills that translate across employers, a maintained professional network, and occasional interviews even when you're not looking. Not disloyalty — preparation.", "People who genuinely can walk away often don't have to. The confidence that comes from real options changes how you show up in every negotiation, every performance review, and every interaction with leadership."]},
        ], "callout": "Financial security is negotiating power. Build it before you need it."},
    ]
}

# ── Book 8 ────────────────────────────────────────────────────────────────────
b8 = {
    "title": "The Minimalist Budget",
    "subtitle": "Spend Less, Stress Less, and Still Have a Life",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Why Most Budgets Fail", "intro": "A budget that makes you miserable doesn't fail because you're undisciplined. It fails because it was designed wrong.", "sections": [
            {"heading": "The Deprivation Model Problem", "body": ["Traditional budgeting treats every spending category as a target to hit exactly and every overage as a failure. This creates a cycle of guilt, restriction, rebellion, and shame that most people can't sustain for more than a few weeks.", "The minimalist budget works differently: instead of tracking every category, you identify your non-negotiable joys, protect them, and reduce friction everywhere else.", "You're not cutting until it hurts. You're cutting until you can't tell the difference — and leaving the things you'd genuinely miss completely intact."]},
        ], "callout": "A budget should free you, not cage you."},
        {"title": "The Reverse Budget", "intro": "Pay yourself first, spend the rest freely. It sounds too simple to work. It works.", "sections": [
            {"heading": "How It Works", "body": ["On payday, immediately transfer your savings target to a separate account. Immediately pay your fixed bills (rent, utilities, debt minimums). Whatever remains is yours to spend freely, without tracking, until the next payday.", "This works because the important money is moved before discretionary spending can reach it. You're not relying on willpower to save — you're saving first and spending what's left.", "Start with 10% savings if your budget allows. If it doesn't, start with $50. The habit is more important than the amount."]},
        ], "callout": "Pay yourself first and stop counting the rest."},
        {"title": "Finding the Fat Without the Pain", "intro": "Most households have $300-$700/month of spending they genuinely wouldn't miss. Finding it is the whole game.", "sections": [
            {"heading": "The Subscription Audit", "body": ["List every recurring charge: streaming services, subscriptions, app purchases, memberships, SaaS tools, automatic renewals. Most households have between 12 and 18 of these, and most people can't name more than six.", "Cancel everything you haven't used in 30 days. Pause anything you use occasionally but not regularly. Keep only what you'd notice being gone.", "The average household saves $150-$300/month doing this audit once. It takes 90 minutes. Do it now."]},
        ], "callout": "The money you're wasting is in the subscriptions you forgot about."},
        {"title": "Food: The Biggest Variable", "intro": "Food spending is the most controllable major expense and the most emotionally loaded.", "sections": [
            {"heading": "The Middle Path", "body": ["Extreme food budgeting — rice and beans every night, never eating out — is sustainable for almost no one. It also misses the point. Food is pleasure, culture, connection, and sustenance. Eliminating joy from eating to save money is a bad trade.", "The middle path: cook the majority of your meals at home, eat out intentionally rather than habitually, and apply the 24-hour rule to food delivery (most late-night delivery orders are boredom, not hunger).", "Meal prep one day per week eliminates the 6pm 'I don't know what to make and I'm exhausted' decision that drives the majority of unnecessary food spending."]},
        ], "callout": "Eat out for joy. Not for convenience."},
        {"title": "Housing and Transportation: The Big Levers", "intro": "These two categories represent 50-70% of most people's budgets. Small changes here dwarf everything else.", "sections": [
            {"heading": "The Housing Calculation", "body": ["The standard guideline is to spend no more than 30% of gross income on housing. Many people in high cost-of-living areas exceed this significantly, which constrains every other financial goal.", "If housing exceeds 35% of your income, it's worth evaluating: roommate options, geographic flexibility, proximity-versus-cost tradeoffs, and the full costs of homeownership versus renting in your specific market.", "Housing decisions are the highest-leverage financial decisions most people make. They deserve more than a weekend of thought."]},
        ], "callout": "Where you live is a financial decision before it's a lifestyle one."},
        {"title": "Building a Life You Don't Need to Escape From", "intro": "The best financial plan is one that funds a life you actually want.", "sections": [
            {"heading": "Aligning Money and Meaning", "body": ["The minimalist budget is not about having less. It's about being intentional about what you spend on — and eliminating the rest to free up money and mental space for what actually matters to you.", "Write down the 10 things that bring you the most genuine satisfaction. Look at where your money goes. Build a budget that funds the list. Cut what isn't on it.", "This is not asceticism. It's clarity. And clarity about what you value is the foundation of a financial plan that you'll actually keep."]},
        ], "callout": "Spend more on what you love. Spend nothing on what you don't."},
    ]
}

# ── Book 9 ────────────────────────────────────────────────────────────────────
b9 = {
    "title": "Investing for People Who Don't Trust the Market",
    "subtitle": "A Skeptic's Guide to Building Wealth Anyway",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Why Skepticism About Investing Is Rational", "intro": "The financial industry has given people plenty of reasons not to trust it. Your skepticism is not uninformed.", "sections": [
            {"heading": "What the Industry Gets Wrong", "body": ["Actively managed funds, on average, underperform their benchmark index after fees. The financial industry knows this. The mutual fund industry exists anyway because fees are very profitable.", "Market crashes are real. 2000, 2008, 2020 — portfolios lose 30-50% in a bad cycle. For people who lived through these, the idea that 'just stay invested' is easy advice is understandably infuriating.", "Your skepticism about flashy stock picks, day trading, crypto speculation, and miracle returns is well-founded. But those are not the same as broad, boring, low-cost index investing."]},
        ], "callout": "Skepticism about bad investing is wisdom. Skepticism about all investing is expensive."},
        {"title": "The Only Strategy That Has Consistently Worked", "intro": "Boring has outperformed exciting for 100 years.", "sections": [
            {"heading": "The Index Fund Case", "body": ["If you had invested $10,000 in an S&P 500 index fund in 1994 and never touched it, you would have approximately $240,000 by 2024 — through multiple crashes, recessions, wars, pandemics, and political crises.", "The strategy: buy a low-cost total market or S&P 500 index fund. Add money consistently. Never sell based on market conditions. Wait 20-30 years.", "This is not exciting. It does not require skill. It does not require following the market. The research supporting it is extensive and bipartisan. It is the most well-documented wealth-building strategy in history for ordinary investors."]},
        ], "callout": "Boring investments build real wealth. Exciting ones mostly build financial media revenue."},
        {"title": "Getting Started With Real Money", "intro": "The gap between understanding investing and doing it is almost entirely emotional.", "sections": [
            {"heading": "Opening an Account in 20 Minutes", "body": ["Fidelity, Vanguard, and Charles Schwab all offer commission-free accounts you can open online in under 20 minutes. You do not need a minimum balance to open a Fidelity or Schwab account.", "Once open: transfer a small amount — $100, $500, whatever you can actually afford. Buy one index fund. VOO (Vanguard S&P 500 ETF), FSKAX (Fidelity Total Market), or SCHB (Schwab US Broad Market) are good starting points with expense ratios under 0.05%.", "You don't need to understand everything. You need to own something. The learning comes from having skin in the game."]},
        ], "callout": "You learn investing by doing it with real money, not by preparing indefinitely."},
        {"title": "Managing Fear During Downturns", "intro": "The only way to lose money in an index fund long-term is to sell when it's down.", "sections": [
            {"heading": "Why Staying Invested Is Hard", "body": ["The psychological experience of watching your portfolio drop 30% is genuinely painful. Research shows that financial losses activate the same pain centers as physical harm, and that losses feel approximately twice as bad as equivalent gains feel good.", "This asymmetry is why people sell low. Not because they're foolish — because the emotional experience of loss is overwhelming.", "The preparation for downturns happens before they occur: understand that they are normal (the market has declined 20%+ twelve times since 1950 and recovered every time), have an emergency fund so you don't need to sell during bad markets, and automate contributions so the habit continues regardless of your emotional state."]},
        ], "callout": "The investor who stays invested wins. Not the one who times the market."},
        {"title": "What to Do With $1,000, $10,000, $100,000", "intro": "The right move at different balances is slightly different — but simpler than most people think.", "sections": [
            {"heading": "Each Threshold", "body": ["$1,000: Open a Roth IRA. Buy one index fund. Set a $50/month automatic contribution. Do not touch it.", "$10,000: Max your Roth IRA contribution for the year ($7,000 in 2024 if under 50). Put the remainder in a taxable brokerage account in the same index fund.", "$100,000: Max 401(k) if available (up to $23,000 in 2024). Max Roth IRA. Remaining in taxable brokerage in a three-fund portfolio (total US market, international index, bond index). Consider speaking with a fee-only fiduciary financial advisor.", "At every level: low cost, diversified, automated, long-term."]},
        ], "callout": "Simplicity compounds just as reliably as complexity — with less risk."},
        {"title": "The Long Game With Eyes Open", "intro": "Investing for the long term doesn't require optimism. It requires patience and a basic understanding of history.", "sections": [
            {"heading": "What You're Actually Betting On", "body": ["Broad market investing is not a bet that any particular company will succeed. It's a bet that human productivity and economic activity will continue — that the collective output of millions of businesses will be larger in 30 years than today.", "This has been true through every war, recession, pandemic, and political crisis in recorded economic history. It may not always be true. But the alternatives — keeping everything in cash, which inflation erodes reliably — carry their own risks.", "You're not betting on a perfect future. You're betting on a functional one."]},
        ], "callout": "Investing isn't optimism. It's a reasonable bet on human resilience."},
    ]
}

# ── Book 10 ───────────────────────────────────────────────────────────────────
b10 = {
    "title": "Couples and Money",
    "subtitle": "How to Stop Fighting About Finances and Start Building Together",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER,
    "chapters": [
        {"title": "Why Money Is the Last Taboo in Relationships", "intro": "Most couples talk about sex before they talk about debt. That's a design problem.", "sections": [
            {"heading": "What Financial Conflict Is Really About", "body": ["Research from the American Psychological Association consistently finds money to be the number-one source of conflict in relationships — above parenting, intimacy, household responsibilities, and in-laws.", "But the conflict is rarely actually about money. It's about values, security, control, trust, and deeply held beliefs about what money means. Two people with similar incomes and identical balance sheets can fight bitterly about money because they grew up with completely different emotional relationships to it.", "The path forward is not a shared spreadsheet. It's a shared vocabulary."]},
        ], "callout": "Money fights are values fights with a dollar sign on top."},
        {"title": "Understanding Your Partner's Money Story", "intro": "Before you can align financially, you need to understand where the other person is coming from.", "sections": [
            {"heading": "The Money Date", "body": ["Schedule a 90-minute conversation — away from distractions, not right before bed, not when either of you is stressed — specifically to share your financial histories.", "Each person answers: What did money mean in your family growing up? What is your most significant financial memory? What does financial security feel like to you? What does financial anxiety feel like?", "The goal is not agreement. It's understanding. Knowing that your partner hoards money because they experienced genuine childhood scarcity changes how you interpret their resistance to spending. Knowing that you spend emotionally helps your partner interpret your behavior accurately instead of personally."]},
        ], "callout": "Financial intimacy starts with financial honesty."},
        {"title": "Building a System That Fits Both of You", "intro": "There is no universally correct way for couples to structure money. There is only the system you both actually use.", "sections": [
            {"heading": "The Three Models", "body": ["Fully combined: all income goes into joint accounts, all spending comes from joint accounts. Works best for couples with similar spending habits and high mutual trust. Requires consistent communication.", "Fully separate: each person maintains their own accounts, expenses are split by a predetermined formula. Works best when income is similar and independence is a core value. Requires discipline about shared financial goals.", "Hybrid: joint account for household expenses, individual accounts for personal spending. Each person contributes proportionally to the joint account; personal spending is fully autonomous. Works for most couples because it preserves individual freedom while handling shared obligations.", "The right system is the one you'll both actually follow."]},
        ], "callout": "The best financial system for couples is the one both people trust."},
        {"title": "When Income Is Unequal", "intro": "Income inequality within couples creates power dynamics that most financial advice ignores entirely.", "sections": [
            {"heading": "The Proportional Contribution Principle", "body": ["When one partner earns significantly more than the other, a 50/50 expense split creates financial strain for the lower earner that frequently breeds resentment. A proportional system — each partner contributes the same percentage of income to shared expenses — creates equity without equalizing income.", "Example: Partner A earns $80,000, Partner B earns $40,000. Shared expenses are $4,000/month. Each contributes 33% of take-home pay. Partner A contributes more dollars; both contribute equally relative to means.", "This requires both partners to agree that contribution is measured in proportion, not absolute amount — which is a values conversation, not a math conversation."]},
        ], "callout": "Equal contribution isn't always the same as fair contribution."},
        {"title": "The Monthly Money Meeting", "intro": "Regular financial check-ins are the single most effective habit for financial alignment in couples.", "sections": [
            {"heading": "How to Do It Without Fighting", "body": ["Schedule 30-60 minutes monthly — same day, same time, treated as non-negotiable. Include: review of last month's spending, progress toward shared goals, any upcoming large expenses, and one financial goal to focus on next month.", "Ground rules: no blame language, no score-keeping, no bringing up past financial mistakes unless they're directly relevant to a current decision. The meeting is forward-looking.", "End every meeting with a shared goal you're both excited about — a trip, a home improvement, an early retirement number. Shared goals transform budgeting from restriction into teamwork."]},
        ], "callout": "A monthly money meeting prevents a thousand money arguments."},
        {"title": "Building Wealth Together", "intro": "Two incomes building toward shared goals is one of the most powerful wealth-building structures that exists.", "sections": [
            {"heading": "The Compound Power of Partnership", "body": ["Two people sharing housing costs, building shared savings, investing together toward shared goals, and making financial decisions in alignment have a structural advantage over single-income households that compounds over decades.", "The return on financial alignment in a partnership is real: lower housing cost per person, shared emergency fund burden, dual income resilience, and the social reinforcement of shared goals.", "None of this is automatic. It requires the conversations, the systems, and the ongoing practice of treating your financial life as a shared project with shared stakes — and acknowledging that you are both always learning."]},
        ], "callout": "The best investment you can make together is in the relationship itself."},
    ]
}

books = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10]
filenames = [
    "01 - The Scarcity Mindset Fix.pdf",
    "02 - Debt Without Shame.pdf",
    "03 - First-Generation Wealth.pdf",
    "04 - The Emotional Spender.pdf",
    "05 - Side Income Without Burnout.pdf",
    "06 - Money and Mental Health.pdf",
    "07 - Negotiating Your Worth.pdf",
    "08 - The Minimalist Budget.pdf",
    "09 - Investing for People Who Don't Trust the Market.pdf",
    "10 - Couples and Money.pdf",
]

for book, fname in zip(books, filenames):
    generate_ebook(os.path.join(OUT, fname), book)

print("SERIES 4 DONE")
