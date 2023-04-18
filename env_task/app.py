from flask import Flask
import asyncio
import os

app = Flask(__name__)

@app.route('/')
async def async_route():
    # Perform some asynchronous task
    result = await async_task()
    
    # Return the result
    return f'The result is: {result}'

async def async_task():
    # Simulate an asynchronous task
    await asyncio.sleep(2)
    
    # Return a result
    return 'Hello, world!'


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3080))
    app.run(host='0.0.0.0' ,port =port)