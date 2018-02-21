image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    y "Привет, [player]!"
    y "Я ждала тебя."
    y 2d "Ты готов продолжить чтение?"
    y "Я сегодня принесла свой лучший чай..."
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Моника!"
    n "Я просила тебя не..."
    n 1g "Уф-ф..."
    n "Она что, опять опаздывает?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Как всегда бестактно, Нацуки."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Что, прости?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Тебе обязательно постоянно прерывать мои разговоры своими нескончаемыми воплями?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "Ты о чём ваще?!"
    n 1q "Типа я делаю это регулярно."
    n "Я просто не заметила, ладно? Прости."
    n 4u "Серьёзно... Что с тобой не так в последнее время?"
    if n_appeal >= 2:
        n "Слушай..."
        n "Я подумала о вчерашнем."
        n 2q "Я вела себя чересчур враждебно..."
        n 1q "Наверное, просто оскорбилась или что-то в этом духе."
        n 1h "Но я понимаю, что мы делаем одно дело."
        n 1q "Новички не повредят, если они классные ребята..."
        n 5w "И думаю, что новенькая девушка нам бы тоже не помешала..."
        n 5u "Так что..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Нацуки..."
        $ style.say_dialogue = style.edited
        y 1f "Всем плевать."
        y "Почему бы тебе не поискать монеты под торговыми автоматами или не поделать что-нибудь ещё?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "...!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "Вот блин..."
        m "Опять я последняя!"
        show yuri zorder 3 at f32
        y 1f "Снова музицировала?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Ага..."
        m "А-ха-ха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты, должно быть, очень трудолюбивая."
        y "Основала этот клуб, а теперь ещё и фортепиано..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Ну, скорее не трудолюбивая..."
        m 3a "А увлечённая."
        m "Это ещё и мотивирует меня трудиться ради фестиваля."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Со мной?"
        y 2o "Н-ничего..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Всё правда так плохо?.."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "Ну, знаешь, с {i}этим{/i} надо что-то делать."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "Я исправлюсь!"
        y 3y6 "Это даже не заслуживает внимания..."
        y 3o "В последнее время я чувствую себя немного на грани..."
        y 3n "В-В любом случае здесь не о чем говорить!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Ну, мне просто показалось, что надо поднять эту тему."
        n 5q "Не то чтобы меня это волновало..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Вот блин..."
        m "Опять я последняя!"
        show natsuki zorder 3 at f33
        n 2c "Ну, [player] тоже только зашёл."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "Ты снова музицировала?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Ага..."
        m "А-ха-ха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты, должно быть, очень трудолюбивая."
        y "Основала этот клуб, а теперь ещё и фортепиано..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Ну, скорее не трудолюбивая..."
        m 3a "А увлечённая."
        m "Это ещё и мотивирует меня трудиться ради фестиваля и..."
        m 3n "Эм..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Точно..."
        m "Я... Я забыла..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Эм, насчёт этого, Нацуки..."
        y "Мы тут вчера обсудили, и..."
        y 2t "В общем... мы тоже решили поддержать фестиваль."
        y 2l "Однако!.."
        y 2h "Я понимаю, что ты не хочешь, чтобы клуб менялся."
        y "Мне кажется, мы все чувствуем приблизительно одно и то же."
        y 2f "Так что до тех пор, пока мы работаем все вместе, этот клуб никогда не станет таким, каким мы бы не желали его видеть."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Эм, и ещё..."
        y "Если ты поможешь нам с фестивалем..."
        y 3r "...То я куплю тебе новую мангу!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "А-ха-ха-ха!"
        n "Прости, последнее было очень смешно."
        n 2c "Слушай..."
        n "Я подумала о вчерашнем."
        n 2q "Я вела себя чересчур враждебно..."
        n 1q "Наверное, просто оскорбилась или что-то в этом духе."
        n 1h "Но я понимаю, что мы делаем одно дело."
        n 1q "Новички не повредят, если они классные ребята..."
        n 5w "И думаю, что новенькая девушка нам бы тоже не помешала..."
        n 5e "...Но главное то, что я не собираюсь кидать вас, чтобы посмотреть, как вы облажаетесь с фестивалем!"
        n "Я же профи, в конце концов!"
        n 5c "Поэтому я тоже в деле. Всё у нас получится."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Слава богу..."
        y "Разве это не замечательно, Моника?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...Моника?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "А..."
        m 1n "Да, это чудесно!"
        m "Без тебя бы ничего не получилось, Нацуки."
    m 5 "Кстати, [player]..."
    m "Чем хочешь сегодня заняться?"
    m "Я подумала, что мы можем..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "У нас уже есть планы на сегодня."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "А..."
    m "Разве, Юри?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "Именно."
    y "[player] уже занят книгой, которую мы читаем вместе."
    y 1y5 "Разве ты не рада, что я знакомлю его с литературой, Моника?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "Я..."
    m "Я думаю..."
    m "Я просто..."
    m 1r "Ладно, это неважно."
    m 1i "Правда неважно."
    m "Делайте, что хотите."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Да!){/i}{w=0.5}{nw}"
    y 2u "Эм... Благодарю за понимание, Моника."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22 from _call_yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2]) from _call_expression_18
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Так, ребята!"
    m "Настало время разбираться с подготовкой к фестивалю."
    m 1i "Давайте поскорее покончим с этим."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Блин..."
        n "Что ж сегодня атмосфера такая странная?"
        n "Вон, даже Юри не устояла."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "У-у..."
    y "Застывший воздух есть характерный предвестник ужасных событий..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Послушайте, мы можем просто с этим закончить?"
    m 2d "Я буду распечатывать и сшивать буклеты со стихами."
    if n_appeal >= 2:
        m 2i "Нацуки, ты можешь испечь кексы."
        m "По крайней мере, я уверена, что в этом ты хороша."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Нацуки, я тут подумала..."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "Я хочу печь кексы!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Ну да, как раз об этом."
        m "Рада, что мы на одной волне."
    m 1m "Юри, ты можешь..."
    m 1r "...Хотя без разницы."
    m 1i "Делай что хочешь, лишь бы от этого польза была."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Моника..."
    y "Я, к твоему сведению, не бесполезная!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "Я... Я в курсе!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "Я уже знаю, чем займусь."
    y 1h "Мы не сможем успешно провести стихотворное выступление, если не создадим нужную атмосферу."
    y "Поэтому я собираюсь сделать декорации, чтобы задать хорошее настроение."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "Ну вот, видишь!"
    m "Отличная идея!"
    m 1a "Теперь работа есть у каждого."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "М?"
    y "А как же [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] будет помогать мне."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Стоп, тебе?"
    n "У тебя самая простая работа, Моника!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Прости, но я так захотела."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Ты так охренела!"
    n "Что это за подстава?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "Я... Я согласна с Нацуки!"
    y "Мало того, что с твоей работой можно справиться в одиночку..."
    y 3l "Так ещё и моя задача достаточно трудоёмкая, чтобы требовать привлечения лишней пары рук."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "И моя!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "Что, кексики твои?"
    y "Я тебя умоляю."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "Да что {i}ты{/i}, сука, понимаешь!"
    n 1x "Тебя же только одно чешет: чтобы [player] таскался за тобой и твоими книжонками придурочными."
    n 1f "Тебя {i}и{/i} Монику!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Эй!"
    m "А я тут причём?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Ладно, тогда, может вместо того, чтобы злоупотреблять своей властью, позволишь, чтобы [player] сам решал, кому помогать?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "Я не... злоупотребляю своей властью."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Злоупотребляешь, Моника."
    y "Просто пускай [player] выберет сам, хорошо?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Хорошо, хорошо!"
    m "Хорошо."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Блин..."
    n "[player], я знаю, что они обе тебя уже достали."
    n 3c "Мы можем просто..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Нацуки, заткни свой поганый рот и дай ему решить самостоятельно."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}Сама{/i} заткнись!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Господи Иисусе..."
    m 1i "Это никогда не кончится. Просто сделай выбор, хорошо?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("Нацуки.", "natsuki"), ("Юри.", "yuri"), ("Моника.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
            "Моника":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "Ура, ты выбрал меня!"
    m "Можем встретиться на этих выходных у тебя дома."
    m "Обещаю, что будет весело."
    m "В воскресенье, идёт?"
    show natsuki 1e zorder 3 at f31
    n "Ты, сука, прикалываешься?"
    n "Это нифига не честно!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "Честно, Нацуки."
    m "Это его выбор."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "Нет, это нечестно!"
    y "Загрузила работой ты нас, а помогать [player] должен тебе."
    y "Вопиющий поступок!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Юри, лично тебя я ничем не загружала."
    m 2i "Ты выбрала себе работу сама."
    m "Так что твои претензии безосновательны."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "Безосновательны?"
    y 2y3 "А-ха-ха-ха!"
    y "Какая же ты лживая, Моника! Даже не верится, что у тебя настолько раздутое самомнение!"
    y "Каждый раз, когда [player] занимается чем-то со мной, ты уволакиваешь его, потому что тебя не позвали."
    y 1y1 "Ты ревнуешь?"
    y "С ума сошла?"
    y 1y3 "Или, может, просто ненавидишь себя настолько сильно, что вымещаешь это на других?"
    y 1y4 "Вот тебе совет. Ты не задумывалась о самоубийстве?"
    y "Это было бы полезно для твоего психического здоровья."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Юри, ты меня немного пугаешь..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Нацуки, давай просто уйдём."
    m 1i "Кажется, она не хочет сейчас нас видеть."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "Видишь, это совсем несложно."
    y "Я всего лишь хочу провести с ним немного времени."
    y "Разве я о многом прошу?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Юри проводила Монику и Нацуки до двери."
    show monika 5a zorder 2 at t11
    m "Эй, [player]..."
    m "Юри та ещё штучка, скажи?"
    show monika zorder 1 at thide
    hide monika
    "Хихикнула Моника, когда Юри выталкивала её в коридор."
    python:
        try: renpy.file(config.basedir + "/have a nice weekend!")
        except: open(config.basedir + "/have a nice weekend!", "w").write("G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/")
        try: os.remove(config.basedir + "/hxppy thxughts.png")
        except: pass
        try: os.remove(config.basedir + "/CAN YOU HEAR ME.txt")
        except: pass
        try: os.remove(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Наконец-то."
    y 2y1 "Наконец-то!"
    y 2s "Как же я этого хотела."
    y 1y6 "[player], ты не обязан проводить выходные с Моникой."
    y "Не слушай её."
    y 1y5 "Идём лучше ко мне."
    y 3y5 "Целый день, только ты и я..."
    y "Звучит заманчиво, не правда ли?"
    y 3y1 "А-ха-ха-ха!"
    y 3y4 "Оу... Со мной и правда что-то не так, да?"
    y "Но знаешь что?"
    y 1y3 "Меня это больше не волнует."
    y "Я ещё ни разу в жизни не чувствовала себя настолько хорошо."
    y 1y4 "Просто находиться рядом с тобой — самое невероятное удовольствие из всех возможных."
    y "Я одержима тобой."
    y 3y4 "Кажется, я умру, если не буду дышать с тобой одним воздухом."
    y 4a "Разве не приятно, когда есть тот, кто настолько тобой озабочен?"
    y "Человек, вся жизнь которого вертится вокруг тебя?"
    y 2y6 "Но если это так хорошо..."
    y 2y4 "Тогда почему во мне нарастает предчувствие чего-то ужасного?"
    y 2y6 "Может быть, поэтому я поначалу пыталась себя останавливать..."
    y "Но теперь мои чувства слишком сильны."
    y 3y1 "Мне уже всё равно, [player]!"
    y "Я должна тебе признаться!"
    y 3y4 "Я... Я безумно люблю тебя!"
    y "Я буквально чувствую, как каждый сантиметр моего тела... каждая капля моей крови... кричит твоё имя."
    y 3y3 "Меня больше не заботят последствия!"
    y "Мне плевать, подслушивает нас Моника или нет!"
    y 3w "Пожалуйста, [player], просто знай, как сильно я тебя люблю."
    y 3m "Я настолько люблю тебя, что даже мастурбировала твоей ручкой, которую украла."
    y 3y4 "Я хочу вскрыть твою кожу и заползти внутрь тебя."
    y 3y6 "Хочу себе всего тебя."
    y "А я буду только твоей."
    y "Правда, звучит прекрасно?"
    y 3s "Скажи мне, [player]."
    y "Скажи, что хочешь быть моим любовником."
    y "Ты принимаешь мои чувства?"

    menu:
        "Да.":
            jump yuri_kill
        "Нет.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "...А-ха-ха-ха."
    y "А-ха-ха-ха-ха-ха-ха!"
    $ style.say_dialogue = style.normal
    y 3y5 "А-ха-ха-ха-ха-ха-ха-ха-ха!"
    $ style.say_dialogue = style.edited
    y 3y3 "А-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА-ХА!{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """Добро пожаловать в Литературный клуб! Я всегда мечтала создать на основе своих увлечений нечто особенное, и раз уж ты вступил в клуб, то можешь помочь мне воплотить мою мечту в реальность с помощью этой замечательной игры! Ни дня не пройдёт без болтовни и весёлых занятий с членами нашего клуба: Саёри — юный солнечный лучик, который больше всего ценит счастье; Нацуки — обманчиво миловидная девушка, которая на деле может отвесить неслабую затрещину; Юри — робкая и таинственная, находит утешение в мире книг; И, конечно же, Моника — лидер клуба! Это я! Жду с нетерпением, когда ты с нами подружишься и поможешь литературному клубу стать родным местом для всех его участников. Хотя я и сейчас уже вижу, что ты душка! Обещаешь проводить большую часть времени со мной? Добро пожаловать в Литературный клуб! Я всегда мечтала создать на основе своих увлечений нечто особенное, и раз уж ты вступил в клуб, то можешь помочь мне воплотить мою мечту в реальность с помощью этой замечательной игры! Ни дня не пройдёт без болтовни и весёлых занятий с членами нашего клуба: Саёри — юный солнечный лучик, который больше всего ценит счастье; Нацуки — обманчиво миловидная девушка, которая на деле может отвесить неслабую затрещину; Юри — робкая и таинственная, находит утешение в мире книг; И, конечно же, Моника — лидер клуба! Это я! Жду с нетерпением, когда ты с нами подружишься и поможешь литературному клубу стать родным местом для всех его участников. Хотя я и сейчас уже вижу, что ты душка! Обещаешь проводить большую часть времени со мной? Добро пожаловать в Литературный клуб! Я всегда мечтала создать на основе своих увлечений нечто особенное, и раз уж ты вступил в клуб, то можешь помочь мне воплотить мою мечту в реальность с помощью этой замечательной игры! Ни дня не пройдёт без болтовни и весёлых занятий с членами нашего клуба: Саёри — юный солнечный лучик, который больше всего ценит счастье; Нацуки — обманчиво миловидная девушка, которая на деле может отвесить неслабую затрещину; Юри – робкая и таинственная, находит утешение в мире книг; И, конечно же, Моника – лидер клуба! Это я! Жду с нетерпением, когда ты с нами подружишься и поможешь литературному клубу стать родным местом для всех его участников. Хотя я и сейчас уже вижу, что ты душка! Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со мной? Обещаешь проводить большую часть времени со""")

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/have a nice weekend!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "Так-с, пора фестивалить!"
    show natsuki 4k zorder 2 at t11
    n "Ух ты, ты пришёл раньше меня?"
    n "Я думала, что я довольно ра...{nw}"
    show natsuki scream at h11
    n "А-А-А!"
    n "А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А-А!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "Нацуки убежала."
    m "..."
    show monika 2b zorder 2 at t11
    m "Я здесь!"
    m 2d "[player], что-то случилось?"
    m "Нацуки только что промчалась мимо меня..."
    m 2i "...Ой..."
    m "...О-ой."
    m 2r "..."
    m 2l "А-ха-ха-ха!"
    m "Какая досада."
    m 2d "Погоди, [player], ты здесь все выходные проторчал?"
    m "Ох, чёрт..."
    m 2g "Я не заметила, что скрипт настолько битый."
    m "Очень-очень извиняюсь!"
    m "Наверное, это было ужасно скучно..."
    m 2e "Сейчас исправлю, окей?"
    m "Секундочку..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr успешно удалён.") from _call_updateconsole_18
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr успешно удалён.") from _call_updateconsole_19
    $ delete_character("natsuki")
    pause 1.0
    m 2a "Почти закончила."
    m 2j "Только кексом перекушу по-быстрому!"
    $ gtext = glitchtext(10)
    "Моника сорвала фольгу с [gtext] подноса и взяла кекс."
    m 2b "Серьёзно, они лучшие!"
    m "Я не могла не угоститься, зная, что это последний шанс их попробовать."
    m 2a "Ну знаешь, перед тем, как они перестанут существовать и всё такое."
    m "...Но в любом случае я не имею права растягивать твоё ожидание."
    m 2j "Просто немножко потерпи, хорошо?"
    m 2a "Это займёт всего секунду."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
