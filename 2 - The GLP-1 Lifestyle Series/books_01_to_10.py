"""
Books 01–10 — The GLP-1 Lifestyle Series
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from generate_ebook import generate_ebook

BASE = os.path.dirname(__file__)
ACCENT = "#00B894"
BG = "#F0FFF9"
SERIES = "The GLP-1 Lifestyle Series"

DISCLAIMER = """This book is for educational and informational purposes only. It is not medical advice and does not constitute a recommendation to start, stop, or change any medication or treatment. GLP-1 receptor agonists are prescription medications that should only be used under the supervision of a qualified healthcare provider.\n\nThe nutritional guidance, exercise information, and lifestyle strategies in this book are general wellness information and are not tailored to your individual medical situation. Always consult your doctor, registered dietitian, or other qualified health professional before making changes to your diet, exercise routine, or medication management.\n\nThe author and publisher accept no liability for outcomes arising from your use of this material."""

def make_book(title, subtitle, chapters):
    return {"title": title, "subtitle": subtitle, "series_name": SERIES,
            "accent_hex": ACCENT, "bg_hex": BG, "disclaimer": DISCLAIMER,
            "chapters": chapters}

B01 = make_book(
    "The GLP-1 Nutrition Guide",
    "What to Eat to Preserve Muscle and Maximize Results",
    [
        {"title": "How GLP-1 Medications Change Your Relationship with Food",
         "intro": "GLP-1 receptor agonists — Ozempic, Wegovy, Mounjaro, Rybelsus — work partly by slowing gastric emptying, reducing appetite, and creating a sustained sense of fullness. This is useful for weight loss. It also creates specific nutritional challenges that nobody warns you about, and that are responsible for a lot of the side effects and suboptimal results people experience.",
         "sections": [
             {"heading": "What GLP-1 Drugs Actually Do", "body": [
                 "GLP-1 (glucagon-like peptide-1) is a naturally occurring gut hormone released in response to food intake. It stimulates insulin secretion, suppresses glucagon, slows the rate at which the stomach empties, and signals satiety to the brain. GLP-1 receptor agonists mimic and amplify this effect pharmacologically.",
                 "The result: food moves through the stomach more slowly, appetite is significantly reduced, and the brain receives earlier and stronger satiety signals. For many people, the reduction in appetite is profound — foods that used to be difficult to resist hold little appeal, and hunger itself may feel muted or absent.",
                 "This appetite suppression is the mechanism of weight loss. It's also why eating enough of the right things becomes an active challenge rather than a passive activity. When you're not hungry, you may not eat enough protein, enough micronutrients, or enough food overall to support lean mass preservation — which is the central nutritional challenge on GLP-1.",
             ]},
             {"heading": "The Muscle Loss Problem", "body": [
                 "Weight loss on GLP-1 medications follows the same pattern as all calorie-restricted weight loss: it includes both fat and lean mass. Studies on semaglutide (the active ingredient in Ozempic and Wegovy) have shown that approximately 25–40% of weight lost can be lean mass, including muscle.",
                 "This matters for several reasons. Muscle is metabolically active — it burns calories at rest and supports healthy blood sugar regulation. Losing significant lean mass during weight loss lowers metabolic rate, increases the risk of weight regain, and in older adults, contributes to sarcopenia — the age-related loss of muscle that is associated with falls, frailty, and poor health outcomes.",
                 "The nutrition and exercise strategies in this book are specifically designed to shift that ratio — to maximise fat loss and minimise lean mass loss while on GLP-1 medication.",
             ]},
         ],
         "callout": "GLP-1 medication handles the appetite. Your job is to make sure what you do eat is working hard enough to protect your muscle."
         },
        {"title": "The Protein Priority",
         "intro": "If there is one nutritional principle that matters above all others on GLP-1, it's this: eat protein first, at every meal, every day.",
         "sections": [
             {"heading": "Why Protein Is Non-Negotiable", "body": [
                 "Protein is the primary dietary determinant of lean mass preservation during calorie restriction. The research is consistent: higher protein intakes during weight loss preserve more muscle. The threshold that most researchers identify for muscle preservation is 1.2–1.6 grams of protein per kilogram of body weight per day — higher than typical dietary guidelines, which are based on minimum requirements rather than optimal body composition outcomes.",
                 "On GLP-1, when total food intake is significantly reduced, getting this amount of protein requires deliberate planning. If you're eating 1,200–1,500 calories per day and protein needs to be 120–160 grams, protein needs to constitute 40–50% of total calories. This leaves limited room for other macronutrients, which is why the composition of each meal matters so much.",
             ]},
             {"heading": "Best Protein Sources on GLP-1", "body": [
                 "The most practical protein sources for GLP-1 users are complete animal proteins with high leucine content. Leucine is the specific amino acid that most directly stimulates muscle protein synthesis, and it's most concentrated in animal proteins. Eggs (particularly egg whites for dense protein with low volume), chicken and turkey breast, Greek yoghurt, cottage cheese, fish and seafood, and lean beef are all excellent choices.",
                 "For those eating less meat, a combination of dairy proteins (whey, casein) with plant proteins (soy, pea) can reach complete amino acid profiles. Soy is the most complete plant protein — tempeh and edamame are high-leucine soy sources. Combining with a high-quality protein powder (whey or pea-based) is often practical when appetite is suppressed and food volume is limited.",
                 "Protein shakes deserve specific mention: when solid food is unappealing due to GLP-1 side effects, a protein shake provides muscle-preserving protein in a tolerable liquid form. A 25–30 gram protein shake consumed in the morning can anchor the day's protein intake when breakfast is the most difficult meal.",
             ]},
             {"heading": "The Eat-Protein-First Rule", "body": [
                 "At every meal, eat protein before anything else. This is practical in two ways: it ensures protein is consumed even when appetite fails before the meal is finished, and it takes advantage of the early satiety signal by filling the available appetite with the most important macronutrient first.",
                 "A plate structured as protein first, then vegetables, then any carbohydrates — rather than eating from all parts of the plate simultaneously — consistently improves protein intake in GLP-1 users without requiring larger total meal volumes.",
             ]},
         ],
         "callout": "On a reduced appetite, every bite has to earn its place. Protein earns its place first."
         },
        {"title": "Managing Nausea and Tolerating Food",
         "intro": "Nausea is the most common side effect of GLP-1 medications, particularly in the first weeks and during dose escalations. This chapter is about eating through it without abandoning nutrition.",
         "sections": [
             {"heading": "Why GLP-1 Causes Nausea", "body": [
                 "The nausea of GLP-1 medications is primarily a consequence of delayed gastric emptying. Food sits in the stomach longer than usual, and the pressure and fermentation that results produces nausea, discomfort, and sometimes vomiting. It tends to be worst in the first two to four weeks of a new dose and typically improves as the body adapts.",
                 "Understanding the mechanism helps identify solutions. Anything that further slows gastric emptying — large meals, high-fat foods, carbonated beverages, lying down after eating — worsens nausea. Anything that allows the stomach to process food without additional mechanical stress — small portions, upright posture after eating, liquid nutrition — reduces it.",
             ]},
             {"heading": "The Nausea Protocol", "body": [
                 "Eat small, frequent portions rather than structured meals when nausea is significant. Four to six small protein-forward servings throughout the day manage nausea better than three meals. Portion size matters: when the stomach is already processing slowly, adding more volume creates pressure. Aim for portions that feel comfortable, not complete.",
                 "Cold or room-temperature foods are generally better tolerated than hot foods during high-nausea periods — heat exacerbates the stomach discomfort. Ginger — in tea, capsule form, or as a food — has genuine evidence for reducing nausea and is safe to use alongside GLP-1 medications.",
                 "Stay upright for at least thirty to forty-five minutes after eating. Gravity assists gastric emptying and reduces the pressure that produces nausea. Lying down immediately after eating is one of the most reliable ways to worsen GLP-1 nausea.",
             ]},
             {"heading": "Foods That Work When Nothing Sounds Good", "body": [
                 "In high-nausea periods, the goal is maintenance — keeping enough protein and hydration in to prevent muscle loss and functional decline — rather than optimisation. Greek yoghurt, cottage cheese, protein shakes, scrambled eggs, and soft fish are typically the best-tolerated protein sources when nausea is significant.",
                 "Saltine crackers and white rice are often recommended during nausea because they're easy on the stomach. They are, however, almost entirely void of protein. If you're relying on these for tolerance, pair them with a protein source — even a tablespoon of peanut butter on crackers is better than crackers alone.",
             ]},
         ],
         "callout": "Getting through the nausea phase is a short-term challenge. The decisions you make during it set the foundation for everything that follows."
         },
        {"title": "Hydration and Micronutrients",
         "intro": "Reduced food intake on GLP-1 creates micronutrient gaps that are easy to miss because the symptoms are gradual and non-specific.",
         "sections": [
             {"heading": "Hydration on GLP-1", "body": [
                 "Reduced food intake means reduced water intake from food — roughly 20% of daily water typically comes from food, not drinks. On GLP-1, when food intake drops significantly, deliberate hydration becomes more important. Dehydration amplifies nausea, fatigue, and headaches — the same symptoms already produced by the medication.",
                 "A practical target: at least 2–2.5 litres of water per day, consumed steadily throughout the day rather than in large amounts at once. Large amounts of liquid at once distend the stomach and worsen nausea. Small, frequent sips are better tolerated.",
                 "Electrolytes deserve attention, particularly if nausea has led to vomiting or significantly reduced food intake. Sodium, potassium, and magnesium — the primary electrolytes lost in reduced food and fluid scenarios — are worth supplementing during high-symptom periods. An electrolyte powder without sugar added to water is practical and effective.",
             ]},
             {"heading": "The Micronutrient Gap", "body": [
                 "When calorie intake drops significantly, micronutrient intake drops proportionally unless deliberate effort is made to include nutrient-dense foods. The nutrients most commonly insufficient on GLP-1 — based on dietary analysis studies and clinical experience — are: B12, iron (particularly in women), zinc, folate, calcium, and vitamin D.",
                 "A comprehensive daily multivitamin is the minimum appropriate supplement on GLP-1. It doesn't replace food micronutrients, but it provides a baseline that reduces the risk of significant deficiency. A bariatric-formulated multivitamin is a good option — these are designed for people eating significantly less than typical and have higher bioavailability forms of key nutrients.",
             ]},
         ],
         "callout": "You're eating less. That means every food choice has to carry more nutritional weight."
         },
        {"title": "Long-Term Nutrition Strategy",
         "intro": "GLP-1 medications work best as part of a long-term lifestyle change, not as a temporary intervention. The nutrition strategy that serves you during active weight loss is different from the one that serves you in maintenance.",
         "sections": [
             {"heading": "Transitioning to Maintenance", "body": [
                 "As weight loss slows and body composition stabilises, the nutrition priority shifts from aggressive protein-first eating to a more balanced, sustainable pattern. Calorie needs increase slightly as body weight stabilises, and the appetite suppression of GLP-1 may need to be managed upward — ensuring you're eating enough to support activity, recovery, and metabolic health.",
                 "Maintenance on GLP-1 looks like: adequate protein (1.0–1.2g/kg body weight), abundant vegetables, appropriate carbohydrate around activity, and quality fats. It looks, in other words, like the Mediterranean diet pattern — which consistently shows the best long-term outcomes for cardiovascular health, metabolic health, and body composition maintenance.",
             ]},
             {"heading": "What to Do If the Medication Stops", "body": [
                 "The weight regain pattern after stopping GLP-1 medications is well-documented. Without the pharmacological appetite suppression, hunger returns — often to levels higher than before treatment, due to the body's homeostatic response to weight loss. Without behavioural and dietary foundations built during treatment, most of the weight is regained within one to two years.",
                 "The most protective factors against rebound are: the strength training habits built during treatment (which maintain a higher metabolic rate), the eating patterns established (particularly protein-first, vegetable-rich meals), and the relationship with hunger that was developed — learning to eat to nourishment rather than to appetite.",
             ]},
         ],
         "callout": "GLP-1 gives you a window. What you build inside that window determines whether the results last."
         },
    ]
)

B02 = make_book(
    "GLP-1 for Women Over 40",
    "Perimenopause, Hormones, and Ozempic",
    [
        {"title": "When Hormones and GLP-1 Intersect",
         "intro": "Weight gain in perimenopause doesn't behave the same way as weight gain from simple overeating, and GLP-1 medications don't have the same effects in the perimenopausal body as they do in younger or postmenopausal women. Understanding the hormonal context changes how you use the medication and what you can realistically expect.",
         "sections": [
             {"heading": "Why Perimenopause Changes Weight", "body": [
                 "The weight changes of perimenopause are driven by several converging factors. Declining estrogen shifts fat distribution from the hips and thighs (peripheral fat) to the abdomen (visceral fat) — a shift that is associated with increased cardiovascular and metabolic risk. Declining progesterone affects sleep quality, and poor sleep directly increases appetite hormones and reduces satiety signals. Cortisol, often elevated in the chronic stress environment of midlife, promotes visceral fat storage. And the muscle loss that begins accelerating in the 40s reduces metabolic rate.",
                 "GLP-1 medications address the appetite and food intake dimension. They don't address the hormonal drivers of visceral fat accumulation, the sleep disruption driving appetite dysregulation, or the muscle loss changing metabolic rate. To get the best results on GLP-1 in perimenopause, you need to address all of these — not just the medication piece.",
             ]},
             {"heading": "GLP-1 and Estrogen — What the Research Says", "body": [
                 "Estrogen and GLP-1 receptors interact in ways that are still being studied. What current research suggests is that estrogen enhances GLP-1 receptor sensitivity — meaning GLP-1 medications may be somewhat less effective in the low-estrogen environment of late perimenopause and postmenopause than in women with higher estrogen levels.",
                 "This is not a reason to avoid GLP-1 medications in perimenopause. The medications still work — clinical trials include women across the age range and show significant efficacy. But it's a reason to understand that the response may differ from what's reported in general populations, and why addressing the hormonal context — including through HRT if appropriate — may amplify results.",
             ]},
         ],
         "callout": "GLP-1 is a tool, not a solution. In perimenopause, the most effective approach combines the medication with the other things your body needs at this stage."
         },
        {"title": "Muscle Preservation in the Perimenopausal Body",
         "intro": "Muscle loss on GLP-1 is a concern for everyone. In perimenopausal women, where estrogen is declining and muscle loss is already accelerating, it's a more urgent concern.",
         "sections": [
             {"heading": "The Estrogen-Muscle Connection", "body": [
                 "Estrogen has direct effects on muscle protein synthesis and muscle satellite cell function. Declining estrogen in perimenopause accelerates the muscle loss that begins with aging — a process called sarcopenic obesity when it occurs alongside increasing fat mass. This is the combination that produces what many perimenopausal women describe as looking different at the same weight: less muscle definition, more fat, even when the scale hasn't changed dramatically.",
                 "On GLP-1, the combination of calorie restriction and declining estrogen creates compounded risk for muscle loss. Aggressive protein intake and resistance training are not optional extras in this context — they are the primary protective measures.",
             ]},
             {"heading": "Resistance Training for Perimenopausal Women on GLP-1", "body": [
                 "The evidence for resistance training in perimenopausal women is comprehensive: it preserves lean mass, improves insulin sensitivity, supports bone density, reduces visceral fat, improves mood, and mitigates many of the metabolic changes driven by declining estrogen. On GLP-1, resistance training also helps ensure that the weight being lost is fat rather than muscle.",
                 "Two to three sessions per week of progressive resistance training is the minimum effective dose. Progressive means gradually increasing the challenge over time — more weight, more repetitions, more sets — so the stimulus remains sufficient to drive adaptation. Compound movements that work multiple muscle groups simultaneously (squats, deadlifts, rows, presses) produce the greatest metabolic and hormonal benefit for the time invested.",
             ]},
         ],
         "callout": "In perimenopause, you don't have to choose between managing your weight and maintaining your strength. You have to do both."
         },
        {"title": "Navigating Side Effects in the Perimenopause Body",
         "intro": "Perimenopause already produces nausea, fatigue, digestive disruption, and sleep problems. GLP-1 medications can intensify all of these temporarily.",
         "sections": [
             {"heading": "Distinguishing GLP-1 Side Effects from Perimenopausal Symptoms", "body": [
                 "This is genuinely difficult, and it matters clinically. Nausea, fatigue, digestive changes, and sleep disruption are common to both perimenopause and GLP-1 side effects. If symptoms are dramatically worse in the first weeks after starting or escalating GLP-1 medication, they're likely medication-related. If they precede the medication or are not dose-dependent, they're more likely perimenopausal.",
                 "Tracking symptoms in relation to dose escalation timing is the most practical way to distinguish causes. A simple daily log — symptoms, severity, dose week — clarifies the pattern relatively quickly.",
             ]},
             {"heading": "Managing Compounded Fatigue", "body": [
                 "Perimenopause fatigue plus GLP-1 initiation fatigue can be genuinely significant. The primary interventions are the same: protein adequacy, hydration, sleep optimisation, and gentle movement (even when motivation is low). The fatigue is typically self-limiting as the body adapts to the medication — usually two to four weeks per dose escalation.",
                 "Caffeine as a fatigue management strategy has limits: it worsens perimenopausal sleep, increases cortisol, and can worsen hot flashes. Strategic use — earlier in the day only, moderate amounts — rather than escalating use is the appropriate approach during this period.",
             ]},
         ],
         "callout": "The worst of GLP-1 side effects in perimenopause is temporary. The metabolic benefits, with the right support, are lasting."
         },
        {"title": "The Hormone Conversation — HRT and GLP-1",
         "intro": "HRT and GLP-1 are not mutually exclusive. For many perimenopausal women, the combination is more effective than either alone.",
         "sections": [
             {"heading": "What HRT Does That GLP-1 Doesn't", "body": [
                 "HRT addresses the hormonal drivers of perimenopausal weight gain — the visceral fat accumulation driven by declining estrogen, the sleep disruption from night sweats, the muscle loss accelerated by low estrogen. GLP-1 addresses appetite and food intake. These are complementary mechanisms.",
                 "Research suggests that estrogen therapy in perimenopause reduces visceral fat accumulation and preserves muscle mass — effects that work in the same direction as the goals of GLP-1 treatment. Women on estrogen therapy who start GLP-1 may find they experience less of the muscle loss typically associated with GLP-1 weight loss.",
             ]},
             {"heading": "Having the Conversation with Your Doctor", "body": [
                 "Many women are on GLP-1 medications without a concurrent conversation about HRT, and vice versa. Bringing both into the same clinical conversation is worthwhile. A doctor who is current on both the GLP-1 evidence and the updated HRT evidence base can help you understand whether the combination is appropriate for your individual situation.",
                 "The updated risk understanding for HRT — based on post-WHI research and analysis — suggests that for healthy women under 60 or within ten years of menopause onset, the benefit-risk profile of HRT is favourable for most women with significant symptoms. This is a decision to make with a qualified clinician, not a one-size-fits-all recommendation.",
             ]},
         ],
         "callout": "Your hormones are part of the story. Don't let them be the part nobody talks about."
         },
        {"title": "Sustainable Results After 40",
         "intro": "The definition of success on GLP-1 in perimenopause needs to be broader than the number on the scale.",
         "sections": [
             {"heading": "Redefining the Goal", "body": [
                 "For perimenopausal women, weight loss goals calibrated to what was achievable at 30 are often both unrealistic and beside the point. The more meaningful goals at this life stage are: reducing visceral fat and the metabolic risk it carries, preserving lean mass and functional strength, improving sleep quality, and supporting cardiovascular and metabolic health for the decades ahead.",
                 "Body composition — the ratio of fat to lean mass — is more predictive of these outcomes than scale weight. A woman who loses ten pounds of fat while maintaining muscle is in a categorically better metabolic position than one who loses fifteen pounds including five pounds of muscle.",
             ]},
             {"heading": "Building the Foundation for the Next Decade", "body": [
                 "The habits built during GLP-1 treatment — protein-prioritised eating, resistance training, sleep hygiene, stress management — are the same habits associated with healthy aging and reduced chronic disease risk. This is the real long-term value proposition: not a number on the scale, but a set of practices that serve your health and body composition into and through menopause and beyond.",
             ]},
         ],
         "callout": "You're not trying to get back the body you had at 30. You're building the strongest version of the body you have now."
         },
    ]
)

B03 = make_book(
    "Managing GLP-1 Side Effects",
    "A Practical Handbook for the First 90 Days",
    [
        {"title": "What to Expect — The First 90 Days Honestly",
         "intro": "The first ninety days on GLP-1 medication are often the most challenging. They're also when most people quit — not because the medication isn't working, but because the side effects in the early weeks are genuinely uncomfortable and nobody prepared them adequately for what was coming.",
         "sections": [
             {"heading": "The Side Effect Timeline", "body": [
                 "GLP-1 side effects are not uniformly distributed across time. They tend to peak in the first two to four weeks of a new dose, then improve as the body adapts. Dose escalations restart the cycle at a lower intensity than the initial start.",
                 "The most common side effects and their typical timeline: nausea (first two to six weeks, usually most intense in weeks one and two), fatigue (first two to four weeks), constipation (ongoing, but typically manageable within four to six weeks), headaches (usually first week, then episodic), and acid reflux or heartburn (variable, often improves within a month).",
                 "Knowing this timeline matters because it reframes the experience. Week two nausea feels different when you know it's the worst it will get rather than a sign the medication isn't agreeing with you.",
             ]},
             {"heading": "The Dose Escalation Protocol", "body": [
                 "GLP-1 medications use a dose escalation schedule precisely because side effects are dose-dependent. Starting low and increasing slowly allows the body to adapt. The schedules vary by medication — semaglutide (Ozempic/Wegovy) typically escalates monthly, tirzepatide (Mounjaro) every four weeks.",
                 "If side effects are severe on a given dose, it is entirely appropriate to remain at that dose for longer than the standard schedule before escalating. Slower escalation is associated with better tolerability without significantly compromising efficacy. Discuss this with your prescribing provider.",
             ]},
         ],
         "callout": "The side effects feel permanent when you're in them. They almost never are."
         },
        {"title": "Nausea — Managing the Most Common Side Effect",
         "intro": "Nausea on GLP-1 is the most frequently reported side effect and the most common reason people discontinue. Most of it is preventable or significantly reducible with the right strategies.",
         "sections": [
             {"heading": "Dietary Strategies for Nausea", "body": [
                 "Small, frequent portions. This is the most important instruction. The stomach is processing food more slowly than usual, and adding volume to an already-processing stomach creates the pressure and discomfort that produces nausea. Aim for portions that fill about a third to a half of what you'd normally eat, eaten three to four times per day.",
                 "Avoid high-fat foods during high-nausea periods. Fat is the macronutrient that most significantly slows gastric emptying — it stays in the stomach longest. Fried foods, creamy sauces, fatty meats, and large amounts of added fat compound the delayed emptying already produced by the medication.",
                 "Cold and bland foods are generally better tolerated. Many GLP-1 users find that hot food smells and rich flavours trigger nausea even when they didn't before. Trust these aversions during the adaptation period — your body is giving you useful information about what it can currently process.",
             ]},
             {"heading": "Non-Dietary Strategies", "body": [
                 "Timing the injection strategically can reduce nausea. Many people find that taking the weekly injection at bedtime (for weekly formulations) means the peak nausea period occurs during sleep. Discuss this option with your prescriber.",
                 "Ginger is the most evidence-supported natural nausea remedy and is safe alongside GLP-1. Ginger tea, ginger chews, or ginger capsules all provide some benefit. The mechanism involves serotonin receptor modulation in the gut — similar to some prescription anti-nausea medications.",
                 "Vitamin B6 (25mg, three times daily) has reasonable evidence for reducing pregnancy-related nausea and is sometimes effective for GLP-1 nausea through similar mechanisms. Check with your doctor before adding supplements.",
             ]},
         ],
         "callout": "Nausea on GLP-1 is mostly about management strategy, not endurance."
         },
        {"title": "Constipation and Digestive Changes",
         "intro": "Constipation is the second most common GLP-1 side effect, and unlike nausea, it often persists beyond the adaptation period and requires ongoing management.",
         "sections": [
             {"heading": "Why GLP-1 Causes Constipation", "body": [
                 "Delayed gastric emptying doesn't just affect the stomach — it slows the entire GI tract. Food moves more slowly through the intestines, allowing more water to be reabsorbed, which produces harder, drier stools. Combined with reduced food intake (less fibre) and often reduced water intake (nausea makes drinking unappealing), constipation on GLP-1 is a predictable consequence rather than an unusual side effect.",
             ]},
             {"heading": "The Constipation Management Protocol", "body": [
                 "Hydration is the most important single intervention — at least 2–2.5 litres of water per day, even when nausea makes drinking unappealing. Sipping steadily throughout the day is more tolerable than large amounts at once.",
                 "Fibre from food: prioritise soluble fibre (oats, beans, lentils, fruits, psyllium) over insoluble fibre in the early stages. Soluble fibre adds bulk and retains water in the stool. Very high insoluble fibre (bran, raw vegetables in large amounts) can worsen bloating when gut motility is already reduced.",
                 "Movement: even gentle walking stimulates gut motility. Ten to fifteen minutes of walking after meals is one of the most effective non-pharmaceutical interventions for constipation.",
                 "Magnesium citrate or glycinate (300–400mg at bedtime) has both laxative effects and general health benefits, and is well-tolerated for most people. Polyethylene glycol (Miralax in the US) is the over-the-counter osmotic laxative most commonly recommended by gastroenterologists for ongoing management.",
             ]},
         ],
         "callout": "Constipation on GLP-1 is manageable. Ignoring it is not — it becomes uncomfortable quickly and compounds other side effects."
         },
        {"title": "Fatigue, Headaches, and Other Early Side Effects",
         "intro": "The non-gastrointestinal side effects of GLP-1 are less discussed but equally real in the adaptation period.",
         "sections": [
             {"heading": "Fatigue", "body": [
                 "GLP-1 fatigue in the early weeks is largely driven by calorie deficit (eating less than the body is used to) and the metabolic adjustment of significant appetite suppression. The body is working with less fuel than it's accustomed to. This typically improves within two to four weeks as the body adapts to the new energy intake.",
                 "During the fatigue period: prioritise sleep, maintain hydration and protein intake (both reduce fatigue), and reduce the intensity of exercise temporarily if needed. This is not the time to add new training demands. Gentle movement is more appropriate than high-intensity exercise while the body is adapting.",
             ]},
             {"heading": "Headaches", "body": [
                 "Headaches in the first days to weeks are most commonly related to dehydration and low calorie intake rather than the medication's direct effects. The approach is simple: increase fluid intake, don't skip meals entirely, and ensure adequate sodium intake (which helps retain fluid and maintain blood pressure, both of which can drop slightly with significant calorie reduction).",
             ]},
             {"heading": "Acid Reflux and Heartburn", "body": [
                 "Delayed gastric emptying allows stomach acid more time to contact the lower oesophagus, which can worsen or create acid reflux. Strategies: don't lie down for at least one to two hours after eating, sleep with the head slightly elevated if reflux is nocturnal, avoid known reflux triggers (caffeine, alcohol, fatty foods, citrus), and eat smaller portions.",
                 "If reflux is severe or persistent, speak with your doctor about appropriate treatment. Over-the-counter antacids are generally safe with GLP-1, but proton pump inhibitors or H2 blockers may be appropriate if reflux is significant.",
             ]},
         ],
         "callout": "Most early GLP-1 side effects are the body adjusting. Support it through the adjustment."
         },
        {"title": "When to Call Your Doctor",
         "intro": "Most GLP-1 side effects are uncomfortable but manageable. Some require medical attention.",
         "sections": [
             {"heading": "Side Effects That Need Medical Evaluation", "body": [
                 "Severe, persistent vomiting that prevents adequate hydration (risk of dehydration and electrolyte imbalance). Severe abdominal pain, particularly radiating to the back (rare risk of pancreatitis, a known but uncommon GLP-1 side effect). Significant changes in vision (associated with rapid blood sugar changes in people with diabetes). Any symptoms that are rapidly worsening or not improving after the typical adaptation period.",
                 "Pancreatitis is the most serious GLP-1 risk. The symptoms — severe upper abdominal pain, often radiating to the back, sometimes with nausea and fever — are distinctive and warrant immediate medical evaluation. The absolute risk is low, but it's important to know the warning signs.",
             ]},
             {"heading": "Building a Working Relationship with Your Prescriber", "body": [
                 "GLP-1 treatment is most effective when managed collaboratively with a knowledgeable provider. If your current prescriber is unfamiliar with GLP-1 side effect management or isn't responsive to your concerns during the adaptation period, a provider with specific obesity medicine or endocrinology training may be worth seeking. The medication is too useful to abandon because of manageable side effects that received inadequate guidance.",
             ]},
         ],
         "callout": "Discomfort is expected. Distress is a signal. Know the difference."
         },
    ]
)

B04 = make_book(
    "GLP-1 and Strength Training",
    "Building Muscle While on Ozempic",
    [
        {"title": "Why Strength Training Is Non-Negotiable on GLP-1",
         "intro": "GLP-1 medications create a calorie deficit. Calorie deficits, without resistance training, result in the loss of muscle alongside fat. Strength training is the primary tool for ensuring the weight you lose is the weight you actually want to lose.",
         "sections": [
             {"heading": "The Research on Muscle Loss with GLP-1", "body": [
                 "Multiple clinical trials and real-world studies have documented significant lean mass loss alongside fat loss on GLP-1 medications. Without countermeasures, 25–40% of the weight lost can be lean tissue. Over a year of treatment losing 30 pounds, that could mean 8–12 pounds of muscle lost alongside 18–22 pounds of fat.",
                 "The long-term metabolic consequences of this are significant. Each pound of muscle burns approximately 6–10 calories per day at rest. Losing 10 pounds of muscle reduces resting metabolic rate by 60–100 calories per day — a reduction that compounds over time and contributes to weight regain when medication stops.",
             ]},
             {"heading": "What Resistance Training Does", "body": [
                 "Progressive resistance training provides a consistent anabolic stimulus — a signal to the body that muscle is being used and needed. Even in a calorie deficit, consistent resistance training dramatically reduces muscle loss and, in some cases (particularly in previously untrained individuals), can produce muscle gain alongside fat loss.",
                 "The combination of adequate protein intake and progressive resistance training is the evidence-based strategy for body recomposition on GLP-1. This is not a peripheral recommendation — it is the central intervention for ensuring that the medication's weight loss benefits translate into improved body composition rather than simply reduced scale weight.",
             ]},
         ],
         "callout": "The scale is the wrong metric. Body composition is the right one."
         },
        {"title": "Starting Strength Training on GLP-1",
         "intro": "The first weeks on GLP-1 are not the time to start an aggressive new training programme. Here's how to sequence it correctly.",
         "sections": [
             {"heading": "Phase One: Establish the Habit (Weeks 1–4)", "body": [
                 "In the first month on GLP-1, energy is reduced, nausea may be present, and the body is adapting to significant metabolic changes. The appropriate training goal in this phase is simply to establish a consistent movement habit without adding physiological stress.",
                 "Two sessions per week of light-to-moderate resistance training — bodyweight exercises or light weights, focusing on form rather than intensity — is appropriate. Keep sessions to thirty to forty minutes. Prioritise recovery. The goal is consistency, not intensity.",
             ]},
             {"heading": "Phase Two: Progressive Loading (Months 2–3)", "body": [
                 "As the body adapts to the medication and side effects reduce, training intensity can increase. Move to two to three sessions per week, progressively increasing the challenge through more weight, more repetitions, or more difficult exercise variations.",
                 "The key principle of progressive overload: the body adapts to the demands placed on it. Once a given level of challenge no longer produces adaptation, the challenge needs to increase. This is not about lifting maximum weight — it's about consistent, gradual progression over months.",
             ]},
             {"heading": "The Essential Exercises", "body": [
                 "A functional strength programme doesn't require a gym. The movements that provide the greatest benefit for muscle preservation and metabolic health are: squats or leg press (lower body push), Romanian deadlifts or hip hinges (lower body pull/posterior chain), rows (upper body pull), and push-ups or chest press (upper body push).",
                 "These four movement patterns, trained twice weekly with progressive resistance, cover the major muscle groups and provide sufficient stimulus for lean mass preservation during GLP-1-assisted weight loss.",
             ]},
         ],
         "callout": "Consistency beats intensity every time. Show up twice a week, progressively challenge yourself, and let time do the work."
         },
        {"title": "Nutrition Timing Around Training",
         "intro": "When you eat — and what you eat — around training sessions matters more when appetite is suppressed.",
         "sections": [
             {"heading": "Pre-Workout Nutrition on GLP-1", "body": [
                 "Training on a completely empty stomach when appetite is suppressed is a common pattern on GLP-1 and a problematic one. Without pre-workout fuel, performance suffers, the workout stimulus is reduced, and muscle breakdown during the session is higher.",
                 "A small pre-workout meal or snack — thirty to sixty minutes before training, containing 20–30 grams of protein and some carbohydrate — significantly improves training performance and reduces muscle breakdown. If solid food is unappealing before training, a protein shake with a banana or piece of fruit is an effective alternative.",
             ]},
             {"heading": "Post-Workout Protein", "body": [
                 "The post-workout period is when the muscle repair and synthesis process is most active. Consuming protein within one to two hours of resistance training consistently improves the body's ability to build and preserve lean tissue from that training session.",
                 "Target 25–40 grams of protein in the post-workout meal or snack. Leucine is the key amino acid for post-workout muscle protein synthesis — found in highest concentrations in whey protein, eggs, and most animal proteins. A whey protein shake is practical and effective if appetite for solid food is limited post-workout.",
             ]},
         ],
         "callout": "Feed the training. Even when you're not hungry, the muscle is asking."
         },
        {"title": "Tracking Progress Beyond the Scale",
         "intro": "Body composition changes on a well-executed GLP-1 plus training programme are often better than the scale suggests.",
         "sections": [
             {"heading": "Measuring Body Composition", "body": [
                 "A DEXA scan is the gold standard for measuring lean mass and fat mass separately. Many gyms, hospitals, and wellness centres offer these for a modest fee, and a scan at the start and end of your programme gives you accurate data on whether your lean mass is being preserved.",
                 "Practical proxies if scanning isn't accessible: clothing fit (how do clothes that were tight in certain places now fit?), gym performance (are you lifting the same or more weight than when you started?), measurements at key sites (waist, hips, upper arm, thigh). Performance and measurements together tell you more than the scale alone.",
             ]},
             {"heading": "The Long-Term Picture", "body": [
                 "The combination of GLP-1 medication and progressive strength training produces a result that neither achieves alone: significant fat loss with preserved or improved lean mass, resulting in a body composition that is metabolically healthier than weight loss without training produces. This combination is increasingly recognised in obesity medicine as the standard of care — medication alongside lifestyle intervention rather than medication alone.",
             ]},
         ],
         "callout": "The goal is a stronger, leaner, more metabolically healthy body. The scale is one data point. Don't let it be the only one."
         },
    ]
)

B05 = make_book(
    "The GLP-1 Meal Prep Playbook",
    "High-Protein, Low-Nausea Recipes That Work",
    [
        {"title": "Meal Prep on GLP-1 — Why It Matters More Than Usual",
         "intro": "When appetite is suppressed, the foods you have available determine the foods you eat. Meal prep on GLP-1 is not about eating more — it's about ensuring that when appetite is limited, the available options are protein-forward, nutrient-dense, and easy to eat.",
         "sections": [
             {"heading": "The Meal Prep Advantage", "body": [
                 "GLP-1 users who meal prep consistently eat more protein, make better food choices, and report fewer side effects than those who rely on spontaneous eating decisions. The reason is simple: when you're not hungry and food doesn't appeal, you default to whatever is easiest. If what's easiest is a bag of crackers, that's what you eat. If what's easiest is a pre-made bowl of Greek yoghurt with berries, or a container of chicken and roasted vegetables, that's what you eat instead.",
                 "The investment is two to three hours once or twice a week. The return is a week of eating that supports your goals without requiring daily effort or decision-making about food.",
             ]},
             {"heading": "GLP-1 Meal Prep Principles", "body": [
                 "Protein first in every container. Every meal prep item should anchor around a protein source. The protein goes in first, then vegetables, then carbohydrates if included.",
                 "Small portions by default. Prep in smaller containers than you'd normally use. Seeing a full container is psychologically different from seeing a normal-sized portion when appetite is suppressed. Smaller containers that feel completable are more likely to be eaten.",
                 "Temperature flexibility. Prep foods that are palatable cold, at room temperature, or warm. On high-nausea days, reheating food may feel impossible. Having options that work cold removes that barrier.",
             ]},
         ],
         "callout": "You don't make food decisions when you're hungry on GLP-1. You make them when you're not. Meal prep is how you make decisions in advance."
         },
        {"title": "High-Protein Recipes Designed for GLP-1",
         "intro": "These recipes are designed specifically for the GLP-1 context: high in protein, easy on the stomach, tolerable on low-appetite days, and practical to prep in bulk.",
         "sections": [
             {"heading": "Greek Yoghurt Protein Bowls", "body": [
                 "Base: 200g full-fat or 2% Greek yoghurt (20g protein). Add: 30g protein powder mixed in (additional 20–25g protein), a tablespoon of almond butter (4g protein, healthy fat), a handful of berries, and a tablespoon of chia seeds (for fibre and omega-3).",
                 "Total protein: approximately 45–50g. Total preparation time: 3 minutes. These keep well in the refrigerator for up to three days and are palatable cold. The combination of yoghurt protein and whey protein provides both fast-digesting (whey) and slow-digesting (casein from yoghurt) protein sources.",
             ]},
             {"heading": "Baked Chicken and Roasted Vegetables", "body": [
                 "Season 150–180g chicken breast with olive oil, garlic, smoked paprika, and salt. Bake at 200°C/400°F for 22–25 minutes. Alongside: roughly chop courgette, bell peppers, and cherry tomatoes, toss with olive oil and seasoning, roast for 20 minutes.",
                 "Prep eight servings at once: the cooking time is the same for one as for eight. Divide into containers. 150g chicken breast provides approximately 35g protein. The vegetables provide fibre, micronutrients, and enough volume to make the meal feel substantial.",
             ]},
             {"heading": "Cottage Cheese and Egg Scramble", "body": [
                 "Two whole eggs scrambled with 100g cottage cheese: the cottage cheese melts into the eggs during cooking, creating a soft, high-protein scramble that is significantly higher in protein than eggs alone (25–28g total). Season simply with salt and chives.",
                 "This is one of the most nausea-friendly high-protein options because the texture is soft, the flavour is mild, and it's quick to make even when appetite is low. It also provides casein protein from the cottage cheese, which digests slowly and supports overnight muscle protein synthesis if eaten in the evening.",
             ]},
             {"heading": "Tuna and White Bean Salad", "body": [
                 "One can of tuna in water (25g protein) mixed with half a can of white beans (7g protein), cherry tomatoes, cucumber, olive oil, lemon juice, and capers. Total protein approximately 32g. Can be eaten cold directly from the refrigerator. Prep six servings on Sunday.",
                 "The white beans add fibre that supports the constipation management critical on GLP-1. The olive oil provides healthy fat for fat-soluble vitamin absorption. The lemon and capers make this palatable even when appetite is low.",
             ]},
         ],
         "callout": "Simple, protein-dense, and palatable on a bad day. That's the brief."
         },
        {"title": "Navigating Eating Out on GLP-1",
         "intro": "Most of life doesn't happen in your meal-prepped kitchen. Here's how to navigate restaurants, social eating, and travel.",
         "sections": [
             {"heading": "Restaurant Strategies", "body": [
                 "Order protein first, and order it simply. Grilled or baked protein with vegetables is available at almost every restaurant. Sauces, complex preparations, and large portions are the main challenges — all of which worsen nausea. Asking for sauces on the side, ordering half portions, or sharing a main course are practical strategies that most restaurants accommodate without difficulty.",
                 "Don't feel obligated to finish. The social pressure to clean your plate is real, but eating past the point of comfortable fullness on GLP-1 produces significant discomfort. Eating slowly, stopping when you feel comfortable, and being honest with dining companions about your situation (if comfortable doing so) protects both your health and your enjoyment of the meal.",
             ]},
             {"heading": "Travel and GLP-1", "body": [
                 "Air travel dehydrates. High-sodium airport food worsens fluid retention and compounds nausea. Long periods of sitting slow gut motility further. Pack protein-dense, portable snacks for travel: individual packets of nut butter, protein bars with at least 20g protein and reasonable ingredients, boiled eggs if carrying a cool bag.",
                 "Medication storage during travel: semaglutide and tirzepatide require refrigeration but can be at room temperature for up to 56 days (check your specific medication's guidance). A portable medication cooler is worth having for long-haul travel.",
             ]},
         ],
         "callout": "The goal isn't perfect eating. It's good-enough eating in the real conditions of your actual life."
         },
        {"title": "Building Sustainable Eating Patterns",
         "intro": "The eating patterns you build on GLP-1 are the eating patterns you need to maintain after.",
         "sections": [
             {"heading": "The Eating Pattern That Lasts", "body": [
                 "The Mediterranean dietary pattern — abundant vegetables, fruits, legumes, whole grains, olive oil, fish, moderate dairy and poultry, limited red meat and ultra-processed food — is the dietary pattern with the most consistent long-term evidence for weight maintenance, cardiovascular health, and metabolic health. It also happens to align naturally with the protein-first, high-vegetable approach appropriate on GLP-1.",
                 "Building the Mediterranean pattern habits during GLP-1 treatment means that when the medication stops — or the dose reduces — the dietary foundation is already in place. This is the evidence-based approach to preventing the weight regain that characterises GLP-1 treatment without lifestyle change.",
             ]},
         ],
         "callout": "You're not on a temporary diet. You're building the eating pattern of the rest of your life."
         },
    ]
)

B06 = make_book(
    "GLP-1 for Long-Term Success",
    "Life After the Medication",
    [
        {"title": "The Discontinuation Reality",
         "intro": "Most people who take GLP-1 medications will eventually stop them — due to cost, side effects, personal choice, or achieving their goals. The research on what happens after is important and often not discussed with patients beforehand.",
         "sections": [
             {"heading": "What Happens When You Stop", "body": [
                 "The STEP 4 trial, which followed patients after stopping semaglutide, found that within one year of discontinuation, participants regained approximately two-thirds of the weight lost during treatment. Hunger and appetite returned to pre-treatment levels within weeks. This is not a personal failure — it's the biological homeostatic response to the removal of a pharmacological signal.",
                 "The two most protective factors against regain are, consistently: the lifestyle habits built during treatment (particularly resistance training and protein-forward eating) and the metabolic state at the time of discontinuation (people who maintained more lean mass regained less fat proportionally).",
             ]},
             {"heading": "Planning for the Transition", "body": [
                 "Successful long-term management after GLP-1 requires planning the transition before it happens. The questions to address with your provider before stopping: What is the taper schedule? What hunger management strategies are in place? What eating and exercise habits are established well enough to maintain without pharmacological support?",
                 "Abrupt discontinuation is harder than gradual reduction. Most providers recommend a taper — reducing dose before stopping entirely — to allow the body's appetite regulation to begin readjusting before the full pharmacological support is removed.",
             ]},
         ],
         "callout": "Stopping GLP-1 is not the end of the journey. It's a transition to a different chapter. The preparation happens before you stop."
         },
        {"title": "The Habits That Bridge the Gap",
         "intro": "The gap between GLP-1-assisted weight management and long-term maintenance is bridged by specific habits.",
         "sections": [
             {"heading": "Resistance Training as the Foundation", "body": [
                 "Of all the lifestyle interventions that predict long-term weight maintenance, resistance training has the strongest evidence. It preserves lean mass (which maintains metabolic rate), improves insulin sensitivity (which supports healthy body composition), and has independent psychological benefits — self-efficacy, stress management, mood — that support the broader behaviour change required for maintenance.",
                 "The goal is to reach a point, before stopping GLP-1, where resistance training is an automatic, non-negotiable part of the weekly schedule — not because it feels like medicine, but because it feels like part of your identity.",
             ]},
             {"heading": "Managing the Return of Hunger", "body": [
                 "When GLP-1 appetite suppression lifts, hunger returns. For most people, it returns to pre-treatment levels or slightly above, due to the homeostatic response to weight loss. Having a pre-planned response to this — a structured eating pattern, awareness of which foods trigger the most hunger and which provide the most satiety, and specific strategies for high-hunger moments — prevents the hunger from driving food decisions by default.",
                 "High-protein, high-fibre, moderate-fat meals provide the most sustained satiety. Processed foods engineered for palatability — ultra-sweet, ultra-salty, ultra-fatty combinations — override the satiety mechanisms most efficiently. Reducing exposure to these foods in the environment (not buying them, not keeping them in the house) is more effective than relying on willpower in the moment.",
             ]},
         ],
         "callout": "The medication changed your weight. The habits change your life."
         },
        {"title": "If You Return to GLP-1",
         "intro": "Returning to GLP-1 medication after a period off is common and appropriate in many cases.",
         "sections": [
             {"heading": "GLP-1 as Chronic Management", "body": [
                 "The medical community is increasingly framing obesity as a chronic condition requiring ongoing management, similar to hypertension or diabetes. For many people, this means that GLP-1 treatment is not a finite course but an ongoing management strategy — with potential periods on and off depending on circumstances, cost, and individual goals.",
                 "There is no evidence that returning to GLP-1 after a period off reduces efficacy. The physiological mechanisms are not subject to tolerance in the same way as some medications. If circumstances change and returning to medication is appropriate, it is both medically reasonable and consistent with a chronic disease management framework.",
             ]},
         ],
         "callout": "There is no shame in using effective medication for a chronic condition. The stigma is the problem, not the treatment."
         },
        {"title": "The Bigger Picture — Metabolic Health for Life",
         "intro": "The goal was never just a number on the scale.",
         "sections": [
             {"heading": "What GLP-1 Actually Changes", "body": [
                 "Beyond weight, GLP-1 medications have demonstrated significant reductions in cardiovascular events (the SELECT trial showed a 20% reduction in major cardiovascular events in people without diabetes), improvements in blood pressure and lipids, reduction in inflammatory markers, improvements in sleep apnoea, and emerging evidence for benefits in non-alcoholic fatty liver disease and kidney disease.",
                 "These are not cosmetic benefits. They are significant, measurable health improvements that extend life and reduce chronic disease burden. Framing GLP-1 treatment as primarily about appearance misses the actual value proposition.",
             ]},
             {"heading": "Living Well Beyond the Scale", "body": [
                 "The people who do best long-term after GLP-1 treatment are those who used the treatment period to build a different relationship with food, movement, and their body. Not a perfect relationship — but a more informed, more intentional, and more compassionate one. The habits, the knowledge, and the changed physiology create a foundation that serves health for the years ahead.",
             ]},
         ],
         "callout": "You didn't do all this just to weigh less. You did it to live better."
         },
    ]
)

B07 = make_book(
    "Hair Loss on GLP-1",
    "What's Really Happening and How to Minimize It",
    [
        {"title": "Why Hair Loss Happens on GLP-1",
         "intro": "Hair loss is one of the more distressing side effects of GLP-1 treatment — partly because it's not immediately obvious why a weight loss medication would cause hair to shed, and partly because hair loss carries significant psychological weight for most people.",
         "sections": [
             {"heading": "Telogen Effluvium — The Mechanism", "body": [
                 "The hair loss most commonly reported by GLP-1 users is telogen effluvium — a form of temporary, diffuse shedding triggered by a significant physiological stress. It's the same type of hair loss that occurs after major surgery, severe illness, childbirth, extreme emotional stress, and any other significant metabolic disruption.",
                 "Hair follicles cycle through active growth (anagen), transition (catagen), and resting/shedding (telogen) phases. Significant physiological stress pushes a larger-than-normal proportion of follicles simultaneously into the telogen phase. The shedding, which occurs as these resting follicles release the hair shaft, typically begins two to three months after the triggering event — which is why people on GLP-1 often don't experience hair loss until several months into treatment.",
                 "The good news about telogen effluvium: it is self-limiting. The follicles are not permanently damaged. When the triggering stress resolves — which for GLP-1 means when the body adapts to the new weight and eating pattern — the follicles return to normal cycling and the hair regrows, usually within three to six months of the shedding stopping.",
             ]},
             {"heading": "What Makes It Worse", "body": [
                 "Rapid weight loss is the primary trigger. The faster the weight is lost, the more physiological stress the body experiences, and the more pronounced the telogen effluvium. This is why GLP-1 users on faster-escalating doses or with higher initial rates of weight loss often report more hair loss.",
                 "Protein deficiency significantly worsens hair loss. Hair is made primarily of keratin — a protein. When protein intake is inadequate, the body deprioritises protein for hair growth in favour of maintaining organ function and lean tissue. Inadequate protein during GLP-1-assisted weight loss compounds the telogen effluvium with protein-deficiency hair loss.",
                 "Micronutrient deficiencies — particularly iron, zinc, and biotin — also contribute. These are common on reduced calorie intakes and all play roles in healthy hair follicle function.",
             ]},
         ],
         "callout": "The hair will come back. The follicles aren't gone. But there are things you can do to reduce the shedding."
         },
        {"title": "Minimising Hair Loss on GLP-1",
         "intro": "You cannot entirely prevent telogen effluvium during significant weight loss. You can meaningfully reduce its severity.",
         "sections": [
             {"heading": "Protein — The Most Important Intervention", "body": [
                 "Meeting protein targets is the single most important thing you can do to minimise hair loss on GLP-1. A minimum of 1.2–1.6 grams of protein per kilogram of body weight per day provides the amino acids required for hair follicle function. In practice, this means prioritising protein at every meal and supplementing with protein shakes if food intake is insufficient to reach targets.",
                 "Collagen peptides deserve specific mention in the context of hair loss. Collagen is rich in the amino acids glycine, proline, and hydroxyproline — precursors for keratin synthesis. While the evidence for collagen supplementation specifically for GLP-1 hair loss is limited, the general evidence for hair, skin, and nail structure is reasonable, and the side effect profile is excellent.",
             ]},
             {"heading": "Targeted Micronutrients", "body": [
                 "Iron: have your ferritin checked if you're experiencing significant hair loss. Ferritin (stored iron) can be in the normal reference range while still being insufficient for optimal hair growth. Most hair loss specialists recommend a ferritin level above 70 ng/mL for hair growth support, though the standard 'normal' range starts at 12–15.",
                 "Zinc: a cofactor for multiple enzymes involved in hair growth. Common in meat, shellfish, legumes, nuts, and seeds. Supplementation is appropriate if dietary intake is low or blood levels are below optimal.",
                 "Biotin: widely marketed for hair growth. The evidence for biotin supplementation in people without a biotin deficiency is actually limited. However, it is safe and inexpensive, and GLP-1 users may have reduced biotin intake from reduced food variety. 5000mcg per day is the typical supplement dose.",
             ]},
             {"heading": "Stress Management", "body": [
                 "Chronic psychological stress independently increases cortisol, which promotes telogen effluvium. The nervous system regulation practices throughout this series — breathwork, movement, sleep — all contribute to stress management and thus, indirectly, to hair health during the weight loss period.",
             ]},
         ],
         "callout": "Eat enough protein. Check your iron. Be patient. The hair comes back."
         },
        {"title": "Scalp Care During Shedding",
         "intro": "Practical scalp and hair care that minimises the appearance of shedding and supports follicle health.",
         "sections": [
             {"heading": "Hair Care Adjustments", "body": [
                 "Gentle handling reduces mechanical hair loss on top of telogen effluvium shedding. Avoid tight hairstyles (ponytails, braids) that put traction on the follicle. Use a wide-tooth comb rather than a brush on wet hair. Minimise heat styling. These adjustments don't change the underlying telogen effluvium, but they reduce the additional shedding from physical manipulation.",
                 "Scalp massages with a scalp massager or fingertips have reasonable evidence for stimulating blood flow to follicles and may modestly support regrowth. They're also pleasant and stress-reducing, which has secondary benefits.",
             ]},
             {"heading": "When to See a Dermatologist", "body": [
                 "If hair loss is severe, patterned (not diffuse), accompanied by scalp changes, or not improving six months after weight loss has stabilised, a dermatologist can assess for other causes — including androgenetic alopecia, thyroid disorders, and other conditions that require specific treatment.",
                 "Telogen effluvium from GLP-1 typically resolves without medical intervention once the triggering stress reduces. Hair loss that is persistent or progressive beyond this warrants professional evaluation.",
             ]},
         ],
         "callout": "Temporary is the key word. Manage it, support it, and let time do the rest."
         },
    ]
)

B08 = make_book(
    "GLP-1 and Mental Health",
    "The Emotional Side of Rapid Weight Loss",
    [
        {"title": "The Emotional Landscape of GLP-1 Treatment",
         "intro": "GLP-1 medications change your relationship with food in ways that go far deeper than appetite. For many people, food has been a source of comfort, pleasure, social connection, and identity management for decades. When the medication significantly reduces that relationship, the emotional consequences can be unexpected and significant.",
         "sections": [
             {"heading": "When Food Loses Its Comfort Function", "body": [
                 "Emotional eating — using food to manage difficult emotions — is extremely common. Studies suggest that 30–50% of adults engage in some degree of emotional eating. GLP-1 medications reduce the appetite and the reward value of food simultaneously, which for emotional eaters can mean losing a coping mechanism without having an alternative in place.",
                 "The emotional states that previously led to eating — boredom, stress, loneliness, anxiety, sadness — don't disappear when the appetite does. Without the food-based coping, they need to be managed differently. For some people, this means those emotions become more prominent than before, surfacing without the buffering that food provided.",
             ]},
             {"heading": "Mood Changes on GLP-1", "body": [
                 "GLP-1 receptors are present in the brain, including in areas involved in mood regulation and reward. Some people report improvement in mood and reduction in anxiety on GLP-1 — possibly related to the medication's direct neurological effects, the metabolic improvements, or the positive psychological effects of weight loss. Others report mood worsening, increased anxiety, or emotional flatness.",
                 "The FDA added a monitoring requirement for suicidal ideation to GLP-1 labels based on case reports, though subsequent analyses have not found a causal link and some studies suggest GLP-1 may have antidepressant effects. If mood changes are significant or include thoughts of self-harm, contact your healthcare provider immediately.",
             ]},
         ],
         "callout": "Weight loss changes your body. It doesn't automatically change the emotional relationship with food that developed over a lifetime."
         },
        {"title": "Identity, Body Image, and Rapid Change",
         "intro": "When the body changes quickly, the mind doesn't always keep up.",
         "sections": [
             {"heading": "The Identity Adjustment", "body": [
                 "Identity is partly anchored in the body. Many people who have lived in larger bodies for years have built coping strategies, social roles, personality adaptations, and self-narratives that relate to their body size. When the body changes significantly and quickly, these identity anchors shift — which can produce unexpected grief, disorientation, and questions about self.",
                 "This is not unique to GLP-1 — bariatric surgery patients have described the same experience for decades. But GLP-1 produces it in a population that didn't expect it: people who thought they just wanted to weigh less, and find that the weight loss brought more complexity than they anticipated.",
             ]},
             {"heading": "Body Dysmorphia and Perception Lag", "body": [
                 "Many people who lose significant weight on GLP-1 continue to perceive themselves in their previous body for months or years after the physical change. Looking in a mirror and not recognising the reflection. Reaching for the larger size in a clothing store by habit. The brain's body map updates slowly relative to the actual physical change.",
                 "This perception lag is normal and resolves with time. It can be disorienting in the interim, particularly when others' reactions to the changed body create a social reality that doesn't match the internal experience.",
             ]},
         ],
         "callout": "The body can change faster than the psyche. Both deserve attention."
         },
        {"title": "Psychological Support During Treatment",
         "intro": "GLP-1 works best as part of a comprehensive approach that includes psychological support.",
         "sections": [
             {"heading": "Therapy and GLP-1", "body": [
                 "Cognitive behavioural therapy for obesity (CBT-O) and acceptance and commitment therapy (ACT) both have evidence for supporting long-term weight management and the psychological adjustments that accompany significant body change. A therapist experienced in body image, eating, and weight — not necessarily an eating disorder specialist, but one with this background — can provide support that the medication cannot.",
                 "Many GLP-1 users find that having professional psychological support during treatment significantly improves both the experience of treatment and the long-term outcomes, by addressing the emotional and behavioural dimensions that the medication doesn't touch.",
             ]},
             {"heading": "Building New Coping Skills", "body": [
                 "The most protective investment during GLP-1 treatment is building alternative coping skills for the emotional states that previously led to eating. The somatic practices throughout this series — breathwork, movement, grounding — are specifically relevant here. They address the physiological states (stress, boredom, anxiety) that drove emotional eating without the metabolic consequences of food-based coping.",
             ]},
         ],
         "callout": "Taking care of the emotional side is not a luxury. It's what makes the physical results sustainable."
         },
    ]
)

B09 = make_book(
    "GLP-1 on a Budget",
    "Making the Most of Your Medication Without Breaking the Bank",
    [
        {"title": "The Cost Reality",
         "intro": "GLP-1 medications are among the most expensive prescription drugs in the world. Without insurance coverage, Ozempic and Wegovy can cost $900–$1,400 per month in the United States. This makes access profoundly inequitable and forces many patients to make difficult financial decisions. This chapter is about navigating that reality practically.",
         "sections": [
             {"heading": "Understanding Your Coverage Options", "body": [
                 "Insurance coverage for GLP-1 medications varies widely. Ozempic (semaglutide 0.5mg–2mg) is typically covered for type 2 diabetes. Wegovy (semaglutide 2.4mg) is the obesity-indication version and has more variable coverage — many insurance plans exclude weight management medications.",
                 "Medicare does not cover GLP-1 medications for weight management (though this may change with legislative updates), but does cover them for diabetes. Medicaid coverage varies by state. Commercial insurance increasingly covers them for obesity with a BMI threshold, though prior authorisation and step therapy requirements are common.",
                 "The first practical step: call your insurance company and ask specifically: 'Is semaglutide or tirzepatide covered under my plan for weight management?' If yes, what are the step therapy requirements and what documentation does my doctor need to provide?",
             ]},
             {"heading": "Manufacturer Savings Programs", "body": [
                 "Novo Nordisk (Ozempic/Wegovy) and Eli Lilly (Mounjaro) offer savings programs for commercially insured patients that can significantly reduce out-of-pocket costs — sometimes to as low as $25 per month. These programs have income eligibility requirements and specific conditions.",
                 "The Novo Nordisk Patient Assistance Program and the Eli Lilly Insulin Value Program (which also covers Mounjaro for qualifying patients) are the primary options. Patient advocacy organisations including the Obesity Action Coalition maintain current information on access programs as these change frequently.",
             ]},
         ],
         "callout": "The cost is real. The options are more numerous than most people know. Advocate for access."
         },
        {"title": "Maximising Medication Efficiency",
         "intro": "When medication is expensive, every dose needs to work as hard as possible.",
         "sections": [
             {"heading": "Lifestyle as a Multiplier", "body": [
                 "The combination of GLP-1 medication with protein-prioritised eating and resistance training consistently produces better body composition outcomes than medication alone. This matters not just for health but for medication efficiency: better muscle preservation means better metabolic outcomes with the same medication dose.",
                 "Sleep, stress management, and the nervous system regulation practices throughout this series all support the medication's effectiveness. GLP-1 works through multiple mechanisms — including effects on the stress and reward systems — that are more available when the nervous system is regulated.",
             ]},
             {"heading": "Managing Dose Escalation Strategically", "body": [
                 "You don't have to escalate to the maximum dose on the manufacturer's recommended schedule. The appropriate dose is the lowest dose that provides adequate benefit with tolerable side effects. Some people achieve their goals at lower doses than the maximum — and lower doses cost less.",
                 "Having this conversation with your provider — 'I'm having good results at this dose; can we discuss whether escalation is necessary?' — is entirely appropriate. The goal is your health outcomes, not adherence to a schedule.",
             ]},
         ],
         "callout": "An expensive medication that works is more cost-effective than a cheaper one that doesn't. Maximise what you're already spending."
         },
        {"title": "International and Compounding Options",
         "intro": "The geographic disparity in GLP-1 pricing has created options for cost reduction that are worth understanding.",
         "sections": [
             {"heading": "International Pharmacy Options", "body": [
                 "Semaglutide is available in many countries at a fraction of US prices. In Canada, the UK, and many European countries, the same medication costs $100–$300 per month. Several legal international pharmacy services allow US residents to purchase medications from licensed international pharmacies — an area of legal grey but common practice that is not federally prosecuted for personal use quantities.",
                 "NABP-accredited international pharmacies and services like Canada Drugs Direct and Canada Pharmacy operate in this space. The medications are the same molecular compound manufactured to the same standards — the price difference reflects US pharmaceutical pricing policy, not manufacturing quality.",
             ]},
             {"heading": "Compounding Pharmacies", "body": [
                 "During the semaglutide shortage period (2023–2024), the FDA allowed compounding pharmacies to produce compounded semaglutide at significantly lower prices. The compounding market for GLP-1 peptides has been controversial — quality varies by pharmacy, and the FDA has issued warnings about some providers.",
                 "If using compounded GLP-1, verification of PCAB accreditation (the pharmacy compounding accreditation board standard) and prescriber oversight are the minimum appropriate safeguards. This is not a do-it-yourself option — it requires a prescribing provider and a reputable compounding pharmacy.",
             ]},
         ],
         "callout": "Access to effective medication should not depend on where you were born or how much you earn. Know your options."
         },
    ]
)

B10 = make_book(
    "The GLP-1 Fasting Protocol",
    "Combining Intermittent Fasting with Your Medication",
    [
        {"title": "Does Intermittent Fasting and GLP-1 Work Together?",
         "intro": "Intermittent fasting and GLP-1 medications both reduce calorie intake — IF by restricting the eating window, GLP-1 by reducing appetite. The question is whether combining them produces additional benefits, makes the experience better or worse, or requires any adjustments to either approach.",
         "sections": [
             {"heading": "The Overlap and the Difference", "body": [
                 "GLP-1 medications naturally produce a pattern that resembles intermittent fasting in many users — appetite is suppressed for significant portions of the day, and many people find themselves eating within a restricted window without deliberately planning to. In this sense, IF may be a description of what GLP-1 users are already doing rather than an additional intervention.",
                 "The additional benefit of deliberate IF over the spontaneous appetite suppression of GLP-1 is debated. Some research suggests IF produces independent metabolic benefits — improved insulin sensitivity, enhanced autophagy (cellular cleanup), and circadian rhythm alignment — beyond calorie restriction alone. Others suggest the benefits are primarily calorie-reduction effects.",
             ]},
             {"heading": "GLP-1 and Fasting — The Concerns", "body": [
                 "The primary concern with combining GLP-1 and IF is protein adequacy. Both approaches reduce the eating window and total food intake. If the remaining eating window doesn't include sufficient protein, the muscle preservation challenge on GLP-1 is compounded.",
                 "The second concern is nausea. GLP-1 users who fast for extended periods and then eat a larger meal in a compressed window may find that the delayed gastric emptying produces significant nausea when larger amounts of food arrive in a stomach that has been empty for an extended period. Smaller, more frequent eating may be better tolerated than the traditional large-meal IF pattern.",
             ]},
         ],
         "callout": "GLP-1 already changes how and when you eat. Any additional protocol should work with that, not against it."
         },
        {"title": "The Practical Protocol",
         "intro": "For those who want to combine GLP-1 with a deliberate fasting structure, here is the approach most compatible with GLP-1's specific demands.",
         "sections": [
             {"heading": "The Modified 16:8 on GLP-1", "body": [
                 "A 16:8 approach — 16 hours fasting, 8 hours eating window — is the most commonly used IF protocol and the one most compatible with GLP-1 for most people. The eating window should be aligned with daylight hours where possible (e.g., 10am–6pm or 11am–7pm), since this aligns with circadian metabolic patterns that support insulin sensitivity.",
                 "Within the eight-hour window on GLP-1: prioritise protein at the first meal of the day. Distribute protein across at least two to three eating occasions within the window rather than one large meal. This maximises muscle protein synthesis stimulation (which requires at least 20–30g protein per serving to maximally stimulate) relative to a single large bolus.",
             ]},
             {"heading": "What to Eat During the Eating Window", "body": [
                 "On GLP-1 with IF, the eating window needs to carry the full protein and micronutrient load for the day in a compressed time. This means every meal and snack within the window should be nutrient-dense. The Mediterranean-style framework applies: protein-centred meals with abundant vegetables, legumes, olive oil, and whole grains where appetite allows.",
                 "Avoid the pattern of using the fasting window as justification for lower nutritional quality in the eating window. The reduced calorie intake means the quality of what is eaten matters proportionally more.",
             ]},
         ],
         "callout": "A good protocol fits your biology. Adjust the protocol to serve you, not the other way around."
         },
        {"title": "When Fasting on GLP-1 Is Not Appropriate",
         "intro": "Not everyone should combine IF with GLP-1.",
         "sections": [
             {"heading": "Contraindications and Cautions", "body": [
                 "If you have a history of disordered eating — particularly restriction-based patterns, orthorexia, or binge-restrict cycles — the combination of appetite-suppressing medication with deliberate food restriction is not appropriate and warrants evaluation by an eating disorder specialist before consideration.",
                 "If you are taking GLP-1 for type 2 diabetes alongside other glucose-lowering medications, fasting requires additional monitoring and adjustment of medication timing. Discuss this explicitly with your prescriber.",
                 "If the motivation for adding IF on top of GLP-1 is a desire to lose weight faster than the medication alone is producing, consider whether the pace of loss is already appropriate. Rapid weight loss produces more muscle loss, more hair loss, and more nutritional deficiency risk. Faster is not always better.",
             ]},
         ],
         "callout": "More is not always more. Sometimes the right protocol is simply letting the medication do its job."
         },
    ]
)

# ─────────────────────────────────────────────────────────────────────────────
# GENERATE ALL
# ─────────────────────────────────────────────────────────────────────────────
books = [
    ("01 - The GLP-1 Nutrition Guide.pdf", B01),
    ("02 - GLP-1 for Women Over 40.pdf", B02),
    ("03 - Managing GLP-1 Side Effects.pdf", B03),
    ("04 - GLP-1 and Strength Training.pdf", B04),
    ("05 - The GLP-1 Meal Prep Playbook.pdf", B05),
    ("06 - GLP-1 for Long-Term Success.pdf", B06),
    ("07 - Hair Loss on GLP-1.pdf", B07),
    ("08 - GLP-1 and Mental Health.pdf", B08),
    ("09 - GLP-1 on a Budget.pdf", B09),
    ("10 - The GLP-1 Fasting Protocol.pdf", B10),
]

if __name__ == "__main__":
    for filename, data in books:
        out = os.path.join(BASE, filename)
        generate_ebook(out, data)
