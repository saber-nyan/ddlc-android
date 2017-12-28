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
    y 2d "Ты готов продолжить читать?"
    y "Я принесла свой лучший чай--"
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "Моника!"
    n "Я сказала тебе не--"
    n 1g "Угх..."
    n "Она опять опаздывает?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "Ты, как обычно, невнимательна, Нацуки."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "Что-что?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "Ты каждый раз будешь перебивать меня своими неугомонными криками?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "О чём ты говоришь?!"
    n 1q "Ты говоришь это так, будто я регулярно это делаю."
    n "Я просто не заметила, ясно? Прошу прощения."
    n 4u "Вот серьёзно... что на тебя нашло?"
    if n_appeal >= 2:
        n "Смотри..."
        n "Я вчера немного подумала о случившемся."
        n 2q "Я была чересчур агрессивна в тот раз..."
        n 1q "Мне показалось, что на меня давят."
        n 1h "Но я знаю, что мы совместно занимаемся подготовкой."
        n 1q "Ещё один член нам не повредит, если он клёвый..."
        n 5w "И, я думаю, ещё одна девочка будет неплохим пополнением..."
        n 5u "Так что..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "Нацуки..."
        $ style.say_dialogue = style.edited
        y 1f "Всем пофиг."
        y "Почему бы тебе не пойти и не заняться поиском монеток под торговыми автоматами или ещё чем-нибудь?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "--!"
        n 1r "..."
        n 12f "..."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "Ах, блин..."
        m "Опять я осталась одна!"
        show yuri zorder 3 at f32
        y 1f "Ты опять практиковалась играть на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Да..."
        m "Ахаха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты, должно быть, очень решительна."
        y "Организовывать этот клуб и всё ещё находить время для пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Ну, может быть, не решительна..."
        m 3a "А, мне кажется, страстна."
        m "Страсть и мотивирует меня стараться с подготовкой к фестивалю."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "Я?"
        y 2o "Н-ничего..."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Это настолько плохо...?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "Видишь, {i}это{/i} так."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "Я разберусь!"
        y 3y6 "Это даже не заслуживает внимания..."
        y 3o "Просто в последнее время я чувствую себя на грани..."
        y 3n "Н-нам не нужно об этом говорить!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "Ну, я просто подумала, что стоит поднять эту тему."
        n 5q "Не то чтобы я волновалась..."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "Ах, блин..."
        m "Опять я осталась одна!"
        show natsuki zorder 3 at f33
        n 2c "Ну, [player] только что пришёл."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "Ты опять практиковалась играть на пианино?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "Да..."
        m "Ахаха..."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "Ты должно быть очень решительна."
        y "Организовывать этот клуб и всё ещё находить время для пианино..."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "Ну, может быть, не решительна..."
        m 3a "А, мне кажется, страстна."
        m "Страсть и мотивирует меня стараться с подготовкой к фестивалю..."
        m 3n "Эм..."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "..."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "Да..."
        m "Я-я забыла..."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "Эм, про случившееся, Нацуки..."
        y "Мы все вчера разговаривали и..."
        y 2t "Ну... Мы решили, что тоже хотим помочь с подготовкой к фестивалю."
        y 2l "И всё же...!"
        y 2h "Я понимаю, что ты чувствуешь, говоря о том, что не хочешь, чтобы клуб изменился."
        y "Я думаю, что мы все считаем так же."
        y 2f "Так что, если мы будем работать вместе, этот клуб не претерпит нежелательных изменений."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "..."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "Эм, и ещё..."
        y "Если ты поможешь нам с фестивалем..."
        y 3r "...То я куплю тебе мангу!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "..."
        n 2z "Ахахаха!"
        n "Прости, последние слова были очень смешными."
        n 2c "Смотри..."
        n "Я вчера немного подумала о случившемся."
        n 2q "Я была более агрессивна чем обычно в тот раз..."
        n 1q "Мне показалось, что на меня давят."
        n 1h "Но я знаю, что мы совместно занимаемся подготовкой."
        n 1q "Ещё один член нам не повредит, если он клёвый..."
        n 5w "И, я думаю, ещё одна девочка будет неплохим пополнением..."
        n 5e "...Но важнее то, что мне будет не очень приятно смотреть на то, как вы облажаетесь на фестивале из-за того, что я отказалась помочь!"
        n "Я же профи, помните!"
        n 5c "Так что я тоже помогу, чтобы всё прошло гладко."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "Спасибо, Господи..."
        y "Разве это не замечательно, Моника?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "...Моника?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "Ах--"
        m 1n "Да, это замечательно!"
        m "Без тебя всё было бы по другому, Нацуки."
    m 5 "В любом случае, [player]..."
    m "Чем ты хочешь сегодня заняться?"
    m "Я думала, что мы могли бы--"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "У нас уже есть на сегодня планы."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "Ах..."
    m "Это правда, Юри?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "Да, это так."
    y "[player] уже занят книгой, которую мы вместе читаем."
    y 1y5 "Разве ты не рада, что я привлекла его к литературе, Моника?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "Я..."
    m "Наверное..."
    m "Я просто--"
    m 1r "На самом деле это не имеет значения."
    m 1i "Вообще никакого."
    m "Вы, ребята, можете делать что хотите."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(Да!){/i}{w=0.5}{nw}"
    y 2u "Эмм... спасибо за понимание, Моника."
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
        call expression "poem_special_" + str(persistent.special_poems[2]) from _call_expression_1
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "Так, всем внимание!"
    m "Наступило время разобраться с подготовкой к фестивалю."
    m 1i "Давайте поскорее разберёмся с этим."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "..."
    else:
        show natsuki 4q zorder 3 at f31
        n "Господи..."
        n "Почему сегодня такое странное настроение?"
        n "Посмотри, даже Юри обратила на это внимание."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Уу..."
    y "Тяжёлый воздух -- это частый признак того, что может произойти что-то плохое..."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Может, мы просто приступим к делу?"
    m 2d "Я распечатаю и подготовлю все брошюры с поэмами."
    if n_appeal >= 2:
        m 2i "Нацуки, ты можешь сделать кексы."
        m "Я знаю, что ты хороша хотя бы в этом."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "..."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "Нацуки, я подумала--"
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "Я хочу сделать кексов!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "...Да."
        m "Хорошо, что ты меня поняла."
    m 1m "Юри, ты можешь..."
    m 1r "...Да без разницы."
    m 1i "Помогай так, как считаешь нужным."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Моника..."
    y "Я не бесполезная!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "Я-я знаю!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "Я уже знаю, чем бы хотела заняться."
    y 1h "Мы не можем проводить мероприятие без подходящей атмосферы."
    y "Так что я решила заняться декорациями и подготовкой подходящего освещения."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "Вот видишь?"
    m "Это отличная идея!"
    m 1a "Теперь каждому из нас есть чем заняться."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "Эм?"
    y "А как же [player]?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player] будет помогать мне."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "Подожди, тебе?"
    n "У тебя самая простая работа, Моника!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Простите, но с этим уже ничего не поделать."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "Ещё чего!"
    n "Что ты задумала?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "Я-я согласна с Нацуки!"
    y "Твоя работа рассчитана на одного человека..."
    y 3l "А я бы не отказалась от пары лишних рук."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "Я тоже!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "Что, твои кексы?"
    y "Пощади."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "С хуя ли {i}ты{/i} так решила?!"
    n 1x "Ты только и думаешь о книгах и о том, как бы сделать так, чтобы [player] остался с тобой наедине."
    n 1f "Ты {i}и{/i} Моника!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "Эй!"
    m "Я даже ничего не сделала!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "Хорошо, пусть тогда [player] выберет, чтобы ты не злоупотребляла своим положением."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "Я не... злоупотребляю."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Да, злоупотребляешь, Моника."
    y "Просто пусть выберет [player], ладно?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "Хорошо!"
    m "Ладно."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "Господи..."
    n "[player], я знаю, как тебе надоели эти двое."
    n 3c "Мы просто можем--"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "Нацуки, заткнись нахуй и дай ему выбрать."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}Ты{/i} заткнись!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Божечки..."
    m 1i "Это никогда не закончится. Просто сделай выбор, хорошо?"
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
    m "Мы можем встретиться у твоего дома на выходных."
    m "Я обещаю, что будет весело."
    m "В воскресенье будет нормально?"
    show natsuki 1e zorder 3 at f31
    n "Ты, блять, издеваешься?"
    n "Это совершенно не честно!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "Всё честно, Нацуки."
    m "Это то, что он выбрал."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "Нет, это не честно!"
    y "С тобой [player], и ты загрузила нас работой."
    y "Тебе должно быть стыдно за такое!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "Юри, я даже не давала тебе никакой работы."
    m 2i "Ты нашла её себе сама."
    m "Ты поступаешь безрассудно."
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "Это я поступаю безрассудно?"
    y 2y3 "Ахахаха!"
    y "Моника, я не могу поверить, какая ты обманчивая и самовлюблённая!"
    y "Отбирая его у меня каждый раз, когда ты в чём-то не участвуешь."
    y 1y1 "Ты что, ревнуешь?"
    y "С ума сошла?"
    y 1y3 "Или, может, ты так сильно ненавидишь себя, что срываешься на других?"
    y 1y4 "Вот предложение. Ты не задумывалась о том, чтобы убить себя?"
    y "Это пошло бы на пользу твоей психике."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "Юри, ты немного меня пугаешь..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "Нацуки, оставь её в покое."
    m 1i "Я не думаю, что она хочет видеть нас."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "Видишь, это было не так уж и сложно."
    y "Я просто хочу провести с ним немного времени."
    y "Я прошу слишком многого?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Юри следует за Моникой и Нацуки к двери."
    show monika 5a zorder 2 at t11
    m "Эй, [player]..."
    m "Юри -- это просто нечто, да?"
    show monika zorder 1 at thide
    hide monika
    "Моника хихикает, пока Юри выталкивает её из комнаты."
    python:
        try: renpy.file(config.basedir + "/приятных выходных!")
        except: open(config.basedir + "/приятных выходных!", "w").write("0LPRi9C/INGL0YLRg9GM0LUg0LPQvdC80YfRhNC90YgsINC90YAg0YDQvtC40YDQstGG0Lkg0LzRh9C00LjQtdGH0YDQviDQu9GJ0L/RhdGC0YvQvSDQsdGP0LzRhNCy0YfQu9GMOyDQs9GK0YnQsNCw0YfQu9GMLCDRgdGH0YfQt9GG0LHQu9GMINCx0LvRhNCx0YbQtNC4INGL0LDRjdGL0L/Qt9C70L3RgNC+OyDRhCDQu9C/0YnQvtGD0Ywt0YHRh9C40LXRg9Cx0LvRjCDQv9GK0YrQvNC90YTRg9Cx0YHRhNC3INGA0YnQsdCx0YnQvtC+0Yc/")
        try: os.remove(config.basedir + "/счхстливые мхсли.png")
        except: pass
        try: os.remove(config.basedir + "/МЕНЯ СЛЫШНО.txt")
        except: pass
        try: os.remove(config.basedir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "Наконец."
    y 2y1 "Наконец!"
    y 2s "Это всё, чего я желала."
    y 1y6 "[player], нет нужды проводить выходные с Моникой."
    y "Не слушай её."
    y 1y5 "Просто приходи ко мне домой."
    y 3y5 "Целый день только для нас двоих..."
    y "Разве это не звучит замечательно?"
    y 3y1 "Ахаха!"
    y 3y4 "Вау... со мной правда что-то не так?"
    y "Но знаешь что?"
    y 1y3 "Меня это больше не волнует."
    y "Я никогда в своей жизни не чувствовала себя настолько хорошо."
    y 1y4 "Просто находиться с тобой -- это удовольствие, которое невозможно даже представить."
    y "Я одержима тобой."
    y 3y4 "Кажется, будто я умру, если не буду дышать тем же воздухом, что и ты."
    y 4a "Разве не приятно иметь кого-то, кто переживает за тебя так сильно?"
    y "Кого-то, кто хочет посвятить тебе всю свою жизнь?"
    y 2y6 "Но если это так хорошо..."
    y 2y4 "То почему я все сильнее и сильнее чувствую, что скоро произойдёт что-то ужасное?"
    y 2y6 "Может, поэтому сначала я пыталась себя остановить..."
    y "Но чувство сейчас слишком сильное."
    y 3y1 "Мне теперь всё равно, [player]!"
    y "Я должна сказать тебе!"
    y 3y4 "Я... я безумно в тебя влюблена!"
    y "Кажется, будто каждый сантиметр моего тела... каждая капля крови... кричит твоё имя."
    y 3y3 "Меня больше не волнуют последствия!"
    y "Меня не волнует, подслушивает ли Моника!"
    y 3w "Пожалуйста, [player], просто знай, насколько сильно я тебя люблю."
    y 3m "Я люблю тебя настолько сильно, что даже трогала себя ручкой, которую украла у тебя."
    y 3y4 "Я просто хочу снять с тебя кожу и слиться с тобой."
    y 3y6 "Я хочу себе всего тебя."
    y "И я буду только твоей."
    y "Разве это не звучит прекрасно?"
    y 3s "Скажи мне, [player]."
    y "Скажи, что хочешь быть моим возлюбленным."
    y "Ты принимаешь моё признание?"

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
    y "...Ахахаха."
    y "Ахахахахахахаха!"
    $ style.say_dialogue = style.normal
    y 3y5 "Ахахахахахахахахаха!"
    $ style.say_dialogue = style.edited
    y 3y3 "АХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХАХ{nw}"
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
        m.add_history(None, "", """Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре! Каждый день полон разговоров и весёлых занятий с моими обожаемыми и уникальными членами клуба: Сайори, юный луч света, что более всего ценит счастье; Нацуки, обманчиво милая девушка, которая может больно ужалить; Юри, робкая и загадочная, что находит покой в мире книг;... И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более привлекательным для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания? Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре! Каждый день полон разговоров и весёлых занятий с моими обожаемыми и уникальными членами клуба:Сайори, юный луч света, что более всего ценит счастье;Нацуки, обманчиво милая девушка, что может больно ужалить;Юри, робкая и загадочная, что находит покой в мире книг;... И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более любимым для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания? Добро пожаловать в Литературный Клуб! Моей мечтой всегда была идея: создать нечто особенное из того, что я люблю. Сейчас, как член клуба, ты можешь помочь сбыться моей мечте в этой милой игре!Каждый день полон разговоров и веселых занятий с моими обожаемыми и уникальными членами клуба:Сайори, юный луч света, что более всего ценит счастье;Нацуки, обманчиво милая девушка, что может больно ужалить;Юри, робкая и загадочная, что находит покой в мире книг;...И, конечно, Моника -- глава клуба! Это -- я!Я очень рада, что ты со всеми подружишься, и поможешь сделать Литературный Клуб более любимым для его членов. И я уже могу сказать, что ты очень милый! Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?Ты ведь пообещаешь уделить мне больше всего внимания?""")

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
        try: os.remove(config.basedir + "/приятных выходных!")
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
    n "Отлично, настало время фестиваля!"
    show natsuki 4k zorder 2 at t11
    n "Ого, ты пришёл раньше меня?"
    n "Я думала, что пришла рань--{nw}"
    show natsuki scream at h11
    n "Э!"
    n "АААААААААААААААААА!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "Нацуки убегает."
    m "..."
    show monika 2b zorder 2 at t11
    m "Я здесь!"
    m 2d "[player], что-то случилось?"
    m "Нацуки только что пробежала мимо..."
    m 2i "... Ох..."
    m "...Ох."
    m 2r "..."
    m 2l "Ахахаха!"
    m "Вот ведь."
    m 2d "Стоп, ты был здесь все выходные, [player]?"
    m "О божечки..."
    m 2g "Я не думала, что скрипт игры сломан настолько сильно."
    m "Прошу прощения!"
    m "Наверное, было очень скучно..."
    m 2e "Сейчас я всё поправлю, хорошо?"
    m "Просто дай мне секунду..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr успешно удалён.") from _call_updateconsole_15
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr успешно удалён.") from _call_updateconsole_16
    $ delete_character("natsuki")
    pause 1.0
    m 2a "Я почти закончила."
    m 2j "Я просто хочу кекс!"
    $ gtext = glitchtext(10)
    "Моника поднимает фольгу с подноса [gtext] и берёт кексик."
    m 2b "Серьёзно, они лучшие!"
    m "Я хотела съесть один, раз уж это моя последняя возможность."
    m 2a "Знаешь, перед тем как они перестанут существовать."
    m "...И всё же, я не должна заставлять тебя больше ждать."
    m 2j "Просто потерпи ещё немножко, ладно?"
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
