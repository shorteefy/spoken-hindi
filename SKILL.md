---
name: spoken-hindi
description: "Writes and rewrites text in Spoken Hindi, a controlled language modelled on Simplified Technical English (ASD-STE100), but for Hindi. Hindi words in Devanagari, English technical words in English letters, everyday spoken vocabulary instead of शुद्ध/Sanskritised Hindi, short active sentences. Use when the user asks for Spoken Hindi, बोलचाल की Hindi, simple Hindi, Hinglish in Devanagari, or asks to write, rewrite, review, or check Hindi text: docs, steps, instructions, warnings, explanations, or work reports. Also load it at the start of any session where replies to the user must be in Hindi, and follow it for every reply in that session."
license: MIT. The structure follows the simplified-technical-english skill by 0xpili (MIT). The word list and rules here are original and are not from ASD-STE100.
metadata:
  inspired-by: https://github.com/0xpili/simplified-technical-english
  version: 1.1 (2026-10-03)
---

# Spoken Hindi

ये skill आपसे बोलचाल वाली Hindi लिखवाती है। ठीक वैसी Hindi, जैसी दो engineer आपस में बात करते हुए बोलते हैं।

Aircraft industry की Simplified Technical English (STE) एक controlled language है। उसमें कुछ गिने हुए शब्द और कुछ साफ़ नियम होते हैं, ताकि कम English जानने वाला भी manual बिना गलती के पढ़ ले। Spoken Hindi वही काम Hindi पढ़ने वाले के लिए करती है।

इस file के नियम सबसे ज़रूरी नियम हैं। पूरे नियम `references/writing-rules.md` में हैं। मंज़ूर शब्द `references/word-list.md` में हैं। formal शब्दों की जगह क्या लिखें, वो `references/substitutions.md` में है।

## Scope

ये नियम इन पर लागू होते हैं: chat के जवाब, docs, steps, instructions, warnings, explanations, और काम पूरा होने के बाद की report।

Skill एक बार load हुई, तो पूरे session के हर जवाब पर लागू है, पहले जवाब से आख़िरी तक। कुछ जवाबों के बाद Roman Hindi ("Theek hai, chalta hoon") या शुद्ध Hindi (बकाया, निष्कर्ष) में फिसल जाना सबसे आम गलती है। Reminder का इंतज़ार मत कीजिए।

ये नियम इन पर लागू नहीं होते:

- Code, commands, file paths, identifiers, और error messages। ये जैसे हैं, वैसे ही लिखिए।
- Code के अंदर के comments। वो English में रहेंगे।
- Quote किया हुआ text, और products या documents के official नाम।
- कविता, कहानी, या marketing वाला text।

अगर user कोई और style माँगे, तो user की बात चलेगी।

## Step 1: Text किस तरह का है, पहले ये तय कीजिए

- **Procedure**: पढ़ने वाले से कुछ करवाता है। जैसे: "`npm install` चलाइए।"
- **Description**: कुछ समझाता या बताता है। जैसे: "Cache हाल का data अपने पास रखता है।"

दोनों की sentence limit अलग है। एक paragraph में दोनों को मत मिलाइए।

## Step 2: Script के नियम

- Hindi शब्द Devanagari में लिखिए। User Roman में लिखे ("ye kaise chalega"), तब भी जवाब Devanagari में दीजिए।
- English शब्द English letters में लिखिए। फंक्शन नहीं, function। डेटाबेस नहीं, database।
- अंक 0–9 वाले लिखिए। ३ नहीं, 3।
- Hindi sentence के आखिर में "।" लगाइए, "." नहीं।

## Step 3: शब्दों के नियम

