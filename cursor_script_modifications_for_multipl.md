# Script modifications for multiple choice tests
_Exported on 3/15/2026 at 00:13:31 GMT+3 from Cursor (2.5.26)_

---

**User**

this is a script for completing tests on a website for me, ive added ANSWER ATTEMPT payload and html for a MULTIPLE CHOICE TYPE OF URL FORMAT 3.2 in @requirements.md , your task is to analyze the script and add changes to the script so it completes tasks of this type

---

**Cursor**


Читаю requirements.md и скрипты, чтобы понять формат 3.2 и добавить поддержку множественного выбора.



Просматриваю парсер страницы и модуль отправки ответов, чтобы добавить поддержку множественного выбора (checkbox).



Добавляю поддержку типа «множественный выбор» (checkbox) для формата 3.2.



Проверяю разбор ответа с переносами строк: исправляю разделители в `similarity.py`.



Кратко, что сделано для поддержки **MULTIPLE CHOICE (формат 3.2)**:

### 1. **page_parser.py**
- В результат парсера добавлено поле `is_multiple_choice`.
- Распознаются чекбоксы: `input type="checkbox"` с `name="questions[ID][]"`.
- Для них заполняются `question_form_key` и `options` (как у radio), метка берётся из той же структуры (следующий div / `MathContent_content`).

### 2. **similarity.py**
- Добавлена функция **`best_matches_multiple(answer, options, threshold)`**:
  - разбивает ответ из Excel по запятой, точке с запятой, `|` и переводу строки;
  - для каждой части ищет лучшее совпадение среди вариантов (как в radio);
  - возвращает список **значений** выбранных вариантов (без дубликатов, порядок сохраняется).

### 3. **api_submit.py**
- Добавлена **`submit_answer_3_2_multiple(session, lesson_id, task_id, form_question_key, answer_values)`**:
  - отправляет POST на `/api/lessons/{lesson_id}/tasks/{task_id}/answer_attempts`;
  - в теле — несколько частей с одним и тем же именем `questions[ID][]`, по одной на каждое значение из `answer_values` (как в вашем curl с 10162093 и 10162094);
  - Referer: `/lessons/.../tasks/...` (как в требованиях для этого типа).

### 4. **run_32.py**
- После проверки `is_text_input` добавлена ветка **`is_multiple_choice`**:
  - вызывается `best_matches_multiple(answer, options)` для получения списка значений;
  - если список пустой — задача пропускается с сообщением;
  - иначе вызывается `submit_answer_3_2_multiple(..., answer_values)`.

**Формат ответа в Excel для множественного выбора:** несколько вариантов через запятую, точку с запятой, `|` или новую строку, например: `def, for` или `print; str`. Текст сопоставляется с подписями вариантов на странице (как для radio), порог задаётся `ANSWER_SIMILARITY_THRESHOLD` в конфиге.

---

**User**

can you comment out the video playback skip part for now? it takes up time looking for  the element to use for skipping to 95% time and doesnt even do it. can you also check for flaws in the approach?

---

**Cursor**


Комментирую блок перемотки видео и добавляю краткий разбор недостатков подхода.



Сделано следующее:

1. **Отключена перемотка видео**  
   Закомментированы вызов `_seek_all_video_tabs_to_95(driver)` и сообщение о перемотке. Открытие ссылок на видео в новых вкладках и пауза 3 с остаются — вкладки по-прежнему открываются.

2. **В начале файла добавлен блок с разбором недостатков подхода** (для возможного включения позже):
   - **Проверяются все вкладки с таймаутом 8 с** — первая вкладка часто страница логина без плеера, из-за чего время тратится впустую.
   - **Плеер может быть в iframe** — переключения во фрейм нет, слайдер так и не находится.
   - **Изменение `input.value` и `dispatchEvent`** может не вызывать реальную перемотку на сайте, если плеер хранит состояние в своём JS и только отображает его в range input.
   - **Нет ожидания загрузки плеера** — перед поиском слайдера только 0.5 с на вкладку, без проверки, что страница/плеер загрузились.

Функции `_seek_video_tab_to_percent` и `_seek_all_video_tabs_to_95` не удалялись — их можно снова использовать, когда будет нужна перемотка (например, после проверки URL вкладки на `/groups/`, переключения в iframe плеера и ожидания появления слайдера).

---

**User**

