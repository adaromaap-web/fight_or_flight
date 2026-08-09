
# --------------------------------------------------
# ПЕРЕМЕННЫЕ
# --------------------------------------------------

default player_name = "Героиня"

default heroine = "R1.png"

default heroine_list = [
    "R1.png",
    "B1.png",
    "A1.png",
    "N1.png"
]

default heroine_index = 0


# Внешности в куртке.

default heroine_jacket = "R2.png"

default heroine_jacket_list = [
    "R2.png",
    "B2.png",
    "A2.png",
    "N2.png"
]


# --------------------------------------------------
# ПЕРСОНАЖИ
# --------------------------------------------------

define e = Character('[player_name]', color="#c8ffc8")

define guard = Character('Охранник', color="#ffffff")

define stranger1 = Character('Незнакомка', color="#ffffff")


# --------------------------------------------------
# ПЕРВЫЙ ЭКРАН
# --------------------------------------------------

screen intro_screen():

    modal True

    frame:
        xfill True
        yfill True
        background "#6b1f2b"

        text "Ты — простая девчонка, живущая в крупном городе.\n\nТы начала увлекаться панк-роком и впервые в жизни решила сходить на концерт, но ты ещё не знала, в какое приключение это выльется…":
            xalign 0.5
            yalign 0.5
            xmaximum 370
            text_align 0.5
            color "#ffffff"
            size 20

    textbutton "Продолжить":
        xalign 0.5
        ypos 740
        text_size 25
        action Return()


# --------------------------------------------------
# ВЫБОР ВНЕШНОСТИ
# --------------------------------------------------

screen heroine_choice():

    modal True

    add "images/Home.png"

    text "Выбери себе внешность":
        xalign 0.5
        ypos 30
        size 28

    add "images/" + heroine_list[heroine_index]:
        xalign 0.5
        yalign 0.5

    textbutton "←":
        xpos 20
        yalign 0.5
        text_size 50
        action SetVariable(
            "heroine_index",
            (heroine_index - 1) % len(heroine_list)
        )

    textbutton "→":
        xpos 365
        yalign 0.5
        text_size 50
        action SetVariable(
            "heroine_index",
            (heroine_index + 1) % len(heroine_list)
        )

    textbutton "Выбрать":
        xalign 0.5
        ypos 740
        text_size 28
        action [
            SetVariable("heroine", heroine_list[heroine_index]),
            Return()
        ]


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
        ypos 250
        size 28

    input:
        value VariableInputValue("player_name")
        xalign 0.5
        ypos 330
        pixel_width 300
        length 20
        size 28

    textbutton "Продолжить":
        xalign 0.5
        ypos 420
        text_size 28
        action Return()


# --------------------------------------------------
# НАЧАЛО ИГРЫ
# --------------------------------------------------

label start:

    call screen intro_screen

    call screen heroine_choice

    call screen name_choice


    if player_name == "":
        $ player_name = "Героиня"


    # --------------------------------------------------
    # ДОМА
    # --------------------------------------------------

    scene image "images/Home.png"

    show image "images/" + heroine

    e "Ура! Я иду на свой первый в жизни панк-рок концерт. Познакомлюсь с другими фанатами, послушаю музыку, а может быть даже и потанцую!"


    "Так как ты недавно начала увлекаться панк-роком, из шмоток у тебя только куртка с шипами с маркетплейса. Ты надела её."


    # --------------------------------------------------
    # ГЕРОИНЯ В КУРТКЕ
    # --------------------------------------------------

    $ heroine_jacket = heroine_jacket_list[heroine_index]

    scene image "images/Home.png"

    show image "images/" + heroine_jacket

    e "Теперь я готова идти на концерт!"


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


    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket

    e "?"


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"


    show image "images/Vika2.png":
        xpos -250
        ypos 100

    stranger1 "Впустите пожалуйста! Я забыла его, но у меня день рождения."


    # --------------------------------------------------
    # ОХРАННИК СНОВА
    # --------------------------------------------------

    scene image "images/Security.png"

    guard "Нет, я сказал!"


    return
