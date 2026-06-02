"""
Books 01–10 — The ADHD Blueprint Series
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generate_ebook import generate_ebook

BASE = os.path.dirname(__file__)
ACCENT = "#FF6B6B"
BG = "#FFF5F5"
SERIES = "The ADHD Blueprint Series"
DISCLAIMER = """This book is for educational and informational purposes only. It does not constitute medical or psychological advice and is not a substitute for professional diagnosis or treatment. ADHD is a neurodevelopmental condition that should be assessed and managed by qualified healthcare professionals.\n\nThe strategies described here are practical approaches that many people with ADHD find helpful. Individual results vary. If you believe you or someone you care for may have ADHD, please seek a comprehensive evaluation from a qualified clinician.\n\nThe author and publisher accept no liability for outcomes arising from use of this material."""

def mb(title, subtitle, chapters):
    return {"title": title, "subtitle": subtitle, "series_name": SERIES,
            "accent_hex": ACCENT, "bg_hex": BG, "disclaimer": DISCLAIMER, "chapters": chapters}

B01 = mb("The ADHD Entrepreneur", "Building a Business That Works With Your Brain", [
    {"title": "Why Entrepreneurship Attracts ADHD Brains",
     "intro": "There's a reason ADHD is overrepresented among entrepreneurs. Studies suggest that entrepreneurs are six times more likely to have ADHD than the general population. This isn't a coincidence — it's a match between the demands of entrepreneurship and the specific cognitive profile of the ADHD brain.",
     "sections": [
         {"heading": "The ADHD Advantages in Business", "body": [
             "The ADHD brain excels at exactly what entrepreneurship demands: pattern recognition across unrelated domains, hyperfocus on genuinely interesting problems, high tolerance for uncertainty and ambiguity, rapid generation of novel ideas, and an ability to take action without the paralysis of overthinking that stops many neurotypical people from starting at all.",
             "Richard Branson, Ingvar Kamprad (IKEA), David Neeleman (JetBlue), and Kinko's founder Paul Orfalea have all spoken publicly about their ADHD diagnoses and how the traits associated with it shaped their entrepreneurial approaches. This isn't a curated list of exceptions — it reflects a genuine statistical overrepresentation in the founder population.",
         ]},
         {"heading": "The ADHD Challenges in Business", "body": [
             "The same traits that drive entrepreneurial success also create specific business vulnerabilities. Boredom with execution after the exciting launch phase. Difficulty maintaining systems and processes that don't feel interesting. Impulsive decisions that bypass the due diligence that would have caught the problem. Starting multiple projects without completing existing ones. Managing the administrative, financial, and operational aspects of a business that require sustained attention to detail.",
             "These challenges don't disqualify ADHD entrepreneurs. But ignoring them is what transforms ADHD advantages into ADHD disasters. The entrepreneurs who do best with ADHD are those who understand their specific profile — both the strengths and the vulnerabilities — and build their business structure accordingly.",
         ]},
     ], "callout": "Build the business around your brain. Don't try to build a neurotypical business and then fit your brain into it."},
    {"title": "Structuring Your Business for ADHD",
     "intro": "Business structure is not just about legal entities and tax efficiency. For ADHD entrepreneurs, it's about creating the conditions in which your brain can actually perform.",
     "sections": [
         {"heading": "Delegation as a Business Model", "body": [
             "The single most important structural decision an ADHD entrepreneur makes is what to keep and what to delegate. The ADHD brain has a finite attention budget, and where it spends that budget determines everything. Keeping tasks that deplete the ADHD brain — detailed bookkeeping, repetitive administration, process management — while delegating everything else is a strategic choice, not a luxury.",
             "The practical question is not 'can I afford to delegate this?' but 'can I afford not to?' An ADHD entrepreneur spending four hours per week on bookkeeping they find excruciating is an entrepreneur not spending four hours per week on the high-value creative and relational work their brain is actually designed for.",
             "The order of delegation for most ADHD entrepreneurs: first, anything that involves sustained attention to detail on routine tasks (bookkeeping, data entry, administrative email). Second, anything that requires consistent follow-through on a fixed process (invoicing, scheduling, project management administration). These are not weaknesses to be ashamed of — they are the specific cognitive profile of a brain wired for novelty.",
         ]},
         {"heading": "Systems That Work Without Willpower", "body": [
             "Neurotypical business systems are designed on the assumption that the person using them has consistent, reliable executive function — the ability to remember to check the system, follow the process, and maintain the habit. ADHD executive function doesn't work this way. Systems for ADHD entrepreneurs need to be automatic, externally prompted, and tied to existing behaviour patterns.",
             "Effective ADHD-compatible systems have three properties: they are triggered by something external rather than relying on memory (calendar reminders, not mental notes); they are the default option rather than requiring extra effort to engage; and they have immediate feedback — you can see the result of using them right away.",
         ]},
         {"heading": "Time Blocking for ADHD Brains", "body": [
             "ADHD time blindness — the difficulty accurately perceiving and managing time — is one of the most practically impairing aspects of the condition in a business context. Missing deadlines, underestimating how long things take, being late to meetings, and losing track of hours inside a hyperfocus session are all manifestations of the same underlying neurological difference.",
             "Time blocking — assigning specific tasks to specific time slots on the calendar, rather than maintaining a to-do list — addresses time blindness by externalising the time structure. The calendar becomes the executive function that the ADHD brain's prefrontal cortex isn't reliably providing. Combined with visual timers (the Time Timer is widely recommended in the ADHD community) that make the passage of time visible, time blocking is one of the most effective single systems for ADHD entrepreneurs.",
         ]},
     ], "callout": "Your business should work with your neurology. Not against it, not despite it — with it."},
    {"title": "Managing Money with an ADHD Brain",
     "intro": "Money management is one of the most consistently challenging areas for ADHD entrepreneurs. Impulsivity, variable income management, and difficulty with the administrative detail of finances are a difficult combination.",
     "sections": [
         {"heading": "The Impulsivity-Finance Problem", "body": [
             "Impulsive spending in business — the shiny-object syndrome that leads to software subscriptions, new equipment, and premature pivots — is one of the most common financial patterns among ADHD entrepreneurs. The dopamine hit of a new tool or approach is real, and the ADHD brain is highly susceptible to it.",
             "The most effective structural protection against impulsive business spending is a waiting rule: any unbudgeted purchase above a set threshold (many ADHD coaches recommend $100–$500 depending on business size) requires a mandatory 48-hour wait before execution. The dopamine excitement of the impulse almost always fades within 48 hours if the purchase isn't genuinely necessary.",
         ]},
         {"heading": "Automating the Financial Architecture", "body": [
             "Every financial process that requires consistent manual action is a process that will eventually be missed by an ADHD brain. The solution is automation: automatic invoice sending, automatic payment reminders, automatic transfers to tax savings accounts, automatic payroll.",
             "The specific financial automation most important for ADHD entrepreneurs: setting up an automatic percentage-of-revenue transfer to a separate tax savings account on receipt of every payment. Tax season ADHD disasters — the unpaid tax bill that comes as a shocking surprise — are almost entirely preventable with this single automation.",
         ]},
     ], "callout": "Automate what you can't reliably remember. Delegate what you can't reliably do. Do the rest."},
    {"title": "Focus, Energy, and Deep Work",
     "intro": "The ADHD entrepreneur has access to hyperfocus — one of the most powerful cognitive states available to any human. The challenge is accessing it reliably rather than accidentally.",
     "sections": [
         {"heading": "Understanding Your Focus Windows", "body": [
             "Every ADHD brain has specific times of day when executive function is most available. For many people with ADHD, this is in the late morning — cortisol has risen sufficiently to support activation, but the day's cumulative demands haven't yet depleted executive function reserves. For others it's late at night. The specific window is individual.",
             "Identifying your focus window and protecting it — no meetings, no interruptions, no administrative tasks — is the highest-leverage scheduling decision an ADHD entrepreneur makes. An ADHD brain doing deep work in its peak window is a fundamentally different cognitive instrument than one doing the same work when executive function is depleted.",
         ]},
         {"heading": "Creating the Conditions for Hyperfocus", "body": [
             "Hyperfocus doesn't arrive on command, but it does respond to conditions. The conditions most reliably associated with hyperfocus for ADHD brains are: a task with clear challenge that's slightly above current ability, immediate feedback on performance, intrinsic interest in the subject matter, and an environment with appropriate sensory stimulation (which varies by individual — some need silence, many ADHD brains work better with background music or ambient noise).",
             "Working on the right things at the right time, in the right environment — this is the framework. It's not about trying harder. It's about stacking the conditions.",
         ]},
     ], "callout": "Hyperfocus is not a distraction. It's your superpower. Learn to summon it."},
    {"title": "Building a Sustainable ADHD Business",
     "intro": "Sustainability for an ADHD entrepreneur means building something that doesn't require constant heroic effort to keep moving.",
     "sections": [
         {"heading": "Knowing Your Limits", "body": [
             "The ADHD entrepreneur's most common growth mistake is expanding into areas that require the executive function skills they don't have, rather than areas that play to the skills they do. Building a team that complements ADHD strengths — detail-oriented operators, consistent follow-through people, process-minded administrators — is how sustainable ADHD businesses are built.",
             "This requires honest self-knowledge. The ADHD brain's tendency toward grandiosity and optimism is part of its entrepreneurial power and also its most dangerous blind spot. The assessment question is not 'can I imagine doing this?' but 'what is my actual track record with this type of task?'",
         ]},
         {"heading": "Managing Energy, Not Just Time", "body": [
             "ADHD burnout is a genuine and underrecognised phenomenon. The chronic effort of compensating for executive function differences, managing a dysregulated nervous system, and suppressing ADHD-related behaviours in professional contexts depletes energy in ways that aren't always visible. The ADHD entrepreneur who appears to be thriving externally is often running on empty internally.",
             "Managing energy means building in recovery: genuine downtime that doesn't involve screens or productivity, physical movement that regulates the nervous system, sleep that is protected rather than sacrificed to the work, and social connection with people who require no management or performance.",
         ]},
     ], "callout": "The most successful ADHD entrepreneurs are not those who overcome their ADHD. They are those who design around it."},
])

B02 = mb("ADHD for Freelancers", "How to Hit Deadlines, Keep Clients, and Stay Sane", [
    {"title": "Freelancing With an ADHD Brain",
     "intro": "Freelancing removes the external structure that neurotypical workplace environments provide — and that ADHD brains depend on more than most. No fixed hours, no supervisor, no accountability from colleagues, no natural transition between work and home. It is simultaneously one of the most ADHD-compatible and ADHD-challenging career paths available.",
     "sections": [
         {"heading": "Why Freelancing Suits ADHD", "body": [
             "The aspects of freelancing that suit ADHD are significant: variety across projects and clients, the interest-based motivation that comes from choosing work you find engaging, the absence of the neurotypical office social dynamics that can be exhausting to navigate, and the flexibility to work in alignment with natural energy rhythms rather than a fixed schedule.",
             "Many ADHD freelancers report that they do their best work in the freelance context precisely because the autonomy removes the constant friction of trying to conform to structures designed for different brains.",
         ]},
         {"heading": "The Specific Freelance ADHD Challenges", "body": [
             "The challenges are equally real. Deadlines without external enforcement are easy to miss. Client communication requiring consistent, timely responses depends on executive function that ADHD impairs. Invoicing and financial management require sustained attention to administrative detail. And the variable income of freelancing interacts badly with the ADHD tendency toward impulsive spending and poor financial planning.",
             "The framework for freelancing success with ADHD is not 'try harder' — it's 'build the external structures that compensate for the internal executive function gaps.' This chapter is about what those structures look like in practice.",
         ]},
     ], "callout": "Freelancing gives you freedom. The structure you build gives that freedom somewhere to go."},
    {"title": "Deadline Management Systems",
     "intro": "Missing deadlines destroys freelance careers. ADHD makes deadline management hard. The solution is systems, not willpower.",
     "sections": [
         {"heading": "The Project Breakdown Method", "body": [
             "The ADHD brain struggles to initiate large, vague tasks. 'Write article on X' is a vague task. 'Spend 20 minutes writing the opening paragraph of the article on X' is a specific, bounded task that ADHD brains can initiate more reliably. Breaking every project into the smallest possible specific actions — at the start of the project, when motivation is available — means that in the low-motivation periods, you always have a clearly defined next action rather than a paralysing blob of work.",
             "The rule: no project enters your system without being broken into at least three to five specific, timed actions. Each action should be completable in one to two hours. Each should have a due date assigned at breakdown time, working backward from the client deadline.",
         ]},
         {"heading": "The Two-Deadline System", "body": [
             "For every client deadline, create an internal deadline 48 hours earlier. This creates a buffer for the late starts, unexpected hyperfocus detours, and time estimation errors that are predictable features of ADHD work patterns. The 48-hour buffer is your insurance policy.",
             "Tell clients your internal deadline, not your actual deadline, if they ask for progress updates. Managing client expectations around the two-deadline system is about transparency without over-disclosure: 'I target completion by Thursday' when the actual deadline is Saturday is honest about your commitment without requiring an explanation of your cognitive architecture.",
         ]},
         {"heading": "Using Accountability Strategically", "body": [
             "Body doubling — working in the physical or virtual presence of another person — dramatically improves ADHD initiation and focus. For freelancers, virtual co-working sessions (via Zoom, FocusMate, or similar) provide the social regulatory input that normalises the work environment without requiring a physical shared space.",
             "Accountability partnerships with other freelancers — daily or weekly check-ins where you state your commitments and report back — add external accountability to self-set deadlines. The knowledge that someone will ask whether you completed the task is often sufficient to activate the ADHD nervous system when internal motivation isn't.",
         ]},
     ], "callout": "The deadline is not the problem. The absence of a system that makes you take the deadline seriously is."},
    {"title": "Client Communication and Relationships",
     "intro": "Client relationships require consistent, responsive communication. ADHD makes consistency and responsiveness hard. Here's the bridge.",
     "sections": [
         {"heading": "The Communication System", "body": [
             "Email is one of the most ADHD-hostile communication formats: it arrives unpredictably, demands context-switching, requires remembering to follow up, and provides no natural closure. Managing client email with ADHD requires a system that removes the memory burden.",
             "The inbox-zero approach — processing every email to a decision immediately rather than leaving it as a mental placeholder — reduces the cognitive load of an inbox full of unresolved items that the ADHD brain keeps trying to remember. Combine with a daily email window (two to three times per day, not continuously) to reduce the context-switching cost.",
         ]},
         {"heading": "Setting Client Expectations Proactively", "body": [
             "Many client relationship problems for ADHD freelancers arise from unmet expectations that were never clearly set. A brief onboarding document that explains your communication style, typical response times, and project management approach sets expectations before they become sources of friction.",
             "You don't need to disclose ADHD. You do need to be honest about how you work: 'I respond to emails within 24 hours on weekdays,' 'I send weekly progress updates on Fridays,' 'I prefer to schedule calls rather than respond to urgent requests by email.' These are professional communication norms, not ADHD accommodations.",
         ]},
     ], "callout": "Clients don't need you to work like they expect. They need you to deliver what you promised."},
    {"title": "The Freelance Money System",
     "intro": "Financial management is where many ADHD freelancers come unstuck. The fix is automation and simplification.",
     "sections": [
         {"heading": "The One-Bank-Account Mistake", "body": [
             "Mixing business income with personal spending in one account is a recipe for ADHD financial disaster. Without clear separation, it's impossible to know how much is available for business expenses, how much should be set aside for taxes, or what's actually profit versus revenue.",
             "The minimum viable financial structure: a business income account into which all client payments arrive; an automatic transfer of 25–30% of every payment into a tax account; and a weekly or monthly transfer of profit into personal spending. Everything is automatic. No manual transfers to forget.",
         ]},
         {"heading": "Invoicing on Time", "body": [
             "Delayed invoicing is a chronic ADHD freelancer problem. Invoice immediately upon project completion or at pre-agreed billing dates — using automation where possible. Most accounting software (FreshBooks, Wave, QuickBooks) can send automatic reminders for unpaid invoices, removing the need to remember to chase payment.",
             "The psychological barrier to invoicing is often perfectionism or anxiety about the money conversation. The practical solution: create a single invoice template, fill in the variables, send immediately. No review, no hesitation, no waiting until you feel ready.",
         ]},
     ], "callout": "Automate your money system once. Then forget about it and do the work."},
    {"title": "Protecting Your Mental Health as an ADHD Freelancer",
     "intro": "The isolation, uncertainty, and self-management demands of freelancing are hard on anyone. With ADHD, they're harder.",
     "sections": [
         {"heading": "The Rejection Sensitivity Trap", "body": [
             "Rejection sensitive dysphoria makes the normal rejections of freelance life — lost pitches, critical feedback, clients who don't renew — particularly painful. The ADHD freelancer who interprets every rejection as evidence of fundamental inadequacy will eventually stop pitching, stop asking for feedback, and stop taking the risks that keep a freelance career growing.",
             "The cognitive reframe that helps most: rejection in business is information, not verdict. A lost pitch tells you something about fit, timing, or positioning. It tells you nothing definitive about your worth or capacity. Building a practice of quickly extracting the information and discarding the personal interpretation is a skill that develops with practice.",
         ]},
         {"heading": "Building Your Support Structure", "body": [
             "Freelancing is structurally isolating. ADHD compounds the isolation by making social initiation harder when executive function is depleted. Deliberately building in social contact — a regular co-working arrangement, a freelancer community, regular calls with colleagues in adjacent fields — is not a nice-to-have. It's a nervous system regulation necessity.",
             "ADHD coaches who specialise in professional and business contexts are worth considering for ADHD freelancers who are struggling with the self-management demands. They provide the external accountability, strategic structure, and ADHD-specific knowledge that generic business coaching doesn't.",
         ]},
     ], "callout": "Freelancing is a solo career, not a solo nervous system. Build your support structure deliberately."},
])

B03 = mb("The ADHD Parent", "Raising Kids When You're Neurodivergent Too", [
    {"title": "Parenting With an ADHD Brain",
     "intro": "Parenting is one of the most executive-function-demanding experiences a human being undertakes. When you're doing it with an ADHD brain — one that struggles with the exact demands parenting makes most heavily: consistency, patience, routine maintenance, emotional regulation under pressure — the challenges are real and specific.",
     "sections": [
         {"heading": "The Particular Challenges", "body": [
             "ADHD parenting challenges tend to cluster around specific scenarios: the morning routine (a sequence of tasks requiring initiation, time management, and emotional regulation under time pressure — a perfect storm for ADHD executive function); transitions (getting children ready to leave, or switching from activity to activity — requiring the ADHD parent to manage their own transition difficulties while managing their child's); and emotional regulation during conflict (when the child's big feelings trigger the ADHD parent's own emotional reactivity).",
             "These are not failures of love or commitment. They are specific executive function demands interacting with specific executive function deficits. Naming them accurately is the first step toward addressing them without shame.",
         ]},
         {"heading": "The Guilt Trap", "body": [
             "ADHD parents carry significant guilt — about the times they lost patience, the activities they forgot, the inconsistency that confused their children, the moments they were present in body but absent in mind. This guilt is often disproportionate to actual harm caused, but it's real and it depletes the emotional resources needed for the next moment of parenting.",
             "Guilt that motivates change is useful. Guilt that produces rumination and shame is not. The distinction: 'I lost my temper at my child in a way that wasn't okay, and I need to repair that and work on my regulation' is useful. 'I am a bad parent' is not a thought that leads anywhere productive.",
         ]},
     ], "callout": "You are not a bad parent who happens to have ADHD. You are a good parent whose brain makes some parts of parenting harder."},
    {"title": "Building Structure That Works for Your Brain",
     "intro": "Consistency and routine are what children need. External structure is what ADHD brains need to provide them. These are compatible — if the structure is designed for ADHD.",
     "sections": [
         {"heading": "ADHD-Compatible Family Routines", "body": [
             "A routine that requires the ADHD parent to hold all the steps in working memory and initiate each one reliably will fail. A routine that is externalised — on a visible checklist on the fridge, in an app that sends reminders, with physical cues built into the environment — has a far better chance.",
             "The morning routine is where most ADHD family breakdowns happen. Design it the night before: lay out clothes, pack bags, prepare breakfast where possible. The morning's executive demands are pre-solved by the previous evening's lower-pressure planning. This is borrowed executive function — using a window of better function to set up the window of worse function.",
         ]},
         {"heading": "When You Have an ADHD Child Too", "body": [
             "ADHD is substantially heritable — estimates suggest 74–80% heritability. Many ADHD parents are raising ADHD children. The combination of two or more ADHD nervous systems in the same household creates a particular dynamic: clashing impulsivity, competing need for stimulation, simultaneous executive function failures, and a profound shared understanding that can be both a source of connection and a source of chaos.",
             "The ADHD parent-ADHD child relationship has a specific strength: you understand, from the inside, what your child's experience is. You know what it feels like when you can't initiate the task even though you want to. You know what it feels like when the emotion arrives before you can catch it. This understanding, when it translates into compassion rather than being overwhelmed alongside the child, is genuinely powerful.",
         ]},
     ], "callout": "Structure is not a prison. For ADHD brains — child or adult — it's a scaffold."},
    {"title": "Emotional Regulation in the Parenting Moment",
     "intro": "The moment of escalating conflict between an ADHD parent and a distressed child is one of the highest neurological difficulty moments that parenting produces.",
     "sections": [
         {"heading": "The Window of Tolerance in Parenting", "body": [
             "When a child is having a tantrum, meltdown, or intense emotional episode, they need a regulated adult to co-regulate with. An ADHD parent who is themselves activated — flooded by their own emotional reactivity, depleted by the day, or overwhelmed by the noise and intensity — cannot provide the regulation the child needs.",
             "The physiological sigh — one of the fastest nervous system regulation tools available — takes eight seconds. It can be done while physically present with a distressed child. Making it a reflexive response to the first signs of your own activation in parenting moments is a trainable skill. It won't work every time. It will work more often than not reacting immediately.",
         ]},
         {"heading": "The Repair Practice", "body": [
             "ADHD parents will have moments they're not proud of. The repair is what matters most. Research by John Gottman on the parent-child relationship consistently shows that the repair after a rupture is more important for the child's attachment security than the rupture itself. Parents who make mistakes and genuinely repair them — naming what happened, taking responsibility, expressing genuine care — model emotional integrity that parents who rarely lose it cannot.",
             "A repair looks like: 'Earlier I got very frustrated and raised my voice at you, and that wasn't okay. You didn't deserve that. I love you and I'm working on managing my feelings better. Are you okay?'",
         ]},
     ], "callout": "You will not be a perfect parent. The repair is where the real parenting happens."},
    {"title": "Asking for and Accepting Help",
     "intro": "ADHD parenting is not a solo sport.",
     "sections": [
         {"heading": "Building Your Co-Parenting and Support Network", "body": [
             "ADHD parents who try to manage alone — whether from pride, guilt, or lack of available support — burn out faster and parent less effectively than those who build support structures. Partner support, extended family involvement, parent community, professional support — all of these reduce the executive function burden on the ADHD parent and create conditions for more connected, regulated parenting.",
             "If you have a co-parent, explicit division of tasks based on each person's strengths — rather than the default equal division of all tasks — reduces the friction that ADHD-specific task avoidance creates. Assigning the detail-oriented administrative parenting tasks (school form management, appointment booking, schedule coordination) to the less-ADHD partner, and the spontaneous, engagement-based parenting to the ADHD parent, plays to each person's strengths.",
         ]},
         {"heading": "ADHD Coaching for Parents", "body": [
             "ADHD coaches who work specifically with parents can provide practical, personalised support for the specific executive function challenges of ADHD parenting in ways that general parenting books and courses don't address. If the challenges described in this book are significantly impacting your family, professional coaching or a therapist with ADHD expertise is worth prioritising.",
         ]},
     ], "callout": "Needing support is not failure. It's how human beings have always raised children."},
    {"title": "The Unexpected Gifts",
     "intro": "ADHD parenting has gifts as well as challenges.",
     "sections": [
         {"heading": "The ADHD Parent Advantages", "body": [
             "ADHD parents are often more playful, more spontaneous, more willing to abandon the agenda and follow the child's interest than neurotypical parents whose executive function keeps them on schedule. The willingness to be present and engaged in an unplanned moment of connection — rather than sticking to the programme — is something many ADHD children desperately need from their ADHD parents.",
             "The shared understanding between an ADHD parent and an ADHD child is a profound relational resource. 'I know what it's like when your brain makes it hard to do something you actually want to do' is not something every parent can say with genuine conviction.",
         ]},
     ], "callout": "Your ADHD is not only the thing that makes parenting harder. It's also part of what makes you the specific parent your child has."},
])

B04 = mb("ADHD and Money", "Stop the Impulse Spending and Build Real Wealth", [
    {"title": "Why Money and ADHD Are a Difficult Combination",
     "intro": "Money management requires exactly the cognitive capacities that ADHD impairs most directly: sustained attention, delayed gratification, planning, consistent follow-through, and impulse control. Understanding why the combination is difficult isn't an excuse — it's the starting point for building systems that work.",
     "sections": [
         {"heading": "The Neurological Root of ADHD Money Problems", "body": [
             "The ADHD brain has a compromised ability to delay reward. Impulse spending is not a character flaw — it's the dopamine system seeking immediate reward in the absence of sufficient frontal lobe inhibition. The $40 online purchase at 11pm produces an immediate dopamine hit. The retirement account contribution produces a reward that is forty years away. The ADHD brain is not well-suited to prioritising the second over the first without external structure.",
             "Ari Tuckman, a psychologist who has written extensively on ADHD executive function, describes the ADHD relationship with time as one where only the present feels real. Future consequences — whether financial or health-related — don't carry the motivational weight they theoretically should, because the future is difficult for the ADHD brain to simulate with sufficient vividness to drive present behaviour.",
         ]},
         {"heading": "Common ADHD Money Patterns", "body": [
             "Impulsive purchases — the late-night online order, the unplanned subscription, the tool or gadget that seemed essential and was forgotten within a week. Disorganised finances — unpaid bills not from unwillingness but from forgetting, mixed personal and business expenses, tax filings that happen in a panic. Income volatility — the ADHD tendency toward career instability, job loss, and variable freelance income compounds any underlying saving or debt problem. And the shame spiral — financial distress produces shame, which produces avoidance of financial information, which produces more financial distress.",
         ]},
     ], "callout": "Your money problems are not moral failures. They are executive function problems. They respond to executive function solutions."},
    {"title": "Building an ADHD-Proof Financial System",
     "intro": "The goal is a financial system that runs on automation and structure, requiring minimal daily executive function to maintain.",
     "sections": [
         {"heading": "The Automated Financial Architecture", "body": [
             "On payday or receipt of income, a cascade of automatic transfers should happen without any action required: a percentage to retirement (ideally matched employer contribution at minimum), a percentage to an emergency fund, a percentage to a sinking fund for known future expenses (car registration, insurance, annual subscriptions), and the remainder to day-to-day spending.",
             "The critical principle: automate all savings and investment transfers to happen before you have the chance to spend the money. Pay yourself first, automatically. What remains in the spending account is what's available to spend — no mental accounting required.",
         ]},
         {"heading": "The Weekly Money Date", "body": [
             "A brief weekly financial check-in — fifteen to twenty minutes, same time each week — is the minimum ongoing maintenance required for an ADHD person's financial health. Review what was spent against budget, pay any bills due, note any upcoming expenses, and make any necessary adjustments. This is not a judgment session — it's a maintenance session.",
             "Pair the money date with something pleasant: a coffee you enjoy, a favourite podcast before or after, a pleasant environment. The ADHD brain is more likely to maintain a habit when there is an immediate pleasant association, not just the abstract long-term benefit.",
         ]},
     ], "callout": "The best financial system for an ADHD brain is one that doesn't rely on an ADHD brain to run it."},
    {"title": "Managing Impulse Spending",
     "intro": "You can't eliminate the impulse. You can build friction between the impulse and the purchase.",
     "sections": [
         {"heading": "The 48-Hour Rule", "body": [
             "For any unbudgeted purchase above a personal threshold (start at $50, adjust as needed), impose a mandatory 48-hour wait. Add the item to a running wishlist rather than buying it. Most impulse purchase desires fade within 48 hours when the dopamine spike of the impulse passes. Those that remain after 48 hours are worth reconsidering as potentially genuine wants rather than purely impulsive ones.",
         ]},
         {"heading": "Reducing Environmental Triggers", "body": [
             "Impulse spending follows exposure to triggers — the late-night scroll through online shops, the saved credit card that makes purchasing frictionless, the marketing emails that create artificial urgency. Reducing exposure to these triggers is more effective than relying on in-the-moment willpower.",
             "Practical friction increases: remove saved credit card information from online shopping accounts (the extra 30 seconds to retrieve the card is often sufficient to interrupt an impulse). Unsubscribe from promotional emails. Set a one-tap purchase limit requiring authentication for purchases above a set amount.",
         ]},
     ], "callout": "Willpower against impulse is a losing battle. Friction against impulse is a winnable one."},
    {"title": "Building Wealth With an ADHD Brain",
     "intro": "Wealth building doesn't require complex active management — which is good, because complex active management is ADHD-hostile. It requires simple, automated systems maintained over time.",
     "sections": [
         {"heading": "The Investment Approach That Fits ADHD", "body": [
             "Index fund investing — buying diversified low-cost index funds and holding them — is the investment strategy most supported by long-term evidence and most compatible with ADHD. It requires a decision once (which funds, how much) and then automation. No daily monitoring, no tactical adjustments, no complex analysis.",
             "Active trading and cryptocurrency are, for most ADHD investors, the opposite of what they need: they provide the dopamine stimulation of novelty and action while producing, on average, worse long-term returns than passive investing. The ADHD brain's attraction to the excitement of active investment is a misalignment between what feels good and what works.",
         ]},
         {"heading": "Debt Management for ADHD", "body": [
             "Debt payoff works best for ADHD brains when it's visible and gamified. The debt snowball method — paying off smallest debts first regardless of interest rate — is less mathematically optimal than the debt avalanche (highest interest first) but produces more ADHD-compatible motivation by generating visible wins quickly.",
             "Making debt repayment automatic — extra payments set up on autopay — removes the monthly decision and the temptation to divert the money elsewhere.",
         ]},
     ], "callout": "Wealth is built through systems and time. Both are available to you. Build the system once and let time do the rest."},
    {"title": "Shame, Avoidance, and Getting Current",
     "intro": "If your finances are in genuine disarray, the path back starts with knowing where you actually are.",
     "sections": [
         {"heading": "Breaking Through Financial Avoidance", "body": [
             "Financial avoidance — the inability to open statements, check balances, or engage with financial reality — is one of the most common and damaging ADHD patterns. It feels like protection from distress but actually increases distress by allowing problems to compound unaddressed.",
             "The way through is not forcing yourself to confront everything at once. It's titration: open one statement this week. Nothing else. Just look at the number. Sit with it. Then close it. Next week, look at two. Gradually, the avoidance response to financial information reduces as the brain learns that looking doesn't kill you.",
         ]},
         {"heading": "Professional Help Without Shame", "body": [
             "A fee-only financial advisor (not commission-based), an accountant who understands ADHD clients, or a financial coach specifically trained in ADHD money management can accelerate the path from financial distress to financial function. Seeking this help is not failure — it's using the delegation principle that applies to every other area of ADHD life.",
         ]},
     ], "callout": "The number in your bank account is information, not verdict. Look at it. Work with it. It can change."},
])

B05 = mb("ADHD in Relationships", "How to Love and Be Loved With a Scattered Brain", [
    {"title": "How ADHD Shows Up in Relationships",
     "intro": "ADHD doesn't stop at the front door of a relationship. The same executive function differences that show up at work show up at home — and in the intimate context of a long-term partnership, they can be significantly more painful.",
     "sections": [
         {"heading": "The Most Common ADHD Relationship Patterns", "body": [
             "Forgetting important things — anniversaries, commitments made in conversation, things asked once and not remembered. Emotional dysregulation during conflict — the ADHD partner's disproportionate responses, quick escalation, and difficulty de-escalating. The hyperfocus trap — intense attention during the early relationship giving way to what feels like inattention once the novelty fades, which non-ADHD partners often experience as withdrawal or reduced love. And the task distribution imbalance — the non-ADHD partner gradually taking on more of the household executive function as the ADHD partner's inconsistency makes delegating unreliable.",
         ]},
         {"heading": "The Non-ADHD Partner's Experience", "body": [
             "Melissa Orlov's research on ADHD in relationships documents the characteristic pattern: the non-ADHD partner feels like a parent, nag, or manager; the ADHD partner feels constantly criticised and misunderstood; both partners feel alone in the relationship despite being physically together. This pattern is recognisable to a remarkable proportion of couples where one partner has ADHD.",
             "Understanding this pattern as a systemic consequence of ADHD dynamics — not a character failure in either partner — is the first step toward addressing it. Neither person is the villain in this story.",
         ]},
     ], "callout": "ADHD is a third party in the relationship. Naming it accurately allows both partners to work with it rather than against each other."},
    {"title": "Communication Strategies That Actually Work",
     "intro": "ADHD impairs working memory, sustained attention, and emotional regulation — all of which are required for effective communication. Strategies that compensate for these are not workarounds, they are the main path.",
     "sections": [
         {"heading": "The Conversation Framework", "body": [
             "Important conversations with an ADHD partner should happen when: both people are not hungry, tired, or already emotionally activated; the environment is quiet with minimal distraction; and there's sufficient time that the conversation doesn't feel artificially truncated. These conditions seem obvious but are rarely deliberately created.",
             "Short, clear requests over long, context-heavy ones. 'Please take the bins out tonight' over 'I've mentioned the bins several times and they still haven't gone out and it's really frustrating because...' The longer the request, the more working memory it demands, and the more likely the ADHD partner is to lose the thread.",
         ]},
         {"heading": "Writing It Down", "body": [
             "The ADHD brain does not reliably retain verbal requests. This is not willful disregard — it is a working memory limitation. Writing down agreements, tasks, and commitments — in a shared system that both partners can see — removes the dependency on the ADHD partner's working memory and the non-ADHD partner's tracking of whether things were remembered.",
             "A shared digital list (Apple Notes, Google Keep, Notion) where household tasks and commitments are logged immediately after discussion is one of the most practical single tools for ADHD couples.",
         ]},
     ], "callout": "Working memory is the constraint. External systems are the solution. Use them without shame."},
    {"title": "Managing Emotional Dysregulation in Partnership",
     "intro": "The emotional intensity of ADHD — the quick escalation, the rejection sensitivity, the difficulty de-escalating — is often the most damaging relationship feature.",
     "sections": [
         {"heading": "Recognising the Activation Early", "body": [
             "Emotional dysregulation in ADHD is faster than in neurotypical nervous systems — from neutral to activated can happen in seconds. Learning to recognise the physical early warning signs of activation — a tightening in the chest, a change in breathing, a particular quality of internal tension — and exit the conversation before escalation is a trainable skill.",
             "The exit needs to be agreed upon in advance: 'When I say I need ten minutes, that means I'm close to escalating and I'm removing myself to regulate. It's not abandonment. I'll come back when I'm calm.' This agreement, made during a calm moment, prevents the exit from being interpreted as stonewalling.",
         ]},
         {"heading": "After the Rupture", "body": [
             "ADHD emotional eruptions often end in genuine remorse — the ADHD partner recognises what happened and feels significant shame. The path through is repair, not self-flagellation. Acknowledging what happened, understanding the impact on the partner, and taking specific action to reduce recurrence (including professional support if the pattern is severe) is the functional response.",
         ]},
     ], "callout": "The intensity is real. The regulation is learnable. The relationship is worth both."},
    {"title": "Rebuilding Fairness in Partnership",
     "intro": "When the division of household and family labour is significantly unequal due to ADHD, resentment builds. Addressing this honestly is necessary for the relationship's health.",
     "sections": [
         {"heading": "A Honest Division of Labour", "body": [
             "Rather than dividing tasks equally, divide them according to capacity and genuine sustainability. The ADHD partner taking responsibility for tasks that genuinely match their profile — physically active tasks, creative tasks, high-interest-level tasks — and being released from tasks that require consistent detail management, produces better outcomes than an equal division that reliably fails.",
             "This requires honest assessment without blame: 'I am not reliable at managing school paperwork. You are. Can we formally assign this to you, and I take on X instead?' This is a negotiation between adults, not a confession of inadequacy.",
         ]},
     ], "callout": "Fair doesn't mean equal. Fair means both partners are contributing in ways that are sustainable for their actual capacities."},
    {"title": "When to Seek Couples Support",
     "intro": "ADHD-aware couples therapy is significantly more effective for ADHD relationship challenges than standard couples therapy.",
     "sections": [
         {"heading": "Finding the Right Support", "body": [
             "A therapist who doesn't understand ADHD may misattribute ADHD behaviour — the forgetting, the emotional reactivity, the inconsistency — to character flaws or relationship motivation problems, which deepens rather than resolves the conflict. Seeking a therapist with specific ADHD training, or using resources like Melissa Orlov's couples programme designed specifically for ADHD relationships, produces better outcomes.",
             "ADHD treatment itself — whether medication, coaching, therapy, or a combination — is one of the most powerful relationship interventions available. When the ADHD partner's symptoms are adequately managed, many of the relationship dynamics that cause the most friction reduce significantly.",
         ]},
     ], "callout": "The relationship is not broken. It has a specific challenge that has specific solutions. Both are worth pursuing."},
])

B06 = mb("The Late-Diagnosed Woman", "Understanding Your ADHD After 30", [
    {"title": "Why It Took This Long",
     "intro": "If you received an ADHD diagnosis in adulthood, you may be carrying two things simultaneously: relief that there's finally an explanation, and grief — or rage — that nobody caught it sooner. Both are entirely warranted.",
     "sections": [
         {"heading": "The Gender Bias in ADHD Diagnosis", "body": [
             "ADHD research and diagnostic criteria were developed primarily from studies of young boys. The hyperactive, disruptive, externally visible presentation — common in male ADHD — became the archetype against which diagnosis was measured. Female ADHD presentation often looks different: more internalised, more characterised by inattention and emotional dysregulation than hyperactivity, more masked by the social pressure girls receive to be organised, compliant, and high-achieving.",
             "Erin Sollee and other researchers have documented how girls with ADHD are more likely to be told they're 'dreamy,' 'sensitive,' or 'not living up to their potential' rather than assessed for the neurodevelopmental difference that underlies these observations. By the time these girls become adults, they have typically developed extensive masking strategies — performing neurotypicality at significant energetic cost — that make the underlying ADHD even less visible to clinicians.",
         ]},
         {"heading": "The Masking Cost", "body": [
             "Masking is the process of consciously or unconsciously suppressing ADHD-related behaviours to appear neurotypical. For late-diagnosed women, masking has often been so thorough and so long-standing that it has become invisible to both the person themselves and the people around them.",
             "The cost of sustained masking is enormous: chronic exhaustion from the effort of appearing functional, anxiety from the constant monitoring of behaviour, shame from the gap between perceived ability and actual performance, and a delayed understanding of what's actually happening. Many late-diagnosed women describe feeling fraudulent for years — capable of appearing competent while internally drowning. The ADHD explains this experience. It doesn't excuse the systems that failed to catch it sooner.",
         ]},
     ], "callout": "You were not failing. You were masking. There's a profound difference."},
    {"title": "The Late Diagnosis Experience",
     "intro": "A late ADHD diagnosis is a complex emotional event. It doesn't only feel like one thing.",
     "sections": [
         {"heading": "The Grief of Lost Time", "body": [
             "Many late-diagnosed women go through a period of retrospective grief after diagnosis: for the years of academic struggle that might have been different, for the relationships affected by unmanaged ADHD, for the careers that might have taken different shapes, for the decades of harsh self-judgment that now has a different explanation.",
             "This grief is legitimate and worth processing, not rushing past. The diagnosis changes the meaning of a lot of personal history. That meaning-making process takes time.",
         ]},
         {"heading": "The Post-Diagnosis Identity Question", "body": [
             "A late diagnosis raises an identity question: who are you if the person you thought you were — scattered, struggling, secretly inadequate — is actually someone with a neurological difference that explains all of that? Some people find this liberating. Others find it disorienting. Many find it both at different times.",
             "The practical answer is that you're the same person you were before the diagnosis. You now have a more accurate explanation for some things about yourself and, ideally, more effective tools and support. The ADHD was there all along. The diagnosis just names it.",
         ]},
     ], "callout": "The diagnosis is not a new identity. It's a more accurate explanation of the identity you've always had."},
    {"title": "Building Support After Late Diagnosis",
     "intro": "Getting diagnosed is the beginning, not the end.",
     "sections": [
         {"heading": "What Assessment and Treatment Looks Like", "body": [
             "A comprehensive ADHD assessment for adults includes structured clinical interviews, rating scales, cognitive testing in some cases, and a review of childhood history. It should be conducted by a psychologist or psychiatrist with specific expertise in adult ADHD.",
             "Treatment may include medication (stimulants and non-stimulants, each with different profiles), therapy (particularly CBT adapted for ADHD), ADHD coaching, and the kind of structural and systemic changes described throughout this book series. Most adults with ADHD benefit from a combination rather than any single approach.",
         ]},
         {"heading": "Finding Your ADHD Community", "body": [
             "The ADHD community for late-diagnosed women has grown substantially in recent years, particularly online. Accounts like ADHD Women, communities on Reddit (r/ADHDwomen), and podcasts including ADHD Experts and Hacking Your ADHD provide both information and the normalising experience of recognising yourself in others.",
             "The relief of having language for your experience, and of finding others who share it, is genuinely therapeutic. It counteracts the isolation and the shame that often accompany years of undiagnosed struggle.",
         ]},
     ], "callout": "You deserved to know sooner. Now that you know, you get to decide what to do with it."},
    {"title": "Hormones and ADHD — The Missing Conversation",
     "intro": "The relationship between ADHD and hormonal cycles is one of the most clinically underaddressed topics in women's ADHD care.",
     "sections": [
         {"heading": "Estrogen and ADHD Symptoms", "body": [
             "Estrogen has direct effects on dopamine signalling — the neurotransmitter system most implicated in ADHD. When estrogen rises (as in the follicular phase of the menstrual cycle), dopamine function improves and ADHD symptoms are often more manageable. When estrogen drops (premenstrual phase, perimenopause, postpartum), dopamine function reduces and ADHD symptoms often worsen significantly.",
             "Many women notice dramatic ADHD symptom fluctuations across their cycle without connecting them to hormonal changes. Tracking symptoms alongside the cycle — using a period tracking app with a symptom logging function — can reveal patterns that are useful both for personal understanding and for clinical conversations about treatment adjustments.",
         ]},
         {"heading": "Perimenopause and Late-Onset ADHD Diagnosis", "body": [
             "A significant proportion of women who receive ADHD diagnoses in their 40s were driven to seek assessment by what felt like a sudden cognitive decline — brain fog, worsening organisation, emotional volatility, inability to concentrate that seemed new. In many cases, ADHD was always present but was compensated by estrogen-supported dopamine function. As estrogen declines in perimenopause, the compensation fails and the ADHD becomes visible.",
             "This means the conversation about hormonal treatment (HRT) and ADHD treatment needs to happen simultaneously. Treating ADHD without addressing the hormonal context in perimenopausal women may produce limited results. Both dimensions deserve attention.",
         ]},
     ], "callout": "Your hormones are not separate from your ADHD. They are part of the same story."},
    {"title": "Moving Forward",
     "intro": "A late diagnosis is an ending and a beginning simultaneously.",
     "sections": [
         {"heading": "Self-Compassion as a Practice", "body": [
             "Self-compassion research by Kristin Neff consistently shows that self-compassion — treating yourself with the same care you'd offer a friend in difficulty — improves motivation, resilience, and wellbeing outcomes. For late-diagnosed ADHD women carrying years of self-criticism and shame, cultivating self-compassion is not a soft nicety. It's a clinical priority.",
             "The practice: when encountering ADHD-related difficulty, apply the three components of self-compassion. Self-kindness: speak to yourself as you would speak to a friend ('this is hard, and that's okay'). Common humanity: remember that struggle is part of the shared human experience, not evidence of unique personal failure. Mindfulness: observe the difficulty without either suppressing it or over-identifying with it.",
         ]},
     ], "callout": "You made it this far figuring it out largely alone. Imagine what becomes possible with accurate information and the right support."},
])

B07 = mb("ADHD and Creativity", "Channeling Your Brain's Chaos Into Brilliant Work", [
    {"title": "The Creative ADHD Brain",
     "intro": "The ADHD brain and the creative brain have significant overlap — not because ADHD makes you creative, but because several of the cognitive patterns associated with ADHD also drive creative output: divergent thinking, pattern recognition across unrelated domains, comfort with novelty, and hyperfocus on genuinely engaging problems.",
     "sections": [
         {"heading": "What Makes ADHD Brains Creative", "body": [
             "Leaky attention — the ADHD tendency to pick up information from the environment without deliberately filtering it — is associated with higher levels of creative ideation. Where a neurotypical brain efficiently ignores irrelevant stimuli, the ADHD brain notices them, stores them, and connects them with other seemingly unrelated information in ways that produce unexpected associations.",
             "Research by Holly White and Priti Shah found that students with ADHD produced more creative solutions on divergent thinking tasks than matched controls. The same distractibility that makes focused work difficult is associated with the broad, non-linear thinking that generates original ideas.",
         ]},
         {"heading": "Hyperfocus as Creative Engine", "body": [
             "Hyperfocus — the ADHD brain's capacity for intense, sustained engagement with genuinely interesting problems — is one of the most powerful creative states available to a human being. When an ADHD person hyperfocuses on a creative project, the depth and speed of output can be extraordinary.",
             "The challenge for creative ADHD people is not the absence of creative capacity. It's the unreliability of access to that capacity, and the difficulty of completing and delivering creative work through the less-interesting phases of production that follow the initial creative excitement.",
         ]},
     ], "callout": "The chaos in your brain is not the enemy of your creativity. It's part of its source."},
    {"title": "Managing the Creative Process With ADHD",
     "intro": "The creative process has phases, and ADHD interacts differently with each one.",
     "sections": [
         {"heading": "The Idea Generation Phase", "body": [
             "This is where ADHD brains shine. The challenge is capturing the ideas before they disappear — ADHD working memory is notoriously poor at retaining insights that aren't immediately recorded. A frictionless capture system — a voice memo app, a notes app accessible in one tap, a physical notebook always in reach — is the foundation of a creative ADHD practice.",
             "Capture everything. Evaluate later. The ADHD brain that pauses to evaluate the quality of an idea before recording it will lose the next three ideas in the time it takes to decide. Capture now, curate later.",
         ]},
         {"heading": "The Development and Execution Phase", "body": [
             "This is where ADHD creative projects die most often. The initial excitement has passed. The work is now about sustaining attention through the difficult, detailed, less-interesting phases of realising the original idea. This is precisely where the ADHD motivation system struggles most.",
             "Strategies for the execution phase: break the project into the smallest possible specific tasks; use timeboxing (commit to one hour on one specific task rather than open-ended work sessions); maintain novelty by varying approach, environment, or tools periodically; and use accountability structures to create external deadlines and pressure that the ADHD motivation system responds to.",
         ]},
     ], "callout": "Ideas are not the bottleneck. Getting from idea to finished is. Build the system for the hard part."},
    {"title": "Protecting Creative Time",
     "intro": "Creative work requires protected time. ADHD makes protecting time difficult. The solution is deliberate structure.",
     "sections": [
         {"heading": "Designing Your Creative Environment", "body": [
             "ADHD brains are highly responsive to environment. The right environment for creative work varies — some ADHD creatives need the social activation of a coffee shop, others need particular music or complete silence, others need physical movement available. Discovering and deliberately creating your optimal creative environment is as important as showing up to do the work.",
             "Consistent creative time — the same slot each day or week, in the same environment — builds associative memory: the brain begins to associate that context with creative work and enters the appropriate state more readily than if context is variable.",
         ]},
         {"heading": "Finishing What You Start", "body": [
             "The graveyard of unfinished projects is a universal ADHD experience. The novel at 40,000 words. The half-built website. The course outline that never became a course. Managing this requires honest assessment: which projects are genuinely worth completing, and which are unfinished because the interest has legitimately passed?",
             "For projects worth completing: set a specific completion deadline; define done explicitly (a project without a clear finish line will keep expanding); and consider whether the project needs to be reduced in scope to match available sustained motivation.",
         ]},
     ], "callout": "Start less. Finish more. The unfinished projects cost more than the projects never started."},
    {"title": "ADHD and Professional Creative Life",
     "intro": "Making a living from creative work with ADHD requires a specific architecture.",
     "sections": [
         {"heading": "The Business Side of Creative Work", "body": [
             "Creative ADHD people often struggle most not with the creative work itself but with the business infrastructure that surrounds it: marketing, client management, invoicing, contract management, administrative follow-through. The strategies throughout this book series — automation, delegation, external systems — apply directly to the business side of creative professional life.",
         ]},
         {"heading": "Managing Creative Cycles", "body": [
             "Creative work produces natural cycles of high energy and low energy, inspiration and drought. ADHD amplifies these cycles. Managing a sustainable creative career requires working with the cycles rather than against them: banking output during hyperfocus and high-motivation periods, reducing commitments during low periods, and building financial buffers that allow for the variable output that ADHD creative cycles produce.",
         ]},
     ], "callout": "Your creative work is real. The business around it is learnable. You don't have to be good at both at the same time."},
    {"title": "The Creative ADHD Community",
     "intro": "You are not alone in navigating this.",
     "sections": [
         {"heading": "Finding Your Creative Tribe", "body": [
             "Creative communities with ADHD representation — writing groups, artist collectives, maker spaces, online creative communities — provide the social activation that supports ADHD creative work and the normalising effect of being around others whose brains work similarly. The combination of creative support and ADHD understanding makes these communities particularly valuable.",
             "Creating accountability structures within creative communities — regular sharing deadlines, critique groups, co-working sessions — adapts the external accountability that ADHD brains need to the specific context of creative work.",
         ]},
     ], "callout": "The best creative work often comes from the most surprising brains. Yours is one of them."},
])

B08 = mb("ADHD + AI", "The Ultimate Productivity Stack for Neurodivergent Minds", [
    {"title": "Why AI Is a Game-Changer for ADHD",
     "intro": "AI tools — particularly large language model assistants like Claude, ChatGPT, and Gemini — are the most significant practical development for ADHD productivity in a generation. Not because they fix ADHD. But because they compensate for its specific executive function deficits in ways that previous tools couldn't.",
     "sections": [
         {"heading": "What AI Compensates For", "body": [
             "AI compensates for exactly the executive function deficits that ADHD impairs most: initiating tasks (AI can provide structure and a starting point for any task that seems impossibly large), working memory (AI can hold context, summarise previous information, and remember details across a conversation), planning and organising (AI can turn a vague intention into a specific plan), and the writing tasks that require sustained focused attention to produce clear output.",
             "For an ADHD person who has spent years struggling with tasks that neurotypical peers seem to manage without effort, having a tool that genuinely reduces the executive function barrier to initiation and completion is significant.",
         ]},
         {"heading": "ADHD and the AI Learning Curve", "body": [
             "AI tools have their own learning curve — learning what prompts produce useful outputs, how to structure requests, how to use different tools for different tasks. For ADHD, this learning curve is worth overcoming because the payoff is high. But it should be approached as deliberate skill-building rather than expecting immediate fluency.",
         ]},
     ], "callout": "AI doesn't do the work for you. It removes the barriers that were preventing you from doing it yourself."},
    {"title": "Practical AI Use Cases for ADHD",
     "intro": "The specific ways AI tools reduce executive function friction for ADHD in daily work and life.",
     "sections": [
         {"heading": "Task Initiation — Breaking Through the Starting Block", "body": [
             "Task initiation paralysis — the inability to start despite wanting to — is one of the most debilitating ADHD experiences. AI addresses this directly: provide the task description and ask for a step-by-step breakdown of the first thirty minutes. The concrete, specific first action removes the cognitive load of figuring out where to begin.",
             "Example: 'I need to write a business proposal for a new client. I keep avoiding it. Give me a step-by-step outline of what to do in the next 30 minutes, starting from right now.' The AI provides a scaffold. You execute.",
         ]},
         {"heading": "Writing and Communication", "body": [
             "ADHD often impairs writing — not because ADHD people can't write, but because the translation from ideas (which arrive rapidly and non-linearly) to structured written text (which requires organising, sequencing, and sustained attention) is precisely the type of cognitive operation ADHD struggles with.",
             "AI dramatically reduces this barrier: talk or type the raw ideas, ask AI to structure them into a coherent document, then edit the result. The editing task is far more ADHD-compatible than the blank-page generation task. The output is yours — you provided the ideas, the direction, and the final decisions. The AI provided the scaffolding.",
         ]},
         {"heading": "Administrative Tasks", "body": [
             "The administrative tasks that pile up for ADHD people — emails requiring thoughtful responses, formal documents, meeting summaries, scheduling coordination — are exactly the tasks AI handles well. A backlog of unanswered emails can be worked through significantly faster when AI drafts responses based on brief instructions.",
         ]},
     ], "callout": "Every executive function task that AI can do for you is executive function you have available for something that only you can do."},
    {"title": "Building Your ADHD AI Stack",
     "intro": "Different AI tools serve different functions. Building a coherent stack means knowing which tool to reach for in which situation.",
     "sections": [
         {"heading": "The Core Tools", "body": [
             "A conversational AI assistant (Claude, ChatGPT) for task initiation, writing, planning, brainstorming, and working through complex decisions. A transcription tool (Otter.ai, Whisper) for capturing ideas by speaking rather than typing — particularly useful for ADHD people who think better verbally than in writing. A calendar/task management system that integrates AI (Reclaim, Motion) for automatically scheduling tasks and protecting focus time.",
         ]},
         {"heading": "The ADHD Prompt Toolkit", "body": [
             "Learning to prompt AI effectively is a skill worth developing. For ADHD specifically, high-value prompt patterns include: 'Break this into the smallest possible steps', 'I have 20 minutes — what should I focus on first?', 'Turn this mess of notes into a clear summary', 'Write an email that says [intention] in a professional tone', 'I keep avoiding [task] — give me the easiest possible starting point.'",
         ]},
     ], "callout": "A tool is only useful if you know how to use it. Learn the prompts that unlock the most value for your specific workflow."},
    {"title": "AI Risks and Boundaries for ADHD",
     "intro": "AI is powerful. It also has specific risks that are worth knowing.",
     "sections": [
         {"heading": "The Procrastination Trap", "body": [
             "For ADHD, AI can become a sophisticated form of productive procrastination — spending hours refining prompts, generating elaborate plans, and optimising systems rather than executing the actual work. The tool should reduce friction to action, not replace action.",
             "A useful self-check: has using AI in the last hour moved a project forward, or has it created the feeling of productivity without the output? If it's the latter, close the AI and do the smallest possible action on the actual project.",
         ]},
         {"heading": "Maintaining Your Own Skills", "body": [
             "Delegating cognitive tasks to AI is appropriate. Losing the underlying skill entirely is worth avoiding. Writing with AI assistance is different from never writing without it. The skill of working through a difficult problem without AI scaffolding remains valuable — both for situations where AI isn't available and for maintaining cognitive capacities that have long-term health implications.",
         ]},
     ], "callout": "Use the tool. Don't become dependent on it. There's a difference."},
    {"title": "The Integrated ADHD Productivity System",
     "intro": "AI is one component of an effective ADHD productivity system, not the whole system.",
     "sections": [
         {"heading": "Bringing It Together", "body": [
             "The complete ADHD productivity system integrates: ADHD management (medication and/or therapy where appropriate), structural systems (time blocking, external accountability, automated administration), environmental design (optimal sensory environment, body doubling, physical movement access), and AI tools (for executive function augmentation on specific task types).",
             "No single component of this system is sufficient alone. Medication without systems produces a more alert ADHD person who still doesn't have structures for managing their time and tasks. Systems without medication or treatment may be too cognitively demanding to maintain. AI without the other components can create sophisticated procrastination. Together, they compound.",
         ]},
     ], "callout": "The system is greater than the sum of its parts. Build all the parts."},
])

B09 = mb("ADHD Burnout Recovery", "Recognizing It, Stopping It, and Coming Back Stronger", [
    {"title": "ADHD Burnout Is Different",
     "intro": "ADHD burnout is distinct from general burnout and is more common and more severe in people with ADHD than the general population. Understanding how and why it develops — specifically in the ADHD context — is the first step toward genuine recovery.",
     "sections": [
         {"heading": "The ADHD Burnout Mechanism", "body": [
             "ADHD burnout accumulates from a specific source: the chronic, sustained effort of managing an ADHD nervous system in a world designed for neurotypical ones. This includes: the daily effort of masking ADHD traits to appear functional; the executive function tax of compensating for working memory, time management, and attention deficits; the emotional regulation effort of managing ADHD emotional reactivity in professional and social contexts; and the accumulated shame of years of underperformance relative to perceived potential.",
             "This is a different energetic burden than the busyness burnout most burnout literature addresses. ADHD burnout can happen even in people who appear to be coping well externally — because the coping is what's producing the depletion.",
         ]},
         {"heading": "Signs of ADHD Burnout", "body": [
             "Increased difficulty with tasks that were previously manageable. Emotional numbing or increased emotional reactivity. Complete inability to access motivation even for previously enjoyed activities. Social withdrawal beyond typical ADHD introversion or recovery needs. Physical symptoms: exhaustion, immune challenges, digestive disruption. And critically — the collapse of previously maintained coping strategies: the systems that were working stop working, the masking that was possible becomes impossible.",
         ]},
     ], "callout": "ADHD burnout is what happens when the compensation system that was holding everything together finally runs out of capacity."},
    {"title": "The Recovery Framework",
     "intro": "ADHD burnout recovery follows a specific sequence. Attempting to skip phases — returning to productivity before the system has genuinely recovered — produces relapse.",
     "sections": [
         {"heading": "Phase One: Permission to Stop", "body": [
             "The first phase of ADHD burnout recovery is permission — permission to stop performing, stop compensating, and stop maintaining the appearance of function that has been depleting the system. This is not permission to abandon all responsibility indefinitely. It's permission for the specific period of acute recovery.",
             "This phase is often the hardest for ADHD people whose sense of worth has been tied to productivity and output. The ADHD brain that has spent years proving it can function as well as neurotypical peers does not easily allow itself to rest.",
         ]},
         {"heading": "Phase Two: Reducing Demand", "body": [
             "ADHD burnout recovery requires reducing the total executive function demand on the system while it recovers. This means simplifying: fewer commitments, more structure, more sleep, less stimulation, less masking. It may mean temporarily reducing work hours, delegating more aggressively, or taking medical leave if symptoms are severe.",
         ]},
         {"heading": "Phase Three: Structural Change", "body": [
             "Recovery without structural change produces recovery and recurrence. The structural changes that prevent ADHD burnout recurrence are: appropriate treatment for ADHD (medication and/or therapy); environmental modifications that reduce the compensation requirement; and honest assessment of which commitments and relationships require the most masking and whether they can be changed.",
         ]},
     ], "callout": "Recovery is not a return to the same conditions that produced the burnout. It's a redesign."},
    {"title": "Nervous System Repair in ADHD Burnout",
     "intro": "The practices most relevant to ADHD burnout recovery are the nervous system regulation approaches throughout this series.",
     "sections": [
         {"heading": "Rest That Actually Restores", "body": [
             "ADHD people often don't find rest restorative — they find it boring or overstimulating in a different way (the absence of external structure producing internal restlessness). Rest that restores the ADHD nervous system tends to be gentle sensory engagement: walking in nature, movement without performance pressure, music, cooking, creating without stakes.",
             "Screen rest — genuinely low-stimulation periods without scrolling, streaming, or gaming — is particularly important during burnout recovery. The dopamine system that has been running on deficit needs a period of reduced demand, not a shift from one high-stimulation source to another.",
         ]},
         {"heading": "ADHD Burnout and Medication", "body": [
             "Some ADHD people find that stimulant medication, while helpful for executive function, contributes to burnout if used to push through depletion rather than to support functional work within sustainable limits. If this pattern is present, a medication review with the prescribing clinician is appropriate.",
         ]},
     ], "callout": "Recovery looks like slowing down. The nervous system cannot repair at speed."},
    {"title": "Coming Back Differently",
     "intro": "The goal of burnout recovery is not a return to the previous state. It's emergence into a different relationship with your own capacity.",
     "sections": [
         {"heading": "Rebuilding on More Honest Foundations", "body": [
             "ADHD burnout recovery, when done well, produces a clearer understanding of actual versus performed capacity, more honest communication about needs and limits, and more ADHD-accommodating structures. The person who comes back from ADHD burnout having done this work is genuinely different — not fixed, but no longer pretending.",
         ]},
         {"heading": "Professional Support in Burnout", "body": [
             "ADHD-aware therapists, coaches, and where appropriate psychiatrists are essential supports for ADHD burnout that is severe or slow to recover. Please don't try to white-knuckle your way through burnout recovery alone — the same self-sufficiency and reluctance to ask for help that contributed to the burnout is often what extends it.",
         ]},
     ], "callout": "You don't have to earn your way back. You just have to come back."},
])

B10 = mb("The ADHD Sales Engine", "High-Energy Selling for the Neurodivergent Mind", [
    {"title": "Why ADHD and Sales Can Be a Perfect Match",
     "intro": "Sales has a reputation for being relationship-dependent, high-energy, and improvisation-based. These are descriptions of the ADHD strength profile. The ADHD brain that struggles with sustained, structured, detail-heavy work frequently excels in the dynamic, interpersonal, and novelty-rich environment of selling.",
     "sections": [
         {"heading": "The ADHD Sales Advantages", "body": [
             "Genuine curiosity about people — one of the most consistent ADHD traits — is one of the most valued qualities in relationship-based selling. The ADHD person who is genuinely interested in understanding the prospect's situation, who asks questions because they actually want to know, and who is visibly engaged in the conversation creates a connection that scripted sales processes can't replicate.",
             "Pattern recognition across industries and situations, the ability to think on their feet without a script, comfort with ambiguity and rejection, and the high-energy presence that characterises many ADHD people in activated states are all genuine sales advantages.",
         ]},
         {"heading": "The Specific ADHD Sales Challenges", "body": [
             "The challenges are equally specific: follow-up consistency (the ADHD brain that finds the initial conversation genuinely engaging often loses interest in the administrative follow-up); CRM hygiene (logging calls, updating pipelines, maintaining records — all detail-management tasks); pipeline management across multiple prospects over time; and the boom-bust pattern of intense activity followed by administrative backlogs.",
         ]},
     ], "callout": "ADHD salespeople don't need to become neurotypical salespeople. They need systems that let them sell like themselves."},
    {"title": "The ADHD Sales System",
     "intro": "A sales system designed for ADHD compensates for the administrative and consistency gaps while protecting the high-energy relationship strengths.",
     "sections": [
         {"heading": "Immediate Follow-Up Protocol", "body": [
             "The most important ADHD sales habit is doing follow-up immediately — within minutes of a call ending, not hours later when the window of motivation has passed. Log the CRM note while the conversation is fresh. Send the follow-up email before moving on to the next activity. Set the next contact reminder before closing the record.",
             "The ADHD brain's enemy in sales administration is the future self who will 'remember to do it later.' There is no later. There is only now, while the interest and context are still present.",
         ]},
         {"heading": "Using AI for Sales Admin", "body": [
             "AI can significantly reduce the cognitive burden of sales administration: transcribing and summarising sales calls, drafting follow-up emails, generating personalised outreach based on prospect information, and maintaining consistency across a high-volume pipeline. The ADHD salesperson who uses AI for the administrative work that depletes them has more energy and attention for the relationship work where they actually excel.",
         ]},
         {"heading": "Pipeline Management for ADHD", "body": [
             "Visual pipeline management — seeing all prospects in a kanban-style view with clear next actions and dates — is more ADHD-compatible than list-based CRM systems. Tools like Trello, Notion, or visual CRMs (Pipedrive, HubSpot) externalise the pipeline in a way that makes the current state visible without requiring working memory to reconstruct it.",
         ]},
     ], "callout": "Your brain wins the conversation. Systems win the deal."},
    {"title": "Managing Rejection and Maintaining Momentum",
     "intro": "Sales involves rejection. ADHD and rejection sensitivity make this particularly challenging.",
     "sections": [
         {"heading": "RSD and Sales", "body": [
             "Rejection sensitive dysphoria — the intense emotional pain triggered by perceived rejection — is a significant challenge for ADHD salespeople. A lost deal, a prospect who ghosts, a critical call debrief — these can produce emotional responses disproportionate to the objective reality, and can derail the activity momentum that sustains a pipeline.",
             "Frameworks that help: reframe rejection as information rather than verdict; separate prospect decisions from personal worth consistently and explicitly; and build in brief regulation practices (physiological sigh, short walk) between difficult calls rather than moving immediately from rejection to the next call in a reactive state.",
         ]},
         {"heading": "Activity-Based Metrics", "body": [
             "The ADHD salesperson benefits from activity-based measurement rather than outcome-based measurement for daily motivation. You cannot control whether a prospect buys. You can control how many qualified conversations you have, how many follow-ups you complete, and how many personalised outreach messages you send. Tracking these inputs — where ADHD energy and effort actually apply — produces more sustainable motivation than tracking outcomes alone.",
         ]},
     ], "callout": "Rejection is part of sales. RSD makes it feel personal. It almost never is."},
    {"title": "Building a Long-Term Sales Career With ADHD",
     "intro": "The ADHD qualities that make for excellent salespeople are sustainable when the environment is right.",
     "sections": [
         {"heading": "Finding the Right Sales Environment", "body": [
             "Not all sales environments suit ADHD equally. High-transaction, repetitive, process-bound sales (insurance cold-calling from a script, for example) play entirely to ADHD weaknesses. Complex, relationship-based, consultative sales — where each engagement is different, problem-solving is required, and relationship development over time is the model — play to ADHD strengths.",
             "Choosing the right sales context is as important as building the right skills. An ADHD salesperson in the wrong environment will underperform despite genuine capability. The same person in a consultative, relationship-based role may be exceptional.",
         ]},
     ], "callout": "The right environment turns your ADHD traits from liabilities into your competitive advantage."},
])

books = [
    ("01 - The ADHD Entrepreneur.pdf", B01),
    ("02 - ADHD for Freelancers.pdf", B02),
    ("03 - The ADHD Parent.pdf", B03),
    ("04 - ADHD and Money.pdf", B04),
    ("05 - ADHD in Relationships.pdf", B05),
    ("06 - The Late-Diagnosed Woman.pdf", B06),
    ("07 - ADHD and Creativity.pdf", B07),
    ("08 - ADHD + AI.pdf", B08),
    ("09 - ADHD Burnout Recovery.pdf", B09),
    ("10 - The ADHD Sales Engine.pdf", B10),
]

if __name__ == "__main__":
    for filename, data in books:
        generate_ebook(os.path.join(BASE, filename), data)
