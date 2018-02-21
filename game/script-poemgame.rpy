init python:
    import random


    class PoemWord:
        def __init__(self, word, sPoint, nPoint, yPoint, glitch=False):
            self.word = word
            self.sPoint = sPoint
            self.nPoint = nPoint
            self.yPoint = yPoint
            self.glitch = glitch


    POEM_DISLIKE_THRESHOLD = 29
    POEM_LIKE_THRESHOLD = 45


    full_wordlist = []
    poemwords_txt = u"""счастье,3,2,1
грусть,3,2,1
смерть,3,1,2
трагедия,3,1,2
одиночество,3,1,2
любовь,3,2,1
приключение,3,2,1
сладкий,3,2,1
возбуждение,3,2,1
фейерверк,3,2,1
романтика,3,2,1
слёзы,3,1,2
депрессия,3,1,2
сердце,3,2,1
свадьба,3,2,1
страсть,3,2,1
детство,3,2,1
веселье,3,2,1
цвет,3,2,1
надежда,3,1,2
друзья,3,2,1
семья,3,2,1
вечеринка,3,2,1
каникулы,3,2,1
ленивая,3,2,1
мечта,3,1,2
боль,3,1,2
праздник,3,2,1
кровать,3,2,1
пух,3,2,1
стыд,3,1,2
страх,3,1,2
тепло,3,2,1
цветок,3,2,1
утешение,3,2,1
танцы,3,2,1
петь,3,2,1
плакать,3,1,2
смеяться,3,2,1
мрачный,3,1,2
солнечный,3,2,1
тучка,3,2,1
спокойный,3,1,2
глупый,3,2,1
летающий,3,2,1
замечательный,3,2,1
неразделённая,3,1,2
роза,3,1,2
вместе,3,2,1
обещаю,3,2,1
очарование,3,2,1
красота,3,2,1
ободрение,3,2,1
улыбка,3,2,1
разбитое,3,1,2
драгоценная,3,2,1
молитва,3,1,2
неуклюжий,3,2,1
прости,3,1,2
природа,3,2,1
океан,3,2,1
ослеплять,3,2,1
особенный,3,2,1
музыка,3,2,1
счастливчик,3,2,1
невезение,3,1,2
громко,3,2,1
безмятежно,3,1,2
восторг,3,1,2
закат,3,2,1
светлячки,3,2,1
радуга,3,2,1
ранить,3,1,2
игра,3,2,1
искорка,3,2,1
рубцы,3,1,2
пусто,3,1,2
невероятно,3,2,1
горе,3,1,2
обнимать,3,1,2
незаурядный,3,2,1
потрясающий,3,2,1
поражение,3,1,2
безнадёжно,3,1,2
страдание,3,1,2
сокровище,3,2,1
блаженство,3,2,1
воспоминания,3,2,1
милый,2,3,1
воздушный,2,3,1
чистый,1,3,2
конфета,2,3,1
шопинг,2,3,1
щеночек,2,3,1
котёнок,2,3,1
облака,2,3,1
помада,1,3,2
парфе,2,3,1
клубника,2,3,1
розовый,2,3,1
шоколад,2,3,1
сердцебиение,1,3,2
поцелуй,1,3,2
мелодия,2,3,1
лента,2,3,1
прыгучий,2,3,1
доки-доки,2,3,1
кавай,2,3,1
юбка,2,3,1
щёки,2,3,1
email,2,3,1
липучка,2,3,1
подвижная,2,3,1
яркий,2,3,1
кусь,2,3,1 
фантазия,1,3,2
сахар,2,3,1
хихикать,2,3,1
зефир,2,3,1
подпрыгивать,2,3,1
прогуливать,2,3,1
покой,2,3,1
вертящийся,2,3,1
вращать,2,3,1
леденец,2,3,1
фу,2,3,1
пузырьки,2,3,1
шёпот,2,3,1
лето,2,3,1
водопад,1,3,2
купальник,2,3,1
ваниль,2,3,1
наушники,2,3,1
игры,2,3,1
носки,2,3,1
волосы,2,3,1
площадка,2,3,1
пеньюар,1,3,2
одеяло,1,3,2
молоко,2,3,1
надуться,2,3,1
ярость,2,3,1
папа,2,3,1
валентинка,2,3,1
мышь,1,3,2
свист,2,3,1
бип,2,3,1
зайчик,2,3,1
аниме,2,3,1
прыгать,2,3,1
решимость,1,1,3
суицид,2,1,3
воображение,2,1,3
скрытный,2,1,3
живучесть,1,1,3
существование,2,1,3
лучезарный,1,1,3
багряный,1,1,3
смерч,1,1,3
послеобраз,1,1,3
головокружение,1,1,3
дезориентированный,1,1,3
сущность,2,1,3
внешний,2,1,3
космос,2,1,3
смятение,1,1,3
загрязнение,1,1,3
интеллектуальный,1,1,3
анализ,1,1,3
энтропия,1,1,3
оживлённый,1,1,3
сверхъестественное,2,1,3
несовпадающий,1,1,3
гнев,2,1,3
ниспосланный,2,1,3
резня,2,1,3
философия,1,1,3
неустойчивый,1,1,3
упорный,1,1,3
аура,2,1,3
нестабильный,1,1,3
преисподняя,2,1,3
неспособный,2,1,3
судьба,2,1,3
непогрешимый,1,1,3
агонизирующий,2,1,3
противоречие,1,1,3
неконтролируемый,2,1,3
предельный,1,1,3
избегать,2,1,3
сон,2,2,3
катастрофа,2,1,3
отчётливый,2,1,3
трепещущий,1,2,3
вопрос,1,2,3
терзать,2,1,3
суждение,1,1,3
клетка,1,2,3
взрываться,1,2,3
удовольствие,1,2,3
вожделение,1,2,3
ощущение,1,2,3
кульминация,1,2,3
электричество,1,2,3
отречься,1,1,3
презирать,2,1,3
бесконечный,2,1,3
вечность,2,1,3
время,2,1,3
вселенная,2,1,3
нескончаемый,2,1,3
дождевые капли,2,1,3
домогаться,1,1,3
необузданный,1,1,3
пейзаж,2,1,3
портрет,2,1,3
поездка,2,1,3
скудный,1,1,3
беспокойство,2,1,3
пугающий,2,1,3
ужас,2,1,3
меланхолия,2,1,3
проницательность,2,1,3
искупить,2,1,3
дыхание,1,2,3
пленный,2,1,3
желание,1,2,3
кладбище,2,1,3"""
    for line in poemwords_txt.splitlines():
        
        line = line.strip()
        
        if line == '' or line[0] == '#': continue
        
        
        x = line.split(',')
        full_wordlist.append(PoemWord(x[0], float(x[1]), float(x[2]), float(x[3])))

    seen_eyes_this_chapter = False
    sayoriTime = renpy.random.random() * 4 + 4
    natsukiTime = renpy.random.random() * 4 + 4
    yuriTime = renpy.random.random() * 4 + 4
    monikaTime = renpy.random.random() * 4 + 4
    sayoriPos = 0
    natsukiPos = 0
    yuriPos = 0
    monikaPos = 0
    sayoriOffset = 0
    natsukiOffset = 0
    yuriOffset = 0
    monikaOffset = 0
    sayoriZoom = 1
    natsukiZoom = 1
    yuriZoom = 1
    monikaZoom = 1

    def randomPauseSayori(trans, st, at):
        if st > sayoriTime:
            global sayoriTime
            sayoriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseNatsuki(trans, st, at):
        if st > natsukiTime:
            global natsukiTime
            natsukiTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseYuri(trans, st, at):
        if st > yuriTime:
            global yuriTime
            yuriTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomPauseMonika(trans, st, at):
        if st > monikaTime:
            global monikaTime
            monikaTime = renpy.random.random() * 4 + 4
            return None
        return 0

    def randomMoveSayori(trans, st, at):
        global sayoriPos
        global sayoriOffset
        global sayoriZoom
        if st > .16:
            if sayoriPos > 0:
                sayoriPos = renpy.random.randint(-1,0)
            elif sayoriPos < 0:
                sayoriPos = renpy.random.randint(0,1)
            else:
                sayoriPos = renpy.random.randint(-1,1)
            if trans.xoffset * sayoriPos > 5: sayoriPos *= -1
            return None
        if sayoriPos > 0:
            trans.xzoom = -1
        elif sayoriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * sayoriPos
        sayoriOffset = trans.xoffset
        sayoriZoom = trans.xzoom
        return 0

    def randomMoveNatsuki(trans, st, at):
        global natsukiPos
        global natsukiOffset
        global natsukiZoom
        if st > .16:
            if natsukiPos > 0:
                natsukiPos = renpy.random.randint(-1,0)
            elif natsukiPos < 0:
                natsukiPos = renpy.random.randint(0,1)
            else:
                natsukiPos = renpy.random.randint(-1,1)
            if trans.xoffset * natsukiPos > 5: natsukiPos *= -1
            return None
        if natsukiPos > 0:
            trans.xzoom = -1
        elif natsukiPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * natsukiPos
        natsukiOffset = trans.xoffset
        natsukiZoom = trans.xzoom
        return 0

    def randomMoveYuri(trans, st, at):
        global yuriPos
        global yuriOffset
        global yuriZoom
        if st > .16:
            if yuriPos > 0:
                yuriPos = renpy.random.randint(-1,0)
            elif yuriPos < 0:
                yuriPos = renpy.random.randint(0,1)
            else:
                yuriPos = renpy.random.randint(-1,1)
            if trans.xoffset * yuriPos > 5: yuriPos *= -1
            return None
        if yuriPos > 0:
            trans.xzoom = -1
        elif yuriPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * yuriPos
        yuriOffset = trans.xoffset
        yuriZoom = trans.xzoom
        return 0

    def randomMoveMonika(trans, st, at):
        global monikaPos
        global monikaOffset
        global monikaZoom
        if st > .16:
            if monikaPos > 0:
                monikaPos = renpy.random.randint(-1,0)
            elif monikaPos < 0:
                monikaPos = renpy.random.randint(0,1)
            else:
                monikaPos = renpy.random.randint(-1,1)
            if trans.xoffset * monikaPos > 5: monikaPos *= -1
            return None
        if monikaPos > 0:
            trans.xzoom = -1
        elif monikaPos < 0:
            trans.xzoom = 1
        trans.xoffset += .16 * 10 * monikaPos
        monikaOffset = trans.xoffset
        monikaZoom = trans.xzoom
        return 0



