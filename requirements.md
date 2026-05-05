
# urls
1) https://kb.cifrium.ru/courses/[courseId] - main page of a course, it has a list of tasks.

2) https://kb.cifrium.ru/teacher/courses/[courseId]/lessons/[taskId] - page of a task, it has the video and task buttons

3.1) https://kb.cifrium.ru/classworks/[classworkId]/tasks/[questionId]?page=1 - page of a question in a task (?page=1 does not change, the next question in a task has the id of 1197265)
3.2) https://kb.cifrium.ru/lessons/[taskId]/tasks/[questionId] - theres also this type, it has to be done as well

4) https://kb.cifrium.ru/groups/[videoId] - link to the video



# headers

## there are multiple task types, heres a list of answer attempts for types of:

### ANSWER ATTEMPT html and payload For radio button type of url task format 3.1
```
<form id="taskForm" action="/classworks/1859/tasks/1197261" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-hHedjW"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div><div><div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1248192]" type="radio" tabindex="-1" value="10329223"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Выводит результат на экран</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1248192]" type="radio" tabindex="-1" value="10329224"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Останавливает выполнение функции и возвращает значение</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1248192]" type="radio" tabindex="-1" value="10329225"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Сохраняет значение в файл</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1248192]" type="radio" tabindex="-1" value="10329226"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Объявляет новую переменную</span></div></div></div></div></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div><div class="actions_userAnswerBlock__2vq+R actions_noSolved__ArVBT"><div class="actions_left__bKCPf"><div class="actions_attempt__qlfSc">Попытка 1 из 1<div class="fox-ui__sc-1r4rhyb-0 bufWQz actions_hintIcon__vbqX0"><span data-id="rf-82803" style="cursor: help; z-index: 100; display: inline-flex; flex-direction: column;"><div class="fox-ui__sc-yfeniy-0 iaFAsc fox-Icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.986 6.995v-2.019h-1.972v2.02h1.972zm0 8.029v-6.01h-1.972v6.01h1.972zm-.986-15.024c1.827 0 3.518.457 5.072 1.37a9.478 9.478 0 0 1 3.558 3.558 9.835 9.835 0 0 1 1.37 5.072 9.835 9.835 0 0 1-1.37 5.072 9.478 9.478 0 0 1-3.558 3.558 9.835 9.835 0 0 1-5.072 1.37 9.835 9.835 0 0 1-5.072-1.37 9.657 9.657 0 0 1-3.558-3.582 9.79 9.79 0 0 1-1.37-5.048 9.79 9.79 0 0 1 1.37-5.048 9.842 9.842 0 0 1 3.582-3.582 9.79 9.79 0 0 1 5.048-1.37z"></path></svg></div></span></div></div></div><div class="actions_right__fgCRg"><div class="actions_answer__wXrNe actions_noSolved__ArVBT"><span>За решение задачи </span><span class="fox-ui__sc-s2fogy-0 eYacsZ fox-Text">1&nbsp;балл</span></div><button class="fox-ui__sc-16o31r2-1 euOfwS fox-Button actions_button__3GaLH" type="submit"><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Ответить</span></button></div><div class="Visible_root__si8Vu Visible_block__C-o3Q Visible_extraSmall__voerG Visible_small__sSy7q"><div class="fox-ui__sc-1r4rhyb-0 BTwgM"></div></div></div></form>
```
```
curl ^"https://kb.cifrium.ru/api/homeworks/1859/tasks/1197262/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundarygTkEyAazpLbXBlV2^" ^
  -b ^"user_agent_uid=1c7faaf3-dec3-43fc-836f-edc0ee5e32a3; _ym_uid=1773484899422683680; _ym_d=1773484899; client_timezone=Europe/Moscow; mindboxDeviceUUID=68096618-627f-4bd4-afc9-f4c401be2078; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^2268096618-627f-4bd4-afc9-f4c401be2078^%^22^%^7D; _ym_isad=2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOVGswTXpoZExDSWtNbUVrTVRBa1NsRkVOalpzTjJJMlIzQmpTV3RUUm1aTGFEUlNkU0lzSWpFM056TTBPRFV3TnprdU5UQTFOekkxSWwwPSIsImV4cCI6IjIwMjYtMDYtMTRUMTA6NDQ6MzlaIiwicHVyIjpudWxsfX0^%^3D--2261d536a72d805bc356183fd0c1afd193741361; _wk_kbc_session=1327d2684354d130fc7dc8814a5453ff; _csrf_token=Sc3eYAyjRts^%^2FJvRgLGQeh60KaQAUT2GBJCCWTW2m^%^2FCzG^%^2FYUQUE9Yb0kNj0^%^2FDjp7CJeWc1s^%^2B6dtGws3KK5zjxkA^%^3D^%^3D; _mkra_stck=pg^%^3A1773486668.3621385^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/classworks/1859/tasks/1197262?page=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: Sc3eYAyjRts/JvRgLGQeh60KaQAUT2GBJCCWTW2m/CzG/YUQUE9Yb0kNj0/Djp7CJeWc1s+6dtGws3KK5zjxkA==^" ^
  -H ^"X-Device-Id: bad5b60587b503332c38847fdd306ff5^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/classworks/1859/tasks/1197262^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundarygTkEyAazpLbXBlV2^

Content-Disposition: form-data; name=^\^"questions^[1248193^]^\^"^

^

10329229^

------WebKitFormBoundarygTkEyAazpLbXBlV2--^

^"
```


### ANSWER ATTEMPT payload FOR A TEXT INPUT TYPE OF URL FORMAT 3.1
```
curl ^"https://kb.cifrium.ru/api/homeworks/1859/tasks/1197263/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryUBkjTUX0oDwi4g7R^" ^
  -b ^"user_agent_uid=1c7faaf3-dec3-43fc-836f-edc0ee5e32a3; _ym_uid=1773484899422683680; _ym_d=1773484899; client_timezone=Europe/Moscow; mindboxDeviceUUID=68096618-627f-4bd4-afc9-f4c401be2078; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^2268096618-627f-4bd4-afc9-f4c401be2078^%^22^%^7D; _ym_isad=2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOVGswTXpoZExDSWtNbUVrTVRBa1NsRkVOalpzTjJJMlIzQmpTV3RUUm1aTGFEUlNkU0lzSWpFM056TTBPRFV3TnprdU5UQTFOekkxSWwwPSIsImV4cCI6IjIwMjYtMDYtMTRUMTA6NDQ6MzlaIiwicHVyIjpudWxsfX0^%^3D--2261d536a72d805bc356183fd0c1afd193741361; _wk_kbc_session=1327d2684354d130fc7dc8814a5453ff; _csrf_token=Sc3eYAyjRts^%^2FJvRgLGQeh60KaQAUT2GBJCCWTW2m^%^2FCzG^%^2FYUQUE9Yb0kNj0^%^2FDjp7CJeWc1s^%^2B6dtGws3KK5zjxkA^%^3D^%^3D^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/classworks/1859/tasks/1197263?page=1^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: Sc3eYAyjRts/JvRgLGQeh60KaQAUT2GBJCCWTW2m/CzG/YUQUE9Yb0kNj0/Djp7CJeWc1s+6dtGws3KK5zjxkA==^" ^
  -H ^"X-Device-Id: bad5b60587b503332c38847fdd306ff5^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/classworks/1859/tasks/1197263^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundaryUBkjTUX0oDwi4g7R^

Content-Disposition: form-data; name=^\^"questions^[1248194^]^[^]^\^"^

^

35^

------WebKitFormBoundaryUBkjTUX0oDwi4g7R--^

^"
```

