# Examples: बदलाव से पहले और बाद

ये file दिखाती है कि text Spoken Hindi में बदलने के बाद कैसा दिखता है। Examples हमारे अपने हैं।

## Example 1: शुद्ध Hindi वाली procedure

पहले:

> प्रक्रिया प्रारंभ करने से पूर्व यह सुनिश्चित करें कि समस्त संचिकाएँ संग्रहीत की जा चुकी हैं, तत्पश्चात सर्वर को पुनः प्रारंभ किया जाना चाहिए; ऐसा न करने पर आँकड़ों की हानि संभव है।

बाद में:

> **ध्यान दीजिए:** पहले सारी files save कीजिए। Save नहीं कीं, तो data जा सकता है।
>
> 1. सारी files save कीजिए।
> 2. Server restart कीजिए।

बदलाव: प्रारंभ → शुरू, संचिका → file, आँकड़े → data, तत्पश्चात → फिर। Passive हटाया। Semicolon हटाया। Warning को step से पहले रखा।

## Example 2: English वाली description

पहले:

> The cache layer is responsible for storing frequently accessed data in memory, thereby reducing the number of round trips to the database and significantly improving response latency for end users.

बाद में:

> हर request पर database तक जाना धीमा है। इसलिए cache हाल का data memory में रखता है। अगली बार वही data cache से मिल जाता है। इससे database तक कम जाना पड़ता है, और user को जवाब जल्दी मिलता है।

बदलाव: पहले problem, फिर हल। एक sentence में एक बात। "significantly" जैसा vague शब्द हटाया।

## Example 3: Devanagari में लिखी English

पहले:

> डेटाबेस में क्वेरी रन करने के बाद रिस्पॉन्स को कैश में सेव कर दीजिए।

बाद में:

> Database में query चलाइए। फिर response को cache में save कर दीजिए।

बदलाव: हर English शब्द English letters में। दो काम, तो दो sentence।

## Example 4: Roman Hinglish

User ने लिखा:

> bhai ye build fail kyun ho raha hai

पहले:

> Ye build isliye fail ho raha hai kyunki node version purana hai.

बाद में:

> ये build इसलिए fail हो रहा है, क्योंकि Node का version पुराना है। `node -v` चलाकर देखिए। 18 से कम आए, तो Node update कीजिए।

बदलाव: Roman Hindi → Devanagari। वजह के बाद अगला काम भी बताया।

## Example 5: Warning

पहले:

> इस कमांड का निष्पादन करते समय अत्यधिक सावधानी बरतनी चाहिए क्योंकि इससे डेटा स्थायी रूप से नष्ट हो सकता है।

बाद में:

> **खतरा:** ये command production database पर मत चलाइए। ये सारी tables मिटा देती है, और data वापस नहीं आता।

बदलाव: पहले हुक्म, फिर वजह। "अत्यधिक सावधानी" की जगह साफ़ हुक्म: कहाँ मत चलाइए।

## Example 6: काम पूरा होने की report

पहले:

> I have successfully implemented the requested changes. The login timeout has been increased from 30 to 60 seconds in auth.ts, and the corresponding tests have been updated. All 42 tests are passing. Note that the mobile app has not been modified.

बाद में:

> Login का timeout 30 से 60 second कर दिया। ये बदलाव `auth.ts` में है। उससे जुड़े tests भी update किए। सारे 42 tests pass हैं।
>
> बस इतना ही बदला। Mobile app को हाथ नहीं लगाया। वहाँ timeout अभी भी 30 second है।

बदलाव: "has been" वाला passive हटाया। Scope अलग से बताया: क्या बदला, क्या नहीं।
