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
    "Уроки закончились, и подошло время собрания клуба."
    "За последние пару дней я немного в нём освоился."
    "В помещении клуба меня встретила знакомая картина."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "С возвращением, [player]..."
    hide yuri_half2
    mc "О, привет, Юри..."
    "То ли мне показалось, то ли дело в выражении лица Юри..."
    "Однако в воздухе до сих пор ощущались остатки вчерашней ссоры."
    y 2v "Эм-м..."
    "Юри обернулась и окинула взглядом комнату."
    "Нацуки читала мангу, сидя за столом."
    "А вот Моники, на удивление, ещё не было."
    "Юри внезапно схватила меня за руку и оттащила в угол."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "По поводу вчерашнего..."
    y "Мне..."
    y 2v "Мне очень нужно извиниться."
    y "Такого ещё никогда не случалось..."
    y 2t "И... На меня просто что-то нашло, наверное..."
    y "Я вела себя как полоумная."
    y 2w "Прошу, не думай, что такое происходит постоянно!"
    y "Не только у меня, но и у Нацуки..."
    show yuri 2t
    mc "Юри..."
    mc "Я рад, что ты повела себя тактично и извинилась."
    mc "Не стоит так сильно переживать."
    mc "Я здесь всего пару дней, но всё равно понял, что вчера что-то было не так..."
    mc "Возможно, мы были слегка чувствительнее, чем обычно, потому что это был наш первый обмен стихами."
    mc "Но как бы то ни было..."
    mc "Я не стал думать о тебе хуже."
    mc "Я уже решил для себя, что ты не можешь быть плохим человеком."
    mc "И теперь, когда ты извиняешься, я уверен, что ты поступила так не нарочно."
    y 3t "А-а..."
    y "[player]..."
    y 3u "Ты сказал об этом так прямо..."
    y "Твои слова делают меня даже чересчур счастливой."
    y 1s "Я очень рада, что ты такой понимающий..."
    y "А ещё я очень рада, что ты вступил в этот клуб."
    y "Рядом с тобой всё становится чуточку ярче, и..."
    y 1t "Ой..."
    y 4c "Прости, что это я такое говорю?.."
    y "Я просто..."
    show natsuki 2c zorder 3 at f33
    n "Эй, вы не видели Монику?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "Ох!"
    mc "Нет, я не видел..."
    mc "Я и сам уже начал думать о том, куда она могла подеваться."
    show natsuki zorder 3 at f33
    n 5g "Блин..."
    n 5c "Юри, я так понимаю, ты тоже?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "..."
    "Юри явно оторопела от того спокойствия, с которым Нацуки обратилась к ней."
    y "Н-нет, не видела..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "Мда-а, это совсем на неё не похоже."
    n "Я знаю, это глупо, но я всё равно немного беспокоюсь..."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "..."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "Чего?"
    n "Чего ты на меня так смотришь?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "Эмм..."
    y "Нацуки, по поводу вчерашнего..."
    y 3w "Я... Я просто хотела извиниться!"
    y "Я совсем не думаю всего того, что вчера тебе наговорила!"
    y 3t "Впредь я постараюсь держать себя в руках..."
    y "Так что..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "Юри, ты о чём ваще?"
    n "Ты что-то сделала вчера?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "Э?.."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "М-да уж..."
    $ style.say_dialogue = style.edited
    n "Что бы тебя там ни волновало, я уверена, что это ерунда."
    n "Я даже не помню, чтобы вчера случалось что-то плохое."
    n "Ты из тех, кто накручивает себя по всяким пустякам, да?"
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
        n 2a "парусина ложнаяслепота спасательныйтрос анан роствверх безошибочно предложил склеромаляция ржал католикос"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "Но я всё равно приму твои извинения, если тебе от этого станет легче."
    n "К тому же это приятно слышать, а то я всегда боялась, что ты меня тайно ненавидишь или что-то в этом роде."
    n 2z "Хе-хе-хе."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "Н-нет, ничего подобного!.."
    y "У меня нет к тебе неприязни..."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "Ха-ха-ха."
    n "Ну, ты это, слегка странноватая, но я тоже к тебе нормально отношусь."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "..."
    "Нацуки повернулась ко мне."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "А вот ты всё ещё подсуден."
    show natsuki zorder 2 at t33
    mc "Эй!.."
    "И тут распахнулась дверь."
    show monika 1g at l41
    m "Извиняюсь! Дико извиняюсь!"
    mc "О, а вот и она..."
    show monika zorder 3 at f41
    m "Не собиралась опаздывать..."
    m "Надеюсь, вы не сильно волновались!"
    show monika zorder 2 at t41
    mc "Не-а..."
    mc "Ну, разве что Нацуки."
    show natsuki zorder 3 at f33
    n 1p "А вот и нет!!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "Ха-ха-ха."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "А чего ты так долго-то, ваще?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "А..."
    m "Ну, сегодня последним уроком было самообучение."
    m "Честно говоря, я просто потеряла счёт времени..."
    m "Ха-ха-ха..."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "Только странно получается."
    n "Ты бы ведь по-любому услышала звонок."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "Скорее всего, я не услышала его потому, что играла на фортепиано..."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "Фортепиано?.."
    y "Не знала, что ты занимаешься ещё и музыкой, Моника."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "Ох, не стоит переоценивать мои способности."
    m 1m "Я уже достаточно долго учусь, но получается пока не очень."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "И всё же..."
    y "Это, должно быть, требует большого упорства."
    y "Так что я всё равно приятно удивлена."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "О-о, спасибочки, Юри-и-и."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "Сыграй как-нибудь что-нибудь для нас!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "Ха-ха-ха, это..."
    "Моника взглянула на меня."
    m 1a "В общем, я тут работаю над написанием песни, но она ещё не совсем готова..."
    m "Возможно, когда я немножечко подучусь, то сыграю для вас."
    show monika zorder 2 at t41
    mc "Звучит здорово."
    mc "Буду ждать с нетерпением."
    show monika zorder 3 at f41
    m 1b "Неужели?"
    m "В таком случае..."
    m "Я не подведу тебя, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "Моника мило улыбнулась."
    mc "Ох..."
    mc "Я совсем не собирался на тебя давить, правда!"
    m 1a "Ха-ха, не переживай."
    m "Я в любом случае надеюсь, что ты сможешь её услышать."
    m "Наверное, поэтому столько и тренируюсь в последнее время."
    mc "Понятно..."
    "Я не совсем понял, будет ли Моника играть для всех или только для меня..."
    mc "В таком случае желаю удачи."
    m 1j "Спа-а-асибо!"
    m 1a "Итак, я ведь ничего не пропустила?"
    mc "Да вроде нет..."
    show monika zorder 1 at thide
    hide monika
    "Я предпочёл не упоминать то, что мы обсуждали втроём."
    "К тому же Нацуки уже унеслась в кладовку."
    show yuri 2q zorder 2 at t11
    y "[player]..."
    y "Эм..."
    y "Раз уж твои комплименты так подняли мне настроение..."
    y "Я подумала, а почему бы нам сегодня не провести немного времени вместе?"
    y 3o "Ну, в смысле... В клубе!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "А, ну давай."
        mc "Не думаю, что смогу отказать тебе после того, как ты дала мне эту книгу."
        mc "Разве что убежусь-ка я, что Нацуки меня не ждёт."
        mc "Вчера, после того, как мы закончили читать, она..."
        if n_appeal >= 2:
            y 3r "Всё с ней хорошо!"
            $ style.say_dialogue = style.normal
            y 3h "Смотри, вот она, читает."
            $ style.say_dialogue = style.edited
            y 3f "Не думай о ней слишком много."
            y "Она уже привыкла, что её не замечают."
            y "Ну же, пойдём вон туда."
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
            y 3r "В-всё с ней хорошо!"
            y 3h "Вот она, сидит, читает."
            y 3y6 "Всё нормально, видишь?"
            mc "Ох..."
            mc "В таком случае, я не против..."
    else:
        $ y_appeal = 2
        mc "Да, конечно."
        mc "Я и сам собирался это предложить."
    show yuri zorder 2 at h11
    y 3y5 "Итак!"
    y "Начинаем?"
    y "Давай найдём, куда присесть..."
    y 3n "О-ой..."
    y "Я же тебя не напрягаю?.."
    y 4c "Прости!"
    y "Просто... Моё сердце почему-то не перестаёт колотиться..."
    mc "Не волнуйся."
    mc "Если что, я очень рад видеть тебя такой энергичной."
    y 3q "Д-да!"
    y "Но..."
    y 3j "Мне нужно попробовать успокоиться."
    y "Я не смогу сконцентрироваться на чтении в таком состоянии..."
    mc "Конечно, я тебя не тороплю."
    "Юри сделала глубокий вдох, а потом вытащила томик из своей сумки."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene from _call_expression_11

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("Вы открыли особый стих.\nХотите прочесть его?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1]) from _call_expression_12
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



    m "Так, ребята!"
    m "Все уже прочитали стихи друг друга?"
    $ config.mouse = None
    m "Нам нужно по кое-чему пробежаться, так что будьте добры, сядьте в передних рядах..."
    show natsuki 3c zorder 3 at f31
    n "Это связано с фестивалем?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "Ну, вроде того."
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "Бе. Нам правда придётся делать что-то для фестиваля?"
    n "Ничего годного всего за пару дней всё равно не склепаешь."
    n "Мы лишь выставим себя на посмешище, а не привлечём новых людей в клуб."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "Да, я тоже беспокоюсь по этому поводу."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "Я плохо справляюсь, когда что-то приходится делать в последний момент..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "Да не переживайте вы так!"
    m "Мы обойдёмся чем-нибудь попроще, ладно?"
    m 2a "Слушайте..."
    m 2m "Я знаю, что вы все несколько оживились после того, как [player] вступил к нам, и мы стали заниматься деятельностью клуба."
    m 2d "Но сейчас не время для самодовольства."
    m "Наш клуб до сих пор состоит всего из четырёх человек..."
    m 2a "А фестиваль — наш единственный шанс найти кого-то ещё, понимаете?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "А какие вообще плюсы в новых лицах?"
    n "У нас достаточно людей, чтобы считаться клубом официально."
    n "Чем больше людей, тем больше шума и сложнее за всем уследить."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "Нацуки..."
    m "Мне кажется, ты подходишь к вопросу не с той стороны."
    m "Разве тебе не хотелось бы разделить своё увлечение с большим числом людей?"
    m 3e "Вдохновить их на поиск тех чувств, что первоначально привели сюда тебя?"
    m "Литературный клуб должен быть тем местом, где все люди могут выразить себя, как нигде ещё."
    m "Он должен быть таким родным, чтобы из него не хотелось уходить."
    m 2e "Я знаю, что вы тоже так думаете."
    m 2b "Все мы так думаем!"
    m "Поэтому нам нужно выложиться по полной и приготовить что-нибудь к фестивалю... Хотя бы что-то небольшое!"
    m "Согласен, [player]?"
    show monika 2a zorder 2 at t32
    mc "Ох..."
    show natsuki zorder 3 at f31
    n 42c "Ой, да хватит!"
    n "Хорош пользоваться тем, что [player] всегда с тобой соглашается, потому что совершенно не умеет отказывать."
    stop music fadeout 1
    n 1c "Слушай, Моника."
    n "Ты правда считаешь, что мы все вступили в клуб из-за того, что думали о других?"
    n "Юри даже толком не разговаривала, пока не появился [player]."
    n 2b "Что касается меня, так мне тут просто нравится больше, чем дома."
    n "А [player] и вовсе не увлекается литературой."
    n "И так тут со всеми."
    n 4w "Извини, но ты реально единственная, кому интересно искать новичков."
    n "Остальным и так хорошо."
    n 4q "Я понимаю, что ты президент клуба и всё такое, но тебе стоит хоть иногда интересоваться и нашим мнением."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "..."
    "Монику явно ошеломили слова Нацуки."
    play music t9
    m 1m "Это... Это вовсе не так."
    m 2m "Я уверена, что и Юри, и [player] тоже хотят, чтобы вступило больше людей..."
    m 2p "Правда?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "..."
    show yuri zorder 2 at t33
    mc "..."
    "Не знаю насчёт Юри, но мне как-то всё равно."
    "Выражать энтузиазм, которого ждала от меня Моника, было бы лицемерием."
    "И всё же, раз уж ответственность за спасение этой ситуации досталась мне..."
    mc "Эм..."
    show monika zorder 3 at f32
    m 1i "Нет."
    m "Нацуки права, не так ли?"
    m 1g "Этот клуб..."
    m "Не более, чем место для совместного досуга нескольких людей."
    m 1r "И почему я считала, что все видят вещи в том же свете, что и я?"
    show monika zorder 2 at t32
    mc "Но это ведь не значит, что мы против привлечения новичков..."
    show monika zorder 3 at f32
    m 1i "[player], а почему ты вообще вступил в наш клуб?"
    m "Что ты надеялся получить от него?"
    show monika zorder 2 at t32
    mc "Ну..."
    "По-моему, это не тот случай, когда стоит отвечать честно, да?"
    show monika zorder 3 at f32
    m 1p "Вообще..."
    m "Если я правильно помню, то у тебя и выбора-то особо не было."
    show monika zorder 1 at thide
    hide monika
    "Моника села и уставилась в свой стол."
    m "Ну и какой во всём этом вообще смысл?"
    m "Что, если основание этого клуба было ошибкой?"
    mc "..."
    show yuri zorder 3 at f33
    y 2g "Ну вот, Нацуки, ты её довела..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "А чё я?"
    n 1s "Я просто сказала, что думаю..."
    n "Быть честной теперь преступление?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "Тут дело не в честности."
    y "А в выборе слов."
    y 2h "К тому же никто не давал тебе права вот так говорить за всех остальных членов клуба..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "Да ты ни черта не понимаешь!"
    n 5s "Мне просто..."
    n "Мне просто хочется место, где мне было бы хорошо и где я могла бы проводить время с парочкой друзей."
    n 5u "Почему этим местом для меня не может быть клуб?"
    n "Ведь... ведь у меня не так много подобных мест..."
    n 5x "А теперь Моника хочет у меня и это отобрать!"
    show natsuki zorder 2 at t31
    mc "Но она ничего не отбирает..."
    show natsuki zorder 3 at f31
    n 1g "Нет, [player]."
    n "Он уже не будет таким."
    n 1q "Он не будет таким, если пойти по пути, которого хочет Моника."
    n "Если бы мне нужно было что-то такое, я бы вступила в любой другой тупой клуб."
    n 12d "Но здесь..."
    n "Ну, в смысле..."
    n 12e "Хоть и недолго..."
    n "Но здесь было хорошо."
    "Нацуки начала собирать свои вещи."
    n 12d "Я иду домой."
    n "Мне кажется, что сейчас мне здесь не место."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "Нацуки..."
    show natsuki zorder 1 at thide
    hide natsuki
    "Нацуки проигнорировала Юри и вышла прямиком из класса."
    show yuri zorder 2 at t11
    y 3v "..."
    y "Плохо дело..."
    y "Я не знаю, как поступить..."
    mc "Ну..."
    mc "Тебе есть, что сказать по поводу фестиваля?"
    y 4b "Н-не знаю..."
    $ style.say_dialogue = style.normal
    y "Мне как-то всё равно, наверное..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Кому есть дело до этой надоедливой соплячки?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "В смысле, наш клуб мне нравится таким, как сейчас: тихим и уютным..."
    y "И я просто... счастлива, что здесь есть ты..."
    y 2t "И всё же!"
    y "Я вице-президент клуба..."
    y "И я не должна так пренебрегать своими обязанностями..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Никто не станет грустить, если она наложит на себя руки."
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
    y 2l "Мне нужно постараться учесть мнение каждого и принять решение, которое будет лучшим для клуба."
    y 1t "А что скажешь ты, [player]?"
    y "Что ты хочешь получить от этого клуба?"
    "Юри повторила вопрос Моники."
    "Я решил, что лучше дать расплывчатый ответ, чем промолчать."
    mc "Я думаю, главное, чтобы мы все ладили..."
    mc "А клуб давал бы нам что-то, что мы не можем получить где-то ещё."
    mc "Я не думаю, что это зависит от количества людей, скорее от качества каждого из них."
    mc "Вот что сделает литературный клуб по-настоящему особым местом."
    y 1u "Понятно..."
    y "Я с тобой совершенно согласна."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "Каждый участник по-своему делает свой качественный вклад."
    y "С каждым изменением в составе будет меняться и сущность всего клуба."
    y 1h "Я думаю, что само по себе это вовсе не плохо."
    y "Время от времени выходить из своей зоны комфорта..."
    y 1a "Так что, если ты хочешь помочь Монике с фестивалем, то я с тобой."
    hide blood_eye2
    mc "Хорошо."
    mc "Ну, нам, наверное, стоит завтра поговорить с Нацуки..."
    "Юри кивнула."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "Эй, Юри..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "Э?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "Эм, я знаю, что вчера всё вышло немного неловко..."
    m "Но мне кажется, что ты заслуживаешь знать, что я все ещё считаю тебя отличным заместителем."
    m 1e "А заодно и прекрасным другом."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "М-моника..."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "Я хочу сделать всё, что в моих силах, чтобы этот клуб был самым лучшим на свете."
    m "Хорошо?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "...Я тоже."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Ага..."
    m "Давайте-ка уже расходиться по домам."
    m "О фестивале поговорим завтра."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "Хорошо."
    y "Буду ждать с нетерпением."
    y 1a "Идём, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "Эм."
    m 1p "Не пойми меня неправильно, но..."
    m "Мне нужен [player], чтобы ещё кое-что обсудить перед тем, как мы уйдём."
    m 1d "Ну, чтобы узнать, что он думает о своём пребывании здесь и всё такое..."
    m "Это важно для меня как для президента клуба."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "..."
    "Юри выглядела немного встревоженной, но не стала возражать."
    y 2t "Хорошо."
    y 2s "Я доверяю твоему суждению, Моника."
    y "В таком случае увидимся завтра."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "До завтра-а."
    show yuri zorder 1 at thide
    hide yuri
    "Моника помахала вслед выходящей из класса Юри."

    show monika 2a zorder 2 at t11
    m "Фух..."
    m 2e "День сегодня выдался несколько напряжённым, не так ли?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], я лишь хотела убедиться, что тебе нравится в нашем клубе."
    m "Я бы очень не хотела видеть тебя расстроенным."
    m 2m "Я чувствую, что, как президент, несу за это ответственность..."
    stop music
    m 4e "И знаешь, ты для меня по-настоящему важен..."
    m "Мне не нравится видеть, как другие девушки доставляют тебе неудобства."
    m 4r "Нацуки со своим гадким поведением..."
    m 4m "Ну и Юри, которая немного, ну... того."
    m 5a "Ха-ха-ха..."
    m "Иногда мне кажется, что только мы с тобой тут являемся настоящими."
    m "Понимаешь, о чём я?"
    m 1g "Но это странно, ведь за всё время, что ты здесь, мы не провели вместе почти ни минуты."
    m 1n "Ах... В смысле..."
    m "Пожалуй, прошла-то всего пара дней, по сути..."
    m 1l "Извини, если я сказала что-то не то!"
    m 1e "Просто я надеялась с тобой кое о чём поговорить..."
    m "О вещах, которые, я уверена, сможешь понять только ты."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "Поэтому...\"{space=5000}{w=0.75}{nw}"
    m 1g "Погоди, рано!\"{space=5000}{w=0.5}{nw}"
    m "Нет!\"{space=5000}{w=0.5}{nw}"
    m "Постой!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