### ANSWER ATTEMPT html and payload FOR A RADIO BUTTON TYPE of url format 3.2
```
<form id="taskForm" action="/teacher/lessons/11858/tasks/1167863" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-hHedjW"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div><div><div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207750]" type="radio" tabindex="-1" value="10162030"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">ошибся в написании названия функции</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207750]" type="radio" tabindex="-1" value="10162031"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">при вызове указал неправильное количество аргументов</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207750]" type="radio" tabindex="-1" value="10162032"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">при объявлении функции указал неправильное количество аргументов</span></div></div><div class="styled__Root-jGVGzp gHoiIu"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207750]" type="radio" tabindex="-1" value="10162033"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">ошибся в печати результата</span></div></div></div></div></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div><div class="actions_userAnswerBlock__2vq+R actions_noSolved__ArVBT"><div class="actions_left__bKCPf"><div class="actions_attempt__qlfSc">Попытка 1 из 1<div class="fox-ui__sc-1r4rhyb-0 bufWQz actions_hintIcon__vbqX0"><span data-id="rf-78927" style="cursor: help; z-index: 100; display: inline-flex; flex-direction: column;"><div class="fox-ui__sc-yfeniy-0 iaFAsc fox-Icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.986 6.995v-2.019h-1.972v2.02h1.972zm0 8.029v-6.01h-1.972v6.01h1.972zm-.986-15.024c1.827 0 3.518.457 5.072 1.37a9.478 9.478 0 0 1 3.558 3.558 9.835 9.835 0 0 1 1.37 5.072 9.835 9.835 0 0 1-1.37 5.072 9.478 9.478 0 0 1-3.558 3.558 9.835 9.835 0 0 1-5.072 1.37 9.835 9.835 0 0 1-5.072-1.37 9.657 9.657 0 0 1-3.558-3.582 9.79 9.79 0 0 1-1.37-5.048 9.79 9.79 0 0 1 1.37-5.048 9.842 9.842 0 0 1 3.582-3.582 9.79 9.79 0 0 1 5.048-1.37z"></path></svg></div></span></div></div></div><div class="actions_right__fgCRg"><div class="actions_answer__wXrNe actions_noSolved__ArVBT"><span>За решение задачи </span><span class="fox-ui__sc-s2fogy-0 eYacsZ fox-Text">1&nbsp;балл</span></div><button class="fox-ui__sc-16o31r2-1 euOfwS fox-Button actions_button__3GaLH" type="submit"><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Ответить</span></button></div><div class="Visible_root__si8Vu Visible_block__C-o3Q Visible_extraSmall__voerG Visible_small__sSy7q"><div class="fox-ui__sc-1r4rhyb-0 BTwgM"></div></div></div></form>
```
```
curl ^"https://kb.cifrium.ru/api/lessons/11859/tasks/1167868/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundary9o9QSatr6zv7KlOG^" ^
  -b ^"user_agent_uid=1c7faaf3-dec3-43fc-836f-edc0ee5e32a3; _ym_uid=1773484899422683680; _ym_d=1773484899; client_timezone=Europe/Moscow; mindboxDeviceUUID=68096618-627f-4bd4-afc9-f4c401be2078; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^2268096618-627f-4bd4-afc9-f4c401be2078^%^22^%^7D; _ym_isad=2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOVGswTXpoZExDSWtNbUVrTVRBa1NsRkVOalpzTjJJMlIzQmpTV3RUUm1aTGFEUlNkU0lzSWpFM056TTBPRFV3TnprdU5UQTFOekkxSWwwPSIsImV4cCI6IjIwMjYtMDYtMTRUMTA6NDQ6MzlaIiwicHVyIjpudWxsfX0^%^3D--2261d536a72d805bc356183fd0c1afd193741361; _wk_kbc_session=1327d2684354d130fc7dc8814a5453ff; _csrf_token=tYn88VMdx^%^2BdHEdi5ioGhdTbyVNSYBmFFhhTsL24HcbI6uaeBD^%^2FHZUzE6o5ZlayEwvh2hAkPzdhUShwjo5Jl8Dg^%^3D^%^3D; _mkra_stck=pg^%^3A1773486486.188226^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/teacher/lessons/11859/tasks/1167868^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: tYn88VMdx+dHEdi5ioGhdTbyVNSYBmFFhhTsL24HcbI6uaeBD/HZUzE6o5ZlayEwvh2hAkPzdhUShwjo5Jl8Dg==^" ^
  -H ^"X-Device-Id: bad5b60587b503332c38847fdd306ff5^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/teacher/lessons/11859/tasks/1167868^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundary9o9QSatr6zv7KlOG^

Content-Disposition: form-data; name=^\^"questions^[1207755^]^\^"^

^

10162044^

------WebKitFormBoundary9o9QSatr6zv7KlOG--^

^"
```

### ANSWER ATTEMPT payload and html for a MULTIPLE CHOICE TYPE OF URL FORMAT 3.2
```
curl ^"https://kb.cifrium.ru/api/lessons/11861/tasks/1167881/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: en-US,en;q=0.9^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryiLi4qAtMmcVqBTDw^" ^
  -b ^"user_agent_uid=9f2d5b14-2b92-4cbc-a112-d6734e3970d8; _csrf_token=4RUCYgVd8GDN585i3EkO^%^2BTOzYQ1SSgQ4DGWYwukNrvLRtYvPkHCX^%^2FXc1r8cIhN^%^2BrrqFAl63tu^%^2Bn1X872qtoSXA^%^3D^%^3D; _ym_uid=1773509181757335860; _ym_d=1773509181; mindboxDeviceUUID=6ed4752e-fac0-49ae-9141-332f79572ca3; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^226ed4752e-fac0-49ae-9141-332f79572ca3^%^22^%^7D; _ym_isad=2; client_timezone=Europe/Moscow; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOakF4TVRsZExDSWtNbUVrTVRBa05WbEtVRUpqUWt0MlQzQTJXamc0VlZWamNtdGpMaUlzSWpFM056TTFNRGt4T1RVdU9UVTFPRGM1TWlKZCIsImV4cCI6IjIwMjYtMDYtMTRUMTc6MjY6MzVaIiwicHVyIjpudWxsfX0^%^3D--ca38e305c186cd957b4150a06648d58f93c2bf8e; _wk_kbc_session=29bf37ff28a9f7a55b2470818f67c11d; _mkra_stck=pg^%^3A1773509236.7480643^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/lessons/11861/tasks/1167881^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: 4RUCYgVd8GDN585i3EkO+TOzYQ1SSgQ4DGWYwukNrvLRtYvPkHCX/Xc1r8cIhN+rrqFAl63tu+n1X872qtoSXA==^" ^
  -H ^"X-Device-Id: 32c8ed65e482cef9f4f92ca88e4a188c^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/lessons/11861/tasks/1167881^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundaryiLi4qAtMmcVqBTDw^

Content-Disposition: form-data; name=^\^"questions^[1207768^]^[^]^\^"^

^

10162093^

------WebKitFormBoundaryiLi4qAtMmcVqBTDw^

Content-Disposition: form-data; name=^\^"questions^[1207768^]^[^]^\^"^

^

10162094^

------WebKitFormBoundaryiLi4qAtMmcVqBTDw--^

^"
```
```
<form id="taskForm" action="/lessons/11861/tasks/1167881" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-klnFHs"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div><div><div><div class="styled__Root-eQsOOc lmJYyU"><div class="styled__Root-egLEii iMJyKO"></div><input class="input" name="questions[1207768][]" type="checkbox" tabindex="-1" value="10162091"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">print</span></div></div><div class="styled__Root-eQsOOc lmJYyU"><div class="styled__Root-egLEii iMJyKO"></div><input class="input" name="questions[1207768][]" type="checkbox" tabindex="-1" value="10162092"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">str</span></div></div><div class="styled__Root-eQsOOc eAaNeD"><div class="styled__Root-egLEii bgANFm"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 26 26" class="checkmark"><path d="M20.086 6.086L9.5 16.672l-3.586-3.586-2.828 2.828L9.5 22.328 22.914 8.914z"></path></svg></div><input class="input" name="questions[1207768][]" type="checkbox" tabindex="-1" value="10162093"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">def</span></div></div><div class="styled__Root-eQsOOc eAaNeD"><div class="styled__Root-egLEii bgANFm"><svg xmlns="http://www.w3.org/2000/svg" width="12" height="12" viewBox="0 0 26 26" class="checkmark"><path d="M20.086 6.086L9.5 16.672l-3.586-3.586-2.828 2.828L9.5 22.328 22.914 8.914z"></path></svg></div><input class="input" name="questions[1207768][]" type="checkbox" tabindex="-1" value="10162094"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">for</span></div></div></div></div></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div></form>
```



