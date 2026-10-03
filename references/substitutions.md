# बदलने वाले शब्द और technical शब्दों की किस्में

इस file में चार हिस्से हैं:

- हिस्सा 1: शुद्ध या formal शब्दों की जगह बोलचाल वाले शब्द
- हिस्सा 2: Devanagari में लिखे English शब्द, जो English letters में लिखने हैं
- हिस्सा 3: वो किस्में जिनके शब्द English में ही रहते हैं
- हिस्सा 4: English शब्दों का gender

`scripts/hindi_check.py` हिस्सा 1 और हिस्सा 2 की tables सीधे इसी file से पढ़ती है। नया शब्द जोड़ना है, तो table में एक row जोड़िए। Script में कुछ नहीं बदलना पड़ेगा।

## हिस्सा 1: शुद्ध शब्द → बोलचाल वाला शब्द

बदलते वक्त sentence का मतलब नहीं बदलना चाहिए। एक-एक शब्द बदलने से मतलब बिगड़े, तो पूरा sentence नए तरीके से लिखिए।

| शुद्ध / formal | बोलचाल वाला | script |
|---|---|---|
| प्रारंभ | शुरू | error |
| प्रारम्भ | शुरू | error |
| आरंभ | शुरू | error |
| समाप्त | ख़त्म, बंद | error |
| समाप्ति | आख़िर, ख़त्म होना | error |
| उपयोग | इस्तेमाल, use | error |
| प्रयोग | इस्तेमाल, use | error |
| उपयोगकर्ता | user | error |
| आवश्यक | ज़रूरी | error |
| आवश्यकता | ज़रूरत | error |
| अनिवार्य | ज़रूरी | error |
| सुनिश्चित | पक्का कर लीजिए, check कर लीजिए | error |
| उपलब्ध | मौजूद, मिलता है | warning |
| संबंधित | से जुड़ा | error |
| सम्बन्धित | से जुड़ा | error |
| के संबंध में | के बारे में | error |
| विषय में | के बारे में | error |
| अत्यधिक | बहुत ज़्यादा | error |
| अत्यंत | बहुत | error |
| पर्याप्त | काफ़ी | error |
| संभव | हो सकता है, possible | warning |
| असंभव | नहीं हो सकता | error |
| तत्पश्चात | उसके बाद | error |
| उपरांत | के बाद | error |
| पश्चात | के बाद | error |
| पूर्व में | पहले | error |
| से पूर्व | से पहले | error |
| अतः | इसलिए | error |
| अतएव | इसलिए | error |
| किंतु | लेकिन | error |
| किन्तु | लेकिन | error |
| परंतु | लेकिन | error |
| परन्तु | लेकिन | error |
| तथापि | फिर भी | error |
| यद्यपि | भले ही | error |
| यदि | अगर | error |
| तथा | और | error |
| एवं | और | error |
| अथवा | या | error |
| द्वारा | से (और sentence को active बनाइए) | error |
| हेतु | के लिए | error |
| प्रदान | देना | error |
| प्राप्त | मिलना, लेना | error |
| निर्माण | बनाना | error |
| निर्मित | बना हुआ | error |
| परिवर्तन | बदलाव, change | error |
| परिवर्तित | बदला हुआ | error |
| संशोधन | बदलाव, fix | error |
| त्रुटि | गलती, error | error |
| त्रुटियाँ | गलतियाँ, errors | error |
| समस्या | problem, दिक्कत | warning |
| समाधान | हल, fix | error |
| प्रक्रिया | process, तरीका | error |
| विधि | तरीका | error |
| उद्देश्य | मकसद, goal | error |
| परिणाम | नतीजा, result | warning |
| सूचना | जानकारी, message | warning |
| निर्देश | instruction, steps | error |
| स्थापित | install | error |
| संग्रहीत | save, store | error |
| पुनः | फिर से, दोबारा | error |
| प्रत्येक | हर | warning |
| सम्पूर्ण | पूरा | error |
| संपूर्ण | पूरा | error |
| केवल | सिर्फ़ | warning |
| अधिक | ज़्यादा | warning |
| अधिकतम | ज़्यादा से ज़्यादा, max | error |
| न्यूनतम | कम से कम, min | error |
| शीघ्र | जल्दी | error |
| विलंब | देर | error |
| प्रतीक्षा | इंतज़ार | error |
| अनुरोध | request | error |
| संगणक | computer | error |
| आँकड़े | data | error |
| संचिका | file | error |
| निर्देशिका | folder | error |
| प्रणाली | system | error |
| तंत्रांश | software | error |
| संजाल | network | error |
| कूटशब्द | password | error |
| अभिलेख | record | error |
| विकल्प | option | warning |
| चयन | चुनना, select | error |
| संपादित | edit | error |
| सहेजें | save कीजिए | error |
| खोज | search, ढूँढना | warning |
| प्रदर्शित | दिखाना | error |
| उत्पन्न | बनाना, generate | error |
| विश्लेषण | analysis, जाँच | error |
| परीक्षण | test | error |
| सत्यापित | verify, check | error |
| सत्यापन | verification, check | error |
| अनुमति | permission, इजाज़त | error |
| प्रमाणीकरण | login, authentication | error |
| संदेश | message | error |
| कार्य | काम | warning |
| कार्यान्वयन | implementation, बनाना | error |
| कार्यान्वित | लागू, implement | error |
| क्रियान्वित | लागू | error |
| वर्तमान | अभी का, current | warning |
| वर्तमान में | अभी | error |
| सर्वप्रथम | सबसे पहले | error |
| निम्नलिखित | नीचे वाले | error |
| उपर्युक्त | ऊपर वाले | error |
| उल्लिखित | ऊपर बताया | error |
| अनुसार | के हिसाब से | warning |
| हानि | नुकसान | warning |
| लाभ | फ़ायदा | warning |
| सावधानी | ध्यान | warning |
| सहायता | मदद | warning |
| ज्ञात | पता | error |
| अज्ञात | पता नहीं, unknown | error |
| समय-सीमा | deadline | error |
| प्रयास | कोशिश | warning |
| उत्तर | जवाब | warning |
| प्रश्न | सवाल | warning |
| कारण | वजह | warning |
| स्थिति | हालत, status | warning |
| अवस्था | हालत | error |
| सम्मिलित | शामिल | error |
| विस्तार | पूरी बात, detail | warning |
| विस्तृत | पूरा, detailed | error |
| संक्षेप | छोटे में | error |
| संक्षिप्त | छोटा | error |
| बाबत | के बारे में | error |
| मुतालिक | से जुड़ा | error |
| तफ़सील | पूरी बात, detail | error |
| इत्तला | जानकारी | error |
| बरख़ास्त | हटाना | error |
| उदाहरण | example, जैसे | warning |
| सूची | list | warning |
| टिप्पणी | comment, note | warning |
| व्यवहार | behaviour, कैसे चलता है | warning |
| वाक्य | sentence, line | warning |
| भूमिका | role, काम | warning |
| सीमा | limit, हद | warning |
| सुझाव | सलाह, suggestion | warning |
| निष्पादन | चलाना, run | error |
| समस्त | सारे, सब | error |

