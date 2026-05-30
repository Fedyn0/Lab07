from database.DB_connect import DBConnect
from model.situazione import Situazione


class DAO():

    @staticmethod
    def getSituazioneMese(self, mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ 
        select Localita, `Data`, Umidita  
        from situazione s 
        where month(`Data`) = %s
        """

        cursor.execute(query, (mese,))

        res = []
        for row in cursor:
            res.append(Situazione(**row))


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getSituazione15giorni(self, mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ 
        select Localita, `Data`, Umidita  
        from situazione s 
        where month(`Data`) = %s
        and day(`Data`) >= 1
        and day(`Data`) <= 15
        """

        cursor.execute(query, (mese,))

        res = []
        for row in cursor:
            res.append(Situazione(**row))


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getCitta(self):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ 
        select distinct Localita
        from situazione s 
        """

        cursor.execute(query,)

        res = []
        for row in cursor:
            res.append(row)



        cursor.close()
        cnx.close()
        return res
