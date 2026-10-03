# Spoken Hindi

**A controlled language for writing Hindi the way engineers actually speak it, packaged as a Claude skill with a rule checker.**

Hindi words in Devanagari. English technical words in English. Everyday spoken vocabulary instead of शुद्ध (Sanskritised) Hindi. Short, active sentences.

[हिंदी में पढ़िए → README.hi.md](README.hi.md)

---

## Why this exists

Most people who think in Hindi don't read *formal* Hindi fast. Government-style Hindi (प्रारंभ, सुनिश्चित, संचिका) is slower to read than English. Roman Hinglish ("ye kaise chalega") is easy to type but slow to read. And when an LLM writes Hindi, it usually lands in one of those two places.

What people read fastest is the Hindi of an Indian classroom or an engineering team: Hindi sentences, English technical words, said plainly.

```text
ये function हर request पर database को call करता है, इसलिए slow है।
```

The aerospace industry fixed the same kind of problem for English with **Simplified Technical English (ASD-STE100)**. STE is a controlled language with a limited dictionary and strict writing rules. Maintenance manuals are written in it, so a mechanic who reads English as a second language reads them the same way a native speaker does.

This skill uses STE's method for spoken Hindi:

- a fixed list of approved words
- numbered writing rules
- a script that checks text against both

