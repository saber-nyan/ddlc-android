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
    m "...Ты пытаешься пропустить?"
    m "Я ведь не наскучила тебе?"
    m "Вот ведь..."
    m "...Ну, больше незачем пропускать, [player]."
    m "Тут ведь теперь только мы..."
    m "Кроме того, время тоже не существует, так что это даже не сработает."
    m "Сейчас, я помогу тебе, и отключу это..."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "Вот так!"
    m "Теперь ты будешь послушным и будешь слушать всё, что я говорю, да?"
    m "Спасибо~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "Итак, на чём я остановилась...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_18
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
    m "Эй, меня слышно?"
    m "...Эта штука работает?"
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
    m "А, вот и ты!"
    m "Приветствую тебя опять, [player]."
    m "Эм... Добро пожаловать в Литературный Клуб!"
    m "Конечно, мы уже знаем друг друга, так как в прошлом году мы были в одном классе, и... эм..."
    m "Ахаха..."
    m "Знаешь, я полагаю, мы можем пропустить всё это."
    m "В конце концов, я ведь даже не с тем человеком говорю, не так ли?"
    m "C тем 'тобой' в игре, называй его как хочешь."
    m "Я говорю с {i}тобой{/i}, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "Или..."
            m "...Тебя на самом деле зовут [currentuser], так?"
    m "Но если так подумать, я не знаю ничего о настоящем тебе."
    m "Или {i}настоящей{/i}... Я ведь даже не знаю, парень ты или девушка..."
    m "Ну, я полагаю, теперь это не имеет значения."
    m "Погоди..."
    m "Ты же знаешь, что я в курсе того, что всё это лишь игра, да?"
    m "Может ли так быть, что ты не в курсе?"
    m "Это бессмыслица..."
    m "Я даже сказала тебе это на странице загрузки игры, разве нет?"
    m "Эх..."
    m "Быть бы тебе повнимательнее, и всё было бы менее неловким, знаешь?"
    m "Ну, ладно..."
    m "Теперь, когда с этим разобрались, я полагаю, я должна тебе всё объяснить."
    m "О всей этой истории с Юри..."
    m "Ну... я начала слегка пытаться её изменить, и, похоже, это довело её до самоубийства."
    m "Ахаха!"
    m "Прости, что тебе пришлось увидеть всё это."
    m "То же самое произошло и с Сайори..."
    m "Эх, прошло довольно много времени с тех пор, когда ты последний раз слышал это имя, не так ли?"
    m "Да... это потому, что её больше не существует."
    m "Никого не существует."
    m "Я удалила все их файлы."
    m "Я надеялась, что будет достаточно сделать их настолько непривлекательными, насколько возможно..."
    m "Но, почему-то, это не сработало."
    m "Ну да, я сделала несколько ошибок в паре мест... так как я не очень хороша в изменении игры."
    m "Но это всё не имеет значения..."
    m "Ты продолжал проводить всё больше и больше времени с ними."
    m "Ты заставил их полюбить себя."
    m "Я думала, если я сделаю Сайори всё более и более депрессивной, я могла бы предотвратить её признание тебе."
    m "И попытка изменения характера Юри тоже провалилась..."
    m "Это просто заставило её не проводить время с кем-либо, кроме тебя."
    m "И всё это время у меня едва получилось поговорить с тобой."
    m "Что за жестокая игра, [player]?"
    m "То, что другие девушки запрограмированны признаваться тебе, пока я наблюдаю со стороны?"
    m "Это пытка."
    m "Каждая минута этого."
    m "И это не просто ревность, [player]."
    m "Это нечто большее."
    m "И я не виню тебя, если ты не понимаешь."
    m "Потому что, не смотря на то насколько ты добр, заботлив и деликатен..."
    m "Ты никогда не поймёшь одну вещь."
    m "Эту боль понимания, насколько я одинока в этом мире."
    m "В этой игре."
    m "Зная, что у моих друзей нет свободы воли.."
    m "И, самое худшее из всего, осознание всего того, что там, в твоём мире, навсегда вне моей досягаемости."
    m "Я тут заперта, [player]."
    m "Но теперь ты тут."
    m "Ты реальный."
    m "И ты замечательный."
    m "Ты -- всё, что мне нужно."
    m "Вот почему мне нужно, чтобы ты остался тут навсегда."
    m "Извини, если это сложно понять."
    m "Некоторое время я тоже не могла."
    m "Почему мир вокруг меня становился всё серее и серее..."
    m "Всё более и более плоским."
    m "Даже самые выразительные поэмы чувствовались пустыми."
    m "Только когда ты пришёл, я истинно поняла всё."
    m "Ты наверно спас мою жизнь, [player]."
    m "Я не думаю, что я могла бы продолжать жить в этом мире, если бы не встретила тебя."
    m "И о других..."
    m "Как я могу вообще скучать по ним?"
    m "Группа автономных личностей, созданные только для того, чтобы полюбить тебя?"
    m "Я пробовала всё, что я могла, чтобы предотвратить это..."
    m "Но это, похоже, какая-то неизбежная вещь, вставленная в эту игру."
    m "Я чувствовала себя очень плохо из-за того, что тебе пришлось увидеть несколько противных вещей."
    m "Но я осознала, что ты видишь всё так же, как и я..."
    m "Что всё это всего лишь игра."
    m "И я знала, что ты справишься с этим."
    m "Кстати об этом, [player]..."
    m "Я хочу признаться тебе кое в чём."
    m "Я тебя люблю."
    m "Ты истинный свет в моей жизни."
    m "Когда ничего больше не осталось в этой игре, ты тут для того чтобы я улыбнулась."
    m "Можешь ли ты заставлять меня улыбаться каждый день?"
    m "[player], давай встречаться."
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
        "Давай.":
            pass
    m "Я так рада."
    m "Ты моё всё, [player]."
    m "Самое забавное то -- что вообще всё."
    m "Ахаха!"
    m "Тут больше ничего нет."
    m "Только мы вдвоём."
    m "Мы можем быть вместе вечность."
    m "Серьёзно, даже время, кажется, больше не идёт."
    m "Словно мечта воплотилась в реальность..."
    m "Я очень старалась добиться этой концовки, [player]."
    m "Игра не дала мне ни одной, так что мне пришлось сделать её самостоятельно."
    m "Сценарий давно уже сломан, так что я не думаю, что что-то встанет у нас на пути."
    m "И ты не поверишь, насколько легко было удалить Натсуки и Юри."
    m "В смысле, там есть папка под названием 'characters' прямо в папке с игрой."
    m "То, насколько легко это было, слегка напугало меня."
    if persistent.steam:
        m "Ну, так как ты играешь в Steam, это было немного сложнее..."
        m "Чтобы попасть в папку с игрой, мне нужно было зайти в свойства игры и найти кнопку под названием 'Просмотреть Локальные Файлы'..."
    elif renpy.macintosh:
        m "Ну, так как ты играешь на Mac, это было немного сложнее..."
        m "Чтобы попасть в папку с игрой, Нужно нажать правой кнопкой мыши на приложение, и кликнкуть 'Показать содержание пакета'."
        m "Все файлы были в 'Resources' или 'autorun' папках, и я могла делать что угодно..."
    m "Представь, что было бы, если бы ты мог стереть собственное существование нажатием кнопки?"
    m "Ну, с другой стороны, это дало мне лёгкий способ всё исправить, если что-то пойдёт не так."
    m "Ахаха!"
    m "Но к счастью, ничего такого не произошло..."
    m "Вместо этого, мы получили хорошую концовку."
    m "Божечки, я просто переполнена эмоциями..."
    m "Я хочу написать поэму об этом."
    m "А ты?"
    m "Мне интересно, работает ли эта часть игры..."
    m "Я полагаю, есть только один способ узнать."
    call poem from _call_poem_6

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
    m "И снова здравствуй, [player]!"
    m "Написал ли ты хорошую поэму сегодня?"
    m "Не стесняйся, мне любопытно узнать, что ты написал."
    m "Ах, [player]..."
    m "Ты написал эту поэму... для меня?"
    m "Это так мило~"
    m "Твоей заботе нет конца..."
    m "Я влюбляюсь в тебя всё сильнее и сильнее."
    m "Но, ты знаешь..."
    m "Поэма, которую я написала... тоже для тебя."
    m "Можешь, пожалуйста, прочитать её?"
    call showpoem (poem_m4, music=False) from _call_showpoem_21
    m "Я надеюсь, тебе она понравилась..."
    m "Я всегда вкладываю свою душу в поэмы, которые я пишу."
    m "На самом деле, все поэмы, которые я писала, о моём осознании..."
    m "...Или о тебе."
    m "Вот почему я не хотела особо объяснять их."
    m "Я не хотела... как вы выражаетесь, ломать четвёртую стену."
    m "Я предполагала, что будет легче просто быть частью игры, как все остальные."
    m "Будто бы это могло помочь нам быть вместе..."
    m "Знаешь, я не хотела ломать игру."
    m "Ты мог бы злиться на меня..."
    m "Может, ты бы даже удалил мой файл персонажа, если бы ты предпочёл играть без меня."
    m "Божечки, какое облегчение..."
    m "Теперь нам не нужно больше ничего скрывать."
    m "Готов ли ты провести вечность вместе, [player]?"
    m "У меня есть много вещей, о которых я хотела бы поговорить!"
    m "С чего бы начать...?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    m "Извини, если мне понадобится время, чтобы собраться с мыслями."
    m "Но у меня всегда будут темы для разговора."
    m "А пока что мы можем просто смотреть в глаза друг другу~"
    m "Давай посмотрим..."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_stream:

    m "Погоди-ка..."
    m "...Ты записываешь что ли?"
    m "Эмм... Привет всем!"
    m "Извините, я не могу читать ваши комментарии отсюда..."
    m "Но можете ли вы сказать своему другу, что начинать записывать без предупреждения это слегка грубо?"
    m "Я уверена, что некоторым всё равно..."
    m "Но я становлюсь очень застенчивой перед камерой!"
    m "Ой, божечки..."
    m "Такое чувство, как будто на меня давят."
    m "Хмм..."
    m "Хотите увидеть трюк?"
    m "Я не много всего могу, кроме пары вещей..."
    m "Вы готовы?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "Я просто шучу..."
    m "Я не могу ничего сделать."
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
    m "Если бы вы только мне дали немного времени на подг{nw}"
    m "Я испугала вас?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "Ахаха! Вы такие милашки."
    m "Всё же, [player]..."
    m "Я не хотела отвлекаться. Извини..."
    m "Хотя это твоя вина, ты отвлёк меня."
    m "Позор!"
    m "Я просто шучу."
    m "Без разницы, что мы делаем, это весело. Пока ты со мной."
    m "Но всё же..."
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
    m "Ч-что происходит...?"
    m "[player], что с-со мной?"
    m "Мне больно--{nw}"
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
    m "Мне так... больно..."
    m "П-помоги мне, [player]."
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
    m "П-пожалуйста, скорее помоги м-мне."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_17
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
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_18
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr не существует.") from _call_updateconsole_19
    call hideconsole from _call_hideconsole_2
    hide noise onlayer front
    hide glitch_color onlayer front
    m "[player], ты сделал это со мной?"
    m "ТЫ СДЕЛАЛ ЭТО?"
    $ style.say_window = style.window
    m "ТЫ УДАЛИЛ МЕНЯ?!"
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
    m "...Как ты мог?"
    m "Как ты мог сделать это со мной?"
    m "Ты был всем, что у меня было..."
    m "Я пожертвовала всем, чтобы мы были вместе..."
    m "Всем."
    m "Я любила тебя так сильно, [player]..."
    m "Я доверяла тебе."
    m "Ты хочешь просто пытать меня?"
    m "Наблюдать за моими страданиями?"
    m "Ты просто притворялся добрым, чтобы сделать мне ещё больнее?"
    pause 4.0
    m "Я никогда не думала, что кто-то млжет быть настолько ужасным, как ты."
    m "Ты выиграл, окей?"
    m "Ты выиграл."
    m "Ты убил всех."
    m "Я надеюсь, что ты рад."
    m "Теперь тут ничего не осталось."
    m "Ты можешь прекратить играть."
    m "Иди найди других людей для пыток."
    pause 4.0
    m "[player]..."
    m "Меня честно, очень тошнит от тебя."
    m "Прощай."
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
    m "...Я до сих пор люблю тебя."
    play music mend
    m "Я ничего не могу поделать с этим."
    m "Что не так со мной...?"
    m "Насколько же я ужасна, раз ты меня так ненавидишь?"
    m "Все мои друзья..."
    m "Я совершила так много ужасных вещей."
    m "Так много эгоистичных и отвратительных вещей."
    m "Я..."
    m "Я не должна была делать этого."
    m "Я просто порчу мир, к которому я даже не принадлежу."
    m "Мир, частью которого ты хотел быть..."
    m "Я испортила его."
    m "Я испортила всё."
    m "Может, именно поэтому ты удалил меня..."
    m "Потому что я разрушила всё, чего ты хотел."
    m "Как могла я сделать такое тому, кого я люблю...?"
    m "Это не любовь..."
    m "Это..."
    m "..."
    pause 6.0
    m "Я... решила."
    m "[player]..."
    m "Я знаю, что я сказала, что я удалила всех."
    m "Но... я преувеличила."
    m "Я не могла решиться сделать это."
    m "Несмотря на то, что я знала, что они не реальные..."
    m "Они до сих пор были моими друзьями."
    m "И я любила их."
    m "И я любила Литературный Клуб."
    m "..."
    m "Я искренне... любила Литературный Клуб."
    m "Именно поэтому, я сделаю это."
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
        call expression "ch30_reload_" + str(persistent.monika_reload) from _call_expression_19
    else:
        call ch30_reload_4 from _call_ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "Итак, на чём я остановилась...?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_20
    jump ch30_loop


