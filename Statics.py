from email.mime.text import MIMEText;

link = "http://www.ontarioimmigration.ca/en/pnp/OI_PNPNEW.html";
oldFP = ".\\OldWebpage.bin";
jsonFP = ".\\users.json";
adminEmail = "harveersingh08@gmail.com";
bodyMsg = MIMEText(u"To visit the webpage, <a href='%s'>Click here</a>" %(link),"html");
