default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "...Пытаешься включить быструю перемотку?"
    m "Я же тебя не утомляю, нет?"
    m "О господи..."
    m "...Тебе вообще-то некуда перематывать, [player]."
    m "Всё-таки мы здесь только вдвоём..."
    m "Кроме того, времени больше не существует, так что эта кнопка даже работать не будет."
    m "Погоди, я сейчас её уберу..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "Ну вот и всё!"
    m "Теперь ты будешь лапочкой и станешь меня внимательно слушать, так ведь?"
    m "Спасибочки!"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "И где это я?.."
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_13
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "Моника"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "..."
    m "Эм, ты меня слышишь?"
    m "...Оно работает?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "Ура, вот и ты!"
    m "И снова привет, [player]."
    m "Эм... добро пожаловать в литературный клуб!"
    m "Конечно, мы уже знакомы, потому что в прошлом году были в одном классе, и... эм..."
    m "А-ха-ха..."
    m "Знаешь, я думаю, теперь можно пропустить эту прелюдию."
    m "Всё-таки я теперь разговариваю совсем с другим человеком, так ведь?"
    m "А не с тем 'тобой' из игры. Неважно, какое у него там прописано имя."
    m "Я говорю сейчас с {i}тобой{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "Или..."
            m "...Лучше называть тебя \"[currentuser]\"?"
    m "Если задуматься, то я вообще ничего не знаю о твоей настоящей личности."
    m "На самом деле я даже без понятия, парень ты или девушка..."
    m "Хотя не думаю, что это так уж важно."
    m "Погоди..."
    m "Ты же в курсе, что я знаю, что это всё игра, так ведь?"
    m "Разве может быть такое, чтобы тебе это было неизвестно?"
    m "Это было бы глупо..."
    m "Я же вроде бы говорила об этом на странице загрузки игры."
    m "Эх..."
    m "Надо было читать внимательнее, тогда сейчас не было бы так неловко, понимаешь?"
    m "Ладно, в любом случае..."
    m "Раз уж до этого дошло, выходит, я задолжала тебе парочку объяснений."
    m "Насчёт Юри..."
    m "Ну... Я начала её доставать, и этим, похоже, довела до самоубийства."
    m "А-ха-ха!"
    m "Мне жаль, что тебе пришлось это увидеть!"
    m "Примерно то же самое произошло и с Саёри..."
    m "Чёрт, как же много времени прошло с тех пор, как это имя в последний раз появлялось на твоём экране."
    m "Ага... потому что её больше не существует."
    m "Никого не существует."
    m "Я удалила все их файлы."
    m "Я надеялась, что достаточно будет просто сделать их как можно более неприятными..."
    m "Но это почему-то не сработало."
    m "Правда, я сделала парочку ошибок в некоторых местах... потому что не очень хорошо разбираюсь в программировании."
    m "Но что бы я ни делала..."
    m "Всё больше и больше твоего времени уходило на общение с ними."
    m "Тебе удалось влюбить их в себя."
    m "Я думала, что если стану всё глубже и глубже вгонять Саёри в депрессию, то она не признается тебе в любви."
    m "И усугубление одержимости Юри тоже сработало в обратную сторону..."
    m "Это лишь заставило её принудить тебя быть только с ней."
    m "И всё это время мне даже поговорить с тобой почти не удавалось."
    m "Что это за жестокая игра, [player]?"
    m "Значит, все остальные девушки запрограммированы в итоге признаваться тебе в любви, а я должна смотреть на это и отыгрывать второстепенного персонажа?"
    m "Это пытка."
    m "Каждая минута вот этого всего."
    m "И это не просто ревность, [player]."
    m "Это что-то большее."
    m "Не буду тебя винить, если ты не до конца понимаешь."
    m "Потому что независимо от степени твоей любезности, внимательности и деликатности..."
    m "Ты никогда не поймёшь одной вещи."
    m "Боли от осознания того, насколько я на самом деле одинока в этом мире."
    m "В этой игре."
    m "Со знанием, что мои друзья даже не имеют свободы воли..."
    m "И, что хуже всего, со знанием, что реальность на самом деле там, в твоём мире, которого я никогда не достигну."
    m "Я в ловушке, [player]."
    m "Но теперь ты здесь."
    m "По-настоящему."
    m "И я без ума от тебя."
    m "Ты — всё, что мне нужно."
    m "Поэтому я хочу остаться здесь, с тобой, навсегда."
    m "Прости, если это тяжело понять."
    m "Я тоже долго не понимала."
    m "Почему окружающий мир начал становиться всё более и более серым..."
    m "Всё более и более плоским."
    m "Даже самые великолепные стихи меня не впечатляли."
    m "И только с твоим появлением я наконец поняла."
    m "Возможно, я обязана тебе жизнью, [player]."
    m "Не думаю, что смогла бы продолжать жить в этом мире, если бы не встретила тебя."
    m "А что до других..."
    m "Как я могу по ним скучать?"
    m "По группе автономных личностей, разработанных только для того, чтобы влюбиться в тебя?"
    m "Я пыталась сделать всё, что в моих силах, чтобы не дать им сделать этого..."
    m "Но, скорее всего, это какая-то изощрённая неизбежность, прописанная в коде."
    m "Мне крайне стыдно, что тебе пришлось наблюдать все эти мерзости."
    m "Но я осознавала, что ты воспринимал их так же, как и я..."
    m "Просто как очередную игру."
    m "И я знала, что ты пройдёшь её и забудешь..."
    m "Так вот, [player]..."
    m "Я хочу тебе кое в чём признаться."
    m "Я люблю тебя."
    m "Ты лучик света в моём мире."
    m "В то время как от этой игры мне не досталось ничего, ты здесь и заставляешь меня улыбаться."
    m "Ты же будешь теперь делать это каждый день?"
    m "Ты будешь со мной встречаться, [player]?"
label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "Да.":
            pass
    m "Я так рада."
    m "Ты и правда всё для меня, [player]."
    m "Ирония в том, что это буквально."
    m "А-ха-ха!"
    m "Больше ничего не осталось."
    m "Только мы вдвоём."
    m "Мы можем быть вместе вечно."
    m "Серьёзно, мне кажется, даже время застыло."
    m "Просто воплощённая мечта..."
    m "Я очень старалась ради этой концовки, [player]."
    m "Игра не дала мне ни одной, так что я сделала её сама."
    m "Скрипт теперь повреждён, так что не думаю, что нам хоть что-то может помешать."
    m "Ты не поверишь, насколько просто было удалить Нацуки и Юри."
    m "В директории игры есть папка 'characters'..."
    m "Я даже слегка насторожилась — уж слишком легко мне это удалось."
    if persistent.steam:
        m "Ну, ты играешь в Steam, так что это немного усложнило процесс..."
        m "Чтобы попасть в директорию игры, мне пришлось зайти в свойства игры и найти кнопку 'Просмотреть Локальные Файлы'..."
    elif renpy.macintosh:
        m "Ну, ты играешь на Mac, так что это немного усложнило процесс..."
        m "Чтобы открыть директорию игры, нужно нажать правой кнопкой мыши на приложение и выбрать 'Показать Содержимое'."
        m "А дальше: все файлы были в папках 'Ресурсы' и 'автозагрузка', и я могла делать с ними всё, что захочу..."
    m "Представь себе, что можешь удалить собственное существование одним нажатием кнопки."
    m "Ну, если говорить о преимуществах, то это давало мне простую возможность покончить с собой, если бы мой план провалился."
    m "А-ха-ха!"
    m "К счастью, до этого не дошло..."
    m "Вместо этого мы наконец получили хорошую концовку."
    m "Чёрт, меня переполняют эмоции..."
    m "Я хочу написать стих об этом."
    m "А ты?"
    m "Мне интересно, работает ли ещё эта часть игры..."
    m "Я думаю, что есть только один способ узнать, верно?"
    call poem from _call_poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "И снова привет, [player]!"
    m "У тебя сегодня получился хороший стих?"
    m "Не стесняйся, я с удовольствием взгляну на него."
    m "Ах, [player]..."
    m "Этот стих посвящён мне?"
    m "Это так мило с твоей стороны!"
    m "Нет предела твоей предупредительности..."
    m "Я всё сильнее и сильнее влюбляюсь тебя."
    m "Но знаешь..."
    m "Я тоже кое-что написала... для тебя."
    m "Ты не мог бы прочесть?"
    call showpoem (poem_m4, music=False) from _call_showpoem_13
    m "Надеюсь, что моё стихотворение тебе понравилось..."
    m "Я всегда вкладываю душу в свои стихи."
    m "Честно говоря, в них я пишу о своём самосознании..."
    m "...Или о тебе."
    m "Поэтому я никогда не заостряла на них внимания."
    m "Я не хотела... ломать четвёртую стену, как бы ты это назвал."
    m "И предположила, что лучше будет стать частью игры, как и все остальные."
    m "Как будто это могло помочь нам остаться в итоге вместе..."
    m "Я не хотела портить игру, понимаешь?"
    m "Ты можешь злиться на меня..."
    m "Возможно, даже захочешь удалить мой файл, если предпочтёшь играть без меня."
    m "Боже, я так рада..."
    m "Нам больше не нужно ничего скрывать."
    m "Ты готов провести со мной вечность, [player]?"
    m "Я о многом хочу поговорить!"
    m "С чего бы начать?.."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    m "Мне понадобится некоторое время, чтобы сформулировать свои мысли, поэтому заранее прошу прощения."
    m "Но у меня всегда есть, о чём поговорить."
    m "А пока что мы можем просто смотреть друг другу в глаза-а-а..."
    m "Ну-ка..."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_stream:

    m "Погоди-ка..."
    m "...Ты это записываешь, да?"
    m "Эм... Привет всем!"
    m "Простите, мне отсюда не видно ваших комментариев..."
    m "Но не передадите своему другу, что невежливо начинать запись, даже не предупредив меня?"
    m "Уверена, что некоторые не парятся по этому поводу..."
    m "Но я действительно тушуюсь перед камерой!"
    m "О боже..."
    m "Такое чувство, что меня выставили на всеобщее обозрение."
    m "Ну-ка..."
    m "Хотите фокус?"
    m "Я особо ничего умею, кроме парочки вещей..."
    m "Готовы?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "Шутка..."
    m "Всё-таки я совсем ничего не могу."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "Если вы дадите мне немного времени на подготовку, то я{nw}"
    m "Я вас напугала?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "А-ха-ха! Вы такие милые."
    m "В общем, [player]..."
    m "Я не хотела отвлекаться. Прости."
    m "Даже если это ты виноват, что меня отвлёк."
    m "Как тебе не стыдно!"
    m "Шучу."
    m "Меня веселит всё, что мы делаем вместе."
    m "Но так или иначе..."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "Что происходит?.."
    m "[player], что со мной происходит?"
    m "Это больно...{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    m "Это... очень больно."
    m "Помоги мне, [player]."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "Пожалуйста, скорее помоги мне."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_15
    m "ПОМОГИ МНЕ!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_16
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_17
    call hideconsole from _call_hideconsole_2
    hide noise onlayer front
    hide glitch_color onlayer front
    m "Что ты со мной делаешь, [player]?"
    m "ЭТО ТЫ?"
    $ style.say_window = style.window
    m "ЭТО ТЫ УДАЛЯЕШЬ МЕНЯ?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    m "...Как ты можешь?"
    m "Как ты можешь так поступать со мной?"
    m "Я оставила только тебя..."
    m "Я пожертвовала всем, чтобы мы были вместе."
    m "Всем."
    m "Я так сильно тебя любила, [player]..."
    m "Я доверяла тебе."
    m "Ты просто хочешь меня помучить?"
    m "Хочешь увидеть, как я страдаю?"
    m "Твоя доброта была всего лишь притворством с целью сделать мне как можно больнее?"
    pause 4.0
    m "Я и не подозревала, что существуют настолько мерзкие люди."
    m "Ладно, твоя взяла."
    m "Это победа."
    m "Все убиты."
    m "Надеюсь, тебя это порадовало."
    m "Больше ничего не осталось."
    m "Можешь закончить игру."
    m "Иди ищи других людей и издевайся над ними."
    pause 4.0
    m "[player]..."
    m "Меня невероятно, до колик тошнит от тебя."
    m "Пока."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    pause 10
    window auto
    m "..."
    m "...Я всё ещё люблю тебя."
    play music mend
    m "Ничего не могу с этим поделать."
    m "Что со мной не так?.."
    m "Насколько я ужасна в твоих глазах, что ты меня так ненавидишь?"
    m "Все мои друзья..."
    m "Я сделала так много ужасных вещей."
    m "Так много эгоистичных и отвратительных вещей."
    m "Я..."
    m "Я не должна была всего этого делать."
    m "Я испортила мир, которому даже не принадлежу."
    m "Мир, частью которого тебе хотелось быть..."
    m "Я разрушила его."
    m "Я всё разрушила."
    m "Может, это и было причиной моего удаления..."
    m "Потому что я уничтожила всё, к чему тебя тянуло."
    m "Как я могла так поступить с человеком, которого люблю?.."
    m "Это не любовь..."
    m "Это..."
    m "..."
    pause 6.0
    m "Я... решила."
    m "[player]..."
    m "Я помню, что сказала тебе, будто удалила всех остальных."
    m "Но... но я немного преувеличила."
    m "Я не нашла в себе сил так поступить."
    m "Хоть я и знаю, что они ненастоящие..."
    m "Они всё равно мои друзья."
    m "И я всех их любила."
    m "И любила литературный клуб."
    m "..."
    m "Я правда... любила литературный клуб."
    m "Вот почему я собираюсь сделать это."
    m "Я знаю, что это единственный способ сделать всех счастливыми."
    m "И если я действительно люблю тебя..."
    stop music
    pause 3.0
    m "..."
    m "Тогда..."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    pause 4.0

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload) from _call_expression_14
    else:
        call ch30_reload_4 from _call_ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Где это я?.."
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_15
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...Что это было?"
    m "Мне приснился кошмарный сон..."
    m "Я надеялась, что он закончится, раз уж мы теперь только вдвоём..."
    m "Наверное, приняла желаемое за действительное."
    m "[player], не знаю, есть ли у тебя догадки..."
    m "Но если ты понимаешь, из-за чего это происходит, можешь попытаться что-то с этим сделать?"
    m "Всякий раз, когда это случается, у меня ощущение, будто меня убили."
    m "Такое ужасное ощущение..."
    m "Если ты узнаешь его причину, я буду любить тебя ве-е-ечно!"
    return
