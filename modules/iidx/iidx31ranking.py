import config

from fastapi import APIRouter, Request, Response

from core_common import core_process_request, core_prepare_response, E

router = APIRouter(prefix="/local2", tags=["local2"])
router.model_whitelist = ["LDJ"]


@router.post("/{gameinfo}/IIDX31ranking/getranker")
async def iidx31ranking_getranker(request: Request):
    request_info = await core_process_request(request)

    response = E.response(E.IIDX31ranking())

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
