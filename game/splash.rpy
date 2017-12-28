init python:
    menu_trans_time = 1
    splash_message_default = "Эта игра не рекомендована для детей\nи легко впечатлительных личностей."
    splash_messages = [
    "Ты мой свет,\nмой единственный свет",
    "Я скучала.",
    "Поиграй со мной",
    "Это только игра, в основном.",
    "Эта игра не рекомендована для детей\nи легко впечатлительных личностей?",
    "ывафывлдапывапыпщшткащутдмив",
    "null",
    "Я подарила детей аду",
    "PM умер за это.",
    "Это была лишь частично твоя вина.",
    "Эта игра не рекомендована для детей\nи легко расчленяемых личностей.",
    "Не забудь создать резервную копию файла персонажа Моники."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_logo:
    "gui/logo.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0


image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun")
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                f.write("0JIg0LvRg9GH0YjQuNGFINGC0YDQsNC00LjRhtC40Y/RhSDQtNCw0L3QvdC+0Lkg0LjQs9GA0Ysg0L7QsdGA0LDRidC10L3QuNC1INC+0YIg0LrQvtC80LDQvdC00Ysg0L/QtdGA0LXQstC+0LTRh9C40LrQvtCyLCDQvNGLINGB0L/RgNGP0YLQsNC70Lgg0LfQtNC10YHRjC4uLg0K0J3Rgywg0YDQsNC3INGD0LYg0LLRiyDRjdGC0L4g0YfQuNGC0LDQtdGC0LUsINC00YPQvNCw0Y4sINCy0Ysg0Lgg0YHQsNC80Lgg0Y3RgtC+INC/0L7QvdGP0LvQuC4NCg0K0KfRgtC+INC2LCDQvtCz0YDQvtC80L3QsNGPINCx0LvQsNCz0L7QtNCw0YDQvdC+0YHRgtGMINCy0YHQtdC8LCDRgdC+0LfQtNCw0YLQtdC70Y/QvCDQuNCz0YDRiyDQt9CwINGC0L4sINGH0YLQviDRgdC+0LfQtNCw0LvQuCDQv9C+0LTQvtCx0L3Ri9C5INGI0LXQtNC10LLRgCDQvtGCINCy0YHQtdGFLCDQutGC0L4g0YPRh9Cw0YHRgtCy0L7QstCw0Lsg0LIg0L/QtdGA0LXQstC+0LTQtSwg0LAg0LjQvNC10L3QvdC+Og0KS0JPUFlNDQpMYXp5Rm94DQrQotGD0YMt0KLQuNC60LrQuA0KTWFlbGRvbQ0KWnlhYmxpaw0K0JLQutGD0YHQvdCw0Y8g0YHQsNGA0LTQtdC70YzQutCwDQrQqNGC0L7RgNC60LANCncyYXJ5Z2FwDQpMZSBHb3VjaHF1ZQ0KZGlydHlfdHlhbg0KTWloYV9hbmRfVGVtYQ0KU2F0YW55YQ0KS2lydWtpcnUgQW1vdQ0KUm9tWmVycjANClRhc2NoZV9DaGFuDQpMb25lIEthc2F0aWsNCnRpbmVubWkNClF1YWNraWVEdWNraWUNCg0K0J7RgtC00LXQu9GM0L3QvtC1INGB0L/QsNGB0LjQsdC+IEVsbGlNYXJzaG1hbGxvdyDQuNC3INCz0YDRg9C/0L/RiyB2ay5jb20vb3VybGl0dGxlcGxhbmV0INC30LAg0L/QtdGA0LXQstC+0LQg0L/QtdGB0L3QuCAiWW91ciBSZWFsaXR5IiANCtCa0YHRgtCw0YLQuCwg0LLQvtGCINC10ZEg0L/QvtC70L3Ri9C5INGC0LXQutGB0YI6DQoNCtCa0LDQttC00YvQuSDQtNC10L3RjCwg0YfRgtC+INGBINGC0L7QsdC+0Lkg0LHRg9C00LXQvCDQstC80LXRgdGC0LUg0LzRiywg0LPRgNC10LbRgyDQvdCw0Y/QstGDLg0K0KDRg9GH0LrQvtC5INGPINC90LAg0LHRg9C80LDQs9C1INC+INC90LDRgSDQv9C+0Y3QvNGDINC/0LjRgdCw0YLRjCDQvdCw0YfQvdGDLg0KDQrQp9C10YDQvdC40LvQsCDQvtGB0YLQsNCy0LjQu9C4INC60LvRj9C60YHRi+KApg0K0KHQvNC+0LPRgyDRgtCy0L7RkSDRgdC10YDQtNGG0LUg0YHRgtGA0L7QutCw0LzQuCDQt9Cw0LTQtdGC0YwuDQrQn9C+0LvQvdC+INGDINC90LDRgSDQstC+0LfQvNC+0LbQvdC+0YHRgtC10Lkg0YDQsNC30L3Ri9GFLA0K0JrQsNC6INGA0LDRgdC/0L7Qt9C90LDRgtGMLCDRh9GC0L4g0L3QsNGB0YLQsNC7INGC0L7RgiDRgdCw0LzRi9C5INC00LXQvdGMPw0K0JrQsNC6INGA0LDRgdC/0L7Qt9C90LDRgtGMLCDRh9GC0L4g0L3QsNGB0YLQsNC7INGC0L7RgiDRgdCw0LzRi9C5INC00LXQvdGMPw0KDQrQo9C00LDQu9C+0YHRjCDQu9C4INC00LvRjyDQutCw0LbQtNC+0LPQviDQv9C+INC00YPRiNC1INC00LXQu9C+INC/0L7QtNC+0LHRgNCw0YLRjD8NCtChINC90LDQvNC4INGC0Ysg4oCTINGN0YLQviDQt9C90LDRh9C40YIsINGH0YLQviDQvNGLINGB0LXQudGH0LDRgSDQvdC1INC00L7Qu9C20L3RiyDRgdC60YPRh9Cw0YLRjCENCg0K0KHQstC+0Lgg0YfRg9Cy0YHRgtCy0LAg0L/RgNC+0YfQtdGB0YLRjCDRjyDQvdC1INCyINGB0LjQu9Cw0YUsDQrQndC+INC70YPRh9GI0LUg0YHQu9C+0LIg0LLRgdGRINGD0LvRi9Cx0LrQsCDQvtCx0YrRj9GB0L3QuNGCIQ0K0KDQsNC3INGE0LjQvdCw0Lsg0LzQvtC5LCDRg9Cy0YssINC90LUg0L3QsNC/0LjRgdCw0L0sDQrQp9GC0L4g0YHQtNC10LvQsNGC0Ywg0LzQvdC1LCDRh9GC0L7QsSDQtdCz0L4g0LfQsNC/0L7Qu9GD0YfQuNGC0Yw/DQoNCtCf0L7Rh9C10LzRgyDQsdC70LjQt9C60LjQvCDQu9GO0LTRj9C8INC80L7Qs9GDINGPINC70LjRiNGMINC+INC/0LvQvtGF0L7QvCDQv9C40YHQsNGC0Yw/DQrQkiDRh9GR0Lwg0LvRjtCx0L7QstGMIOKAkyDQvtGC0L/Rg9GB0YLQuNGC0Ywg0LjQu9C4INC20LUg0Log0YHQtdCx0LUg0LrRgNC10L/Rh9C1INC/0YDQuNCy0Y/Qt9Cw0YLRjD8NCg0K0JLQvdC+0LLRjCDRh9C10YDQvdC40LvQsCDQvtGB0YLQsNCy0LjQu9C4INC60LvRj9C60YHRi+KApg0K0JrQsNC6INC/0YDQtdGC0LLQvtGA0LjRgtGMINCyINC20LjQt9C90Ywg0L/QvtGN0LzRgyDQviDQu9GO0LHQstC4Pw0K0KLQstC+0Lkg0YHRgtGD0Log0YHQtdGA0LTRhtCwINC90LUg0YHQu9GL0YjRgyDRjyDRj9GB0L3Qvi4NCtCa0LDQutC+0Lkg0LvRjtCx0L7QstGMINCx0YvRgtGMINC00L7Qu9C20L3QsCDQsiDRgNC10LDQu9GM0L3QvtGB0YLQuD8NCtCg0LDQtyDQsiDRgtCy0L7QtdC5INGA0LXQsNC70YzQvdC+0YHRgtC4INC60LDQuiDQu9GO0LHQuNGC0YwsINGPINC90LUg0YPQt9C90LDRjiwNCtCi0L7Qs9C00LAg0YPQudC00YMu")
                pass
    if not firstrun:
        if persistent.first_run:
            $ quick_menu = False
            scene black
            menu:
                "Был обнаружен прошлый файл сохранений. Вы хотите удалить ваши сохранённые данные и начать с начала?"
                "Да, удалить существующие данные.":
                    "Удаление сохранённых данных...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "Нет, продолжить там, где я остановился.":
                    pass

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("0JIg0LvRg9GH0YjQuNGFINGC0YDQsNC00LjRhtC40Y/RhSDQtNCw0L3QvdC+0Lkg0LjQs9GA0Ysg0L7QsdGA0LDRidC10L3QuNC1INC+0YIg0LrQvtC80LDQvdC00Ysg0L/QtdGA0LXQstC+0LTRh9C40LrQvtCyLCDQvNGLINGB0L/RgNGP0YLQsNC70Lgg0LfQtNC10YHRjC4uLg0K0J3Rgywg0YDQsNC3INGD0LYg0LLRiyDRjdGC0L4g0YfQuNGC0LDQtdGC0LUsINC00YPQvNCw0Y4sINCy0Ysg0Lgg0YHQsNC80Lgg0Y3RgtC+INC/0L7QvdGP0LvQuC4NCg0K0KfRgtC+INC2LCDQvtCz0YDQvtC80L3QsNGPINCx0LvQsNCz0L7QtNCw0YDQvdC+0YHRgtGMINCy0YHQtdC8LCDRgdC+0LfQtNCw0YLQtdC70Y/QvCDQuNCz0YDRiyDQt9CwINGC0L4sINGH0YLQviDRgdC+0LfQtNCw0LvQuCDQv9C+0LTQvtCx0L3Ri9C5INGI0LXQtNC10LLRgCDQvtGCINCy0YHQtdGFLCDQutGC0L4g0YPRh9Cw0YHRgtCy0L7QstCw0Lsg0LIg0L/QtdGA0LXQstC+0LTQtSwg0LAg0LjQvNC10L3QvdC+Og0KS0JPUFlNDQpMYXp5Rm94DQrQotGD0YMt0KLQuNC60LrQuA0KTWFlbGRvbQ0KWnlhYmxpaw0K0JLQutGD0YHQvdCw0Y8g0YHQsNGA0LTQtdC70YzQutCwDQrQqNGC0L7RgNC60LANCncyYXJ5Z2FwDQpMZSBHb3VjaHF1ZQ0KZGlydHlfdHlhbg0KTWloYV9hbmRfVGVtYQ0KU2F0YW55YQ0KS2lydWtpcnUgQW1vdQ0KUm9tWmVycjANClRhc2NoZV9DaGFuDQpMb25lIEthc2F0aWsNCnRpbmVubWkNClF1YWNraWVEdWNraWUNCg0K0J7RgtC00LXQu9GM0L3QvtC1INGB0L/QsNGB0LjQsdC+IEVsbGlNYXJzaG1hbGxvdyDQuNC3INCz0YDRg9C/0L/RiyB2ay5jb20vb3VybGl0dGxlcGxhbmV0INC30LAg0L/QtdGA0LXQstC+0LQg0L/QtdGB0L3QuCAiWW91ciBSZWFsaXR5IiANCtCa0YHRgtCw0YLQuCwg0LLQvtGCINC10ZEg0L/QvtC70L3Ri9C5INGC0LXQutGB0YI6DQoNCtCa0LDQttC00YvQuSDQtNC10L3RjCwg0YfRgtC+INGBINGC0L7QsdC+0Lkg0LHRg9C00LXQvCDQstC80LXRgdGC0LUg0LzRiywg0LPRgNC10LbRgyDQvdCw0Y/QstGDLg0K0KDRg9GH0LrQvtC5INGPINC90LAg0LHRg9C80LDQs9C1INC+INC90LDRgSDQv9C+0Y3QvNGDINC/0LjRgdCw0YLRjCDQvdCw0YfQvdGDLg0KDQrQp9C10YDQvdC40LvQsCDQvtGB0YLQsNCy0LjQu9C4INC60LvRj9C60YHRi+KApg0K0KHQvNC+0LPRgyDRgtCy0L7RkSDRgdC10YDQtNGG0LUg0YHRgtGA0L7QutCw0LzQuCDQt9Cw0LTQtdGC0YwuDQrQn9C+0LvQvdC+INGDINC90LDRgSDQstC+0LfQvNC+0LbQvdC+0YHRgtC10Lkg0YDQsNC30L3Ri9GFLA0K0JrQsNC6INGA0LDRgdC/0L7Qt9C90LDRgtGMLCDRh9GC0L4g0L3QsNGB0YLQsNC7INGC0L7RgiDRgdCw0LzRi9C5INC00LXQvdGMPw0K0JrQsNC6INGA0LDRgdC/0L7Qt9C90LDRgtGMLCDRh9GC0L4g0L3QsNGB0YLQsNC7INGC0L7RgiDRgdCw0LzRi9C5INC00LXQvdGMPw0KDQrQo9C00LDQu9C+0YHRjCDQu9C4INC00LvRjyDQutCw0LbQtNC+0LPQviDQv9C+INC00YPRiNC1INC00LXQu9C+INC/0L7QtNC+0LHRgNCw0YLRjD8NCtChINC90LDQvNC4INGC0Ysg4oCTINGN0YLQviDQt9C90LDRh9C40YIsINGH0YLQviDQvNGLINGB0LXQudGH0LDRgSDQvdC1INC00L7Qu9C20L3RiyDRgdC60YPRh9Cw0YLRjCENCg0K0KHQstC+0Lgg0YfRg9Cy0YHRgtCy0LAg0L/RgNC+0YfQtdGB0YLRjCDRjyDQvdC1INCyINGB0LjQu9Cw0YUsDQrQndC+INC70YPRh9GI0LUg0YHQu9C+0LIg0LLRgdGRINGD0LvRi9Cx0LrQsCDQvtCx0YrRj9GB0L3QuNGCIQ0K0KDQsNC3INGE0LjQvdCw0Lsg0LzQvtC5LCDRg9Cy0YssINC90LUg0L3QsNC/0LjRgdCw0L0sDQrQp9GC0L4g0YHQtNC10LvQsNGC0Ywg0LzQvdC1LCDRh9GC0L7QsSDQtdCz0L4g0LfQsNC/0L7Qu9GD0YfQuNGC0Yw/DQoNCtCf0L7Rh9C10LzRgyDQsdC70LjQt9C60LjQvCDQu9GO0LTRj9C8INC80L7Qs9GDINGPINC70LjRiNGMINC+INC/0LvQvtGF0L7QvCDQv9C40YHQsNGC0Yw/DQrQkiDRh9GR0Lwg0LvRjtCx0L7QstGMIOKAkyDQvtGC0L/Rg9GB0YLQuNGC0Ywg0LjQu9C4INC20LUg0Log0YHQtdCx0LUg0LrRgNC10L/Rh9C1INC/0YDQuNCy0Y/Qt9Cw0YLRjD8NCg0K0JLQvdC+0LLRjCDRh9C10YDQvdC40LvQsCDQvtGB0YLQsNCy0LjQu9C4INC60LvRj9C60YHRi+KApg0K0JrQsNC6INC/0YDQtdGC0LLQvtGA0LjRgtGMINCyINC20LjQt9C90Ywg0L/QvtGN0LzRgyDQviDQu9GO0LHQstC4Pw0K0KLQstC+0Lkg0YHRgtGD0Log0YHQtdGA0LTRhtCwINC90LUg0YHQu9GL0YjRgyDRjyDRj9GB0L3Qvi4NCtCa0LDQutC+0Lkg0LvRjtCx0L7QstGMINCx0YvRgtGMINC00L7Qu9C20L3QsCDQsiDRgNC10LDQu9GM0L3QvtGB0YLQuD8NCtCg0LDQtyDQsiDRgtCy0L7QtdC5INGA0LXQsNC70YzQvdC+0YHRgtC4INC60LDQuiDQu9GO0LHQuNGC0YwsINGPINC90LUg0YPQt9C90LDRjiwNCtCi0L7Qs9C00LAg0YPQudC00YMu")
                except:
                    renpy.jump("readonly")

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene white
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Эта игра не рекомендована для детей и легко впечатлительных личностей."
        "Личности, страдающие от беспокойства или депрессии, могут пострадать при прохождении данной игры. Для предупреждений о содержании, пожалуйста, посетите: http://ddlc.moe/warning.html или прочтите WARNING.html в папке с игрой"
        menu:
            "Играя в Doki Doki Literature Club, вы подтверждаете, что вам как минимум 16 лет и вы согласны увидеть очень тревожащее содержимое."
            "Я подтверждаю.":
                pass
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        pause 1.0
        scene white


    python:
        s_kill_early = None
        if persistent.playthrough == 0:
            try: renpy.file("../characters/sayori.chr")
            except: s_kill_early = True
        if not s_kill_early:
            if persistent.playthrough <= 2 and persistent.playthrough != 0:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

    if not persistent.special_poems:
        python hide:
            persistent.special_poems = [0,0,0]
            a = range(1,12)
            for i in range(3):
                b = renpy.random.choice(a)
                persistent.special_poems[i] = b
                a.remove(b)

    $ basedir = config.basedir.replace('\\', '/')



    if persistent.autoload:
        jump autoload



    $ config.allow_skipping = False

    if persistent.playthrough == 2 and not persistent.seen_ghost_menu and renpy.random.randint(0, 63) == 0:
        show black
        $ config.main_menu_music = audio.ghostmenu
        $ persistent.seen_ghost_menu = True
        $ persistent.ghost_menu = True
        $ renpy.music.play(config.main_menu_music)
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        $ config.allow_skipping = True
        return


    if s_kill_early:
        show black
        play music "bgm/s_kill_early.ogg"
        pause 1.0
        show end with dissolve_cg
        pause 3.0
        scene white
        show expression "images/cg/s_kill_early.png":
            yalign -0.05
            xalign 0.25
            dizzy(1.0, 4.0, subpixel=False)
        show white as w2:
            choice:
                ease 0.25 alpha 0.1
            choice:
                ease 0.25 alpha 0.125
            choice:
                ease 0.25 alpha 0.15
            choice:
                ease 0.25 alpha 0.175
            choice:
                ease 0.25 alpha 0.2
            choice:
                ease 0.25 alpha 0.225
            choice:
                ease 0.25 alpha 0.25
            choice:
                ease 0.25 alpha 0.275
            choice:
                ease 0.25 alpha 0.3
            pass
            choice:
                pass
            choice:
                0.25
            choice:
                0.5
            choice:
                0.75
            repeat
        show noise:
            alpha 0.1
        with Dissolve(1.0)
        show expression Text("Теперь все могут быть счастливы.", style="sayori_text"):
            xalign 0.8
            yalign 0.5
            alpha 0.0
            600
            linear 60 alpha 0.5
        pause
        $ renpy.quit()


    show white
    $ persistent.ghost_menu = False
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.t1
    $ renpy.music.play(config.main_menu_music)
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200
        jump expression persistent.autoload

    elif anticheat != persistent.anticheat:
        stop music
        scene black
        "Файл сохранения нельзя загрузить."
        "Ты пытаешься читерить?"
        $ m_name = "Моника"
        show monika 1 at t11
        if persistent.playername == "":
            m "Ты такой смешной."
        else:
            m "Ты такой смешной, [persistent.playername]."
        $ renpy.utter_restart()
    else:
        if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
            $ persistent.first_load = True
            call screen dialog("Подсказка: Можно использовать кнопку \"Пропуск\", чтобы пропускать виденный ранее текст.", ok_action=Return())
    return



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yuri_kill_2":
        $ persistent.yuri_kill += 200


    if renpy.get_return_stack():
        $ renpy.pop_call()
    jump expression persistent.autoload

label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label quit:
    if persistent.ghost_menu:
        hide screen main_menu
        scene white
        show expression "gui/menu_art_m_ghost.png":
            xpos -100 ypos -100 zoom 3.5
        pause 0.01
    return

label readonly:
    scene black
    "Игру нельзя запустить, поскольку вы пытаетесь запустить её из места, в котором разрешено лишь чтение."
    "Пожалуйста, скопируйте приложение DDLC на рабочий стол или любое другое доступное место и попробуйте снова."
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