label poem(transition=True):
    stop music fadeout 2.0
    if persistent.playthrough == 3:
        scene bg notebook-glitch
    else:
        scene bg notebook
    show screen quick_menu
    if persistent.playthrough == 3:
        show m_sticker at sticker_mid
    else:
        if persistent.playthrough == 0:
            show s_sticker at sticker_left
        show n_sticker at sticker_mid
        if persistent.playthrough == 2 and chapter == 2:
            show y_sticker_cut at sticker_right
        else:
            show y_sticker at sticker_right
        if persistent.playthrough == 2 and chapter == 2:
            show m_sticker at sticker_m_glitch
    if transition:
        with dissolve_scene_full
    if persistent.playthrough == 3:
        play music ghostmenu
    else:
        play music t4
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    if persistent.playthrough == 0 and chapter == 0:
        call screen dialog("Пора сочинять стихотворение!\n\nВыбери слова, которые могут понравиться твоей любимой девушке\nиз клуба. И тогда между тобой и той, кому твой стих понравится больше всех,\nможет произойти нечто приятное!", ok_action=Return())
    python:
        poemgame_glitch = False
        played_baa = False
        progress = 1
        numWords = 20
        sPointTotal = 0
        nPointTotal = 0
        yPointTotal = 0
        wordlist = list(full_wordlist)

        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        sayoriPos = renpy.random.randint(-1,1)
        natsukiPos = renpy.random.randint(-1,1)
        yuriPos = renpy.random.randint(-1,1)
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1





        while True:
            ystart = 160
            if persistent.playthrough == 2 and chapter == 2:
                pstring = ""
                for i in range(progress):
                    pstring += "1"
            else:
                pstring = str(progress)
            ui.text(pstring + "/" + str(numWords), style="poemgame_text", xpos=810, ypos=80, color='#000')
            for j in range(2):
                if j == 0: x = 440
                else: x = 680
                ui.vbox()
                for i in range(5):
                    if persistent.playthrough == 3:
                        s = list("Моника")
                        for k in range(6):
                            if random.randint(0, 4) == 0:
                                s[k] = ' '
                            elif random.randint(0, 4) == 0:
                                s[k] = random.choice(nonunicode)
                        word = PoemWord("".join(s), 0, 0, 0, False)
                    elif persistent.playthrough == 2 and not poemgame_glitch and chapter >= 1 and progress < numWords and random.randint(0, 400) == 0:
                        word = PoemWord(glitchtext(80), 0, 0, 0, True)
                    else:
                        word = random.choice(wordlist)
                        wordlist.remove(word)
                    ui.textbutton(word.word, clicked=ui.returns(word), text_style="poemgame_text", xpos=x, ypos=i * 56 + ystart)
                ui.close()
            
            t = ui.interact()
            if not poemgame_glitch:
                if t.glitch:
                    poemgame_glitch = True
                    renpy.music.play(audio.t4g)
                    renpy.scene()
                    renpy.show("white")
                    renpy.show("y_sticker glitch", at_list=[sticker_glitch])
                elif persistent.playthrough != 3:
                    renpy.play(gui.activate_sound)
                    if persistent.playthrough == 0:
                        if t.sPoint >= 3:
                            renpy.show("s_sticker hop")
                        if t.nPoint >= 3:
                            renpy.show("n_sticker hop")
                        if t.yPoint >= 3:
                            renpy.show("y_sticker hop")
                    else:
                        if persistent.playthrough == 2 and chapter == 2 and random.randint(0,10) == 0: renpy.show("m_sticker hop")
                        elif t.nPoint > t.yPoint: renpy.show("n_sticker hop")
                        elif persistent.playthrough == 2 and not persistent.seen_sticker and random.randint(0,100) == 0:
                            renpy.show("y_sticker hopg")
                            persistent.seen_sticker = True
                        elif persistent.playthrough == 2 and chapter == 2: renpy.show("y_sticker_cut hop")
                        else: renpy.show("y_sticker hop")
            else:
                r = random.randint(0, 10)
                if r == 0 and not played_baa:
                    renpy.play("gui/sfx/baa.ogg")
                    played_baa = True
                elif r <= 5: renpy.play(gui.activate_sound_glitch)
            sPointTotal += t.sPoint
            nPointTotal += t.nPoint
            yPointTotal += t.yPoint
            progress += 1
            if progress > numWords:
                break

        if persistent.playthrough == 0:
            
            if chapter == 1:
                exec(ch1_choice[0] + "PointTotal += 5")
            
            unsorted_pointlist = {"sayori": sPointTotal, "natsuki": nPointTotal, "yuri": yPointTotal}
            pointlist = sorted(unsorted_pointlist, key=unsorted_pointlist.get)
            
            
            poemwinner[chapter] = pointlist[2]
        else:
            if nPointTotal > yPointTotal: poemwinner[chapter] = "natsuki"
            else: poemwinner[chapter] = "yuri"


        exec(poemwinner[chapter][0] + "_appeal += 1")


        if sPointTotal < POEM_DISLIKE_THRESHOLD: s_poemappeal[chapter] = -1
        elif sPointTotal > POEM_LIKE_THRESHOLD: s_poemappeal[chapter] = 1
        if nPointTotal < POEM_DISLIKE_THRESHOLD: n_poemappeal[chapter] = -1
        elif nPointTotal > POEM_LIKE_THRESHOLD: n_poemappeal[chapter] = 1
        if yPointTotal < POEM_DISLIKE_THRESHOLD: y_poemappeal[chapter] = -1
        elif yPointTotal > POEM_LIKE_THRESHOLD: y_poemappeal[chapter] = 1


        exec(poemwinner[chapter][0] + "_poemappeal[chapter] = 1")

    if persistent.playthrough == 2 and persistent.seen_eyes == None and renpy.random.randint(0,5) == 0:
        $ seen_eyes_this_chapter = True
        $ quick_menu = False
        play sound "sfx/eyes.ogg"
        $ persistent.seen_eyes = True
        stop music
        scene black with None
        show bg eyes_move
        pause 1.2
        hide bg eyes_move
        show bg eyes
        pause 0.5
        hide bg eyes
        show bg eyes_move
        pause 1.25
        hide bg eyes with None
        $ quick_menu = True
    $ config.allow_skipping = True
    $ allow_skipping = True
    stop music fadeout 2.0
    hide screen quick_menu
    show black as fadeout:
        alpha 0
        linear 1.0 alpha 1.0
    pause 1.0
    return