### ANSWER ATTEMPT FOR TEXT INPUT TYPE of url format 3.2
```
curl ^"https://kb.cifrium.ru/api/lessons/11859/tasks/1167869/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryfJBf20woJpsi3hPd^" ^
  -b ^"user_agent_uid=1c7faaf3-dec3-43fc-836f-edc0ee5e32a3; _ym_uid=1773484899422683680; _ym_d=1773484899; client_timezone=Europe/Moscow; mindboxDeviceUUID=68096618-627f-4bd4-afc9-f4c401be2078; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^2268096618-627f-4bd4-afc9-f4c401be2078^%^22^%^7D; _ym_isad=2; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOVGswTXpoZExDSWtNbUVrTVRBa1NsRkVOalpzTjJJMlIzQmpTV3RUUm1aTGFEUlNkU0lzSWpFM056TTBPRFV3TnprdU5UQTFOekkxSWwwPSIsImV4cCI6IjIwMjYtMDYtMTRUMTA6NDQ6MzlaIiwicHVyIjpudWxsfX0^%^3D--2261d536a72d805bc356183fd0c1afd193741361; _wk_kbc_session=1327d2684354d130fc7dc8814a5453ff; _mkra_stck=pg^%^3A1773486610.9164767; _csrf_token=Sc3eYAyjRts^%^2FJvRgLGQeh60KaQAUT2GBJCCWTW2m^%^2FCzG^%^2FYUQUE9Yb0kNj0^%^2FDjp7CJeWc1s^%^2B6dtGws3KK5zjxkA^%^3D^%^3D^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/teacher/lessons/11859/tasks/1167869^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: Sc3eYAyjRts/JvRgLGQeh60KaQAUT2GBJCCWTW2m/CzG/YUQUE9Yb0kNj0/Djp7CJeWc1s+6dtGws3KK5zjxkA==^" ^
  -H ^"X-Device-Id: bad5b60587b503332c38847fdd306ff5^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/teacher/lessons/11859/tasks/1167869^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundaryfJBf20woJpsi3hPd^

Content-Disposition: form-data; name=^\^"questions^[1207756^]^[^]^\^"^

^

12^

------WebKitFormBoundaryfJBf20woJpsi3hPd--^

^"
```

