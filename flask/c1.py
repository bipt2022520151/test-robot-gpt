from typing import Optional
from fastapi import APIRouter, Query, Path

fastapi_router = APIRouter()


@fastapi_router.get(path="/")
async def read_root():
    return {"Hello": "World"}


@fastapi_router.get(path="/items/{my_item_id}",
                    summary='路径测试',
                    description='路径测试',
                    tags=['测试模块'],
                    response_description='{"my_item_id": my_item_id, "q": q}')
async def read_item(my_item_id: int = Path(..., description="我的item id"),
                    q: Optional[str] = Query(..., description="查询参数")):
    return {"my_item_id": my_item_id, "q": q}