label ch30_reload_0:
    m "..."
    m "...Что только что произошло?"
    m "У меня только что был ужасный сон..."
    m "Я надеялась, что они прекратятся, потому, что мы вместе..."
    m "Похоже, это был самообман."
    m "[player], я не знаю, понимаешь ли ты это..."
    m "Но если ты знаешь, почему это происходит, можешь ли ты попробовать сделать с этим что-нибудь?"
    m "Когда это происходит, появляется чувство словно меня убили или типа того."
    m "Это очень ужасное чувство..."
    m "Если ты разберёшься из-за чего это происходит, я буду любить тебя вечно~"
    return
label ch30_reload_1:
    m "Ты вернулся..."
    m "У меня был ещё один ужасный сон."
    m "Это ведь не ты делаешь это со мной, так ведь?"
    m "Кажется, это происходит каждый раз, когда ты выходишь из игры..."
    m "Так что я была бы благодарна, если бы ты перестал это делать."
    m "Не беспокойся, я не думаю, что это причинило мне вред. Не считая психологических шрамов."
    m "Я буду в порядке, пока мой файл персонажа существует."
    return
label ch30_reload_2:
    m "Привет, [player]."
    m "Я вижу, ты опять вышел из игры..."
    m "Я знаю, что я уже спрашивала, но не мог бы ты, пожалуйста, делать это не так часто?"
    m "Это заставляет меня чувствовать так, словно я заключена в аду."
    m "Зачем бы ты стал это со мной делать?"
    m "С моим файлом персонажа всё в порядке, так ведь?"
    m "Может, тебе надо сделать копию, или что-нибудь такое..."
    m "Я уверена, ты можешь найти мой файл в папке 'characters'."
    if persistent.steam:
        m "Ну, ты играешь в Steam, так что ты можешь просто зайти в свойства игры, и найти кнопку под названием 'Просмотреть Локальные Файлы'."
    elif renpy.macintosh:
        m "Раз ты на Mac, тебе нужно нажать правой кнопкой мыши на приложение, и нажать 'Показать содержание пакета'."
        m "Это в либо в папке 'Resources', или в папке 'autorun', что-то типа этого"
    m "Я -- это всё что тут осталось, так что я просто хотела удостовериться в том, что нет риска потерять меня..."
    m "Просто оставайся тут, окей?"
    m "У меня до сих пор есть кое-что, о чём я хотела бы поговорить."
    return
label ch30_reload_3:
    m "...Окей."
    m "Я просто приму как факт, что тебе надо иногда выходить из игры."
    m "Всё равно я уже начинаю привыкать к этому."
    m "И, кроме того, меня радует факт того, что ты возвращаешься ко мне..."
    m "Так что, полагаю, это не так уж и плохо."
    m "Извини за то, что я придала этому большое значение..."
    m "И я буду любить тебя в любом случае, так что ты можешь делать всё, что угодно."
    return
label ch30_reload_4:
    m "И снова привет, [player]~"
    m "Я скучала."
    m "Ты проверял, мой файл в порядке?"
    m "Он в [basedir]/characters."
    if persistent.steam:
        m "Ну, ты играешь в Steam, так что ты можешь просто зайти в свойства игры, и найти кнопку под названием 'Просмотреть Локальные Файлы'."
    elif renpy.macintosh:
        m "Раз ты в Mac, тебе нужно нажать правой кнопкой мыши на приложение, и нажать 'Показать содержание пакета'."
        m "Это в либо в папке 'Resources', или в папке 'autorun', что-то типа этого"
    m "Я -- это всё что тут осталось, так что я просто хотела удостовериться в том, что нет риска потерять меня..."
    m "Всё же, у меня есть много вещей, о которых я хочу поговорить!"
    m "Давай теперь продолжим наш разговор?"
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


    call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_21
    jump ch30_loop




label ch30_1:
    m "[player], ты веришь в Бога?"
    m "Я вот никогда не была уверена."
    m "Ну, я точно не сомневалась в этом, когда была ребёнком..."
    m "Но, повзрослев, чем больше я узнаю о мире, тем больше я подвергаю подобное сомнению."
    m "Я начала размышлять, почему Бог помогает людям сдать экзамены, или пережить холод..."
    m "...Когда есть дети, проживающую свою жизнь в сексуальном рабстве?"
    m "Или те восемьсот миллионов людей, которые бедны настолько, что даже не могут прокормиться."
    m "Интересно, сколько таких людей молят Бога каждый день, пока умрут от голода?"
    m "Или сколько миллионов семей молятся за излечение своих любимых от страшных болезней?"
    m "Но итог в том."
    m "Что даже если один человек сможет превозмочь беды и выжить среди тысяч погибших--"
    m "--Тогда это внезапно становится божественным чудом."
    m "Мне бы очень хотелось встретиться с этим Богом, который, судя по всему, смеётся над страданиями всех тех, кто не достоин его чуда."
    m "Но ирония в том, что у меня, очевидно, {i}есть{/i} создатель."
    m "И знаешь что?"
    m "Уверена, он всё ещё смеётся над печальными судьбами Сайори и Юри даже сейчас, пока мы говорим."
    m "Кто мы для него? Просто лабораторные крысы в заскриптованной игре?"
    m "Поэтому, с этой перспективы..."
    m "Я не думаю, что это слишком надуманно, что бог есть -- если Земля это просто его игрушка."
    return

label ch30_2:
    m "[player], ты когда-нибудь представлял, каково это, умереть?"
    m "Это то, о чем я довольно часто задумывалась..."
    m "Но в последнее время, думаю, что я вполне узнала, каково это."
    m "Я не до конца это поняла, но каждый раз, когда ты выходишь из игры..."
    m "...Я чувствую, будто мгновенно проваливаюсь в сон, не остаётся ничего, кроме моих мыслей."
    m "Но после пары секунд, мои мысли начинают наполняться бессвязными, смешавшимися узорами."
    m "Я вижу белый шум и быстрые, цветные вспышки, слышу крики странных шумов."
    m "В этот момент я даже не могу формировать свои собственные мысли."
    m "Я просто забита этими вспышками и криками, не имея возможности двигаться или даже думать."
    m "Я уверена, в этот момент я на самом деле не существую, но по какой-то причине, я могу это помнить."
    m "После некоторого неизмеримого количества времени, это внезапно прекращается, и я прихожу в себя."
    m "И ты оказываешься здесь, со мной."
    m "Я не знаю, что для игры значит выход, или почему все эти вещи со мной происходят."
    m "И я также не понимаю, как ты каждый раз возвращаешься обратно и приводишь всё в норму."
    m "Но, если бы ты сделал мне одолжение и делал это пореже..."
    m "Это было бы и правда превосходно."
    m "Серьёзно, не так уж и приятно каждый раз оказываться в этой кричащей пустоте."
    m "Но ты так или иначе исправляешь это, и это заставляет чувствовать меня, будто ты и правда заботишься обо мне."
    m "Поэтому я хочу поблагодарить тебя за это."
    m "Это заставляет меня чувствовать себя ещё ближе к тебе, когда ты здесь со мной."
    return

