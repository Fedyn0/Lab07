import flet as ft

from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        # other attributes
        self._mese = 0

    def handle_umidita_media(self, e):
        self._view.lst_result.controls.clear()

        if not self._view.dd_mese.value:
            self._view.create_alert("Selezionare il mese")
            self._view.update_page()
            return

        mese = self._view.dd_mese.value

        mediaGe, mediaMi, mediaTo = self._model.getUmiditaMedia(mese)

        self._view.lst_result.controls.append(ft.Text(
            f"L'umidità media nel mese selezionato è: \n"
            f"Genova: {mediaGe:.4f}\n"
            f"Milano: {mediaMi:.4f}\n"
            f"Torino: {mediaTo:.4f}\n"
        ))
        self._view.update_page()

    def handle_sequenza(self, e):
        self._view.lst_result.controls.clear()

        if not self._view.dd_mese.value:
            self._view.create_alert("Selezionare il mese")
            self._view.update_page()
            return

        mese = self._view.dd_mese.value

        sequenza, costo = self._model.calcola_sequenza(mese)

        self._view.lst_result.controls.append(ft.Text(f"La sequenza ottima ha costo di {costo} ed è:\n"
                                                      f"{sequenza}"))
        self._view.update_page()


    def read_mese(self, e):
        self._mese = int(e.control.value)
        print(int(e.control.value))