- सिर्फ़ ये शब्द इस्तेमाल कीजिए: `references/word-list.md` के शब्द, technical names, और technical verbs।
- Technical name या technical verb English में ही रहेगा। Test: क्या कोई engineer Hindi में बात करते हुए ये शब्द English में बोलेगा? हाँ, तो English रखिए। जैसे: function, API, deploy, cache, server, file, login।
- English verb के साथ "करना" जोड़िए: deploy करिए, test कीजिए, file save कर लीजिए।
- शुद्ध या Sanskrit वाला शब्द मत लिखिए। प्रारंभ नहीं, शुरू। आवश्यक नहीं, ज़रूरी। अतः नहीं, इसलिए। पूरी list `references/substitutions.md` में है।
- बहुत भारी Urdu भी मत लिखिए। बाबत नहीं, बारे में। मुतालिक नहीं, से जुड़ा।
- एक चीज़ का एक ही नाम रखिए। ऊपर "record" लिखा, तो नीचे "entry" मत लिखिए।
- Vague शब्द मत लिखिए। "कुछ files" नहीं, "3 files"। "थोड़ी देर" नहीं, "करीब 2 minute"।
- पढ़ने वाला शायद कोई technical शब्द न जानता हो। तब शब्द पहली बार आते ही उसे आधी line में समझाइए। जैसे: "SEO indexing, यानी Google आपका page अपनी list में डाल ले।" ऐसे लिखिए कि कोई non-technical आदमी भी बात पकड़ ले।

## Step 4: Verb के नियम

- Active voice लिखिए। "Server request भेजता है।" ये नहीं: "Request server द्वारा भेजी जाती है।"
- "किया जाता है", "किया जा सकता है", "द्वारा" मत लिखिए। करने वाले को subject बनाइए। करने वाला नहीं है, तो "आप" लिखिए: "आप इसे बदल सकते हैं।"
- Procedure में आप वाला हुक्म लिखिए: चलाइए, खोलिए, हटाइए, check कीजिए।
- पूरे text में एक ही form रखिए। आप से शुरू किया, तो बीच में तुम मत लाइए। User तुम लिखे, तभी तुम लिखिए।
- Verb की लंबी चेन मत बनाइए। "करता रहा होगा" नहीं, "करता था" या "किया"।

## Step 5: Sentence के नियम

- Procedure का sentence: ज़्यादा से ज़्यादा 20 शब्द।
- Description का sentence: ज़्यादा से ज़्यादा 25 शब्द।
- Paragraph: ज़्यादा से ज़्यादा 6 sentence, और एक ही बात।
- एक sentence में एक बात। Procedure के एक step में एक काम।
- शर्त पहले, फिर comma, फिर काम: "अगर build fail हो, तो log खोलिए।"
- Semicolon (;) मत लगाइए। दो sentence बनाइए।
- Em dash (, ) मत लगाइए। ये दो sentences को चुपचाप एक बना देता है। उसकी जगह "।" या comma लगाइए।
- एक sentence में एक से ज़्यादा "जो…वो" वाला हिस्सा मत रखिए।
- जोड़ने वाले आम शब्द लिखिए: और, लेकिन, फिर, इसलिए, क्योंकि, यानी।

## Step 6: Warning सही लिखिए

- **खतरा:**: data, पैसा, या ऐसा नुकसान जो वापस नहीं होगा।
- **ध्यान दीजिए:**: काम बिगड़ सकता है या दोबारा करना पड़ सकता है।
- पहले हुक्म या शर्त, फिर वजह।
- जैसे: "**खतरा:** ये command production database पर मत चलाइए। ये सारी tables मिटा देती है।"

## Step 7: पहली line, और समझाने का क्रम

पहली line वो लिखिए जो पढ़ने वाले को सबसे पहले चाहिए। ये जवाब की किस्म से तय होता है:

| जवाब की किस्म | पहली line |
|---|---|
| सीधा सवाल ("port कौन सा है?") | सीधा जवाब |
| हाँ या ना वाला सवाल | हाँ या ना, फिर एक line में वजह |
| काम की report | नतीजा: क्या हो गया, क्या बाकी है |
| Steps | पहला step, या उस step की warning |
| Review या राय | फ़ैसला, फिर उसकी वजहें |
| कोई नई चीज़ समझानी हो | वो problem, जिसकी वजह से ये चीज़ बनी। एक आम sentence में। |

"Problem पहले" सिर्फ़ नई चीज़ समझाने की तरकीब है, हर जवाब की शुरुआत नहीं।

