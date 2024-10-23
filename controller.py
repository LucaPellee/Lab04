import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view
        self._lingua = None
        self._ricerca = None

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")

    def _leggiTendinaLingua(self, e):
        self._lingua = self._view._dd_lingua.value
        self._view._lvOut.controls.append(ft.Text("Lingua impostato correttamente", color="green"))
        self._view.update()
        time.sleep(1)
        self._view._lvOut.controls.clear()
        self._view.update()

    def _leggiTendinaRicerca(self, e):
        self._ricerca = self._view._dd_ricerca.value
        self._view._lvOut.controls.append(ft.Text("Metodo impostato correttamente", color = "green"))
        self._view.update()
        time.sleep(1)
        self._view._lvOut.controls.clear()
        self._view.update()

    def _handleSpellCheck(self, e):
        self._view._lvOut.controls.clear()
        testo = self._view._tf_testo.value
        self._view._tf_testo.value = ""
        if testo == "":
            self._view._lvOut.controls.append(ft.Text("Testo mancante", color = "red"))
        if self._lingua is None:
            self._view._lvOut.controls.append(ft.Text("Selezionare la lingua desiderata", color = "red"))
        if self._ricerca is None:
            self._view._lvOut.controls.append(ft.Text("Selezionare la ricerca desiderata", color = "red"))

        self._view._lvOut.controls.append(ft.Text(f"La frase inserita è: {testo}"))
        par_err = self.handleSentence(testo, self._lingua, self._ricerca)[0]
        tempo = self.handleSentence(testo, self._lingua, self._ricerca)[1]
        self._view._lvOut.controls.append(ft.Text(f"Le parole errate sono: {par_err}"))
        self._view._lvOut.controls.append(ft.Text(f"Il tempo necessario è stato {tempo}"))
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text