NOTE: "script" column बताता है कि check करने वाली script क्या दिखाएगी। कुछ शब्द ("कारण", "उत्तर", "समस्या") कई लोग बोलते भी हैं। इसलिए उन पर warning आती है, error नहीं। Context देखकर फ़ैसला कीजिए।

## हिस्सा 2: Devanagari में लिखे English शब्द

ये शब्द English letters में लिखिए। Devanagari में मत लिखिए।

"script" column में warning वाले शब्द (मिनट, नंबर, फ़ोन) Hindi में इतने आम हैं कि कई लोग इन्हें Hindi ही मानते हैं। फिर भी English letters बेहतर हैं।

| Devanagari में (गलत) | English में (सही) | script |
|---|---|---|
| फंक्शन | function | error |
| फ़ंक्शन | function | error |
| डेटाबेस | database | error |
| डाटाबेस | database | error |
| सर्वर | server | error |
| फ़ाइल | file | error |
| फाइल | file | error |
| फ़ाइलें | files | error |
| फाइलें | files | error |
| कोड | code | error |
| प्रॉब्लम | problem | error |
| प्रोब्लम | problem | error |
| सिस्टम | system | error |
| यूज़र | user | error |
| यूजर | user | error |
| डेटा | data | error |
| डाटा | data | error |
| कमांड | command | error |
| एरर | error | error |
| बग | bug | error |
| टेस्ट | test | error |
| डिप्लॉय | deploy | error |
| डिप्लोय | deploy | error |
| कैश | cache | error |
| क्वेरी | query | error |
| रिक्वेस्ट | request | error |
| रिस्पॉन्स | response | error |
| रिस्पांस | response | error |
| पेज | page | error |
| बटन | button | error |
| लिंक | link | error |
| ऐप | app | error |
| एप | app | error |
| ऐप्लिकेशन | application | error |
| एप्लीकेशन | application | error |
| वेबसाइट | website | error |
| कंप्यूटर | computer | error |
| कम्प्यूटर | computer | error |
| सॉफ्टवेयर | software | error |
| सॉफ़्टवेयर | software | error |
| नेटवर्क | network | error |
| इंटरनेट | internet | error |
| ईमेल | email | error |
| पासवर्ड | password | error |
| लॉगिन | login | error |
| लॉग इन | log in | error |
| अकाउंट | account | error |
| फ़ोल्डर | folder | error |
| फोल्डर | folder | error |
| ब्रांच | branch | error |
| कमिट | commit | error |
| प्रोसेस | process | error |
| मेमोरी | memory | error |
| स्क्रीन | screen | error |
| डैशबोर्ड | dashboard | error |
| रिकॉर्ड | record | error |
| रिकार्ड | record | error |
| सेटिंग | setting | error |
| सेटिंग्स | settings | error |
| ऑप्शन | option | error |
| मैसेज | message | error |
| नोटिफ़िकेशन | notification | error |
| नोटिफिकेशन | notification | error |
| अपडेट | update | error |
| इंस्टॉल | install | error |
| इंस्टाल | install | error |
| डाउनलोड | download | error |
| अपलोड | upload | error |
| क्लिक | click | error |
| टाइप | type | error |
| वर्ज़न | version | error |
| वर्जन | version | error |
| मॉडल | model | error |
| प्रॉम्प्ट | prompt | error |
| टोकन | token | error |
| लॉग | log | error |
| बिल्ड | build | error |
| कॉन्फ़िग | config | error |
| कॉन्फिग | config | error |
| वेरिएबल | variable | error |
| लूप | loop | error |
| क्लास | class | error |
| ऑब्जेक्ट | object | error |
| स्ट्रिंग | string | error |
| लिस्ट | list | error |
| इंडेक्स | index | error |
| थ्रेड | thread | error |
| लेटेंसी | latency | error |
| ब्राउज़र | browser | error |
| ब्राउजर | browser | error |
| टर्मिनल | terminal | error |
| स्क्रिप्ट | script | error |
| प्रोजेक्ट | project | error |
| टीम | team | warning |
| मीटिंग | meeting | warning |
| रिपोर्ट | report | warning |
| स्टेप | step | error |
| चेक | check | warning |
| फ़िक्स | fix | error |
| फिक्स | fix | error |
| इश्यू | issue | error |
| फ़ीचर | feature | error |
| फीचर | feature | error |
| वीडियो | video | warning |
| ऑडियो | audio | warning |
| फ़ॉन्ट | font | error |
| फॉन्ट | font | error |
| पेमेंट | payment | error |
| प्लान | plan | warning |
| लाइन | line | error |
| लाइनें | lines | error |
| नेविगेशन | navigation | error |
| ट्रिमर | trimmer | error |
| क्लिप | clip | error |
| क्लिप्स | clips | error |
| स्टूडियो | studio | error |
| कैप्शन | caption | error |
| सबटाइटल | subtitle | error |
| थंबनेल | thumbnail | error |
| प्लेयर | player | error |
| टैब | tab | error |
| मेनू | menu | error |
| पॉपअप | popup | error |
| डायलॉग | dialog | error |
| फ़ॉर्म | form | error |
| फॉर्म | form | error |
| शेयर | share | error |
| लोड | load | error |
| लोडिंग | loading | error |
| स्क्रॉल | scroll | error |
| डेस्कटॉप | desktop | error |
| लैपटॉप | laptop | error |
| कार्ड | card | error |
| आइकन | icon | error |
| टेक्स्ट | text | error |
| इमेज | image | error |
| प्रीव्यू | preview | error |
| एडिट | edit | error |
| सेव | save | error |
| डिलीट | delete | error |
| सर्च | search | error |
| फ़िल्टर | filter | error |
| फिल्टर | filter | error |
| सपोर्ट | support | error |
| टूल | tool | error |
| टूल्स | tools | error |
| रेंडर | render | error |
| ट्रांसक्रिप्ट | transcript | error |
| ऑफ़र | offer | error |
| ऑफर | offer | error |
| सब्सक्रिप्शन | subscription | error |
| यूआरएल | URL | error |
| सेक्शन | section | error |
| हेडर | header | error |
| फ़ुटर | footer | error |
| विंडो | window | error |
| कीबोर्ड | keyboard | error |
| ऑनलाइन | online | error |
| ऑफ़लाइन | offline | error |
| ऑफलाइन | offline | error |
| स्लाइडर | slider | error |
| टूलबार | toolbar | error |
| मिनट | minute | warning |
| सेकंड | second | warning |
| नंबर | number | warning |
| फ़ोन | phone | warning |
| फोन | phone | warning |
| टाइम | time | warning |
| मोबाइल | mobile | warning |

