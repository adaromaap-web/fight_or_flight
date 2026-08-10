
# --------------------------------------------------
# ПЕРЕМЕННЫЕ
# --------------------------------------------------

default player_name = "Героиня"

# Обычная внешность
default heroine = "R1.png"

default heroine_list = [
    "R1.png",
    "B1.png",
    "A1.png",
    "N1.png"
]

default heroine_index = 0

# Внешность в куртке
default heroine_jacket = "R2.png"

default heroine_jacket_list = [
    "R2.png",
    "B2.png",
    "A2.png",
    "N2.png"
]

# Внешность для сцены с полицией
default heroine_police = "R3.png"

default heroine_police_list = [
    "R3.png",
    "B3.png",
    "A3.png",
    "N3.png"
]

# Отношения
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

    add "images/" + heroine_list[heroine_index]:
        xalign 0.5
        yalign 0.5

    # Левая стрелка
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

    # Правая стрелка
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

    # Продолжить
    textbutton "Продолжить":
        xalign 0.5
        yalign 0.9

        text_size 28
        text_color "#FFFFFF"
        text_hover_color "#E8DDF2"
        text_outlines [(2, "#00000080", 0, 2)]

        background None
        hover_background None
        insensitive_background None

        action Return()

# --------------------------------------------------
# ВЫБОР ИМЕНИ
# --------------------------------------------------



style heroine_choice_text:
    color "#FFFFFF"
    size 28
    outlines [(2, "#00000080", 0, 2)]


style heroine_choice_button_text:
    color "#FFFFFF"
    hover_color "#E8DDF2"
    size 28
    outlines [(2, "#00000080", 0, 2)]


screen name_choice():

    modal True

    add "images/Home.png"

    add "images/" + heroine:
        xalign 0.5
        yalign 0.5

    text "Выбери себе имя":
        xalign 0.5
        ypos 250
        style "heroine_choice_text"

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

        style "heroine_choice_button"

        action Return()


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


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika2.png":
        xpos -250
        ypos 100

    stranger1 "Блин, и что теперь делать?"


    # --------------------------------------------------
    # ИГОРЬ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Igor2.png":
        xpos -300
        ypos 65

    stranger2 "Может на такси по-быстрому сгонять?"


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika2.png":
        xpos -250
        ypos 100

    stranger1 "Можно было бы, но у меня нет денег. Ребят?"


    # --------------------------------------------------
    # ЖЕНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Zhenya2.png":
        xpos -250
        ypos 100

    stranger3 "Такси стоит недорого, но у меня тоже нет, последние потратила на этот билет."


    # --------------------------------------------------
    # МАКС
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Max2.png":
        xpos -300
        ypos 65

    stranger4 "Тоже нет, сорян..."


    # --------------------------------------------------
    # ЯША
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Yasha2.png":
        xpos -300
        ypos 65

    stranger5 "Реально, что делать будем?"


    # --------------------------------------------------
    # ГЕРОИНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket

    e "Привет! Я могу помочь тебе. Вызвать такси."


    # --------------------------------------------------
    # ВИКА
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png":
        xpos -250
        ypos 100

    stranger1 "О, привет! Правда? Ты бы нас очень выручила, как тебя зовут?"


    # --------------------------------------------------
    # ГЕРОИНЯ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/" + heroine_jacket

    e "[player_name]. А вас как зовут?"


    # --------------------------------------------------
    # ЗНАКОМСТВО
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png":
        xpos -250
        ypos 100

    vika "А я Вика, очень приятно!"


    scene image "images/Bar_Street.png"

    show image "images/Igor1.png":
        xpos -300
        ypos 65

    igor "Привет! Я Игорь"


    scene image "images/Bar_Street.png"

    show image "images/Zhenya1.png":
        xpos -250
        ypos 100

    zhenya "Хэй! Я Женя!"


    scene image "images/Bar_Street.png"

    show image "images/Max1.png":
        xpos -300
        ypos 65

    maks "Привет, я Макс!"


    scene image "images/Bar_Street.png"

    show image "images/Yasha1.png":
        xpos -300
        ypos 65

    yasha "Я Яша, привет, новая подруга!"


    # --------------------------------------------------
    # ВИКА — ПРЕДЛОЖЕНИЕ СИГАРЕТЫ
    # --------------------------------------------------

    scene image "images/Bar_Street.png"

    show image "images/Vika1.png":
        xpos -250
        ypos 100

    vika "Спасибо большое за такси! Я обязательно верну. Курить будешь?"


    # --------------------------------------------------
    # ВЫБОР
    # --------------------------------------------------

    menu:

        "Да":

            scene image "images/Bar_Street.png"

            show image "images/" + heroine_jacket

            e "Да, давай."


        "Спасибо, не курю":

            $ igor_relationship += 1
            $ zhenya_relationship += 1

            scene image "images/Bar_Street.png"

            show image "images/Zhenya1.png":
                xpos -250
                ypos 100

            zhenya "Ну и правильно!"


            scene image "images/Bar_Street.png"

            show image "images/Igor1.png":
                xpos -300
                ypos 65

            igor "Молодец, что не куришь!"


            scene image "images/Bar_Street.png"

            show image "images/" + heroine_jacket

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

    show image "images/" + heroine_jacket

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

            show image "images/Max2.png":
                xpos -300
                ypos 65

            maks "???"


            # --------------------------------------------------
            # ЖЕНЯ
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Zhenya2.png":
                xpos -250
                ypos 100

            zhenya "..."


            # --------------------------------------------------
            # ИГОРЬ
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Igor2.png":
                xpos -300
                ypos 65

            igor "Ну вот..."


            # --------------------------------------------------
            # ЯША
            # --------------------------------------------------

            scene image "images/Bar_Silence.png"

            show image "images/Yasha2.png":
                xpos -300
                ypos 65

            yasha "Ну и дела..."


            # --------------------------------------------------
            # ГЕРОИНЯ — НОВАЯ ВНЕШНОСТЬ
            # --------------------------------------------------

            $ heroine_police = heroine_police_list[heroine_index]

            scene image "images/Bar_Silence.png"

            show image "images/" + heroine_police

            e "Что происходит?"


        "Взять в магазине возле бара":

            scene image "images/Bar.png"

            "Ты решила сэкономить."


            scene image "images/Street.png"

            "Ты взяла то что хотела в магазине и направилась к бару. Кто ж знал, что это будет очень вовремя."


            scene image "images/Street.png"

            "Ты заглянула за угол и увидела, как к дверям подъехала полицейская машина…"


    return

