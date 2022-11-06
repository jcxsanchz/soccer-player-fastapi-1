import fastapi
from fastapi import status, HTTPException, Response
from SQL import create_players_table
from SQL.create_players_table import cursor, conn
from models.player import Player

router = fastapi.APIRouter()


create_players_table.create_table()


# path operation or route. route path
@router.get('/')
def root():
    return {"message": "Welcome to Soccer Manager!"}


@router.get('/players')
def get_players():
    cursor.execute("""SELECT * FROM players""")
    players = cursor.fetchall()
    return {"data": players}


@router.post('/players', status_code=status.HTTP_201_CREATED)
def add_player(player: Player):
    cursor.execute("""INSERT INTO players (player_name, player_age, player_nationality, player_rating)
    VALUES (%s, %s, %s, %s) RETURNING *
    """, (player.player_name, player.player_age, player.player_nationality, player.player_rating))
    new_player_dict = player.dict()
    conn.commit()
    return {"data": new_player_dict}


# id path parameter will allow user to see specific player. id must be converted to list for it to work
@router.get('/players/{id}')
def get_player(id: int):
    cursor.execute("""SELECT * FROM players WHERE player_id=%s""", [id])
    found_player = cursor.fetchone()
    if not found_player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id {id} was not found")
    return {"player detail": found_player}


@router.delete('/players/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_player(id: int):
    cursor.execute("""DELETE FROM players WHERE player_id=%s RETURNING *""", [id])
    deleted_player = cursor.fetchone()
    conn.commit()

    if deleted_player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id: {id} does not exist.")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/players/{id}')
def update_player(id: int, player: Player):
    cursor.execute("""UPDATE players SET player_name=%s, player_age=%s, player_nationality=%s, player_rating=%s WHERE 
    player_id=%s RETURNING *""",
                   (player.player_name, player.player_age, player.player_nationality, player.player_rating, id))

    player_to_update = cursor.fetchone()
    conn.commit()

    if player_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id: {id} does not exist.")

    return {"data": player_to_update}