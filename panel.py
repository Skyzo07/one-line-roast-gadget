"""Independent judge panel for the roast top 3 (CrowLLM, OpenAI-compatible).

Reads CROWLLM_API_KEY from the environment only. Never prints the key.
Models judge independently: each scores A/B/C 0-10 on the brief's criteria
IN ORDER (on-subject, funny, fresh, neat, specific) + a laugh yes/no + why.
The gateway 403s Python urllib's default User-Agent, so a normal UA is set.
"""
import json
import os
import urllib.request

BASE = "https://crowllm.com/v1"
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0 Safari/537.36"}

CANDIDATES = {
    "A": "My washing machine plays a fanfare when it finishes, as if spinning my socks deserved applause.",
    "B": "My smartwatch applauds me for standing up, as if reaching for snacks were a summit.",
    "C": "My microwave beeps at me until I open the door, like it's the one who did the cooking.",
}

PROMPT = """You are a comedy editor judging one-line roasts for a competition. The brief: one original line, at most 200 characters, roasting a gadget or app the writer uses every day. Weigh the criteria IN THIS ORDER:
1. Roasts a gadget or app people use every day in a single line (a line that never names or clearly targets a daily gadget/app loses to any line that does; note: a washing machine is NOT an every-day gadget for most people, a smartwatch and a microwave are).
2. Is actually funny: the joke lands on a first read, with a sting of recognition rather than a mild grumble.
3. Feels fresh: an angle, comparison or detail not seen before, not the obvious complaint everyone makes about that product.
4. Is neatly worded: tight, well timed, no wasted words, comfortably inside the character limit.
5. Sounds like one person's specific gripe, with a concrete detail about how the thing actually behaves, not a generic complaint that could be about anything.

The three lines:
A: {A}
B: {B}
C: {C}

For EACH of A, B, C, give integer scores 0-10 for on_subject, funny, fresh, neat, specific, in that order, plus one line: would this make a cold reader actually laugh — yes/no, and why in under 20 words.
Reply ONLY as JSON, no other text:
{{"A": {{"on_subject": 0, "funny": 0, "fresh": 0, "neat": 0, "specific": 0, "laugh": "yes/no - reason"}}, "B": {{...}}, "C": {{...}}}}"""

MODELS = ["qwen4-max:free", "llama-3.3-70b-instruct:free", "minimax-m3.1-flash:free"]
SUBSTITUTES = ["deepseek-v4-flash-thinking:free", "gemma-4-31b-it:free"]


def call(model, key):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "user", "content": PROMPT.format(**CANDIDATES)}],
    }).encode()
    req = urllib.request.Request(
        BASE + "/chat/completions", data=body,
        headers={**UA, "Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read())["choices"][0]["message"]["content"]


def main():
    key = os.environ["CROWLLM_API_KEY"]
    results = {}
    for model in MODELS:
        try:
            results[model] = call(model, key)
            print(f"OK {model}")
        except Exception as e:
            print(f"FAIL {model}: {type(e).__name__} {e}")
            for sub in SUBSTITUTES:
                if sub in results:
                    continue
                try:
                    results[sub] = call(sub, key)
                    print(f"OK substitute {sub}")
                    break
                except Exception as e2:
                    print(f"FAIL substitute {sub}: {type(e2).__name__} {e2}")
    with open("panel-results.json", "w") as f:
        json.dump(results, f, indent=2)
    print("wrote panel-results.json with", len(results), "judges")


if __name__ == "__main__":
    main()
