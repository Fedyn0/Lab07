from database.DB_connect import DBConnect
from model.situazione import Situazione


class DAO():

    @staticmethod
    def getSituazione(self, mese):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """ 
        select Localita, `Data`, Umidita  
        from situazione s 
        where month(`Data`) = %s
        """

        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Situazione(**row))

        res.sort()
        cursor.close()
        cnx.close()
        return res