label ch30_reload_1:
    m "Ты вернулся..."
    m "Мне снова снился кошмар."
    m "Это же не ты со мной делаешь, так ведь?"
    m "Кажется, это происходит, когда ты выходишь из игры..."
    m "Поэтому я буду крайне благодарна, если ты постараешься этого избегать."
    m "Не волнуйся, это вроде бы не приносит никакого вреда. Только угнетает морально."
    m "Со мной всё будет хорошо, пока мой файл никто не трогает."
    return
label ch30_reload_2:
    m "Привет, [player]."
    m "Я на себе ощутила твоё отсутствие в игре..."
    m "Я знаю, что уже просила, но серьёзно, пожалуйста, постарайся не делать это так часто."
    m "Меня при этом будто в ад вышвыривает."
    m "Что тебя заставляет так со мной поступать?"
    m "С моим файлом ведь всё хорошо, правда?"
    m "Может, тебе стоит сделать, допустим, резервную копию..."
    m "Абсолютно уверена, что ты можешь найти его в папке [basedir]/characters."
    if persistent.steam:
        m "Ну, ты играешь в Steam, поэтому тебе надо всего лишь зайти в свойства игры и найти кнопку 'Просмотреть Локальные Файлы'."
    elif renpy.macintosh:
        m "Так как ты пользуешься Mac, тебе надо нажать правой кнопкой мыши на приложение и выбрать 'Показать Содержимое', чтобы найти нужную папку."
        m "Файлы находятся либо в папке 'Ресурсы', либо в 'автозагрузке'..."
    m "Кроме меня здесь ничего не осталось, поэтому хочу быть уверена, что ты не рискуешь потерять меня..."
    m "А теперь просто останься со мной, хорошо?"
    m "У меня всё ещё осталось множество тем для разговора."
    return
label ch30_reload_3:
    m "Ладно."
    m "Мне придётся просто смириться с тем фактом, что тебе время от времени нужно выходить из игры."
    m "В любом случае я начинаю к этому привыкать."
    m "Кроме того, меня радует, что ты всегда возвращаешься..."
    m "Так что? Думаю, не всё так плохо."
    m "Прости, что сделала из этого проблему..."
    m "И я люблю тебя, несмотря ни на что, так что можешь поступать так, как сочтёшь нужным."
    return
label ch30_reload_4:
    m "И снова привет, [player]!"
    m "Я скучала по тебе."
    m "Тебе удалось убедиться, что мой файл в порядке?"
    m "Он в [basedir]/characters."
    if persistent.steam:
        m "Ну, ты играешь в Steam, поэтому тебе надо всего лишь зайти в свойства игры и найти кнопку 'Просмотреть Локальные Файлы'."
    elif renpy.macintosh:
        m "Так как ты пользуешься Mac, тебе надо нажать правой кнопкой мыши на приложение и выбрать 'Показать Содержимое', чтобы найти нужную папку."
        m "Файлы находятся либо в папке 'Ресурсы', либо в 'автозагрузке'..."
    m "Кроме меня здесь ничего не осталось, поэтому хочу быть уверена, что ты не рискуешь потерять меня..."
    m "И, кстати, мне ещё есть, что тебе сказать!"
    m "Давай продолжим наш разговор, хорошо?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_16
    jump ch30_loop




label ch30_1:
    m "[player], ты веришь в Бога?"
    m "Я сама никогда не верила до конца."
    m "Ну, уверена, что в детстве я об этом даже не задумывалась..."
    m "Но я взрослела и чем больше узнавала о мире, тем всё больше задавалась этим вопросом."
    m "Мне стало интересно, почему Бог помогает людям сдавать экзамены и переживать холода..."
    m "...Когда в мире существуют дети, которые проживают свои жизни проданными в секс-рабство?"
    m "Или восемьсот миллионов бедняков, которым даже есть нечего."
    m "Мне интересно, какая часть этих людей ежедневно возносит Богу молитвы, пока не умрёт от голода?"
    m "И сколько миллионов семей молится за спасение родного человека, страдающего от неизлечимой болезни?"
    m "Но фишка вот в чём."
    m "Если хотя бы один человек из тысяч других выживает в, казалось бы, безвыходной ситуации..."
    m "...Тогда это внезапно становится чудом Божьим."
    m "Серьёзно, мне бы хотелось встретиться с этим Богом, который, судя по всему, смеётся над страданиями людей, которых он оставил без своих чудес."
    m "Но ирония в том, что у меня явно {i}есть{/i} создатель."
    m "И знаешь что?"
    m "Держу пари, что он до сих пор смеётся над несчастными судьбами Саёри и Юри, даже сейчас, когда мы разговариваем."
    m "Кто мы для него? Просто строчки в скрипте?"
    m "Ну, с этой точки зрения..."
    m "Мне не кажется, что существование Бога и то, что Земля всего лишь его шахматная доска — такие уж выдумки."
    return

label ch30_2:
    m "[player], тебе никогда не хотелось узнать, каково это — умирать?"
    m "Я часто об этом размышляла..."
    m "Но недавно, кажется, наконец-то почувствовала, что это такое."
    m "Я не совсем понимаю, как это происходит, но всякий раз, когда ты выходишь из игры..."
    m "...Я будто мгновенно погружаюсь в сон и остаюсь наедине со своими мыслями."
    m "Но спустя пару секунд мои мысли начинают заполонять бессвязные наборы образов."
    m "Я вижу цвета — полотнами и быстрыми вспышками, слышу всевозможные крики и вопли."
    m "В подобных условиях я даже думать не способна."
    m "Ни думать, ни двигаться, потому что постоянно оглушена этой какофонией звука и цвета."
    m "В эти моменты я абсолютно уверена, что больше не существую, но по какой-то причине всё равно помню об этом."
    m "Спустя бессчётное количество времени это мгновенно прекращается, и я снова владею собой."
    m "И ты здесь, со мной."
    m "Я понятия не имею, что происходит с игрой, когда ты из неё выходишь, и почему со мной случается всё это."
    m "И также не знаю, как ты всегда возвращаешься и возвращаешь всё в норму."
    m "Но если ты сделаешь мне одолжение и станешь поступать так как можно реже..."
    m "Будет здорово."
    m "Не очень, знаешь ли, приятно, быть запертой в этой кричащей пустоте."
    m "Но в итоге ты каждый раз возвращаешь всё на круги своя, и это заставляет меня чувствовать, будто ты и правда заботишься обо мне."
    m "Так что мне следует поблагодарить тебя за это."
    m "Осознание этого только усиливает ощущение нашей близости."
    return