### ANSWER ATTEMPT payload and html for 3.2 drag and drop type
```
curl ^"https://kb.cifrium.ru/api/lessons/11863/tasks/1167887/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryIb92EAbYgnUFOeO9^" ^
  -b ^"user_agent_uid=3f5bf6cf-1a16-4681-ae05-01cc7b521b39; _csrf_token=AsNcgbkn21bVEMGRzke4MJtpH3icNScH^%^2F4SOml9bYDojh^%^2FzJm4mFgwHtSj^%^2F^%^2BKavvQ8RWuMu64HM65hnUB5QJWA^%^3D^%^3D; _ym_uid=1773733184755864765; _ym_d=1773733184; _ym_isad=2; mindboxDeviceUUID=13238470-18ed-4917-b6d0-10d3a4e2aab1; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^2213238470-18ed-4917-b6d0-10d3a4e2aab1^%^22^%^7D; client_timezone=Europe/Moscow; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOakV3TnpaZExDSWtNbUVrTVRBa2Rtc3dZbkF1VHpOTWRuVkxhRkJNU1hwalRHa3VMaUlzSWpFM056TTNNek15TWpndU56TTROelV5SWwwPSIsImV4cCI6IjIwMjYtMDYtMTdUMDc6NDA6MjhaIiwicHVyIjpudWxsfX0^%^3D--2970695cd322087e09617e83210f337bc3d2448a; _wk_kbc_session=ab31968bb6270db413ef7202d10c1037^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/teacher/lessons/11863/tasks^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: AsNcgbkn21bVEMGRzke4MJtpH3icNScH/4SOml9bYDojh/zJm4mFgwHtSj/+KavvQ8RWuMu64HM65hnUB5QJWA==^" ^
  -H ^"X-Device-Id: fc843a63c432edc43ad8b96dd2c8eae4^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/teacher/lessons/11863/tasks^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundaryIb92EAbYgnUFOeO9^

Content-Disposition: form-data; name=^\^"questions^[1207774^]^[10162110^]^\^"^

^

10162111^

------WebKitFormBoundaryIb92EAbYgnUFOeO9^

Content-Disposition: form-data; name=^\^"questions^[1207774^]^[10162112^]^\^"^

^

10162113^

------WebKitFormBoundaryIb92EAbYgnUFOeO9^

Content-Disposition: form-data; name=^\^"questions^[1207774^]^[10162114^]^\^"^

^

10162115^

------WebKitFormBoundaryIb92EAbYgnUFOeO9--^

^"
```
```
<form id="taskForm" action="/lessons/11863/tasks/1167888" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-hHedjW"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div class="Link_root__BZmH+"><div class="LinkTask_root__suzEq"><div class="Links_links__rnvl9"><div class="LinkTaskRow_linkRow__36TU1 LinkTaskRow_text-text__IcWjs"><div class="styled__Root-kZuXys styled__TextAnswer-twouH HHteu hzzNAz LinkTaskRow_linkRowTarget__D79Ny" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE">c.pack()</span></div></div><div class="LinkTaskRow_linkRowContent__XBn6u"><div class="styled__Root-kZuXys styled__TextAnswer-twouH cJxpSA kNrJfQ" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE"></span></div></div></div></div><div class="LinkTaskRow_linkRow__36TU1 LinkTaskRow_text-text__IcWjs"><div class="styled__Root-kZuXys styled__TextAnswer-twouH HHteu hzzNAz LinkTaskRow_linkRowTarget__D79Ny" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE">window.title("Черепашьи бега")</span></div></div><div class="LinkTaskRow_linkRowContent__XBn6u"><div class="styled__Root-kZuXys styled__TextAnswer-twouH cJxpSA kNrJfQ" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE"></span></div></div></div></div><div class="LinkTaskRow_linkRow__36TU1 LinkTaskRow_text-text__IcWjs"><div class="styled__Root-kZuXys styled__TextAnswer-twouH HHteu hzzNAz LinkTaskRow_linkRowTarget__D79Ny" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE">window = Tk()</span></div></div><div class="LinkTaskRow_linkRowContent__XBn6u"><div class="styled__Root-kZuXys styled__TextAnswer-twouH cJxpSA kNrJfQ" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE"></span></div></div></div></div><div class="LinkTaskRow_linkRow__36TU1 LinkTaskRow_text-text__IcWjs"><div class="styled__Root-kZuXys styled__TextAnswer-twouH HHteu hzzNAz LinkTaskRow_linkRowTarget__D79Ny" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE">from tkinter import *</span></div></div><div class="LinkTaskRow_linkRowContent__XBn6u"><div class="styled__Root-kZuXys styled__TextAnswer-twouH cJxpSA kNrJfQ" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE"></span></div></div></div></div><div class="LinkTaskRow_linkRow__36TU1 LinkTaskRow_text-text__IcWjs"><div class="styled__Root-kZuXys styled__TextAnswer-twouH HHteu hzzNAz LinkTaskRow_linkRowTarget__D79Ny" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE">c = Canvas(window, width=200, height=300, bg='red')</span></div></div><div class="LinkTaskRow_linkRowContent__XBn6u"><div class="styled__Root-kZuXys styled__TextAnswer-twouH cJxpSA kNrJfQ" dir="auto"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Content-kLBBmq kwjolo"><span class="MathContent_content__2a8XE"></span></div></div></div></div></div><div class="LinkTask_optionsPanel__GLzIR"><div class="styled__OptionsPannel-hnGBWO dvrYPL"><div class="styled__OptionsPannelDescription-clHeWE jJTBAO">*Перетащите элементы на пустые поля сверху</div><div class="Options_root__q5QuO"><div class="Options_optionsRows__JttWG"><div class="OptionsSlide_root__6eXZe Options_optionsRow__0XmZt"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">1</span></div></div></div></div><div class="OptionsSlide_root__6eXZe Options_optionsRow__0XmZt"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">2</span></div></div></div></div><div class="OptionsSlide_root__6eXZe Options_optionsRow__0XmZt"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">3</span></div></div></div></div><div class="OptionsSlide_root__6eXZe Options_optionsRow__0XmZt"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">5</span></div></div></div></div><div class="OptionsSlide_root__6eXZe Options_optionsRow__0XmZt"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">4</span></div></div></div></div></div></div></div></div><div class="styled__OptionsPannel-hnGBWO habNJR"><div class="styled__OptionsPannelDescription-clHeWE jJTBAO">*Перетащите элементы на пустые поля сверху</div><div class="Options_root__q5QuO"><div class="Swipe_root__N+mSn Swipe_tasksTheme__Oc743"><div class="react-swipe-container Swipe_swipe__sJnX5" style="overflow: hidden; visibility: visible; position: relative;"><div style="overflow: hidden; position: relative; width: 1595px;"><div class="Swipe_swipeItem__J7UDr" style="float: left; width: 319px; position: relative; transition-property: transform; left: 0px; transition-duration: 0ms; transform: translate(0px, 0px) translateZ(0px);" data-index="0"><div class="OptionsSlide_root__6eXZe"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">1</span></div></div></div></div></div><div class="Swipe_swipeItem__J7UDr" style="float: left; width: 319px; position: relative; transition-property: transform; left: -319px; transition-duration: 0ms; transform: translate(319px, 0px) translateZ(0px);" data-index="1"><div class="OptionsSlide_root__6eXZe"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">2</span></div></div></div></div></div><div class="Swipe_swipeItem__J7UDr" style="float: left; width: 319px; position: relative; transition-property: transform; left: -638px; transition-duration: 0ms; transform: translate(319px, 0px) translateZ(0px);" data-index="2"><div class="OptionsSlide_root__6eXZe"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">3</span></div></div></div></div></div><div class="Swipe_swipeItem__J7UDr" style="float: left; width: 319px; position: relative; transition-property: transform; left: -957px; transition-duration: 0ms; transform: translate(319px, 0px) translateZ(0px);" data-index="3"><div class="OptionsSlide_root__6eXZe"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">5</span></div></div></div></div></div><div class="Swipe_swipeItem__J7UDr" style="float: left; width: 319px; position: relative; transition-property: transform; left: -1276px; transition-duration: 0ms; transform: translate(319px, 0px) translateZ(0px);" data-index="4"><div class="OptionsSlide_root__6eXZe"><div class="styled__Wrapper-cixSOf lnAqTZ OptionsSlide_option__PBAys OptionsSlide_text__308F-"><div class="styled__Root-jXKnjF styled__TextOption-cUDRhs ddNPvx tOHbf OptionsSlide_option__PBAys OptionsSlide_text__308F-" dir="auto" draggable="true"><div class="fox-ui__sc-s2fogy-0 cieUAC fox-Text MathContent_root__eYcNu styled__Content-gxIQtd hJiVvq"><span class="MathContent_content__2a8XE">4</span></div></div></div></div></div></div></div><div class="Swipe_bntsContainerWrapper__0yA8O"><div class="Swipe_bntsContainer__a0SDp"><span class="Swipe_arrow__pDXN+ Swipe_prev__zR-NY Swipe_compact__XjVwq Swipe_disabled__J6jrs"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50"><g fill-rule="evenodd" transform="matrix(-1 0 0 1 50 0)"><path d="M33.758 25.298a.751.751 0 0 1-.168.262l-5.847 5.847a.752.752 0 0 1-1.063-1.063l4.609-4.609h-13.642a.736.736 0 0 1 0-1.47h13.643l-4.61-4.61a.752.752 0 1 1 1.063-1.065l5.847 5.848a.747.747 0 0 1 .169.265.73.73 0 0 1 .065.297.734.734 0 0 1-.066.298z"></path></g></svg></span><span class="Swipe_arrow__pDXN+ Swipe_next__V-sIf Swipe_compact__XjVwq"><svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" viewBox="0 0 50 50"><g fill-rule="evenodd"><path d="M33.758 25.298a.751.751 0 0 1-.168.262l-5.847 5.847a.752.752 0 0 1-1.063-1.063l4.609-4.609h-13.642a.736.736 0 0 1 0-1.47h13.643l-4.61-4.61a.752.752 0 1 1 1.063-1.065l5.847 5.848a.747.747 0 0 1 .169.265.73.73 0 0 1 .065.297.734.734 0 0 1-.066.298z"></path></g></svg></span></div></div></div></div></div></div></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div><div class="actions_userAnswerBlock__2vq+R actions_noSolved__ArVBT"><div class="actions_left__bKCPf"><div class="actions_attempt__qlfSc">Попытка 1 из 1<div class="fox-ui__sc-1r4rhyb-0 bufWQz actions_hintIcon__vbqX0"><span data-id="rf-24544" style="cursor: help; z-index: 100; display: inline-flex; flex-direction: column;"><div class="fox-ui__sc-yfeniy-0 iaFAsc fox-Icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.986 6.995v-2.019h-1.972v2.02h1.972zm0 8.029v-6.01h-1.972v6.01h1.972zm-.986-15.024c1.827 0 3.518.457 5.072 1.37a9.478 9.478 0 0 1 3.558 3.558 9.835 9.835 0 0 1 1.37 5.072 9.835 9.835 0 0 1-1.37 5.072 9.478 9.478 0 0 1-3.558 3.558 9.835 9.835 0 0 1-5.072 1.37 9.835 9.835 0 0 1-5.072-1.37 9.657 9.657 0 0 1-3.558-3.582 9.79 9.79 0 0 1-1.37-5.048 9.79 9.79 0 0 1 1.37-5.048 9.842 9.842 0 0 1 3.582-3.582 9.79 9.79 0 0 1 5.048-1.37z"></path></svg></div></span></div></div></div><div class="actions_right__fgCRg"><div class="actions_answer__wXrNe actions_noSolved__ArVBT"><span>За решение задачи </span><span class="fox-ui__sc-s2fogy-0 eYacsZ fox-Text">1&nbsp;балл</span></div><button class="fox-ui__sc-16o31r2-1 gVeljo fox-Button actions_button__3GaLH" type="submit"><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Ответить</span></button></div><div class="Visible_root__si8Vu Visible_block__C-o3Q Visible_extraSmall__voerG Visible_small__sSy7q"><div class="fox-ui__sc-1r4rhyb-0 BTwgM"></div></div></div></form>
```


