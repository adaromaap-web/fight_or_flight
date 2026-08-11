# --------------------------------------------------
# ПЕРЕМЕННЫЕ
# --------------------------------------------------

# --------------------------------------------------
# АНИМАЦИЯ ПЕРСОНАЖЕЙ
# --------------------------------------------------

# Персонажи слева, конечная координата -250

transform character_left_250_in:
    xpos -900
    ypos 100
    easein 0.6 xpos -250

transform character_left_250_out:
    xpos -250
    easeout 0.5 xpos -900


# Персонажи слева, конечная координата -300

transform character_left_300_in:
    xpos -900
    ypos 65
    easein 0.6 xpos -300

transform character_left_300_out:
    xpos -300
    easeout 0.5 xpos -900


# Вика

transform vika_left_in:
    xpos -900
    ypos 100
    easein 0.6 xpos -250


# Игорь

transform igor_left_in:
    xpos -900
    ypos 65
    easein 0.6 xpos -300


# Женя

transform zhenya_left_in:
    xpos -900
    ypos 100
    easein 0.6 xpos -250


# Макс

transform max_left_in:
    xpos -900
    ypos 65
    easein 0.6 xpos -300


# Яша

transform yasha_left_in:
    xpos -900
    ypos 65
    easein 0.6 xpos -300


# --------------------------------------------------
# ГЕРОИНЯ СПРАВА
# --------------------------------------------------

transform heroine_right_in:
    xpos 900
    easein 0.6 xpos 0

transform heroine_right_out:
    xpos 0
    easeout 0.5 xpos 900


default player_name = "Героиня"

default heroine = "R1.png"

default heroine_list = [
    "R1.png",
    "B1.png",
    "A1.png",
    "N1.png"
]

default heroine_index = 0

default heroine_jacket = "R2.png"

default heroine_jacket_list = [
    "R2.png",
    "B2.png",
    "A2.png",
    "N2.png"
]

default heroine_police = "R3.png"

default heroine_police_list = [
    "R3.png",
    "B3.png",
    "A3.png",
    "N3.png"
]

default igor_relationship = 0
default zhenya_relationship = 0


# --------------------------------------------------
# ПЕРСОНАЖИ
# --------------------------------------------------

define e = Character("[player_name]", color="#FFF2A6")

define guard = Character("Охранник", color="#FFFFFF")

define stranger1 = Character("Незнакомка", color="#FFFFFF")
define stranger2 = Character("Незнакомец", color="#FFFFFF")
define stranger3 = Character("Незнакомка", color="#FFFFFF")
define stranger4 = Character("Незнакомец", color="#FFFFFF")
define stranger5 = Character("Незнакомец", color="#FFFFFF")

define vika = Character("Вика", color="#FFFFFF")
define igor = Character("Игорь", color="#FFFFFF")
define zhenya = Character("Женя", color="#FFFFFF")
define maks = Character("Макс", color="#FFFFFF")
define yasha = Character("Яша", color="#FFFFFF")


# --------------------------------------------------
# ПЕРВЫЙ ЭКРАН
# --------------------------------------------------

screen intro_screen():

    modal True

    frame:
        xfill True
        yfill True
        background "#000000"

        text "Ты — простая девчонка, живущая в крупном городе.\n\nТы начала увлекаться панк-роком и впервые в жизни решила сходить на концерт, но ты ещё не знала, в какое приключение это выльется…":
            xalign 0.5
            yalign 0.5
            xmaximum 370
            text_align 0.5
            color "#FFFFFF"
            size 20

    textbutton "Продолжить":
        xalign 0.5
        ypos 740
        text_size 25
        action Return()
                
screen home_screen():

    add "images/Home.png"

    text "Музыкальное сопровождение":
        xalign 0.5
        yalign 0.3
        text_align 0.5
        color "#FFFFFF"
        size 22

    hbox:
        xalign 0.5
        yalign 0.45
        spacing 15

        textbutton "Включить":
            action Play("music", "audio/attic13-punk-rock-track-149124.mp3")
            xsize 180
            yminimum 90

            background Frame(
                Solid("#2A2433F5"),
                18, 18, 18, 18
            )

            hover_background Frame(
                Solid("#4A3C58FF"),
                18, 18, 18, 18
            )

            text_color "#FFFFFF"
            text_hover_color "#FFFFFF"
            text_size 20
            text_font "DejaVuSans-Bold.ttf"
            text_xalign 0.5
            text_yalign 0.5
            text_text_align 0.5

        textbutton "Выключить":
            action Stop("music")
            xsize 180
            yminimum 90

            background Frame(
                Solid("#2A2433F5"),
                18, 18, 18, 18
            )

            hover_background Frame(
                Solid("#4A3C58FF"),
                18, 18, 18, 18
            )

            text_color "#FFFFFF"
            text_hover_color "#FFFFFF"
            text_size 20
            text_font "DejaVuSans-Bold.ttf"
            text_xalign 0.5
            text_yalign 0.5
            text_text_align 0.5

    textbutton "Продолжить":
        style "choice_button"
        xalign 0.5
        ypos 650

        background Frame(
            Solid("#2A2433F5"),
            20, 20, 20, 20
        )

        hover_background Frame(
            Solid("#4A3C58FF"),
            20, 20, 20, 20
        )

        text_color "#FFFFFF"
        text_hover_color "#FFFFFF"
        text_size 23
        text_font "DejaVuSans-Bold.ttf"
        text_xalign 0.5
        text_yalign 0.5
        text_text_align 0.5

        action Return()

