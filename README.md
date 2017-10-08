H'okay so:

This is a twitter retweet bot hosted on a Raspberry Pi 3 made with Python 2.7. It retweets keywords continually 5 tweets/every 2 minutes.


To create one like it:

Create a new twitter account with a new phonenumber. (You can get a free one with google voice with any gmail account.)

Register your account as an app (via https://apps.twitter.com/app/new).
Get its access keys.

Create a file: 

touch credentials.py 

and input your access key info as variables (there should be 4).

If you want to continually tweet, you have to host your code from a computer that is always on. 
For me this meant using my Raspberry Pi 3.

Make a github repository of your code. 
Get a public SSH key from your pi and post it to your repository on GitHub (We do this to let the raspi and github communicate).
Navigate to the Python directory and create a new directory on your pi and clone your github repository to it.
Also make a duplicate of the credentials.py file.
To easily execute my code, I made a shell script that pulls from the latests version of my git repository. So in my directory that I just made on the pi, I created a file run.sh and here is what I put:

   #!/bin/bash

  # replace "retweetbot" with your repository name
  cd ~/Python/NewDirYouCreated/retweetbot

  # get the latest version from the remote Git repository
  git reset --hard
  git pull origin

  # run your bot
  python ./retweetbot.py
  
At this point you should do an execute test of this .sh file to make sure it's tweeting what you want it to and it's coming from your pi.
  
Now I wanted it to retweet continually. In my bot code, I set 5 retweets every time the code is executed.
I arbitrarily decided I would like to execute my code every 2 minutes so that my bot retweets the 5 newest tweets of my search query every 2 minutes.
  
To retweet continually I made a cron job. You can tweek your cron job to do a bunch of specific things, but for my purpose, I wanted a straightforward task.
From terminal on my pi I typed crontab -e
If you have never created a cron job it will ask you how you want to set up your default. I set mine to nano.
  
Below the hashed out comments, this is what your cron job should look like,
  
  */2 * * * * /home/pi/Python/NewDirYouCreated/run.sh
  
'*/2 * * * *' is the time of the cronjob scheduled and '/home/pi/Python/NewDirYouCreated/run.sh' is the file you wish to execute when scheduled. You can google how to write your own specific cron job schedule.
  
Press control x to exit, y to save.
If the cron job saved correctlyl, it will print "creating new cronjob" below your contab -e command 
Just to double check, type crontab -l and it will show you what cronjobs are scheduled. 
Now check your bot and make sure its working!
 
 
