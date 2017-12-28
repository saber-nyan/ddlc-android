image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "Очередной день подходит к концу, и наступает время встречи нашего клуба."
    "Прошло несколько дней, и я даже начал к нему привыкать."
    "Я вхожу в комнату, и передо мной предстаёт привычная сцена."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "С возвращением, [player]..."
    hide yuri_half2
    mc "А, привет, Юри..."
    "Не могу сказать точно, может, мне кажется, а может, из-за выражения лица Юри..."
    "Но тяжесть от вчерашней ссоры по-прежнему висит в воздухе."
    y 2v "Э-эм..."
    "Юри взглянула через плечо, оглядывая комнату."
    "Нацуки читает мангу за столом."
    "И, что удивительно, Моники ещё нет."
    "Вдруг, Юри берёт меня за руку и тянет в угол комнаты."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "По поводу вчерашнего..."
    y "Мне..."
    y 2v "Мне нужно перед тобой извиниться."
    y "Ничего подобного раньше не случалось..."
    y 2t "И... похоже, что на меня что-то нашло..."
    y "Я была не в своём уме."
    y 2w "Пожалуйста, не думай, что мы всегда так себя ведём!"
    y "Ни я, ни Нацуки..."
    show yuri 2t
    mc "Юри..."
    mc "Я очень рад, что ты этим обеспокоена и признателен за извинение."
    mc "Но тебе не нужно так переживать."
    mc "Даже я, побывав здесь лишь пару дней, мог заметить, что вчера всё вышло из-под контроля..."
    mc "Может, мы все немного перенервничали из-за того, что в первый раз менялись поэмами."
    mc "Но, как бы там ни было..."
    mc "Я не стал хуже о тебе думать."
    mc "Я уже понял, что ты не можешь быть плохим человеком."
    mc "И теперь, когда ты извиняешься, я убеждаюсь, что ты всего этого совсем не хотела."
    y 3t "А-ах..."
    y "[player]..."
    y 3u "Не говори такие вещи так искренне..."
    y "Они делают меня слишком счастливой."
    y 1s "Я очень рада, что ты такой понимающий..."
    y "И очень рада, что ты присоединился к этому клубу."
    y "Рядом с тобой всё кажется немного ярче..."
    y 1t "Ах!.."
    y 4c "Прости, что же это я такое говорю...?"
    y "Я просто..."
    show natsuki 2c zorder 3 at f33
    n "Эй, ребята, вы не видели Монику?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ах!.."
    mc "Нет, я не видел..."
    mc "Мне тоже было интересно, где она."
    show natsuki zorder 3 at f33
    n 5g "Блин..."
    n 5c "Юри, я так понимаю, ты тоже не знаешь?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Юри явно была удивлена тем, как спокойно Нацуки к ней обратилась."
    y "Н-нет, я не..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Чёрт, это так на неё не похоже."
    n "Я знаю, выглядит глупо, но я почему-то немного беспокоюсь..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "Что?"
    n "Чего это вы на меня так смотрите?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Э-эм..."
    y "Нацуки, насчёт вчерашнего..."
    y 3w "Я-я хотела бы извиниться!"
    y "Уверяю, я не хотела наговорить всего этого!"
    y 3t "И теперь я изо всех сил постараюсь держать себя в руках..."
    y "Поэтому..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Юри, да о чём ты вообще говоришь-то?"
    n "Ты вчера что-то сделала?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "...А?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "Блин..."
    $ style.say_dialogue = style.edited
    n "Что бы ты там себе не придумала, я думаю, это ерунда."
    n "Я вообще не помню, чтобы вчера что-то плохое случалось"
    n "А ты такой уж человек, вечно беспокоишься о всяких мелочах, да?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "..."
    y "Н-но..."
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show yuri zorder 2 at t32
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "мибуллы канифас слепозрение леер анат прямонаправленность безукоризненно предложивший склеромаляция ржавший католикос"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "Но если тебе так легче, то я принимаю твои извинения."
    n "И вообще, приятно от тебя это слышать, я ведь всегда боялась, что ты меня тайно ненавидишь или типа того."
    n 2z "Хе-хе."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "Нет, совсем нет...!"
    y "Я тебя не ненавижу..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "Ахаха."
    n "Ну, ты хоть немного странная, но я тебя тоже не ненавижу."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Нацуки повернулась ко мне."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "А ты ещё на испытательном сроке."
    show natsuki zorder 2 at t33
    mc "Эй...!"
    "Внезапно открылась дверь."
    show monika 1g at l41
    m "Простите! Простите меня, пожалуйста!"
    mc "А вот и ты..."
    show monika zorder 3 at f41
    m "Я не хотела опоздать...."
    m "Надеюсь, вы не переживали из-за меня!"
    show monika zorder 2 at t41
    mc "Не..."
    mc "Может, только Нацуки."
    show natsuki zorder 3 at f33
    n 1p "Не было такого!!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Ахаха."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "...И всё же, что тебя задержало?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "А..."
    m "Ну, сегодня у меня были дополнительные занятия."
    m "Честно говоря, я совсем потеряла счёт времени..."
    m "Ахаха..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "Да ну, бред какой-то."
    n "Ты бы, по крайней мере, услышала звонок."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "Видимо, я не услышала его, потому что играла на пианино..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Пианино...?"
    y "Я не знала, что ты играешь на музыкальных инструментах, Моника."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "Ой, только не перехваливайте меня."
    m 1m "Я уже некоторое время практикуюсь, но я ещё не овладела этим в достаточной степени."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "И всё же..."
    y "От тебя это требует большой усидчивости."
    y "Поэтому я впечатлена."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "О, огромное спасибо, Юри~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "Ты должна сыграть что-нибудь для нас, Моника!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Ахаха, ну..."
    "Моника посмотрела на меня."
    m 1a "Ну, я тружусь над написанием одной песни, но она пока ещё не готова..."
    m "Может, когда-нибудь, когда буду чувствовать себя увереннее, я сыграю."
    show monika zorder 2 at t41
    mc "Звучит круто."
    mc "Буду с нетерпением ждать."
    show monika zorder 3 at f41
    m 1b "Правда?"
    m "Ну тогда..."
    m "Я тебя не разочарую, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "Моника нежно улыбнулась."
    mc "Эм..."
    mc "Я не хотел на тебя давить!"
    m 1a "Ахаха, не беспокойся."
    m "Я рассчитывала в любом случае показать её вам."
    m "Наверное, поэтому я в последнее время так усердно практикуюсь."
    mc "Понятно..."
    "Я не мог понять, Моника обращалась ко всему клубу, или ко мне лично?.."
    mc "Тогда желаю удачи."
    m 1j "Спасибо~!"
    m 1a "Так, я ничего не пропустила?"
    mc "Нет... ничего такого."
    show monika zorder 1 at thide
    hide monika
    "Я решил не рассказывать о том, что мы втроём обсуждали."
    "Кроме того, Нацуки уже убежала в свой чулан."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Эм..."
    y "Так как твои добрые слова подняли мне настроение..."
    y "Я подумала, может, мы сегодня проведём с тобой немного времени."
    y 3o "Я имею в виду... в клубе, конечно!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "А, ну, наверное, можно."
        mc "Я думаю, что не могу тебе отказать после того, как ты дала мне ту книгу."
        mc "Только, я думаю, мне надо убедиться, вдруг меня Нацуки ждёт."
        mc "После того, как мы вчера закончили читать, она..."
        if n_appeal >= 2:
            y 3r "Она в порядке!"
            $ style.say_dialogue = style.normal
            y 3h "Видишь? Вон она сидит там и читает."
            $ style.say_dialogue = style.edited
            y 3f "Не надо так много о ней думать."
            y "Она привыкла, когда её игнорируют."
            y "Пойдём, мы сядем тут."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            pause 2.0
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "О-она в норме!"
            y 3h "Она читает вон там."
            y 3y6 "Так что всё в порядке, да ведь?"
            mc "Э..."
            mc "Ну, раз так, то я не вижу проблемы..."
    else:
        $ y_appeal = 2
        mc "Да, конечно."
        mc "Я всё равно так и хотел."
    show yuri zorder 2 at h11
    y 3y5 "Хорошо!"
    y "Мы можем начать сейчас?"
    y "Так, давай найдём куда сесть..."
    y 3n "А-ах..."
    y "Я сегодня немного взвинчена, да?"
    y 4c "Извини меня!"
    y "Просто... моё сердце... отчего-то так колотится..."
    mc "Да не волнуйся ты так."
    mc "Между прочим, приятно видеть, что у тебя столько энергии."
    y 3q "А-ага!"
    y "Только..."
    y 3j "Мне надо немного успокоиться."
    y "А то я не смогу сконцентрироваться на чтении..."
    mc "Не спеши."
    "Юри делает глубокий вдох, затем достаёт свою копию книги из сумки."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene from _call_expression_24

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("Вы открыли особую поэму.\nХотите её прочитать?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1]) from _call_expression_25
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "Итак, ребята!"
    m "Вы уже закончили читать поэмы друг друга, верно?"
    $ config.mouse = None
    m "Я запланировала на сегодня ещё кое-что, и, если вы все могли бы подойти..."
    show natsuki 3c zorder 3 at f31
    n "Ты про фестиваль?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Ну, типа того~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Угх. Мы действительно должны делать что-то для фестиваля?"
    n "Не то чтобы мы не могли сообразить что-то интересное за пару дней."
    n "Всё просто закончится тем, что мы выставим себя на посмешище вместо того, чтобы набрать новых людей."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "Меня это тоже беспокоит."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "Я как-то не слишком хорошо справляюсь, когда сроки поджимают..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "Не переживайте вы так!"
    m "Мы придумаем что-то незатейливое, ладно?"
    m 2a "Смотрите..."
    m 2m "Я понимаю, что все немного... оживились... с тех пор, как к нам присоединился [player], и когда мы ввели разные клубные мероприятия."
    m 2d "Но это -- не повод расслабляться."
    m "У нас всего лишь четверо участников..."
    m 2a "А фестиваль, между прочим, единственная реальная возможность найти ещё."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "А что такого хорошего в наборе новых участников?"
    n "Нас и так достаточно, чтобы официально считаться клубом."
    n "Появление новых участников означает лишь то, что их будет трудно организовывать, и тут будет шумнее."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Нацуки..."
    m "Я думаю, ты смотришь на это совсем не под тем углом."
    m "Разве ты не хотела бы разделить свою страсть с как можно большим количеством людей?"
    m 3e "Вдохновлять их получить те же впечатления, которые привели тебя сюда в самом начале?"
    m "Литературный Клуб должен быть тем местом, где люди могут выражать себя так, как нигде больше."
    m "Он должен быть настолько родным местом, что тебе не захочется его покидать."
    m 2e "Я уверена, что ты тоже так думаешь."
    m 2b "Я уверена, что мы все так думаем!"
    m "Вот почему мы и должны приложить все силы, чтобы подготовить что-то для фестиваля... даже что-то маленькое!"
    m "Так ведь, [player]?"
    show monika 2a zorder 2 at t32
    mc "Э..."
    show natsuki zorder 3 at f31
    n 42c "Ой, да ладно тебе!"
    n "Ты думаешь, это считается, если [player] с тобой согласится? Он ведь не знает, как кому-то отказать."
    stop music fadeout 1
    n 1c "Слушай, Моника."
    n "Ты серьёзно думаешь, что хоть кто-то из нас присоединился к клубу, думая о ком-то ещё?"
    n "Да Юри и не разговаривала ни с кем до того, как [player] присоединился."
    n 2b "А что до меня, мне просто нравится здесь больше чем дома."
    n "Ну а [player] вообще с самого начала не очень-то увлекался литературой."
    n "Как и все остальные."
    n 4w "Ты уж прости, но похоже, что ты -- единственная, кто настолько заинтересована в привлечении новых участников."
    n "Остальным нравится всё как есть."
    n 4q "Я понимаю, ты президент и всё такое, но хотя бы раз тебе следовало бы прислушаться к нашему мнению."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Монику явно ошарашили слова Нацуки."
    play music t9
    m 1m "Это... совсем не так."
    m 2m "Я уверена, что Юри и [player] хотели бы увидеть новых участников..."
    m 2p "...Так ведь?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "Не знаю, как Юри, но лично мне по больше части всё равно."
    "Если бы я проявил тот энтузиазм, которого ждёт от меня Моника, то не был бы до конца честен."
    "И всё же, если это поможет спасти положение..."
    mc "Эм..."
    show monika zorder 3 at f32
    m 1i "Нет."
    m "Нацуки права, не так ли?"
    m 1g "Этот клуб..."
    m "Это не более чем место, где люди любят позависать."
    m 1r "И почему я считала, что все тут думают так же, как и я?"
    show monika zorder 2 at t32
    mc "Но это же не значит, что мы совсем против новых участников или типа того..."
    show monika zorder 3 at f32
    m 1i "[player], а почему ты вообще присоединился к этому клубу?"
    m "Что ты ожидал от него получить?"
    show monika zorder 2 at t32
    mc "Ну..."
    "Я не могу тут дать честный ответ, так ведь?"
    show monika zorder 3 at f32
    m 1p "И кстати..."
    m "Насколько я помню, тебе даже не дали возможности отказаться от вступления."
    show monika zorder 1 at thide
    hide monika
    "Моника села и уставилась на парту."
    m "Какой во всём этом вообще смысл?"
    m "Может, создание этого клуба было ошибкой?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "Ну отлично, Нацуки..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "А чего я-то?"
    n 1s "Сказала просто, что думала..."
    n "Быть честной что -- преступление?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "Дело не в честности."
    y "А в том, чтобы подбирать слова."
    y 2h "И кроме того, ты не имеешь права говорить вот так за всех в клубе..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "Ты вообще ничего не понимаешь!"
    n 5s "Я ведь просто..."
    n "Я просто хотела, чтобы было место, где я могу посидеть с друзьями."
    n 5u "Клуб что, не может быть таким местом для меня?"
    n "Таких... у меня не так уж много таких мест."
    n 5x "А теперь Моника хочет его у меня отнять!"
    show natsuki zorder 2 at t31
    mc "Ничего она у тебя не отнимает..."
    show natsuki zorder 3 at f31
    n 1g "Нет, [player]."
    n "Это будет не то же самое."
    n 1q "Он больше не останется прежним, если она сделает по-своему."
    n "Если бы я хотела того же самого, я бы могла присоединиться к любому другому дурацкому клубу."
    n 12d "Но этот..."
    n "Ну, то есть..."
    n 12e "Хоть на какое-то время..."
    n "Всё было так хорошо."
    "Нацуки стала собирать свои вещи."
    n 12d "Я домой пойду."
    n "Я... я думаю, мне здесь сейчас не место."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Нацуки..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Нацуки проигнорировала Юри и вышла из класса."
    show yuri zorder 2 at t11
    y 3v "..."
    y "Нехорошо это..."
    y "Не знаю, что теперь делать..."
    mc "Ну..."
    mc "Может, у тебя есть идеи для фестиваля?"
    y 4b "Я-я не знаю..."
    $ style.say_dialogue = style.normal
    y "Наверное, мне всё равно... "
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Да кого волнует это мерзкое отродье?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "Ну то есть, мне нравится тишина и покой, царящие сейчас в клубе..."
    y "И я... ну, счастлива здесь с тобой..."
    y 2t "И всё-таки!"
    y "Я же вице-президент..."
    y "Мне было бы неправильно так игнорировать свои обязанности..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Никто не заплачет, если она себя убьёт."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    pause 0.5
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    pause 0.75
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "Я должна приложить все усилия, чтобы рассмотреть вопрос с точек зрения каждого и выбрать лучшее для клуба решение."
    y 1t "А ты что думаешь, [player]?"
    y "Что ты хочешь получить от этого клуба?"
    "Юри спросила то же, что и Моника."
    "Я подумал, что дать размытый ответ будет лучше, чем ничего."
    mc "...Я думаю, что всем нам надо лучше ладить друг с другом..."
    mc "...Ну, а клубу надо предоставлять участникам то, что они нигде больше не смогут получить."
    mc "Не думаю, что дело в количестве участников, скорее, в их качестве."
    mc "Вот что делает Литературный Клуб таким особым местом."
    y 1u "Понятно..."
    y "Я с тобой полностью согласна."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Каждый участник привносит частичку себя."
    y "И с каждым участником сущность клуба, как целого, менятся соответственно."
    y 1h "Я не думаю, что это так уж плохо."
    y "Выходить ненамного из своей зоны комфорта..."
    y 1a "Поэтому, если ты решишь помочь Монике с подготовкой к фестивалю, то я с тобой."
    hide blood_eye2
    mc "Отлично."
    mc "Ну, тогда, может, мы сможем и с Нацуки завтра поговорить..."
    "Юри кивнула."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Эй, Юри..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "А?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Эм, вчера ситуация немного вышла из-под контроля..."
    m "Но я подумала, что тебе стоит знать, что я всё так же считаю тебя великолепным вице-президентом."
    m 1e "И к тому же -- замечательным другом."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "М-Моника..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "Я хочу сделать всё, чтобы этот клуб стал самым лучшим."
    m "Понимаешь?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...Я тоже."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Ура..."
    m "Давайте тогда пойдём домой."
    m "Поговорим о фестивале завтра."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Хорошо."
    y "Буду ждать с нетерпением."
    y 1a "Пойдём, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Эм.."
    m 1p "Не пойми меня, пожалуйста, неправильно, но... "
    m "Позволь, я и [player] немного поболтаем перед уходом."
    m 1d "Просто нужно уточнить его мнение о его присутствии здесь и остальном..."
    m "Это для меня, как для президента, очень важно."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Юри выглядела немного встревоженной, но перечить не стала."
    y 2t "Ладно."
    y 2s "Я доверяю твоему решению, Моника."
    y "Раз так, то увидимся с вами двумя завтра."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "Увидимся завтра~"
    show yuri zorder 1 at thide
    hide yuri
    "Моника помахала вслед Юри, выходящей из класса."

    show monika 2a zorder 2 at t11
    m "Фхух..."
    m 2e "Какие бурные события тут происходят в последнее время, да?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], я просто хотела убедиться, что тебе хорошо в этом клубе."
    m "Мне бы очень не хотелось, чтобы тебе было нехорошо."
    m 2m "И я, как президент, чувствую некоторую ответственность за всё это..."
    stop music
    m 4e "И, к твоему сведению, я о тебе очень беспокоюсь...."
    m "Мне не нравится, что остальные девочки доставляют тебе столько хлопот."
    m 4r "Как, например, себя ведёт Нацуки, и так далее..."
    m 4m "Ну и Юри была немного... ну ты знаешь."
    m 5a "Ахаха..."
    m "Иногда кажется, что ты и я -- единственные настоящие люди здесь."
    m "Понимаешь, о чём я?"
    m 1g "Но это так странно, ведь за всё время, что ты тут, у нас едва ли было хоть немного времени пообщаться."
    m 1n "Э... ну то есть..."
    m "Наверное, прошло-то всего несколько дней..."
    m 1l "Прости, я не хотела говорить ничего странного!"
    m 1e "Просто есть кое-что, о чём я хотела с тобой поговорить..."
    m "То, что только ты, я уверена, можешь понять."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "И поэтому я...\"{space=5000}{w=0.75}{nw}"
    m 1g "Подожди, ещё рано!\"{space=5000}{w=0.5}{nw}"
    m "Нет!\"{space=5000}{w=0.5}{nw}"
    m "Останови это!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
