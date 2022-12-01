import fastapi
from fastapi import status, HTTPException, Response, Depends
from typing import List
import models.table
import oauth2
from api.database import get_db
from models.schemas import CreatePlayer, PlayerResponse
from sqlalchemy.orm import Session

router = fastapi.APIRouter(
    prefix='/players',
    tags=['Players']
)


@router.get('/', response_model=List[PlayerResponse])
def get_players(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM players""")
    # players = cursor.fetchall()
    players = db.query(models.table.Player).filter(models.table.Player.player_id == current_user.user_id).all()
    return players


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PlayerResponse)
def add_player(player: CreatePlayer, db: Session = Depends(get_db),
               current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO players (player_name, player_age, player_nationality, player_rating)
    # VALUES (%s, %s, %s, %s) RETURNING *
    # """, (player.player_name, player.player_age, player.player_nationality, player.player_rating))
    # new_player_dict = player.dict()
    # conn.commit()

    new_player_dict = models.table.Player(owner_id=current_user.user_id, **player.dict())
    db.add(new_player_dict)
    db.commit()
    db.refresh(new_player_dict)
    return new_player_dict


# id path parameter will allow user to see specific player. id must be converted to list for it to work
@router.get('/{id}', response_model=PlayerResponse)
def get_player(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""SELECT * FROM players WHERE player_id=%s""", [id])
    # found_player = cursor.fetchone()

    found_player = db.query(models.table.Player).filter(models.table.Player.player_id == id).first()

    if not found_player:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id {id} was not found")
    return found_player


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_player(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM players WHERE player_id=%s RETURNING *""", [id])
    # deleted_player = cursor.fetchone()
    # conn.commit()

    deleted_player_query = db.query(models.table.Player).filter(models.table.Player.player_id == id)

    deleted_player = deleted_player_query.first()

    if deleted_player == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id: {id} does not exist.")

    if deleted_player.owner_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    deleted_player_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=PlayerResponse)
def update_player(id: int, player: CreatePlayer, db: Session = Depends(get_db),
                  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE players SET player_name=%s, player_age=%s, player_nationality=%s, player_rating=%s WHERE
    # player_id=%s RETURNING *""",
    #                (player.player_name, player.player_age, player.player_nationality, player.player_rating, id))
    #
    # player_to_update = cursor.fetchone()
    # conn.commit()
    player_query = db.query(models.table.Player).filter(models.table.Player.player_id == id)

    player_to_update = player_query.first()

    if player_to_update is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"player with id: {id} does not exist.")

    if player_to_update.owner_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")

    player_query.update(player.dict(), synchronize_session=False)

    db.commit()

    return player_query.first()
