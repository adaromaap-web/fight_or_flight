################################################################################
## Инициализация
################################################################################

init offset = -2

init python:
    gui.init(424, 800)

define config.check_conflicting_properties = True


################################################################################
## Конфигурируемые Переменные GUI
################################################################################


## Цвета #######################################################################

define gui.accent_color = '#000066'

define gui.idle_color = '#707070'

define gui.idle_small_color = '#606060'

define gui.hover_color = '#000066'

define gui.selected_color = '#555555'

define gui.insensitive_color = '#7070707f'

define gui.muted_color = '#6666a3'
define gui.hover_muted_color = '#9999c1'


## ТЕКСТ ДИАЛОГОВ ##############################################################

# Обычный текст диалога — белый.
define gui.text_color = '#FFFFFF'

# Текст интерфейса — белый.
define gui.interface_text_color = '#FFFFFF'


## Шрифты ######################################################################

# Более тяжёлый шрифт для игры.
define gui.text_font = "DejaVuSans-Bold.ttf"

# Шрифт имени персонажа.
define gui.name_text_font = "DejaVuSans-Bold.ttf"

# Шрифт интерфейса.
define gui.interface_text_font = "DejaVuSans-Bold.ttf"


## Размеры текста ##############################################################

define gui.text_size = 20

define gui.name_text_size = 38

define gui.interface_text_size = 33

define gui.label_text_size = 36

define gui.notify_text_size = 24

define gui.title_text_size = 75


################################################################################
## Главное и игровое меню
################################################################################

define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


################################################################################
## Диалог
################################################################################

# Высота текстового окна.
define gui.textbox_height = 230

# Окно находится внизу экрана.
define gui.textbox_yalign = 1.0


## ЧЁРНОЕ ПОЛУПРОЗРАЧНОЕ ОКНО ###############################################

# AA = примерно 67% непрозрачности.
# 00 = полностью прозрачный.
# FF = полностью непрозрачный.
#
# Поэтому #000000AA — чёрный полупрозрачный фон.

define gui.textbox_background = Solid("#000000AA")


## Имя персонажа ###############################################################

# Позиция имени.
define gui.name_xpos = 30
define gui.name_ypos = 0

# Выравнивание имени.
define gui.name_xalign = 0.0

# Размер окна имени.
define gui.namebox_width = None
define gui.namebox_height = None

define gui.namebox_borders = Borders(5, 5, 5, 5)

define gui.namebox_tile = False


## Диалоговый текст ############################################################

define gui.dialogue_xpos = 30
define gui.dialogue_ypos = 65

define gui.dialogue_width = 364

define gui.dialogue_text_xalign = 0.0


################################################################################
## Стили окна диалога
################################################################################

init python:

    # Главное окно диалога.
    style.say_window.background = Solid("#000000AA")

    # Имя говорящего.
    style.say_label.color = "#FFF2A6"

    # Текст диалога.
    style.say_dialogue.color = "#FFFFFF"

    # Жирный художественный шрифт.
    style.say_label.font = "DejaVuSans-Bold.ttf"
    style.say_dialogue.font = "DejaVuSans-Bold.ttf"

    # Размер имени.
    style.say_label.size = 45

    # Размер текста.
    style.say_dialogue.size = 22


################################################################################
## Кнопки
################################################################################

define gui.button_width = None
define gui.button_height = None

define gui.button_borders = Borders(6, 6, 6, 6)

define gui.button_tile = False

define gui.button_text_font = gui.interface_text_font

define gui.button_text_size = gui.interface_text_size

define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

define gui.button_text_xalign = 0.0


################################################################################
## Стандартные кнопки
################################################################################

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)

define gui.quick_button_text_size = 21

define gui.quick_button_text_idle_color = gui.idle_small_color

define gui.quick_button_text_selected_color = gui.accent_color


################################################################################
## Кнопки выбора
################################################################################

define gui.choice_button_width = 1185

define gui.choice_button_height = None

define gui.choice_button_tile = False

define gui.choice_button_borders = Borders(150, 8, 150, 8)

define gui.choice_button_text_font = gui.text_font

define gui.choice_button_text_size = gui.text_size

define gui.choice_button_text_xalign = 0.5

define gui.choice_button_text_idle_color = '#707070'

define gui.choice_button_text_hover_color = '#FFFFFF'

define gui.choice_button_text_insensitive_color = '#7070707f'


################################################################################
## Кнопки слотов
################################################################################

define gui.slot_button_width = 414

define gui.slot_button_height = 309

