"""
Books 03–10 — The Somatic Reset Series
Generates all remaining books in Series 1
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generate_ebook import generate_ebook

BASE = os.path.dirname(__file__)
ACCENT = "#3A86FF"
BG = "#F0F6FF"
SERIES = "The Somatic Reset Series"

DISCLAIMER_HEALTH = """This book is intended for educational and informational purposes only. It is not a substitute for professional medical, psychological, or psychiatric advice, diagnosis, or treatment. Always consult a qualified healthcare provider before making changes to your health routine, especially if you have a pre-existing condition.\n\nThe practices described here are general wellness approaches. Results will vary between individuals. The author and publisher accept no liability for outcomes arising from use of this material."""

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 03
# ─────────────────────────────────────────────────────────────────────────────
BOOK_03 = {
    "title": "The Dopamine Reset",
    "subtitle": "Breaking the Overstimulation Cycle Naturally",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "The Overstimulated Nervous System",
            "intro": "There's a particular kind of exhaustion that comes not from doing too much, but from being stimulated too much. Scrolling when you're already drained. Noise-cancelling headphones that somehow never cancel the noise inside. The feeling of being tired and wired at the same time. That's the overstimulated nervous system — and it has everything to do with dopamine.",
            "sections": [
                {"heading": "What Dopamine Actually Does", "body": [
                    "Dopamine is probably the most misunderstood neurochemical in popular culture. It's not the pleasure chemical — it's the anticipation chemical. Dopamine is released in response to the prediction of reward, not the reward itself. The notification sound triggers dopamine. The scroll releases it. The bite of food before you've tasted it.",
                    "This distinction matters enormously because it explains why modern technology is so exhausting. Infinite scroll, variable reward schedules, notification systems — these are engineered to exploit the dopamine prediction system continuously. The result isn't satisfaction. It's a dopamine system that's been flooded and depleted at the same time: always seeking, never arriving, never actually receiving.",
                    "Low dopamine isn't about being unhappy. It's about a specific cluster of experiences: difficulty feeling motivated by things that used to interest you, finding quiet boring rather than restful, needing more and more stimulation to feel anything, struggling to complete tasks that don't offer immediate feedback. Sound familiar?",
                ]},
                {"heading": "The Nervous System in Overstimulation", "body": [
                    "Chronic overstimulation keeps the sympathetic nervous system partially activated — not at full fight-or-flight, but at a low-level hum of readiness. The body is braced for the next input. Rest feels uncomfortable because the system has been calibrated to expect constant incoming signals.",
                    "This is why many people find genuine silence or unstructured time more stressful than a busy schedule. The dopamine system has been conditioned to require stimulation, and its absence produces a withdrawal-like state — restlessness, irritability, difficulty concentrating, and a reaching for the nearest available input.",
                    "Resetting this doesn't require dramatic deprivation. It requires deliberately, consistently reducing the density of stimulation — creating spaces where the nervous system isn't processing something — and tolerating the discomfort of that until the system recalibrates.",
                ]},
            ],
            "callout": "The problem isn't that you don't enjoy things. It's that the signal-to-noise ratio has been reversed."
        },
        {
            "title": "Understanding Your Stimulation Baseline",
            "intro": "Before you can reset anything, you need to know where you're starting from.",
            "sections": [
                {"heading": "Mapping Your Stimulation Habits", "body": [
                    "For one day, without judgment, notice every time you reach for stimulation outside of deliberate tasks. The phone check in the middle of a conversation. The background noise you put on immediately when the house gets quiet. The podcast during your commute that started as enrichment and became something you need in order not to think.",
                    "These reaching behaviours are not moral failures. They're neurological patterns — responses to the mild discomfort of an understimulated dopamine system. Noticing them is the first step toward having a choice about them.",
                ]},
                {"heading": "High, Medium, and Low Dopamine Activities", "body": [
                    "Not all stimulation is equivalent. High-dopamine activities — those that trigger fast, high spikes — include social media, video games, pornography, sugar and ultra-processed food, gambling, and most streaming. These produce intense spikes followed by rapid depletion.",
                    "Medium-dopamine activities include conversation, music, exercise, cooking, and most social activity. They produce moderate, sustained dopamine that doesn't deplete as sharply.",
                    "Low-dopamine activities are things like walking in nature, journaling, reading physical books, long stretches of focused work, meditation, and most physical craft. These produce slow, low-level dopamine releases that are sustainable and don't create the boom-bust cycle.",
                    "A dopamine reset doesn't mean eliminating high-dopamine activities entirely. It means shifting the balance — spending less time in the high-spike zone and more time in the low-to-medium range — so the baseline recalibrates.",
                ]},
            ],
            "callout": "You haven't lost your ability to enjoy simple things. You've temporarily overwhelmed the system that registers them."
        },
        {
            "title": "The Reset Protocol — Week by Week",
            "intro": "This is a graduated approach, not a cold-turkey detox. Dramatic changes tend to produce rebound. Gradual reduction produces recalibration.",
            "sections": [
                {"heading": "Week One: Reduction Without Elimination", "body": [
                    "In week one, the single change is this: no high-stimulation activities for the first hour of the day and the last hour before sleep. That's it. Two protected hours — one in the morning, one at night — during which you do not check social media, stream video, play games, or consume any fast-moving digital content.",
                    "Replace these hours with low-stimulation activities: slow movement, reading, journaling, quiet conversation, sitting with a hot drink. The discomfort of this is informative — the degree of restlessness you feel in those two hours tells you something accurate about the degree to which your system has adapted to constant stimulation.",
                ]},
                {"heading": "Week Two: Extending the Low-Stimulation Window", "body": [
                    "Add a third protected window: a midday hour of low stimulation. This might mean a walk without headphones, a lunch without a screen, or fifteen minutes of sitting in a park with no agenda. The nervous system needs multiple low-stimulation periods throughout the day, not just at the edges.",
                    "Also in week two: notice which high-stimulation activities you miss most and which you barely notice having reduced. The ones you miss most are the ones the dopamine system has most strongly attached to. They deserve the most deliberate attention going forward.",
                ]},
                {"heading": "Weeks Three and Four: Natural Pleasures", "body": [
                    "By week three, most people notice that some things that seemed boring in week one are more interesting. A walk that felt dull now registers more — the specific quality of light, the smell of the air, details that were previously filtered out by a system tuned to high-input signals.",
                    "The reset is working when simple things start to feel like enough. Not as a consolation prize — genuinely enough. This is not regression to a less sophisticated form of enjoyment. It's the restoration of a dopamine system that can again register the rewards that don't require infinite stimulation to produce.",
                ]},
            ],
            "callout": "Boredom is not an emergency. It's the starting point for almost everything interesting."
        },
        {
            "title": "Movement, Sleep, and Nutrition for Dopamine",
            "intro": "The fastest way to restore dopamine function is not behavioural — it's biological. Your lifestyle either supports healthy dopamine cycling or works against it.",
            "sections": [
                {"heading": "Exercise and Dopamine", "body": [
                    "Aerobic exercise increases dopamine receptor density — not just the amount of dopamine released, but the number of receptors available to receive it. This is one of the most robust findings in exercise neuroscience. Even twenty to thirty minutes of moderate aerobic exercise produces acute dopamine increases comparable to certain stimulant medications.",
                    "For dopamine reset purposes, consistency matters more than intensity. A daily twenty-minute walk does more than one intense weekly workout. The regularity of the dopamine signal from exercise gradually recalibrates the baseline.",
                ]},
                {"heading": "Sleep as Dopamine Restoration", "body": [
                    "Dopamine is synthesised and receptor sensitivity is restored primarily during sleep. Chronic sleep restriction depletes dopamine function — which is why sleep-deprived people show the same reaching behaviours as high-stimulation addicts: more food seeking, more novelty seeking, more dopamine-activating behaviours to compensate for a depleted system.",
                    "Seven to nine hours of sleep is not a luxury. It's the physiological mechanism by which dopamine restores itself. Protecting sleep during a dopamine reset is not optional.",
                ]},
                {"heading": "Nutrition and the Dopamine Precursor Chain", "body": [
                    "Dopamine is synthesised from the amino acid tyrosine, which comes from protein. Diets low in complete protein can impair dopamine synthesis. Good dietary sources of tyrosine include eggs, fish, meat, dairy, almonds, avocados, and seeds.",
                    "The gut microbiome also plays a role in dopamine production — several bacterial strains produce dopamine precursors. A diverse, fibre-rich diet that supports microbiome health indirectly supports dopamine function. The connection between gut health and mood is partly a dopamine story.",
                ]},
            ],
            "callout": "You can't think your way to better dopamine function. You have to live your way there."
        },
        {
            "title": "Sustainable Enjoyment — Life After the Reset",
            "intro": "The goal of a dopamine reset is not asceticism. It's restoring the capacity for genuine pleasure — including the pleasures of high-stimulation activities — without dependency on them.",
            "sections": [
                {"heading": "Reintroducing High-Stimulation Activities Intentionally", "body": [
                    "After a genuine reset period, high-stimulation activities can be reintroduced deliberately rather than habitually. The difference is significant. Watching two hours of television because you chose to and are enjoying it is physiologically different from watching two hours because you couldn't stop. Intentionality preserves agency; habit erodes it.",
                    "The practical question is: can you do this thing and stop when you planned to? If the answer is reliably no — if the activity pulls you further than you intended — that's useful information about where your dopamine system still has calibration to do.",
                ]},
                {"heading": "The Long Game", "body": [
                    "Dopamine recalibration is not a one-time reset. It's an ongoing relationship with stimulation that requires periodic attention, especially during high-stress periods when the pull toward escapism is strongest.",
                    "Building in regular low-stimulation periods — not as deprivation but as maintenance — keeps the system calibrated. One full day per week without social media. One week per year without streaming services. These are not dramatic sacrifices. They're the equivalent of servicing an engine so it runs well.",
                ]},
            ],
            "callout": "When you're no longer dependent on stimulation to feel okay, you get to enjoy it for what it actually is."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 04
# ─────────────────────────────────────────────────────────────────────────────
BOOK_04 = {
    "title": "Nervous System Healing for Burnout",
    "subtitle": "Rewire Your Body After Chronic Stress",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "What Burnout Actually Is",
            "intro": "Burnout is not a mindset problem. It's a physiological one. The word has been so overused that it now carries a vague association with being very tired from work. But clinical burnout is a specific state of nervous system collapse — and understanding it accurately is the first step toward genuine recovery.",
            "sections": [
                {"heading": "The Three Phases of Burnout", "body": [
                    "Burnout typically progresses through recognisable stages. In the first phase, there's high activation and drive — working intensely, feeling capable, perhaps even thriving on the pressure. The nervous system is running on sympathetic activation, cortisol is elevated, and the productivity feels sustainable because it's producing results.",
                    "The second phase is the erosion phase. The system can no longer sustain the output it was producing. Sleep becomes less restorative. Motivation fluctuates. There are more bad days than good. Emotions are less regulated. This phase is often when people push harder, interpreting the decline as a personal failing rather than a physiological signal.",
                    "The third phase is collapse. The nervous system cannot sustain even basic function. Getting out of bed feels effortful. Concentration is severely impaired. Emotional responses are either blunted or disproportionate. Physical symptoms — frequent illness, chronic pain, digestive disruption, heart palpitations — become prominent. This is dorsal vagal shutdown, as described in the first book in this series. The system has exhausted its capacity for sympathetic activation and has moved into conservation mode.",
                ]},
                {"heading": "Why Conventional Recovery Advice Fails", "body": [
                    "The standard advice for burnout — take a holiday, get more sleep, practice self-care — is not wrong, but it's insufficient for the third phase. The nervous system in collapse doesn't recover from a week off. It requires systematic rehabilitation, in the same way that a physically injured body requires specific rehabilitation rather than just rest.",
                    "The mistake is treating burnout as if it's simply accumulated fatigue that needs rest to resolve. In reality, the nervous system has undergone adaptive changes — altered cortisol rhythms, down-regulated sympathetic responsiveness, impaired prefrontal function — that don't reverse without deliberate intervention.",
                ]},
            ],
            "callout": "Burnout is not the consequence of caring too much. It's what happens when a body runs empty and keeps being asked to produce."
        },
        {
            "title": "The Recovery Sequence",
            "intro": "Recovery from burnout follows a sequence. Attempting to skip phases — going straight from collapse to productivity — reliably produces relapse. Understanding the sequence saves time.",
            "sections": [
                {"heading": "Phase One: Safety and Stabilisation", "body": [
                    "The first phase of recovery is about creating physiological safety. Not psychological reassurance — actual biological safety signals sent to the nervous system through consistent, predictable daily rhythms. Regular sleep and wake times. Regular meals. Minimal over-stimulation. Very gentle movement.",
                    "This phase feels slow and often unsatisfying because it doesn't produce visible results. You're not building strength or productivity. You're rebuilding the foundation. The analogy of a cracked structural wall is useful: you can paint over it, but the crack will return unless the foundation is repaired first.",
                    "Breathwork is the most accessible tool in this phase. The extended exhale breathing and coherent breathing from earlier books in this series are appropriate. Avoid high-intensity exercise, significant dietary changes, or any practice that adds physiological demand. The system is in triage. Give it conditions, not challenges.",
                ]},
                {"heading": "Phase Two: Gentle Reactivation", "body": [
                    "Once some stability has returned — sleep is somewhat consistent, acute physical symptoms are reducing, there are more functional hours in the day — it's appropriate to begin gentle reactivation of the system. This might look like short walks, light mobility work, brief social contact, small creative projects with no stakes attached.",
                    "The critical instruction in this phase is pacing. Burnout recovery has a characteristic pattern of boom-and-bust: a good day leads to overactivity, which leads to a crash, which leads to frustration, which leads to another push. Breaking this cycle requires deliberately doing less than you feel capable of on good days — banking the capacity rather than spending it immediately.",
                ]},
                {"heading": "Phase Three: Rebuilding Capacity", "body": [
                    "Phase three is where genuine rebuilding happens. Gradually increasing exercise intensity, returning to work or meaningful activity in measured doses, reintroducing challenge without recreating the conditions that led to collapse.",
                    "The questions worth sitting with at this phase: What in the original environment produced the burnout? What structural changes — to workload, schedule, relationships, expectations — would make a recurrence less likely? Burnout recovery without environmental change produces burnout recurrence. The nervous system cannot heal in the same conditions that injured it.",
                ]},
            ],
            "callout": "Recovery is not weakness. Pacing is not giving up. Rebuilding slowly is the only way to rebuild that lasts."
        },
        {
            "title": "The Burnout Body — Specific Somatic Work",
            "intro": "Burnout has a characteristic body signature. This chapter addresses that specific physical territory.",
            "sections": [
                {"heading": "The Collapsed Posture", "body": [
                    "Burnout produces a recognisable posture: shoulders forward, head dropped, spine curved, chest compressed. This is the dorsal vagal posture — the physical expression of shutdown. It both reflects and reinforces the underlying state.",
                    "Gentle postural work — not aggressive correction, but deliberate expansion — sends opposite signals. Wall angels: stand with your back against a wall, feet slightly away, and slowly raise and lower your arms in a snow-angel motion, maintaining contact with the wall throughout. Two sets of ten, done slowly. The opening of the chest and upper back activates different proprioceptive signals than the collapsed posture.",
                ]},
                {"heading": "Fatigue vs. Rest Deficits", "body": [
                    "An important distinction in burnout recovery: there are different types of rest. Physical rest (sleep, lying down) addresses physical fatigue. Mental rest addresses cognitive overload. Sensory rest addresses overstimulation. Emotional rest addresses the exhaustion of managing others' emotions. Creative rest addresses depletion of imagination and generativity.",
                    "Most burnout sufferers have deficits in multiple types simultaneously. A holiday that involves managing family dynamics, constant social stimulation, and a packed schedule addresses physical rest but deepens emotional and sensory deficits. Genuine recovery requires identifying which rest types are most depleted and addressing those specifically.",
                ]},
                {"heading": "Body-Based Practices for Burnout Recovery", "body": [
                    "Restorative yoga — specifically postures held for three to five minutes with full support from props (blankets, bolsters) — activates the parasympathetic system without requiring physical effort. Legs-up-the-wall pose (viparita karani) is the single most frequently recommended posture by somatic therapists for burnout: lie on your back and rest your legs up against a wall for five to fifteen minutes. The mild inversion calms the nervous system and reduces cortisol measurably.",
                    "Weighted blankets or firm physical pressure (a hand pressed firmly on the sternum, or the forehead pressed lightly against a surface) activates deep pressure receptors that have a reliably calming effect on the autonomic nervous system. This is the same mechanism as therapeutic touch and weighted therapy blankets used in occupational therapy.",
                ]},
            ],
            "callout": "The body that burned out needs a fundamentally different relationship with effort. Not less effort forever — just a different starting point."
        },
        {
            "title": "What Sustainable Looks Like",
            "intro": "Recovery from burnout is an opportunity most people don't fully use. This chapter is about using it.",
            "sections": [
                {"heading": "Redesigning the Conditions", "body": [
                    "Recovery without change is preparation for recurrence. The nervous system that burned out did so in a specific context — a specific job structure, relational dynamic, sleep pattern, workload expectation, or combination of these. Before returning to full function, it's worth conducting a clear-eyed inventory of which conditions contributed most to the burnout and which of them can actually change.",
                    "Some conditions are external and changeable: work hours, job role, physical environment, commute. Some are internal and changeable with work: perfectionism, difficulty delegating, inability to say no, chronic over-responsibility. Some may not be changeable in the short term. Understanding the difference allows for realistic planning rather than either passivity or futile effort.",
                ]},
                {"heading": "Early Warning System", "body": [
                    "Most people, in retrospect, can identify signs that were present six to twelve months before they fully burned out. The challenge is that those signs are easy to dismiss when you're in the middle of a busy life. Building a personal early warning system — a set of two or three specific, observable indicators that signal your system is under unmanageable pressure — creates the opportunity to intervene earlier next time.",
                    "Early warning signs tend to be individual. For some people it's sleep: three nights of poor sleep in a row is a signal. For others it's social withdrawal: cancelling plans without wanting to. For others it's physical: a specific kind of jaw tension, or recurring headaches. Know your signs. When they appear, treat them as information rather than inconvenience.",
                ]},
            ],
            "callout": "The goal is not to become someone who doesn't burn out because they feel less. It's to become someone who reads their body accurately enough to stop before collapse."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 05
# ─────────────────────────────────────────────────────────────────────────────
BOOK_05 = {
    "title": "Sleep & the Nervous System",
    "subtitle": "How to Turn Off Night Vigilance for Good",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "Why Your Nervous System Won't Let You Sleep",
            "intro": "For most people who struggle with sleep, the problem isn't an inability to fall asleep — it's an inability to feel safe enough to fall asleep. The nervous system that's on watch all day doesn't automatically switch off at night. It needs specific signals that the watch is over.",
            "sections": [
                {"heading": "Night Vigilance and Its Origins", "body": [
                    "Night vigilance is the nervous system's tendency to remain partially activated during nighttime hours — scanning for threats, processing unresolved stress from the day, anticipating tomorrow's demands. For most people who sleep poorly, the issue is not a broken sleep mechanism. It's a nervous system that genuinely cannot determine whether it's safe to stop monitoring.",
                    "This pattern has deep evolutionary roots. Nighttime is when predators hunt. Sleeping deeply and completely in an unsafe environment is dangerous. The nervous system's preference for light, easily-disrupted sleep in threatening conditions is a feature, not a bug. The problem is that it can't always tell the difference between genuine threat and the ambient, persistent stress of modern life.",
                    "Chronic stress, anxiety, trauma, and burnout all produce elevated night vigilance. So does anything that keeps the sympathetic system activated close to bedtime: bright screens, emotionally demanding content, unresolved conflicts, work that follows you to bed on your phone.",
                ]},
                {"heading": "The Biology of Sleep Architecture", "body": [
                    "Sleep is not a uniform state. It cycles through stages: light sleep (N1 and N2), deep slow-wave sleep (N3), and REM sleep, in roughly ninety-minute cycles. Each stage serves different functions. Slow-wave sleep is when physical repair, immune function, and memory consolidation happen. REM sleep is when emotional processing, threat simulation, and creative integration occur.",
                    "Night vigilance disrupts this architecture. It tends to reduce slow-wave sleep and fragment REM, producing the subjective experience of sleeping but not feeling rested — waking feeling as though you never went deep. The nervous system regulation practices in this book are specifically aimed at the conditions that produce this fragmentation.",
                ]},
            ],
            "callout": "Sleep is not something you do. It's something you create the conditions for."
        },
        {
            "title": "The Pre-Sleep Nervous System Protocol",
            "intro": "The hour before sleep is the most important hour for sleep quality. What you do — and don't do — in that window determines whether your nervous system can make the transition into genuine rest.",
            "sections": [
                {"heading": "Creating the Wind-Down Sequence", "body": [
                    "The nervous system needs a transition — a gradual dimming rather than an abrupt switch. An evening wind-down sequence is not a rigid ritual but a set of deliberate conditions that signal to the nervous system that the active part of the day is done and rest is coming.",
                    "The core elements: reduced light exposure in the sixty minutes before bed (dim lighting, or blue-light filtering if using screens), reduced temperature (the body needs to drop core temperature by 1–2°F to initiate sleep onset), reduced cognitive load (no emails, news, or anything requiring problem-solving), and a consistent transition activity that the nervous system begins to associate with sleep.",
                    "Consistency is more important than perfection. A wind-down that happens at roughly the same time most nights creates a conditioned response — the nervous system begins to shift into lower activation at the accustomed time, even before you've done anything deliberate.",
                ]},
                {"heading": "Breathwork for Sleep Onset", "body": [
                    "The extended exhale breathing from the first book in this series is the most evidence-supported single technique for reducing sleep onset latency. Lying in bed, breathing in for four counts and out for seven to eight counts, for five to ten minutes, reduces heart rate, increases HRV, and shifts the autonomic system toward parasympathetic dominance — the conditions sleep requires.",
                    "A variation specifically for 3am waking: the 4-7-8 breath (in for 4, hold for 7, out for 8). The longer hold and extended exhale produce a strong parasympathetic response that can interrupt the cortisol spike that often underlies early morning waking. Most people find that two to three cycles of 4-7-8 breathing is sufficient to return to sleep if the waking has not been longer than ten to fifteen minutes.",
                ]},
                {"heading": "Progressive Relaxation for Night Vigilance", "body": [
                    "Lying in bed, work systematically through the body using the condensed PMR technique from the second book: feet, calves, thighs, belly, hands and arms, shoulders, face. Hold each contraction for five seconds, then release completely. By the time you reach the face, most people are significantly more relaxed than when they started, and many are asleep before they finish.",
                    "The physiological mechanism is straightforward: the muscular tension-release cycle sends clear, concrete relaxation signals to the brainstem, which begins reducing arousal. Unlike counting sheep or trying to empty the mind, this gives the nervous system something specific and somatic to engage with, which prevents the ruminative spiral that often accompanies lying awake.",
                ]},
            ],
            "callout": "The body knows how to sleep. Your job is to stop accidentally convincing it that now isn't the right time."
        },
        {
            "title": "Managing Night Waking",
            "intro": "Waking between 2am and 4am is one of the most common and distressing sleep complaints. Understanding what's driving it changes the response to it.",
            "sections": [
                {"heading": "The 3am Cortisol Spike", "body": [
                    "Early morning waking — typically between 2am and 5am — is often driven by a premature cortisol surge. Cortisol is supposed to begin rising around 4–5am as part of the circadian awakening response. In people with disrupted cortisol rhythms (common in chronic stress, burnout, and HPA axis dysregulation), this surge happens too early, pulling the person out of sleep.",
                    "This is physiologically different from difficulty falling asleep. Difficulty falling asleep is usually about insufficient parasympathetic activation at sleep onset. Early morning waking is about a cortisol system that's out of calibration. The treatments differ accordingly.",
                    "For the cortisol-driven early waking, the most useful interventions are: consistent sleep and wake times (including weekends) to stabilise the circadian rhythm, avoiding high-cortisol experiences in the hours before bed, and the breathwork techniques described above to calm the cortisol spike when waking occurs.",
                ]},
                {"heading": "The Waking Mind", "body": [
                    "One of the most unhelpful things about nighttime waking is the quality of thinking that occurs in it. Worries that are manageable in the daylight become catastrophic at 3am. This is partly neurological: in the middle of the night, the prefrontal cortex is less active and the amygdala is relatively more dominant, producing threat-biased thinking.",
                    "Knowing this changes the relationship to night thoughts. They are not accurate assessments of your situation — they are the output of an amygdala running the show without appropriate prefrontal modulation. They don't deserve the same credence as your daytime thinking. Naming this explicitly — 'this is 3am thinking, not accurate thinking' — combined with the breathwork, is often sufficient to break the spiral.",
                ]},
            ],
            "callout": "The thoughts you have at 3am are not the truth. They're the fear. There's a difference."
        },
        {
            "title": "The Sleep Environment and Circadian Rhythm",
            "intro": "External conditions either support or undermine everything the nervous system is trying to do at night.",
            "sections": [
                {"heading": "Light, Temperature, and Sound", "body": [
                    "The three most powerful environmental levers for sleep are light, temperature, and sound. Light is the primary synchroniser of the circadian rhythm — bright light in the morning sets the clock forward; bright light in the evening delays sleep onset. Getting ten to twenty minutes of natural morning light within an hour of waking is one of the single most effective free interventions for sleep quality.",
                    "Temperature: the ideal sleep environment is between 65–68°F (18–20°C). A cooler room facilitates the drop in core body temperature that sleep initiation requires. A warm shower or bath one to two hours before bed paradoxically helps — the peripheral vasodilation it produces speeds the subsequent drop in core temperature.",
                    "Sound: consistent ambient sound (white noise, pink noise, or natural sound) is more sleep-conducive than attempting absolute silence, because absolute silence makes any sudden sound more jarring. A consistent sound environment reduces the acoustic vigilance that partial waking produces.",
                ]},
                {"heading": "Caffeine, Alcohol, and Sleep Architecture", "body": [
                    "Caffeine has a half-life of five to seven hours in most adults. A coffee at 2pm still has 50% of its caffeine active at 8–9pm, and that residual caffeine disrupts deep slow-wave sleep even when it doesn't prevent sleep onset. You might fall asleep without difficulty and still lose a significant portion of slow-wave sleep due to afternoon caffeine.",
                    "Alcohol is sleep-disruptive in a way that's counterintuitive because it reliably induces sleep onset. The problem is what happens after: alcohol disrupts REM sleep in the second half of the night, produces rebound sympathetic activation as it metabolises (typically three to four hours after consumption), and suppresses the slow-wave sleep that does the most physical repair. A drink before bed borrows from tomorrow's recovery.",
                ]},
            ],
            "callout": "You can't override biology with willpower. You can work with it."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 06
# ─────────────────────────────────────────────────────────────────────────────
BOOK_06 = {
    "title": "Somatic Tools for Grief",
    "subtitle": "Processing Loss Through the Body",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "Grief Lives in the Body",
            "intro": "Grief has a physical address. It lives in the chest — that actual ache that isn't metaphor. In the throat. In the heaviness of limbs that don't want to move. In the inability to eat, or the inability to stop eating. The body knows about loss in ways that precede language, and healing grief requires meeting it where it actually lives.",
            "sections": [
                {"heading": "What Grief Does to the Nervous System", "body": [
                    "Loss activates the nervous system in ways that are physiologically significant. Research by George Bonanno and others has shown that grief produces measurable changes in cortisol levels, immune function, sleep architecture, cardiovascular activity, and inflammatory markers. These are not psychosomatic — they are direct biological responses to the disruption of an attachment bond.",
                    "The autonomic nervous system experiences grief as a safety threat. When someone we are attached to — or something we are attached to, including a role, a future, a home — is no longer present, the nervous system loses a regulatory resource. We co-regulate with people we love. Their presence, their voice, their physical warmth help maintain our own nervous system stability. When they're gone, the system has to find new equilibrium. That process is what grief is, partly.",
                    "This is why grief can produce symptoms that look like anxiety (the searching, the hypervigilance, the scanning for the person who isn't there), symptoms that look like depression (the shutdown, the flatness, the withdrawal), and symptoms that look like physical illness (fatigue, pain, lowered immunity). It is all of these things and none of them, exactly. It is the nervous system reorganising itself around an absence.",
                ]},
                {"heading": "The Problem with Grief That Gets Stuck", "body": [
                    "Grief moves. When it's allowed to, it moves through waves — intense activation followed by rest, activation followed by rest. The physiological stress response rises, peaks, and passes. Over time, the waves become less frequent and less overwhelming, and the nervous system integrates the loss.",
                    "Grief gets stuck when the waves are not allowed to complete. When crying is suppressed, when the physical activation of grief is interrupted by the need to be functional, when there is not enough safety or time to feel the feelings — the stress response activates but doesn't discharge, and the grief doesn't move. It becomes stored tension, frozen activation, chronic low-level distress.",
                    "Somatic tools for grief are not about processing grief faster or bypassing the pain. They're about creating conditions where the physiological activation of grief can complete — so it can move, rather than become lodged.",
                ]},
            ],
            "callout": "Grief is not a problem to solve. It's a process to support."
        },
        {
            "title": "Creating Safety for Grief",
            "intro": "Before any processing can happen, there has to be enough safety. This is the foundation everything else rests on.",
            "sections": [
                {"heading": "Titration — Working in Small Doses", "body": [
                    "One of the most important concepts in somatic grief work is titration — working with grief in small, manageable doses rather than trying to feel everything at once. Full immersion in grief can be retraumatising and doesn't actually accelerate processing. Small doses, followed by returns to a stable baseline, are how the nervous system learns to tolerate and integrate loss.",
                    "Practical titration: set a time container. Allow yourself to feel fully for twenty minutes — with whatever physical expression the grief calls for: crying, moving, making sound — then stop, do a grounding practice, and return to ordinary activity. This is not suppression. It's paced engagement.",
                ]},
                {"heading": "Pendulation — Between Grief and Resource", "body": [
                    "Pendulation is a concept from Somatic Experiencing — the practice of deliberately moving attention between the site of pain and a resource. A resource, in this context, is anything that feels genuinely supportive: a memory of the person who is gone, a physical sensation of comfort, a place in the body that doesn't hurt, a sensory experience that brings even a mild sense of okayness.",
                    "Moving attention back and forth between the grief and the resource — rather than staying immersed in the grief — allows the nervous system to process without being overwhelmed. It teaches the system that it can touch the pain and return from it.",
                ]},
            ],
            "callout": "You don't have to carry grief alone and you don't have to face it all at once."
        },
        {
            "title": "Somatic Practices for Active Grief",
            "intro": "These practices are for the acute phases of grief — the times when the body is activated and needs support in moving through rather than getting stuck.",
            "sections": [
                {"heading": "Allowing the Cry", "body": [
                    "Crying is a physiological discharge mechanism. It releases stored tension, activates the parasympathetic system, and produces a specific neurochemical response — including the release of oxytocin — that produces the paradoxical sense of relief that often follows a full cry.",
                    "Many people suppress crying reflexively — particularly in public, or in the presence of others who are uncomfortable with it. Practising allowing the cry in private, with full physical expression — sound, movement, letting the face do what it wants to do — can be a genuine release mechanism for grief that has been held.",
                    "Creating a cry container: dim light, privacy, a pillow or blanket, and perhaps music that opens the channel. Allow ten to twenty minutes. Then ground: feet on floor, several slow breaths, something warm to drink.",
                ]},
                {"heading": "Movement for Grief Energy", "body": [
                    "Grief produces physical activation that needs movement. The restlessness, the inability to sit still, the urge to pace — these are the nervous system trying to discharge mobilised energy that doesn't have anywhere to go.",
                    "Walking, particularly slow walking in nature or another quiet environment, is one of the most consistent somatic grief tools because it matches the natural rhythm of grief waves — moving through them rather than trying to stop them. The bilateral movement of walking also has a gentle processing effect, similar to the bilateral stimulation used in EMDR.",
                    "Expressive movement — moving the body however it wants to move, without structure or performance — can be a powerful discharge tool for grief, particularly for people who find talking about their feelings less accessible than moving through them.",
                ]},
                {"heading": "The Body Holds the Connection", "body": [
                    "One aspect of somatic grief work that is rarely discussed is the way the body holds our connection to those we've lost. Smell is particularly powerful — it bypasses the cognitive brain and goes directly to the limbic system, producing the vivid, immediate memory response that a rational description cannot. Holding an object belonging to someone who has died, returning to a place that carries their presence — these sensory engagements are not morbid or unhealthy. They are ways the nervous system maintains connection while simultaneously processing loss.",
                ]},
            ],
            "callout": "What the body loved, the body grieves. Give it the space to do so."
        },
        {
            "title": "Living Forward",
            "intro": "Grief changes over time. Not by becoming smaller, exactly, but by changing shape — and by the rest of life gradually growing larger around it.",
            "sections": [
                {"heading": "Continuing Bonds", "body": [
                    "Modern grief research, particularly the work of Klass, Silverman, and Nickman, has challenged the older view that healthy grief requires 'letting go' and severing the bond with the person who has died. The research suggests that maintaining an ongoing, transformed relationship with the deceased — talking to them, carrying their values, feeling their presence in meaningful places — is associated with better grief outcomes, not worse ones.",
                    "Somatic practices can support this: creating a physical ritual of connection, keeping sensory anchors, returning to places that held shared meaning. These are not signs of inability to move forward. They are ways of carrying love across the boundary of loss.",
                ]},
                {"heading": "When to Seek Support", "body": [
                    "Grief that is complicated — particularly when it involves traumatic loss, sudden loss, suicide bereavement, or when it is not moving at all after many months — generally requires professional support. Complicated grief disorder is a real clinical presentation that responds well to specific therapeutic approaches, including somatic therapies.",
                    "If grief is preventing you from functioning, eating, sleeping, or finding any moments of relief after several months, please seek support. This is not a sign of weakness. It is a sign that the loss was enormous and the nervous system needs more than individual practice to process it.",
                ]},
            ],
            "callout": "Love doesn't end when someone dies. It finds a different form. Grief is what it feels like while the transformation is happening."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 07
# ─────────────────────────────────────────────────────────────────────────────
BOOK_07 = {
    "title": "The ADHD Nervous System",
    "subtitle": "A Somatic Approach to Focus and Calm",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "ADHD Is a Nervous System Difference",
            "intro": "ADHD is not a deficit of attention. It's a difference in how the nervous system regulates attention, motivation, emotion, and activation. Understanding it this way — as a fundamentally different regulatory system rather than a broken version of a neurotypical one — changes everything about how you work with it.",
            "sections": [
                {"heading": "The ADHD Nervous System in Plain Language", "body": [
                    "The ADHD nervous system is interest-based, not importance-based. Neurotypical nervous systems can activate for tasks based on perceived importance, obligation, or deadline — even when those tasks are not interesting. The ADHD nervous system activates most reliably for tasks that are interesting, urgent, novel, or personally meaningful. Everything else is a struggle — not because of laziness or poor character, but because of a difference in the dopamine-driven motivation circuitry.",
                    "Dr Edward Hallowell and Dr John Ratey, two of the most respected ADHD researchers and clinicians, describe the ADHD nervous system as inconsistent rather than deficient. It's not that focus is always unavailable — many people with ADHD have hyperfocus states where they can concentrate for hours on something genuinely engaging. The problem is control: the inability to reliably direct focus, rather than the absence of focus itself.",
                    "Emotionally, the ADHD nervous system is more reactive than neurotypical ones. Rejection sensitive dysphoria (RSD), described by William Dodson, is the experience of intense emotional pain triggered by perceived criticism or rejection. For many people with ADHD, this is actually the most impairing aspect of the condition — more than the focus difficulties.",
                ]},
                {"heading": "The Dysregulated ADHD Nervous System", "body": [
                    "Without appropriate support, the ADHD nervous system tends toward two poles: under-activated (bored, flat, unable to start) and over-activated (overwhelmed, flooded, unable to stop). The transitions between these states, and the time spent at the extremes, produce enormous nervous system strain over time.",
                    "Many adults with ADHD — particularly those who were never diagnosed or who relied on coping mechanisms — arrive at midlife with nervous systems that are simultaneously depleted and dysregulated. The chronic effort of managing a system that works differently from the expected norm, in environments designed for neurotypical regulation, creates a specific kind of burnout that standard burnout literature doesn't quite capture.",
                ]},
            ],
            "callout": "The ADHD nervous system is not broken. It's a Ferrari engine in a body that was handed sedan instructions."
        },
        {
            "title": "Somatic Regulation for ADHD",
            "intro": "The body is one of the most accessible regulation tools for the ADHD nervous system — and one of the most underutilised.",
            "sections": [
                {"heading": "Movement as Regulation, Not Reward", "body": [
                    "Exercise is one of the most evidence-supported interventions for ADHD. John Ratey's research has shown that aerobic exercise produces dopamine, norepinephrine, and serotonin increases that are functionally similar to the effect of stimulant medication — without the side effects, and with additional benefits for neuroplasticity.",
                    "For the ADHD nervous system, movement is not a reward for completing tasks. It's a regulatory input that makes task completion possible. Scheduling movement before demanding cognitive work — rather than after — is a practical application of this: fifteen to twenty minutes of aerobic activity before a period of focused work consistently improves executive function in ADHD.",
                ]},
                {"heading": "Fidgeting as a Regulation Tool", "body": [
                    "Fidgeting has historically been treated as a symptom to suppress. Research by Dustin Sarver and others has challenged this: fidgeting in children with ADHD is associated with better working memory performance on difficult tasks. The physical movement activates the nervous system sufficiently to improve cognitive performance.",
                    "Practical application: have a designated fidget tool for focused work — a stress ball, a spinner ring, textured surfaces. Stand while working if possible. Pace during phone calls. Allow the physical movement that the nervous system is requesting rather than trying to suppress it.",
                ]},
                {"heading": "Breathwork for ADHD Transitions", "body": [
                    "Transitions are among the most difficult moments for ADHD nervous systems — ending one activity and beginning another, shifting cognitive modes, moving between environments. The executive function required for smooth transitions is exactly what ADHD impairs.",
                    "A brief breathwork practice at transition points creates a physiological pause that supports the executive function shift: three physiological sighs before switching tasks, box breathing for two minutes before starting a difficult project, or a brief body scan when arriving home from work. These thirty-second to two-minute practices function as transition bridges — they interrupt the momentum of one state and create space to enter the next.",
                ]},
            ],
            "callout": "For the ADHD nervous system, the body is often the most direct path to the mind."
        },
        {
            "title": "Working With the Interest-Based System",
            "intro": "Fighting the interest-based ADHD nervous system is exhausting and largely ineffective. Working with it is faster and less demoralising.",
            "sections": [
                {"heading": "Body Doubling and Co-Regulation", "body": [
                    "Body doubling — the practice of working in the presence of another person, even without interaction — is one of the most widely used ADHD regulation strategies and one of the least scientifically studied despite overwhelming anecdotal support. The presence of another person activates the social engagement system (ventral vagal), which appears to support executive function and reduce the nervous system dysregulation that makes starting difficult.",
                    "This is why ADHD people often work better in coffee shops, co-working spaces, or on video calls with a friend. The social regulatory input from another nervous system stabilises the ADHD one sufficiently to make initiation possible.",
                ]},
                {"heading": "Sensory Environments for ADHD Focus", "body": [
                    "The ADHD nervous system responds strongly to sensory environment. The right sensory input can be regulatory; the wrong kind can tip the system into overwhelm or boredom. Finding your specific sensory profile — whether you work better with background music or silence, warm or cool environments, dimmer or brighter light, more or less physical movement — is a practical regulation tool.",
                    "Many people with ADHD work well with music that has a consistent beat and no lyrics (film scores, electronic, classical) because it provides a steady rhythmic input that keeps the nervous system from seeking stimulation elsewhere. Others need silence. There's no universal answer — the answer is your answer, found through deliberate experimentation.",
                ]},
            ],
            "callout": "The ADHD nervous system will always seek interest. Your job is to become the architect of that interest, not its victim."
        },
        {
            "title": "Managing the Emotional Intensity",
            "intro": "The emotional dimension of ADHD is, for many people, the hardest part.",
            "sections": [
                {"heading": "Rejection Sensitive Dysphoria", "body": [
                    "RSD produces sudden, intense emotional pain in response to perceived criticism, rejection, or failure. The operative word is perceived — the triggering event does not need to be objectively rejecting. A neutral tone in an email, an unreturned call, an unintentional slight — these can produce emotional responses that are disproportionate in intensity and genuinely debilitating.",
                    "Somatic tools for RSD: when the emotional intensity arrives, ground immediately — feet on floor, physiological sigh, cold water on face if available. This is not suppression. It's reducing the acute intensity enough to allow choice. The emotion is real and valid. The goal is to give the prefrontal cortex a chance to come online before responding.",
                ]},
                {"heading": "After the Storm", "body": [
                    "ADHD emotional responses typically resolve as quickly as they arrive — another distinguishing feature from mood disorders, where the states are more sustained. After an intense emotional episode, the nervous system needs recovery time and physical reset: movement, warmth, water, and time to settle before re-engaging with the triggering situation.",
                    "Building in explicit recovery time after emotional intensity — not pushing immediately back into productivity — is not weakness. It's how the ADHD nervous system functions. Honour the recovery time and you spend less total time in the cycle.",
                ]},
            ],
            "callout": "You are not too sensitive. You have a nervous system that feels everything at full volume. That's different."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 08
# ─────────────────────────────────────────────────────────────────────────────
BOOK_08 = {
    "title": "Chronic Pain & the Nervous System",
    "subtitle": "A Mind-Body Reset Guide",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "Pain Is a Message, Not a Measurement",
            "intro": "Pain is not a faithful measurement of tissue damage. It's a signal produced by the brain — a protective output generated when the brain concludes that something requires attention. This distinction is not semantic. It changes everything about how chronic pain can be approached.",
            "sections": [
                {"heading": "The New Understanding of Pain", "body": [
                    "For most of the twentieth century, pain was understood as a simple input-output system: damaged tissue sends a danger signal, the brain registers it as pain. The intensity of pain was assumed to correspond to the extent of damage.",
                    "This model has been comprehensively challenged by modern pain neuroscience. Lorimer Moseley and David Butler, among others, have demonstrated that pain is an output of the brain, not an input from the body — a protective response generated when the brain perceives threat, regardless of whether tissue damage is present or proportionate to the pain experienced.",
                    "This explains findings that previously seemed inexplicable: phantom limb pain (pain in a limb that no longer exists), the fact that many people with severe structural changes on MRI have no pain while others with minimal findings have disabling pain, and the well-documented phenomenon of nocebo — pain that increases when patients are told something is wrong with them, even when nothing has changed structurally.",
                ]},
                {"heading": "Central Sensitisation", "body": [
                    "In chronic pain, the nervous system itself becomes sensitised — the alarm system turns up its sensitivity, producing pain from inputs that would not normally register as painful and amplifying those that would. This is called central sensitisation, and it's the primary mechanism in conditions like fibromyalgia, chronic widespread pain, and many presentations of chronic back and neck pain.",
                    "Understanding central sensitisation changes the treatment target. The problem is not (only) in the tissues. It's in the sensitivity of the nervous system itself. And the nervous system responds to exactly the kinds of practices described throughout this series — with modifications for chronic pain contexts.",
                ]},
            ],
            "callout": "Pain is real. It is not imagined. But it is also not an accurate GPS reading of where the damage is or how bad it is."
        },
        {
            "title": "Calming the Sensitised System",
            "intro": "A sensitised nervous system cannot be argued with. It can be gradually recalibrated.",
            "sections": [
                {"heading": "Safety Signals for a Pain-Sensitised Nervous System", "body": [
                    "The brain increases pain output when it concludes that the body is in danger. Reducing pain, over time, involves increasing the brain's sense of safety — through information, experience, and physiological input. Education itself has been shown to reduce pain: understanding that chronic pain is a sensitisation phenomenon rather than evidence of ongoing damage reduces the threat value the brain assigns to the sensation, which reduces the pain output.",
                    "Breathwork, gentle movement, social connection, and positive sensory experiences all send safety signals to the pain-producing systems. They don't override the pain immediately. But over time, consistent safety inputs recalibrate the system's threat assessment.",
                ]},
                {"heading": "Movement Despite Pain — The Graded Approach", "body": [
                    "Avoiding movement in chronic pain feels logical — moving hurts, so don't move. But the evidence is clear that movement avoidance strengthens the central sensitisation cycle. The nervous system interprets movement avoidance as confirmation that movement is dangerous, which maintains and often increases pain sensitivity.",
                    "Graded motor imagery and graded exposure to movement, developed by Moseley and others, involve gradually introducing movement in small, non-threatening increments — beginning with imagining movement before performing it, starting with very small ranges of motion, and incrementally expanding. The goal is to provide evidence to the brain that movement is safe.",
                ]},
                {"heading": "Breathwork and Pain Perception", "body": [
                    "Slow, diaphragmatic breathing reliably reduces pain perception through multiple mechanisms: it activates the parasympathetic system, reduces cortisol and adrenaline (which amplify pain), and shifts attention. Research consistently shows that breathwork reduces both self-reported pain intensity and the neural signatures of pain on brain imaging.",
                    "Coherent breathing (five breaths per minute, as described in the second book) is particularly well-studied for pain conditions. Consistent daily practice over weeks to months produces lasting changes in pain sensitivity through its effects on HRV and vagal tone.",
                ]},
            ],
            "callout": "The nervous system learns. It learned to amplify pain. With the right inputs, it can learn to turn down the volume."
        },
        {
            "title": "The Emotional Dimension of Chronic Pain",
            "intro": "Chronic pain and emotional pain share neural pathways. This is not a metaphor.",
            "sections": [
                {"heading": "Adverse Experiences and Pain", "body": [
                    "The ACE (Adverse Childhood Experiences) study found a strong dose-response relationship between the number of adverse childhood experiences and the likelihood of chronic pain conditions in adulthood. Other research has replicated this finding across multiple pain conditions.",
                    "This is not saying that chronic pain is 'all in the head' or is imagined. It is saying that the nervous system that developed under adversity developed different threat-sensitivity calibrations, which over time express in pain responses. The biological pathway from early adversity to chronic pain runs through the nervous system, the HPA axis, and inflammatory pathways — all real, all measurable.",
                ]},
                {"heading": "Trauma-Informed Approaches to Chronic Pain", "body": [
                    "Working with chronic pain from a nervous system perspective often means working with the emotional history that shaped the nervous system's sensitivity. This doesn't require reliving trauma or psychologising physical symptoms. It means creating enough nervous system safety to allow the system to recalibrate.",
                    "Somatic Experiencing, TRE, and EMDR have all shown promise in research contexts for chronic pain conditions, particularly where trauma or adverse experience is part of the history. A trauma-informed physiotherapist or pain psychologist trained in these approaches is worth seeking if chronic pain is your primary concern.",
                ]},
            ],
            "callout": "The body has its reasons. Understanding them is not the same as agreeing that the pain is inevitable."
        },
        {
            "title": "A Daily Practice for Chronic Pain",
            "intro": "Chronic pain management through nervous system regulation is a long game. The practices are simple; the commitment is sustained.",
            "sections": [
                {"heading": "The Core Daily Practice", "body": [
                    "For chronic pain specifically, the daily practice prioritises safety and consistency over intensity. Ten minutes of coherent breathing morning and evening. One brief period of gentle graded movement. One practice of deliberate engagement with positive sensation — not to override the pain, but to give the nervous system evidence that not everything is threatening.",
                    "The positive sensation practice is often overlooked. A warm shower attended to with full sensory attention. A cup of tea savoured. A brief period of being in a comfortable position and noticing what feels okay in the body, rather than scanning for what doesn't. These small interventions shift the data the brain is working with.",
                ]},
                {"heading": "Pacing and Energy Management", "body": [
                    "Chronic pain is often accompanied by fatigue and a boom-bust activity pattern that amplifies both. Pacing — doing a consistent, moderate level of activity rather than alternating between overdoing and crashing — is the evidence-based approach to managing the energy economics of chronic pain.",
                    "The aim is to find the activity level that can be sustained consistently without producing flare-ups, then gradually and incrementally expand from there. This is slower than the instinctive approach (push through the good days, collapse on the bad ones) but produces more consistent function over time.",
                ]},
            ],
            "callout": "Managing chronic pain is not about willpower over pain. It's about intelligence applied to the system that produces it."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 09
# ─────────────────────────────────────────────────────────────────────────────
BOOK_09 = {
    "title": "Trauma Release for Beginners",
    "subtitle": "Simple Somatic Practices You Can Do at Home",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "What Trauma Actually Is",
            "intro": "Trauma is not what happened to you. It's what happened inside you as a result of what happened. This distinction, from Gabor Maté, is one of the most useful reframes in modern trauma understanding — because it shifts the focus from the event to the response, and the response is where healing lives.",
            "sections": [
                {"heading": "Big T and Little t Trauma", "body": [
                    "When most people hear the word trauma, they think of specific catastrophic events: combat, assault, serious accidents, natural disasters. This is what clinicians call big-T trauma. But the concept of small-t trauma — the accumulation of smaller, less dramatic experiences that nonetheless overwhelm the nervous system's capacity to process and integrate — has become increasingly central to understanding why so many people carry the physiological signatures of trauma without a single defining traumatic event.",
                    "Small-t trauma includes: chronic emotional neglect, persistent humiliation or criticism in childhood, unstable or unpredictable caregiving environments, experiences of powerlessness or helplessness that didn't involve physical danger, medical procedures undergone without adequate emotional support, and many others. These experiences, particularly when they occur early and repeatedly, shape the nervous system's threat sensitivity in lasting ways.",
                    "Peter Levine, whose work on somatic experiencing is foundational to this book, describes trauma as the result of an incomplete defensive response — a threat response that was mobilised but couldn't complete its intended action. The energy remains in the body as frozen activation.",
                ]},
                {"heading": "Trauma in the Body", "body": [
                    "Bessel van der Kolk's research, summarised in The Body Keeps the Score, has documented how trauma is stored in the body's systems — in altered stress hormone patterns, in the body map in the brain, in immune function, in posture, in the way breath moves. Brain imaging of people with PTSD shows not just changes in the emotional brain but changes in the body-sensing areas, the areas that construct our sense of physical self.",
                    "This is why talking about trauma has limits. Talking engages the verbal, cognitive parts of the brain. Trauma is stored in systems that don't have verbal access. Somatic approaches — working directly with the body, breath, movement, sensation — access these systems in ways that conversation can't.",
                ]},
            ],
            "callout": "Trauma is not a life sentence. It is a pattern of activation stored in the body, and the body can learn new patterns."
        },
        {
            "title": "Safety Before Processing",
            "intro": "This is the most important chapter in this book. Please read it before attempting any of the practices.",
            "sections": [
                {"heading": "Why Safety Comes First", "body": [
                    "Trauma processing that happens without adequate safety does not heal trauma — it retraumatises. The nervous system cannot process what it cannot tolerate experiencing. Pushing into trauma material before sufficient capacity has been built produces overwhelm, flooding, and often a temporary worsening of symptoms.",
                    "The practices in this book are designed for self-directed beginners. They are titrated and gentle. They are not a substitute for working with a trained trauma therapist for complex or severe presentations. If you have a history of significant trauma — particularly developmental trauma, severe PTSD, or a history of dissociation — please work with a qualified professional rather than, or in addition to, using this book.",
                ]},
                {"heading": "Building a Safety Foundation", "body": [
                    "Before engaging with any trauma-focused practice, spend at least one to two weeks establishing a solid grounding and regulation foundation using the practices from earlier books in this series: consistent breathwork, grounding exercises, and at least basic sleep hygiene. These build the nervous system capacity that trauma processing requires.",
                    "Also establish a reliable way to stop: if at any point during a practice you feel overwhelmed, flooded, dissociated, or unable to function, stop the practice immediately and ground: feet on floor, eyes open, slow breath, orienting to the room by naming five visible objects. This is your emergency exit and it's important to know it clearly before you begin.",
                ]},
            ],
            "callout": "Go only as fast as the slowest part of you can go."
        },
        {
            "title": "The Core Trauma Release Practices",
            "intro": "These practices are drawn from Somatic Experiencing, TRE, and related body-based approaches. They are adapted for safe self-directed use.",
            "sections": [
                {"heading": "Tracking Sensation", "body": [
                    "The most fundamental somatic skill in trauma work is tracking sensation — noticing physical sensations in the body without immediately moving to interpret or change them. This is harder than it sounds. The tendency is to move quickly from sensation to meaning: 'my chest is tight' → 'something is wrong' → 'I need to fix this'. Tracking interrupts this sequence at the first step.",
                    "Practice: sit quietly, close your eyes, and simply notice physical sensations in the body for five minutes. Where is there warmth? Tightness? Tingling? Heaviness? Openness? Don't analyze. Don't follow the story. Just track, the way you'd track weather through a window — observing without getting wet.",
                ]},
                {"heading": "Pendulation Practice", "body": [
                    "As described in the grief chapter, pendulation involves moving attention between a site of discomfort and a resource. In trauma work, this is the core processing tool. A resource can be a physical sensation of comfort, a memory of safety, a supportive person's face, a place in the body that feels neutral or pleasant.",
                    "Practice: identify a mild, manageable sensation associated with a stressful memory (not the worst thing — start with something small). Notice it in the body: where is it? What does it feel like? Now move attention completely to the resource. Stay there until you feel some settling. Then, briefly, to the stressor sensation. Then back to resource. Repeat. Each cycle processes a small amount of the activation without overwhelming the system.",
                ]},
                {"heading": "Completing the Defensive Response", "body": [
                    "Levine's approach to trauma processing often involves physically completing the defensive movement that was interrupted during the traumatic event. This is not about re-enacting the trauma — it's about allowing the body's impulse toward protective action to complete.",
                    "A simplified version: sit or lie comfortably. Bring gentle attention to a stressful memory. Notice if there's an impulse — however small — toward any particular movement. Perhaps a hand wants to push away. An arm wants to extend. The spine wants to curl. Allow the movement to happen in slow motion, extremely slowly, with full sensory attention. Let it complete. Then pause and notice what has changed in the body.",
                ]},
            ],
            "callout": "The body doesn't forget. But it can finish what it started."
        },
        {
            "title": "Building a Sustainable Practice",
            "intro": "Trauma work done well is slow. The pace that feels frustratingly slow is usually exactly right.",
            "sections": [
                {"heading": "How Often and How Long", "body": [
                    "For self-directed trauma-oriented somatic practice, less is often more. Daily short sessions (ten to fifteen minutes) are more appropriate than long occasional sessions. The nervous system needs time to integrate between sessions.",
                    "Signs that you're moving at the right pace: you feel slightly unsettled after sessions but return to baseline within a few hours. Signs that you're moving too fast: you feel significantly worse for days after a session, or you're experiencing intrusive thoughts, sleep disruption, or dissociation. If the latter, slow down dramatically and prioritise grounding practices.",
                ]},
                {"heading": "When Professional Support Is Essential", "body": [
                    "Self-directed somatic practice is appropriate for mild to moderate presentations and as a supplement to professional work. It is not appropriate as the primary intervention for PTSD, complex developmental trauma, trauma involving violence or sexual assault, or any presentation where symptoms are severe and significantly impacting function.",
                    "A trained somatic trauma therapist offers something no book can: real-time attunement to your nervous system state, the ability to adjust the pace and direction as you go, and the co-regulatory safety of a skilled therapeutic relationship. If you have significant trauma, please find a Somatic Experiencing practitioner, an EMDR therapist, or a trauma-informed therapist. The Somatic Experiencing International website maintains a practitioner directory.",
                ]},
            ],
            "callout": "Healing trauma is not a heroic solo journey. It's a relational process that often goes better in good company."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# BOOK 10
# ─────────────────────────────────────────────────────────────────────────────
BOOK_10 = {
    "title": "Somatic Healing for Perimenopause",
    "subtitle": "Managing Hormonal Anxiety Through the Body",
    "series_name": SERIES, "accent_hex": ACCENT, "bg_hex": BG,
    "disclaimer": DISCLAIMER_HEALTH,
    "chapters": [
        {
            "title": "When Your Nervous System Changes with Your Hormones",
            "intro": "Many women in perimenopause — the hormonal transition that typically begins in the late 30s or 40s, sometimes earlier — describe a sudden onset of anxiety that feels qualitatively different from anything they've experienced before. Not situational anxiety tied to a specific worry, but a nervous system agitation that seems to come from nowhere. This chapter explains why, because understanding it makes it less frightening.",
            "sections": [
                {"heading": "Estrogen and the Nervous System", "body": [
                    "Estrogen has direct effects on the nervous system that go far beyond reproductive function. It modulates neurotransmitter activity — including serotonin, dopamine, and GABA — and has anti-anxiety effects that are broadly protective. It supports the function of the hippocampus, the brain structure involved in memory and in regulating the stress response. It influences the myelination of neural pathways. It has anti-inflammatory properties in the brain.",
                    "During perimenopause, estrogen levels fluctuate irregularly — sometimes dramatically — before eventually declining. These fluctuations affect the nervous system directly. The anxiety, mood instability, brain fog, sleep disruption, and emotional reactivity that many women in perimenopause experience are not symptoms of psychological weakness. They are the direct neurological effects of a fluctuating hormone that has been keeping multiple systems in calibration for decades.",
                    "This is important because many women in perimenopause present to doctors with anxiety or mood symptoms and are referred to mental health treatment without the hormonal dimension being addressed. Both dimensions may need attention. But the hormonal piece is real and significant.",
                ]},
                {"heading": "The Specific Nervous System Presentations of Perimenopause", "body": [
                    "The anxiety of perimenopause has some characteristic features: it often presents as a physical sensation of internal vibration or agitation, it frequently worsens in the premenstrual phase of an irregular cycle, it is often accompanied by a new sensitivity to stimulation (noise, light, crowds), and it tends to peak in the years of most irregular hormone levels before improving once levels stabilise in postmenopause.",
                    "Night sweats are a direct nervous system event — a vasomotor response driven by disrupted thermoregulation that activates the sympathetic system in the middle of the night, producing the cortisol spike that underlies much perimenopausal insomnia. The night sweat itself is uncomfortable; the subsequent inability to return to sleep is a nervous system regulation problem.",
                    "Rage — sudden, intense, and often disproportionate — is another perimenopausal nervous system presentation that is rarely discussed with adequate honesty. The loss of estrogen's buffering effect on amygdala reactivity means that the emotional brake is less effective. This is not who you are. It's your nervous system under hormonal pressure.",
                ]},
            ],
            "callout": "What is happening to your nervous system in perimenopause is real, biological, and temporary. It also responds to the same things that have always helped regulate the nervous system — applied with more consistency and more compassion."
        },
        {
            "title": "Somatic Practices for Hormonal Anxiety",
            "intro": "The practices here are specifically adapted for the perimenopausal nervous system — which needs gentler, more consistent approaches and responds less well to high-intensity interventions that add physiological demand.",
            "sections": [
                {"heading": "Breathwork for Hot Flashes and Night Sweats", "body": [
                    "The physiological sigh — double inhale followed by a slow, complete exhale — is effective for interrupting the vasomotor cascade of a hot flash if used at the first sign of onset. When you notice the initial warmth, double inhale through the nose and release completely through the mouth. Repeat three to five times.",
                    "Several small studies have found that paced breathing at roughly six breaths per minute (coherent breathing) reduces the frequency and severity of hot flashes when practiced consistently. The mechanism is likely through HPA axis regulation — the same stress-response pathways that drive vasomotor symptoms are calmed by consistent vagal activation.",
                    "For night sweats: the 4-7-8 breath immediately upon waking helps interrupt the sympathetic activation that prolongs the waking episode. Combined with a consistently cool sleep environment and the sleep practices from Book 5 in this series, most women find significant improvement in sleep continuity.",
                ]},
                {"heading": "Grounding for Perimenopausal Anxiety Spikes", "body": [
                    "When perimenopausal anxiety spikes — the sudden, sourceless agitation that can arrive in the middle of an ordinary moment — grounding is the most effective immediate intervention. Feet firmly on the floor, deliberate sensory engagement with the environment, physiological sigh.",
                    "Cold water is particularly effective for the perimenopausal nervous system: splashing cold water on the face and wrists provides immediate vasomotor relief while also triggering the calming mammalian dive reflex. Keep a small spray bottle of cold water if you're in situations where this matters.",
                ]},
                {"heading": "Yoga Nidra for Hormonal Sleep Disruption", "body": [
                    "Yoga nidra — often called yogic sleep — is a guided relaxation practice that induces a hypnagogic state (between waking and sleep) through body scanning and visualisation. Multiple studies have found it effective for insomnia, and it appears particularly well-suited to perimenopausal sleep disruption because it works regardless of whether sleep occurs.",
                    "The key benefit: thirty to forty-five minutes of yoga nidra is associated with the equivalent restorative effect of two to four hours of sleep in some research. When genuine sleep is disrupted by night sweats or hormonal anxiety, yoga nidra offers a restorative alternative that doesn't require sleep onset. Recordings are freely available on YouTube and most meditation apps.",
                ]},
            ],
            "callout": "Your nervous system is adjusting to a new hormonal reality. Give it more support during the transition, not less."
        },
        {
            "title": "Supporting the Whole System",
            "intro": "Somatic practices are one dimension of perimenopausal support. This chapter addresses the others.",
            "sections": [
                {"heading": "Nutrition and the Perimenopausal Nervous System", "body": [
                    "The fluctuating estrogen of perimenopause increases inflammatory signalling and can disrupt blood sugar regulation — both of which directly affect nervous system stability. Dietary approaches that reduce inflammation and stabilise blood sugar are therefore directly relevant to perimenopausal anxiety and mood.",
                    "Protein at each meal (particularly leucine-rich sources: eggs, meat, fish, dairy) stabilises blood glucose and supports neurotransmitter synthesis. Omega-3 fatty acids (fatty fish, flaxseed, walnuts) reduce neuroinflammation. Magnesium (leafy greens, nuts, seeds, dark chocolate) supports GABA activity — the brain's natural calming neurotransmitter — and is frequently depleted in perimenopausal women.",
                    "Caffeine and alcohol are both more disruptive to the perimenopausal nervous system than they were earlier in life, due to changes in liver metabolism and increased nervous system sensitivity. Neither needs to be eliminated, but their effects are worth monitoring — particularly their impact on sleep and anxiety levels.",
                ]},
                {"heading": "Strength Training as Nervous System Support", "body": [
                    "Resistance training during perimenopause provides benefits that go well beyond muscle maintenance. It improves insulin sensitivity, reduces inflammatory markers, supports bone density (which begins declining with estrogen), and — particularly relevant here — has been shown to reduce anxiety and depression through mechanisms including BDNF (brain-derived neurotrophic factor) release and HPA axis regulation.",
                    "Two to three sessions per week of progressive resistance training is the evidence-based recommendation. This doesn't require a gym membership or heavy equipment — bodyweight resistance training (squats, push-ups, hinges, rows) produces the same hormonal and neurological benefits.",
                ]},
                {"heading": "When to Talk to a Doctor About HRT", "body": [
                    "The evidence base for hormone replacement therapy (HRT) has been substantially revised since the Women's Health Initiative study in the early 2000s. Current understanding, based on more recent research and the work of clinicians like Avrum Bluming, Christiane Northrup, and Mary Claire Haver, is that HRT is appropriate for many perimenopausal women — particularly those with significant symptoms — and that the risk profile is more favourable than was previously believed.",
                    "This book is not the appropriate place for a detailed HRT discussion, and any decision about hormonal treatment should be made with a qualified healthcare provider who is current on the evidence. The somatic and lifestyle practices in this book are appropriate alongside any treatment approach — they support the nervous system regardless of hormonal management strategy.",
                ]},
            ],
            "callout": "Perimenopause is not the beginning of decline. It is a transition with real challenges and real tools to meet them."
        },
        {
            "title": "The Other Side",
            "intro": "Perimenopause ends. Postmenopause has its own landscape, and it's worth knowing what to expect.",
            "sections": [
                {"heading": "Nervous System Stabilisation in Postmenopause", "body": [
                    "Once hormones stabilise at their postmenopausal levels — which typically happens within two to three years of the final menstrual period — many women report a significant reduction in the nervous system agitation of perimenopause. The anxiety that felt constant and sourceless often diminishes substantially. Sleep, while still sometimes a challenge, becomes more predictable.",
                    "The nervous system practices built during the perimenopausal transition become even more valuable postmenopausally — as prevention and maintenance rather than crisis management. The reduced estrogen environment means the nervous system is slightly more vulnerable to stress activation than it was during the reproductive years, but a consistently practiced regulation toolkit provides significant compensation.",
                ]},
                {"heading": "What Stays and What Changes", "body": [
                    "The intense vasomotor symptoms of perimenopause typically reduce significantly in postmenopause. The sleep disruption usually improves. The anxiety and mood volatility that tracked estrogen fluctuations tends to stabilise.",
                    "What doesn't automatically improve without attention: the reduced stress resilience that comes with lower estrogen, the increased importance of physical activity for mood and nervous system health, and the need for proactive management of the conditions — cardiovascular health, bone density, cognitive health — that estrogen was protecting against.",
                    "The women who navigate this transition best, in both research and clinical observation, are those who build the practices and relationships that support their nervous system during the difficult years, and carry them forward into the next chapter with the knowledge of their own system that the transition gave them.",
                ]},
            ],
            "callout": "The nervous system that survived perimenopause has been through something. It deserves recognition — and the ongoing care of someone who now knows it well."
        },
    ]
}

# ─────────────────────────────────────────────────────────────────────────────
# GENERATE ALL
# ─────────────────────────────────────────────────────────────────────────────
books = [
    ("03 - The Dopamine Reset.pdf", BOOK_03),
    ("04 - Nervous System Healing for Burnout.pdf", BOOK_04),
    ("05 - Sleep & the Nervous System.pdf", BOOK_05),
    ("06 - Somatic Tools for Grief.pdf", BOOK_06),
    ("07 - The ADHD Nervous System.pdf", BOOK_07),
    ("08 - Chronic Pain & the Nervous System.pdf", BOOK_08),
    ("09 - Trauma Release for Beginners.pdf", BOOK_09),
    ("10 - Somatic Healing for Perimenopause.pdf", BOOK_10),
]

if __name__ == "__main__":
    for filename, data in books:
        out = os.path.join(BASE, filename)
        generate_ebook(out, data)
