from fastapi import APIRouter, Depends,  HTTPException,  status
from sqlalchemy.orm import Session
from  utils.database_connection import get_db as session
from controllers  import article_controller


import view_models.scenes_vm as scenes_vm


router = APIRouter(
    prefix="/scenes",
    tags=["scenes"],
    responses={404: {"description": "Not found"}},
)





@router.get("/", response_model=list[scenes_vm.ScenesVM])
def get_data(skip: int = 0, limit: int = 100,db: Session = Depends(session)):
    try:
        db_user = article_controller.get_data(db, skip, limit)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    
@router.post("/", response_model=scenes_vm.ScenesVM)
def create_data(data: scenes_vm.ScenesCreateVM, db: Session = Depends(session)):
    try:
        db_user = article_controller.create_data(db, data=data)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
