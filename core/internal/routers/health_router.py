from fastapi import APIRouter

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health_check():
    """
    Simple health check endpoint.
    Returns a JSON response with a single key "status" and value "ok".
    """
    return {"status": "ok"}
