import gpsd
import requests
import os
import datetime

from hermesDB import hermesDB

API_URL = os.getenv('HERMES_LOGGER_URL')

def main():
    # Conecta ao socket do GPSD
    gpsd.connect()
    pos = gpsd.get_current()

    # Abre a conexão com banco
    db = hermesDB()
    
    # Coleta os dados
    time = str(datetime.datetime.now().replace(microsecond=0))
    mode = pos.mode
    sats = pos.sats

    lat = lon = alt = climb = hspeed = track = sat_time = None

    error=None

    if mode >= 2:
        lat      = pos.lat
        lon      = pos.lon
        hspeed   = pos.hspeed
        track    = pos.track
        sat_time = pos.get_time(local_time=True)
        error    = str(pos.error)

    if mode >= 3:
        alt   = pos.alt
        climb = pos.climb
        
    print(f'Modo: {mode}')

    db.inserir_posicao(
        time = time,
        mode = mode,
        sats = sats,
        lat  = lat,
        lon  = lon,
        alt  = alt,
        hspeed = hspeed,
        track  = track,
        climb  = climb,
        sat_time = sat_time,
        error    = error
    )

    db.cursor.execute("""
        SELECT * FROM tgpslog
    """)

    for linha in db.cursor.fetchall():
        print(linha)
    

if __name__ == "__main__":
    main()