# --------------------------------------------------
# ВЫБОР ВНЕШНОСТИ
# --------------------------------------------------

screen heroine_choice():

    modal True

    add "images/Home.png"

    text "Выбери себе внешность":
        xalign 0.5
        ypos 80
        size 28
        color "#FFFFFF"
        text_align 0.5
        outlines [(2, "#00000080", 0, 2)]

    add "images/" + heroine_list[heroine_index]:
        xalign 0.5
        yalign 0.5

    textbutton "‹":
        xpos 20
        yalign 0.5
        text_size 64
        text_color "#FFFFFF"
        text_hover_color "#E8DDF2"
        text_outlines [(2, "#00000080", 0, 2)]
        background None
        hover_background None
        insensitive_background None

        action SetVariable(
            "heroine_index",
            (heroine_index - 1) % len(heroine_list)
        )

    textbutton "›":
        xpos 365
        yalign 0.5
        text_size 64
        text_color "#FFFFFF"
        text_hover_color "#E8DDF2"
        text_outlines [(2, "#00000080", 0, 2)]
        background None
        hover_background None
        insensitive_background None

        action SetVariable(
            "heroine_index",
            (heroine_index + 1) % len(heroine_list)
        )

    textbutton "Продолжить":
        style "choice_button"
        xalign 0.5
        ypos 650
        action Return()


# --------------------------------------------------
# СТИЛИ ВЫБОРА
# --------------------------------------------------

style heroine_choice_text:
    color "#FFFFFF"
    size 28
    outlines [(2, "#00000080", 0, 2)]

style heroine_choice_button:
    background None
    hover_background None
    padding (0, 0)

style heroine_choice_button_text:
    color "#FFFFFF"
    hover_color "#E8DDF2"
    size 28
    outlines [(2, "#00000080", 0, 2)]


# --------------------------------------------------
# ВЫБОР ИМЕНИ
# --------------------------------------------------

screen name_choice():

    modal True

    add "images/Home.png"

    add "images/" + heroine:
        xalign 0.5
        yalign 0.5

    text "Выбери себе имя":
        xalign 0.5
        ypos 80
        size 28
        color "#FFFFFF"
        outlines [(2, "#00000080", 0, 2)]

    input:
        id "name_input"
        value VariableInputValue("player_name")
        xalign 0.5
        ypos 120
        pixel_width 300
        length 20
        size 28
        action Return()

    textbutton "Продолжить":
        style "choice_button"
        xalign 0.5
        ypos 650
        action Return()

screen startup_splash(image_name):

    add "images/" + image_name

    timer 2.0 action Return()
# --------------------------------------------------
# НАЧАЛО ИГРЫ
# --------------------------------------------------

screen finish_screen():

    button:
        xfill True
        yfill True
        background "images/Finish1.png"
        action Quit(confirm=False)

