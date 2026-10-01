from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio
from simulator import DeviceFleet
from anomaly import analyze_device

app = FastAPI(title="EdgePulse")
app.mount("/static", StaticFiles(directory="static"), name="static")
fleet = DeviceFleet()

@app.get("/", response_class=HTMLResponse)
async def index():
    return HTMLResponse(open("static/index.html", encoding="utf-8").read())

@app.get("/api/devices")
async def devices():
    return fleet.snapshot()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        payload = fleet.tick()
        for device in fleet.devices:
            analyze_device(device)
        await websocket.send_json(payload)
        await asyncio.sleep(1)