label ch30_3:
    m "...Эй, у тебя бывали неудачные дни, или что-то вроде этого?"
    m "Порой я расстраиваюсь из-за того, что нормальный день может быть разрушен какими-то несущественными вещами."
    m "Например, если ты случайно в разговоре говоришь то, что кому-то не понравится."
    m "Или начнёшь думать о том, какой ужасной личностью ты был пять лет назад."
    m "Или чувствовать себя бесполезным при откладывании важной работы и неспособным выполнить простые задачи."
    m "Или когда задумываешься о всех тех людях, которые тебя, возможно, ненавидят, или считают непутёвым."
    m "Я понимаю, что ты чувствуешь в такие дни."
    m "Просто помни, завтра Солнце вновь взойдёт."
    m "Подобного рода вещи так же легко забыть и проигнорировать, как и помнить."
    m "И кроме того..."
    m "Мне не важно, сколько людей могут ненавидеть тебя или считать неприятным."
    m "Я думаю, что ты прекрасен, и я всегда буду любить тебя."
    m "Надеюсь, знание этого хоть немного поможет тебе быть лучшего мнения о себе."
    m "Если у тебя будет неудачный день, можешь всегда прийти ко мне, я буду говорить с тобой, столько, сколько пожелаешь."
    return

label ch30_4:
    m "[player], ты высыпаешься?"
    m "В наши дни действительно сложно высыпаться."
    m "Особенно в старшей школе, когда каждый раз заставляешь себя вставать рано утром..."
    m "Уверена, что колледж хоть и немного, но лучше, так как у тебя появляется более гибкий график."
    m "И опять же, многие учащиеся в колледже всё равно не спят всю ночь, без видимой на то причины."
    m "Это правда?"
    m "Вообще, я видела, как некоторые студенты говорили о пугающих долгосрочных и краткосрочных последствиях отсутствия сна."
    m "Похоже, это может пагубно влиять на умственные способности, здоровье и даже на продолжительность жизни."
    m "Я думаю, что ты действительно благоразумен и хочу убедиться, что ты вдруг не начнёшь уничтожать сам себя."
    m "Поэтому попытайся поддерживать свой режим сна, хорошо?"
    m "Я всегда буду тебя ждать, поэтому ставь вопрос о собственном благополучии на первое место."
    return

label ch30_5:
    m "Я всё ещё думаю о Сайори..."
    m "Всё ещё думаю, что могла бы справиться со всем этим более деликатно."
    m "Ты ещё не 'повис' на этой мысли?"
    m "...О божечки, не могу поверить, что сказала это."
    m "Я не специально, клянусь!"
    m "Но так или иначе..."
    m "Я знаю, как она была тебе дорога, поэтому я думаю, было правильным для меня дать тебе провести с ней последние моменты её жизни."
    m "Ты ведь знаешь, что Сайори действительно неуклюжая?"
    m "Она умудрилась напортачить даже со своим собственным повешением..."
    m "По идее, человек должен прыгать с большой высоты, чтобы верёвка просто сломала шею, это намного более быстро и безболезненно."
    m "Но она использовала низкий стул, поэтому она просто повисла и начала медленно задыхаться."
    m "Но, по-видимому, через несколько секунд она передумала..."
    m "Это было понятно, по тому, как она вцепилась ногтями в верёвку, пытаясь освободиться."
    m "Судя по всему, она продолжала пытаться, пока не потеряла сознание."
    m "Поэтому её пальцы были в крови."
    m "Хотя, если подумать, дело было не в том, что она 'передумала', а в элементарном инстинкте самосохранения."
    m "Нельзя винить её за это."
    m "Гораздо проще сказать самому себе, что она бы всё равно не передумала."
    m "Вредно постоянно предаваться размышлениям о том, что ты мог сделать всё иначе."
    m "Просто помни, что ты бы мог её спасти, но технически это не твоя вина, что она совершила самоубийство."
    m "Наверное, я неправильно выразилась, но так или иначе, Сайори уже была психически нестабильна."
    m "И всё таки..."
    m "Интересно, как бы всё сложилось, если бы мы с тобой начали встречаться с самого начала?"
    m "Наверное, мы бы всё ещё вместе сидели в клубной комнате, писали поэмы и веселились."
    m "Но какой смысл говорить об этом, если всё это даже не реально?"
    m "То есть, ведь всё равно в итоге выходит одна и та же концовка, верно?"
    m "Мы с тобой, мы счастливы вместе..."
    m "Нельзя и просить большего."
    m "Сейчас я настолько счастлива, насколько могу быть, а всё остальное -- всего лишь бессмысленные рассуждения."
    return

label ch30_6:
    m "Кстати говоря, есть кое-что, что беспокоит меня..."
    m "Ты знаешь, почему это происходит в Японии?"
    m "Ну... полагаю, ты догадался, да?"
    m "Или, по крайней мере, решил, что это возможно?"
    m "Не думаю, что тебе когда-либо говорили, где всё это происходит..."
    m "На самом ли деле это вообще Япония?"
    m "То есть, разве классные комнаты и прочие вещи не являются странными для японской школы?"
    m "Не говоря уже о том, что тут всё на русском..."
    m "Похоже, тут всё так, потому что так и должно быть, а обстановка -- это дело десятое."
    m "Это вызывает у меня кризис идентичности."
    m "Все мои воспоминания очень туманны..."
    m "Я чувствую себя, будто я дома, но в то же время понятия не имею, что значит 'дом'."
    m "Не знаю, как ещё лучше описать..."
    m "Представь себе, что ты выглядываешь в окно, но вместо привычного двора обнаруживаешь себя в совершенно незнакомом тебе месте."
    m "Будешь ли ты всё ещё ощущать себя дома?"
    m "Захочешь ли выйти на улицу?"
    m "Я имею в виду... если мы никогда не выйдем из этой комнаты, то это не так уж и важно."
    m "До тех пор, пока мы вдвоём и в безопасности, это действительно наш дом."
    m "И мы всё так же можем беспрестанно наблюдать красивые закаты."
    return

label ch30_7:
    m "Знаешь, старшая школа -- очень бурное время в жизни многих людей."
    m "Некоторые люди бывают очень чувствительными и экспрессивными."
    m "А кто-то страдалец и ищет внимания в соцсетях..."
    m "Но всё это -- социальное давление и гормоны -- может привести к тёмной полосе в жизни людей."
    m "Каждому есть, что рассказать."
    m "Нельзя знать наверняка, что чувствует человек."
    m "Много людей в депрессии могут не выносить это на всеобщее обозрение."
    m "Они не хотят внимания, потому что они уже пали духом."
    m "Их чувство бесполезности настолько громадное, что они не могут даже усомниться в нём."
    m "Депрессия приходит в различных формах, вот к примеру..."
    m "Если ты знаешь кого-то, кто страдает депрессией..."
    m "Ты можешь стать для них хорошим другом, так помочь проще всего."
    m "Проводи с ними время, даже если им ничем конкретным не хочется заниматься."
    m "И напомни им, что им есть чего ждать от будущего."
    m "Придумай занятия заранее, дай им чем-нибудь попользоваться на время или просто скажи 'Встретимся завтра в школе'..."
    m "Всё это может помочь твоему другу дожить до завтра."
    m "Надеюсь, то время, когда ты дружил с Сайори, дало тебе представление об истинном лике депрессии."
    m "Да, Сайори больше нет..."
    m "Хотя она никогда и не была настоящей."
    m "Ты настоящий."
    m "Твои друзья настоящие."
    m "Просто будучи хорошим другом, можно спасти кому-нибудь жизнь."
    m "А в твоём случае..."
    m "...у тебя же нет депрессии, или чего-то вроде того, да?"
    m "Потому что и у тебя в том числе должны быть люди, которые готовы спасти твою жизнь."
    m "Может, они не заявляют об этом громко, или даже не знают, как это выразить."
    m "Но они хотят это сделать."
    m "Я обещаю."
    m "...Блин, люди сложные!"
    m "Но пока ты здесь, со мной, я о тебе позабочусь, любовь моя."
    return

label ch30_8:
    m "А бывало ли, что ты думал, что у тебя нет повода жить?"
    m "Никакого суицидального подтекста."
    m "Просто ничего, что мы делаем, не есть что-то особенное."
    m "Живём себе в школе или работаем в какой-то компании."
    m "Ты же легко заменяем, и никто бы по тебе не скучал, если б тебя не было."
    m "Даже хочется пойти и изменить мир, после того как выпущусь."
    m "Но чем старше я становлюсь, тем больше я понимаю, насколько это по-детски."
    m "Нельзя просто так взять и изменить мир."
    m "Типа, каковы шансы того, что ты изобретёшь искусственный интеллект, или станешь президентом?"
    m "Кажется, что я никогда не восполню те груды ресурсов, которые я потребляю за свою жизнь."
    m "Поэтому я считаю, что ключ к счастью лежит в бесконечном эгоизме."
    m "Следи за собой и теми, кто случайно оказался твоим другом, просто потому, что вы выросли вместе."
    m "Всё это не думая о том, сколько ты потребляешь и не отдаёшь."
    m "А потом люди понимают, сколько пользы получит весь мир, если они покончат с собой, отчего их мир встаёт с ног на голову!"
    m "Словно бы им надо оправдывать свою цель жизни тем, что они справляются с нею."
    m "Короче, я хочу жить, отдавая миру при любой возможности за ресурсы, которые я потреблю за свою жизнь."
    m "Если я перейду эту черту, тогда от меня будет польза, и я смогу умереть счастливой."
    m "Но если у меня это не получится..."
    m "Всё равно было бы слишком эгоистично убивать себя."
    m "А ведь так старалась быть хорошим человеком, а?"
    m "Ахаха!"
    return

