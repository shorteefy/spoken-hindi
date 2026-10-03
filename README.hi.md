# Spoken Hindi skill

ये skill LLM से बोलचाल वाली Hindi लिखवाती है। Hindi शब्द Devanagari में, English technical शब्द English में, और छोटे active sentences।

इसका ढाँचा [simplified-technical-english](https://github.com/0xpili/simplified-technical-english) से लिया है। वो skill aircraft manuals वाली Simplified Technical English (ASD-STE100) सिखाती है। ये skill वही तरीका Hindi पर लगाती है: गिने हुए शब्द, साफ़ नियम, और check करने वाली script।

ये README भी Spoken Hindi में है। [English README](README.md)

## Example

पहले:

> प्रक्रिया प्रारंभ करने से पूर्व यह सुनिश्चित करें कि समस्त संचिकाएँ संग्रहीत की जा चुकी हैं।

बाद में:

> शुरू करने से पहले सारी files save कीजिए।

## Files

| File | काम |
|---|---|
| `SKILL.md` | LLM के लिए मुख्य नियम |
| `references/writing-rules.md` | 56 नियम और 4 आम सलाह, examples के साथ |
| `references/word-list.md` | 464 मंज़ूर Hindi शब्द |
| `references/substitutions.md` | शुद्ध → बोलचाल, Devanagari में लिखी English, English शब्दों का gender |
| `examples/before-after.md` | 6 examples: बदलाव से पहले और बाद |
| `scripts/hindi_check.py` | Check करने वाली script |
| `LICENSE`, `NOTICE.md` | MIT license, और credit किसे जाता है |

## Skill कहाँ है

Skill सिर्फ़ `~/.claude/skills/spoken-hindi/` में है। इसकी कोई दूसरी copy नहीं है। इसलिए ये हर project में चलती है, जैसे Shorteefy में। आप `/spoken-hindi` लिखकर सीधे भी चला सकते हैं।

बदलाव इसी folder में कीजिए।

## Text check कैसे करें

Markdown, text, या HTML file पर चलाइए। HTML में tags, `<pre>`, और `<code>` अपने आप छूट जाते हैं:

    python scripts/hindi_check.py --mode procedural steps.md
    python scripts/hindi_check.py --mode descriptive notes.md
    python scripts/hindi_check.py --strict notes.md
    python scripts/hindi_check.py plan.html

Windows पर Hindi ठीक दिखे, इसके लिए पहले `PYTHONUTF8=1` set कीजिए।

Script ये गलतियाँ पकड़ती है:

- Devanagari में लिखे English शब्द (फ़ाइल, सर्वर)
- शुद्ध या formal शब्द (प्रारंभ, आवश्यक, अतः)
- Roman Hindi (hai, karo, nahi)
- "जाता है" और "द्वारा" वाले passive
- लंबे sentences और लंबे paragraphs (सिर्फ़ वो जिनमें Hindi है)
- Semicolon, em dash (—), देवनागरी अंक, और "." से ख़त्म होने वाला Hindi sentence
- एक ही text में आप और तुम

`--strict` से वो Hindi शब्द भी दिखते हैं जो word list में नहीं हैं। ये सिर्फ़ warning है।

नए शब्द `references/substitutions.md` की tables में जोड़िए। Script उन्हें वहीं से पढ़ती है।

## हद

Script सारी गलतियाँ नहीं पकड़ती। वो ये नहीं जानती कि शब्द का मतलब सही बैठा या नहीं। Gender भी check नहीं करती। ज़रूरी text को कोई इंसान भी पढ़ ले।
