


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "???"
    $ m_name = "Девушка 3"
    $ n_name = "Девушка 2"
    $ y_name = "Девушка 1"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:

        $ chapter = 0
        call ch0_main from _call_ch0_main


        call poem from _call_poem


        $ chapter = 1
        call ch1_main from _call_ch1_main
        call poemresponse_start from _call_poemresponse_start
        call ch1_end from _call_ch1_end


        call poem from _call_poem_1


        $ chapter = 2
        call ch2_main from _call_ch2_main
        call poemresponse_start from _call_poemresponse_start_1
        call ch2_end from _call_ch2_end


        call poem from _call_poem_2


        $ chapter = 3
        call ch3_main from _call_ch3_main
        call poemresponse_start from _call_poemresponse_start_2
        call ch3_end from _call_ch3_end

        $ chapter = 4
        call ch4_main from _call_ch4_main

        python:
            try: renpy.file(config.basedir + "/счхстливые мхсли.png")
            except: open(config.basedir + "/счхстливые мхсли.png", "wb").write(renpy.file("счхстливые мхсли.png").read())
        $ chapter = 5
        call ch5_main from _call_ch5_main

        call endgame from _call_endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main from _call_ch10_main
        jump playthrough2


    elif persistent.playthrough == 2:

        $ chapter = 0
        call ch20_main from _call_ch20_main

        label playthrough2:


            call poem from _call_poem_3
            python:
                try: renpy.file(config.basedir + "/МЕНЯ СЛЫШНО.txt")
                except: open(config.basedir + "/МЕНЯ СЛЫШНО.txt", "wb").write(renpy.file("МЕНЯ СЛЫШНО.txt").read())


            $ chapter = 1
            call ch21_main from _call_ch21_main
            call poemresponse_start from _call_poemresponse_start_3
            call ch21_end from _call_ch21_end


            call poem (False) from _call_poem_4
            python:
                try: renpy.file(config.basedir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt")
                except: open(config.basedir + "/яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt", "wb").write(renpy.file("яяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяя.txt").read())


            $ chapter = 2
            call ch22_main from _call_ch22_main
            call poemresponse_start from _call_poemresponse_start_4
            call ch22_end from _call_ch22_end


            call poem (False) from _call_poem_5


            $ chapter = 3
            call ch23_main from _call_ch23_main
            if y_appeal >= 3:
                call poemresponse_start2 from _call_poemresponse_start2
            else:
                call poemresponse_start from _call_poemresponse_start_5

            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "Конец демо"
                return

            call ch23_end from _call_ch23_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main from _call_ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
