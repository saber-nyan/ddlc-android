label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "И снова привет, [player]!"
    m "Рада видеть, что ты не сбежал от нас. Ха-ха-ха!"
    mc "Не-а, не волнуйся."
    mc "Занятие для меня, конечно, непривычное, но я стараюсь держать слово."
    show monika zorder 1 at thide
    hide monika
    "Ну, я вернулся в литературный клуб."
    "Я зашёл последним, все остальные уже были в сборе."
    show yuri glitch2 zorder 2 at t32
    y "Спасибо, что держишь слово, [player]."
    y 1a "Надеюсь, что ты не сковываешь себя этим обязательством."
    y 1u "Заставляем тебя погрузиться в литературу, когда ты не привык читать..."
    show natsuki glitch1 zorder 2 at i33
    n "Да ты чё! Нефиг ему сачковать."
    n 4e "Тебя же Моника сюда притащила."
    n "Я не в курсе, ты собрался просто тусоваться сюда приходить, или чё..."
    n "Но если не будешь относиться к нам всерьёз, то до конца не доживёшь."
    show monika 2b onlayer front at l41
    m "Нацуки, у тебя слишком длинный язык для той, кто хранит свою коллекцию манги в помещении клуба."
    n 4o "М-М-М!.."
    show monika onlayer front at lhide
    hide monika onlayer front
    "Промычала Нацуки, разрываясь между словами \"Моника\" и \"Манга\"."
    show natsuki at h33
    n 1v "Манга — это литература!!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Огрызнулась напоследок Нацуки и плюхнулась на своё место."
    show yuri 2s zorder 2 at t11
    y "Прости, [player]..."
    y "Мы постараемся сделать так, чтобы тебе было комфортно, хорошо?"
    show yuri 2g
    "Юри стрельнула разочарованным взглядом в Нацуки."
    y 1a "Эм, к слову..."
    y "Теперь, когда ты в клубе и всё такое..."
    y "...Возможно, ты захочешь выбрать себе какую-то книгу?"
    mc "Ну..."
    mc "Я в любом случае не смогу отказаться."
    mc "Как ты и сказала, теперь я в клубе."
    mc "Поэтому, раз уж ты спросила, мне кажется, будет правильно заняться этим."
    y 4b "П-Погоди..."
    y "Я не это имела в виду!"
    y "Т-ты..."
    y "Если ты не хочешь, тогда забудь о моих словах..."
    mc "О... Нет, это не так, Юри."
    mc "Я хочу постараться стать частью клуба."
    mc "Так что, пусть я и не особо часто читаю, я был бы рад взять книгу, если ты этого хочешь."
    y 3t "Т-Ты уверен?.."
    y "Я просто чувствую, что..."
    y 3u "...Ну как вице-президент и всё такое..."
    y "...Что должна помочь тебе начать с того, что тебе может понравиться."
    "Юри потянулась за своей сумкой и достала оттуда книгу."
    y 1s "Я не хотела, чтобы ты чувствовал себя обделённым..."
    y "Поэтому взяла книгу, которая предположительно могла бы тебе понравиться."
    y "Она короткая, так что должна удержать твоё внимание, даже если ты не привык к чтению."
    y "И мы могли бы, ну... знаешь..."
    show yuri at sink
    y 4b "Обсудить её... Если захочешь..."
    "Э-Это..."
    "Откуда в ней столько естественного очарования?"
    "Она даже выбрала книгу, которая, по её мнению, мне понравится, несмотря на то, что я мало читаю..."
    mc "Спасибо, Юри! Я обязательно это прочту!"
    "Я с энтузиазмом принял книгу."
    show yuri 2m zorder 2 at t11
    y "Фух..."
    y 2a "Ну, ты можешь и не торопиться."
    y "Я подожду, пока ты сложишь мнение о ней."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Все расселись. Я ожидал, что теперь-то Моника раздаст нам какие-то плановые задания."
    "Но она, похоже, и не собиралась."
    "Юри уже успела уткнуться в книгу."
    "Я не мог не заметить её нетерпение, как будто она только и ждала этого момента."
    "А Нацуки тем временем закопалась в кладовку."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_19

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Фух..."
    "Вроде бы всё."
    "Я оглядел комнату."
    "Это было более напряжно, чем я ожидал."
    "Такое чувство, будто все оценивали мои посредственные писательские способности..."
    "Пускай мне не сказали ни одного плохого слова, но тем не менее мои стихи и близко не стояли с их."
    "Это ведь всё-таки литературный клуб."
    "Я вздохнул."
    "В конце концов, сам на это подписался."
    "На другом конце класса Моника что-то писала в своём блокноте."
    "Мой взгляд упал на Юри и Нацуки."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Они робко обмениваются своими листиками, делясь стихами."
    show yuri 2i zorder 2 at t21
    "Пока они одновременно читали, я наблюдал за изменением выражений их лиц."
    "Нацуки раздосадованно поморщилась."
    "А Юри печально улыбнулась."
    show natsuki zorder 3 at f22
    n 1q "{i}(Что с этим стилем?...){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "А?"
    y "Эм... Ты что-то сказала?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Ой, ничего."
    "Нацуки равнодушно протянула руку и оставила стихотворение на парте."
    n "Ты бы на моём месте сказала, что это довольно вычурно."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ох... Спасибо..."
    y "Твоё тоже... милое..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Милое?"
    n 1h "Ты чё, ваще не вникала в символизм?"
    n "Очевидно же, что оно о безнадёге."
    n "Как это может быть милым?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "Я... Я поняла!"
    y "Я просто имела в виду..."
    y 3h "Стиль, что ли..."
    y "Я пыталась сказать что-нибудь приятное..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Чё?"
    n 4w "Хочешь сказать, тебе офигеть как сложно придумать приятные слова?"
    n "Спасибо, конечно, но это было нифига не приятно!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Эм..."
    y "Ну, у меня есть пара советов..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Пф."
    n "Если бы мне нужны были советы, я бы спросила у тех, кому по-настоящему понравилось."
    n "А такие люди, кстати, {i}есть{/i}."
    n 5e "Монике вот понравилось."
    n "И [player] тоже оценил!"
    n "Так, что, пожалуй, я сама выдам тебе парочку советов."
    n "Во-первых..."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Извини..."
    y "Я ценю твоё предложение, но я посвятила формированию собственного авторского стиля достаточно времени."
    y 2h "Я не собираюсь в нём что-то менять в ближайшее время, по крайней мере, пока не встречу новый источник вдохновения."
    y "А я пока его не нашла."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Н-н...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "И к твоему сведению, [player] оценил и мой стих тоже."
    y "Он даже сказал, что восхищён."
    stop music fadeout 1.0
    "Нацуки внезапно встала."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "О..."
    n "А я и не подозревала, что ты так выложилась ради того, чтобы произвести впечатление на нашего новичка, Юри."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "Что-о-о?!"
    y "Я совсем не!.."
    y 1o "Т-т..."
    y "Ты... Ты просто..."
    "Юри тоже вскочила."
    y 2r "По-моему, ты просто завидуешь, что [player] ценит мои советы больше, чем твои!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Ха! А с чего ты взяла, что он не ценит {i}мои{/i} советы больше?"
    n "Дофига самоуверенная?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "Я!.."
    y "Нет..."
    y "Если бы я была самоуверенной..."
    y 1r "...Я бы из кожи вон лезла, чтобы любое моё действие казалось миленьким!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Т-т-т-т-т-ты!.."
    n "Так, знаешь что?!"
    n "Это не мои сиськи волшебным образом раздуваются, как только объявляется [player]!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "Н-Нацуки!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Эм, Нацуки, это уже немного..."
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "Не лезь!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Срываться на других из-за собственных комплексов..."
    y "Ты, Нацуки, выглядишь, как дитя, и ведёшь себя так же по-детски."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}Я?{/i} Кто бы говорил, сука пафосная, миром непонятая!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Пафосная?.."
    y 2r "Прости, что мой образ жизни недоступен для понимания в твоём психологическом возрасте!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "Видишь?"
    n "Ты только что со мной согласилась!"
    n 4e "Большинство людей, чтоб ты знала, перерастают это ещё в средней школе."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Если хочешь что-то доказать, перестань оскорблять людей своими грязными словами!"
    y "Думаешь, сможешь затмить свою ядовитую натуру, просто нося маску милой девочки?"
    y 1k "Единственная вещь, которая в тебе умиляет — это твои бессмысленные потуги."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Вау, полегче, Юри, а то дойдёшь до крайностей, и об краешек-то порежешься."
    n "О, прости, я забыла... Ты уже это сделала, да?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "Т-ты только что обвинила меня в том, что я режу себя???"
    y 3r "Что за херня у тебя в голове?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "О да, продолжай!"
    n "Пусть [player] услышит твои настоящие мысли!"
    n "Уверена, после этого его мнение о тебе упадёт ниже плинтуса!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "О-ох!.."
    show yuri zorder 2 at t21
    "Юри резко повернулась ко мне, будто только что заметив, что я стою рядом."
    show yuri zorder 3 at f21
    y 2n "[player]!.."
    y "Она... Она просто пытается выставить меня в плохом свете!.."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "Неправда!"
    n "Она первая начала!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}Каким боком меня сюда приплели?!{/cps}{nw}"
    "{cps=*2} вообще не особо разбираюсь в писательстве...{/cps}{nw}"
    "{cps=*2}Но с кем бы я ни согласился, это добавит мне авторитета!{/cps}{nw}"
    "{cps=*2}И, конечно, это будет!..{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Нацуки.":
                jump menu_click
            "Юри.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "..."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Эм..."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Эй, [player]..."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Может,\nвыйдем\nненадолго?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Ладно?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Ты извини за это..."
    m "Им правда не стоило пытаться втянуть в это тебя."
    m 1e "Нам, наверное, лучше пока не вмешиваться..."
    m "Вернёмся, когда они перестанут кричать друг на друга."
    m 5 "А-ха-ха..."
    m "Да уж, что же я за президент?"
    m 1m "Я даже не могу справиться с собственными товарищами по клубу..."
    m "Как мне иногда хочется быть немного более напористой."
    m "Но я никогда не умела держать других под контролем..."
    m 1e "Ты понимаешь, так ведь?"
    m "В общем..."
    m 1a "Если это заставит тебя проводить меньше времени с другими, тогда всё хорошо."
    m 1j "Я с радостью займу это твоё время собой..."
    show monika zorder 1 at thide
    hide monika
    "Нацуки внезапно выскочила из класса."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "И быстро побежала прочь."
    show monika 1l zorder 2 at t11
    m "О боже..."
    m "...Ну, видимо, они закончили."
    scene bg club_day2
    with wipeleft_scene
    y "Я не хотела..."
    y "Я не хотела..."
    y "Я не хотела..."
    "Юри сидела на парте, обхватив голову руками, и ритмично раскачивалась."
    mc "Юри?.."
    show yuri 4d zorder 2 at t11
    y "Я не хотела!!!"
    mc "Я... я верю тебе..."
    "Даже не догадываюсь, что Юри могла сказать Нацуки."
    "Или сделать."
    y "[player]."
    y "Пожалуйста, не злись на меня."
    y "Пожалуйста!"
    y "Я не такая!"
    y "Просто со мной сегодня что-то не так..."
    show monika 1d zorder 3 at f31
    m "Всё в порядке, Юри."
    m "Мы знаем, что ты не хотела."
    m 1j "Кроме того, я уверена, что Нацуки уже завтра забудет об этом."
    m 1a "Напрочь."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "В общем, встреча окончена, можете расходиться по домам, если хотите."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Юри посмотрела на меня так, будто хотела что-то сказать."
    "Но при этом не переставала поглядывать на Монику."
    show yuri zorder 3 at f32
    y 2v "Т-Ты можешь идти первая, Моника..."
    y "Я ненадолго останусь."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "Я президент, поэтому должна уходить последней."
    m "Подожду, пока ты закончишь."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Ну... Я вице-президент, так что..."
    y "Пожалуйста, позволь мне сегодня взять ответственность на себя."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "Звучит так, будто ты меня выгоняешь, Юри."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "Э... Это не так!"
    y 3o "Это не так..."
    y 3n "Я просто..."
    y 3q "[player]... Он... У меня... У меня не было возможности обсудить с ним свою книгу."
    y "И мне будет... неловко, если ты станешь слушать..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Вздох*{/i}"
    m 1d "Полагаю, у меня нет выбора, так ведь?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "П-Прошу прощения за причинённые неудобства..."
    $ gtext = glitchtext(20)
    y 1s "Но я очень ценю твоё понима{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "Но я очень ценю твоё понима{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
