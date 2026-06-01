import copy

from database.DAO import DAO

class Model:
    def __init__(self):
        self.lista_citta = [i["Localita"] for i in DAO.getCitta(self)]
        self.costo_minimo = float("inf")
        self.dizionario_meteo = {}



    def getUmiditaMedia(self, mese):

        lista = DAO.getSituazioneMese(self, mese)
        counter_ge = 0
        umidita_ge_tot = 0
        counter_mi = 0
        umidita_mi_tot = 0
        counter_to = 0
        umidita_to_tot = 0

        for situazione in lista:

            if situazione.Localita == "Genova":
                counter_ge += 1
                umidita_ge_tot += situazione.Umidita

            if situazione.Localita == "Milano":
                counter_mi += 1
                umidita_mi_tot += situazione.Umidita

            if situazione.Localita == "Torino":
                counter_to += 1
                umidita_to_tot += situazione.Umidita

        mediaGen = umidita_ge_tot / counter_ge
        mediaMil = umidita_mi_tot / counter_mi
        mediaTor = umidita_to_tot / counter_to

        return mediaGen, mediaMil, mediaTor

    def calcola_sequenza(self,mese):

        self.dati_meteo = DAO.getSituazione15giorni(self, mese)

        for situazione in self.dati_meteo:
            chiave = (situazione.Localita, situazione.Data.day)
            self.dizionario_meteo[chiave] = situazione

        self.costo_minimo = float("inf")
        self.sequenza_ottima = []

        self._ricorsione([])

        sequenza_oggetti = []

        for i in range(len(self.sequenza_ottima)):
            citta = self.sequenza_ottima[i]
            giorno = i + 1
            oggetto_reale = self.dizionario_meteo[(citta, giorno)]
            sequenza_oggetti.append(oggetto_reale)

            # Restituisco al Controller la lista degli OGGETTI, non delle stringhe!
        return sequenza_oggetti, self.costo_minimo

    def _ricorsione(self, parziale: list):

        if len(parziale) == 15:
            costo_attuale = self._calcola_costo(parziale)

            if costo_attuale < self.costo_minimo:
                self.costo_minimo = costo_attuale
                self.sequenza_ottima = copy.deepcopy(parziale)


        else:
            for citta in self.lista_citta:
                parziale.append(citta)

                if self._is_valida(parziale):
                    self._ricorsione(parziale)

                parziale.pop()


    def _is_valida(self, parziale):

        ultima = parziale[-1]
        contatore = 0

        for i in parziale:
            if i == ultima:
                contatore += 1

        if contatore > 6:
            return False

        if len(parziale) == 1:
            return True

        if len(parziale) <= 3:

            if len(parziale) == 3:
                return parziale[2] == parziale[1] == parziale[0]

            if len(parziale) == 2:
                return parziale[1] == parziale[0]

        if len(parziale) >3:
            ieri = parziale[-2]
            oggi = parziale[-1]

            if oggi != ieri:
                due_giorni_fa = parziale[-3]
                tre_giorni_fa = parziale[-4]

                if (ieri == due_giorni_fa == tre_giorni_fa) is False:
                    return False

        return True

    def _calcola_costo(self, parziale):

        contatore = 0

        for i in range(len(parziale)):
            citta_attuale = parziale[i]
            giorno_attuale = i + 1

            contatore += self.dizionario_meteo[(citta_attuale, giorno_attuale)].Umidita

        return contatore