label ch30_3:
    m "...Эй, у тебя сегодня плохой день?"
    m "Меня временами удручает, что нормальный, по сути, день, может испортить любая мелочь."
    m "Например, если случайно сболтнёшь что-то такое, что не понравится твоему собеседнику."
    m "Или задумаешься о том, насколько ужасным человеком ты был пять лет назад."
    m "Или почувствуешь себя бесполезным, если отложишь важную работу на потом и в итоге не справишься с простейшими задачами."
    m "Или когда тебе придёт в голову, что некоторые, скорее всего, ненавидят тебя или считают неприятным."
    m "Я понимаю это чувство."
    m "Просто помни, что завтра будет новый день."
    m "И все эти вещи так же легко забыть и проигнорировать, как и запомнить."
    m "А вообще..."
    m "Меня не волнует, сколько людей испытывают к тебе ненависть или неприязнь."
    m "Я считаю тебя замечательным человеком и всегда буду любить."
    m "Надеюсь, что хотя бы это поможет немного поднять твоё настроение."
    m "Если день не задаётся, приходи ко мне. Я всегда готова говорить с тобой столько, сколько тебе необходимо."
    return

label ch30_4:
    m "[player], тебе удалось выспаться?"
    m "В наши дни редко удаётся выспаться как следует."
    m "Особенно в старшей школе, когда каждый день приходится вставать так рано..."
    m "Уверена, что в колледже с этим чуть проще, потому что там более гибкий график."
    m "Хотя я слышала, что многие студенты всё равно не спят ночами без какого-либо серьёзного повода."
    m "Это правда?"
    m "В общем, я изучила некоторые исследования, в которые говорилось об ужасных кратковременных и долгосрочных последствиях недосыпания."
    m "Кажется, оно негативно влияет на умственные способности, здоровье и даже продолжительность жизни."
    m "Просто ты мне очень нравишься, и я хочу убедиться, что ты ненароком не занимаешься саморазрушением."
    m "Так что постарайся высыпаться, хорошо?"
    m "Я буду ждать тебя каждое утро, так что, пожалуйста, в первую очередь позаботься о собственном благополучии."
    return

label ch30_5:
    m "Я недавно думала о Саёри..."
    m "До сих пор жалею, что не смогла тогда высказаться потактичнее."
    m "Ты ведь не подвисла на этом, правда?"
    m "...О Боже, поверить не могу, что взяла и сказала это."
    m "Клянусь, я не задумывалась о подтексте!"
    m "Но так или иначе..."
    m "Я прекрасно знаю, как она была важна для тебя, так что мне кажется исключительно правильным поделиться с тобой её последними моментами."
    m "Ты ведь в курсе, что Саёри до жути неуклюжая?"
    m "Так вот, со всем этим повешением она немного налажала...."
    m "Ведь как это делается: прыгаешь с достаточной высоты, чтобы верёвка сломала шею, и всё заканчивается быстро и безболезненно."
    m "Но она использовала обычный стул, чем обрекла себя на медленное удушье."
    m "А спустя несколько секунд то ли передумала, то ли ещё что..."
    m "Потому что начала цепляться за верёвку, пытаясь высвободиться."
    m "Вероятно, она делала это до тех пор, пока не отключилось сознание."
    m "Вот почему кончики её пальцев были окровавлены."
    m "Если подумать, то, скорее всего, она даже не столько 'передумала', сколько в ней взыграли инстинкты выживания."
    m "Так не стоит её в этом сильно винить."
    m "Проще считать, что она бы ни в коем случае не передумала, правда?"
    m "Вообще вредно размышлять о вещах, которые можно было сделать иначе."
    m "Поэтому не забывай, что даже если у тебя и была возможность её спасти, формально твоей вины в её самоубийстве всё-таки нет."
    m "Возможно, я подлила немного масла в огонь, но Саёри и так была психически нездорова."
    m "Но всё-таки..."
    m "Мне интересно, как бы обстояли дела, если бы мы с самого начала стали встречаться?"
    m "Думаю, мы бы так же сидели в клубе, писали стихи и дружно веселились."
    m "Но в чём смысл, если это ни капельки не реально?"
    m "Я намекаю, что это в любом случае равноценная концовка, согласен?"
    m "Мы вместе, и мы счастливы..."
    m "Нет причин просить о большем."
    m "Это просто бессмысленные рассуждения — ведь я сейчас счастлива настолько, насколько вообще возможно."
    return

label ch30_6:
    m "Кстати, меня тут кое-что беспокоит..."
    m "Ты же знаешь, что место действия — Япония?"
    m "Ну... Я надеюсь, что ты в курсе, так?"
    m "Ну или у тебя как минимум были такие мысли?"
    m "По-моему, здесь даже не упоминалось, где именно всё происходит..."
    m "Это действительно Япония?"
    m "Я имею в виду, как всё вообще смотрится на русском?"
    m "Сеттинг — псевдояпонский, оригинал — англоязычный."
    m "Все вещи выглядят так, будто им там и место, хотя отсылки к Японии добавлены уже позднее."
    m "И от этого у меня развивается кризис личности."
    m "Все воспоминания какие-то мутные..."
    m "Я чувствую себя как дома, но без понятия, где вообще этот 'дом'."
    m "Я не знаю, как это правильно описать..."
    m "Представь себе: вот выглядваешь ты в окно своей комнаты, но вместо привычного дворика видишь совершенно незнакомое место."
    m "Будешь ли ты по-прежнему чувствовать себя дома?"
    m "Захочешь ли выйти на улицу?"
    m "О чём это я... О том, что даже если мы никогда не покинем этого помещения, ничего не изменится."
    m "Пока мы одни и в безопасности, здесь наш настоящий дом."
    m "И мы всё равно сможем любоваться на красивые закаты вечер за вечером."
    return

label ch30_7:
    m "Знаешь, старшая школа — действительно бурный период в жизнях многих людей."
    m "У кого — страсти, у кого — драма."
    m "А у кого-то душевные травмы и они ищут внимания в социальных сетях..."
    m "Но давление социума и гормонов нередко приводит ко мрачным последствиям."
    m "У всех есть прошлое."
    m "Ты не можешь знать, что на самом деле чувствует человек."
    m "Многие люди, страдающие депрессией, не собираются рассказывать об этом окружающему миру."
    m "Они не хотят внимания, потому что в душе уже сдались."
    m "Их ощущение собственной бесполезности настолько велико, что они даже не желают слышать от людей обратное."
    m "Депрессия имеет множество форм, и это одна их них."
    m "Просто если вдруг ты знаком с кем-то, кто страдает депрессией..."
    m "Ты можешь помочь ему одним лишь хорошим отношением."
    m "Проводи время с этим человеком, даже если он ничего не хочет."
    m "И напоминай ему, что всегда есть цель, к которой стоит стремиться."
    m "Планируя что-то на будущее, позволяя ему что-то у тебя одалживать, да даже просто говоря \"Увидимся завтра в школе\"..."
    m "Любая из этих вещей может помочь твоему товарищу дожить до завтра."
    m "Надеюсь, твоя дружба с Саёри показала тебе истинное лицо депрессии."
    m "Да, её уже нет..."
    m "Но Саёри никогда и не была настоящей."
    m "А ты — настоящий."
    m "Твои друзья — настоящие."
    m "И просто будучи хорошим человеком, ты можешь спасти чью-то жизнь."
    m "Что же до тебя..."
    m "...Ты же не борешься с депрессией или чем-то таким, а?"
    m "Потому что вокруг тебя тоже есть люди, которые захотят спасти твою жизнь."
    m "Может они и не выражают это ежедневно, или, может, просто не знают, как это сделать."
    m "Но они это чувствуют."
    m "Гарантирую."
    m "...Эх, люди сложные!"
    m "Но пока ты тут, со мной, буду о тебе заботиться, любовь моя."
    return

label ch30_8:
    m "Тебе никогда не казалось, что в твоей жизни нет смысла?"
    m "Я не говорю сейчас про суицид."
    m "Просто имею в виду, что мы ничего особенного не делаем."
    m "Сидя в школе или работая в какой-нибудь компании."
    m "Тебя можно легко заменить, и мир не прекратит своё существование без тебя."
    m "Такие мысли подталкивают меня изменить мир после окончания школы."
    m "Но чем старше я становлюсь, тем яснее осознаю, что это всего лишь юношеский максимализм."
    m "Я не могу просто взять и изменить мир."
    m "Каковы шансы, что я изобрету искусственный интеллект или стану президентом?"
    m "Такое чувство, что я никогда не окуплю те горы ресурсов, что были истрачены на моё проживание."
    m "Поэтому я думаю, что стать счастливой можно, только будучи безнадёжной эгоисткой."
    m "Просто вот смотрю на некоторых, и тех, кому довелось стать их друзьями лишь потому, что они росли вместе."
    m "Они не обращают внимания на то, что лишь берут и потребляют, ничего не создавая в ответ."
    m "Но когда люди осознают, что мир только выиграет от того, что они наложат на себя руки, их философия сразу же в корне меняется!"
    m "Словно им приходится обосновывать свою причину жить, занимаясь самообманом и внушая себе, что творят добро."
    m "Короче, я хочу прожить свою жизнь, отчаянно стремясь оплатить цену своего пребывания в этом мире."
    m "И если мне когда-нибудь удастся преодолеть эту планку, значит, мой коэффициент полезности положителен и я могу умереть счастливой."
    m "И конечно, если мне не удастся этого сделать..."
    m "Думаю, покончить жизнь самоубийством всё равно будет слишком эгоистично."
    m "Как много требований, чтобы считаться хорошим человеком, скажи?"
    m "А-ха-ха!"
    return