define gui.slot_button_borders = Borders(15, 15, 15, 15)

define gui.slot_button_text_size = 21

define gui.slot_button_text_xalign = 0.5

define gui.slot_button_text_idle_color = gui.idle_small_color

define gui.slot_button_text_selected_idle_color = gui.selected_color

define gui.slot_button_text_selected_hover_color = gui.hover_color


################################################################################
## Миниатюры
################################################################################

define config.thumbnail_width = 384
define config.thumbnail_height = 216


################################################################################
## Количество колонок и рядов
################################################################################

define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


################################################################################
## Позиционирование и интервалы
################################################################################

define gui.navigation_xpos = 60

define gui.skip_ypos = 15

define gui.notify_ypos = 68

define gui.choice_spacing = 33

define gui.navigation_spacing = 6

define gui.pref_spacing = 15

define gui.pref_button_spacing = 0

define gui.page_spacing = 0

define gui.slot_spacing = 15

define gui.main_menu_text_xalign = 1.0


################################################################################
## Рамки
################################################################################

define gui.frame_borders = Borders(6, 6, 6, 6)

define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

define gui.skip_frame_borders = Borders(24, 8, 75, 8)

define gui.notify_frame_borders = Borders(24, 8, 60, 8)

define gui.frame_tile = False


################################################################################
## Панели, полосы прокрутки и ползунки
################################################################################

define gui.bar_size = 38

define gui.scrollbar_size = 18

define gui.slider_size = 38


define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False


define gui.bar_borders = Borders(6, 6, 6, 6)

define gui.scrollbar_borders = Borders(6, 6, 6, 6)

define gui.slider_borders = Borders(6, 6, 6, 6)


define gui.vbar_borders = Borders(6, 6, 6, 6)

define gui.vscrollbar_borders = Borders(6, 6, 6, 6)

define gui.vslider_borders = Borders(6, 6, 6, 6)


define gui.unscrollable = "hide"


################################################################################
## История
################################################################################

define config.history_length = 250

define gui.history_height = 210

define gui.history_spacing = 0


define gui.history_name_xpos = 233

define gui.history_name_ypos = 0

define gui.history_name_width = 233

define gui.history_name_xalign = 1.0


define gui.history_text_xpos = 255

define gui.history_text_ypos = 3

define gui.history_text_width = 1110

define gui.history_text_xalign = 0.0


################################################################################
## Режим NVL
################################################################################

define gui.nvl_borders = Borders(0, 15, 0, 30)

define gui.nvl_list_length = 6

define gui.nvl_height = 173

define gui.nvl_spacing = 15


define gui.nvl_name_xpos = 645

define gui.nvl_name_ypos = 0

define gui.nvl_name_width = 225

define gui.nvl_name_xalign = 1.0


define gui.nvl_text_xpos = 675

define gui.nvl_text_ypos = 12

define gui.nvl_text_width = 885

define gui.nvl_text_xalign = 0.0


define gui.nvl_thought_xpos = 360

define gui.nvl_thought_ypos = 0

define gui.nvl_thought_width = 1170

define gui.nvl_thought_xalign = 0.0


define gui.nvl_button_xpos = 675

define gui.nvl_button_xalign = 0.0


################################################################################
## Локализация
################################################################################

define gui.language = "unicode"


################################################################################
## Мобильные устройства
################################################################################

init python:

    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)


    @gui.variant
    def small():

        ## Размеры шрифтов.
        gui.text_size = 45

        gui.name_text_size = 54

        gui.notify_text_size = 38

        gui.interface_text_size = 45

        gui.button_text_size = 45

        gui.label_text_size = 51


        ## Текстовое окно.
        gui.textbox_height = 360

        gui.name_xpos = 120

        gui.dialogue_xpos = 135

        gui.dialogue_width = 370


        ## Ползунки.
        gui.slider_size = 54


        ## Кнопки выбора.
        gui.choice_button_width = 1860

        gui.choice_button_text_size = 45


        ## Интервалы.
        gui.navigation_spacing = 30

        gui.pref_button_spacing = 15


        ## История.
        gui.history_height = 285

        gui.history_text_width = 1035


        ## Быстрые кнопки.
        gui.quick_button_text_size = 30


        ## Слоты.
        gui.file_slot_cols = 2

        gui.file_slot_rows = 2


        ## NVL.
        gui.nvl_height = 255

        gui.nvl_name_width = 458

        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373

        gui.nvl_text_xpos = 518

        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860

        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860

        gui.nvl_button_xpos = 30