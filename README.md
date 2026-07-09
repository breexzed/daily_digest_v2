## Daily Digest V2 

An un-entangled, event-driven news orchestration pipeline built on decoupled architectural principles. Inspired by Rich Hickey's *"Simple Made Easy"*, this engine separates execution scopes (fetching, extraction, AI transformation, and network routing) into isolated, single-responsibility modules.

---

## The Pipeline Workflow
1. **Fetch:** Pulls raw RSS payloads directly from configuration arrays.
2. **Extract:** Maps feed metadata (source, title) and targets individual entry nodes.
3. **Scrape:** Loops lazily over data streams via Trafilatura to extract raw text.
4. **Sanitize:** Strips HTML noise, structural artifacts, and boilerplate tracking banners.
5. **Enrich:** Re-binds original feed metadata to the clean web text schemas.
6. **Dispatch:** Formats payloads and routes alerts directly to the Telegram Bot API.

---

## Execution Modes
The orchestrator supports dynamic execution flags handled directly via the command line interface:

* **Direct Mode (Raw Fallback Dispatch):**
  ```bash
  python dispatch.py
  ```
* **Intelligence Mode (Unified LLM Transformation Pipeline):**
  ```bash
  python dispatch.py --ai
  ```

---

## Environmental Requirements
The runtime requires a local virtual environment (`.venv`) injected with the following secure environment variables:

```env
GEMINI_API_KEY="AIzaSy..."
BOT_TOKEN="123456:ABC..."
MY_CHAT_ID="-100..."
```
or just use a .env file
---


I created a previous version of this project at {https://github.com/breexzed/daily_digest.git}, but after watching Simple Made Easy by Ritch Hickey the Man who built the Clojure Programming Language, i thought to myself "wow this is amazing". I figured, befoore the programming conventions of this modern age calcified in me, it's best to follow Ritch Hickey's blueprint now that i'm still a beginner, hopefully this will makew me a beter enginner, i plan to keep making things simple and making them easy. 

 Lesson Learned From this is basically to decouple everythng to the core and ruthless reduce everything that's doing sny sort of heavy lifting to just one simple scope of work. Functions, variables, objects in the future, etc. it really makes sense if you watch the video. if you already have, kudos to you.

So basically i built this program to learn, i don't think anybody will really use it as it is, not yet, maybe when i'm able to turn it into something more funky and intelligent, then we'll see. For now it basically just an RSS feed reader with ai sprinkled untop of it


I Programmed this myself, being taught by ai, not gonna lie those tools are somewhat the worst teachers cause they just want to spit out the code right out for you, takes a lot of will to close that chat open a new one with "DO NOT SPIT CODE!!!!!", "DO NOT WRITE CODE AT ALL UNDER NO CIRCUMSTANCE!!!", all over the prompt, but guess what... they still write code smh. All fof them. As a result i had to sit with an odd amount of discomfort that would be considered stupid in this age, i think it is also, but i'm toturing myself in that way for not being idk magical enough to not already know these things even if i havent learned them, but i guess i'm aware of the fact so its not that serious. Its just unreal how there's a lot of things in the world to do with all of these tools racing to get them done on your behalf, but wont even listen to you when you say they shouldnt do stuff, i know right, thats all it is about them, doing stuff, and i know somewhere someone including myself here might have discovered that maybe the potential for someting to be done well is latent and unleashable within those/things who are able to do non-doing. but only God knows what they're teaching these models, more reason to learn to do stuff yourself, not that they cant do it, but that they dont know how and when to not do things, like a computer program does not know how and when to do things without you telling what is and what is to be done with what is, in what way and what time. ai is like the opposite. sure its a good thing, but... there's that as well. i guess this is becoming a long ass pointless readme, but it once fun once again doing this, i can't say that if i dont have ai i can replicate this exact program bare, i can't if i'm being honest yet, but i know i learnt, and i know with enough DSA grind and more project, i'll get there, i'm already building the mental blocks of how all of this works, programming that is, and i think its one of te coolest things on earth. i gotta get good at this.


breexzed.