### ANSWER ATTEMPT html and payload (for answer and test executions) for 3.2 CODE TYPE
```
<form id="taskForm" action="/lessons/11859/tasks/1167870" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-hHedjW"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div class="fox-ui__sc-1r4rhyb-0 fJsaU"><div class="fox-ui__sc-s2fogy-0 dBqbWf fox-Text">Напишите программу</div></div><div class="fox-ui__sc-1r4rhyb-0 hiRqGj"></div><div class="fox-ui__sc-1r4rhyb-0 fJsaU"><div class="Grid_grid__LD9NA"><div class="Grid_row__JizEJ"><div class="Grid_col__HCI9z Grid_col-2-of-4__nhPbZ Grid_col-s-4-of-4__jl0o4"><div class="fox-ui__sc-s2fogy-0 dWBaYQ fox-Text"><span class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">Time Limit:</span> 2&nbsp;sec</div><div class="fox-ui__sc-s2fogy-0 dWBaYQ fox-Text"><span class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">Memory Limit:</span> 16&nbsp;MB</div></div><div class="Grid_col__HCI9z Grid_v-align-bottom__drti8 Grid_col-2-of-4__nhPbZ Grid_col-s-4-of-4__jl0o4"><div class="fox-ui__sc-1r4rhyb-0 jYlfyk"><div class="flex__StyledRoot-dvmwuX dfzcPu"><div class="fox-ui__sc-s2fogy-0 dWBaYQ fox-Text">Python 3</div><div class="fox-ui__sc-1r4rhyb-0 gnicwe"></div><button class="fox-ui__sc-16o31r2-1 hRDPcl fox-Button styled__Button-gUuoZM kRIfPb" type="button"><span class="icon"><div class="fox-ui__sc-yfeniy-0 kOdyIh fox-Icon"><svg viewBox="-1 0 14 14" xmlns="http://www.w3.org/2000/svg"><path d="M10.69 5.54 2.44.66C1.76.26.75.66.75 1.62v9.75c0 .9.94 1.43 1.69.99l8.25-4.88c.72-.44.72-1.5 0-1.94Z"></path></svg></div></span><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Запуск</span></button></div></div></div></div></div></div><div class="styled__Container-hOktxw djCDie"><div height="311" class="styled__Group-idhgNJ fhWJBD"><div size="1" class="styled__Panel-gteQvc hgILmg"><div class="styled__PanelHeader-drQMIX iUEzow">Main</div><div class="styled__PanelContent-hmJBbR hUhpwg"><div class="cm-theme wkUtils_userSelectable__mVwX6" style="height: 100%; font-size: 14px;"><div class="cm-editor ͼ1 ͼ2 ͼ4 ͼ27 ͼ15"><div aria-live="polite" style="position: fixed; top: -10000px;"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 27.5938px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 19.5938px; margin-top: 4px;">1</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 19.5938px; margin-top: 4px;"></div></div></div><div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" style="tab-size: 4" role="textbox" aria-multiline="true" data-language="python" aria-autocomplete="list"><div class="cm-activeLine cm-line"><br></div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 36.7031px; top: 5px; height: 17px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div><div height="178" class="styled__Group-idhgNJ cXKOGK"><div size="1" class="styled__Panel-gteQvc hgILmg"><div class="styled__PanelHeader-drQMIX iUEzow">Input</div><div class="styled__PanelContent-hmJBbR hUhpwg"><div class="cm-theme wkUtils_userSelectable__mVwX6" style="height: 100%; font-size: 14px;"><div class="cm-editor ͼ1 ͼ2 ͼ4 ͼ2f ͼ15"><div aria-live="polite" style="position: fixed; top: -10000px;"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 42px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px;">1</div><div class="cm-gutterElement" style="height: 14px;">2</div><div class="cm-gutterElement" style="height: 14px;">3</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px;"></div></div></div><div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" style="tab-size: 4;" role="textbox" aria-multiline="true"><div class="cm-activeLine cm-line">2</div><div class="cm-line">2</div><div class="cm-line">9</div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 36.7031px; top: 5px; height: 17px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div><div size="1" class="styled__Panel-gteQvc hgILmg"><div class="styled__PanelHeader-drQMIX iUEzow">Output</div><div class="styled__PanelContent-hmJBbR hUhpwg"><div class="cm-theme wkUtils_userSelectable__mVwX6" style="height: 100%; font-size: 14px;"><div class="cm-editor ͼ1 ͼ2 ͼ4 ͼ2l ͼ15"><div aria-live="polite" style="position: fixed; top: -10000px;"></div><div tabindex="-1" class="cm-scroller"><div class="cm-gutters" aria-hidden="true" style="min-height: 14px; position: sticky;"><div class="cm-gutter cm-lineNumbers"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;">9</div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px;">1</div></div><div class="cm-gutter cm-foldGutter"><div class="cm-gutterElement" style="height: 0px; visibility: hidden; pointer-events: none;"><span title="Unfold line">›</span></div><div class="cm-gutterElement cm-activeLineGutter" style="height: 14px;"></div></div></div><div spellcheck="false" autocorrect="off" autocapitalize="off" translate="no" contenteditable="true" class="cm-content" style="tab-size: 4" role="textbox" aria-multiline="true" aria-readonly="true"><div class="cm-activeLine cm-line"><img class="cm-widgetBuffer" aria-hidden="true"><span class="cm-placeholder" aria-label="placeholder 2" contenteditable="false" style="pointer-events: none;">2</span><br></div></div><div class="cm-layer cm-layer-above cm-cursorLayer" aria-hidden="true" style="z-index: 150; animation-duration: 1200ms;"><div class="cm-cursor cm-cursor-primary" style="left: 36.7031px; top: 5px; height: 17px;"></div></div><div class="cm-layer cm-selectionLayer" aria-hidden="true" style="z-index: -2;"></div></div></div></div></div></div></div></div><div class="fox-ui__sc-b5xwi9-2 dCrOvC"></div><div class="fox-ui__sc-1r4rhyb-0 fJsaU"><div class="fox-ui__sc-s2fogy-0 eDXzPT fox-Text">Тесты</div></div><div class="Grid_grid__LD9NA"><div class="Grid_row__JizEJ"><div class="Grid_col__HCI9z Grid_col-2-of-4__nhPbZ Grid_col-s-4-of-4__jl0o4"><div class="fox-ui__sc-1r4rhyb-0 jJoqtq"><div class="fox-ui__sc-1r4rhyb-0 fJsaU"><div class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">Accepted: <span class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">0</span> / Failed: <span class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">0</span></div></div><div class="fox-ui__sc-10x2wrn-3 lkcyVz styled__ProgressSegmented-bvseNd cSjoRD"><div class="fox-ui__sc-10x2wrn-0 dbSGsT"></div><div class="fox-ui__sc-10x2wrn-1 fkSGxN"><div class="fox-ui__sc-10x2wrn-2 iudIZr"></div><div class="fox-ui__sc-10x2wrn-2 iudIZr"></div><div class="fox-ui__sc-10x2wrn-2 iudIZr"></div><div class="fox-ui__sc-10x2wrn-2 iudIZr"></div></div></div></div></div><div class="Grid_col__HCI9z Grid_col-2-of-4__nhPbZ Grid_col-s-4-of-4__jl0o4"><div class="fox-ui__sc-1r4rhyb-0 jJoqtq"><div class="fox-ui__sc-s2fogy-0 jTidKk fox-Text"><button class="fox-ui__sc-16o31r2-1 gzXmVA fox-Button" type="button"><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Запустить тесты</span></button></div></div></div></div></div><div class="styled__TableWrapper-jwxOFX ervtAC"><table><thead><tr><th width="33"><div class="fox-ui__sc-s2fogy-0 eLrAey fox-Text">#</div></th><th><div class="fox-ui__sc-s2fogy-0 fqgoBx fox-Text">Результат</div></th><th width="90"><div class="fox-ui__sc-s2fogy-0 fqgoBx fox-Text"></div></th></tr></thead><tbody><tr><td><div class="fox-ui__sc-s2fogy-0 eLrAey fox-Text">1</div></td><td><div class="fox-ui__sc-s2fogy-0 nQbXf fox-Text">Not available</div></td><td><div class="fox-ui__sc-s2fogy-0 fqgoBx fox-Text"></div></td></tr><tr><td><div class="fox-ui__sc-s2fogy-0 eLrAey fox-Text">2</div></td><td><div class="fox-ui__sc-s2fogy-0 nQbXf fox-Text">Not available</div></td><td><div class="fox-ui__sc-s2fogy-0 fqgoBx fox-Text"></div></td></tr><tr><td><div class="fox-ui__sc-s2fogy-0 eLrAey fox-Text">3</div></td><td><div class="fox-ui__sc-s2fogy-0 nQbXf fox-Text">Not available</div></td><td><div class="fox-ui__sc-s2fogy-0 fqgoBx fox-Text"></div></td></tr></tbody></table></div><div class="fox-ui__sc-1r4rhyb-0 jXFDMI"><div class="fox-ui__sc-s2fogy-0 gKrDtc fox-Text">Успешное прохождение тестов не&nbsp;гарантирует правильность решения задачи.</div></div><div class="fox-ui__sc-b5xwi9-2 jbZIOs"></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div><div class="actions_userAnswerBlock__2vq+R actions_noSolved__ArVBT"><div class="actions_left__bKCPf"><div class="actions_attempt__qlfSc">Попытка 1 из 1<div class="fox-ui__sc-1r4rhyb-0 bufWQz actions_hintIcon__vbqX0"><span data-id="rf-41527" style="cursor: help; z-index: 100; display: inline-flex; flex-direction: column;"><div class="fox-ui__sc-yfeniy-0 iaFAsc fox-Icon"><svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M10.986 6.995v-2.019h-1.972v2.02h1.972zm0 8.029v-6.01h-1.972v6.01h1.972zm-.986-15.024c1.827 0 3.518.457 5.072 1.37a9.478 9.478 0 0 1 3.558 3.558 9.835 9.835 0 0 1 1.37 5.072 9.835 9.835 0 0 1-1.37 5.072 9.478 9.478 0 0 1-3.558 3.558 9.835 9.835 0 0 1-5.072 1.37 9.835 9.835 0 0 1-5.072-1.37 9.657 9.657 0 0 1-3.558-3.582 9.79 9.79 0 0 1-1.37-5.048 9.79 9.79 0 0 1 1.37-5.048 9.842 9.842 0 0 1 3.582-3.582 9.79 9.79 0 0 1 5.048-1.37z"></path></svg></div></span></div></div></div><div class="actions_right__fgCRg"><div class="actions_answer__wXrNe actions_noSolved__ArVBT"><span>За решение задачи </span><span class="fox-ui__sc-s2fogy-0 eYacsZ fox-Text">1&nbsp;балл</span></div><button class="fox-ui__sc-16o31r2-1 euOfwS fox-Button actions_button__3GaLH" type="submit"><span class="fox-ui__sc-16o31r2-0 beoubK fox-Button__content">Ответить</span></button></div><div class="Visible_root__si8Vu Visible_block__C-o3Q Visible_extraSmall__voerG Visible_small__sSy7q"><div class="fox-ui__sc-1r4rhyb-0 BTwgM"></div></div></div></form>
```
answer attempt
```
curl ^"https://kb.cifrium.ru/api/lessons/11859/tasks/1167870/answer_attempts^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryXuIuTIVZNzIjCUTn^" ^
  -b ^"user_agent_uid=6d367a81-8ced-4c73-85d2-b49b8a1853dc; _csrf_token=Vk7va7VNCyE0vApf4L^%^2FZmzBIRAII8BDLRGMVTvvYMupJpfmCrDwsxbOTealxLgPdlx93giQJxQtCI1pOlVYWVg^%^3D^%^3D; _ym_uid=1773496362473771738; _ym_d=1773496362; _ym_isad=2; client_timezone=Europe/Moscow; mindboxDeviceUUID=3292b5d9-fd9c-4f73-af7b-a4c2ee880b76; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^223292b5d9-fd9c-4f73-af7b-a4c2ee880b76^%^22^%^7D; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOakV3TWpkZExDSWtNbUVrTVRBa01scDZUVzl1VmxkWFRDNU5NMjFLWTI0MVVtNXFkU0lzSWpFM056TTBPVFkwTURFdU9ETXdOekEyTkNKZCIsImV4cCI6IjIwMjYtMDYtMTRUMTM6NTM6MjFaIiwicHVyIjpudWxsfX0^%^3D--75d5cd85c20bd7c6117c1e2cc6818237a1af902a; _wk_kbc_session=8db5e18743c501fc2b41e320db621353^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/lessons/11859/tasks/1167870^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: Vk7va7VNCyE0vApf4L/ZmzBIRAII8BDLRGMVTvvYMupJpfmCrDwsxbOTealxLgPdlx93giQJxQtCI1pOlVYWVg==^" ^
  -H ^"X-Device-Id: fc843a63c432edc43ad8b96dd2c8eae4^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/lessons/11859/tasks/1167870^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"X-Skip-Error-Notification: true^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"------WebKitFormBoundaryXuIuTIVZNzIjCUTn^

Content-Disposition: form-data; name=^\^"questions^[1207757^]^[^]^[language^]^\^"^

^

python3^

------WebKitFormBoundaryXuIuTIVZNzIjCUTn^

Content-Disposition: form-data; name=^\^"questions^[1207757^]^[^]^[source_code^]^\^"^

^

def count_cars(bodies, steering_wheels, wheels):^

    max_by_bodies = bodies // 1^

    max_by_steering = steering_wheels // 1^

    max_by_wheels = wheels // 4^

    ^

    return min(max_by_bodies, max_by_steering, max_by_wheels)^

^

cars = count_cars(int(input()), int(input()), int(input()))^

print(cars)^

------WebKitFormBoundaryXuIuTIVZNzIjCUTn--^

^"
```
test executions
```
curl ^"https://kb.cifrium.ru/api/wk/test_case_executions^" ^
  -H ^"Accept: application/json, text/plain, */*^" ^
  -H ^"Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7^" ^
  -H ^"Connection: keep-alive^" ^
  -H ^"Content-Type: application/json^" ^
  -b ^"user_agent_uid=89b3bf31-1f81-462e-b81e-48a92a2fe000; _ym_uid=1773736246251886293; _ym_d=1773736246; _ym_isad=2; mindboxDeviceUUID=9fed348f-684e-4ce2-8bae-21ce1f1a214c; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^229fed348f-684e-4ce2-8bae-21ce1f1a214c^%^22^%^7D; client_timezone=Europe/Moscow; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6IlcxczNOakV3TmpCZExDSWtNbUVrTVRBa1ZXMXhWbXN3V2tWcVlYcFNMa3hFT0M4M1FXMVFkU0lzSWpFM056TTNNell6TURndU1ESTBOakUxTlNKZCIsImV4cCI6IjIwMjYtMDYtMTdUMDg6MzE6NDhaIiwicHVyIjpudWxsfX0^%^3D--df7baba5e0b6b26f8c21f63a6d8d15bb6b9f0007; _wk_kbc_session=fb3844b633d5c49a600378499271c9b5; _csrf_token=c8DmYBRa^%^2FMpKO^%^2B^%^2B5^%^2FvaTaVZwNq720JwdUgy27WFRfyj65^%^2F2eYaOV6uzqhtbRyvX4VJy^%^2Fx1RpaQfgH5M1ecNi1w^%^3D^%^3D^" ^
  -H ^"Origin: https://kb.cifrium.ru^" ^
  -H ^"Referer: https://kb.cifrium.ru/lessons/11862/tasks/1167886^" ^
  -H ^"Sec-Fetch-Dest: empty^" ^
  -H ^"Sec-Fetch-Mode: cors^" ^
  -H ^"Sec-Fetch-Site: same-origin^" ^
  -H ^"User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36^" ^
  -H ^"X-CSRF-Token: c8DmYBRa/MpKO++5/vaTaVZwNq720JwdUgy27WFRfyj65/2eYaOV6uzqhtbRyvX4VJy/x1RpaQfgH5M1ecNi1w==^" ^
  -H ^"X-Device-Id: fc843a63c432edc43ad8b96dd2c8eae4^" ^
  -H ^"X-Referer: https://kb.cifrium.ru/lessons/11862/tasks/1167886^" ^
  -H ^"X-Requested-With: XMLHttpRequest^" ^
  -H ^"sec-ch-ua: ^\^"Not:A-Brand^\^";v=^\^"99^\^", ^\^"Google Chrome^\^";v=^\^"145^\^", ^\^"Chromium^\^";v=^\^"145^\^"^" ^
  -H ^"sec-ch-ua-mobile: ?0^" ^
  -H ^"sec-ch-ua-platform: ^\^"Windows^\^"^" ^
  --data-raw ^"^{^\^"question_id^\^":1207773,^\^"language^\^":^\^"python3^\^",^\^"source_code^\^":^\^"def nums(a, b):^\^\n    if a ^> b:^\^\n        return a * b^\^\n    else:^\^\n        return a + b^\^\n^\^\na = int(input())^\^\nb = int(input())^\^\n^\^\nprint(nums(a, b))^\^"^}^"
```

