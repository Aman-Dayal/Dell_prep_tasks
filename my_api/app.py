from flask import Flask ,redirect
import motor.motor_asyncio


app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/my_api')


@app.route('/my_api')
async def my_api():
    
    user1 = {}
    user1['Name'] = str(input("Enter your name: "))
    user1['Phone no.'] = int(input("Enter your number: "))
    user1['_id'] = input('Enter an id: ')
    await myfnc(user1) 
    return user1



async def myfnc(user):
    
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/")
    db = client.get_database("my_api")
    coll = db.get_collection('ist')
    await coll.insert_one(user)
  

if __name__ == '__main__':
    app.run(debug=True , port= 9000)
