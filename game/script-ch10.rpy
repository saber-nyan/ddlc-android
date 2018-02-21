label ch10_main:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ gtext = glitchtext(48)
    stop music
    $ config.window_hide_transition = None
    scene bg residential_day
    with dissolve_scene_half
    $ config.window_hide_transition = Dissolve(.2)
    play music t2g
    queue music t2g2

    s "[gtext]"
    $ s_name = glitchtext(12)
    "Я увидел надоедливую девчонку, которая бежала ко мне, размахивая руками и совершенно не замечая, что привлекает к себе внимание окружающих.."
    "Это [s_name], моя соседка и близкая подруга детства."
    "Ну, знаете, такой человек, с которым сейчас вы бы уже не стали дружить, но ваши отношения сохраняются за счёт того, что вы знакомы целую вечность."
    "Мы всегда ходили в школу вместе, но, когда перешли в старшую, Саёри стала всё реже просыпаться вовремя, и мне надоело каждый раз дожидаться её."
    "Однако, если она собралась таскаться за мной подобным образом, то, по-моему, лучше сразу бежать."
    "Тем не менее я лишь вздохнул и притормозил перед пешеходным переходом, позволяя [s_name] меня догнать."

    show sayori glitch zorder 2 at t11
    python:
        currentpos = get_pos()
        startpos = currentpos - 0.3
        if startpos < 0: startpos = 0
        track = "<from " + str(startpos) + " to " + str(currentpos) + ">bgm/2.ogg"
        renpy.music.play(track, loop=True)
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    pause 1.0
    $ gtext = glitchtext(48)
    s "{cps=60}[gtext]{/cps}{nw}"
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5
    hide screen tear
    window hide(None)
    window auto
    scene black with trueblack
    $ delete_all_saves()
    $ persistent.playthrough = 2
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ anticheat = persistent.anticheat

    jump ch20_from_ch10
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