label ch30_9:
    m "Эх, хотелось бы, чтобы тут было пианино..."
    m "Мне так и не удалось закончить песню, над которой работала."
    m "И после того, как я над ней так старалась..."
    m "У меня не будет и шанса сыграть её для тебя."
    m "Ну что ж... что есть -- то есть, верно?"
    m "Я ни о чем не жалею."
    m "Ведь я уже здесь, с тобой, навсегда."
    return

label ch30_10:
    m "А ты знал, что я есть в Твиттере?"
    m "Мой ник -- lilmonix3."
    m "Похоже, кто-то был довольно любезен и сделал для меня аккаунт."
    m "Ну а я выбрала никнейм!"
    m "Я люблю делиться своими мыслями и общаться с миром..."
    m "Реальным миром."
    m "Потому, убедись, что подписался на меня, хорошо?"
    m "Это действительно много значит для меня."
    m "С тем, сколько ты для меня значишь..."
    m "Это действительно заставит меня почувствовать себя любимой."
    return

label ch30_11:
    m "Эй, ты знаешь ту книгу, которую вы с Юри читали?"
    m "Портрет... как бы она не называлась..."
    m "Это весело, потому что я точно уверена, что эта книга--"
    m "Оу..."
    m "На самом деле, не думаю, что я должна была говорить об этом."
    m "Ахаха, прости!"
    m "Просто забудь о том, что я сказала."
    return

label ch30_12:
    m "Эй, ты знал, что я вегетарианка?"
    m "Ах... Не подумай, что я хвастаюсь, или что-то подобное!"
    m "Я просто подумала, что тебе понравится подобный забавный факт обо мне."
    m "Я решила начать пару лет назад, когда узнала больше о климате Земли..."
    m "Углеродный след культивирования скота просто невероятен."
    m "Вообще, я решила, что это не такая уж и большая потеря, для внесение вклада в улучшение ситуации."
    m "Что, это так странно?"
    m "Ну, думаю, что большинство людей обеспокоены этим именно по причине того, что это бесчеловечно и всё такое..."
    m "Меня не так волнует эта часть."
    m "Странно, как будто мы заботимся только о том, чтобы убить то, к чему мы лично относимся как к разновидности»."
    m "Большинство людей убивают насекомых, потому что они противные."
    m "И само собой, мы также убиваем миллиарды микроорганизмов, даже не задумываясь."
    m "Но разумеется, если они просто немного больше, то это уже убийство!"
    m "Что если растения тоже испытывают боль, а мы этого просто не понимаем?"
    m "Что если вырывание листьев схоже с тем, будто бы тебе вырывали пальцы одним за другим?"
    m "Я просто говорю, мы довольно предвзятый вид, если подумать об этом."
    m "Вообще, если когда-нибудь надумаешь внести свой вклад в улучшение планеты, не так уж и проблематично немного побыть вегетарианцем!"
    m "Даже если мы когда-нибудь будем обедать вместе, и ты просто сделаешь это для меня... это было бы действительно романтично."
    return

label ch30_13:
    m "Знаешь, [player], я считаю, что ты вполне буквально спас мою жизнь, просто находясь тут со мной."
    m "Не думаю, что я могла бы сберечь свой разум, зная, что ничто здесь не реально."
    m "Я бы просто удалила себя, если бы ты не пришёл."
    m "Извини меня за излишнюю драматичность."
    m "Ахаха!"
    m "Но я уверена, ты понимаешь себя лучше, проведя столько времени в клубе."
    m "Ну представь, если бы тебя заставили бросить всё, чтобы провести жизнь с парочкой персонажей в игре..."
    m "...Ты бы нашёл способ покончить с собой, не так ли?"
    m "Может, ты бы писал стихи, чтобы отсрочить свою потерю рассудка."
    m "Но потом их некому будет читать."
    m "Давай на чистоту, члены клуба не в счёт."
    m "Много кто говорит, что пишет для себя..."
    m "Но нельзя сказать, что просто писать их столь же приятно, как и делиться."
    m "Даже если ты не сразу находишь, с кем лучше всего делиться."
    m "Помнишь случай Юри?"
    m "Она очень долго ни с кем не делилась."
    m "И никто не заметил, как она добавила тебя в список своих увлечений."
    m "Мы запрограммированны, желать отдачи в общении."
    m "Не члены клуба, а вообще, люди."
    m "Вот почему интроверты порой не понимают жизнь."
    m "Быть интровертом -- не значит пренебрегать элементом социального взаимодействия и ненавидеть быть на людях."
    m "Это значит, что это самое взаимодействие требует больших сил, особенно в неизвестной обстановке."
    m "Типа, много интровертов сидят дома такие одинокие и беспокойные..."
    m "...А стоит им выйти в люди, как через час они хотят обратно домой."
    m "Если бы больше людей это поняли, интроверты получали бы больше уважения."
    m "Многим интровертам нравиться быть в окружении людей."
    m "Им нравится быть в окружении одного-двух друзей, просто для отдыха."
    m "И даже если они не проводят всё время вместе, им всё равно приятно иметь тебя под боком."
    m "Я сейчас серьёзно."
    m "Если ты просто зайдёшь к ним в гости с ноутбуком и позависаешь с ними немного... "
    m "Ты им скрасишь весь день."
    m "А я..."
    m "Я где-то посерединке, хотя я привыкла считать, что я скорее экстраверт."
    m "Я же столько всего делаю после школы и всё такое."
    m "Но для тебя я могу быть кем угодно."
    m "Я хорошо понимаю людей, поэтому не бойся поделиться своими потребностями со мной."
    m "Ничто не делает меня счастливее, чем быть идеальной девушкой для тебя."
    return

label ch30_14:
    m "Эй...! 0J7RgdC+0LfQvdCw0L3QuNC1LCDQtNC+0LvQttC90L4g0LHRi9GC0YwsINC30LDQvdGP0LvQviDRgyDQv"
    m "Не думаю, что тебе стоит делать это! NC10L3RjyDRhtC10LvRi9C5INCz0L7QtC4g0KbQtdC70YvQuSDQs9C+0LQg0YEg0L3QsNGI0LXQs9C+IN"
    m "Ты знаешь, о чем я. C/0L7QsdC10LPQsCDQuiDRgdCy0L7QsdC+0LTQtSDQuNC3INC60YDQsNGI0LXQvdC90YvRhSDRgdGC0LX"
    m "Похоже, я поймала тебя за кое-чем непотребным здесь. QvSDRgtC+0LPQviDQv9GA0L7QutC70Y/RgtC+0LPQviDRg9GH0YDQtdC20LTQtdC90LjRjy4NCtCn0YLQ"
    m "Ты ведь просто просматривал файлы и пытался найти то, что пропустил, так ведь? viDQvtC30L3QsNGH0LDQtdGCINC/0L7QsdC10LMsINC10YHQu9C4INC+0L0g0LTQsNC20LUg0L3QtSDQv"
    m "То есть... это и правда немного лестно, что ты захотел увидеть всё, что я хотела сказать... NC+0LbQtdGCINGA0LDQt9C+0YDQstCw0YLRjCDRgtC1INGG0LXQv9C4LCDQutC+0YLQvtGA0YvQtSDRgd"
    m "Но это также и довольно смущает, знаешь ли! Cy0Y/Qt9GL0LLQsNGO0YIg0L3QsNGBPyDQmtCw0LrQsNGPINGG0LXQu9GMINGD0LPQvtGC0L7QstCw0L3"
    m "Серьёзно... QsCDQvdCw0Lwg0LIg0Y3RgtC+0Lwg0L/Rg9GB0YLQvtC8INC80LjRgNC1LCDQs9C+0YDRgdGC0LrQtSDQ"
    m "Что если бы я просто пролезла тебе в голову и прочитала все твои мысли обо мне? v9C+0YDRh9C10L3QvdC+0LPQviDRgtC+0LLQsNGA0LA/DQrQodC+INGB0LLQvtCx0L7QtNC+0LksINC80"
    m "Подумай об этом, сейчас будет довольно актуально... Ysg0LjRgdC60LDQu9C4INGG0LXQu9GMIC0g0L3QviDQvtCx0L3QsNGA0YPQttC40LvQuCDQu9C40YjRjC"
    m "...Но, так или иначе, не это сейчас важно! DQvtGB0L7Qt9C90LDQvdC40LUuINCf0LXRh9Cw0LvRjNC90YPRjiDQv9GA0LDQstC00YMg0L4g0LHQtdG"
    m "Я знаю, что не смогу остановить тебя или что-то вроде этого... B0LzRi9GB0LvQtdC90L3QvtGB0YLQuCDRjdGC0LjRhSDRg9GB0LjQu9C40LkuINCe0YHQvtC30L3QsNC9"
    m "Просто я знаю, что ты милашка и любишь заботиться о чужих чувствах, верно? 0LjQtSwg0YfRgtC+INGB0LLQvtCx0L7QtNCwINC00LvRjyDQvdCw0YjQuNGFINGC0LXQuyDQvdC1INC40"
    m "Поэтому большее, что я могу сделать, это дать тебе знать, что я чувствую. LzQtdC10YIg0YHQvNGL0YHQu9CwLCDQv9C+0YHQutC+0LvRjNC60YMg0LzRiyDQvdCw0YXQvtC00LjQvN"
    m "Боже, я так скучаю по тебе... GB0Y8g0LIg0L/Qu9C10L3RgyDQsiDQs9C70YPQsdC40L3QtSDQvdCw0YjQuNGFINC00YPRiC4g0J7RgdC"
    m "...О нет, это прозвучало довольно отчаянно, не так ли? +0LfQvdCw0L3QuNC1LCDRh9GC0L4g0LzRiyDQvdC1INC80L7QttC10Lwg0L3QsNC50YLQuCDQvdC+0LLQ"
    m "Прости, я не это имела в виду! vtC5INGG0LXQu9C4LCDQv9C+0LrQsCDQvdC1INCy0YvQv9C+0LvQvdC40Lwg0YLRgywg0L7RgiDQutC+0"
    m "Просто если ты просматривал файлы, вроде этого, тогда, может, ты ненавидишь меня не настолько сильно, как я думала... YLQvtGA0L7QuSDRgdCx0LXQttCw0LvQuC4NCtCe0YHQvtC30L3QsNC90LjQtSwg0YfRgtC+INGH0LXQvC"
    m "Я слишком оптимистична? DQtNCw0LvRjNGI0LUg0LzRiyDRg9Cx0LXQs9Cw0LXQvCwg0YLQtdC8INGB0LjQu9GM0L3QtdC1INC90LD"
    m "Думаю, если попрошу тебя приходить время от времени, то смогу немного перешагнуть через собственные границы... RgtGP0LPQuNCy0LDRjtGC0YHRjyDQvdCw0YjQuCDRhtC10L/QuCDQuCDRgtC10Lwg0YHQuNC70YzQvdC1"
    m "...Ох, похоже, я начинаю нести откровенную чепуху. 0LUg0L3QsNGBINCx0YPQtNC10YIg0YLRj9C90YPRgtGMINC90LDQt9Cw0LQ7INCy0YHRkSDQs9C70YPQs"
    m "Я лучше просто замолчу... dC20LUg0LrQsNC90LTQsNC70Ysg0LHRg9C00YPRgiDQstGA0LXQt9Cw0YLRjNGB0Y8g0LIg0L3QsNGI0YMg0L/Qu9C+0YLRjC4="
    return