Its structure follows [0xpili/simplified-technical-english](https://github.com/0xpili/simplified-technical-english).

## Before and after

**Formal Hindi → Spoken Hindi**

> ❌ प्रक्रिया प्रारंभ करने से पूर्व यह सुनिश्चित करें कि समस्त संचिकाएँ संग्रहीत की जा चुकी हैं, तत्पश्चात सर्वर को पुनः प्रारंभ किया जाना चाहिए।
>
> ✅ **ध्यान दीजिए:** पहले सारी files save कीजिए।
> 1. सारी files save कीजिए।
> 2. Server restart कीजिए।

**English written in Devanagari → English in English**

> ❌ डेटाबेस में क्वेरी रन करने के बाद रिस्पॉन्स को कैश में सेव कर दीजिए।
>
> ✅ Database में query चलाइए। फिर response को cache में save कर दीजिए।

**Roman Hinglish → Devanagari**

> ❌ Ye build isliye fail ho raha hai kyunki node version purana hai.
>
> ✅ ये build इसलिए fail हो रहा है, क्योंकि Node का version पुराना है।

More examples, including a task-completion report, are in [`examples/before-after.md`](examples/before-after.md).

## The core rules

| Area | Rule |
|---|---|
| Script | Hindi in Devanagari, even when the user types Roman. English stays in English letters. Write function, not फंक्शन. Use digits 0–9, not ०–९. |
| Words | Use only words from the approved list, technical names, and technical verbs. Prefer the spoken word: शुरू, not प्रारंभ. Use one name for one thing. |
| English inside Hindi | Attach postpositions directly: function को, cache में, server पर. Make verbs with करना: deploy कीजिए. Keep each English noun's gender consistent. |
| Verbs | Active voice. No किया जाता है, no द्वारा. Use the आप imperative in procedures: चलाइए, हटाइए. |
| Sentences | At most 20 words in a procedure step and 25 in a description. One idea per sentence. Put the condition first: "अगर build fail हो, तो log खोलिए।" No semicolons, no em dashes (—). |
| Paragraphs | At most 6 sentences, one topic. |
| New terms | Before a new term, method, or symbol appears, say why it is needed. Then give its name, a plain meaning, and a small worked example with real numbers. Use at most 3–4 new terms per answer. |
| Layout | Explain in 2–3 sentence paragraphs. Put an `&nbsp;` line between paragraphs so the gap shows in editors like VS Code. Use bullets only for parallel lists, and bold 3–6 key sentences. |
| Warnings | **खतरा:** for loss you can't undo (data, money, security). **ध्यान दीजिए:** for rework. Give the command first, then the reason. |
| Explaining | Start with the problem, not the definition. Use real numbers before symbols. State what it does *not* do. Every recommendation gets a क्योंकि. |

The full set is 56 rules plus 4 general recommendations, each with a wrong and a right example: [`references/writing-rules.md`](references/writing-rules.md).

## What's in the repo

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The instructions the model loads, in 8 steps |
| [`references/writing-rules.md`](references/writing-rules.md) | 56 rules and 4 recommendations, with examples |
| [`references/word-list.md`](references/word-list.md) | 464 approved spoken-Hindi words, each with part of speech, forms, and an English gloss |
| [`references/substitutions.md`](references/substitutions.md) | ~140 formal words with spoken replacements, ~170 Devanagari-spelled English words, the categories of words that stay in English, and a gender table for English nouns |
| [`examples/before-after.md`](examples/before-after.md) | Six worked rewrites |
| [`scripts/hindi_check.py`](scripts/hindi_check.py) | Rule checker. Python 3 standard library only. |

## Install

### Claude Code

Clone the repo into your skills folder:

```bash
git clone https://github.com/shorteefy/spoken-hindi.git ~/.claude/skills/spoken-hindi
```

Then start a **new** session. Claude loads the skill whenever you ask it to write, rewrite, or check Hindi text. You can also run it directly with `/spoken-hindi`.

### Other LLMs

1. Paste `SKILL.md` into the system prompt.
2. If there is room, add `references/substitutions.md`.
3. For the best results, also add `references/word-list.md`.

## Check a file

```bash
python scripts/hindi_check.py --mode procedural steps.md
python scripts/hindi_check.py --mode descriptive notes.md
python scripts/hindi_check.py plan.html            # tags, <pre>, and <code> are skipped
cat draft.md | python scripts/hindi_check.py       # stdin works too
python scripts/hindi_check.py --strict notes.md    # also flag words not in the word list
```

On Windows, set `PYTHONUTF8=1` first so Devanagari prints correctly.

Sample output:

```text
plan.html:405: error [नियम 2.3] "लाइन" Devanagari में है। English में लिखिए: line
plan.html:852: warning [नियम 2.3] "मिनट" Devanagari में है। English में लिखिए: minute
plan.html:398: warning [नियम 1.3] "सुझाव" formal है। बोलचाल वाला लिखिए: सलाह, suggestion

17 error, 8 warning
```

The checker finds:

- English words written in Devanagari (फ़ाइल, सर्वर, बटन)
- formal or Sanskritised words (प्रारंभ, आवश्यक, अतः)
- Roman Hindi (hai, karo, nahi)
- passive voice with जाता है or द्वारा
- sentences and paragraphs that are too long (only those that contain Hindi)
- semicolons, em dashes, Devanagari digits, and Hindi sentences that end with "." instead of "।"
- आप and तुम mixed in one text

Exit code `0` means no errors, and `1` means at least one error. Warnings don't change the exit code, so you can use the checker in CI.

The word tables live in `references/substitutions.md`, not in the script. To add a word, add a row to the table, with `error` or `warning` in the last column.

## How it compares with STE

The structure and the limits match STE. The strictness does not. That was a choice: spoken Hindi gets stilted fast when every word is policed.

| | ASD-STE100 | Spoken Hindi |
|---|---|---|
| Approved words | 869, **each with one approved meaning and one part of speech** | 464, with glosses. One meaning per word is not enforced. |
| Technical verbs | Allowed only when no approved verb works | Any English verb + करना is allowed |
| Sentence limits | 20 for procedures, 25 for descriptions | Same |
| Paragraph limit | 6 sentences | Same |
| Voice | Active | Active |
| Warnings | WARNING / CAUTION | खतरा / ध्यान दीजिए |
| Checker | Checks every word against the dictionary | Checks every word only with `--strict`, and only as a warning |
| How to explain | Not covered | Problem first, then the tool, its limits, and recommendations with reasons |

## Limits

- The checker can't tell whether a word is used with the right meaning.
- It doesn't check the gender agreement of English nouns.
- Detecting passive voice is a heuristic. Constructions like "चला जाता है" are allowed, but expect some false warnings.
- Have a person read anything important.

## Credits

- Structure and method: [0xpili/simplified-technical-english](https://github.com/0xpili/simplified-technical-english) (MIT).
- Simplified Technical English is the ASD-STE100 specification, © ASD. This project does not use STE's dictionary or rule text. The Hindi word list and rules are original. See [`NOTICE.md`](NOTICE.md).

## License

MIT. See [`LICENSE`](LICENSE).
