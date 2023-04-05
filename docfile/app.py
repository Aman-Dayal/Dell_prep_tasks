from flask import Flask
import asyncio

app = Flask(__name__)

@app.route('/')
async def async_route():
    # Perform some asynchronous task
    result = await async_task()
    
    # Return the result
    return f'The result is: {result}'

async def async_task():
    # Simulate an asynchronous task
    await asyncio.sleep(5)
    
    # Return a result
    return 'Hello, world!'


if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True)