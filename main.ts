input.onButtonPressed(Button.A, function () {
    lang = lang + 1
    if (lang > 2) {
        lang = 0
    }
    if (lang == 0) {
        basic.showString("K")
    }
    if (lang == 1) {
        basic.showString("M")
    }
    if (lang == 2) {
        basic.showString("N")
    }
})
input.onGesture(Gesture.TiltLeft, function () {
    kvoc = kvoc - 1
    if (kvoc < 0) {
        kvoc = klist.length - 1
    }
    basic.showString("" + (elist[kvoc]))
})
input.onButtonPressed(Button.AB, function () {
    kvoc = randint(0, klist.length - 1)
    mvoc = randint(0, mlist.length - 1)
})
input.onButtonPressed(Button.B, function () {
    if (lang == 0) {
        basic.showString("" + (klist[kvoc]))
    }
    if (lang == 1) {
        basic.showString("" + (mlist[kvoc]))
    }
    if (lang == 2) {
        basic.showString("" + (nlist[kvoc]))
    }
    basic.showString(" / " + elist[kvoc])
})
input.onGesture(Gesture.Shake, function () {
    basic.showString("nuqneH!")
    lang = 0
    kvoc = 0
})
input.onGesture(Gesture.TiltRight, function () {
    kvoc = kvoc + 1
    if (kvoc == klist.length) {
        kvoc = 0
    }
    basic.showString("" + (elist[kvoc]))
})
let elist: string[] = []
let klist: string[] = []
let mlist: string[] = []
let nlist: string[] = []
let mvoc = 0
let kvoc = 0
let lang = 0
lang = 2
kvoc = 0
mvoc = 0
nlist = ["yawne", "kaltxi", "tawsip", "'eylan", "kelku", "safla", "tiyora'", "'itan", "'ite", "'ipu", "uvan", "syure", "yom"]
mlist = ["cyare", "Sucuy'gar", "me'sen", "burc'ya", "yaim", "bralov", "parjai", "ad", "ad", "nuh'la", "geroya", "kai'tome", "epar"]
klist = ["bang", "nuqneH", "'ejDo'", "jup ", "juH", "Qapla'", "yay", "puqloD", "puqbe'", "tlhaq", "Quj", "Soj", "Sop"]
elist = ["beloved", "hello", "starship", "friend", "home", "success", "victory", "son", "daughter", "funny", "game", "food", "eat"]
