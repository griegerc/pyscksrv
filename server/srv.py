import asyncio
import websockets

async def server(websocket, path):
    while True:
        message = await websocket.recv()
        print(f"Received message: {message}")
        await websocket.send(f"Your message: {message}")

start_server = websockets.serve(server, "0.0.0.0", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()