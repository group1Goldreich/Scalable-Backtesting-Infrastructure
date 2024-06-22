from fastapi import APIRouter, Depends,  HTTPException,  status
from sqlalchemy.orm import Session
from ..utils.database_connection import get_db as session
from ..controllers  import backtest_controller


from ..view_models.scenes_vm import ScenesBaseVM


router = APIRouter(
    prefix="/scenes",
    tags=["scenes"],
    responses={404: {"description": "Not found"}},
)


    
@router.post("/backtest", response_model=ScenesBaseVM)
def create_data(data: ScenesBaseVM, db: Session = Depends(session)):
    try:
        db_user = backtest_controller.backtest(db, data=data)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