label start:

    call screen startup_splash("Start1.png")
    
    call screen startup_splash("Start2.png")

    call screen intro_screen

    call screen home_screen

    call screen heroine_choice

    $ heroine = heroine_list[heroine_index]

    call screen name_choice

    if player_name == "":
        $ player_name = "Героиня"


    # --------------------------------------------------
    # ДОМА
    # --------------------------------------------------

    scene image "images/Home.png"

    show image "images/" + heroine at heroine_right_in

    e "Ура! Я иду на свой первый в жизни панк-рок концерт. Познакомлюсь с другими фанатами, послушаю музыку, а может быть даже и потанцую!"

    "Так как ты недавно начала увлекаться панк-роком, из шмоток у тебя только куртка с шипами с маркетплейса. Ты надела её."


    # --------------------------------------------------
    # ГЕРОИНЯ В КУРТКЕ
    # --------------------------------------------------

    $ heroine_jacket = heroine_jacket_list[heroine_index]

    scene image "images/Home.png"

    show image "images/" + heroine_jacket at heroine_right_in

    e "Теперь я готова!"


    # --------------------------------------------------
    # БАР
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    "Ты подошла к бару."


    # --------------------------------------------------
    # ОХРАННИК
    # --------------------------------------------------

    scene image "images/Security.png"

    guard "Без паспорта не впущу!"


    # --------------------------------------------------
    # ГЕРОИНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket at heroine_right_in

    e "?"


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika2.png" at vika_left_in

    stranger1 "Впустите пожалуйста! Я забыла его, но у меня день рождения."


    # --------------------------------------------------
    # ОХРАННИК СНОВА
    # --------------------------------------------------

    scene image "images/Security.png"

    guard "Нет, я сказал!"


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika2.png" at vika_left_in

    stranger1 "Блин, и что теперь делать?"


    # --------------------------------------------------
    # ИГОРЬ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Igor2.png" at igor_left_in

    stranger2 "Может на такси по-быстрому сгонять?"


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika2.png" at vika_left_in

    stranger1 "Можно было бы, но у меня нет денег. Ребят?"


    # --------------------------------------------------
    # ЖЕНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Zhenya2.png" at zhenya_left_in

    stranger3 "Такси стоит недорого, но у меня тоже нет, последние потратила на этот билет."


    # --------------------------------------------------
    # МАКС
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Max2.png" at max_left_in

    stranger4 "Тоже нет, сорян..."


    # --------------------------------------------------
    # ЯША
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Yasha2.png" at yasha_left_in

    stranger5 "Реально, что делать будем?"


    # --------------------------------------------------
    # ГЕРОИНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket at heroine_right_in

    e "Привет! Я могу помочь тебе. Вызвать такси."


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png" at vika_left_in

    stranger1 "О, привет! Правда? Ты бы нас очень выручила, как тебя зовут?"


    # --------------------------------------------------
    # ГЕРОИНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket at heroine_right_in

    e "[player_name]. А вас как зовут?"


    # --------------------------------------------------
    # ЗНАКОМСТВО
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png" at vika_left_in

    vika "А я Вика, очень приятно!"


    scene image "images/Bar_Street.png"

    show image "images/Igor1.png" at igor_left_in

    igor "Привет! Я Игорь"


    scene image "images/Bar_Street.png"

    show image "images/Zhenya1.png" at zhenya_left_in

    zhenya "Хэй! Я Женя!"


    scene image "images/Bar_Street.png"

    show image "images/Max1.png" at max_left_in

    maks "Привет, я Макс!"


    scene image "images/Bar_Street.png"

    show image "images/Yasha2.png" at yasha_left_in

    yasha "Я Яша, привет, новая подруга!"


    # --------------------------------------------------
    # ВИКА — ПРЕДЛОЖЕНИЕ СИГАРЕТЫ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png" at vika_left_in

    vika "Спасибо большое за такси! Я обязательно верну. Курить будешь?"


    # --------------------------------------------------
    # ВЫБОР
    # --------------------------------------------------

    menu:

        "Да":

            scene image "images/Bar_Street.png"

            show image "images/" + heroine_jacket at heroine_right_in

            e "Да, давай."


        "Спасибо, не курю":

            $ igor_relationship += 1
            $ zhenya_relationship += 1

            scene image "images/Bar_Street.png"

            show image "images/Zhenya1.png" at zhenya_left_in

            zhenya "Ну и правильно!"


            scene image "images/Bar_Street.png"

            show image "images/Igor1.png" at igor_left_in

            igor "Молодец, что не куришь!"


            scene image "images/Bar_Street.png"

            show image "images/" + heroine_jacket at heroine_right_in

            e "«А я думала, в панк-рок тусовке все курят»"


    # --------------------------------------------------
    # БАР
    # --------------------------------------------------

    scene image "images/Bar.png"

    "Вика поехала за паспортом, а вы зашли в заведение. Первые три песни отыграли. Ты в восторге."


    # --------------------------------------------------
    # ГЕРОИНЯ — ХОЧЕТ ПИТЬ
    # --------------------------------------------------

    scene image "images/Bar.png"

    show image "images/" + heroine_jacket at heroine_right_in

    e "Класс! Отличный вечер. Только пить очень хочется"


    # --------------------------------------------------
    # ВЫБОР — ГДЕ ВЗЯТЬ НАПИТОК
    # --------------------------------------------------

    menu:

        "Взять в баре":

            scene image "images/Bar.png"

            "Ты решила поддержать заведение."


            # --------------------------------------------------
            # ПОЛИЦИЯ
            # --------------------------------------------------

            scene image "images/Police.png"

            "Всем оставаться на местах! Приготовить документы!"


            # --------------------------------------------------
            # МАКС
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Max2.png" at max_left_in

            maks "???"


            # --------------------------------------------------
            # ЖЕНЯ
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Zhenya2.png" at zhenya_left_in

            zhenya "..."


            # --------------------------------------------------
            # ИГОРЬ
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Igor2.png" at igor_left_in

            igor "Ну вот..."


            # --------------------------------------------------
            # ЯША
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Yasha2.png" at yasha_left_in

            yasha "Ну и дела..."


            # --------------------------------------------------
            # ГЕРОИНЯ — НОВАЯ ВНЕШНОСТЬ
            # --------------------------------------------------

            $ heroine_police = heroine_police_list[heroine_index]

            scene image "images/Bar_Silence.png"

            show image "images/" + heroine_police at heroine_right_in

            e "Что происходит?"


        "Взять в магазине возле бара":

            scene image "images/Bar.png"

            "Ты решила сэкономить."


            scene image "images/Street.png"

            "Ты взяла то что хотела в магазине и направилась к бару. Кто ж знал, что это будет очень вовремя."


            scene image "images/Street.png"

            "Ты заглянула за угол и увидела, как к дверям подъехала полицейская машина…"


    call screen finish_screen