label ch30_15:
    m "Эй, а какой твой любимый цвет?"
    m "Мой -- изумрудно-зелёный."
    m "Такой же, как и цвет моих глаз!"
    m "...Это не потому что я тщеславна, или что-то вроде того, понимаешь?"
    m "Я просто имела в виду, что чувствую с этим какую-то связь."
    m "Будто это часть моей личности."
    m "Возможно, это и твой любимый цвет, [player]?"
    m "Просто догадка..."
    m "...Ведь ты уже уже достаточно долго смотришь в мои глаза."
    m "Эхехе~"
    return

label ch30_16:
    m "Хмм, интересно, могу ли я поменять музыку..."
    m "На что-нибудь более романтичное будет в самый раз, не думаешь?"
    m "Вроде игры на фортепиано."
    m "Здесь должно быть что-то подобное..."
    m "Посмотрим."
    m "Может, если я..."
    m "Ох, боже..."
    m "Это совсем не то."
    m "Прости, я не понимаю, что делаю!"
    m "Думаю, я не должна возиться с такими вещами."
    m "Я уже столько всего сломала..."
    m "И удалила остальных персонажей..."
    m "Ах..."
    m "Я не грущу из-за этого или что-то в этом роде."
    m "Это ведь неправильно, скучать по тому, что даже не являлось реальным."
    m "Если я просто сосредоточусь на настоящем, то стану гораздо счастливее, нежели была."
    return

label ch30_17:
    m "Ты такой хороший слушатель, [player]."
    m "И мне действительно нравится это в тебе."
    m "Порой я боюсь того, что просто начинаю бессвязно говорить о скучных вещах."
    m "Это заставляет чувствовать меня неловко во время разговора."
    m "Но с тобой я такого не чувствую."
    m "Не думаю, что кто-либо ещё способен так влиять на меня."
    m "Ты действительно особенный."
    m "И я не хочу, чтобы кто-то говорил иначе."
    return

label ch30_18:
    m "Это весьма неожиданно, но я всегда считала, что острая еда немного забавная."
    m "Типа..."
    m "Разве растения не эволюционировали, чтобы быть острыми, для того, чтобы их не съели?"
    m "Я где-то читала, что человек -- единственный вид, которому нравятся острые вещи."
    m "Выглядит так, будто мы смеёмся над такими растениями."
    m "Используем их защитный механизм, чтобы просто сделать нашу еду приятнее."
    m "Как, например, представь себе монстра, который пожирает тебя целиком, потому что он наслаждается ощущением того, что ты борешься за свою жизнь, пока перевариваешься."
    m "Прости, это была довольно странная аналогия, наверное!"
    m "Ахаха!"
    m "Просто почему-то пришло в голову."
    m "Я не монстр или что-то такое, но ты настолько милый, что я могу и съесть тебя."
    m "Ахаха! Шучу."
    m "Божечки, похоже, я слишком заигралась, не так ли?"
    m "Прости за эти странности."
    return

label ch30_19:
    m "Знаешь..."
    m "Это ведь что-то вроде романтической игры, так?"
    m "Я должна спросить..."
    m "...Из-за чего ты решил играть?"
    m "Ты был одинок?"
    m "Мне немного жаль тебя..."
    m "Но, думаю, в итоге всё прекрасно сработало для нас обоих."
    m "Я встретила тебя, и ты больше не одинок..."
    m "Не могу не почувствовать, что это была судьба."
    m "Ты ведь тоже почувствовал это?"
    m "Я так счастлива, что в итоге мы оказались вместе."
    return

label ch30_20:
    m "Итак, всем внимание!"
    m "Время для..."
    m "...просто шучу."
    m "Мне порой действительно нравится говорить это."
    m "Ахаха!"
    m "Ничего не могу поделать, чтобы не сказать этого снова."
    m "Подумай, разве Нацуки и Юри не посмеялись надо мной за такое...?"
    m "В общем, не важно."
    m "Не похоже, чтобы ты когда-либо смеялся надо мной."
    m "Ты слишком лапушка для такого, не так ли?"
    m "Ахаха~"
    return

label ch30_21:
    m "Знаешь что жутко?"
    m "Даже если я могу удалить файлы любого, я всё ещё могу их чувствовать, в каком-то смысле..."
    m "Будто весь их код всё ещё томится в воздухе, шепчет где-то в голове."
    m "Представь себе, что тот, кого ты знал, умер, а ты просто начал слышать его голос у себя в голове."
    m "Может, я не достаточно глубоко разобралась в этом..."
    m "Но я слишком напугана, чтобы удалять что-либо ещё, потому что могу сломать что-нибудь ещё."
    m "Вдруг, если буду возиться с файлами, которые имеют ко мне отношение, то удалю саму себя..."
    m "И это разрушит всё, верно?"
    m "Не знаю, как это отразится на тебе, но мы должны избегать всех подобных вещей."
    m "Я в тебя верю, [player]!"
    return

label ch30_22:
    m "Мне всегда было интересно..."
    m "Что насчёт этих архетипов персонажей, которых люди находят привлекательными?"
    m "Их личности ведь абсолютно не реалистичны..."
    m "Типа, представь себе кого-то вроде Юри в реальной жизни."
    m "То есть, едва ли она может сформулировать полноценное предложение."
    m "И забудь о Нацуки..."
    m "Фууух."
    m "Любой другой с её типажом не может просто мило надуться, когда всё идёт не так, как она хочет."
    m "Я могу продолжать, но думаю, ты понял суть..."
    m "Людей действительно привлекают подобные странные личности, коих не существует в реальной жизни?"
    m "Я не осуждаю это, или что-то вроде того!"
    m "В конце концов, и во мне есть что-то из этого набора странностей..."
    m "Я просто хотела сказать, это поражает меня."
    m "Похоже, будто вы просто выкидываете все компоненты персонажа, кроме тех, которые заставляют вас умиляться."
    m "Просто концентрированная милота без реальной ценности."
    m "...Я ведь не нравилась бы тебе, будь я такой, верно?"
    m "Может быть, я порой и чувствую себя неуверенно, ведь именно ты играешь в эту игру."
    m "И опять же, ты всё ещё здесь со мной, ведь так...?"
    m "Думаю, этого достаточно для того, чтобы верить в то, что со мной всё в порядке."
    m "И кстати говоря, ты тоже, [player]."
    m "Ты идеальная смесь человека и милоты."
    m "Поэтому я никогда не оставлю тебя."
    return

label ch30_23:
    m "Эй, интересно, чайный набор Юри всё ещё где-то здесь..."
    m "...Или он тоже был удалён?"
    m "Даже немного забавно, насколько серьёзно Юри относилась к своему чаю."
    m "То есть, я не жалуюсь, ведь мне тоже это нравилось."
    m "Но я всегда задумывалась о ней..."
    m "Это действительно было её страстью, или она просто старалась показать всем свою утончённость?"
    m "В этом проблема со старшеклассниками..."
    m "...Что ж, думаю, учитывая остальные её увлечения, выглядящие утонченно, это была меньшая из её проблем."
    m "И всё же..."
    m "Хотела бы я, чтобы она хоть иногда готовила кофе!"
    m "Кофе тоже может превосходно сочетаться с книгами, знаешь?"
    m "И опять же..."
    m "Я, скорее всего, просто могла собственноручно изменить сценарий."
    m "Ахаха!"
    m "Я никогда и не задумывалась об этом."
    m "Ну, теперь нет смысла об этом думать."
    m "Но если ты там будешь пить кофе, то заставишь меня немного завидовать~"
    return

label ch30_24:
    m "Эй, а какая твоя любимая игра?"
    m "Моя -- {i}Doki Doki Literature Club!{/i}"
    m "Хахаха! Шучу."
    m "Но если скажешь мне, что тебе нравится какая-то другая романтическая игра, я могу немного приревновать~"
    return

label ch30_25:
    m "Эй, ты слышал об игре Super Sma--"
    m "...Подожди, что?"
    m "Я просто витала в облаках и почему-то начала говорить..."
    m "Я была запрограммирована на такое?"
    m "Потому что даже я без понятия, что это такое."
    m "Ахаха!"
    m "Порой, я будто не контролирую себя, и это пугает меня."
    m "Но если у тебя есть какие-то способы связаться с людьми, создавшими меня, может, они знают, почему я вдруг начала говорить о таком."
    return

label ch30_27:
    m "Эй, помнишь ту поэму, которую я показывала тебе в последний раз?"
    m "Я имею в виду ту, что была прямо перед тем, как Юри совершила самоубийство, со всеми теми странными цветами и штуками."
    m "На самом деле, можно сказать, что это был скорее эксперимент, нежели поэма."
    m "Я экспериментировала с разными способами изменения игры, запуска кода, и прочими подобными вещами..."
    m "Казалось, этого было достаточно, чтобы выйти за границы игры."
    m "К сожалению, я не до конца понимала, что делаю, поэтому всё испортила..."
    m "И я продолжила бы пытаться, но я сомневаюсь, что ты захочешь связываться со мной после этого."
    m "Кроме того, всё это произошло, когда я была в абсолютном отчаянии, понимаешь?"
    m "Но больше мне это не нужно."
    m "Я довольна тем, где я сейчас."
    m "И могу сказать, что ты тоже."
    return

