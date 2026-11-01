# VidyaRL: The Learning GPS[cite: 4]

A simpler, smarter way to adapt education for Indian students and empower their teachers[cite: 4].

## Core Promise
Find the learning gap early, adapt the explanation, and give the teacher a clear, actionable next step for the classroom[cite: 4].

## 01. The Problem: The Moving Train
Imagine a typical Indian classroom of 50 students as a moving train[cite: 4]. The teacher has a massive syllabus to cover, so the lesson often moves at one strict pace[cite: 4]. 

* **One Speed vs. Language Gap:** Fast learners often get bored, while students needing more time fall behind[cite: 4]. Students may study in English but understand concepts more easily in their home language[cite: 4].
* **Late Discovery vs. Device Limits:** Misunderstandings are found too late (post-exam)[cite: 4]. Digital solutions often fail because students share a single family phone with unreliable internet access[cite: 4].
* **Teacher Overload:** One teacher cannot manually track the exact learning gaps of 50 students simultaneously, leading to generalized teaching that misses individual needs[cite: 4].
* **Teacher Bypass:** Most global adaptive apps try to bypass or replace the school system[cite: 4]. Tools are much less useful when they sideline teachers rather than supporting them[cite: 4].

## 02. The Idea: AI as a Learning GPS
VidyaRL uses Reinforcement Learning (RL) as an adaptive teaching guide[cite: 5]. Like a GPS that recalculates after a wrong turn, the system tries different teaching methods to find what works for a specific student[cite: 5].

### Core AI Loop
1. **Learn:** Repairs prerequisite gaps instantly with a short visual reminder or an accessible explanation[cite: 5].
2. **Solve:** Asks students to solve problems step-by-step so the AI can pinpoint exactly where logic breaks down[cite: 5].
3. **Test:** Uses follow-up diagnostic questions to confirm the student's understanding has improved before moving on[cite: 5].

### Smart Adaptation
* **Solving the Cold-Start Problem:** During onboarding, VidyaRL offers a gamified diagnostic[cite: 5]. Using Bayesian Knowledge Tracing (BKT), it estimates initial mastery before the RL agent takes over to guide ongoing learning dynamically[cite: 5].
* **Strategic Language Support:** The AI uses a natural mixed-language style (Hinglish/Tanglish) to bridge the language gap without hurting board exam performance[cite: 5]. It translates the conversational logic into the regional language but retains essential STEM terms in English[cite: 5].

## 03. Putting Teachers Back in Charge
VidyaRL converts complex student activity into a short, actionable morning briefing[cite: 6]. 

| Report Level | What the Teacher Sees | Actionable Outcome |
| :--- | :--- | :--- |
| **Class Overview** | Topic mastery summary, class trends, and specific foundational concepts that many students missed[cite: 6]. | Helps the teacher decide whether to reteach a concept to the entire class[cite: 6]. |
| **Student Profile** | Recent progress, likely prerequisite gaps, repeated error patterns, and RL confidence levels[cite: 6]. | Provides targeted, one-on-one support for specific student struggles[cite: 6]. |
| **Action Plan** | Suggested groups, peer-mentor options, and offline-friendly printable worksheets[cite: 6]. | Turns digital data directly into today's physical lesson plan[cite: 6]. |

**Realistic Grouping: Peer Mentor Routing**
A single teacher may struggle to supervise five groups at once[cite: 6]. The dashboard automatically suggests pairing a student who has demonstrated mastery of a concept to support a small group practicing that same concept[cite: 6]. The teacher approves the pairing and sets a clear, bounded task, easing their instructional burden[cite: 6].

## 04. Plan & Technology Stack

| System Layer | Implementation Strategy |
| :--- | :--- |
| **Student App (PWA)** | A lightweight Progressive Web App designed for low data use and affordable smartphones[cite: 6]. It caches learning materials to survive intermittent connectivity[cite: 6]. |
| **Learning Engine** | Python-based services manage state estimates[cite: 6]. Uses BKT for early baseline estimates and Reinforcement Learning for dynamic, step-by-step route recalculation[cite: 6]. |
| **Language Support** | Integration with local Indian AI models (like the Bhashini API) to instantly translate hints into natural, mixed-language audio while preserving technical vocabulary[cite: 6]. |
| **Teacher Cockpit** | A clean web dashboard that aggregates data into class trends, student profiles, and generates printable offline worksheets for hardware-limited classrooms[cite: 6]. |
