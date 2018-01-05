init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "Уф...!"
    "Я слышу, как Нацуки издаёт раздражённый вздох изнутри шкафа."
    "Похоже, что она чем-то недовольна."
    "Я иду к ней, на случай, если ей нужна помощь."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "Ты что-то ищешь?"
    $ style.say_dialogue = style.edited
    n 4x "Ебаная Моникамммммммммммммммммммммммммммммммммммммммммммммм"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Чёртова Моника..."
    n "Она никогда не кладёт мои вещи обратно на место!"
    n "Что толку раскладывать всю коллекцию по порядку, если кто-то может прийти и всё испортить?"
    "Нацуки сдвигает кучу сложенных книг и коробок на полке."
    mc "Манга..."
    n 2c "Ты же читаешь мангу, да?"
    mc "Ах--"
    mc "...Иногда..."
    "Манга -- это одна из тех вещей, признаться в любви к которой ты не можешь, пока не узнаешь, как другой человек к этому относится."
    mc "...Как ты догадалась?"
    n 2k "Я слышала, что ты как-то упоминал об этом."
    n "Кроме того, у тебя это на лице написано."
    "О чем это она...?"
    mc "Я-ясно..."
    "Одинокий том манги стоит посреди разнообразных книг, на краю одной из полок."
    "Заинтересованный, я вытаскиваю его."
    n 1b "{i}Вот{/i} он где!"
    "Нацуки выхватывает его из моих рук."
    "Потом поворачивается к коробке с мангой и вставляет том ровно в середину между остальными."
    n 4d "Ахх, так гораздо лучше!"
    n "Видеть полный сборник без одной книги -- так режет глаз."
    mc "Мне знакомо это чувство..."
    "Я присматриваюсь к сборнику, которым она восхищена."
    mc "Девочки Парфе...?"
    "Это серия, о которой я никогда не слышал."
    "Скорее всего, это потому, что она не для моего возраста, или, может, потому, что просто отвратительна."
    n 5g "Если собираешься осуждать, можешь делать это через стекло вот этой двери."
    "Она указывает на дверь класса."
    mc "Э-эй, я никого не осуждаю...!"
    mc "Я даже ничего не сказал."
    n 5c "Тон твоего голоса."
    $ style.say_dialogue = style.normal
    n "Но я скажу тебе одну вещь, [player]."
    n 4l "Считай это уроком прямиком от Литературного Клуба:{nw}"
    $ _history_list[-1].what = "Считай это уроком прямиком от Литературного Клуба: нельзя судить книгу по её обложке!"
    $ style.say_dialogue = style.edited
    n "Нельза судить книгуууууууууууу ууууу уу{space=20}у{space=40}у{space=120}у{space=160}у{space=200}у"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "А вообще--"
    "Нацуки достаёт первый том Девочек Парфе из коробки."
    n "Я покажу тебе, почему!"
    "Она впихивает книгу мне в руки."
    mc "Ах..."
    "Я рассматриваю обложку."
    "На ней четыре девочки в разноцветных нарядах стоят в женственных позах."
    "Это такое 'моэ'."
    n 4b "Не стой столбом!"
    mc "Воу--"
    show natsuki zorder 1 at thide
    hide natsuki
    "Нацуки хватает меня за руку и вытягивает из шкафа."
    "Затем она садится к стенке, под окном."
    "Она хлопает по полу рядом с собой, указывая мне, где сесть."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "Разве на стульях не удобнее...?"
    "Я сажусь."
    n 2k "На стульях не выйдет."
    n "Так мы не сможем читать одновременно."
    mc "Э? Почему?"
    mc "А... так проще сесть ближе друг к другу..."
    n 2o "--!"
    n 5r "Н-не говори так!"
    n "Ты заставляешь меня чувствовать себя странно!"
    "Нацуки скрещивает руки и отползает от меня на пару сантиметров."
    mc "Извини..."
    show natsuki 5g
    "Я тоже не ожидал, что буду сидеть так близко к ней..."
    "Не могу сказать, что это что-то плохое."
    "Я открываю книгу."
    "Всего через пару секунд Нацуки снова приближается, занимая оставшееся место, надеясь, что я не замечу."
    "Более устремлённая начать читать, чем я, она пристально смотрит через моё плечо."
    n 1k "Ого, как же много времени прошло с тех пор, как я читала начало...?"
    mc "Мм?"
    mc "Разве ты не перечитываешь старые тома время от времени?"
    n 2k "Если честно, нет."
    n "Может, как-нибудь позже, после того, как я закончу серию."
    n 2c "Эй, ты внимательно читаешь?"
    mc "Ух..."
    "Я внимателен, но ничего особенного не происходит, поэтому я могу говорить и читать одновременно."
    "Похоже, это про группу подруг в старшей школе."
    "Типичная 'повседневка'."
    "Я их уже перерос, поскольку редко какое произведение достаточно развлекает, чтобы был незаметен недостаток сюжета."
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "...Ты уверена, что тебе не скучно?"
    n "Не скучно!"
    mc "Несмотря на то, что ты просто смотришь, как я читаю?"
    n "Ну...!"
    n "Мне... и так нормально."
    mc "Ну, как скажешь..."
    mc "...Я думаю, что должно быть весело делиться с другими тем, что ты любишь."
    mc "Мне очень нравится, когда получается уговорить кого-то попробовать мангу, которая мне по душе."
    mc "Ты ведь понимаешь, о чём я?"
    n "...?"
    mc "Хм?"
    mc "Не понимаешь?"
    show n_cg1_exp2 at cgfade
    n "Умм..."
    n "Это не..."
    n "Ну, откуда мне знать."
    mc "...О чём ты?"
    mc "Разве ты не делилась мангой со своими друзьями?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Ты не мог бы не давить на больное?"
    n "Блин..."
    mc "Ах... извини..."
    n "Пфф."
    n "Как будто я могу заставить своих друзей это читать..."
    n "Они думают, что манга -- это для детей."
    n "Я не могу даже упомянуть о ней, как они начинают, типа..."
    n "'Э? Ты ещё не выросла из этого?'"
    n "Как врезала бы..."
    mc "Эх, я знаю таких людей..."
    mc "Если честно, сложно найти друзей, которые не станут это осуждать, легче найти тех, кто так же это любит..."
    mc "Я уже, вроде как, неудачник, видимо меня притягивает к другим неудачникам."
    mc "Должно быть, это ещё сложнее для кого-то вроде тебя..."
    hide n_cg1_exp3
    n "Хм."
    n "Да, пожалуй."
    "{i}...Погодите, что 'да'??{/i}"
    $ style.say_dialogue = style.normal
    n "Мне кажется, я даже не могу держать мангу в своей комнате..."
    $ style.say_dialogue = style.edited
    n "Мой отец отпиздил бы меня, если бы нашёл это."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "Даже не знаю, что сделал бы отец, если бы нашёл это."
    n "По крайней мере, в клубной комнате она в безопасности."
    show n_cg1_exp3 at cgfade
    n "Разве что Моника ведёт себя как дура из-за этого..."
    n "Ух! Весь мир против меня, да?"
    mc "Ну, это же стоило того, да?"
    mc "В смысле, вот я, сижу, читаю."
    n "А толку-то?"
    mc "Ну..."
    mc "По крайней мере, тебе нравится, да?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...И?"
    mc "Ахаха."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Блин, задолбал!"
    n "Ты читать будешь, или как?"
    mc "Да, да..."
    "Я переворачиваю страницу."
    show black with dissolve_cg
    "..."
    "..."
    "....."
    "......."
    "........."
    "Проходит время."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "Нацуки какая-то тихая сегодня."
    "Я мельком взглянул на неё."
    hide black with dissolve_cg
    "Кажется, она засыпает."
    mc "Эй, Нацуки..."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "Д-да...?"
    "Внезапно, Нацуки рухнула прямиком на меня."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "Х-хей--"
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "Вот блин..."
    m 1d "Нацуки, ты в п-порядке?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "..."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Вот..."
    show monika zorder 2 at t21
    "Моника достаёт из своей сумочки что-то вроде протеинового батончика."
    "Она кидает его в сторону Нацуки."
    "Глаза Нацуки неожиданно вновь загорелись."
    "Она подхватывает батончик с пола и разрывает обёртку."
    show natsuki zorder 3 at f22
    n 1s "Я говорила тебе не давать ммф..."
    show natsuki zorder 2 at t22
    "Она даже не закончила предложение перед тем, как запихнуть его в рот."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "Не беспокойся, [player]."
    m "Она в порядке."
    m "Такое иногда бывает."
    m 1a "Поэтому у меня в сумке всегда есть вкусняшка для неё."
    m 5a "Как бы то ни было...!"
    m "Почему бы нам не поделиться поэмами?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
