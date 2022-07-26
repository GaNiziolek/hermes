import sqlite3

class hermesDB():
    def __init__(self):

        db_path = 'hermes.db'

        print(f'Conectando ao banco "{db_path}"...', end='')

        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # tgpslog
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tgpslog (
                id_gps INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                sync INTEGER DEFAULT 0 NOT NULL,
                mode INTEGER NOT NULL,
                satellites INTEGER NOT NULL,
                latitude REAL,
                longitude REAL,
                track REAL,
                hspeed REAL,
                sat_time TEXT,
                error TEXT,
                altitude REAL,
                climb REAL,
                rasp_time TEXT NOT NULL
            );
        """)

        self.conn.commit()

        print(' Sucesso!')
    
    def inserir_posicao(
            self, time, mode, sats,
            lat=None,
            lon=None,
            alt=None,
            hspeed=None,
            track=None,
            climb=None,
            sat_time=None,
            error=None
        ):

        self.cursor.execute(
            """
                INSERT INTO tgpslog
                      (rasp_time, mode, satellites, latitude, longitude, altitude, hspeed, track, climb, sat_time, error)
                VALUES(?,         ?,    ?,          ?,        ?,         ?,        ?,      ?,     ?,     ?,        ?);
            """,
            (time, mode, sats, lat, lon, alt, hspeed, track, climb, sat_time, error)
        )

        self.conn.commit()
    


if __name__ == '__main__':
    db = hermesDB()
    



    
