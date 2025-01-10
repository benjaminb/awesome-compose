from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/healthcheck")
async def healthcheck():
    return {
        'statusCode': 200,
        'body': json.dumps('Alive')
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)