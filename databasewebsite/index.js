const {Client} = require('pg')
const express = require('express')
const app = express()
const port = 3000
const client = new Client({
    user: "pguser",
    password: "password",
    host: "127.0.0.1",
    port: 5432,
    database: "tools"
})



async function execute() {
    try{
    await client.connect()
    console.log("Connected successfully.")

    var {rows} = await client.query("select to_regclass('users')")
    if (!rows[0].to_regclass){
        console.log("Table does not exist")
    }

    var {rows} = await client.query("insert into users (username) values ('sheiya');")
    console.log(rows);
    }
    catch (ex)
    {
        console.log(`Something wrong happend ${ex}`)
    }
    finally 
    {
        await client.end()
        console.log("Client disconnected successfully.")    
    }
    return rows;
}


app.get('/', function(req,res){
    var rows = execute();
    res.send (`Hello World! ${rows[1]}`)
    }
)

app.listen(port, () =>console.log(`Server listening on http://localhost ${port}`))