## हिस्सा 3: English में रहने वाले शब्दों की किस्में

इन किस्मों के शब्द English में ही रहते हैं। ये technical names और technical verbs हैं।

### Technical names (noun)

1. Software और IT के शब्द। जैसे: file, folder, server, database, API, cache, query, branch, commit, log।
2. Product, company, और tool के नाम। जैसे: GitHub, VS Code, Python, AWS, Claude।
3. Code के नाम। जैसे: function, class, variable, `user_id`, `index.html`।
4. Machine, device, और उसके हिस्सों के नाम। जैसे: laptop, phone, screen, keyboard, battery।
5. Science, maths, और engineering के शब्द। जैसे: voltage, latency, average, percent, formula।
6. नाप की इकाई। जैसे: MB, GB, ms, second, minute, km, kg।
7. Screen, button, या label पर लिखा text। जैसे: "Save" button, `Done` message।
8. Documents और उनके हिस्सों के नाम। जैसे: README, section, chapter, page, PR।
9. Roles और teams के नाम। जैसे: admin, user, owner, reviewer, team।
10. पैसे और business के शब्द। जैसे: payment, invoice, plan, refund, GST।
11. ऐसे आम English शब्द जो Hindi बोलते वक्त English में ही बोले जाते हैं। जैसे: problem, check, time, step, issue, simple, normal, ready, example।

