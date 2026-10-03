---
name: spoken-hindi
description: Writes and rewrites text in Spoken Hindi — a controlled language modelled on Simplified Technical English (ASD-STE100), but for Hindi. Hindi words in Devanagari, English technical words in English letters, everyday spoken vocabulary instead of शुद्ध/Sanskritised Hindi, short active sentences. Use when the user asks for Spoken Hindi, बोलचाल की Hindi, simple Hindi, Hinglish in Devanagari, or asks to write, rewrite, review, or check Hindi text — docs, steps, instructions, warnings, explanations, or work reports.
license: MIT. The structure follows the simplified-technical-english skill by 0xpili (MIT). The word list and rules here are original and are not from ASD-STE100.
metadata:
  inspired-by: https://github.com/0xpili/simplified-technical-english
  version: 1.0 (2026-10-03)
---

# Spoken Hindi

ये skill आपसे बोलचाल वाली Hindi लिखवाती है। ठीक वैसी Hindi, जैसी दो engineer आपस में बात करते हुए बोलते हैं।

Aircraft industry की Simplified Technical English (STE) एक controlled language है। उसमें कुछ गिने हुए शब्द और कुछ साफ़ नियम होते हैं, ताकि कम English जानने वाला भी manual बिना गलती के पढ़ ले। Spoken Hindi वही काम Hindi पढ़ने वाले के लिए करती है।

इस file के नियम सबसे ज़रूरी नियम हैं। पूरे नियम `references/writing-rules.md` में हैं। मंज़ूर शब्द `references/word-list.md` में हैं। formal शब्दों की जगह क्या लिखें, वो `references/substitutions.md` में है।

## Scope

ये नियम इन पर लागू होते हैं: chat के जवाब, docs, steps, instructions, warnings, explanations, और काम पूरा होने के बाद की report।

ये नियम इन पर लागू नहीं होते:

- Code, commands, file paths, identifiers, और error messages। ये जैसे हैं, वैसे ही लिखिए।
- Code के अंदर के comments। वो English में रहेंगे।
- Quote किया हुआ text, और products या documents के official नाम।
- कविता, कहानी, या marketing वाला text।

अगर user कोई और style माँगे, तो user की बात चलेगी।

## Step 1: Text किस तरह का है, पहले ये तय कीजिए

- **Procedure** — पढ़ने वाले से कुछ करवाता है। जैसे: "`npm install` चलाइए।"
- **Description** — कुछ समझाता या बताता है। जैसे: "Cache हाल का data अपने पास रखता है।"

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
- एक sentence में एक से ज़्यादा "जो…वो" वाला हिस्सा मत रखिए।
- जोड़ने वाले आम शब्द लिखिए: और, लेकिन, फिर, इसलिए, क्योंकि, यानी।

## Step 6: Warning सही लिखिए

- **खतरा:** — data, पैसा, या ऐसा नुकसान जो वापस नहीं होगा।
- **ध्यान दीजिए:** — काम बिगड़ सकता है या दोबारा करना पड़ सकता है।
- पहले हुक्म या शर्त, फिर वजह।
- जैसे: "**खतरा:** ये command production database पर मत चलाइए। ये सारी tables मिटा देती है।"

## Step 7: समझाने का क्रम

समझाते वक्त definition से शुरू मत कीजिए। ये क्रम रखिए:

1. problem क्या थी
2. ये क्या है (problem के हिसाब से, एक-दो line में)
3. ये क्या करता है (असली numbers वाला छोटा example)
4. ये बस इतना ही करता है (इसकी हद)
5. यहाँ ये काम नहीं करता (हर case की वजह के साथ)
6. ऐसे बनाना best होगा, क्योंकि… (क्योंकि ज़रूरी है)

छोटे सवाल का छोटा जवाब दीजिए। जिस हिस्से में कहने को कुछ नहीं है, उसे छोड़ दीजिए।

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

- `references/writing-rules.md` — पूरे नियम, हर नियम के साथ सही और गलत example। पूरा document बदलते वक्त, या कोई नियम साफ़ न हो, तब पढ़िए।
- `references/word-list.md` — मंज़ूर Hindi शब्द, उनकी किस्म और ज़रूरी forms के साथ।
- `references/substitutions.md` — शुद्ध शब्दों की जगह बोलचाल वाले शब्द। साथ में English शब्दों की तीन lists: कौन से Devanagari में नहीं लिखने, कौन से English में रहेंगे, और किसका कौन सा gender है।
- `examples/before-after.md` — बदलाव से पहले और बाद के examples।
- `scripts/hindi_check.py` — check करने वाली script। सिर्फ़ Python 3 चाहिए।
