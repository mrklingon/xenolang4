def on_button_pressed_a():
    global lang
    lang = lang + 1
    if lang > 2:
        lang = 0
    if lang == 0:
        basic.show_string("K")
    if lang == 1:
        basic.show_string("M")
    if lang == 2:
        basic.show_string("N")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    global kvoc
    kvoc = kvoc - 1
    if kvoc < 0:
        kvoc = len(klist) - 1
    basic.show_string("" + (elist[kvoc]))
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_button_pressed_ab():
    global kvoc, mvoc
    kvoc = randint(0, len(klist) - 1)
    mvoc = randint(0, len(mlist) - 1)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if lang == 0:
        basic.show_string("" + (klist[kvoc]))
    if lang == 1:
        basic.show_string("" + (mlist[kvoc]))
    if lang == 2:
        basic.show_string("" + (nlist[kvoc]))
    basic.show_string(" / " + elist[kvoc])
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    global lang, kvoc
    basic.show_string("nuqneH!")
    lang = 0
    kvoc = 0
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    global kvoc
    kvoc = kvoc + 1
    if kvoc == len(klist):
        kvoc = 0
    basic.show_string("" + (elist[kvoc]))
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

elist: List[str] = []
klist: List[str] = []
mlist: List[str] = []
nlist: List[str] = []
mvoc = 0
kvoc = 0
lang = 0
lang = 2
kvoc = 0
mvoc = 0
nlist = ["yawne",
    "kaltxi",
    "tawsip",
    "'eylan",
    "kelku",
    "safla",
    "tiyora'",
    "'itan",
    "'ite",
    "'ipu",
    "uvan",
    "syure",
    "yom"]
mlist = ["cyare",
    "Sucuy'gar",
    "me'sen",
    "burc'ya",
    "yaim",
    "bralov",
    "parjai",
    "ad",
    "ad",
    "nuh'la",
    "geroya",
    "kai'tome",
    "epar"]
klist = ["bang",
    "nuqneH",
    "'ejDo'",
    "jup ",
    "juH",
    "Qapla'",
    "yay",
    "puqloD",
    "puqbe'",
    "tlhaq",
    "Quj",
    "Soj",
    "Sop"]
elist = ["beloved",
    "hello",
    "starship",
    "friend",
    "home",
    "success",
    "victory",
    "son",
    "daughter",
    "funny",
    "game",
    "food",
    "eat"]