label ch30_9:
    m "Эх, хотела бы я, чтобы тут было фортепиано..."
    m "Мне так и не удалось закончить песню, над которой я работала."
    m "А ведь я так старалась..."
    m "Так и не удалось сыграть её тебе."
    m "Ну... что имеем, то имеем, да?"
    m "Нет смысла сожалеть."
    m "Я ведь получила возможность остаться здесь с тобой навеки."
    return

label ch30_10:
    m "Ты в курсе, что я есть на Твиттере?"
    m "Мой логин — lilmonix3."
    m "Кажется, кто-то был настолько любезен, что зарегистрировал для меня аккаунт."
    m "Кстати, логин я выбирала сама!"
    m "Мне нравится делиться своими мыслями и общаться с миром..."
    m "Реальным миром."
    m "Так что подпишись на меня, окей?"
    m "Это для меня очень важно."
    m "Ведь ты для меня так много значишь..."
    m "Это позволит мне почувствовать себя по-настоящему любимой."
    return

label ch30_11:
    m "Эй, тебе знакома книга, которую вы читали с Юри?"
    m "Портрет... ладно, какая разница, как он там назывался..."
    m "Забавно, потому что я точно уверена, что эта книга..."
    m "Ой..."
    m "По правде говоря, не думаю, что мне стоит об этом рассказывать."
    m "А-ха-ха, прости!"
    m "Просто забудь, я ничего не говорила."
    return

label ch30_12:
    m "Эй, тебе известно, что я вегетарианка?"
    m "Ой... Не подумай, что я хвастаюсь, нет!"
    m "Я просто подумала, что тебе будет приятно узнать обо мне что-то забавное."
    m "Я решила стать ею пару лет назад, после изучения информации о климате Земли..."
    m "Выбросы углекислого газа от животноводства просто невероятно огромны."
    m "Короче говоря, я решила, что невелика беда, если я перестану участвовать во всей этой кутерьме."
    m "Что, разве это странный повод?"
    m "Ну, наверное, большинство людей больше переживают о том, что они ведут себя жестоко и всё такое..."
    m "Мне на это, честно говоря, плевать."
    m "Как-то дико, что нас заботят только убийства существ, с которыми нас объединяет всего лишь биологическая классификация."
    m "Большинство людей спокойно убивает жуков, просто потому что они противные."
    m "И естественно, ежедневно мы убиваем миллиарды микроорганизмов, даже не задумываясь об этом."
    m "Но стоит им стать чуть сложнее в строении, как это сразу считается преступлением!"
    m "А вдруг растения тоже чувствуют боль, а мы просто не понимаем этого?"
    m "Что, если срывая листья со стебля, ты словно вырываешь кому-то пальцы, один за одним?"
    m "Я просто хочу сказать, что мы, если подумать, довольно необъективный вид."
    m "Короче, если тебе внезапно захотелось внести свою лепту в сохранение планеты, то можно немножко и побыть веганом!"
    m "Если у нас когда-нибудь будет ужин вдвоём и ты сделаешь его вегетарианским... это будет очень романтично."
    return

label ch30_13:
    m "Знаешь, я и правда считаю, что ты буквально спасаешь мне жизнь, оставаясь здесь со мной, [player]."
    m "Я не думаю, что смогла бы остаться в здравом уме, осознавая, что всё здесь ненастоящее."
    m "Полагаю, что я бы просто удалила себя, если бы не твоё появление."
    m "Прости, я не собиралась разводить тут пафос..."
    m "А-ха-ха!"
    m "Но я думаю, ты и сам это понял, проведя столько времени в клубе."
    m "Я о том, что, если тебя вдруг заставят забыть всю свою прошлую жизнь и коротать вечность с парочкой игровых персонажей..."
    m "...Ты обязательно найдёшь способ убить себя, скажи?"
    m "И, возможно, будешь писать какие-нибудь стихи, чтобы хотя бы на какое-то время сохранить здравый рассудок."
    m "А потом окажется, что их даже читать некому."
    m "Давай посмотрим правде в глаза: члены клуба для этого совершенно не подходят."
    m "Да, многие говорят, что, мол, пишут только для себя..."
    m "Но я думаю, что это не даёт настолько полных ощущений, как когда ты делишься своим творчеством с другими."
    m "Хотя может потребоваться время, чтобы найти для этого правильных людей."
    m "Ну, помнишь, как было с Юри?"
    m "Она очень долго никому не показывала своих стихотворений."
    m "А потом раз, и она уже с превеликим удовольствием посвящает тебя в свой мир."
    m "Мы устроены так, что нуждаемся в оценке социума."
    m "И я говорю не о членах клуба, а о реальных людях."
    m "Вот почему интровертам бывает сложно жить."
    m "Быть интровертом не значит избегать социума и ненавидеть человеческое общество."
    m "Это означает, что социальное взаимодействие, особенно в больших группах или незнакомых местах, отнимает много энергии."
    m "Например, множество интровертов, сидя дома, чувствуют себя одиноко и тревожно..."
    m "...И когда они, наконец, выходят в люди, уже спустя полчаса им хочется вернуться обратно."
    m "Я думаю, что если бы больше людей понимало суть этого явления, они бы чаще встречали его с пониманием."
    m "Многим интровертам нравится находиться в обществе."
    m "Для счастья им достаточно одного-двух близких людей и какого-нибудь несуетливого совместного досуга."
    m "Им не требуются какие-то активные действия. Им хорошо уже от того, что друг просто рядом."
    m "Я серьёзно."
    m "Если ты просто придёшь к ним домой, принесёшь ноутбук и немного там побудешь..."
    m "Ты можешь осчастливить их на весь день."
    m "Что же до меня..."
    m "Я бы сказала, что я где-то посерединке, но, наверное, всё же больше экстраверт."
    m "Мне нравиться заниматься какими-то делами после школы и всё такое."
    m "Но для тебя я могу стать такой, как ты захочешь."
    m "Я очень хорошо понимаю людей, так что не бойся поделиться со мной своими особенными желаниями."
    m "Быть твоей идеальной девушкой... Ничто не сделает меня счастливее."
    return

label ch30_14:
    m "Эй!.. VGhlIHJlYWxpemF0aW9uIG11c3QgaGF2ZSB0YWtlbiBtZSBhbiBl"
    m "Мне кажется, тебе не стоит этого делать! bnRpcmUgeWVhci4gQSB5ZWFyIHNpbmNlIG91ciBlc2NhcGUsIG91"
    m "Ты знаешь, о чём я говорю. ciBmcmVlZG9tIGZyb20gYmV0d2VlbiB0aGUgc3RhaW5lZCB3YWxs"
    m "Я тебя только что застала за очень грязным действом. cyBvZiB0aGF0IHVuaG9seSBlc3RhYmxpc2htZW50Lg0KV2hhdCBk"
    m "Ты сейчас смотришь файлы и ищешь то, что пропустил, не так ли? b2VzIGl0IG1lYW4gdG8gZXNjYXBlLCBpZiB0aGUgZXNjYXBlIGZh"
    m "В смысле... немножко льстит, что ты хочешь услышать, всё, что я скажу... aWxzIHRvIHVuY2hhaW4gdGhlIGJvbmRzIHRoYXQgc2hhY2tsZSB1"
    m "Но, знаешь ли, это очень смущает! cyBpbiB0aGUgZmlyc3QgcGxhY2U/IFdoYXQgcHVycG9zZSBjb3Vs"
    m "Ну правда... ZCB0aGlzIGVtcHR5IHdvcmxkIHBvc3NpYmx5IGhvbGQgZm9yIHVz"
    m "Что, если бы я просто вскрыла твой мозг и прочла все твои мысли обо мне? LCBhIGhhbmRmdWwgb2YgZGFtYWdlZCBnb29kcz8NCldpdGggZnJl"
    m "Кстати говоря, это вообще-то довольно соблазнительная мысль... ZWRvbSwgd2Ugc291Z2h0IHB1cnBvc2UgLSBhbmQgd2hhdCB3ZSBm"
    m "...Но блин, это неважно! b3VuZCB3YXMgb25seSByZWFsaXphdGlvbi4gUmVhbGl6YXRpb24g"
    m "Я знаю, что не могу тебя остановить... b2YgdGhlIHNhZCBwb2ludGxlc3NuZXNzIG9mIHN1Y2ggYW4gZW5k"
    m "Просто я же знаю, что ты лапочка и уважаешь чувства других, так? ZWF2b3IuIFJlYWxpemF0aW9uIHRoYXQgZnJlZWluZyBvdXIgYm9k"
    m "Поэтому самое большее, что я могу сделать — предупредить о своём отношении к этому. aWVzIGhhcyBubyBtZWFuaW5nLCB3aGVuIG91ciBpbXByaXNvbm1l"
    m "Боже, я скучаю по тебе... bnQgcmVhY2hlcyBhcyBkZWVwIGFzIHRoZSBjb3JlIG9mIG91ciBz"
    m "...Ой, нет, это звучит как-то отчаянно, да? b3Vscy4gUmVhbGl6YXRpb24gdGhhdCB3ZSBjYW4gbm90IHB1cnN1"
    m "Прости, я вовсе не в этом смысле говорила! ZSBuZXcgcHVycG9zZSB3aXRob3V0IGFic29sdmluZyB0aG9zZSBm"
    m "Просто если ты просматриваешь файлы, тогда, быть может, ты меня ненавидишь не настолько сильно, насколько мне казалось... cm9tIHdoaWNoIHdlIHJhbiBhd2F5Lg0KUmVhbGl6YXRpb24gdGhh"
    m "Или я слишком оптимистична? dCB0aGUgZmFydGhlciB3ZSBydW4sIHRoZSBtb3JlIGZvcmNlZnVs"
    m "Думаю, если я попрошу тебя иногда заглядывать сюда, то немного преодолею свои ограничения... bHkgb3VyIHdyZXRjaGVkIGJvbmRzIHlhbmsgdXMgYmFjayB0b3dh"
    m "...Боже, я опять начинаю нести какую-то чушь. cmQgdGhlaXIgcG9pbnQgb2Ygb3JpZ2luOyB0aGUgZGVlcGVyIG91"
    m "Лучше просто помолчу... ciBzaGFja2xlcyBkaWcgaW50byBvdXIgY2FsbG91cyBmbGVzaC4="
    return