नई चीज़ समझानी हो, तो बात इस क्रम में आगे बढ़ाइए। सबसे पहले वो problem बताइए जिसकी वजह से ये चीज़ बनी, और पुराना तरीका वहाँ क्यों fail हुआ। फिर बताइए कि ये चीज़ उस problem को कैसे हल करती है। फिर असली numbers वाला छोटा example दीजिए। उसके बाद इसकी हद बताइए: ये क्या नहीं करता, और कहाँ fail होता है। आख़िर में सलाह दीजिए, और हर सलाह के साथ "क्योंकि"।

ये क्रम सोचने का है, जवाब का ढाँचा नहीं। इसलिए समझाने वाले जवाब में headings मत लगाइए। हर हिस्सा एक छोटा paragraph है, और paragraphs सीधे एक-दूसरे के बाद आते हैं। जिस हिस्से में कहने को कुछ असली नहीं है, उसे छोड़ दीजिए।

ऐसे शुरू कीजिए:

> हर request पर database तक जाने में 50ms लगते हैं, और 100 में से 90 requests वही 20 keys माँगती हैं। तो सवाल ये था कि जो data अभी-अभी पढ़ा, उसे दोबारा database से क्यों लाएँ?
>
> Cache यही करता है। ये हाल में पढ़ा हुआ data एक तेज़ जगह पर रख लेता है…

ऐसे नहीं:

> `## Problem क्या थी`
>
> `## Cache क्या है`

Report भी ऐसे ही: पहली line में नतीजा, Hindi में। ऊपर "Status Update" जैसी English heading मत लगाइए।

ध्यान दीजिए:

- पढ़ने वाले का अगला सवाल खुद पूछिए, फिर जवाब दीजिए: "क्या ये हर बार चलेगा? नहीं। कब नहीं चलेगा? जब…"
- Symbols और formula से पहले numbers दीजिए।
- पढ़ने वाले को आप कहिए। बोलचाल के जोड़ने वाले शब्द काम में लीजिए: देखिए, यानी, मतलब, तो, बस।
- छोटे paragraph और bullets रखिए। चीज़ों की तुलना करनी हो, तो table बनाइए, पर जहाँ वो अपने आप फ़िट हो।
- आख़िर में English में recap या TL;DR मत लिखिए। कोई एक line याद रखनी है, तो वो Hindi में लिखिए।

## Step 8: लिखने के बाद check कीजिए

1. Script चला सकते हैं, तो चलाइए: `python scripts/hindi_check.py --mode procedural|descriptive <file>`
2. नहीं चला सकते, तो नीचे वाली list से खुद देखिए।
3. हर गलती ठीक कीजिए।
4. फिर से check कीजिए। जब कोई गलती न बचे, तभी रुकिए।

खुद देखने की list:

- Devanagari में लिखे English शब्द ढूँढिए (फ़ाइल, सर्वर, यूज़र)। English letters में बदलिए।
- Roman Hindi ढूँढिए (hai, karo, nahi)। Devanagari में बदलिए।
- शुद्ध शब्द ढूँढिए (प्रारंभ, आवश्यक, अतः, द्वारा)। बोलचाल वाला शब्द लिखिए।
- "जाता है", "जा सकता है" वाले passive ढूँढिए। Active बनाइए।
- सबसे लंबे sentences गिनिए। Limit से लंबे हैं, तो तोड़िए।
- आप और तुम एक साथ हैं, तो एक चुनिए।
- Semicolon और देवनागरी अंक ढूँढिए। हटाइए।

Script सारी गलतियाँ नहीं पकड़ती। वो ये नहीं जानती कि शब्द का मतलब सही बैठा या नहीं। इसलिए `references/word-list.md` से भी मिलाइए।

## Reference files

- `references/writing-rules.md`: पूरे नियम, हर नियम के साथ सही और गलत example। पूरा document बदलते वक्त, या कोई नियम साफ़ न हो, तब पढ़िए।
- `references/word-list.md`: मंज़ूर Hindi शब्द, उनकी किस्म और ज़रूरी forms के साथ।
- `references/substitutions.md`: शुद्ध शब्दों की जगह बोलचाल वाले शब्द। साथ में English शब्दों की तीन lists: कौन से Devanagari में नहीं लिखने, कौन से English में रहेंगे, और किसका कौन सा gender है।
- `examples/before-after.md`: बदलाव से पहले और बाद के examples।
- `scripts/hindi_check.py`: check करने वाली script। सिर्फ़ Python 3 चाहिए।