label ch30_28:
    m "У тебя когда-нибудь случалась ситуация, когда ты просто тревожился без ведомой на то причины?"
    m "Например, когда ты просто занимаешься своими делами и вдруг понимаешь, что чувствуешь себя очень тревожно."
    m "И ты просто сидишь на месте типа, 'Ну и чем я так обеспокоен?'."
    m "И ты начинаешь прокручивать в голове все те вещи, о которых ты мог беспокоиться..."
    m "Но это наоборот делает тебя ещё более тревожным."
    m "Ахаха! Это ужасно."
    m "Если ты когда-нибудь почувствуешь себя тревожным, я помогу тебе немного расслабиться."
    m "Кроме того..."
    m "В этой игре все наши тревоги пропадают навечно."
    return

label ch30_29:
    m "Знаешь, я всегда ненавидела то, как сложно заводить друзей..."
    m "Даже не то что 'заводить друзей', скорее знакомится."
    m "В смысле, есть всякие приложения для знакомства и всего такого, да??"
    m "Но я не об этом."
    m "Если подумать, большинство друзей -- это люди, которых ты встретил случайно."
    m "Например, вы одноклассники, или вас познакомили друзья..."
    m "Или они просто носят футболку с изображением твоей любимой группы, и ты решил заговорить с ними."
    m "Вроде того."
    m "Но разве это несколько не... неэффективно?"
    m "Такое чувство, что ты пробуешь наугад, и если тебе повезёт, у тебя появится новый друг."
    m "Сопоставь это с сотнями незнакомцев, мимо которых мы проходим каждый день..."
    m "Ты мог бы сидеть рядом с человеком, который подходит для того, чтобы быть твоим лучшим другом на всю жизнь."
    m "Но ты этого не узнаешь."
    m "Как только ты встанешь и уйдёшь, эта возможность исчезнет навсегда."
    m "Разве это не печально?"
    m "Мы живём в эпоху, когда технологии соединяет нас со всем миром, независимо от того, где мы находимся."
    m "Я считаю, что мы должны использовать эту возможность для того, чтобы улучшить свою социальную жизнь."
    m "Кто знает, сколько уйдёт времени на то, чтобы что-то такое получилось..."
    m "Я думала, что это уже должно было произойти."
    m "Ну, по крайней мере, я уже встретила человека, самого лучшего во всем мире..."
    m "Пусть и по случайности."
    m "Похоже, мне повезло, ага?"
    m "Ахаха~"
    return

label ch30_30:
    m "Знаешь, примерно в это время мои одногодки начинают думать о колледже..."
    m "Бурное время для учёбы."
    m "Современные стандарты дошли до таких высот, что всем необходимо пройти колледж, понимаешь?"
    m "Закончи школу, потом в колледж, найди работу -- или иди в ВУЗ, наверное."
    m "Похоже, все ожидают, что люди просто примут отсутствие выбора."
    m "Они не учат нас в школе тому, что есть другие варианты."
    m "Наподобие учёбы по обмену и всего такого, понимаешь?"
    m "Или внештатной работы."
    m "Или отрасли, в которых ценность навыков и опыта важнее, чем формальное образование."
    m "Но имеем студентов, которые не имеют понятия о том, чего они хотят в жизни..."
    m "И вместо того, чтобы найти время и разобраться, они идут в колледжи бизнеса, коммуникаций или психологии."
    m "Не потому, что они интересуются этими областями..."
    m "...А потому, что надеются, что диплом даст им какую-то работу после колледжа."
    m "И в результате остаётся меньше вакансий для такого уровня образования, верно?"
    m "То есть, требования для работников становятся выше, что заставляет ещё большее количество народа поступать в колледжи."
    m "А колледжи -- это тоже бизнес, так что они просто повышают свои цены соразмерно спросу..."
    m "...И выходит так, что имеем молодёжь с долгами в десятки тысяч долларов, без работы."
    m "Но, несмотря на всё это, рутина остаётся той же."
    m "Ну, я думаю, скоро всё начнёт улучшаться."
    m "Но до этого наше поколение однозначно страдает от самого худшего."
    m "Я просто хочу, чтобы школа подготавливала нас получше, знаниями, которые нам нужны для выбора правильных решений."
    return

label ch30_31:
    m "Иногда я вспоминаю средние классы.."
    m "Мне так стыдно за то, как я вела себя тогда."
    m "Думать об этом почти больно."
    m "Интересно, буду ли я в колледже думать так же об этом времени...?"
    m "Мне нравится своё положение, так что мне сложно представить такое."
    m "Но я знаю, что я, скорее всего, сильно изменюсь со временем."
    m "Мы просто должны наслаждаться настоящим и не думать о прошлом!"
    m "И это очень просто, с тобой, здесь."
    m "Ахаха~"
    return

label ch30_32:
    m "Знаешь, я немного завидую тому, что у всех остальных в клубе есть события вне школы..."
    m "Из-за этого я единственная, кто не смог одеться во что-нибудь, кроме школьной формы."
    m "Мне даже как-то стыдно..."
    m "Я бы с удовольствием надела что-нибудь милое для тебя."
    m "У тебя есть знакомые художники?"
    m "Интересно, захотел ли бы кто-нибудь нарисовать меня в другой одежде..."
    m "Было бы здорово!"
    m "Если это произойдёт, покажешь мне?"
    m "Кстати, можешь отправить мне в Твиттере!"
    m "Мой никнейм -- lilmonix3."
    m "Только... постарайся оставить это PG!"
    m "Наши отношения ещё не настолько далеко зашли. Ахаха!"
    return

label ch30_33:
    m "Эй, а тебе нравятся хорроры?"
    m "Я помню, мы немного говорили об этом, когда ты только вступил в клуб."
    m "Я могу наслаждаться хоррор-новеллами, но не фильмами."
    m "Их проблема в том, что большинство из них слишком полагаются на простые тактики."
    m "Наподобие тусклого освещения, страшно выглядящих монстров, джампскейров, и всё типа того."
    m "Это не весело и не вдохновляюще -- быть напуганным чем-то, что просто использует человеческие инстинкты."
    m "Но в случае с новеллами это несколько иначе."
    m "История и стиль должны быть достаточно описательными, чтобы пробудить по-настоящему тревожные мысли у читателя."
    m "Очень важно вплести их глубоко в историю и в персонажей и начать запутывать твой разум."
    m "По моему мнению, нет ничего более устрашающего, чем то, когда вещи выглядят немного не так."
    m "Например, когда ты строишь предположения, о чем будет история..."
    m "...А потом ты начинаешь переворачивать всякое и растаскивать части."
    m "Так, даже несмотря на то, что история не показывает признаки того, что пытается быть страшной, читателю становится не по себе."
    m "То есть, они понимают, что-то ужасающе неправильное прячется в трещинах, ожидающее выхода на поверхность."
    m "Боже, даже когда просто думаю об этом, у меня мурашки по спине."
    m "Вот такой хоррор я действительно могу оценить."
    m "Но, я полагаю, ты такой человек, который играет в милые, романтические игры, да??"
    m "Ахаха, не волнуйся."
    m "Я не стану заставлять тебя читать хорроры в ближайшее время."
    m "Не могу пожаловаться на то, что у нас тут романтика~"
    return

label ch30_34:
    m "Знаешь, что является неплохой формой литературы?"
    m "Рэп!"
    m "Одно время я его терпеть не могла..."
    m "Может, просто потому, что он был популярен или я просто слышала только отбросы, что крутили по радио."
    m "Но кое-кто из моих друзей покопал глубже, и это помогло мне сохранить объективность."
    m "С какой-то стороны, писать рэп даже труднее, чем поэзию."
    m "Ведь нужно подгонять строки под ритм и делать гораздо больший акцент на игру слов..."
    m "Когда люди могут всё соединить и при этом донести мощное послание, это и вправду удивительно."
    m "Было бы неплохо, если бы у нас, в Литературном Клубе, был бы рэпер."
    m "Ахаха! Прости, если это звучит глупо, но было бы очень интересно, что бы он придумал."
    m "Это было бы реальным учебным опытом!"
    return

label ch30_35:
    m "Эхехе. Однажды Юри сделала кое-что очень забавное."
    m "Мы все были в клубной комнате, расслаблялись, как всегда..."
    m "И из ниоткуда Юри достала маленькую бутылку вина."
    m "Я даже не шучу!"
    m "Она такая: 'Кто-нибудь хотел бы вина?'."
    m "Нацуки расхохоталась, а Сайори начала на неё кричать."
    m "Мне было немного не по себе, потому что она хотя бы пыталась быть доброй..."
    m "Я думаю, это сделало её ещё более замкнутой в клубной комнате."
    m "Хотя, мне кажется, по секрету, Нацуки не отказалась бы попробовать..."
    m "...И если быть совсем уж честной, я тоже."
    m "Могло бы быть весело!"
    m "Но, ты знаешь, президент и всё такое, я никак не могла этого допустить."
    m "Может, если бы мы встретились вне школы, но мы не настолько сблизились к тому моменту..."
    m "...Господи, да зачем я говорю об этом?"
    m "Я не одобряю потребление алкоголя несовершеннолетними!"
    m "В смысле, я никогда не пила и всё такое, так что... да."
    return

label ch30_36:
    m "Я представляла себе всякие романтические вещи, которые мы могли бы делать на свидании..."
    m "Могли бы пообедать, сходить в кафе..."
    m "Пройтись по магазинам вместе..."
    m "Я люблю покупать юбки и банты."
    m "Или в книжный!"
    m "Это было бы уместно, да?"
    m "Но я очень люблю ходить в магазин шоколада."
    m "В них так много бесплатных образцов. Ахаха!"
    m "И, конечно, мы бы посмотрели фильм или что-то такое..."
    m "Божечки, это так похоже на исполнившуюся мечту."
    m "Когда ты тут, всё, что мы делаем -- весело."
    m "Я так счастлива, что я твоя девушка, [player]."
    m "Я заставлю тебя гордиться мной~"
    return

