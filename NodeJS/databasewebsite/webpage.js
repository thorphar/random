var express=require('express');
var app=express();
app.set('view engine','jade');
app.get('/',function(req,res)
{
    let date_ob = new Date();
res.render('index',
{title:'Guru99',message:date_ob})
});
var server=app.listen(3000,function() {});