label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Здравствуй ещё раз, [player]!"
    m "Приятно видеть, что ты не сбежал от нас. Хахаха!"
    mc "Хех, не беспокойся."
    mc "Пусть это и странно для меня, но я, по крайней мере, держу своё слово."
    show monika zorder 1 at thide
    hide monika
    "Что ж, я вернулся в Литературный Клуб."
    "Я был последним, кто пришёл, поэтому остальные, похоже, уже на своих местах."
    show yuri glitch2 zorder 2 at t32
    y "Спасибо за то, что держишь обещание, [player]."
    y "Надеюсь, это не слишком обременяюще для тебя."
    y 1u "Затягивать тебя с головой в литературу, когда ты к ней ещё толком не привык..."
    show natsuki glitch1 zorder 2 at i33
    n "О, да ладно тебе! Как будто он заслуживает поблажку."
    n 4e "Моника всё равно должна была тебя сюда затащить."
    n "Не знаю, будешь ли ты просто приходить сюда общаться или заниматься чем-то ещё..."
    n "Но если не станешь относиться к этому серьёзно, тогда ты не увидишь здесь счастливого конца."
    show monika 2b onlayer front at l41
    m "Нацуки, ты слишком много говоришь для той, кто держит в клубной комнате свою коллекцию манги."
    n 4o "М-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Нацуки замешкалась между словами \"Моника\" и \"Манга\"."
    show natsuki at h33
    n 1v "Манга -- тоже литература!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Будучи побеждённой, Нацуки шлепнулась обратно на своё место."
    show yuri 2s zorder 2 at t11
    y "Прошу прощения, [player]..."
    y "Твой комфорт будет нашей первостепенной задачей, хорошо?"
    show yuri 2g
    "Юри бросает в сторону Нацуки разочарованный взгляд."
    y 1a "Эм, итак..."
    y "Сейчас, когда ты в нашем клубе и это всё..."
    y "...возможно, ты захочешь выбрать книгу?"
    mc "Чтож..."
    mc "Я в любом случае не могу отказаться."
    mc "Как ты сказала, я сейчас в этом клубе."
    mc "Думаю, правильно будет сделать что-то подобное, раз уж ты настаиваешь."
    y 4b "П-подожди..."
    y "Я не это имела в виду!"
    y "Уу..."
    y "Если ты на самом деле не хочешь, то забудь о том, что я сказала..."
    mc "А... Нет, дело не в этом, Юри."
    mc "Я хочу стать частью этого клуба."
    mc "Так что даже при том, что я редко читаю, я с радостью выберу книгу, если хочешь."
    y 3t "Т-ты уверен?.."
    y "Мне просто показалось..."
    y 3u "...Я ведь вице-президент и всё такое..."
    y "...Я должна помочь тебе начать с того, что тебе может понравиться."
    "Юри достаёт из сумки книгу."
    y 1s "Я не хотела, чтобы ты почувствовал себя брошенным..."
    y "Поэтому я выбрала книгу, которая может тебе понравиться."
    y "Это короткое чтиво, поэтому оно должно удержать твое внимание, даже если ты не часто читаешь."
    y "И мы могли бы, ну, знаешь..."
    show yuri at sink
    y 4b "Обсудить её... если хочешь..."
    "Э-это..."
    "Как у этой девушки получается быть такой милой?"
    "Она даже взяла с собой книгу, которая, по её мнению, может понравиться мне, несмотря на то, что читаю я не так много..."
    mc "Юри, спасибо тебе! Я обязательно прочитаю её!"
    "Я с энтузиазмом схватил книгу."
    show yuri 2m zorder 2 at t11
    y "Фух..."
    y 2a "Что ж, ты можешь читать её в своем темпе."
    y "Буду ждать твоего мнения."
    show yuri zorder 1 at thide
    hide yuri
    show layer master


    "Я думал, что сейчас, когда все освоились, Моника объявит о каком-нибудь запланированном клубном мероприятии."
    "Но, похоже, сегодня не тот случай."
    "Юри уже зарылась лицом в книгу."
    "Я не мог не заметить напряжённого выражения её лица: она будто ждала этой возможности."
    "Нацуки, тем временем, роется в шкафу."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_3

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Фух..."
    "Думаю, это все."
    "Я оглядел комнату."
    "Кажется, это немного более напряженно, чем я ожидал."
    "Как если бы все начали обвинять меня в моих несомненно посредственных писательских навыках..."
    "Даже если они и будут относиться ко мне с пониманием, нет никаких шансов, что мои поэмы смогут соперничать с их."
    "Это ведь Литературный Клуб, как никак."
    "Я вздыхаю."
    "Полагаю, я сам позволил себя в это втянуть."
    "В другом конце комнаты Моника пишет что-то в теради."
    "Мой взгляд упал на Юри и Нацуки."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Они робко обменялись листами бумаги со своими поэмами."
    show yuri 2i zorder 2 at t21
    "В то время как они читали, я наблюдал за каждым изменением выражения их лиц."
    "Нацуки расстроенно опустила брови."
    "В то же время, Юри улыбалась с грустью."
    show natsuki zorder 3 at f22
    n 1q "{i}(Что это за стиль такой...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "М?"
    y "Эм... ты что-то сказала?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Оу, да ничего."
    "Нацуки пренебрежительно одной рукой положила поэму на стол."
    n "Полагаю, можно сказать, что это довольно причудливо."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ээ-- Спасибо..."
    y "А твоя... милая..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Милая?"
    n 1h "Ты полностью проглядела символичность или что?"
    n "Явно же, что речь о чувстве обреченности."
    n "Как это может быть милым?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "Я-я поняла это!"
    y "Я просто имела в виду..."
    y 3h "Этот стиль, я считаю..."
    y "Я просто пыталась сказать что-то приятное..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Э?"
    n 4w "Хочешь сказать, что тебе пришлось настолько потрудиться, чтобы сказать что-то приятное?"
    n "Спасибо, но в итоге вышло не очень-то приятно!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Эм..."
    y "Ну, у меня есть парочка советов..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Хмпф."
    n "Если бы я искала совета, то спросила бы кого-то, кому на самом деле понравилось."
    n "А такие {i}есть{/i}, кстати говоря."
    n 5e "Она понравилась Монике."
    n "И [player] тоже её оценил!"
    n "Поэтому, я сама с радостью дам тебе несколько советов."
    n "Во-первых..."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Прошу прощения..."
    y "Я ценю предложение, но я работала над своим авторским стилем в течение долгого времени."
    y 2h "Он вряд ли изменится в ближайшее время, разве что, если я наткнусь на что-нибудь особенно вдохновляющее."
    y "Но этого пока не произошло."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Нх...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "И мою поэму [player] тоже высоко оценил."
    y "Он даже сказал, что был ей впечатлен."
    stop music fadeout 1.0
    "Нацуки резко вскочила."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Оо?"
    n "Я и не заметила, что ты настолько хочешь впечатлить нашего нового участника, Юри."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "Э-Ээ?!"
    y "Это не то, что я...!"
    y 1o "Уу..."
    y "Ты... ты просто..."
    "Юри также вскочила."
    y 2r "Может, тебе просто завидно, что [player] ценит моё мнение больше, чем твоё!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Хаа! И с чего ты решила, что он не ценит {i}моё{/i} мнение больше?"
    n "Настолько самоуверенна?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "Я...!"
    y "Нет..."
    y "Если бы я была самоуверенна..."
    y 1r "...Я бы осознанно из кожи вон лезла, чтобы делать всё, что я делаю, чересчур милым!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Ууууу...!"
    n "Ладно, знаешь что?!"
    n "По крайней мере, я не та, чья грудь магически выросла на размер с тех пор, как [player] начал ходить сюда!!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "Н-Нацуки!"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "Эм, Нацуки, это немного--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "Это тебя не касается!"
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
    y "Вот так переносить на других свои комплексы..."
    y "Ты действительно ведёшь себя так же незрело, как выглядишь."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}Я?{/i} Кто бы говорил, несдержанная выпендрежная сучка!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "В-Выпендрёжная?.."
    y 2r "Уж прости, что мой образ жизни слишком сложен для твоего психологического возраста!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "Видишь?"
    n "Ты только что подтвердила мои слова!"
    n 4e "Знаешь, большинство людей после окончания средних классов спускаются на землю."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "Если ты хочешь что-то доказать, то перестань утомлять окружающих своим тошнотворным отношением!"
    y "Думаешь, ты можешь уравновесить свой отвратительный характер милой одеждой и поведением?"
    y 1k "Единственное, что в тебе мило, -- это то, как ты стараешься."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "Ух ты, будь осторожна, а то порежешься о тонкие грани своей натуры, Юри."
    n "О, подожди... Уже порезалась, не так ли?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "Т-ты только что обвинила меня в том, что я себя режу?"
    y 3r "Что с твоей ебучей башкой не так?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Да, давай!"
    n "Пусть [player] услышит всё, что ты на самом деле думаешь!"
    n "Уверена, после этого он влюбится в тебя до безумия!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "А-ах!.."
    show yuri zorder 2 at t21
    "Внезапно Юри поворачивается ко мне, будто она только сейчас заметила, что я стою рядом."
    show yuri zorder 3 at f21
    y 2n "[player]!.."
    y "Она... она просто пытается выставить меня в плохом свете!.."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "Это не так!"
    n "Это она всё начала!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}Как я вообще оказался в это втянут?!{/cps}{nw}"
    "{cps=*2}Не то чтобы я хоть что-то знаю о писательстве...{/cps}{nw}"
    "{cps=*2}Но с кем бы я ни согласился, они, скорее всего, будут думать обо мне лучше!{/cps}{nw}"
    "{cps=*2}Что ж, конечно, это будет...{/cps}{nw}"
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
    m "Почему бы нам не\nвыйти наружу\nненадолго?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "Хорошо?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Прости за это..."
    m "Им действительно не стоило тебя втягивать."
    m 1e "Вероятно, нам лучше оставаться в стороне..."
    m "Вернёмся внутрь, когда они закончат кричать."
    m 5 "Ахаха..."
    m "Посредственный из меня президент, правда?"
    m 1m "Не могу даже толком поспорить с членами собственного клуба..."
    m "Хотела бы я иногда быть более убедительной."
    m "Но я никогда не умела решительно выступать против других..."
    m 1e "Ты ведь меня понимаешь?"
    m "Как бы то ни было..."
    m 1a "Если из-за этого тебе хочется проводить с ними меньше времени, ничего страшного."
    m 1j "Я с радостью проведу время с тобой вместо этого..."
    show monika zorder 1 at thide
    hide monika
    "Внезапно из комнаты выбегает Нацуки..."
    show natsuki 12h zorder 2 at t11
    n "..."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "...и быстро убегает."
    show monika 1l zorder 2 at t11
    m "Мамочки..."
    m "...Что ж, похоже, они закончили..."
    scene bg club_day2
    with wipeleft_scene
    y "Я этого не хотела..."
    y "Я этого не хотела..."
    y "Я этого не хотела..."
    "Юри качается из стороны в сторону, сидя за партой и схватившись руками за голову."
    mc "Юри?.."
    show yuri 4d zorder 2 at t11
    y "Я этого не хотела!"
    mc "Я-я тебе верю..."
    "Представить не могу, что Юри могла сказать Нацуки."
    "Или сказала."
    y "[player]."
    y "Пожалуйста, не относись ко мне плохо."
    y "Пожалуйста!"
    y "Я не такая!"
    y "Со мной сегодня что-то не так..."
    show monika 1d zorder 3 at f31
    m "Всё хорошо, Юри."
    m "Мы знаем, что ты этого не хотела."
    m 1j "Кроме того, я уверена, что к завтрашнему дню Нацуки всё забудет."
    m 1a "Полностью."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "В любом случае, собрание окончено. Вы можете идти."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "..."
    show yuri zorder 2 at t32
    "Юри смотрит на меня так, будто хочет что-то сказать."
    "Но продолжает посматривать на Монику."
    show yuri zorder 3 at f32
    y 2v "М-можешь идти, Моника..."
    y "Я бы хотела ненадолго задержаться."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "Я президент, так что уйду последней."
    m "Я подожду, пока ты закончишь."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "..."
    y "..."
    y "Что ж... я вице-президент, так что..."
    y "Позволь мне сегодня взять эту обязанность на себя."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "Юри, звучит так, будто ты почему-то не хочешь, чтобы я была рядом."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "Э-это не так!"
    y 3o "Это не так..."
    y 3n "Я просто..."
    y 3q "Сегодня не было времени на то, чтобы [player] смог обсудить со мной мою книгу..."
    y "Я просто буду... смущаться, если ты будешь слушать..."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}*Вздох*{/i}"
    m 1d "Думаю, на самом деле у меня нет выбора, не так ли?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "П-прости, что доставляю неприятности..."
    $ gtext = glitchtext(20)
    y 1s "Но я действительно ценю твое понимани{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "Но я действительно ценю то, что ты меня понимае{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
