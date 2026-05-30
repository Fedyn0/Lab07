from database.DAO import DAO

class Model:
    def __init__(self):
        pass

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