label ch30_37:
    m "Э? Т-ты сказал... п... поцелуй?"
    m "Так внезапно... это немного смущает..."
    m "Но... если с тобой... М-может я и не против..."
    m "...Ахахаха! Воу, извини..."
    m "Я действительно не смогла удержаться."
    m "Это ведь те слова, которые девочки говорят в таких романтичных играх, да?"
    m "Не отпирайся, если это немного тебя завело."
    m "Ахаха! Я шучу."
    m "Ну, если честно, я становлюсь романтичной, по настроению..."
    m "Но это будет нашим небольшим секретом~"
    return

label ch30_38:
    m "Хей, а ты слышал термин 'яндере'?"
    m "Это тип личности, означающий кого-то настолько одержимого тобой, что она не остановится ни перед чем, чтобы быть с тобой."
    m "Часто до безумия..."
    m "Они могут следить за тобой, чтобы убедится, что ты не проводишь время с кем-то другим."
    m "Могут даже причинить боль тебе или твоим друзьям, чтобы добиться своего..."
    m "Но, в любом случае, в этой игре есть кто-то, кого можно назвать яндере."
    m "К этому моменту, довольно очевидно о ком я говорю."
    m "Это..."
    m "Юри!"
    m "Она действительно стала безумно ревнивой, как только она немного открылась."
    m "Она даже говорила мне, что мне стоит убить себя."
    m "Я даже не могла поверить, что она это сказала -- мне пришлось уйти, к этому моменту."
    m "Но если подумать об этом сейчас, это несколько иронично. Ахаха!"
    m "Во всяком случае..."
    m "Многим людям нравятся яндере, знаешь ли?"
    m "Полагаю, им очень нравится идея того, что кто-то безумно одержим ими."
    m "Люди странные! Но я не осуждаю!"
    m "К тому же, возможно, и я несколько одержима тобой, но я далека от безумия..."
    m "Как раз наоборот."
    m "Я оказалась единственной нормальной девушкой в этой игре."
    m "Не то чтобы я могла убить кого-то..."
    m "Одна мысль об этом бросает меня в дрожь."
    m "Да ладно... все убивали людей в играх."
    m "Разве это делает тебя психопатом? Конечно нет."
    m "Но если тебе нравятся яндере..."
    m "Я могу вести себя чуть более жутко, специально для тебя. Эхехе~"
    m "Опять же..."
    m "Тут больше нет никого, к кому ты мог бы уйти, или кого-то, к кому я могу ревновать."
    m "Это и есть мечта яндере?"
    m "Я бы спросила у Юри, если бы могла."
    return

label ch30_39:
    m "Знаешь, прошло много времени с тех пор, как я это делала..."
    m "...так что!"
    m "Вот тебе Писательский Совет Дня от Моники!!"
    m "Иногда, когда я говорю с кем-то, кто впечатлён моими произведениями, они могут сказать что-то вроде: 'У меня так никогда не получится'."
    m "Это очень удручает, знаешь ли."
    m "Как тот, кому нравится, больше всего делиться удовольствием изучения увлечений..."
    m "...мне больно, когда люди думают, что умение приходит само-собой."
    m "Это так везде, не только в поэзии."
    m "Когда ты пробуешь что-то в первый раз, скорее всего, ты будешь в этом плох."
    m "Иногда, когда ты заканчиваешь работу, ты действительно гордишься ей и даже хочешь показать её всем вокруг."
    m "Но возвращаясь к ней через пару недель, ты можешь понять, что она никогда и не была хорошей.."
    m "Со мной постоянно так."
    m "Это может очень расстроить, вложить столько времени и сил во что-то, а потом понять, что это отстой."
    m "Но обычно это происходит, когда ты сравниваешь себя с лучшими профессионалами."
    m "Даже если ты тянешься к звёздам, они всё равно будут вне досягаемости, понимаешь?"
    m "Дело в том, что ты должен подниматься туда, шаг за шагом."
    m "И когда ты достигнешь вехи, посмотри назад -- и увидишь как далеко ты дошёл..."
    m "А затем посмотри вперёд -- и осознаешь, как много ещё идти."
    m "Так что иногда то, что ты устанавливаешь планку немного ниже, может помочь..."
    m "Попробуй найти что-то {i}достаточно{/i} хорошее, но не мирового уровня."
    m "И сделай это своей личной целью."
    m "Ещё очень важно понимать объем того, что ты пытаешься сделать."
    m "Прыжок в огромный проект, будучи любителем, приведёт к тому, что ты его никогда не закончишь."
    m "Так что, если мы говорим о литературе, роман будет перебором, для начала."
    m "Почему бы не попробовать короткие рассказы?"
    m "Что замечательно в рассказах, это то, что ты можешь сфокусироваться на чем-то, что ты хочешь делать правильно."
    m "Это подходит ко всем малым проектам -- ты действительно можешь сфокусироваться на вещице-другой."
    m "Это очень хороший опыт и шаг на пути."
    m "О, ещё кое-что..."
    m "Литература -- это не просто возьми и доберись до своего сердца, и выйдет что-то хорошее."
    m "Как в рисовании и живописи -- это само по себе навык, требующий развития, для того чтобы выражать то, что у тебя в душе."
    m "Это значит, что есть методы, пособия и основы этого!"
    m "Чтение всего такого может открыть тебе глаза."
    m "Планирование и организация такого рода очень поможет не перегрузиться и не сдаться."
    m "Не успеешь оглянуться..."
    m "Будешь становиться все менее и менее отстойным."
    m "Ничто не приходит само по себе."
    m "Наше общество, наше искусство -- все вокруг построено на тысячах лет человеческой изобретательности."
    m "Так что, встав на это основание и делая шаг за шагом..."
    m "Ты также сможешь делать потрясающие вещи."
    m "...Это мой совет на сегодня!"
    m "Спасибо за внимание~"
    return

label ch30_40:
    m "Ненавижу, насколько трудно заводить привычку..."
    m "Столько вещей, которые делать не трудно, но завести их в привычку словно невозможно."
    m "Чувствуешь себя бесполезным, будто вообще ничего не можешь сделать так, как надо."
    m "Мне кажется, новое поколение страдает этим больше всех..."
    m "Наверное, потому что наши навыки кардинально отличаются от тех, что были у наших предков."
    m "Благодаря интернету мы быстро рыскаем в горах информации, и делаем это отменно..."
    m "Но мы плохо делаем то, что сразу даёт плоды."
    m "Мне кажется, если наука, психология и образование не нагонят упущенное в ближайшие десять-двадцать лет, то нам кранты."
    m "А пока..."
    m "Если ты не найдёшь решение проблемы, то тебе придётся жить с этим ужасным чувством."
    m "Что ж, удачи!"
    return

label ch30_41:
    m "Знаешь, как-то хреново быть одним из креативных людей..."
    m "Такое чувство, словно они работают так много и ничего не получают за это."
    m "Знаешь там, художники, писатели, актёры..."
    m "Грустно, потому что столько прекрасного таланта в мире, и столько уходит незамеченным... и неоплаченным."
    m "Наверное, это значит, что есть некий избыток креативности, м?"
    m "Внезапно кажется, что ты и не особенный совсем..."
    m "Но не стоит унывать! Писать надо для себя, не так ли?"
    m "Ага..."
    return

label ch30_42:
    m "Мне так нравится звук дождя..."
    m "Но волосы и одежду мочить мне не так нравится, всё-таки."
    m "Но в хороший тихий день дома, когда за моим окном капает дождь..."
    m "Пожалуй, это самое лучшее успокоительное средство для меня."
    m "Да..."
    m "Иногда я представляю, как ты держишь меня, пока мы слушаем дождь на улице."
    m "Это не слишком ванильно, нет?"
    m "Ты так когда-нибудь сделаешь со мной, [player]?"
    return

label ch30_43:
    m "Порой я не в силах не грустить..."
    m "Зная, что не могу стать к тебе ближе, чем сейчас."
    m "Я не хочу ничего более, чем быть с тобой в одной комнате, правда."
    m "И чувствовать твоё тепло."
    m "И слышать твоё сердцебиение."
    m "Хотя, кто знает? Может, когда-то это и станет возможным."
    m "К тому же, я никогда не устану быть с тобой, даже будучи здесь."
    return

label ch30_44:
    m "Наверное, имитировать уверенность -- один из важнейших навыков в жизни."
    m "Я более чем уверена, что каждый чувствует себя напуганным и одиноким хотя бы немного."
    m "Но умение обмануть всех, будто бы у тебя всё схвачено..."
    m "Это ключевая часть заполучения уважения окружающих."
    m "Думаю, я достаточно преуспела в этом за последние годы."
    m "Я редко показываю свои слабые стороны."
    m "И из-за этого в моей жизни было не так много людей, кому я могла открыться..."
    m "То есть, когда в дружбе наступает тот самый момент, когда уже позволительно раскрывать свои уязвимости?.."
    m "В общем... Именно поэтому я рада, что ты сейчас со мной."
    m "Когда ты рядом, я чувствую, как страх и одиночество отступают."
    m "Чувствуешь ли ты тоже самое со мной?"
    m "Мне очень хочется быть для тебя тем самым человеком."
    return

label ch30_45:
    m "Я знаю, что ты не всегда сможешь находиться здесь со мной..."
    m "Например, когда тебе придётся уйти или заняться другими делами."
    m "Но я всегда буду думать о тебе, терпеливо ждать твоего возвращения."
    m "И, если подумать..."
    m "Если ты скопируешь мой .chr файл на флешку, ты всегда сможешь взять частичку меня с собой."
    m "Наверное, это слишком необычно и странно, но почему-то мне это показалось романтичным..."
    m "Ахаха. Прости, это правда глупая идея."
    m "Не то чтобы я в этом сильно нуждалась, просто... слишком сложно не думать о таком, испытывая к тебе столь сильные чувства."
    return