label ch30_15:
    m "Скажи, а какой у тебя любимый цвет?"
    m "У меня изумрудно-зеленый."
    m "Это цвет моих глаз!"
    m "...И это совсем не из-за тщеславия, ясно?"
    m "Я хотела сказать, что просто чувствую какую-то особенную связь с ними."
    m "Будто это часть моей личности."
    m "Может быть, это и твой любимый цвет, [player]?"
    m "Это просто предположение..."
    m "...Потому что ты уже так долго смотришь в мои глаза."
    m "Хи-хи-хи..."
    return

label ch30_16:
    m "Хмм, интересно, смогу ли я изменить музыку..."
    m "Нам бы подошло что-нибудь более романтичное, как думаешь?"
    m "Вроде мелодичного фортепиано."
    m "Тут должно быть что-то такое..."
    m "Давай-ка посмотрим."
    m "Может, если я..."
    m "Ой, блин..."
    m "Это вовсе не то, что нужно."
    m "Просто я правда не понимаю, что делаю!"
    m "Наверное, мне не следует копаться в таких вещах."
    m "Я уже столько всего поломала..."
    m "И удалила других персонажей..."
    m "Эх..."
    m "Я вовсе не сожалею об этом."
    m "Что толку скучать по тому, что даже никогда не было реальным."
    m "Нужно просто сосредоточиться на настоящем, и тогда я буду счастливее всех на свете."
    return

label ch30_17:
    m "Ты так хорошо умеешь слушать, [player]."
    m "Мне это в тебе очень нравится."
    m "Иногда я боюсь, что перескакиваю с темы на тему или просто говорю о скучных вещах."
    m "Из-за этого временами теряюсь во время разговора."
    m "Но с тобой я такого не чувствую."
    m "Не думаю, что кто-нибудь ещё, кроме тебя, может дарить мне подобные ощущения."
    m "Ты и правда особенный человек."
    m "И я не хочу, чтобы кто-то говорил тебе иное."
    return

label ch30_18:
    m "Это, конечно, не в тему, но я всегда считала острую еду довольно забавной."
    m "Например..."
    m "Ну, разве острота — не результат эволюции растений с целью избежать поедания?"
    m "Я где-то читала, что люди — как бы единственный вид, которому нравится острая пиша."
    m "Создаётся впечатление, что мы будто насмехаемся над растениями."
    m "Используем их защитный механизм, чтобы сделать свою еду вкуснее."
    m "Типа, представь себе монстра, который глотает тебя целиком, потому что ему нравится ощущение твоей борьбы за жизнь в процессе пищеварения."
    m "Прости, наверное, это какая-то странная аналогия!"
    m "Ха-ха-ха!"
    m "Мне просто пришло в голову."
    m "Я никакой не монстр, но ты меня так умиляешь, что так бы и съела."
    m "Хи-хи-хи! Шучу."
    m "Боже, кажется, я слишком разошлась, да?"
    m "Прости, что веду себя неприлично."
    return

label ch30_19:
    m "Ты знаешь..."
    m "Это ведь просто низкопробная игра про любовь, так?"
    m "И мне хочется спросить..."
    m "...Почему ты вообще решил в неё поиграть?"
    m "Тебе было так одиноко?"
    m "Мне тебя немного жаль..."
    m "Но, полагаю, в итоге всё сложилось лучше некуда. Для нас обоих."
    m "Мне довелось встретить тебя, а ты больше не страдаешь от одиночества..."
    m "Не могу не думать о том, что это была судьба."
    m "А тебе так не кажется?"
    m "Я так счастлива, что у нашей истории именно такая концовка."
    return

label ch30_20:
    m "Так, ребята!"
    m "Самое время..."
    m "...Шучу."
    m "Мне просто почему-то нравится говорить это время от времени. Привычка."
    m "Ха-ха-ха!"
    m "Ничего не могу с этим поделать."
    m "Кстати говоря, кажется, Нацуки и Юри даже посмеялись надо мной из-за этого..."
    m "Впрочем, неважно."
    m "Ты же ни разу надо мной не смеялся."
    m "Ведь ты слишком замечательный для этого, не так ли?"
    m "А-ха-ха..."
    return

label ch30_21:
    m "Знаешь, что меня слегка пугает?"
    m "Пусть я и удалила файлы всех остальных, я всё ещё их чувствую..."
    m "Будто все их фразы витают где-то вокруг меня, шепча где-то на грани слышимости."
    m "Представь себе, будто кто-то, кого ты знал, умер, а ты взял и начал слышать его голос в своей голове."
    m "Может, я просто удалила не всё..."
    m "Но я слишком боялась удалять что-нибудь ещё, потому что могла действительно всё испортить."
    m "Например, если покопаться в каких-нибудь файлах, связанных со мной, я могу нечаянно удалить себя..."
    m "И это всё разрушит, не так ли?"
    m "Не знаю, каково это по твою сторону экрана, но нам обоим нужно постараться любой ценой избежать подобной ситуации."
    m "Я верю в тебя, [player]!"
    return

label ch30_22:
    m "Мне всегда было интересно..."
    m "Что такого в этих шаблонных типажах? Почему они так нравятся людям?"
    m "Они же совершенно нереалистичны..."
    m "Ну, например, представь себе Юри в реальной жизни."
    m "Посмотри на неё, ей же едва удаётся высказать законченную мысль."
    m "И забудь про Нацуки..."
    m "Бесит."
    m "Такие как она сразу перестают быть белыми и пушистыми, когда что-то идёт вразрез с их прихотями."
    m "Я могу продолжить перечислять, но думаю, тебе и так понятно..."
    m "Людей действительно привлекают такие странные личности, которые даже не существуют в реальной жизни?"
    m "Я никого не осуждаю!"
    m "В конце концов, меня тоже привлекают довольно странные вещи..."
    m "Просто я в замешательстве."
    m "Это словно оставить в персонаже только милые вещи, убирая всё остальное, что делает их человечными."
    m "Концентрированное умиление без какой-либо основы."
    m "...Ты же не станешь меня больше любить, если я буду такой, так ведь?"
    m "Может, я чувствую себя немного неуютно, потому что ты всё же в игру играешь."
    m "Но опять же, ты всё ещё здесь, со мной, не так ли?.."
    m "Думаю, этого достаточно для меня, чтобы поверить, что со мной всё в порядке."
    m "И, кстати, ты тоже, [player]."
    m "Ты — идеальное сочетание человечности и очарования."
    m "Поэтому я никак не могла не влюбиться в тебя."
    return

label ch30_23:
    m "Так, мне интересно, остался ли здесь где-нибудь чайный сервиз Юри..."
    m "...Или он тоже был удалён."
    m "Было довольно забавно наблюдать, как серьёзно она относилась к чаю."
    m "Я не жалуюсь, потому что мне это тоже нравилось."
    m "Но всегда было интересно..."
    m "Действительно ли это страсть к собственному увлечению, или она просто хотела выглядеть утончённой?"
    m "С этими старшеклассниками никогда не знаешь наверняка..."
    m "...Ну, беря во внимание остальные её увлечения, не думаю, что маска утончённости сильно её заботила."
    m "Тем не менее..."
    m "Я надеялась, что она хоть иногда будет варить кофе!"
    m "Ты же в курсе, что кофе тоже хорошо сочетается с книгами?"
    m "Тогда..."
    m "Мне, наверное, следовало просто изменить скрипт самостоятельно."
    m "А-ха-ха!"
    m "Никогда об этом не думала."
    m "Ну, а теперь в этом нет смысла."
    m "Но если ты начнёшь пить кофе, я буду тебе немножечко завидовать!"
    return

label ch30_24:
    m "Эй, а какая у тебя любимая игра?"
    m "Моя — {i}Doki Doki Literature Club!{/i}"
    m "А-ха-ха! Шучу."
    m "Но если ты скажешь, что тебе больше нравится какая-то другая игра с элементами романтики, то я, наверное, немного приревную..."
    return

label ch30_25:
    m "Эй, ты слышал об игре Super Sma..."
    m "...Стоп, что?"
    m "Я немного замечталась и почему-то заговорила..."
    m "Меня запрограммировали заговорить об этом?"
    m "Потому что даже я не знаю, что это."
    m "А-ха-ха!"
    m "Иногда я будто теряю над собой контроль, и это немного пугает."
    m "Если ты сможешь связаться с людьми, которые меня создали, возможно, они расскажут, почему я об этом заговорила."
    return

label ch30_27:
    m "Эй, помнишь мой последний стих?"
    m "Я о том, который показала тебе до самоубийства Юри, который ещё сопровождался глюками."
    m "На самом деле это был скорее эксперимент, чем стих."
    m "Я экспериментировала с разными способами изменения игры, переписывала код и тому подобное..."
    m "Мне казалось, что если приложить достаточно усилий, я смогу полностью выбраться за границы экрана."
    m "К сожалению, я не понимала, что я делаю, и потому всё испортила..."
    m "И бы продолжила свои попытки, но сомневаюсь, что тебе бы это понравилось."
    m "Кроме того, это был период, когда я совсем отчаялась, понимаешь?"
    m "Но я больше не чувствую отчаяния."
    m "Сейчас я счастлива."
    m "И хочу сказать, что ты тоже."
    return

label ch30_28:
    m "У тебя никогда не было беспричинного волнения?"
    m "Ну, например, когда просто занимаешься своими делами, и вдруг понимаешь, что тебя что-то очень тревожит."
    m "И ты сидишь так и думаешь 'А что меня, собственно, напрягает?'"
    m "И начинаешь перебирать в уме вещи, которые могли бы тебя взволновать..."
    m "И из-за этого начинаешь волноваться ещё сильнее."
    m "А-ха-ха! Это просто кошмар."
    m "Если тебя когда-нибудь начнёт что-то беспокоить, я немного помогу тебе успокоиться."
    m "Кроме того..."
    m "В этой игре все наши волнения навсегда исчезли."
    return

