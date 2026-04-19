from fastapi import APIRouter,UploadFile,File
from typing import List
from modules.load_vectorstore import load_vectorestore
from fastapi.responses import JSONResponse
from logger import logger

router=APIRouter()

@router.post("/upload_pdfs/")
async def upload_pdfs(files:List[UploadFile]=File(...)):
    try:
        logger.info("Recieved uploaded files")
        load_vectorestore(files)
        logger.info("Document added to Vector Store")
        return {"message":"Files Processed and Vector Store Updated"}
    
    except Exception as e:
        logger.exception("Error tuning PDF Upload")
        return JSONResponse(status_code=500,content={"error":str(e)})