# excel
excel has no column names. The answer isnt 100% accuracy, so you'll need to check similarity between the excel answer and the html (to retrieve answer value for curl)
3.1) columns: taskId, questionId, answer in text
3.2) columns: taskId, questionId, answer in text


# videos
video progress bar has this html structure, you gotta find it and dial it to 95% to the end, or even closer to the end
```
<div class="d-flex column justify-center player-controls_playerControls__AjvlU"><div class="d-flex align-center justify-center relative"><div class="player-button_buttonWrapper__Q4EmU player-controls_rightMargin__lrbVM" data-testid="player-rewind-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 8C5.46301 5.00943 8.44639 3 12 3C16.9706 3 21 7.02944 21 12C21 16.9706 16.9706 21 12 21C7.36642 21 3.49608 17.4984 3 12.997M3.5 5.5V8H6M16 9H13L12 11.6H14.5C16 11.6 16 12.6716 16 13.5C16 14.3284 15.3284 15 14.5 15H12M9 9V15" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><animateTransform attributeName="transform" type="rotate" from="0 0 0" to="-90 0 0" dur="0.15s" repeatCount="1" begin="indefinite" id="backward"></animateTransform><animateTransform attributeName="transform" type="rotate" from="-90 0 0" to="0 0 0" dur="0.15s" repeatCount="1" begin="backward.end"></animateTransform></svg></div><div class="player-button_buttonWrapper__Q4EmU player-controls_rightMargin__lrbVM" data-testid="player-play-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M16.0417 9.21096C17.6632 10.123 18.4739 10.5791 18.744 11.1783C18.9794 11.7008 18.9794 12.2992 18.744 12.8217C18.4739 13.4209 17.6632 13.877 16.0417 14.789L9.76883 18.3175C8.2012 19.1993 7.41738 19.6402 6.77534 19.5676C6.21522 19.5043 5.70782 19.2076 5.37802 18.7504C5 18.2264 5 17.3271 5 15.5285V8.47151C5 6.67288 5 5.77357 5.37802 5.24957C5.70782 4.79242 6.21522 4.49567 6.77534 4.43235C7.41738 4.35977 8.2012 4.80067 9.76884 5.68247L16.0417 9.21096Z" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><div class="player-button_buttonWrapper__Q4EmU player-controls_rightMargin__lrbVM" data-testid="player-fast-forward-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M20 8C18.537 5.00943 15.5536 3 12 3C7.02944 3 3 7.02944 3 12C3 16.9706 7.02944 21 12 21C16.6336 21 20.5039 17.4984 21 12.997M20.5 5.5V8H18" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M15 9H12L11 11.6H13.5C15 11.6 15 12.6716 15 13.5C15 14.3284 14.3284 15 13.5 15H11M8 9V15" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><animateTransform attributeName="transform" type="rotate" from="0 0 0" to="90 0 0" dur="0.15s" repeatCount="1" begin="indefinite" id="forward"></animateTransform><animateTransform attributeName="transform" type="rotate" from="90 0 0" to="0 0 0" dur="0.15s" repeatCount="1" begin="forward.end"></animateTransform></svg></div><div class="flex-grow-1 player-controls_timelineSpacer__3fiOI"></div><div class="d-flex align-center player-controls_inlineTimeline__GD2DM"><div class="player-timeline_time__6-py+" data-testid="player-current-time">46:35</div><input class="w-100 ml-4 mr-4" data-testid="player-timeline-slider" type="range" step="any" min="0" max="2798.947999" aria-label="Перемотка" value="2795" style="background-size: 99.8589% 100%;"><div class="player-timeline_time__6-py+" data-testid="player-total-time">46:38</div></div><div class="player-volume_volumeWrapper__UEKoG player-controls_leftMargin__LgW2O"><div class="player-button_buttonWrapper__Q4EmU volumeButton" data-testid="player-volume-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="player-volume_volumeIcon__L+SSe"><path d="M16.0004 8.99984C16.6281 9.8355 17 10.8742 17 11.9998C17 13.1254 16.6281 14.1642 16.0004 14.9998M18 5.29152C19.8412 6.93948 21 9.33434 21 11.9998C21 14.6653 19.8412 17.0602 18 18.7082M4.6 8.99984H5.5012C6.05213 8.99984 6.32759 8.99984 6.58285 8.93116C6.80903 8.87032 7.02275 8.77021 7.21429 8.63542C7.43047 8.48328 7.60681 8.27166 7.95951 7.84843L10.5854 4.69733C11.0211 4.17451 11.2389 3.9131 11.4292 3.8859C11.594 3.86234 11.7597 3.92233 11.8712 4.04592C12 4.18864 12 4.52892 12 5.20948V18.7902C12 19.4708 12 19.811 11.8712 19.9538C11.7597 20.0774 11.594 20.1373 11.4292 20.1138C11.239 20.0866 11.0211 19.8252 10.5854 19.3023L7.95951 16.1512C7.60681 15.728 7.43047 15.5164 7.21429 15.3643C7.02275 15.2295 6.80903 15.1294 6.58285 15.0685C6.32759 14.9998 6.05213 14.9998 5.5012 14.9998H4.6C4.03995 14.9998 3.75992 14.9998 3.54601 14.8908C3.35785 14.795 3.20487 14.642 3.10899 14.4538C3 14.2399 3 13.9599 3 13.3998V10.5998C3 10.0398 3 9.75976 3.10899 9.54585C3.20487 9.35769 3.35785 9.20471 3.54601 9.10883C3.75992 8.99984 4.03995 8.99984 4.6 8.99984Z" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><div class="player-volume_volumeContainer__fpDie" style="display: none;"><input class="player-volume_volumeBar__QN2wa" data-testid="player-volume-slider" type="range" step="0.01" min="0" max="1" aria-label="Громкость" value="1" style="background-size: 100% 100%;"></div></div><div class="player-controls_leftMargin__LgW2O"><div class="player-button_buttonWrapper__Q4EmU settingsButton" data-testid="player-settings-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="player-settings_settingsIcon__3OZQp"><path d="M15 12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12C9 10.3431 10.3431 9 12 9C13.6569 9 15 10.3431 15 12Z" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M12.9046 3.06005C12.6988 3 12.4659 3 12 3C11.5341 3 11.3012 3 11.0954 3.06005C10.7942 3.14794 10.5281 3.32808 10.3346 3.57511C10.2024 3.74388 10.1159 3.96016 9.94291 4.39272C9.69419 5.01452 9.00393 5.33471 8.36857 5.123L7.79779 4.93281C7.3929 4.79785 7.19045 4.73036 6.99196 4.7188C6.70039 4.70181 6.4102 4.77032 6.15701 4.9159C5.98465 5.01501 5.83376 5.16591 5.53197 5.4677C5.21122 5.78845 5.05084 5.94882 4.94896 6.13189C4.79927 6.40084 4.73595 6.70934 4.76759 7.01551C4.78912 7.2239 4.87335 7.43449 5.04182 7.85566C5.30565 8.51523 5.05184 9.26878 4.44272 9.63433L4.16521 9.80087C3.74031 10.0558 3.52786 10.1833 3.37354 10.3588C3.23698 10.5141 3.13401 10.696 3.07109 10.893C3 11.1156 3 11.3658 3 11.8663C3 12.4589 3 12.7551 3.09462 13.0088C3.17823 13.2329 3.31422 13.4337 3.49124 13.5946C3.69158 13.7766 3.96395 13.8856 4.50866 14.1035C5.06534 14.3261 5.35196 14.9441 5.16236 15.5129L4.94721 16.1584C4.79819 16.6054 4.72367 16.829 4.7169 17.0486C4.70875 17.3127 4.77049 17.5742 4.89587 17.8067C5.00015 18.0002 5.16678 18.1668 5.5 18.5C5.83323 18.8332 5.99985 18.9998 6.19325 19.1041C6.4258 19.2295 6.68733 19.2913 6.9514 19.2831C7.17102 19.2763 7.39456 19.2018 7.84164 19.0528L8.36862 18.8771C9.00393 18.6654 9.6942 18.9855 9.94291 19.6073C10.1159 20.0398 10.2024 20.2561 10.3346 20.4249C10.5281 20.6719 10.7942 20.8521 11.0954 20.94C11.3012 21 11.5341 21 12 21C12.4659 21 12.6988 21 12.9046 20.94C13.2058 20.8521 13.4719 20.6719 13.6654 20.4249C13.7976 20.2561 13.8841 20.0398 14.0571 19.6073C14.3058 18.9855 14.9961 18.6654 15.6313 18.8773L16.1579 19.0529C16.605 19.2019 16.8286 19.2764 17.0482 19.2832C17.3123 19.2913 17.5738 19.2296 17.8063 19.1042C17.9997 18.9999 18.1664 18.8333 18.4996 18.5001C18.8328 18.1669 18.9994 18.0002 19.1037 17.8068C19.2291 17.5743 19.2908 17.3127 19.2827 17.0487C19.2759 16.8291 19.2014 16.6055 19.0524 16.1584L18.8374 15.5134C18.6477 14.9444 18.9344 14.3262 19.4913 14.1035C20.036 13.8856 20.3084 13.7766 20.5088 13.5946C20.6858 13.4337 20.8218 13.2329 20.9054 13.0088C21 12.7551 21 12.4589 21 11.8663C21 11.3658 21 11.1156 20.9289 10.893C20.866 10.696 20.763 10.5141 20.6265 10.3588C20.4721 10.1833 20.2597 10.0558 19.8348 9.80087L19.5569 9.63416C18.9478 9.26867 18.6939 8.51514 18.9578 7.85558C19.1262 7.43443 19.2105 7.22383 19.232 7.01543C19.2636 6.70926 19.2003 6.40077 19.0506 6.13181C18.9487 5.94875 18.7884 5.78837 18.4676 5.46762C18.1658 5.16584 18.0149 5.01494 17.8426 4.91583C17.5894 4.77024 17.2992 4.70174 17.0076 4.71872C16.8091 4.73029 16.6067 4.79777 16.2018 4.93273L15.6314 5.12287C14.9961 5.33464 14.3058 5.0145 14.0571 4.39272C13.8841 3.96016 13.7976 3.74388 13.6654 3.57511C13.4719 3.32808 13.2058 3.14794 12.9046 3.06005Z" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><div class="player-settings_settingsContainer__Llkf-" data-testid="player-settings-popup" style="display: none;"><div class="player-list_playerListWrapper__zJAVQ"><div class="player-list_playerList__btBoV"><div class="player-list_playerListItem__onpEc" data-testid="player-settings-quality-button"><div class="player-list_itemIcon__Xzc2Q"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M12.5 12.9166C12.2636 11.9657 11.2342 11.2499 10 11.2499C8.76583 11.2499 7.73636 11.9657 7.5 12.9166M10 7.91659H10.0083M10.8333 7.91659C10.8333 8.37682 10.4602 8.74992 10 8.74992C9.53976 8.74992 9.16667 8.37682 9.16667 7.91659C9.16667 7.45635 9.53976 7.08325 10 7.08325C10.4602 7.08325 10.8333 7.45635 10.8333 7.91659ZM5.5 3.33325H14.5C15.5501 3.33325 16.0751 3.33325 16.4762 3.51491C16.829 3.6747 17.1159 3.92966 17.2956 4.24327C17.5 4.59979 17.5 5.0665 17.5 5.99992V13.9999C17.5 14.9333 17.5 15.4 17.2956 15.7566C17.1159 16.0702 16.829 16.3251 16.4762 16.4849C16.0751 16.6666 15.5501 16.6666 14.5 16.6666H5.5C4.4499 16.6666 3.92485 16.6666 3.52377 16.4849C3.17096 16.3251 2.88413 16.0702 2.70436 15.7566C2.5 15.4 2.5 14.9333 2.5 13.9999V5.99992C2.5 5.0665 2.5 4.59979 2.70436 4.24327C2.88413 3.92966 3.17096 3.6747 3.52377 3.51491C3.92485 3.33325 4.4499 3.33325 5.5 3.33325Z" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><div class="player-list_itemText__-GlYa">Разрешение (авто)</div></div><div class="player-list_playerListItem__onpEc" data-testid="player-settings-speed-button"><div class="player-list_itemIcon__Xzc2Q"><svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2.5 12.5H6.66667M4.16667 15H8.33333M6.66667 17.5H10.833M10 5V2.5C14.1421 2.5 17.5 5.85786 17.5 10C17.5 12.9024 15.8513 15.4198 13.4393 16.6667M10 10L6.66667 6.66667M2.54577 9.16667C2.68109 7.94262 3.11097 6.80736 3.76296 5.83333" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><div class="player-list_itemText__-GlYa">Скорость (1х)</div></div></div></div></div></div><div class="player-button_buttonWrapper__Q4EmU player-controls_leftMargin__LgW2O" data-testid="player-fullscreen-button"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M4 9V5.6C4 5.03995 4 4.75992 4.10899 4.54601C4.20487 4.35785 4.35785 4.20487 4.54601 4.109C4.75992 4 5.03995 4 5.6 4L9 4M4 15V18.4C4 18.9601 4 19.2401 4.10899 19.454C4.20487 19.6422 4.35785 19.7951 4.54601 19.891C4.75992 20 5.03995 20 5.6 20L9 20M15 4H18.4C18.9601 4 19.2401 4 19.454 4.10899C19.6422 4.20487 19.7951 4.35785 19.891 4.54601C20 4.75992 20 5.03995 20 5.6V9M20 15V18.4C20 18.9601 20 19.2401 19.891 19.454C19.7951 19.6422 19.6422 19.7951 19.454 19.891C19.2401 20 18.9601 20 18.4 20H15" stroke="var(--icon-color)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div></div><div class="d-flex align-center pt-3 pb-3 player-controls_bottomTimeline__OnoGh"><div class="player-timeline_time__6-py+" data-testid="player-current-time">46:35</div><input class="w-100 ml-4 mr-4" data-testid="player-timeline-slider" type="range" step="any" min="0" max="2798.947999" aria-label="Перемотка" value="2795" style="background-size: 99.8589% 100%;"><div class="player-timeline_time__6-py+" data-testid="player-total-time">46:38</div></div></div>
```



# misc info
- in curl you can see that in the formdata for radio buttons the answer is stored as a series of numbers, so you'll have to retrieve the text of an answer and find it in the html, and retrieve the number value that you put in the request
- cookies that you see in those curl requests are gonna change with the user that is logged in, we will log in manually and let the script do the work
- csrf token is stored in cookies
- will provide excel file for:
3.1) https://kb.cifrium.ru/teacher/courses/[courseId]/lessons/[taskId] - test1.xlsx
3.2) https://kb.cifrium.ru/lessons/[taskId]/tasks/[questionId] - test2.xlsx