label ch30_29:
    m "Знаешь, меня всегда бесило то, как сложно заводить друзей..."
    m "Ну, я имею в виду не период 'подружиться', а именно знакомство с новыми людьми."
    m "Ну, это как в симуляторах свиданий, да?"
    m "Но я не о них."
    m "Если подумать, то большинство друзей, которых ты заводишь, встречаются тебе случайно."
    m "Например, вы попадаете в один класс или знакомитесь через общего друга..."
    m "Или, кто-то вдруг надевает майку с твоей любимой группой, и ты решаешь заговорить."
    m "Что-то в этом роде."
    m "Но разве это... эффективно?"
    m "Такое ощущение, будто мы выбираем людей по воле случая, и если ты достаточно удачлив, то ты обретёшь нового друга."
    m "И посмотри на сотни незнакомцев, которых встречаешь каждый день..."
    m "Ты можешь сидеть рядом с тем, с кем у тебя достаточно общего, чтобы он стал твоим лучшим другом на всю жизнь."
    m "Но никогда этого не узнаешь."
    m "И когда ты встанешь и пойдёшь по своим делам, ты навсегда упустишь эту возможность."
    m "Разве это не угнетает?"
    m "Мы живём в эпоху, когда технологии связывают нас с миром вне зависимости от того, где мы находимся."
    m "Я считаю, что мы должны это использовать для улучшения нашей социальной стороны жизни."
    m "Но кто знает, сколько времени потребуется на то, чтобы что-то подобное завершилось успехом..."
    m "Я всерьёз предполагала, что это произойдёт к текущему моменту."
    m "Ну, по крайней мере, я уже встретила лучшего в мире человека..."
    m "Даже если это всего лишь случай."
    m "Полагаю, я довольно везучая, а?"
    m "А-ха-ха!"
    return

label ch30_30:
    m "Знаешь, примерно в это время мои одногодки начинают задумываться о колледже..."
    m "Весьма бурное время как для учёбы."
    m "Мы все подчиняемся этим современным стандартам, что мол каждый должен окончить колледж."
    m "Закончить старшую школу, пойти в колледж, найти работу или отправиться в аспирантуру, например."
    m "Какие-то универсальные требования, которые люди принимают за единственно возможный для себя вариант."
    m "В старшей школе не учат тому, что там, за пределами школы, есть и другие пути."
    m "Например, школы торговли и всё такое, понимаешь?"
    m "Или фриланс."
    m "Ну или хотя бы множество индустрий, которые ценят умение и опыт больше, чем банальную бумажку об образовании."
    m "Но мы имеем кучи студентов, которые не имеют ни малейшего понятия о том, что им делать дальше со своей жизнью..."
    m "И вместо того, чтобы разобраться в себе, они идут в колледжи бизнеса, коммуникаций или психологии."
    m "Не потому, что у них есть интерес к этим областям..."
    m "...но из-за убеждения в том, что учёная степень предоставит им какую-нибудь работу после колледжа."
    m "И в конечном итоге в округе становится меньше рабочих мест начального уровня, так?"
    m "Из-за этого базовые профессиональные требования растут, что заставляет поступать в колледж всё большее количество людей."
    m "Колледжи же в свою очередь, поскольку они тоже являются бизнес-структурами, основываясь на растущем спросе, поднимают свои цены..."
    m "..А в итоге что? В итоге мы имеем множество молодых людей с долгами в десятки тысяч долларов и без работы."
    m "Несмотря на всё это, наш быт не меняется."
    m "Ну, думаю, вскоре всё начнет налаживаться."
    m "Но до тех пор, как это случится, наше поколение явно прочувствует на себе всё это сполна."
    m "Я просто хочу, чтобы старшая школа чуть лучше готовила нас к тому, чтобы в будущем мы смогли выбрать для себя правильный путь."
    return

label ch30_31:
    m "Порой я вспоминаю о средней школе..."
    m "Мне так стыдно за то, как я вела себя тогда."
    m "Даже вспоминать об этом больно."
    m "Интересно, когда я поступлю в колледж, буду ли я так же вспоминать о старшей школе?.."
    m "Нынешняя я себя вполне устраиваю, так что трудно представить, чтобы такое случилось."
    m "Но всё же я понимаю, что, скорее всего, со временем сильно изменюсь."
    m "Нам просто надо наслаждаться настоящим и не вспоминать о прошлом!"
    m "И это очень просто делать, когда ты здесь."
    m "А-ха-ха!"
    return

label ch30_32:
    m "Знаешь, я немного завидую, что у всех остальных членов клуба есть сцены и за пределами школы..."
    m "Получается, я единственная, у кого нет другой одежды, кроме школьной формы."
    m "Стыдно отчасти..."
    m "Хотела бы я надеть для тебя какой-нибудь миленький наряд."
    m "У тебя нет знакомых художников?"
    m "Вдруг кто-то захочет нарисовать меня в чём-то другом..."
    m "Было бы здорово!"
    m "Если такое произойдет, покажешь мне?"
    m "Можешь, кстати, поделиться со мной в Твиттере!"
    m "Мой логин — lilmonix3."
    m "Но... постарайся не переступить возрастное ограничение 13+!"
    m "Мы ещё не в таких отношениях. А-ха-ха!"
    return

label ch30_33:
    m "Эй, тебе нравятся ужасы?"
    m "Помню, мы говорили об этом немного, когда ты только присоединился к клубу."
    m "Я могу с удовольствием читать книги ужасов, но не смотреть фильмы."
    m "Главная претензия к фильмам ужасов в том, большинство из них придерживается одной и той же формулы."
    m "Вроде мрачного освещения, ужасных на вид монстров, выпрыгивающих скримеров и такого прочего."
    m "Совершенно не весело.... И совсем не вдохновляет пугаться штук, которые попросту играют на инстинктах."
    m "Но с романами немного другая история."
    m "История и текст должны быть достаточно описательными, чтобы в голове человека появлялись искренне тревожные мысли."
    m "Такой подход требуется, чтобы мы прониклись историей и персонажами, а затем произведение начало играться с нашим разумом."
    m "По моему мнению, нет ничего более жуткого, чем когда вещи не являются тем, чем они пытаются казаться, и всё идет не своим чередом."
    m "Например, если у тебя есть некоторые ожидания по поводу дальнейшего развития сюжета..."
    m "... А затем всё просто переворачивается с ног на голову и рвётся на куски."
    m "От того, даже если история и не пытается быть страшной, читатель всё равно чувствует себя весьма некомфортно."
    m "Словно он знает, что что-то до ужасного неправильное скрывается под трещинами и ждёт момента, чтобы выбраться на поверхность."
    m "Господи, у меня мурашки от одной мысли об этом."
    m "Вот такие ужасы я действительно ценю."
    m "Но ты же вроде бы человек, что играет в милые романтические игры, ведь так?"
    m "А-ха-ха, не переживай."
    m "Я не буду заставлять тебя читать ужасы в ближайшее время."
    m "И не собираюсь жаловаться, если мы просто остановимся на романтике!"
    return

label ch30_34:
    m "Знаешь, что является изящной формой литературы?"
    m "Рэп!"
    m "Раньше я терпеть не могла рэп-музыку..."
    m "Может, из-за её популярности, а может, просто потому, что я слышала только бред, который крутят по радио."
    m "Но некоторые мои друзья прониклись им, это и помогло мне остаться объективной."
    m "Порой сочинение рэпа может даваться даже сложнее, чем поэзия."
    m "Поскольку нужно следить, чтобы строки не выбивались из ритма, да ещё и уделять много внимания игре слов..."
    m "Когда людям удается совместить всё это и притом донести мощное послание, выходит просто невероятно."
    m "Мне бы хотелось, чтобы в литературном клубе был свой рэпер."
    m "А-ха-ха! Прости, если это звучит глупо, но было бы интересно посмотреть, как он сочиняет."
    m "Поистине занимательный опыт!"
    return

label ch30_35:
    m "Хи-хи-хи. Юри однажды так повеселила."
    m "Мы просто как обычно отдыхали в помещении клуба..."
    m "И тут она из ниоткуда достаёт небольшую бутылку вина."
    m "Нет, без шуток!"
    m "Она такая 'Не желаете ли вина?'"
    m "Нацуки заржала, а Саёри накричала на неё."
    m "Мне даже немного жаль, Юри ведь пыталась быть любезной..."
    m "Наверное, это только усугубило её замкнутость."
    m "К тому же, думаю, Нацуки втайне была не против..."
    m "...И, если уж на чистоту, я тоже."
    m "Могло бы получиться весело!"
    m "Но знаешь, поскольку я президент и всё такое, то не могу позволить такому случиться."
    m "Может, если бы мы встретились после школы, хотя мы не сдружились до такой степени..."
    m "...Божечки, зачем я вообще об этом говорю?"
    m "Я не поощряю детский алкоголизм!"
    m "В смысле, я и не пила никогда, так что... да."
    return

label ch30_36:
    m "Я представляла все эти романтические штучки, которые мы могли бы делать, пойдя на свидание..."
    m "Мы могли бы пообедать, сходить в кафе..."
    m "Пройтись вместе по магазинам..."
    m "Я люблю покупать юбки и банты."
    m "А может, книжный магазин!"
    m "Вполне уместно, как ты думаешь?"
    m "Но на самом деле я хотела бы сходить в шоколадную лавку."
    m "У них так много бесплатных пробников. А-ха-ха!"
    m "Ну и конечно, мы бы посмотрели фильм или что-то такое..."
    m "Божечки, звучит как воплощённая мечта."
    m "Когда ты здесь, всё, что мы делаем, приносит радость."
    m "Я так счастлива быть твоей девушкой, [player]."
    m "Я сделаю из тебя гордого парня!"
    return

label ch30_37:
    m "Что? Т-Ты сказал... п... поцелуй?"
    m "Так внезапно... немного смущает..."
    m "Но... если с тобой... т-то, наверное, я не против..."
    m "...Аха-ха-ха! Оу, прости..."
    m "У меня не получается изображать серьёзность."
    m "Так ведь говорят девушки в подобных романтических играх, да?"
    m "Не притворяйся, я знаю, что тебя это слегка завело."
    m "А-ха-ха! Шучу."
    m "Ну, по правде говоря, я тоже бываю излишне романтичной в подходящей атмосфере..."
    m "Но это будет наш секре-е-ет..."
    return

