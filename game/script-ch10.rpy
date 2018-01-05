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
    s "Эээээээээээй!!"
    "Вдалеке я увидел шумную девушку, она бежала по направлению ко мне, размахивая руками в воздухе так, будто ей плевать на то излишнее внимание, которое она к себе привлекает."
    "Эта девушка -- [s_name], моя соседка и хорошая подруга детства."
    "Ну знаете, такие друзья, с которыми вы толком и не видитесь, но они остаются таковыми просто потому, что вы знаете друг друга слишком долго?"
    "В такие дни, как этот, мы раньше ходили в школу вместе, но, начиная со старшей школы, она начала всё чаще и чаще просыпать, в конце концов я просто устал постоянно ждать её."
    "Но если она так и будет бегать за мной, как сейчас, то будет лучше просто убежать подальше."
    "В итоге, я просто вздохнул и встал напротив перехода, дав [s_name] догнать меня."

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