1) when a question has already been answered the html changes i guess, which causes the script to stall because its trying to find a form question key which takes up a solid 8 seconds.

when a question has already been answered,  the html for the form looks like this (this is radio type question, probabbly should work for other types)

<form id="taskForm" action="/lessons/11861/tasks/1167880" method="post" class="wkUtils_userUnselectable__tdz2n notranslate" translate="no"><div class="styled__Wrapper-hHedjW"><div class="fox-ui__sc-1r4rhyb-0 cklDCA"><div><div><div><div class="styled__Root-jGVGzp elJqVq"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207767]" type="radio" tabindex="-1" value="10162087"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Сумма чисел a и b</span></div></div><div class="styled__Root-jGVGzp elJqVq"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207767]" type="radio" tabindex="-1" value="10162088"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Произведение чисел a и b</span></div></div><div class="styled__Root-jGVGzp elJqVq"><div class="styled__Root-fWNNWA iMjaXV"></div><input class="input" name="questions[1207767]" type="radio" tabindex="-1" value="10162089"><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Ошибка</span></div></div><div class="styled__Root-jGVGzp kbsdwh"><div class="styled__Root-fWNNWA bNtOQf"><div class="styled__Dot-hfknO RXeBB"></div></div><input class="input" name="questions[1207767]" type="radio" tabindex="-1" value="10162090" checked=""><div class="fox-ui__sc-s2fogy-0 iwHwmg fox-Text MathContent_root__eYcNu styled__Label-iUCEmK jNuXTI"><span class="MathContent_content__2a8XE" dir="auto">Ничего</span></div></div></div></div></div></div><div class="wkUtils_avoidPageBreakInside__55agg"></div></div></form>



2) in code type questions it waits too long before answering for some reason

---

**Cursor**


Просматриваю полный поток в run_32 и page_parser, чтобы добавить определение «уже решено» и сократить ожидания для кода.



Добавляю определение «уже решено» и сокращаю ожидания для кода.



Учитывая кнопку «Ответить» с атрибутом disabled:



Меняю `run_32`: возвращаю кортеж из `_get_page_html`, добавляю проверку «уже решено» в ожидание и сокращаю таймауты.



Проверяю run_31 на ту же логику ожидания формы:



Кратко, что сделано:

---

### 1) Уже решённые задания — без долгого ожидания

**В `page_parser.py` добавлена функция `is_task_already_answered(html)`.** Она считает задание уже решённым, если:
- в форме `#taskForm` нет кнопки «Ответить» или у кнопки есть атрибут `disabled`;
- в HTML есть классы/текст вроде `actions_solved`, `alreadySolved`, `taskSolved`, или фразы «Решено», «Принято», «Верно», «Ответ засчитан» и т.п.

**В `run_32.py` обновлена логика ожидания:**
- Сразу после загрузки страницы проверяется «уже решено»; если да — возвращается `(None, True)` без ожидания формы.
- Условие ожидания заменено на: **форма появилась ИЛИ страница в состоянии «уже решено»**. Ожидание прерывается, как только выполняется одно из двух, поэтому не будет полных 8 секунд на «результатной» странице.
- Таймауты уменьшены: `FORM_WAIT_MAIN` с 2 до 1.5 с, `FORM_WAIT_IFRAME` с 2 до 1 с.
- Если форма так и не найдена (в т.ч. во фреймах), перед возвратом ещё раз проверяется «уже решено» по текущему `page_source`; при положительной проверке возвращается `(None, True)`.

В цикле по заданиям: при `already_answered` выводится «Task … already answered, skip.» и переход к следующему заданию без попытки отправить ответ.

---

### 2) Код-задачи — меньше ожиданий перед ответом

- **Сначала запрос к API:** для код-задач сначала вызывается `_get_code_ids_from_api()` (без ожидания в браузере). Только если API не вернул id, делаются попытки через браузер.
- **Меньше и короче паузы в браузере:** вместо трёх попыток по 0.8 с — две попытки по 0.3 с.
- **Меньше пауза при CodeMirror:** после обнаружения `taskForm` и `cm-editor` пауза уменьшена с 1.2 с до 0.4 с перед повторным чтением HTML.

В итоге для уже решённых заданий скрипт почти не ждёт, для код-задач время до отправки ответа сокращено (особенно когда API сразу отдаёт id).

---

**User**