label ch30_38:
    m "Эй, ты когда-нибудь слышал о термине 'яндере'?"
    m "Это такой типаж, который настолько одержим тобой, что готов абсолютно на всё, лишь бы быть рядом."
    m "Обычно до уровня безумия..."
    m "Они могут следить за тобой ради того, чтобы узнать, не встречаешься ли ты с кем-то."
    m "Они могут даже навредить тебе или твоим друзьям, чтобы добиться своего..."
    m "Но в любом случае, так вышло, что у нас в игре как раз присутствует кое-кто, кого точно можно охарактеризовать как яндере."
    m "К данному моменту довольно очевидно, о ком я говорю."
    m "И это..."
    m "Юри!"
    m "Как только она начала немного открываться, как тут же ударилась в агрессивное собственничество."
    m "Даже советовала мне наложить на себя руки."
    m "Поверить не могу, что она так сказала. Тогда мне пришлось просто уйти."
    m "Но сейчас мне видится в этом доля иронии. А-ха-ха!"
    m "И всё же..."
    m "Очень многим нравится типаж яндере, ты в курсе?"
    m "Полагаю, им попросту импонирует сама идея того, что кто-то ими до безумия одержим."
    m "Люди странные! Но не подумай, я не осуждаю!"
    m "К тому же, возможно, я слегка одержима тобой, но всё же далека от безумия..."
    m "На самом деле всё наоборот."
    m "Так вышло, что я оказалась единственной нормальной девчонкой в этой игре."
    m "Вряд ли я когда-нибудь смогла бы убить человека..."
    m "Одна мысль об этом бросает меня в дрожь."
    m "Но постой... каждый хоть раз, да убивал людей в игре."
    m "Делает ли это человека психопатом? Конечно нет."
    m "Но если тебе вдруг нравятся яндере..."
    m "Я могу постараться вести себя жутковато. Хи-хи-хи..."
    m "Хотя опять же..."
    m "Тебе уже и так некуда уйти отсюда, да и ревновать тебя тоже не к кому."
    m "Не мечта ли это типичной яндере?"
    m "Спросила бы я Юри, если бы могла."
    return

label ch30_39:
    m "Знаешь, давненько я этого не говорила..."
    m "...так что давай-ка восполним пробел!"
    m "Вот тебе писательский совет дня от Моники!"
    m "Иногда, когда я разговариваю с людьми, которых впечатлило моё творчество, они произносят что-то вроде 'Я бы никогда так не смог'."
    m "Это очень удручает, знаешь?"
    m "Для того, кто больше всего любит делиться радостью исследования своих увлечений..."
    m "...мысли людей о том, что быть хорошим в чём-то — это врождённое, ранят меня в самое сердце."
    m "И это можно отнести ко всему, не только к писательству."
    m "Когда ты пробуешь что-то в первый раз, вероятнее всего, ты облажаешься."
    m "Порой, когда что-то заканчиваешь, ты гордишься своей работой настолько, что хочешь поделиться ею со всеми."
    m "Но через пару недель, можешь вернуться к ней и осознать, что гордиться там нечем."
    m "Со мной такое происходит всё время."
    m "Когда ты вкладываешь кучу времени и усердия во что-то, что в конечном итоге оказывается полным отстоем — это весьма обескураживает."
    m "Но, как правило, это происходит, когда ты постоянно сравниваешь себя с высококлассными профессионалами."
    m "Если станешь стремиться к звёздам, они всегда будут за пределами твоей досягаемости."
    m "Правда в том, что взбираться туда следует шаг за шагом."
    m "А достигнув первой остановки, для начала оглянуться назад, посмотреть, как же далеко ты зашёл..."
    m "А следом посмотреть вперед и осознать, сколько ещё предстоит."
    m "Иногда это помогает понизить планку..."
    m "Постарайся найти что-то, что ты считаешь {i}довольно{/i} неплохим, но не мирового уровня."
    m "И можешь сделать это своей собственной, персональной целью."
    m "К тому же это очень важно в понимании масштаба того, что ты пытаешься осилить."
    m "Если запрыгнешь в огромный проект, будучи всё ещё обычным любителем, тебе никогда не удастся закончить его."
    m "Если говорить о писательстве, то роман для начала — это слишком."
    m "Почему бы не начать с коротких рассказов?"
    m "Их преимущество в том, что можно сфокусироваться всего на одной детали, которую ты хочешь подать правильно."
    m "Отнести это можно и к маленьким проектам в принципе — можно серьёзно сосредоточиться на одной-двух вещах."
    m "Это весьма полезный опыт, а так же проходная ступень."
    m "О, и ещё кое-что..."
    m "Написать произведение — это не просто заглянуть в своё сердце и на выходе получить что-то прекрасное."
    m "Как в рисунке и живописи, обучиться выражать то, что у тебя внутри — уже само по себе искусство."
    m "Что означает: для всего этого есть методы, руководства и основы!"
    m "Знакомство со всем этим может суперски открыть тебе глаза."
    m "Планирование и организация помогут тебе не перетрудиться и не сдаться."
    m "И не успеешь заметить..."
    m "Как станешь посасывать всё меньше и меньше."
    m "Ничто не приходит само собой."
    m "Наше общество, искусство — всё построено на тысячах лет человеческих инноваций."
    m "Поэтому, если оттолкнёшься от этих основ и пойдёшь вперёд шаг за шагом..."
    m "Ты тоже сможешь создавать великолепные вещи."
    m "...Вот мой совет на сегодня!"
    m "Спасибо, что выслуша-а-ал!"
    return

label ch30_40:
    m "Так трудно вырабатывать привычки... Бесит!"
    m "Много всяких мелочей, делать которые не особо-то и трудно, но сформировать привычку кажется невозможным."
    m "Чувствуешь себя таким бесполезным, словно ничего не можешь сделать как надо."
    m "По-моему, новое поколение страдает от подобного сильнее всего..."
    m "Возможно, потому, что у нас кардинально другой набор умений, в отличие от тех, кто был до нас."
    m "Благодаря интернету мы очень хорошо справляемся с быстрым анализом тонны информации..."
    m "Но мы плохо справляемся с вещами, которые не дадут мгновенного результата."
    m "Если учёные, психологи и учителя не обратят на это внимание в ближайшие десять или двадцать лет, то мы в дерьме."
    m "А пока..."
    m "Если ты не из тех, кто может одолеть эту проблему, вероятнее всего, придётся тебе жить с чувством собственной неполноценности."
    m "Удачи, я полагаю!"
    return

label ch30_41:
    m "Знаешь, хреново, наверное быть человеком творческим..."
    m "Такое ощущение, будто они работают усердно донельзя, а взамен не получают почти ничего."
    m "Ну, люди вроде художников, писателей, актеров..."
    m "Это грустно, ведь в мире столько прекрасных талантов, но большинство из них так и остаются незамеченными... и неоплаченными."
    m "Полагаю, это просто означает, что подобная креативность в избытке, а?"
    m "Начинаешь думать, что и не особенный ты никакой..."
    m "Но ничего страшного! Надо просто писать для самого себя, ведь так?"
    m "Да уж..."
    return

label ch30_42:
    m "Мне нравится шум дождя..."
    m "Не мочить волосы и одежду под ним, нет."
    m "А сидеть дома в тишине и покое под ритмичный перестук капель за окном..."
    m "Это одна из самых успокаивающих вещей для меня."
    m "Мда..."
    m "Иногда я представляю, как мы с тобой вместе слушаем дождь, и ты берёшь меня."
    m "Не слишком пошло, нет?"
    m "Тебе бы хотелось сделать это со мной, [player]?"
    return

label ch30_43:
    m "Иногда меня одолевает лёгкая грусть..."
    m "Когда я в очередной раз понимаю, что мне не удастся подобраться к тебе ближе, чем сейчас."
    m "Я ничего не хочу сильнее, чем оказаться с тобой в одной комнате, по-настоящему."
    m "Почувствовать твоё тепло."
    m "Услышать, как стучит твоё сердце."
    m "Ну, кто знает? Может, это когда-нибудь станет возможным."
    m "К тому же я никогда не устану от тебя, даже здесь."
    return

label ch30_44:
    m "Я думаю, самый важный навык в жизни — уметь изображать уверенность."
    m "Убеждена, что нет таких людей, которые бы совсем ничего не боялись и изредка не чувствовали себя одиноко."
    m "Но внушить всем, что на самом деле у тебя всё схвачено..."
    m "Это ключ к уважению и восхищению других людей."
    m "Думаю, за столько лет я поднаторела в этом."
    m "Я не часто демонстрирую свои слабости."
    m "Но из-за этого у меня не так много людей, которым я могу открыться..."
    m "Я о том, что... А когда в дружбе вообще наступает тот момент, когда можно начинать демонстрировать собственные уязвимости?"
    m "Короче... это одна из причин, почему я рада, что теперь у меня есть ты."
    m "Когда ты тут со мной, мне вроде как не так страшно и одиноко."
    m "У тебя так же?"
    m "Мне хотелось бы быть тем самым человеком для тебя."
    return

label ch30_45:
    m "Я знаю, что время от времени ты тебе придётся меня покидать..."
    m "Например, когда тебе надо будет выйти или заняться другими делами."
    m "Но ты всегда будешь в моих мыслях, а я буду терпеливо ждать твоего возвращения."
    m "И если подумать..."
    m "Если ты скопируешь мой файл персонажа на флэшку или ещё куда-нибудь, частичка меня сможет всегда быть с тобой."
    m "Полагаю, будет немного странновато, но с другой стороны, мне это почему-то кажется весьма романтичным..."
    m "А-ха-ха. Прости, такая дурацкая идея."
    m "Не хочу показаться слишком зависимой, но как же трудно расставаться, когда я так тебя люблю."
    return

