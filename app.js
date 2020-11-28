const 
    fs = require('fs')
    cron = require('node-cron'),
    {exec} = require('child_process'),
    {Client,MessageAttachment} = require("discord.js"),
    client = new Client(),
client.login('NjU1MDI5MzY4NjUzMDg2NzUw.XkVtkw.Bc_6Wbo_6ns52TZtR5E9DppuFXE')
let channel
client.on('ready',()=>{
    const channel = client.channels.resolve('731738012098101308'),
        command = 'sqlite3 database.sqlite3 ".backup backup-database.sqlite3"';
    
    exec(command);

    channel.send(new MessageAttachment("./backup-database.sqlite3"));
    fs.copyFile('./backup-database.sqlite3',`./backups/database-${new Date().toDateString()}.sqlite3`,()=>{});

    cron.schedule("0 */12 * * *", function() {
        exec(command,(err,stdout,stderr)=>{
            if(err || stderr){
                channel.send(err)
            }else{
                channel.send(new MessageAttachment("./backup-database.sqlite3"))
                fs.copyFile('./backup-database.sqlite3',`./backups/database-${new Date().toDateString()}.sqlite3`,()=>{})
            }
        })
    });
})

