from typing import Any, Dict, Optional
from pydantic import BaseModel



class ScenesBaseVM(BaseModel):
    strategy_name : str  #//ind
    start_date : str #back
    end_date : str #back
    params :Dict[str, int]
    start_cash : float
    commission : float
   
   
   
 
   
class ScenesCreateVM(ScenesBaseVM):
    pass

class ScenesVM(ScenesBaseVM):
    id: int
   

class Config:
    orm_mode = True


