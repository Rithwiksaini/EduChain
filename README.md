# VidyaRL: The Learning GPS 🧭

> **A simpler, smarter way to adapt education for Indian classrooms and empower their teachers.**

---

## 📌 Core Promise
Find the learning gap early, adapt the explanation dynamically, and give the teacher a clear, actionable next step for the classroom.

---

## 🚨 The Problem: "The Moving Train"
In a typical Indian classroom of 50 students, the curriculum moves forward like a strict train schedule:
* **One Speed vs. Language Gap:** Fast learners get bored while others fall behind. Students studying in English often think and comprehend concepts faster in their home language.
* **Late Discovery vs. Device Limits:** Misconceptions are caught too late (post-exam). Meanwhile, digital EdTech often fails because students share a single family smartphone with intermittent internet connectivity.
* **Teacher Overload:** One teacher cannot manually track the micro-gaps of 50 students simultaneously.
* **Teacher Bypass:** Global adaptive apps attempt to replace or bypass teachers instead of empowering them.

---

## 💡 The Solution: AI as a Learning GPS

Like a GPS recalculating routes after a missed turn, VidyaRL uses Reinforcement Learning (RL) to adapt teaching strategies dynamically when a student struggles.

```
+-----------+  Struggles  +-----------------------+  Adapts   +------------------------------+
|  Student  | ----------> |   RL Agent (GPS)      | --------> |     New Teaching Strategy    |
|           |             | (Recalculates Route)  |           | (Hinglish/Visuals/Review)    |
+-----------+             +-----------------------+           +------------------------------+
```

### 1. Cold-Start Solution
* **Bayesian Knowledge Tracing (BKT):** During onboarding, a short gamified diagnostic establishes an initial baseline of mastery without frustrating the learner.
* **Dynamic RL Adaptation:** Once the baseline is established, the RL agent dynamically steers practice problems, hints, and prerequisites.

### 2. The 3-Step Learning Loop
1. **Learn:** Instantly repairs prerequisite gaps with concise visual reminders or intuitive explanations.
2. **Solve:** Students solve problems step-by-step so the engine pinpoints exactly where reasoning breaks down.
3. **Test:** Follow-up diagnostic checks confirm understanding before advancing to higher-order topics.

### 3. Strategic Language Bridging (Hinglish / Tanglish)
Translates conversational context into regional dialects while retaining standard STEM terms required for board exams:
> *"Velocity ante object position time ki ela change avutundo cheptundi. Remember: the technical term is **velocity**."*

---

## 👩‍🏫 Putting Teachers Back in Charge

VidyaRL synthesizes student telemetry into an actionable morning briefing for educators:

| Report Level | What the Teacher Sees | Actionable Classroom Outcome |
| :--- | :--- | :--- |
| **Class Overview** | Topic mastery summary, class trends, and specific foundational gaps missed by multiple students. | Decides whether to reteach a core concept to the entire class. |
| **Student Profile** | Recent progress, prerequisite deficiencies, repeated error patterns, and RL confidence scores. | Enables precise, one-on-one interventions. |
| **Action Plan** | Recommended peer groupings, mentor assignments, and offline printable worksheets. | Directly translates software insights into physical classroom activities. |

### 🤝 Peer Mentor Routing
Rather than requiring one teacher to supervise multiple struggling groups simultaneously, the system pairs high-mastery students as peer mentors to assist peers practicing target concepts.

---

## 🛠️ System Architecture & Technology Stack

| Layer | Technology & Strategy |
| :--- | :--- |
| **Student App (PWA)** | Lightweight Progressive Web App optimized for budget smartphones; full offline-first caching for low-connectivity environments. |
| **Learning Engine** | Python backend utilizing Bayesian Knowledge Tracing (BKT) for baseline diagnostic modeling and Reinforcement Learning for real-time pedagogical pathing. |
| **Language Support** | Integration with Indian vernacular AI models (e.g., Bhashini API) for natural voice and mixed-language hint synthesis. |
| **Teacher Cockpit** | Clean web dashboard aggregating student telemetry and generating offline-ready printable worksheets. |

---

## 🚀 Getting Started

### Prerequisites
* Web browser (Chrome / Edge / Firefox / Safari) or Node.js / Python environment depending on subsystem.

### Running Locally
1. Clone this repository:
   ```bash
   git clone https://github.com/rithwiksaini/EduChain.git
   cd EduChain
   ```
2. Open `index.html` in your browser to view the client interface.

---

## 📄 License
This project is developed for educational innovation. Distributed under the MIT License.