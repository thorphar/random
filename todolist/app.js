const express = require('express')
const bodyParser = require('body-parser')
const date = require(__dirname+"/date.js")
const app = express()
app.set('view engine', 'ejs');
app.use(bodyParser.urlencoded({extended: true}));
app.use(express.static("public"));

let items = [];
let workitems = [];

app.get('/',function(req,res){
    let day = date.getDate();
    res.render('list',{pageTitle:day,newListItems:items})
});

app.post('/',function(req,res){
    let item = req.body.newItem;
    if(req.body.list === "Work"){
        workitems.push(item);
        res.redirect("/work");
    }
    else{
    items.push(item);
    res.redirect("/");
    }
    
})


app.get('/work',function(req,res){
    res.render('list',{pageTitle:"Work List - Sheiya",newListItems:workitems})
})

app.get('/about',function(req,res){
    res.render('about',{pageTitle:"About"})
})

app.listen(3000,function(){
    console.log("Server listening on 3000"); 
});