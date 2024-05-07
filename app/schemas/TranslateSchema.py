from pydantic import BaseModel

class TranslateBase(BaseModel):
    sl : str = "ko"
    tl : str = "en"
    text : str = "내 안의 불꽃들로 이 밤을 찬란히 밝히는 걸 지켜봐"

class TranslateCreate(TranslateBase):
    mt: str = "Watch me bring the fire and set the night alight"