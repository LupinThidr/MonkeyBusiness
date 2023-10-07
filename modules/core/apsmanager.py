from fastapi import APIRouter, Request, Response

from core_common import core_process_request, core_prepare_response, E

router = APIRouter(prefix="/core", tags=["apsmanager"])


@router.post("/{gameinfo}/apsmanager/getstat")
async def apsmanager_getstat(request: Request):
    request_info = await core_process_request(request)

    response = E.response(E.apsmanager(expire=600))

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