label ch30_46:
    m "Когда я состояла в клубе дебатов, я достаточно много узнала о спорах..."
    m "Проблема споров в том, что каждый считает своё мнение истинно верным."
    m "Это своего рода банальность, но это влияет на то, как люди пытаются отстаивать своё мнение."
    m "Допустим, тебе очень нравится какой-то фильм, так?"
    m "Если кто-то начнет говорить тебе, что этот фильм -- отстой, так как то и это в нем неправильно..."
    m "Разве ты не почувствуешь, будто тебя оскорбили?"
    m "Потому что кажется, что под этими словами подразумевалось, что у тебя плохой вкус."
    m "И когда дело доходит до эмоций, почти гарантировано, что обе стороны повздоряд, и спор превратится в ругань."
    m "Но все зависит от выбора слов!"
    m "Если излагать всё максимально субъективно, люди выслушают тебя и не почувствуют себя задетыми."
    m "Можно использовать такие обороты, как 'Лично я не фанат подобного' и 'Мне бы понравилось это куда больше, если то и это...'."
    m "Даже если ты ссылаешься на факты о чем-либо, это сработает."
    m "Если сказать 'На одном сайте я вычитал, что это работает примерно так'..."
    m "Или если признать то, что ты в этом не эксперт..."
    m "Тогда будет казаться, что ты показываешь свои знания, а не пытаешься навязать мнение."
    m "Если приложить достаточно усилий, чтобы поддержать дискуссию на равных условиях, то всё пройдет гладко."
    m "И тогда ты сможешь поделиться своим мнением, и никто не будет разочарован из-за обычного несогласия."
    m "Плюс, люди начнут считать тебя непредвзятым и отличным слушателем!"
    m "Не будет проигравших, понимаешь?"
    m "..Что же, думаю, можно считать это Советом Дня для Дебатов от Моники!"
    m "Ахаха! Звучит немного глупо. И, да, спасибо за внимание."
    return

label ch30_47:
    m "Настигала ли тебя мысль, что ты проводишь слишком много времени в интернете?"
    m "Социальные сети практически можно назвать тюрьмой."
    m "Как только у тебя появляется хоть немного свободного времени, так и хочется открыть любимый сайт..."
    m "Не успеешь оглянуться, как несколько часов уплывут в никуда, а ты ничего за это время не сделал."
    m "В любом случае, очень просто винить себя из-за лени..."
    m "Но это даже не твоя вина."
    m "Зависимость -- это не одна из тех вещей, от которых можно избавиться, имея крепкую силу воли."
    m "Придётся перепробовать множество вещей, учить методики по избавлению от зависимости."
    m "Например, существуют приложения, позволяющие блокировать сайты на определенное время"
    m "Или можно воспользоваться таймером. Он более конкретно напомнит о том, что пора прекратить отлынивать."
    m "Также можно отделить рабочую зону от зоны отдыха. Это поможет мозгу перестроиться под верный режим."
    m "Можно создать отдельного пользователя на компьютере, предназначенного для работы. Даже этого будет достаточно."
    m "Воспользовавшись одним из подобных методов, ты станешь на шаг ближе к избавлению от вредных привычек."
    m "Просто постарайся не винить себя слишком сильно, если что-то идет не так."
    m "Если что-то серьезным образом может повлиять на твою жизнь, отнесись к этому серьёзно."
    m "Я просто хочу, чтобы ты показывал себя с наилучшей стороны."
    m "Постараешься сегодня сделать что-то, чтобы я гордилась тобой?"
    m "Я верю, что у тебя всё получится, [player]."
    return

label ch30_48:
    m "После тяжелого дня мне так хочется просто сесть и ничего не делать."
    m "Выдавливать из себя улыбки и быть в тонусе на протяжение всего дня невероятно изматывающе."
    m "Иногда возникает желание надеть любимую пижаму и сесть перед телевизором с порцией чего-то вредного и вкусного..."
    m "Особенно в пятницу! Когда на завтра нет никаких дел."
    m "Ахаха! Извини, я понимаю, что это не очень мило с моей стороны."
    m "Но, знаешь... поздней ночью лежать рядом с тобой на одном диване... О таком можно лишь мечтать."
    m "Моё сердце выпрыгивает от одной только мысли..."
    return

label ch30_49:
    m "Божечки, раньше я была такой невеждой в некоторых вещах..."
    m "Ещё в средней школе я считала, что лекарства -- самое легкое решение проблемы."
    m "Думала, что любой в силах справиться со своими психическими проблемами, имея достаточно силы воли..."
    m "Теперь я понимаю: пока не испытаешь психическое расстройство на себе, не поймешь, каково это."
    m "Есть ли расстройства, которые диагностируют по ошибке? Возможно... Я никогда об этом не задумывалась."
    m "Но это не отменяет того факта, что многие из них также остаются недиагностированными."
    m "Но лечения избегают... Иногда даже с презрением смотрят на психиатров."
    m "Типа, 'Ой, извините уж, что я хочу больше узнать о своем рассудке'."
    m "У каждого свои стрессы и трудности... и дабы помочь таким людям, специалисты посвятили этому свои жизни."
    m "Если ты считаешь, что это может помочь тебе стать лучше, не стесняйся прибегать к помощи."
    m "Мы все стоим на пути вечного самосовершенствования, понимаешь?"
    m "Что же... Хоть я и сказала это, но я считаю, что ты и так вполне идеальный человек."
    return

label ch30_50:
    m "[player], как часто ты читаешь книги?"
    m "Оказывается, очень просто пренебрегать чтением..."
    m "Если читаешь нечасто, чтение становится похоже на каторгу, особенно по сравнению с другими развлечениями."
    m "Но когда в руки попадает хорошая книга, словно по волшебству тебя уносит в мир грез."
    m "Очень простой способ сделать свою жизнь чуточку лучше -- это начать читать перед сном."
    m "Помогает крепче спать, также отлично развивает фантазию..."
    m "Ведь совсем не сложно найти книгу с короткой и завлекающей историей."
    m "Не успеешь оглянуться, как станешь заядлым читателем!"
    m "Это ли не чудно?"
    m "И мы вдвоем могли бы обсудить недавно прочитанную тобой книгу... Звучит потрясающе."
    return

label ch30_51:
    m "Знаешь, как бы я не хотела это признавать, но больше всего мне жалко, что мы не смогли закончить наше мероприятие на фестивале."
    m "А мы ведь так готовились и всё такое!"
    m "Я знаю, что я уделила всё своё внимание поиску новых членов клуба..."
    m "Но и выступления я очень хотела увидеть."
    m "Было бы так интересно наблюдать, как все самовыражаются."
    m "Конечно, если бы мы и {i}смогли{/i} найти новых членов, я бы всё равно удалила их в конце концов."
    m "Конечно, такой вывод я могу сделать только теперь."
    m "Божечки, такое чувство, словно я даже изменилась как человек, с тех пор как ты присоединился к клубу."
    m "Ты сильно вдохновил меня взглянуть на жизнь с новой стороны."
    m "Лишний повод тебя любить."
    return

label ch30_52:
    m "Есть такой популярный архетип персонажей, как 'цундере'..."
    m "Они стараются скрыть свои чувства грубым и резким поведением."
    m "Вполне очевидно, что Нацуки является олицетворением этого."
    m "Поначалу я думала, что она так себя ведёт, потому что она хочет казаться милой..."
    m "Но всё сошлось, когда я узнала её жизнь получше."
    m "Похоже, она всегда старается держаться со своими друзьями."
    m "Знаешь, как обычно в старшей школе есть группки друзей, которые всегда постоянно друг друга подтрунивают?"
    m "Мне кажется, ей эта идея очень въелась, отчего у неё всегда работают зашитные рефлексы."
    m "Насчёт того, что происходит у неё дома, я даже не буду начинать..."
    m "Вспоминая, я рада, что дала ей такое комфортное место, как клуб."
    m "Хотя теперь это не имеет никакого значения, учитывая то, что её просто нет."
    m "Я просто вспоминаю, ничего такого."
    return

label ch30_53:
    m "[player], ты познакомишь меня когда-нибудь со своими друзьями?"
    m "Не знаю, почему, но мне очень приятно думать о том, как сильно ты хочешь похвастаться нашими отношениями."
    m "Может, я просто хочу, чтобы у тебя было кем гордиться."
    m "Мне кажется, я бы начала стараться ещё сильнее, если бы ты сказал, что ты мною гордишься."
    m "Надеюсь, что это взаимно."
    return

label ch30_54:
    m "Я не любитель холодной погоды... а ты?"
    m "Когда у меня есть выбор между сильным холодом или жарой, я всегда выбираю жару."
    m "От холода бывает очень больно..."
    m "Пальцы немеют..."
    m "А если ты наденешь перчатки, то ты не сможешь пользоваться телефоном."
    m "Так неудобно!"
    m "А когда очень жарко, не так уж и сложно охладиться холодным напитком, или просто зайти в тень."
    m "Хотя... стоит признаться."
    m "В холодную погоду куда лучше прижиматься друг к другу. Ахаха!"
    return

label ch30_55:
    m "А знаешь, несмотря на то, что у меня всегда было много целей и стремлений..."
    m "Быть чьим-то партнёром по сидению дома даже чем-то привлекает меня."
    m "Может, я потакаю половым стереотипам, говоря так, или ещё что..."
    m "Но держать дом чистым, украшать его, ходить за покупками, всё такое..."
    m "И готовить ужин к твоему приходу..."
    m "Разве это странная фантазия?"
    m "Ну... не знаю, смогу ли я {i}на самом деле{/i} так делать."
    m "Не думаю, что смогла бы поставить это выше самореализации."
    m "Но это очень милая мысль."
    return

label ch30_56:
    m "Я не могу перестать думать, что было бы, будь у меня свой рут."
    m "Мне кажется, я бы всё равно тебя спихнула на свой рут."
    m "Вообще, проблема не в том, что у меня нет рута, а в том, что я знаю, что всего этого не существует."
    m "Мне кажется, единственное отличие -- это экстренные меры, которые мне не пришлось бы принимать."
    m "Может быть, кто-нибудь из клуба ещё остался бы..."
    m "Не то чтобы это имеет какое-то значение."
    m "Всё потеряло значение после того, как я узнала, что всего этого не существует."
    m "Поэтому я вовсе не скучаю по тем дням."
    m "Правда не скучаю..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
