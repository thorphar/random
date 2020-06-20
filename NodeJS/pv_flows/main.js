const electron = require('electron');
const url = require('url');
const path = require('path');


const {app, BrowserWindow,Menu} = electron;
let mainWindow;


app.on('ready', function(){
    mainWindow = new BrowserWindow({});
    mainWindow.setSize(400,600);
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'mainWindow.html'),
        protocol:'file:',
        slashes:true
    }))
    const mainMenu = Menu.buildFromTemplate(mainMenuTemplate);
    Menu.setApplicationMenu(null);//(mainMenu);
});


const mainMenuTemplate = [
    {
        label:'File'
    }
];

if(process.platform.NODE_ENV !== 'prodcution'){
    mainMenuTemplate.push({
        label: 'Development Tools',
        submenu:[{
            label: 'Toggle Developer Tools',
            click(item,focusedWindow){
                focusedWindow.toggleDevTools();
            }
        }]
    });
}