image bg eyes_move:
    "images/bg/eyes.png"
    parallel:
        yoffset 720 ytile 2
        linear 0.5 yoffset 0
        repeat
    parallel:
        0.1
        choice:
            xoffset 20
            0.05
            xoffset 0
        choice:
            xoffset 0
        repeat
image bg eyes:
    "images/bg/eyes.png"

image s_sticker:
    "gui/poemgame/s_sticker_1.png"
    xoffset sayoriOffset xzoom sayoriZoom
    block:
        function randomPauseSayori
        parallel:
            sticker_move_n
        parallel:
            function randomMoveSayori
        repeat

image n_sticker:
    "gui/poemgame/n_sticker_1.png"
    xoffset natsukiOffset xzoom natsukiZoom
    block:
        function randomPauseNatsuki
        parallel:
            sticker_move_n
        parallel:
            function randomMoveNatsuki
        repeat

image y_sticker:
    "gui/poemgame/y_sticker_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image y_sticker_cut:
    "gui/poemgame/y_sticker_cut_1.png"
    xoffset yuriOffset xzoom yuriZoom
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

image m_sticker:
    "gui/poemgame/m_sticker_1.png"
    xoffset monikaOffset xzoom monikaZoom
    block:
        function randomPauseMonika
        parallel:
            sticker_move_n
        parallel:
            function randomMoveMonika
        repeat