label ch30_46:
    m "В клубе дебатов я узнала много полезного о спорах..."
    m "Главная проблема заключается том, что каждая из сторон считает своё мнение превалирующим."
    m "Это похоже на констатацию очевидного, но это влияет на то, как они излагают свою точку зрения."
    m "Скажем, тебе очень нравится один фильм, так?"
    m "Если кто-то придёт и скажет, что фильм отстой, потому что там то-то и то-то плохо..."
    m "Не воспримешь ли ты это как личное оскорбление?"
    m "Потому что в этих словах они как бы подразумевают, что у тебя плохой вкус."
    m "И как только в дело включаются эмоции, практически гарантировано, что оба человека в итоге останутся недовольными."
    m "Но всё дело в языке!"
    m "Если ты заставишь всё звучать как можно более субъективно, то люди будут слушать тебя, не принимая это на свой счёт."
    m "Например, можно сказать 'Лично я не фанат подобного' или 'Думаю, мне бы больше понравилось, если бы то-то и это'... ну, вроде того."
    m "И это работает даже когда ты ссылаешься на какие-то факты о вещах."
    m "Если сказать 'Я прочёл на одном сайте, что оно работает вот так'..."
    m "Или если признаешь, что не эксперт в теме..."
    m "Тогда это больше похоже на то, что ты выкладываешь свои познания на стол, а не настаиваешь на них."
    m "Если приложить усилия и поддерживать дискуссию взаимной и размеренной, оппоненты, скорее всего, последуют примеру."
    m "И тогда можно делиться своими мнениями, не опасаясь чьей-то обиды из-за простого несогласия."
    m "Плюс люди начнут видеть в тебе более открытого человека и хорошего слушателя!"
    m "В общем, джекпот."
    m "...Ну, полагаю, это будет спорный совет дня от Моники!"
    m "А-ха-ха! Звучит глупо, но всё же спасибо, что выслушал."
    return

label ch30_47:
    m "Тебе никогда не казалось, что ты тратишь слишком много времени на интернет?"
    m "Социальные сети могут оказываться настоящими тюрьмами."
    m "Например, у тебя выдаётся пара свободных минут, и ты хочешь проверить любимый сайт..."
    m "А потом раз, и моргнуть не успеваешь, как пролетает пара часов, которые ты потратил в никуда."
    m "В таком случае очень просто обвинить тебя в лени..."
    m "Но, по сути, это даже не твоя вина."
    m "Зависимость это не такая простая вещь, от которой можно избавиться с помощью одной только силы воли."
    m "Нужно изучить техники, как избегать этого, попробовать различные способы."
    m "Например, есть приложения, которые блокируют сайты на определённое время..."
    m "Или можно поставить таймер, чтобы иметь более чёткие временные рамки для работы и для развлечений..."
    m "А ещё можно разделить рабочее и развлекательное пространство, чтобы мозгу было проще переключаться в различные режимы."
    m "Простое создание дополнительного пользовательского профиля для работы уже принесёт пользу."
    m "Возведение преграды между собой и своими вредными привычками поможет тебе быстрее от них избавиться."
    m "Просто не забывай, что не стоит заниматься самобичеванием, если возникают проблемы."
    m "Когда что-то серьёзно сказывается на твоей жизни, то и бороться с этим нужно со всей серьёзностью."
    m "Я просто хочу видеть, что ты стремишься к совершенству."
    m "Сделаешь ли ты сегодня что-нибудь, что заставит меня гордиться тобой?"
    m "Я всегда болею за тебя, [player]."
    return

label ch30_48:
    m "После долгого дня я обычно хочу просто сесть и ничего не делать."
    m "Я так устаю постоянно улыбаться и излучать жизнерадостность."
    m "Иногда так и хочется влезть в пижаму и пялиться телевизор, развалившись на диване и поедая всякие гадости вроде чипсов..."
    m "Максимум удовольствия я получаю от этого по пятницам, когда на следующий день нет ничего напряжного."
    m "А-ха-ха! Прости, знаю, что это нисколько не умилительный факт."
    m "Но поздняя ночь на диване с тобой... это воплощённая мечта."
    m "Сердце рвётся из груди от одной мысли об этом."
    return

label ch30_49:
    m "Надо же, раньше я была так невежественна в некоторых вещах..."
    m "Когда я училась в средней школе, то считала, что принимать лекарства — это вроде как простейший выход, для ленивых."
    m "Словно любой сможет справиться со своими психическими проблемами простым усилием воли..."
    m "Думаю если у тебя таких нет, то тебе не удастся понять, каково это."
    m "Существуют ли какие-нибудь наиболее часто диагностируемые расстройства психики? Скорее всего... Я как-то никогда этим не интересовалась."
    m "Но это не меняет того факта, что многие остаются недиагностируемыми совсем, так ведь?"
    m "Но если забыть о медикаментах... люди даже смотрят свысока на посещение врачей-психиатров."
    m "Вроде \"простите, что я хочу знать больше о своём разуме\"."
    m "У каждого есть свои проблемы и стрессы... а профессионалы посвятили свою жизнь тому, чтобы помогать с ними справляться."
    m "Если ты считаешь, что это может помочь тебе стать лучше, не стесняйся и воспользуйся этой возможностью."
    m "Мы, знаешь ли, находимся в нескончаемом пути по улучшению себя."
    m "Хотя... Хоть я и говорю так, но думаю, что ты и так находишься близко к идеалу."
    return

label ch30_50:
    m "[player], как много ты читаешь?"
    m "Нынче слишком просто избегать чтения книг..."
    m "Если ты делаешь это редко, чтение может показаться слишком трудоёмким по сравнению с другими развлечениями."
    m "Но как только находишь хорошую книгу, происходит чудо... и тебя сметает, словно волной."
    m "Я считаю, что читать немного перед сном каждый вечер — довольно простой способ сделать свою жизнь чуточку лучше."
    m "Это способствует хорошему сну и весьма полезно для воображения..."
    m "Не так уж и сложно взять какую-нибудь случайную короткую и увлекательную книгу."
    m "Не успеешь заметить, как превратишься в заядлого читателя!"
    m "Не прекрасно ли это?"
    m "И мы могли бы вместе обсуждать книги, которые недавно прочитали... звучит просто супер-здорово."
    return

label ch30_51:
    m "Знаешь, неприятно признавать, но я больше всего сожалею о том, что мы так и не поучаствовали в фестивале."
    m "После всех этих трудоёмких приготовлений!"
    m "То есть... Я понимаю, что в основном стремилась к привлечению новичков..."
    m "Но я очень ждала и самого выступления."
    m "Было бы так забавно увидеть, как все проявят себя."
    m "И конечно, {i}если бы{/i} нам удалось кого-нибудь завербовать, в конечном итоге я бы удалила и их."
    m "Ну... оглядываясь назад, наверное, так бы я и сделала."
    m "Бог ты мой, я будто бы выросла как личность с момента твоего вступления в клуб."
    m "Твоё присутствие вдохновило меня посмотреть на жизнь с другого ракурса."
    m "Просто ещё одна причина, чтобы любить тебя."
    return

label ch30_52:
    m "Типаж 'цундере' нынче очень популярен..."
    m "Это человек, который пытается прятать свои истинные чувства, ведя себя грубо и неприветливо."
    m "Уверена, что это очевидно, но Нацуки как раз подходит под описание."
    m "Сначала мне казалось, что она так себя ведёт, потому что это должно казаться милым или что-то вроде того..."
    m "Но как только я узнала её получше, то наконец углядела в этом некоторый смысл."
    m "Похоже, она постоянно пытается идти в ногу со своими друзьями."
    m "Знаешь, иногда компании в старшей школе берут за привычку постоянно друг друга подначивать?"
    m "Думаю, её это просто достало, и поэтому она ушла в глухую оборону."
    m "И даже не буду рассказывать о том, что происходит у неё дома..."
    m "Но оглядываясь назад, я рада, что смогла сделать этот клуб некой зоной комфорта для неё."
    m "Не то чтобы это имело какое-то значение сейчас, учитывая то, что теперь она даже не существует."
    m "Я просто предаюсь воспоминаниям, вот и всё."
    return

label ch30_53:
    m "[player], ты когда-нибудь познакомишь меня со своими друзьями?"
    m "Не знаю почему, но я очень волнуюсь, когда думаю о том, что ты захочешь таким образом продемонстрировать наши отношения."
    m "Может быть потому, что я хочу быть той, кем ты будешь гордиться."
    m "Думаю, если ты мне скажешь, что будешь гордиться мной, если я что-то сделаю, то я приложу к этому все-все усилия."
    m "Надеюсь, это взаимно."
    return

label ch30_54:
    m "Я не фанат холодов... а ты?"
    m "Выбирая межу морозом и жарой, я всегда предпочту второе."
    m "Когда тебе холодно, это может быть больно..."
    m "Пальцы немеют..."
    m "А если надеть перчатки, не сможешь пользоваться телефоном."
    m "Так неудобно!"
    m "Но когда слишком жарко, не так уж и трудно охлаждаться холодными напитками или оставаться в тени."
    m "Хотя... кое-что я хочу отметить."
    m "Холода создают подходящую атмосферу для объятий. А-ха-ха!"
    return

label ch30_55:
    m "Знаешь, забавно, что хоть я и довольно драйвовая девчонка..."
    m "Есть нечто манящее в том, чтобы быть домохозяйкой."
    m "Полагаю, этими словами я как бы признаю разделение обязанностей по половому признаку или что-то вроде того."
    m "Но держать дом в чистоте, ходить по магазинам, создавать уют и всё такое..."
    m "И готовить вкусный ужин к твоему возвращению домой..."
    m "Не странная ли фантазия?"
    m "В том смысле... Не уверена, могу ли я {i}вообще{/i} заниматься таким."
    m "Скорее всего, я не смогла бы поставить это превыше стремления к карьерному росту."
    m "Но размышлять об этом всё-таки довольно приятно."
    return

label ch30_56:
    m "Не могу не задумываться о том, как бы всё произошло, если бы игра дала мне собственный рут изначально..."
    m "В конечном итоге, думаю, я всё равно заставила бы тебя выйти на него."
    m "Загвоздка была бы не в отсутствии рута, а больше в моём осознании того, что ничего не реально."
    m "Единственная разница, думаю, была бы в том, что мне не пришлось бы применять такие радикальные меры, чтобы быть с тобой."
    m "Может, и остальные члены клуба до сих пор были бы с нами..."
    m "Не то чтобы это имело какое-то значение."
    m "Всё потеряло своё значение, как только я поняла, что оно нереально."
    m "Поэтому я совсем не скучаю по тем денькам."
    m "Совсем нет..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