it still waits a solid 8 seconds at the last question of the  task if that question has already been answered:

[3.1] Question 1197266 ...
[3.1] Page loaded, waiting for form...

---

**Cursor**


Добавляю в run_31 ту же проверку «уже решено», что и в run_32.



Исправляя логику: `continue` внутри цикла по iframe переходит к следующему iframe, а не к следующему вопросу. Вынесем проверку и переход к следующему вопросу после цикла (флаг + break).



В **run_31** сделаны такие изменения:

1. **Сразу после загрузки страницы** вызывается `is_task_already_answered(driver.page_source)`. Если задание уже решено — выводится «Question … already answered, skip.» и переход к следующему вопросу **без ожидания формы** (0 вместо ~8 секунд).

2. **Условие ожидания формы** заменено на кастомное: форма найдена **или** страница в состоянии «уже решено» (`_form_or_solved`). Как только выполняется одно из двух, ожидание прекращается (таймаут 1.5 с вместо 2 с, в iframe — 1 с вместо 2 с).

3. **После получения HTML** (из основного документа или iframe) снова вызывается `is_task_already_answered(page_html)` — если решено, задание пропускается.

4. **Если форма не найдена ни на странице, ни во фреймах** — перед сообщением «Form not found» проверяется «уже решено» по `driver.page_source`; при положительной проверке выводится «already answered, skip.» и переход к следующему вопросу.

В результате для уже решённого последнего вопроса 3.1 скрипт не ждёт 8 секунд: либо срабатывает проверка сразу после загрузки, либо — при первом же вызове `_form_or_solved` во время ожидания.

---

**User**

theres still a noticeable delay in 3.1 and 3.2:

in 3.1 it pauses on the last question of a task, but the previous are fine

in 3.2 it skips a few but pauses on one question for no reason (maybe its because you think there are 3 questions in 3.2, but there are actually 5)

---

**Cursor**


Сокращаю таймауты и добавляю ранний выход, если на странице нет формы (страница завершения или другая).



Добавляю ранний выход при отсутствии формы и сокращаю таймауты.



В ветке с iframe в run_32 при успехе проверять «уже решено» и возвращать (None, True).



Вот что изменено:

---

### 1) Ранний выход, если на странице нет формы (3.1 и 3.2)

После загрузки страницы:
- если в HTML нет ни `questions[`, ни `taskForm` (страница завершения, итог, другой экран),
- делается одна короткая пауза **0.3 с** (чтобы успел подгрузиться JS),
- затем повторная проверка HTML.

Если форма так и не появилась — задание сразу пропускается **без** ожидания 0.8–1.5 с и без перебора iframe. В 3.1 выводится либо «already answered, skip.», либо «No form for question … (completion page?), skip.»

Так убирается долгая пауза на последнем вопросе 3.1 (страница «задание сдано» без формы) и лишняя задержка в 3.2 на страницах без формы.

---

### 2) Более короткие таймауты

- **3.1:** ожидание формы 1.5 с → **0.8 с**, в iframe 1 с → **0.5 с**.
- **3.2:** `FORM_WAIT_MAIN` 1.5 с → **0.8 с**, `FORM_WAIT_IFRAME` 1 с → **0.5 с**.

В сумме при отсутствии формы задержка теперь около **0.3 с** (ранний выход) вместо 0.8 + 0.5×N секунд.

---

### 3) Про «3 вопроса в 3.2, а по факту 5»

Скрипт не задаёт число вопросов сам — он обрабатывает **строки из test2.xlsx**: одна строка = один вопрос (taskId, questionId, ответ). Чтобы обрабатывались все 5 вопросов урока, в файле для этого урока должно быть **5 строк** (по одной на каждый questionId). Если строк только 3, обрабатываются только эти три; остальные два в Excel просто не указаны. Пауза «на одном вопросе» должна уменьшиться за счёт раннего выхода и укороченных таймаутов.

---

**User**

1) increase the wait for form load time by a second

2) it still pauses on the code section, probably because its waiting for the form to load for too long

---

**Cursor**


Увеличиваю таймауты ожидания формы на 1 с и добавляю короткую задержку для код-страниц, чтобы форма и скрытые поля успели подгрузиться.



Сделаны такие изменения:

**1) Увеличены таймауты ожидания формы на 1 с**
- **run_31:** ожидание формы 0.8 с → **1.8 с**, в iframe 0.5 с → **1.5 с**.
- **run_32:** `FORM_WAIT_MAIN` 0.8 с → **1.8 с**, `FORM_WAIT_IFRAME` 0.5 с → **1.5 с**.

**2) Код-задачи в 3.2**
- После получения HTML страницы с `taskForm` и `cm-editor` пауза перед повторным чтением страницы увеличена с 0.4 с до **0.7 с**, чтобы успели подгрузиться CodeMirror и скрытые поля с `code_question_id` перед запросом code_ids.

Итог: у формы и код-редактора больше времени появиться (1.8 с вместо 0.8 с), а на код-странице даётся 0.7 с на инициализацию формы перед отправкой ответа.

---

**User**

why is there a check for iframe on 3.2? i didnt notice any iframes present anywhere

---

**Cursor**


Удаляю проверку iframe в run_32 — она, скорее всего, скопирована из run_31 и только добавляет задержки при переборе несуществующих фреймов.



Сделано. Проверка iframe в 3.2 убрана.

**Почему она там была:** логика была перенесена из run_31 (classworks), где форма иногда может быть во фрейме. Для 3.2 (lessons) страницы `/lessons/.../tasks/...` iframe не используются, форма всегда в основном документе.

**Что изменено:**
- Удалён цикл по iframe в `_get_page_html`: при таймауте ожидания формы сразу проверяется «уже решено» по основной странице и возвращается результат.
- Удалены константа `FORM_WAIT_IFRAME` и импорт `EC` (expected_conditions).

В 3.2 при отсутствии формы больше не тратится 1.5 с на каждый несуществующий iframe.

---

**User**

in 3.1 you should increase the waiting for form  period by 1 second

---

**Cursor**


В 3.1 таймауты ожидания формы увеличены на 1 с:
- основной документ: 1.8 с → **2.8 с**
- iframe: 1.5 с → **2.5 с**

---

**User**

give it another 1.5 seconds

---

**Cursor**


В 3.1 таймауты снова увеличены на 1.5 с:
- основной документ: **4.3 с**
- iframe: **4.0 с**

---

**User**

the form check in 3.2 is now faulty, remove the check of form that ive told you to add,  make it so that if it sees a form in  the html that i've specified it sends the payload anyways 

---

**Cursor**


Удаляю раннюю проверку «нет формы» в 3.2 и оставляю только проверку «уже решено».



Удаляю раннюю проверку «нет формы» и при таймауте ожидания возвращаю HTML страницы, если в нём есть форма — тогда отправка всё равно попытается выполниться.



Удаляю дублирующую проверку.



В 3.2 сделано так:

1. **Убрана ранняя проверка «нет формы»**  
   Больше нет проверки «если в HTML нет `questions[` и `taskForm`, подождать 0.3 с и выйти». Остаётся только быстрая проверка «уже решено» сразу после загрузки.

2. **После ожидания формы всегда берётся текущий HTML**  
   После `WebDriverWait` (успех или таймаут) в любом случае вызывается `driver.page_source` и этот HTML возвращается. Если форма не успела появиться в DOM, но уже есть в HTML — он всё равно будет использован.

3. **Логика в основном цикле не менялась**  
   Условие по-прежнему: если есть `page_html` и в нём есть `questions[` или `taskForm`, идём в парсинг и отправку. То есть при наличии формы в HTML payload отправляется в любом случае.

---

**User**

do the same for 3.1 pls

---

**Cursor**


Меняю проверку: пропускать только при отсутствии и `questions[`, и `taskForm` в HTML.



В 3.1 сделаны те же изменения:

1. **Убрана ранняя проверка «нет формы»**  
   Удалена проверка «если в HTML нет `questions[` и `taskForm`, подождать 0.3 с и выйти». Остаётся только быстрая проверка «уже решено» после загрузки.

2. **После ожидания формы всегда используется текущий HTML**  
   Если после основного ожидания и перебора iframe `page_html` так и не получили, теперь берётся `driver.page_source` (страница по умолчанию), и по этому HTML идёт дальнейшая обработка.

3. **Пропуск только при полном отсутствии формы**  
   Сообщение «Page has no form» и пропуск вопроса выводятся только если в HTML нет ни `questions[`, ни `taskForm`. Если есть хотя бы один из них, выполняется парсинг и отправка.

4. **Удалён неиспользуемый `import time`.**

