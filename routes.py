from fastapi import APIRouter
from api import YacineTV

ytv = YacineTV()
router = APIRouter(tags=["YacineTV"])


@router.get("/categories")
def categories():
    return ytv.get_categories()


@router.get("/categories/<int:category_id>")
def category(category_id):
    return ytv.get_category(category_id)

@router.get("/categories/<int:category_id>/channels")
def channels(category_id):
    return ytv.get_category_channels(category_id)

@router.get("/channel/<int:channel_id>")
def channel(channel_id):
    return ytv.get_channel(channel_id)
