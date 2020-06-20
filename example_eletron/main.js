const electron = require('electron');
const url = require('url');
const path = require('path');


const {app, BrowserWindow,Menu} = electron;
let mainWindow;


app.on('ready', function(){
    mainWindow = new BrowserWindow({});
    mainWindow.setSize(400,600);
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'index.html'),
        protocol:'file:',
        slashes:true
    }))
    Menu.setApplicationMenu(null);//(mainMenu);
});