### Technical verbs

English verb के साथ "करना" जोड़िए। "होना" से हालत बताइए।

1. Computer का काम: click, save, copy, paste, delete, install, download, restart, login, scroll।
2. Software बनाने का काम: deploy, build, commit, merge, push, test, debug, refactor, review।
3. Data का काम: sort, filter, query, cache, sync, backup, import, export।
4. आम काम जो English में बोला जाता है: check, fix, update, share, confirm, cancel, approve।

Technical verbs के नियम:

- Hindi verb आम हो और मतलब पूरा दे, तो Hindi लिखिए। "हटा दीजिए" ठीक है, "delete कीजिए" भी ठीक है। Text में एक ही रखिए।
- English verb को Hindi ending मत दीजिए। "deployिए" नहीं, "deploy कीजिए"।

## हिस्सा 4: English शब्दों का gender

लोग जैसे बोलते हैं, वैसा gender रखिए। एक text में एक शब्द का एक ही gender रखिए। ये नियम book से ज़्यादा ज़रूरी है।

| Masculine (पुल्लिंग) — "बड़ा error आया" | Feminine (स्त्रीलिंग) — "बड़ी file आई" |
|---|---|
| function, server, database, cache, index | API, request, file, query, memory |
| thread, bug, code, process, config | line, string, list, call, value |
| class, object, loop, commit, branch | key, table, row, image, setting |
| error, message, page, button, link | site, website, app, script, story |
| system, user, account, folder, project | team, meeting, payment, problem* |
| test, build, log, version, model | window, screen, field, entry |
| deploy, update, response, record, token | date, theory, category, policy |
| plan, issue, step, result, dashboard | language, sheet, permission, deadline |

\* "problem" दोनों तरह बोलते हैं: "problem आ गया" और "problem आ गई"। एक चुनिए और वही रखिए।
