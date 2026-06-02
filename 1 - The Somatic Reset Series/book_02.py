"""
Book 02 — Somatic Exercises for Anxiety: 5-Minute Daily Practices to Regulate Your Body
Series: The Somatic Reset Series
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generate_ebook import generate_ebook

DISCLAIMER = """This book is for educational and informational purposes only. It is not a substitute for professional psychological, psychiatric, or medical advice. The somatic exercises described here are general wellness practices and are not intended to diagnose, treat, cure, or prevent anxiety disorders or any other mental health condition.\n\nIf you are experiencing severe anxiety, panic disorder, PTSD, or any condition that significantly impairs your daily functioning, please seek guidance from a qualified mental health professional. Always consult your doctor before beginning any new physical practice, particularly if you have cardiovascular, respiratory, or neurological conditions.\n\nBy using this material, you agree that the author and publisher bear no responsibility for any outcomes resulting from your application of the practices described."""

BOOK = {
    "title": "Somatic Exercises for Anxiety",
    "subtitle": "5-Minute Daily Practices to Regulate Your Body",
    "series_name": "The Somatic Reset Series",
    "accent_hex": "#3A86FF",
    "bg_hex": "#F0F6FF",
    "disclaimer": DISCLAIMER,
    "chapters": [
        {
            "title": "Why Your Body Holds the Answer",
            "intro": "Anxiety lives in the body. Not just as a feeling — as a physical state. Tight chest, shallow breathing, clenched jaw, shoulders that won't drop. Cognitive therapy gives you ways to argue with anxious thoughts. Somatic work gives you ways to change the underlying physical state that generates them.",
            "sections": [
                {"heading": "The Body-First Approach", "body": [
                    "Most conventional approaches to anxiety start from the top down — they try to change how you think, and hope the body follows. Somatic approaches invert this. They work with the body first, on the premise that physiological state shapes thought far more than thought shapes physiological state.",
                    "When you're in a high-anxiety state, the prefrontal cortex — the part of the brain responsible for rational thought, perspective, and problem-solving — is functionally less available. The amygdala, which processes threat, is running the show. Trying to reason with yourself in this state is a bit like trying to have a calm conversation with someone in the middle of a sprint. The biology isn't set up for it.",
                    "Somatic exercises work by changing the physiological conditions first — shifting the nervous system out of sympathetic dominance — which then makes the cognitive and emotional processing far more accessible. The sequence matters: body first, then mind.",
                ]},
                {"heading": "What Makes an Exercise Somatic", "body": [
                    "The word somatic comes from the Greek soma, meaning body. A somatic exercise is one that works through body sensation and movement rather than through thinking or talking. The goal is not to understand your anxiety better. The goal is to change what your nervous system is doing right now.",
                    "The exercises in this book are designed to be brief, practical, and usable in everyday situations — at your desk, in your car, before a meeting, in a bathroom stall if that's what you have. None of them require equipment, special clothing, or any previous experience with bodywork or yoga. They require only your attention and five minutes.",
                    "Some will feel immediately effective. Others may take a few days of practice before the effect becomes noticeable. This is normal. The nervous system learns through repetition, not revelation.",
                ]},
            ],
            "callout": "The body is not where anxiety gets stuck. It's where anxiety gets resolved."
        },
        {
            "title": "Grounding — When Everything Feels Too Much",
            "intro": "Grounding exercises bring attention back to the present moment through physical sensation. They are the first line of response when anxiety is acute — when thoughts are racing, the chest is tight, and the world feels slightly unreal.",
            "sections": [
                {"heading": "The 5-4-3-2-1 Sensory Reset", "body": [
                    "This is the most widely used grounding technique in somatic and trauma therapy, and for good reason — it works quickly and requires nothing except your senses. When anxiety spikes, the mind tends to time-travel: it projects into future threats or replays past ones. The 5-4-3-2-1 exercise anchors attention in the present by systematically engaging all five senses.",
                    "Name five things you can see. Really look — notice colour, shape, shadow, the specific way light falls on something. Then four things you can physically feel: the weight of your body in the chair, the texture of fabric on your skin, the temperature of the air. Three things you can hear: traffic, your own breathing, a distant sound. Two things you can smell, even if faint. One thing you can taste.",
                    "The exercise takes roughly two to three minutes and reliably reduces acute anxiety symptoms by redirecting attention away from threat-focused rumination and into present sensory experience. Do it slowly. The slower the better.",
                ]},
                {"heading": "Feet on the Floor", "body": [
                    "This is the simplest grounding practice and one of the most portable. Take off your shoes if possible, or simply press both feet flat against the floor with firm, deliberate pressure. Feel the ground pushing back. Notice the specific sensations: temperature, texture, the weight distribution across your foot.",
                    "Now press your feet down a little harder — engage the muscles in your legs slightly as if you're about to stand, then release. Repeat three times. This physical engagement of the lower body activates proprioceptive feedback — your body's sense of where it is in space — which is a reliable anchor when anxiety is pulling attention into abstract threat.",
                    "The reason this works is partly mechanical and partly neurological. Physically pressing into something solid communicates stability to the nervous system in a direct, non-cognitive way. It's hard to feel completely unmoored when you can feel the floor.",
                ]},
                {"heading": "The Body Scan Grounding Practice", "body": [
                    "This five-minute version of the body scan is designed specifically for acute anxiety moments rather than as a meditation. Sit or stand. Starting at the top of your head, slowly move attention down through your body, pausing briefly at each region: scalp, face, jaw, neck, shoulders, chest, upper back, arms and hands, belly, lower back, hips, thighs, knees, calves, feet.",
                    "At each location, notice what's there. Tension, warmth, numbness, pressure, nothing at all. Don't try to change it. Just register it. If you find an area that's particularly tight or held, take one slow breath that moves toward that area on the inhale, and releases from it on the exhale.",
                    "The deliberate movement of attention through the body short-circuits the tendency of anxious attention to fixate on threat-related thoughts. It also develops interoceptive awareness — the ability to sense your internal state — which over time makes you better at catching anxiety early, before it escalates.",
                ]},
            ],
            "callout": "You cannot think your way into the present moment. But you can feel your way there."
        },
        {
            "title": "Releasing Tension From the Top Down",
            "intro": "Anxiety concentrates in predictable places. For most people: the jaw, the shoulders, the neck, the chest. These areas hold tension so habitually that they stop registering as tense — they just become the background. These exercises target those specific zones.",
            "sections": [
                {"heading": "Jaw Release", "body": [
                    "The jaw is one of the most reliable tension storage sites in the body. The muscles around the temporomandibular joint (TMJ) are activated during stress, and in people with chronic anxiety, they're often partially contracted all day without awareness. TMJ pain, teeth grinding, headaches, and neck tension frequently trace back to habitual jaw clenching.",
                    "Place your fingertips lightly on your jaw muscles — just in front of your ears. Now deliberately clench your jaw for five seconds as hard as you comfortably can. Then release completely, letting the jaw drop slightly open. Notice the contrast. Repeat three times. The deliberate clenching followed by release creates a more complete relaxation than trying to simply relax would achieve — it uses the neuromuscular principle of proprioceptive neuromuscular facilitation, or PNF.",
                    "Follow this with a gentle massage of the jaw muscles using your fingertips. Work in small circles for thirty seconds each side. Many people are surprised how much tenderness they find in muscles they didn't know were chronically contracted.",
                ]},
                {"heading": "Shoulder and Neck Release", "body": [
                    "Lift both shoulders up toward your ears in an exaggerated shrug — hold for five counts — then drop them completely. Let gravity do the work of the release. Don't guide them down. Just let go. Repeat four times. The drop at the end should feel like genuine release, not a controlled lowering.",
                    "Follow with neck rolls: let the chin drop toward the chest, then slowly roll the head to the right, back toward the right shoulder, back to centre, to the left shoulder, and back down to centre. Two to three slow rolls each direction. Keep the movement unhurried. The neck carries a remarkable amount of stress-related tension and responds well to slow, deliberate movement.",
                    "Finish with a practice called ear-to-shoulder: tilt the right ear toward the right shoulder, hold for twenty seconds, then switch. For most people, one side will feel tighter than the other. That asymmetry is useful information — the tighter side is often the one you habitually brace toward.",
                ]},
                {"heading": "Chest Opening and Heart Breathing", "body": [
                    "Anxiety compresses the chest inward. Shoulders roll forward, the sternum drops, and breathing becomes shallower. This postural pattern reinforces the anxious state — the body is literally in a protective posture that signals threat to the nervous system.",
                    "Sit or stand with your back straight. Interlace your fingers behind your head. Gently press your head back into your hands and draw your elbows back and apart, opening the chest. Hold for five slow breaths, each one expanding the chest rather than the belly. Release. This physical opening of the chest sends proprioceptive signals in the opposite direction of compression — an expansion that the nervous system reads, at least partially, as safety.",
                    "Heart-focused breathing, developed by the HeartMath Institute, extends this by coupling the open posture with deliberate attention to the heart area. Breathe slowly in and out, imagining the breath moving through the centre of your chest. The research on heart-focused breathing suggests measurable HRV improvements within minutes — one of the few somatic techniques with this level of rapidly-demonstrable physiological effect.",
                ]},
            ],
            "callout": "Posture is not just how you hold your body. It's one of the most constant signals your nervous system receives about whether you're safe."
        },
        {
            "title": "Movement as Medicine",
            "intro": "Static tension needs movement to discharge. The body stores stress as muscular contraction, and contraction that doesn't get to complete its intended action — run, fight, flee — stays in the tissue. These exercises use movement to complete what the stress response started.",
            "sections": [
                {"heading": "Shaking to Discharge", "body": [
                    "As discussed in the first book in this series, animals in the wild naturally tremble and shake after a threat has passed. This physiological tremoring is how the nervous system completes the stress cycle and returns to baseline. Humans suppress this response through social conditioning, which means we accumulate unresolved stress activations in our bodies.",
                    "Stand with feet hip-width apart. Allow your knees to soften slightly. Begin to gently bounce through your knees — small, rhythmic, easy bounces — and let this vibration travel up through your body. After thirty seconds, allow the shaking to become more spontaneous rather than controlled. Your hands might tremble, your arms might move. Let it happen for two to three minutes, then slow gradually and stand still. Notice what's changed.",
                    "This takes practice and a willingness to look a bit ridiculous. Start in private. The effect — a particular warmth, tingling, and quieting — becomes more pronounced with each session.",
                ]},
                {"heading": "Walking as Nervous System Regulation", "body": [
                    "Bilateral movement — movement that alternates between the left and right sides of the body — has a specific regulatory effect on the nervous system. Walking is the most natural form of this. The alternating arm swing, the rhythmic activation of alternating legs, the proprioceptive feedback from each footfall — these combine to produce a gentle, consistent calming effect that sustained physical exercise doesn't always replicate.",
                    "The specific kind of walking that produces the most reliable regulatory effect is slow, deliberate, and preferably in nature or a quiet environment. Five to ten minutes of unhurried walking — not exercise walking, but attention-walking, noticing what you see and feel — consistently reduces cortisol and self-reported anxiety in studies.",
                    "Combining walking with the physiological sigh (a double inhale followed by a long exhale) amplifies the effect. One physiological sigh every three to four minutes of walking is a simple protocol that many people find works better than a full meditation session.",
                ]},
                {"heading": "Progressive Muscle Relaxation — Condensed Version", "body": [
                    "Progressive muscle relaxation (PMR) was developed by Edmund Jacobson in the 1920s and remains one of the most well-researched anxiety interventions available. The full protocol takes twenty to thirty minutes. This condensed version takes five.",
                    "Sit comfortably. Working from the feet up: tense the muscles in both feet and calves for five seconds — release. Tense the thighs and glutes — release. Tense the belly — release. Clench both fists and tense the arms — release. Squeeze the shoulders up to the ears — release. Scrunch the face: jaw, eyes, forehead — hold for five seconds — release completely.",
                    "The release phase is where the benefit lies. The deliberate tension followed by complete release produces a deeper relaxation than attempting to relax from a neutral state. Over time, the contrast between contracted and released becomes a tool for recognising habitual tension that you'd otherwise miss.",
                ]},
            ],
            "callout": "The stress response was designed for movement. When we don't move, it has nowhere to go."
        },
        {
            "title": "Breathwork for Anxiety States",
            "intro": "Different anxiety states call for different breath approaches. The racing heart and racing thoughts of acute anxiety require something different from the low-grade dread that settles in and doesn't move. This chapter maps breathing practices to specific anxiety presentations.",
            "sections": [
                {"heading": "For Acute Panic: The Physiological Sigh", "body": [
                    "When anxiety spikes acutely — heart pounding, thoughts fragmenting, the world narrowing — the fastest physiological intervention available is the physiological sigh. Double inhale through the nose (full breath, then a small top-up), followed by a complete, slow exhale through the mouth. Repeat three to five times.",
                    "The mechanism: during high anxiety, CO2 levels in the blood drop due to rapid, shallow breathing. This actually amplifies the panic response — low CO2 causes light-headedness, tingling, and the sense of unreality that characterises panic. The long exhale corrects this CO2 imbalance within a few breaths.",
                ]},
                {"heading": "For Chronic Low-Grade Anxiety: Coherent Breathing", "body": [
                    "Coherent breathing is a specific breath rhythm — five breaths per minute, or six seconds in and six seconds out — that research consistently shows maximises heart rate variability and vagal tone. It's not about relaxation per se; it's about physiological coherence — the synchronisation of respiratory, cardiovascular, and nervous system rhythms.",
                    "Inhale for six counts, exhale for six counts. No holds. No force. Just a smooth, gentle rhythm maintained for five to ten minutes. This is the practice most likely to produce measurable HRV improvements with consistent daily use. It's also the one that most people find easiest to maintain because the rhythm is steady and not demanding.",
                ]},
                {"heading": "For Anxious Overthinking: Alternate Nostril Breathing", "body": [
                    "Nadi Shodhana, or alternate nostril breathing, comes from the yogic tradition but has been studied in modern research contexts. The practice involves alternating the breath between the left and right nostrils using the thumb and ring finger to close each nostril in turn.",
                    "The research suggests that this practice balances activity between the left and right hemispheres of the brain and reduces the predominance of the default mode network — the ruminative mind that generates most anxious thinking. A five-minute session reliably reduces subjective anxiety and produces a calming that many people describe as qualitatively different from other breathwork — quieter, more even.",
                    "Instructions: Close the right nostril with the right thumb. Inhale through the left for four counts. Close both nostrils briefly. Open the right, exhale through it for six counts. Inhale right for four. Close both. Exhale left for six. This is one cycle. Repeat for five to ten cycles.",
                ]},
            ],
            "callout": "Breath is the remote control to your nervous system. Use it deliberately."
        },
        {
            "title": "Building a Daily 5-Minute Practice",
            "intro": "The most effective somatic practice is the one you actually do. Five minutes a day, consistently, produces more benefit than an hour-long session once a week. This chapter helps you build something that fits into your actual life.",
            "sections": [
                {"heading": "The Architecture of a 5-Minute Session", "body": [
                    "A well-structured five-minute somatic session moves through three phases: arrival, active practice, and integration. Arrival takes about sixty seconds — feet on the floor, two or three slow breaths, a brief body scan to notice where you're starting from. Active practice is three to three-and-a-half minutes of whatever the day calls for. Integration is thirty to sixty seconds of stillness — sitting or standing quietly and letting the practice land.",
                    "The integration phase is the most commonly skipped, and skipping it reduces the effect. The nervous system needs a moment of stillness after an active practice to consolidate what just happened. Jumping straight from breathwork into your email defeats a significant portion of the purpose.",
                ]},
                {"heading": "Choosing Your Practice by State", "body": [
                    "Rather than choosing a fixed practice and doing it regardless of how you feel, the more sophisticated approach is to match the practice to your current state:",
                    "• Acute spike of anxiety → Physiological sigh, then 5-4-3-2-1 grounding",
                    "• Chronic tension in the body → Jaw release, shoulder drop, PMR condensed",
                    "• Racing thoughts and overthinking → Alternate nostril breathing or body scan",
                    "• Flat, numb, disconnected → Shaking, walking, movement",
                    "• General baseline maintenance → Coherent breathing or extended exhale",
                    "Over time, you'll develop a feel for what your system needs. The goal is fluency — moving through these tools with the ease of someone who knows their own nervous system.",
                ]},
                {"heading": "When to Practice", "body": [
                    "The most powerful times for somatic practice are at transition points — the transitions that bookend high-stress activities. Five minutes before a difficult conversation, a presentation, a medical appointment, or a family gathering. Five minutes after returning home from work, before switching into evening mode.",
                    "Transition points are where nervous system states shift, and intervening at those moments with a deliberate practice gives you agency over what state you carry forward. The five minutes before bed is the most consistently beneficial single slot for almost everyone — the body is already preparing for rest and is particularly receptive to downregulation.",
                ]},
            ],
            "callout": "Five minutes isn't nothing. Over a year, it's thirty hours of building a different relationship with your own nervous system."
        },
        {
            "title": "Long-Term Integration",
            "intro": "The practices in this book are not a course you take and complete. They're a language you're learning — one that gets more useful the more fluent you become.",
            "sections": [
                {"heading": "Building Interoceptive Awareness", "body": [
                    "The underlying skill that all somatic practices build is interoceptive awareness — the ability to sense your internal physical state. Research by Lisa Feldman Barrett and others has shown that people with higher interoceptive awareness have greater emotional regulation capacity, more accurate perception of their emotional states, and better recovery from stress.",
                    "Interoceptive awareness develops through consistent practice of noticing — the body scan, the grounding exercises, the deliberate attention to physical sensation during breathwork. It's a trainable skill, not a fixed trait. And it's the single most transferable skill this work offers, because once you can feel your anxiety state shifting in real time, you can intervene before it escalates rather than after.",
                ]},
                {"heading": "What Progress Actually Looks Like", "body": [
                    "Progress in somatic anxiety work is usually invisible until suddenly it isn't. You don't feel yourself getting better day by day. You notice, after six weeks, that something that would have sent you spiralling for two days barely registered. You notice that your shoulders are at a different resting height than they were three months ago. You notice that you caught the early signs of an anxiety spike and did something about it before it became a problem.",
                    "This non-linear, often invisible quality of progress is what causes people to give up too early. The changes are happening whether or not they're perceptible. Trust the practice.",
                ]},
                {"heading": "When to Seek More Support", "body": [
                    "If anxiety is severe, persistent, or significantly disrupting your life, please don't rely on self-directed practices alone. A qualified therapist who is trained in somatic approaches — Somatic Experiencing, sensorimotor psychotherapy, or EMDR — can offer a level of support and attunement that no book can provide.",
                    "These practices are a foundation. They work best in combination with good sleep, adequate nutrition, meaningful social connection, and where needed, professional support. No single intervention is sufficient for everyone. Use what helps. Add what you need.",
                ]},
            ],
            "callout": "The goal is not the absence of anxiety. It's a body that knows how to move through it."
        },
    ]
}

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "02 - Somatic Exercises for Anxiety.pdf")
    generate_ebook(out, BOOK)