image s_sticker hop:
    "gui/poemgame/s_sticker_2.png"
    xoffset sayoriOffset xzoom sayoriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "s_sticker"

image n_sticker hop:
    "gui/poemgame/n_sticker_2.png"
    xoffset natsukiOffset xzoom natsukiZoom
    sticker_hop
    xoffset 0 xzoom 1
    "n_sticker"

image y_sticker hop:
    "gui/poemgame/y_sticker_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image y_sticker_cut hop:
    "gui/poemgame/y_sticker_cut_2.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker_cut"

image y_sticker hopg:
    "gui/poemgame/y_sticker_2g.png"
    xoffset yuriOffset xzoom yuriZoom
    sticker_hop
    xoffset 0 xzoom 1
    "y_sticker"

image m_sticker hop:
    "gui/poemgame/m_sticker_2.png"
    xoffset monikaOffset xzoom monikaZoom
    sticker_hop
    xoffset 0 xzoom 1
    "m_sticker"

image y_sticker glitch:
    "gui/poemgame/y_sticker_1_broken.png"
    xoffset yuriOffset xzoom yuriZoom zoom 3.0
    block:
        function randomPauseYuri
        parallel:
            sticker_move_n
        parallel:
            function randomMoveYuri
        repeat

transform sticker_left:
    xcenter 100 yalign 0.9 subpixel True

transform sticker_mid:
    xcenter 220 yalign 0.9 subpixel True

transform sticker_right:
    xcenter 340 yalign 0.9 subpixel True

transform sticker_glitch:
    xcenter 50 yalign 1.8 subpixel True

transform sticker_m_glitch:
    xcenter 100 yalign 1.35 subpixel True

transform sticker_move_n:
    easein_quad .08 yoffset -15
    easeout_quad .08 yoffset 0

transform sticker_hop:
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
    easein_quad .18 yoffset -80
    easeout_quad .18 yoffset 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
